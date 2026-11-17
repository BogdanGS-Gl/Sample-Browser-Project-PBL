# Better Spotify / Sample Browser (CrateTrack): Presentation Pitch Deck

**Document:** Pitch & Defense Deck (11 Slides: 9 Core + 2 Appendix)  
**Event:** Midterm 2 Architecture & Customer Discovery Defense (7-Minute Pitch)  
**Course:** FAF.PCAS25.1 · Conceptual Design of a Software Application (Problem-Based Learning)  
**Institution:** Technical University of Moldova (UTM), Faculty of Computers, Informatics and Microelectronics (FCIM)  
**Supervision:** Mentor Prof. Elena Graur  
**Team 16:** Bogdan Glavan (FAF-261), Andrei Simon (FAF-261), Nikita Creciun (FAF-263), Leonid Tiscenco (FAF-263), Mihai-Constantin Sîrghii (FAF-262)  

---

## Slide 01: Title & Overview
* **Institution:** Technical University of Moldova · FCIM · FAF.PCAS25.1
* **Event:** Midterm 2 Architecture & Customer Discovery Defense · 7-Min Pitch
* **Project Title:** Sample Browser (CrateTrack)
* **Subtitle:** Granular Audio Passage Discovery for Independent Music Creators
* **Core Theme:** Problem-Based Learning: Transitioning from Consumer Audio Streaming to a Compliance-First Sample Discovery Workspace
* **Team 16 (FAF Students):**
  * Bogdan Glavan (FAF-261)
  * Andrei Simon (FAF-261)
  * Nikita Creciun (FAF-263)
  * Leonid Tiscenco (FAF-263)
  * Mihai-Constantin Sîrghii (FAF-262)
* **Project Supervision:** Prof. Elena Graur (Faculty of Computers, Informatics and Microelectronics, Department of Software Engineering and Automatics · Chișinău, 2026)

## Slide 02: Introduction & Context — The Reality and Friction of Modern Audio Sampling
* **Category Tag:** 01. INTRODUCTION & CONTEXT
* **Headline:** The Reality and Friction of Modern Audio Sampling
* **Core Concept:**
  * **Sampling Definition:** Reusing a localized portion of an existing sound recording in a new musical work.
  * Producers hunt for localized 2–8 bar passages (4–30s) — drum breaks, melodic motifs, isolated phrases — not whole songs.
* **Production Context:** Modern bedroom workstations; 53% of sample-based creators work alongside day jobs, making studio time scarce.
* **Key Industry Metrics:**
  * **17%:** Billboard Hot 100 hits rely on samples (Tracklib State of Sampling report).
  * **250M+:** Streaming catalog tracks indexed exclusively as whole-track monoliths.

## Slide 03: Domain Analysis & Existing Tools — Three Existing Paradigms vs. Granular Passage Discovery
* **Category Tag:** 02. DOMAIN ANALYSIS & EXISTING TOOLS
* **Headline:** Three Existing Paradigms vs. Granular Passage Discovery
* **Existing Market Paradigms:**
  * **Splice (Pre-Cut Library):** Standardized loops & one-shots; risk of sterile, identical beats across hip-hop/pop; no whole-track context.
  * **Samplette.io (Full-Track Digging):** Random discovery over YouTube via Discogs metadata; no intra-track passage indexing, requiring manual scrubbing.
  * **Tracklib (Pre-Cleared Songs):** Licensed catalog with stem isolation & loop tools; expensive, high clearance barrier for indie beatmakers.
* **Sample Browser (CrateTrack) Positioning:** Sub-track passage retrieval across public catalogs with zero media storage or licensing lock-in.

## Slide 04: Problem Analysis & Strategic Pivot — The Granularity Gap & The Compliance Pivot
* **Category Tag:** 03. PROBLEM ANALYSIS & PIVOT
* **Headline:** The Granularity Gap & The Compliance Pivot
* **The Core Friction (Dual Bottlenecks):**
  * **Whole-Track Indexing:** Streaming search returns 4-minute songs, leaving 2–8 bar passages hidden.
  * **URL Bookmark Friction:** Producers accumulate disorganized lists of YouTube links with lost timestamps and forgotten contexts.
* **Timeline Comparison:**
  * **Current Scrubbing Loop:** Full Track Monolith → Manual Scrubbing (10–30 min) → Creative Fatigue & Flow Broken.
  * **Proposed Passage Workflow:** Objective Preset Filter → Jump to Cue Point (`seekTo`) → Seamless Loop Audition (Immediate Flow).
* **PBL Strategic Pivot (Nov 7 Decision):**
  * **Initial Plan:** Server-side Essentia MIR analysis & consumer streaming integration.
  * **Pivot Triggers:** YouTube TOS Section III.E explicitly forbids raw audio downloading and scraping; mentor guidance on legal and technical compliance.
  * **Post-Pivot Architecture:** 100% legal client-side YouTube IFrame player + community-curated Two-Tier taxonomy.

## Slide 05: Target Group & User Personas — Two Creator Personas & Empirical Validation Plan
* **Category Tag:** 04. TARGET GROUP & USER PERSONAS
* **Headline:** Two Creator Personas & Empirical Validation Plan
* **Persona 1: Alex Miller (Aspiring Producer | Age 22, Bedroom Beatmaker — FL Studio)**
  * **Available Time:** 8–12 hours/week creative window outside day job.
  * **Core Friction:** Loses creative momentum scrubbing 5-minute jazz tracks to find isolated drum breaks or unlayered Rhodes chords.
  * **Goal:** Needs quick acoustic cues to match rhythmic textures with existing project stems (`Found vocal → needs matching guitar`).
* **Persona 2: Annie Lee (Hobbyist Producer | Age 20, Student & Lo-Fi Beatmaker — Ableton)**
  * **Available Time:** Sporadic, exploratory evening studio sessions.
  * **Core Friction:** Disillusioned by overused commercial sample packs; bookmarks YouTube links but forgets specific timestamps.
  * **Goal:** Wants serendipitous crate-digging through vintage recordings with zero file clutter (`Found interesting sound → cannot find similar passages`).
* **Target Market Composition (Tracklib Survey, N ≈ 1,000):**
  * **58%:** Aspiring producers aiming for careers (Alex).
  * **25%:** Hobbyists and casual creators (Annie).
  * **10%:** Full-time professional producers.
  * **7%:** Beginners.

## Slide 06: The Solution — Two-Tier Taxonomy & Granular Passage Audition
* **Category Tag:** 05. THE SOLUTION
* **Headline:** Two-Tier Taxonomy & Granular Passage Audition
* **Value Proposition:** A passage-indexed discovery platform connecting independent producers directly to timestamped musical sections across public streaming catalogs.
* **Core Product Capabilities:**
  1. **Two-Tier Objective Taxonomy:**
     * *Tier 1 (Functional Musical Role):* `[Drum Break]`, `[Melodic Loop]`, `[Bassline]`, `[Vocal Hook]`.
     * *Tier 2 (Structural Acoustic Facts):* `[Solo Instrument]`, `[No Drums]`, `[Clean Break]`, `[Acapella]`.
     * Eliminates subjective vocabulary gaps using verifiable musical facts, confirmed via 1-click audio preview.
  2. **Dynamic Berrypicking Feed:**
     * *Bates' Berrypicking Model:* Producers iteratively refine queries as they hear new cues without restarting their search session.
     * *Direct Cue + Loop:* Instant playhead jump via YouTube Player API (`seekTo`) and seamless auto-loop playback of the selected 4–30s passage.

## Slide 07: System Architecture & Compliance — Three-Tier Client-Side Pointer Architecture
* **Category Tag:** 05. SYSTEM ARCHITECTURE & COMPLIANCE
* **Headline:** Three-Tier Client-Side Pointer Architecture
* **Interaction Pipeline & Core Tiers:**
  * **Client-Side Web UI (React/TypeScript):** Segmented waveform & cue visualizer, objective tag multi-selector, auto-loop controller.
  * **YouTube IFrame API:** Audio rendered entirely client-side via Google servers (`player.seekTo(start)`).
  * **Metadata Backend (Node.js / Express):** REST API managing passage pointers (Video ID, `start_sec`, `end_sec`, tags, community quality votes).
  * **PostgreSQL Database:** Relational storage for catalog pointers, user crates, and quality scoring.
* **Strict Legal & Technical Compliance:**
  * **YouTube TOS Section III.E Compliance:** Zero audio downloads, zero stream caching, zero server-side audio ingestion.
  * **Serverless Media Overhead:** Zero hosting costs, zero transcoding bandwidth, zero copyright infringement liabilities.

## Slide 08: Comparative Analysis & Strategic SWOT Overview
* **Category Tag:** 06. COMPARATIVE ANALYSIS & SWOT
* **Headline:** Competitive Positioning & Strategic SWOT Overview
* **Competitor Positioning:**
  * **Splice:** Curated loop packs (isolated pre-cut samples).
  * **Samplette:** YouTube digging based on Discogs metadata (full-track only).
  * **Tracklib:** Pre-cleared master recording catalog + basic looping.
  * **Sononym:** Local disk sample organizer (requires local files).
  * **Cyanite.ai:** Enterprise B2B sync intelligence (audio analysis API).
  * **Sample Browser:** Sub-track passage indexing + zero-download IFrame preview.
* **Strategic SWOT Overview:**
  * **Strengths (S):** Granular sub-track indexing, direct IFrame cueing, zero audio storage overhead.
  * **Weaknesses (W):** Cold-start community catalog, reliance on third-party streams, IFrame seek precision limit.
  * **Opportunities (O):** Overcoming Splice sample pack fatigue, personal Smart Crates digging workspace, browser VST sidecar.
  * **Threats (T):** YouTube embed policy shifts, video takedowns / broken links, competitor feature replication.

## Slide 09: Customer Discovery & Validation Roadmap
* **Category Tag:** 07. CUSTOMER DISCOVERY & VALIDATION ROADMAP
* **Headline:** Customer Discovery ($N \approx 20$) & Engineering Roadmap
* **4 Validation Hypotheses (Investigated in Midterm 2):**
  * **H1 (Scrubbing Friction):** $\ge 70\%$ of producers report scrubbing full tracks as a primary friction point.
  * **H2 (Tool Gap):** Existing market tools fail for intra-track acoustic passage discovery across public catalogs.
  * **H3 (Community Sharing):** Producers are willing to tag and share sample timestamps with other creators.
  * **H4 (Contingency Pivot):** If $H3$ fails due to producer gatekeeping, pivot product into a *Personal Crate-Digging Workspace* (Smart Crates).
* **Empirical Validation Plan ($N \approx 20$):**
  * **Target Channels:** Reddit (`r/makinghiphop`, `r/edmproduction`), Discord producer communities, Soundbetter, Telegram producer groups.
  * **Methodology:** Semi-structured qualitative interviews following The Mom Test principles (past behaviors, not hypothetical praise).
* **3-Stage Engineering Roadmap:**
  * **Stage 1: Validate & Conceptualize (Midterm 1):** Problem discovery and conceptual design (Completed).
  * **Stage 2: Customer Validation & Architecture (Midterm 2):** $N \approx 20$ producer interviews, DVC data setup, and client-side pointer architecture (Current).
  * **Stage 3: Interactive Prototype & Evaluation (Exam Milestone):** Functional web prototype, usability testing, and passage retrieval speed evaluation.

## Slide 10 (Appendix): Strategic SWOT Analysis (Detailed Reference Matrix)
* **Category Tag:** APPENDIX · Q&A REFERENCE
* **Headline:** Strategic SWOT Analysis (Report Section 2.4, Table 3)
* **Detailed Breakdown:**
  * **Strengths (S):**
    * *Sub-Track Granularity:* Indexes at 2–16 bar interval level, designed to reduce manual scrubbing.
    * *Two-Tier Objective Taxonomy:* Eliminates subjective vocabulary gaps using objective musical facts verified by audio preview.
    * *Zero Audio Hosting:* 100% compliant with YouTube API Section III.E; zero media storage overhead.
    * *Contextual Playback:* Audition passages within original arrangements and dynamics.
  * **Weaknesses (W):**
    * *Cold-Start Catalog:* Early platform utility depends on seed curation and initial community indexing.
    * *Third-Party Stream Reliance:* Vulnerable to YouTube video takedowns, regional geo-blocks, or link rot.
    * *IFrame Seek Precision:* Dependent on YouTube player API responsiveness (0.1–0.3s variance).
    * *No Direct Audio Export:* Users must acquire source audio externally under API terms.
  * **Opportunities (O):**
    * *Sample Pack Fatigue:* Growing producer backlash against overused commercial sample libraries (Splice).
    * *Personal Digging Workspace (Smart Crates):* Contingency pivot to private crate organization if gatekeeping limits sharing.
    * *DAW Integration:* Future browser extension or VST/AU sidecar directly inside Ableton/FL Studio.
    * *Archival Partnerships:* Partnership pathways with public domain/archival labels to index catalog gems.
  * **Threats (T):**
    * *API Policy Lockdowns:* Risk of YouTube restricting embedded player controls or ad-free playback.
    * *Incumbent Expansion:* Established platforms (Samplette, Tracklib) adding segment-level tagging.
    * *Producer Gatekeeping:* Cultural reluctance to share sample sources publicly (mitigated by $H4$).

## Slide 11 (Appendix): Formal Problem Statement & Evaluation Matrix
* **Category Tag:** APPENDIX · Q&A REFERENCE
* **Headline:** Formal Problem Statement & Evaluation Matrix
* **Verbatim Formal Problem Statement (Report Section 2.1 & Pivot Agreement):**
  > "Independent music producers lack an efficient way to discover and locate specific musical passages within full-length catalog recordings based on acoustic references, because contemporary streaming search interfaces index music exclusively at the whole-track metadata level, forcing producers into tedious, manual scrubbing that disrupts the creative workflow."
* **Comparative Tool Matrix (Report Table 2):**

| Platform | Index Granularity | Query Paradigm | Catalog Type | Storage/Legal Overhead | Workflow Role |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Splice** | Isolated samples | Text / Tags | Curated proprietary | High (Full audio hosting) | Ready-made sound packs |
| **Samplette** | Full-track | Random / Discogs | Public (YouTube) | Low (IFrame embed) | Full-record digging |
| **Tracklib** | Track + Bar loops | Metadata / Mood | Pre-cleared master | High (Licensed catalog) | Licensing marketplace |
| **Sononym** | Local sample files | Audio similarity | Local user disk | None (Local files) | Sample library organizer |
| **Cyanite.ai** | Track & Segment | Audio similarity | Enterprise B2B | Cloud API | Sync intelligence API |
| **Sample Browser** | **Passage (4–30s)** | **Two-Tier Presets** | **Public (YouTube)** | **Zero (Client IFrame)** | **Granular passage discovery** |
