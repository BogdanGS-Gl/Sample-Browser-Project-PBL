# Midterm 1 Presentation (Defense Slide Deck)

> [!NOTE]
> **Milestone Status:** Midterm 1 Passed (October 23, 2026).  
> **Target Audience:** Academic Committee (Prof. Elena Graur, FCIM / UTM).  
> **Format:** 11 Slides (9 Core + 2 Appendix), 16:9 widescreen LaTeX Beamer (`main.tex`).  
> **Handoff Artifacts:** [`presentation.pdf`](presentation.pdf) / [`output.pptx`](output.pptx).

---

## ⚠️ Important Note on Project Evolution (Post-Pivot State)

This presentation represents the project state as defended at **Midterm 1**. Please be aware of the subsequent architectural pivot finalized on **November 6–7, 2026**:

1. **Architecture & Audio Processing (Slide 7):**
   * *In this Midterm 1 deck:* Mentions planned evaluation of automated MIR classifiers (Essentia) and displays the preliminary raster diagram `our_system_architecture.jpg`.
   * *Current (Post-Pivot):* All server-side audio ingestion and automated MIR were dropped to ensure 100% compliance with YouTube TOS Section III.E. The production architecture operates strictly via client-side YouTube IFrame API and a PostgreSQL metadata store. See [`conceptual_design/meetings/2026-11-07_pivot_meeting_notes.md`](../meetings/2026-11-07_pivot_meeting_notes.md) and the new vector architecture diagram [`conceptual_design/report/images/architecture_overview.png`](../report/images/architecture_overview.png).

2. **Validation Roadmap & Hypotheses (Slide 9):**
   * *In this Midterm 1 deck:* Lists preliminary exploratory hypotheses and Free/Pro business models.
   * *Current (Post-Pivot):* Streamlined into four falsifiable hypotheses ($H_1$–$H_4$) and a 10-question *The Mom Test* interview protocol documented in [`conceptual_design/docs/validation_protocol.md`](../docs/validation_protocol.md).

A dedicated presentation deck for **Midterm 2** reflecting the post-pivot architecture, empirical validation results ($N \approx 20$), and UML specifications will be prepared in a dedicated milestone folder.
