# Customer Validation Data (Interviews)

This directory houses the raw and processed materials collected from customer discovery interviews ($N \approx 20$) for Midterm 2 validation.

---

## 🗂️ Structure

* **`recordings/`**: Video and audio recordings (.mp4, .webm, .m4a) from Zoom, Google Meet, Discord, or in-person sessions.
  > ⚠️ **DO NOT COMMIT MEDIA FILES TO GIT.**  
  > All video/audio files must be tracked via DVC:
  > ```bash
  > dvc add conceptual_design/data/interviews/recordings/
  > dvc push
  > ```
* **`transcripts/`**: Markdown text transcripts, coding cards, and notes.

---

## 🏷️ Standard Naming Protocol

To ensure seamless traceability across the team:

| Artifact | File Name Format | Example |
| :--- | :--- | :--- |
| **Video Recording** | `YYYY-MM-DD-interviewXX-<pseudonym>.mp4` | `2026-11-16-interview01-soundphace.mp4` |
| **Text Transcript** | `YYYY-MM-DD-interviewXX-<pseudonym>_transcript.md` | `2026-11-16-interview01-soundphace_transcript.md` |
| **Hypothesis Coding Card** | `YYYY-MM-DD-interviewXX-<pseudonym>_card.md` | `2026-11-16-interview01-soundphace_card.md` |

---

## ☁️ Google Drive Remote
* Recordings Folder ID on Drive: [`116C1g7NSWrzBwp-J8NU8g5M_O_ycymUk`](https://drive.google.com/drive/folders/116C1g7NSWrzBwp-J8NU8g5M_O_ycymUk)
* DVC Storage Folder ID: [`1I5NWw52JejkocnxIXLhkj20QthEx2auu`](https://drive.google.com/drive/folders/1I5NWw52JejkocnxIXLhkj20QthEx2auu)
