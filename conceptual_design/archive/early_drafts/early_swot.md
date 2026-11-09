> [!WARNING]
> **ARCHIVE / HISTORICAL DRAFT (OCTOBER 2026)**
> Этот документ является ранним историческим черновиком до архитектурного пивота 6–7 ноября 2026 г.
> Он содержит устаревшие концепции (серверный анализ аудиопотока YouTube, неструктурированные текстовые теги, старую концепцию «Better Spotify» и Spotify API).
> **Актуальные канонические материалы проекта находятся в папке `docs/`:**
> - Архитектура и протокол валидации: [`docs/validation_protocol.md`](../../docs/validation_protocol.md)
> - Полный отчёт: [`docs/report_text.md`](../../docs/report_text.md)

---

## SWOT Analysis: Reference-Based Passage Search in Spotify

### Strengths (S)
* **Vast Catalog Leverage:** Access to >250M tracks compared to limited, closed sample libraries.
* **Native Ecosystem Integration:** Eliminates external browser tabs, third-party downloaders, and disconnected desktop apps.
* **Segment-Level Granularity:** Direct playback jumping to relevant timestamps (bars/seconds) rather than track starts.
* **High Creative Context:** Lets producers audition samples in their original musical context (arrangement, dynamics).

### Weaknesses (W)
* **High Computational Cost:** Audio embedding and similarity indexing across hundreds of millions of tracks require substantial server infrastructure.
* **Subjectivity of Timbre:** Segment similarity may return polyphonic matches that do not isolate the specific instrument the producer intended.
* **Preview Duration Limits:** External third-party integrations are capped by Spotify API preview limits (30s snippets).

### Opportunities (O)
* **Creator Economy Expansion:** Repositioning Spotify from a passive listener player to a creator-first workspace.
* **Monetization & Licensing Pathways:** Partnerships with rights management or automated licensing systems (similar to Tracklib) for sample clearances.
* **Deep Catalog Monetization:** Resurfacing dormant, non-charting back-catalogs to active producers.

### Threats (T)
* **Spotify Developer API Restrictions:** Recent platform policy changes restrict third-party audio analysis, ingestion, and feature extraction.
* **Copyright & Legal Sensitivities:** Record labels may resist features facilitating unlicensed sampling without built-in clearance mechanisms.
* **Market Incumbent Pivots:** Dedicated producer platforms (Splice, Tracklib) or AI search providers (Cyanite) expanding directly into consumer catalogs.