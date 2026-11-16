# DVC & Google Drive Workflow Guide

This document establishes the official workflow for storing, versioning, and sharing large files (interview video recordings, audio datasets, and binary models) using **DVC (Data Version Control)** backed by **Google Drive**.

---

## ☁️ Remote Storage Layout (Google Drive)

All heavy files are stored in the shared team Google Drive:
* **Root Storage Folder:** `Sample-Browser-PBL-Data` (ID: [`1Yok9241R2tXjZjan97RcAFVRuPVwLu39`](https://drive.google.com/drive/folders/1Yok9241R2tXjZjan97RcAFVRuPVwLu39))
* **DVC Remote Endpoint:** `dvc_storage` (ID: [`1I5NWw52JejkocnxIXLhkj20QthEx2auu`](https://drive.google.com/drive/folders/1I5NWw52JejkocnxIXLhkj20QthEx2auu))
* **Interview Recordings:** `interviews/recordings` (ID: [`116C1g7NSWrzBwp-J8NU8g5M_O_ycymUk`](https://drive.google.com/drive/folders/116C1g7NSWrzBwp-J8NU8g5M_O_ycymUk))
* **Audio Datasets:** `datasets/audio_samples` (ID: [`1RU3s3qfDgEMvwpiIM8O_lMwrh9unIfhx`](https://drive.google.com/drive/folders/1RU3s3qfDgEMvwpiIM8O_lMwrh9unIfhx))

---

## 🛠️ Step-by-Step Instructions for Team Members

### 1. Prerequisites (Installing DVC with Google Drive support)
In your local Python environment:
```bash
pip install "dvc[gdrive]"
```

### 2. Authenticating with Google Drive
The project's `.dvc/config` is already configured with:
```ini
['remote "gdrive-storage"']
    url = gdrive://1I5NWw52JejkocnxIXLhkj20QthEx2auu
[core]
    remote = gdrive-storage
```

The first time you run `dvc push` or `dvc pull`, DVC will open your browser to authorize access to Google Drive using your Google account.

### 3. Adding and Versioning a New Interview Video
When you finish an interview recording (e.g. `2026-11-16-interview01-soundphace.mp4`):
```bash
# 1. Place the recording into the data directory
mv /path/to/recording.mp4 conceptual_design/data/interviews/recordings/

# 2. Tell DVC to track the recordings directory (or individual file)
dvc add conceptual_design/data/interviews/recordings

# 3. DVC generates 'conceptual_design/data/interviews/recordings.dvc' (a small metadata text pointer)
# Stage the DVC pointer file in Git:
git add conceptual_design/data/interviews/recordings.dvc

# 4. Push the actual large video bytes to Google Drive:
dvc push
```

### 4. Pulling Heavy Files on Another Machine
When a teammate wants to download the interview videos:
```bash
git pull
dvc pull
```
DVC will inspect the `.dvc` pointer files and download the exact binary blobs from the team's Google Drive.

---

## 📌 Rules on What Goes into Git vs. DVC

| Content Type | Storage Engine | Reason |
| :--- | :---: | :--- |
| LaTeX reports, slides, TeX source | **Git** | Text files, requires line-by-line diffs and version history. |
| Vector diagrams (SVG), Python scripts | **Git** | Lightweight source assets (< 100 KB). |
| Markdown docs, transcripts, interview notes | **Git** | Plain text; facilitates review and search. |
| Interview video recordings (.mp4, .webm) | **DVC / Google Drive** | Large binaries (100 MB – 1 GB+ per file); breaks Git limits. |
| Audio stems and test sound packs (.wav, .flac) | **DVC / Google Drive** | Large audio buffers; irrelevant for source code control. |
| Model weights / ML checkpoints (.pt, .onnx) | **DVC / Google Drive** | Binary weights; non-diffable. |
