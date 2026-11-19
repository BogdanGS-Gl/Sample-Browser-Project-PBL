# Google Drive & Git Storage Workflow Guide

This document establishes the official team workflow for managing project assets, datasets, and interview recordings across **Git** (lightweight source and text) and **Google Drive** (heavy binary media).

---

## ☁️ Remote Storage Layout (Google Drive)

All heavy binary files are stored in the team Google Drive:
* **Root Storage Folder:** `Sample-Browser-PBL-Data` (ID: [`1Yok9241R2tXjZjan97RcAFVRuPVwLu39`](https://drive.google.com/drive/folders/1Yok9241R2tXjZjan97RcAFVRuPVwLu39))
* **Interview Recordings:**
  - `interviews/recordings` (ID: [`116C1g7NSWrzBwp-J8NU8g5M_O_ycymUk`](https://drive.google.com/drive/folders/116C1g7NSWrzBwp-J8NU8g5M_O_ycymUk))
  - `Interviews SB` (ID: [`1DzVfMfZD6TnPMOT6AUwI4PvQOtT6N2nw`](https://drive.google.com/drive/folders/1DzVfMfZD6TnPMOT6AUwI4PvQOtT6N2nw))
* **Telegram Chat Media:** `telegram_chat_media` (ID: [`14NvPYoT-LM24Uoo7vRZ7wAFq0xyyYRCJ`](https://drive.google.com/drive/folders/14NvPYoT-LM24Uoo7vRZ7wAFq0xyyYRCJ))
* **Audio Datasets:** `datasets/audio_samples` (ID: [`1RU3s3qfDgEMvwpiIM8O_lMwrh9unIfhx`](https://drive.google.com/drive/folders/1RU3s3qfDgEMvwpiIM8O_lMwrh9unIfhx))

---

## 🛠️ Team Workflow: Git vs. Google Drive

### Separation of Concerns:
- **Git** tracks code, configuration, markdown reports, presentation slides, meeting notes, and indexes.
- **Google Drive** stores video recordings (`.mp4`), audio stems (`.mp3`, `.wav`), large archives (`.zip`), and exported chat attachments.
- **`.gitignore`** is configured to prevent accidental commits of large media files.

### Cataloging Rule:
Whenever new interview recordings or datasets are uploaded to Google Drive:
1. Upload the file to the corresponding folder on Google Drive.
2. Add an entry to the markdown catalog table (e.g. [`conceptual_design/data/interviews/recordings/README.md`](file:///home/thr/Desktop/faf/Sample-Browser-Project-PBL/conceptual_design/data/interviews/recordings/README.md)) with:
   - Respondent pseudonym and date
   - File format and size
   - Direct Google Drive view link (`https://drive.google.com/file/d/<FILE_ID>/view`)

---

## 🤖 Telegram Chat Backup Automation

If you export updated Telegram chat history, use the automation script:
```bash
python3 conceptual_design/scripts/sync_telegram_chat_to_gdrive.py
```
This script:
1. Uploads new media files (`files/`, `photos/`, `stickers/`) to the Google Drive folder `telegram_chat_media`.
2. Automatically replaces all local relative file references in `result.json` with direct Google Drive view links.
3. Caches upload IDs in `telegram_media_cache.json` to avoid redundant uploads.
