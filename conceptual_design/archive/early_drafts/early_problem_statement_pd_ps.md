> [!WARNING]
> **ARCHIVE / HISTORICAL DRAFT (OCTOBER 2026)**
> Этот документ является ранним историческим черновиком до архитектурного пивота 6–7 ноября 2026 г.
> Он содержит устаревшие концепции (серверный анализ аудиопотока YouTube, неструктурированные текстовые теги, старую концепцию «Better Spotify» и Spotify API).
> **Актуальные канонические материалы проекта находятся в папке `docs/`:**
> - Архитектура и протокол валидации: [`docs/validation_protocol.md`](../../docs/validation_protocol.md)
> - Полный отчёт: [`docs/report_text.md`](../../docs/report_text.md)

---

# 1. Problem Description & Problem Statement

## 1.1 Problem Description

### Who Has the Problem
The target group comprises independent music producers working primarily in sample-based and electronic genres (hip-hop, electronic, neo-soul, experimental). 

According to Tracklib’s 2024 Producer Survey ($N = 1,107$), 58% of respondents identify as aspiring producers seeking to build a professional career, 25% as hobbyists, 8% as beginners, and 10% as full-time professionals. Furthermore, data from the UK Musicians' Census ($N \approx 6,000$) reveals that 53% of music creators must sustain their living through outside employment. Consequently, independent producers operate under severe time constraints, where prolonged, repetitive search tasks directly reduce time available for actual music composition and production.

### Why It Is a Problem
Sampling and reference-based production fundamentally rely on discovering specific musical passages within existing recordings. However, modern audio streaming architectures create two critical bottlenecks:

1. **The Vocabulary Gap (Sound Discovery):** 
   Producers typically search for subjective acoustic textures, distinct instrumental timbres, or harmonic moods. Translating an auditory reference into conventional keyword queries fails because natural language lacks universal descriptors for complex acoustic characteristics. As research demonstrates, timbral descriptions ("warm", "dry", "gritty") are ambiguous, and synthesized or mixed textures frequently lack agreed-upon semantic keywords.

2. **The Whole-Track Bottleneck (Passage Discovery):**
   Commercial streaming catalogs index audio at the whole-track metadata level (Track Title, Artist, Genre, Album, Key, BPM). A producer, however, does not sample whole tracks; they look for localized segments—a 4-bar rhythm break, an unlayered Rhodes progression, or an intro section devoid of drums. Because platforms do not index or search within sub-track time boundaries, producers must manually scrub through hundreds of candidate tracks. 

This audition cycle disrupts creative "flow" and cognitive momentum. In music information retrieval (MIR) studies, producers explicitly report that repetitive browsing and scrubbing "takes forever and ruins the creative flow." While unstructured crate-digging provides occasional serendipity, the inability to execute targeted reference matching turns routine discovery into an inefficient manual audit.

### Stakeholders
* **Primary (Independent Producers):** Gain immediate workflow efficiency, preserving cognitive focus and discovering relevant source material faster.
* **Secondary (Original Rights Holders & Catalog Artists):** Deep-catalog recordings receive increased visibility, engagement, and potential licensing/clearance opportunities.
* **Tertiary (Streaming & Sample Platforms):** Transition from passive listening tools into active creator utilities, increasing user retention among professional and semi-professional creators.

### Domain Relevance
Sampling remains central to contemporary music culture. Industry analyses show that approximately 17% of Billboard Hot 100 hits rely on sampled material. Simultaneously, music catalogs are expanding exponentially: streaming platforms currently host over 250 million tracks, with more than 100,000 new recordings ingested daily. Without segment-level acoustic indexing, this massive catalog volume exacerbates the needle-in-a-haystack dilemma for creators.

---

## 1.2 Problem Statement

> **"Independent music producers lack an efficient way to discover and locate specific musical passages within full-length catalog recordings based on acoustic references, because contemporary streaming search interfaces index music exclusively at the whole-track metadata level, forcing producers into tedious, manual scrubbing that disrupts the creative workflow."**

---

## 1.3 Customer Validation Hypotheses & Methodology

To validate whether segment-level acoustic search provides measurable utility over baseline crate-digging, we establish three verifiable hypotheses:

* **H1 (Frequency and Friction):** Independent producers identify manual passage scrubbing across full-length tracks as a primary friction point in their sampling workflow.
  * *Method:* Semi-structured interviews ($N=10$) and task-based screener questionnaires measuring search abandonment rates.
* **H2 (Workflow Insufficiency):** Current market solutions (Spotify SongDNA, YouTube digging, pre-made loop marketplaces like Splice) are insufficient when the goal is locating *unlinked acoustic passages within full compositions*.
  * *Method:* Observational user testing comparing task completion and perceived limitations across existing tools.
* **H3 (Integrated Passage Discovery Utility):** A workflow enabling reference-based segment matching with timestamped playback reduces search/audition time by at least 40% while preserving perceived creative serendipity.
  * *Method:* A/B usability testing with interactive interactive prototype vs. manual streaming search baseline, logging Time-on-Task (ToT) and System Usability Scale (SUS).