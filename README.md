# Sample Browser (CrateTrack)

> **Granular Audio Passage Discovery and Acoustic Bookmarking for Independent Music Producers**

[![Course](https://img.shields.io/badge/Course-FAF.PCAS25.1%20(PBL)-blue.svg)](conceptual_design/docs/guidelines/PCAS_Project_PBL_Guideline.pdf)
[![Institution](https://img.shields.io/badge/Institution-UTM%20%2F%20FCIM-red.svg)](https://utm.md/)
[![Status](https://img.shields.io/badge/Status-Midterm%201%20Passed%20%7C%20Midterm%202%20Field%20Validation-success.svg)]()
[![Report](https://img.shields.io/badge/Report-PDF%20(34%20pages)-orange.svg)](conceptual_design/FAF.PCAS25.1_Team16_Report.pdf)

---

## 📌 Executive Summary

**Sample Browser (CrateTrack)** is an academic software engineering project developed within the **Problem-Based Learning (PBL)** framework at the **Technical University of Moldova (UTM)**. 

Independent music producers operating in sample-based genres (hip-hop, lo-fi, neo-soul, electronic) spend disproportionate hours manually scrubbing through full-length recordings to locate short, usable 4–30 second passages (such as isolated drum breaks, vocal-free Rhodes progressions, or clean melodic hooks). 

Contemporary platforms (Spotify, YouTube) index audio strictly by **whole-track metadata** (Artist, Title, Album), leaving creators trapped between generic, overused loop libraries (Splice) and unstructured, fatiguing crate-digging across streaming catalogs. **Sample Browser** resolves this via:
1. **Sub-Track Timestamp Indexing (`start_time`, `end_time`):** Zero server-side audio downloading or parsing (100% compliant with YouTube API Section III.E Terms of Service). Playback is handled client-side via the official YouTube IFrame Player API.
2. **Two-Tier Preset Taxonomy:** Eliminating tag disagreement and vocabulary friction through high-priority objective tags (*Isolation*, *Instrumentation*, *Section Role*) paired with instant audio auditioning.
3. **Seed-Passage ("Berrypicking") Exploration:** Navigation by associative chains from acoustic segments the producer is actively listening to, bypassing blank text search queries.

---

## 👥 Team 16 Members & Responsibilities

* **Mentor:** Prof. Elena Graur (Technical University of Moldova, FCIM)
* **Students (FAF-261 / FAF-262 / FAF-263):**
  * **Bogdan Glavan** (`FAF-261`) — *Team Leader*: Project coordination, YouTube IFrame architecture boundaries, and Berrypicking UI concept design.
  * **Leonid Tiscenco** (`FAF-263`) — *Methodology & Systems Architecture*: Architectural analysis, pivot synthesis, and validation hypothesis formulation ($H_1$–$H_4$).
  * **Andrei Simon** (`FAF-261`) — *Field Validation & Customer Discovery*: Interview questionnaire drafting, producer outreach, and field interviews.
  * **Nikita Creciun** (`FAF-263`) — *Domain Analysis & Competitive Research*: Problem analysis refinement, market landscape, and comparative SWOT benchmarking.
  * **Mihai-Constantin Sîrghii** (`FAF-262`) — *User Research & Personas*: Target creator segmentation, user personas (Annie Lee & Alex Rivera), and workflow mapping.

> [!NOTE]
> Within the Problem-Based Learning (PBL) framework, team members collaboratively conduct customer validation interviews (~4 interviews per student, $N \approx 20$ total) and jointly author project specifications.

---

## 🚀 Key Project Deliverables

| Deliverable | Format | Path / Link | Description |
| :--- | :--- | :--- | :--- |
| **Academic Project Report** | PDF | [`conceptual_design/FAF.PCAS25.1_Team16_Report.pdf`](conceptual_design/FAF.PCAS25.1_Team16_Report.pdf) | Canonical 34-page Midterm 1 & Midterm 2 engineering report with empirical interview validation. |
| **Interactive HTML Pitch Deck** | HTML | [`conceptual_design/presentation/html/index.html`](conceptual_design/presentation/html/index.html) | Responsive 16:9 minimalist visual pitch deck ([`variant_3_clean_pitch.html`](conceptual_design/presentation/html/variant_3_clean_pitch.html)) for Midterm 2 defense. |
| **Interview Transcripts & Viewer** | JSON / Python | [`conceptual_design/data/interviews/transcripts/`](conceptual_design/data/interviews/transcripts/) | WhisperX dialogue transcripts ($P_1$–$P_4$) and interactive CLI reader (`viewer.py`). |
| **Interview Recordings Catalog** | Markdown / Drive | [`conceptual_design/data/interviews/recordings/README.md`](conceptual_design/data/interviews/recordings/README.md) | Direct index to video/audio recordings on Google Drive. |
| **Course Guidelines & Summaries** | Markdown / DOCX | [`conceptual_design/docs/guidelines/`](conceptual_design/docs/guidelines/) | Course requirements, syllabus summary, and executive summary of mandatory 2026 template. |
| **Validation Protocol & Script** | Markdown | [`conceptual_design/docs/validation_protocol.md`](conceptual_design/docs/validation_protocol.md) | Single Source of Truth for $N \approx 20$ interviews and Google Forms survey. |
| **Customer Interview Kit** | PDF / TeX / MD | [`conceptual_design/interview_files/`](conceptual_design/interview_files/) | 10-question Mom Test interview script and multi-language survey form links. |
| **Google Drive Storage Workflow** | Markdown | [`conceptual_design/docs/gdrive_storage_workflow.md`](conceptual_design/docs/gdrive_storage_workflow.md) | Replaces DVC: lightweight Git tracking paired with team Google Drive media storage. |
| **Telegram Sync Automation** | Python Script | [`scripts/sync_telegram_chat_to_gdrive.py`](scripts/sync_telegram_chat_to_gdrive.py) | Reusable tool syncing chat attachments to Google Drive and embedding links into `result.json`. |
| **Beamer Presentation** | PDF / PPTX | [`conceptual_design/presentation/presentation.pdf`](conceptual_design/presentation/presentation.pdf) | Original Midterm 1 slide deck with architecture and SWOT appendices. |

---

## 🗂️ Repository Structure

```text
sample-browser/
├── README.md                      # Project overview, team onboarding, and architectural index
├── .gitignore                     # Ignore rules for LaTeX, media (*.mp4, *.mp3, *.wav, archives) & OS files
├── scripts/
│   └── sync_telegram_chat_to_gdrive.py  # Convenient symlink to chat sync automation tool
│
└── conceptual_design/
    ├── FAF.PCAS25.1_Team16_Report.pdf   # Primary compiled PDF report (34 pages)
    │
    ├── docs/                            # CANONICAL DOCUMENTATION (Single Source of Truth)
    │   ├── validation_protocol.md       # Hypotheses H1–H4, 10-Q Mom Test script, 4 recruitment channels
    │   ├── report_text.md               # Full markdown text of the academic report
    │   ├── gdrive_storage_workflow.md   # Google Drive team remote storage rules (replacing DVC)
    │   ├── guidelines/                  # Course guidelines and executive summaries
    │   │   ├── MANDATORY_PBL report_template_26.docx      # Official 2026 mandatory template
    │   │   ├── MANDATORY_PBL_report_template_26_summary.md # Distilled requirements & conflict analysis
    │   │   ├── PCAS_Project_PBL_Guideline.pdf             # Course syllabus from Prof. Elena Graur
    │   │   ├── PBL_GUIDELINE.md                           # Markdown transcript of syllabus
    │   │   └── PCAS_Project_PBL_Guideline_summary.md      # Summary of grading rubrics & milestones
    │   └── templates/                   # University templates and LaTeX cheat sheets
    │       ├── getting_started.md
    │       ├── latex_cheat_sheet.md
    │       └── presentation_template.docx
    │
    ├── interview_files/                 # Customer validation assets & survey links
    │   ├── SB_Interview_Questions.pdf   # Typeset 10-question interview script
    │   ├── SB_Interview_Questions.tex   # LaTeX source for interview guide
    │   └── form_links.md                # Google Forms distribution links (EN, RO, RU)
    │
    ├── data/                            # Customer validation data and interviews
    │   └── interviews/
    │       ├── README.md                # Overview of customer discovery data
    │       ├── recordings/              # Media directory (binaries ignored by Git)
    │       │   └── README.md            # Direct Google Drive catalog for interviews P01–P04
    │       └── transcripts/             # Qualitative interview data
    │           ├── 2026-11-16-interview1-soundphace.json
    │           ├── 2026-11-17_interview2-Boris_Iurcu.json
    │           ├── 2026-11-17-interview3-Mihai_Macaru.json
    │           ├── 2026-11-17-interview4-Anonymous_Producer1.json
    │           └── viewer.py            # Interactive CLI viewer for WhisperX transcripts
    │
    ├── meetings/                        # Official team minutes & decisions
    │   └── 2026-11-07_pivot_meeting_notes.md  # Architectural pivot notes (Bogdan & Leonid debate)
    │
    ├── report/                          # LaTeX source code for the project report
    │   ├── main.tex                     # Master LaTeX document
    │   ├── tum_report.cls               # Technical University of Moldova document class
    │   ├── title_page.tex               # Title and signature page
    │   ├── abstract.tex                 # Project abstract
    │   ├── introduction.tex             # Chapter 1: Introduction
    │   ├── midterm1.tex                 # Chapter 2: Midterm 1 Domain Analysis & Problem Description
    │   ├── midterm2.tex                 # Chapter 3: Midterm 2 Validation Findings, SRS & UML
    │   ├── conclusion.tex               # Chapter 4: Conclusions
    │   ├── bibliography.tex             # Academic & industry references
    │   └── images/                      # High-resolution vector diagrams & UI mockups
    │       ├── problem_bottlenecks.png
    │       ├── architecture_overview.png
    │       ├── before_after_workflow.png
    │       ├── ui_concept_mockup.png
    │       └── ...
    │
    ├── presentation/                    # Presentations (Beamer & HTML)
    │   ├── html/                        # Interactive 16:9 Presentation Deck (Chosen Pitch Format)
    │   │   ├── index.html               # Hub & presentation launcher
    │   │   ├── variant_3_clean_pitch.html # Minimalist, photo-centric startup pitch deck
    │   │   └── assets/                  # High-resolution studio photography & hardware visuals
    │   ├── README.md                    # Context note regarding Midterm 1 vs. post-pivot architecture
    │   ├── main.tex                     # Master Beamer LaTeX file
    │   ├── presentation.pdf             # Compiled Beamer presentation slides
    │   ├── output.pptx                  # PowerPoint conversion
    │   └── images/                      # Slide graphics & photos
    │
    ├── scripts/                         # Automation tools
    │   ├── generate_diagrams.py         # Vector diagram rendering script (Inkscape 3900px native)
    │   ├── sync_telegram_chat_to_gdrive.py  # Telegram media uploader & result.json link updater
    │   └── telegram_media_cache.json    # Upload cache mapping local files to Google Drive IDs
    │
    └── archive/                         # Historical archive (early drafts & audits with deprecation notices)
        ├── README.md                    # Explanation of superseded concepts and project evolution
        ├── audits/                      # Independent audit reports (RU/EN) identifying initial gaps
        ├── early_drafts/                # Pre-pivot drafts (Oct 2026) with explicit [!WARNING] banners
        │   └── interviews/              # Deprecated questionnaire versions (OLD_InterviewQ_update1/2)
        ├── milestone0_ideation/         # Milanote ideation maps and initial pitch attempts
        └── raw_logs/                    # Team communication records
            └── TelegramChatExport_2026-11-19/
                └── result.json          # Chat export with 135 direct permanent Google Drive links
```

---

## 🛠️ Instructions for Team Members

### 1. Compiling the LaTeX Report
The report is typeset using standard `pdflatex` (TeX Live 2023+).
```bash
cd conceptual_design/report
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
cp main.pdf ../FAF.PCAS25.1_Team16_Report.pdf
```

### 2. Viewing the Interactive HTML Presentation
Open [`conceptual_design/presentation/html/index.html`](conceptual_design/presentation/html/index.html) in any modern browser or jump directly to the active deck:
* **Active Deck:** [`conceptual_design/presentation/html/variant_3_clean_pitch.html`](conceptual_design/presentation/html/variant_3_clean_pitch.html)
* **Controls:** `→` / `Space` (Next slide), `←` / `Backspace` (Previous slide), `F` (Toggle 16:9 fullscreen mode).

### 3. Reading Interview Transcripts (Interactive CLI Viewer)
To inspect qualitative dialogues with timestamps, search keywords, and speaker turns:
```bash
python3 conceptual_design/data/interviews/transcripts/viewer.py
```

### 4. Syncing Telegram Chat Backups to Google Drive
When exporting an updated Telegram chat history into `conceptual_design/archive/raw_logs/`:
```bash
python3 scripts/sync_telegram_chat_to_gdrive.py --delete-local
```
This automatically uploads new media to Google Drive, updates `result.json` with direct drive URLs, and cleans local binaries.

### 5. Running Customer Interviews (Midterm 2 Protocol)
* Review the interview script and rules in [`conceptual_design/docs/validation_protocol.md`](conceptual_design/docs/validation_protocol.md).
* **Sample Target:** $N \approx 20$ recorded video interviews (~4 per team member) across 4 channels (University peers, Instagram DMs, Discord servers, and YouTube sample-flip creators).
* **Language:** Any language (English, Romanian, Russian) as long as the respondent is an active music maker.
* **Core Rule:** Strictly adhere to *The Mom Test* (ask about concrete past behavior in recent digging sessions; do not pitch future hypothetical features).
