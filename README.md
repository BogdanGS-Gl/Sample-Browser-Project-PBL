# Sample Browser (CrateTrack)

> **Granular Audio Passage Discovery and Acoustic Bookmarking for Independent Music Producers**

[![Course](https://img.shields.io/badge/Course-FAF.PCAS25.1%20(PBL)-blue.svg)](conceptual_design/docs/guidelines/PCAS_Project_PBL_Guideline.pdf)
[![Institution](https://img.shields.io/badge/Institution-UTM%20%2F%20FCIM-red.svg)](https://utm.md/)
[![Status](https://img.shields.io/badge/Status-Midterm%201%20Passed%20%7C%20Midterm%202%20Validation-success.svg)]()
[![Report](https://img.shields.io/badge/Report-PDF%20(33%20pages)-orange.svg)](conceptual_design/FAF.PCAS25.1_Team16_Report.pdf)

---

## 📌 Executive Summary

**Sample Browser** is an academic software engineering project developed within the **Problem-Based Learning (PBL)** framework at the **Technical University of Moldova (UTM)**. 

Independent music producers operating in sample-based genres (hip-hop, lo-fi, neo-soul, electronic) spend disproportionate hours manually scrubbing through full-length recordings to locate short, usable 4–30 second passages (such as isolated drum breaks, vocal-free Rhodes progressions, or clean melodic hooks). 

Contemporary platforms (Spotify, YouTube) index audio strictly by **whole-track metadata** (Artist, Title, Album), leaving creators trapped between generic, overused loop libraries (Splice) and unstructured, fatiguing crate-digging across streaming catalogs. **Sample Browser** resolves this via:
1. **Sub-Track Timestamp Indexing (`start_time`, `end_time`):** Zero server-side audio downloading or parsing (100% compliant with YouTube API Section III.E Terms of Service). Playback is handled client-side via the official YouTube IFrame Player API.
2. **Two-Tier Preset Taxonomy:** Eliminating tag disagreement and vocabulary friction through high-priority objective tags (*Isolation*, *Instrumentation*, *Section Role*) paired with instant audio auditioning.
3. **Seed-Passage ("Berrypicking") Exploration:** Navigation by associative chains from acoustic segments the producer is actively listening to, bypassing blank text search queries.

---

## 👥 Team 16 Members & Responsibilities

* **Mentor:** Prof. Elena Graur (Technical University of Moldova, FCIM)
* **Students:**
  * **Bogdan Glavan** (`FAF-261`) — *Team Leader*: Domain research, technical solution boundaries, YouTube IFrame architecture, and Berrypicking UI design.
  * **Leonid Tiscenco** (`FAF-263`) — *Methodology & Audit*: System architecture synthesis, hypothesis formulation (H1–H4), and Mom Test interview protocol audit.
  * **Andrei Simon** (`FAF-261`) — *Validation & Field Testing*: Producer outreach, initial questionnaire drafting, and customer interview execution.
  * **Nikita Creciun** (`FAF-263`) — *Problem Analysis*: Problem description refinement, competitive landscape, and SWOT benchmarking (Splice, Tracklib, Samplette).
  * **Mihai-Constantin Sîrghii** (`FAF-262`) — *Target Audience*: User personas (Annie Lee & Alex Rivera), target creator segments, and workflow scenario mapping.

---

## 🚀 Key Project Deliverables

| Deliverable | Format | Path / Link | Description |
| :--- | :--- | :--- | :--- |
| **Academic Project Report** | PDF | [`conceptual_design/FAF.PCAS25.1_Team16_Report.pdf`](conceptual_design/FAF.PCAS25.1_Team16_Report.pdf) | Canonical 33-page Midterm 1 & Midterm 2 engineering report. |
| **Validation Protocol & Script** | Markdown | [`conceptual_design/docs/validation_protocol.md`](conceptual_design/docs/validation_protocol.md) | Single Source of Truth for $N \approx 20$ interviews and Google Forms survey. |
| **Pivot Meeting Notes** | Markdown | [`conceptual_design/meetings/2026-11-07_pivot_meeting_notes.md`](conceptual_design/meetings/2026-11-07_pivot_meeting_notes.md) | Architectural pivot consensus, debate resolution, and action items. |
| **Beamer Presentation** | PDF / PPTX | [`conceptual_design/presentation/presentation.pdf`](conceptual_design/presentation/presentation.pdf) | Slide deck with interactive architecture and SWOT appendices. |
| **Report Markdown Mirror** | Markdown | [`conceptual_design/docs/report_text.md`](conceptual_design/docs/report_text.md) | Full text mirror of the 33-page report for quick diffs and search. |

---

## 🗂️ Repository Structure

```text
sample-browser/
├── README.md                      # Project overview, team onboarding, and architectural index
├── .gitignore                     # Clean ignore rules for LaTeX, Python, and OS artifacts
└── conceptual_design/
    ├── FAF.PCAS25.1_Team16_Report.pdf # Primary compiled PDF report (33 pages)
    │
    ├── docs/                          # CANONICAL DOCUMENTATION (Single Source of Truth)
    │   ├── validation_protocol.md     # Falsifiable hypotheses H1–H4, 10-Q Mom Test script, 4 channels
    │   ├── report_text.md             # Full markdown text of the academic report
    │   ├── guidelines/                # Course guidelines and rubrics from Prof. Elena Graur
    │   │   ├── PCAS_Project_PBL_Guideline.pdf
    │   │   └── PBL_GUIDELINE.md
    │   └── templates/                 # University templates and LaTeX cheat sheets
    │       ├── getting_started.md
    │       ├── latex_cheat_sheet.md
    │       └── presentation_template.docx
    │
    ├── meetings/                      # Official team minutes & decisions
    │   └── 2026-11-07_pivot_meeting_notes.md  # Architectural pivot notes (Bogdan & Leonid debate)
    │
    ├── report/                        # LaTeX source code for the 33-page project report
    │   ├── main.tex                   # Master LaTeX document
    │   ├── tum_report.cls             # Technical University of Moldova document class
    │   ├── title_page.tex             # Title and signature page
    │   ├── abstract.tex               # Project abstract
    │   ├── introduction.tex           # Chapter 1: Introduction
    │   ├── midterm1.tex               # Chapter 2: Midterm 1 Domain Analysis & Problem Description
    │   ├── midterm2.tex               # Chapter 3: Midterm 2 Roadmap, Requirements & UML
    │   ├── conclusion.tex             # Chapter 4: Conclusions
    │   ├── bibliography.tex           # Academic & industry references
    │   └── images/                    # High-resolution vector diagrams & UI mockups
    │       ├── problem_bottlenecks.png
    │       ├── architecture_overview.png
    │       ├── before_after_workflow.png
    │       ├── ui_concept_mockup.png
    │       └── ...
    │
    ├── presentation/                  # LaTeX Beamer presentation for Midterm 1
    │   ├── main.tex                   # Master Beamer file
    │   ├── slide01_title.tex .. slide11_appendix_problem_table.tex
    │   ├── presentation_text.md       # Speaker notes & slide content
    │   ├── CONTENT_CHANGELOG.md       # Slide version history
    │   ├── presentation.pdf           # Compiled presentation slides
    │   ├── output.pptx                # PowerPoint conversion
    │   └── images/                    # Slide graphics & photos
    │
    ├── scripts/                       # Developer automation scripts
    │   └── generate_diagrams.py       # Vector diagram rendering script (Inkscape 3900px native)
    │
    └── archive/                       # Historical archive (early drafts & audits with deprecation notices)
        ├── README.md                  # Explanation of superseded concepts and project evolution
        ├── audits/                    # Independent audit reports (RU/EN) identifying initial gaps
        ├── early_drafts/              # Pre-pivot drafts (Oct 2026) with explicit [!WARNING] banners
        ├── milestone0_ideation/       # Milanote ideation maps and initial pitch attempts
        └── raw_logs/                  # Telegram team chat dumps
```

---

## 🛠️ Instructions for Team Members

### 1. Compiling the LaTeX Report
The report is typeset using standard `pdflatex` (TeX Live 2023+).
```bash
cd conceptual_design/report
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
```
To update the root deliverable:
```bash
cp conceptual_design/report/main.pdf ../FAF.PCAS25.1_Team16_Report.pdf
```

### 2. Regenerating Vector Graphics
All architectural diagrams in `report/images/` are generated via Python and rendered with native vector crispness (3900px width) through `inkscape`:
```bash
# From repository root:
python3 conceptual_design/scripts/generate_diagrams.py
```

### 3. Compiling the Presentation
```bash
cd conceptual_design/presentation
pdflatex -interaction=nonstopmode main.tex
cp main.pdf presentation.pdf
```

### 4. Running Customer Interviews (Midterm 2 Protocol)
* Review the interview script and rules in [`docs/validation_protocol.md`](docs/validation_protocol.md).
* **Sample Target:** $N \approx 20$ recorded video interviews (~4 per team member) across 4 channels (University peers, Instagram DMs, Discord servers, and YouTube sample-flip creators).
* **Language:** Any language (English, Romanian, Russian) as long as the respondent is an active music maker.
* **Core Rule:** Strictly adhere to *The Mom Test* (ask about concrete past behavior in recent digging sessions; do not pitch future hypothetical features).
