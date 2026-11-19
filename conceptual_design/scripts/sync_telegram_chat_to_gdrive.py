#!/usr/bin/env python3
"""
sync_telegram_chat_to_gdrive.py

Uploads Telegram export media files (photos, files, stickers, symlinks) to Google Drive,
and updates result.json so all media references point to permanent Google Drive links.

Usage:
    python3 conceptual_design/scripts/sync_telegram_chat_to_gdrive.py [OPTIONS]

Options:
    --json-path PATH     Path to result.json (default: automatically finds latest TelegramChatExport_*/result.json)
    --parent-id ID       Google Drive parent folder ID (default: 14NvPYoT-LM24Uoo7vRZ7wAFq0xyyYRCJ - telegram_chat_media)
    --cache-path PATH    Path to cache file (default: conceptual_design/scripts/telegram_media_cache.json)
    --workers N          Number of concurrent upload threads (default: 4)
    --delete-local       Delete local media folders (files, photos, stickers) after upload & verification
    --dry-run            Simulate execution without modifying anything
"""

import argparse
import glob
import json
import os
import re
import shutil
import subprocess
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

DEFAULT_PARENT_ID = "14NvPYoT-LM24Uoo7vRZ7wAFq0xyyYRCJ"
DEFAULT_CACHE_PATH = "conceptual_design/scripts/telegram_media_cache.json"

cache_lock = threading.Lock()


def find_default_json_path() -> str:
    """Finds the most recent TelegramChatExport result.json or falls back to known default."""
    candidates = sorted(glob.glob("conceptual_design/archive/raw_logs/TelegramChatExport_*/result.json"), reverse=True)
    if candidates:
        return candidates[0]
    return "conceptual_design/archive/raw_logs/TelegramChatExport_2026-11-19/result.json"


def load_drive_existing_files(parent_id: str) -> dict:
    """Fetch existing files in the Drive folder via 'gdrive readonly ls <parent_id> --max 0 --json'."""
    cmd = ["gdrive", "readonly", "ls", parent_id, "--max", "0", "--json"]
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, check=True)
        items = json.loads(res.stdout)
        # Mapping: filename -> id
        return {item["name"]: item["id"] for item in items if "name" in item and "id" in item}
    except Exception as e:
        print(f"[WARN] Could not query Drive folder items: {e}")
        return {}


def upload_single_file(file_path: str, parent_id: str, max_retries: int = 3) -> str:
    """Uploads a file (or resolved symlink) to Google Drive and returns the file ID."""
    # Resolve symlinks to target real path
    real_path = os.path.realpath(file_path)
    filename = os.path.basename(file_path)

    if not os.path.exists(real_path):
        raise FileNotFoundError(f"Source file does not exist: {file_path} -> {real_path}")

    cmd = ["gdrive", "mutate", "upload", real_path, "--parent", parent_id]

    for attempt in range(1, max_retries + 1):
        try:
            res = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
            if res.returncode == 0:
                match = re.search(r"\(ID:\s*([a-zA-Z0-9_-]+)\)", res.stdout)
                if match:
                    return match.group(1)
                else:
                    raise RuntimeError(f"Could not parse file ID from output: {res.stdout.strip()}")
            else:
                err_msg = res.stderr.strip() or res.stdout.strip()
                print(f"[RETRY {attempt}/{max_retries}] Upload failed for {filename}: {err_msg}")
        except subprocess.TimeoutExpired:
            print(f"[RETRY {attempt}/{max_retries}] Upload timed out for {filename}")
        except Exception as e:
            print(f"[RETRY {attempt}/{max_retries}] Exception uploading {filename}: {e}")

        if attempt < max_retries:
            time.sleep(2 * attempt)

    raise RuntimeError(f"Failed to upload {filename} after {max_retries} attempts.")


def build_drive_url(file_id: str) -> str:
    return f"https://drive.google.com/file/d/{file_id}/view?usp=drivesdk"


def main():
    parser = argparse.ArgumentParser(description="Sync Telegram media to Google Drive and update result.json")
    parser.add_argument("--json-path", default=None, help="Path to result.json (defaults to latest export)")
    parser.add_argument("--parent-id", default=DEFAULT_PARENT_ID, help="Google Drive folder ID")
    parser.add_argument("--cache-path", default=DEFAULT_CACHE_PATH, help="Path to upload cache file")
    parser.add_argument("--workers", type=int, default=4, help="Concurrent upload threads")
    parser.add_argument("--delete-local", action="store_true", help="Delete local media folders after completion")
    parser.add_argument("--dry-run", action="store_true", help="Simulate without uploading or editing")
    args = parser.parse_args()

    raw_json_path = args.json_path or find_default_json_path()
    json_path = os.path.abspath(raw_json_path)
    base_dir = os.path.dirname(json_path)
    cache_path = os.path.abspath(args.cache_path)

    if not os.path.exists(json_path):
        print(f"[ERROR] JSON file not found: {json_path}")
        sys.exit(1)

    print(f"=== Starting Telegram Chat Media Sync to Google Drive ===")
    print(f"JSON Path:    {json_path}")
    print(f"Base Dir:     {base_dir}")
    print(f"Parent ID:    {args.parent_id}")
    print(f"Cache Path:   {cache_path}")
    print(f"Workers:      {args.workers}")
    print(f"Dry Run:      {args.dry_run}")
    print(f"Delete Local: {args.delete_local}")

    # 1. Load cache if exists
    cache = {}
    if os.path.exists(cache_path):
        try:
            with open(cache_path, "r", encoding="utf-8") as f:
                cache = json.load(f)
            print(f"[CACHE] Loaded {len(cache)} existing entries from {cache_path}")
        except Exception as e:
            print(f"[WARN] Failed to load cache: {e}")

    # 2. Check Drive existing items
    print("[DRIVE] Checking existing files in Drive folder...")
    drive_existing = load_drive_existing_files(args.parent_id)
    print(f"[DRIVE] Found {len(drive_existing)} existing files in target Drive folder.")

    # 3. Discover all local media files (and symlinks) on disk
    media_subdirs = ["files", "photos", "stickers"]
    disk_files = []
    for d in media_subdirs:
        sub_path = os.path.join(base_dir, d)
        if os.path.exists(sub_path):
            for root, _, files in os.walk(sub_path, followlinks=True):
                for f in files:
                    full_p = os.path.join(root, f)
                    rel = os.path.relpath(full_p, base_dir)
                    disk_files.append(rel)

    print(f"[SCAN] Found {len(disk_files)} media files across disk folders ({', '.join(media_subdirs)}).")

    # Match files from drive_existing into cache if not present
    for rel in disk_files:
        fname = os.path.basename(rel)
        if rel not in cache and fname in drive_existing:
            file_id = drive_existing[fname]
            cache[rel] = {
                "drive_id": file_id,
                "url": build_drive_url(file_id),
                "filename": fname
            }

    # 4. Determine which files need uploading
    to_upload = [rel for rel in disk_files if rel not in cache]
    print(f"[UPLOAD] {len(cache)} files already resolved. {len(to_upload)} files need upload.")

    if not args.dry_run and to_upload:
        print(f"[UPLOAD] Starting parallel upload with {args.workers} workers...")
        completed_count = 0
        total_to_upload = len(to_upload)

        def worker_task(rel_path):
            abs_path = os.path.join(base_dir, rel_path)
            file_id = upload_single_file(abs_path, args.parent_id)
            url = build_drive_url(file_id)
            return rel_path, file_id, url

        with ThreadPoolExecutor(max_workers=args.workers) as executor:
            future_to_file = {executor.submit(worker_task, rel): rel for rel in to_upload}
            for future in as_completed(future_to_file):
                rel = future_to_file[future]
                try:
                    rel_path, file_id, url = future.result()
                    with cache_lock:
                        cache[rel_path] = {
                            "drive_id": file_id,
                            "url": url,
                            "filename": os.path.basename(rel_path)
                        }
                        completed_count += 1
                        print(f"[{completed_count}/{total_to_upload}] Uploaded {rel_path} -> {file_id}")
                        # Persist cache incrementally
                        os.makedirs(os.path.dirname(cache_path), exist_ok=True)
                        with open(cache_path, "w", encoding="utf-8") as cf:
                            json.dump(cache, cf, indent=2, ensure_ascii=False)
                except Exception as exc:
                    print(f"[ERROR] Failed uploading {rel}: {exc}")
                    raise exc

    # Persist final cache
    if not args.dry_run:
        os.makedirs(os.path.dirname(cache_path), exist_ok=True)
        with open(cache_path, "w", encoding="utf-8") as cf:
            json.dump(cache, cf, indent=2, ensure_ascii=False)

    # 5. Read result.json and replace links
    print("[JSON] Reading result.json...")
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Build filename lookup for recovery of "(File unavailable, please try again later)"
    filename_to_url = {}
    for rel_path, info in cache.items():
        fname = os.path.basename(rel_path)
        filename_to_url[fname] = info["url"]

    replacements_count = 0
    recovered_count = 0

    def replace_paths(obj):
        nonlocal replacements_count, recovered_count
        if isinstance(obj, dict):
            # Check for recovered files where file was unavailable but file_name matches
            if obj.get("file") == "(File unavailable, please try again later)" and "file_name" in obj:
                fname = obj["file_name"]
                if fname in filename_to_url:
                    obj["file"] = filename_to_url[fname]
                    recovered_count += 1
                    replacements_count += 1

            for k, v in obj.items():
                if isinstance(v, str):
                    if v in cache:
                        obj[k] = cache[v]["url"]
                        replacements_count += 1
                    elif v.startswith(("files/", "photos/", "stickers/")):
                        # Also check if base name matches cache
                        bname = os.path.basename(v)
                        if bname in filename_to_url:
                            obj[k] = filename_to_url[bname]
                            replacements_count += 1
                elif isinstance(v, (dict, list)):
                    replace_paths(v)
        elif isinstance(obj, list):
            for i, item in enumerate(obj):
                if isinstance(item, str):
                    if item in cache:
                        obj[i] = cache[item]["url"]
                        replacements_count += 1
                    elif item.startswith(("files/", "photos/", "stickers/")):
                        bname = os.path.basename(item)
                        if bname in filename_to_url:
                            obj[i] = filename_to_url[bname]
                            replacements_count += 1
                elif isinstance(item, (dict, list)):
                    replace_paths(item)

    replace_paths(data)
    print(f"[JSON] Completed replacements: {replacements_count} total (including {recovered_count} recovered unavailable files).")

    if not args.dry_run and replacements_count > 0:
        # Create backup if not already present
        bak_path = json_path + ".bak"
        if not os.path.exists(bak_path):
            shutil.copy2(json_path, bak_path)
            print(f"[BACKUP] Created backup at {bak_path}")

        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=1, ensure_ascii=False)
        print(f"[JSON] Updated {json_path} successfully.")

    # 6. Delete local media if requested
    if args.delete_local and not args.dry_run:
        print("[CLEANUP] Deleting local media folders...")
        for d in media_subdirs:
            sub_path = os.path.join(base_dir, d)
            if os.path.exists(sub_path):
                if os.path.islink(sub_path):
                    os.unlink(sub_path)
                elif os.path.isdir(sub_path):
                    shutil.rmtree(sub_path)
                print(f"[CLEANUP] Removed {sub_path}")

    print("=== Sync completed successfully! ===")


if __name__ == "__main__":
    main()
