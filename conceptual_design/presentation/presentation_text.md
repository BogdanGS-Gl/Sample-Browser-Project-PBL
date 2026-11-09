# Better Spotify / Sample Browser: Presentation Pitch Deck

**Document:** Pitch & Defense Deck (11 Slides: 9 Core + 2 Appendix)  
**Event:** Midterm 1 Defense (7-Minute Pitch)  
**Course:** FAF.PCAS25.1 · Conceptual Design of a Software Application (Problem-Based Learning)  
**Institution:** Technical University of Moldova (UTM), Faculty of Computers, Informatics and Microelectronics (FCIM)  
**Supervision:** Mentor Prof. Elena Graur  
**Team 16:** Bogdan Glavan (FAF-261), Andrei Simon (FAF-261), Nikita Creciun (FAF-263), Leonid Tiscenco (FAF-263), Mihai-Constantin Sîrghii (FAF-262)  

---

## Slide 01: Title & Overview
* **Institution:** Technical University of Moldova · FCIM · FAF.PCAS25.1
* **Event:** Midterm 1 Defense · 7-Min Pitch
* **Project Title:** Better Spotify / Sample Browser
* **Subtitle:** Granular Audio Passage Discovery for Independent Music Producers
* **Core Theme:** Problem-Based Learning Journey: Evolving from a Passive Playback Concept into an Active Creator Workspace
* **Team 16 (FAF Students):**
  * Bogdan Glavan (FAF-261)
  * Andrei Simon (FAF-261)
  * Nikita Creciun (FAF-263)
  * Leonid Tiscenco (FAF-263)
  * Mihai-Constantin Sîrghii (FAF-262)
* **Project Supervision:** Prof. Elena Graur (Faculty of Computers, Informatics and Microelectronics, Department of Software Engineering and Automatics · Chișinău, 2026)

## Slide 02: Introduction & Context — The Environment and Reality of Audio Sampling
* **Category Tag:** 01. INTRODUCTION & CONTEXT
* **Headline:** The Environment and Reality of Audio Sampling
* **Core Concept:**
  * **Sampling Definition:** Reusing a portion of an existing recording in a new composition.
  * Producers hunt for localized 2–8 bar passages (4–30s), not whole songs.
* **Production Context:** Bedroom workstation with DAW, keyboard, and monitoring.
* **Key Industry Metrics:**
  * **17%:** Billboard Hot 100 hits rely on samples (Tracklib State of Sampling report).
  * **250M+:** Streaming catalog tracks indexed almost exclusively at whole-track level.

## Slide 03: Domain Analysis & Existing Tools — Three Existing Paradigms vs. Passage Discovery
* **Category Tag:** 02. DOMAIN ANALYSIS & EXISTING TOOLS
* **Headline:** Three Existing Paradigms vs. Passage Discovery
* **Existing Market Paradigms:**
  * **Splice (Ready-Made Samples):** Catalog of pre-cut loops & one-shots; prepared library workflow. Overused, lacks unique context.
  * **Samplette.io (Discover Full Recordings):** Randomized YouTube digging via Discogs; whole-track search only. Unstructured serendipity without targeted passage retrieval.
  * **Tracklib (Licensed Catalog + Tools):** Pre-cleared songs with stem isolation and bar-looping tools. High clearance friction for indie creators.
* **Sample Browser Positioning:** Discover and compare specific passages across full-length catalog recordings.

## Slide 04: Problem Analysis & Strategic Workflow Pivot
* **Category Tag:** 03. PROBLEM ANALYSIS & PIVOT
* **Headline:** The Core Problem & Strategic Workflow Pivot
* **The Core Friction:**
  * Producers lack an efficient way to find specific passages inside full recordings.
  * Streaming catalogs index music as 4-minute monoliths; producers search by sound timbre for 2–8 bar passages (e.g. `0:00 Break (8s) [Dusty, Unlayered]`, `Rhodes Chords (16s) [Warm, Tape Rhodes]`, `4:00 End`).
* **Current Scrubbing Loop:**
  * Full Track Monolith → Manual Scrubbing → Flow Lost / Creative Fatigue.
* **Proposed Passage Workflow:**
  * Describe Sound → Find Exact Timestamped Passage → Jump to Cue & Audition Loop.
* **PBL Strategic Pivot:**
  * Initial Concept: Consumer streaming overlay / alternative Spotify shell.
  * Pivot Triggers: Spotify 2024–2026 API locks (audio analysis endpoints deprecated, developer quota caps) + mentor feedback on unfeasibility.
  * New Direction: Creator-focused passage search connecting directly to public embedded audio via YouTube IFrame API.

## Slide 05: Target Group & User Personas — Two Illustrative Creator Personas
* **Category Tag:** 04. TARGET GROUP & USER PERSONAS
* **Headline:** Two Illustrative Creator Personas (Validation Planned)
* **Persona 1: Alex Miller (Aspiring Producer | Age 22)**
  * **Role:** Bedroom beatmaker / producer (FL Studio).
  * **Available Time:** 8–12 hours/week creative time alongside outside job.
  * **Core Friction:** Scrubbing full-length tracks for drum breaks and melodies ruins creative momentum.
  * **Scenario:** *Found vocal → needs matching guitar.*
* **Persona 2: Annie Lee (Hobbyist Producer | Age 20)**
  * **Role:** Student sound designer / indie game composer.
  * **Available Time:** Exploratory / sporadic studio sessions.
  * **Core Friction:** Fatigue from generic, sterile commercial sample packs.
  * **Scenario:** *Found interesting sound → cannot find similar passages.*
* **Target Market Distribution (Tracklib Survey, N ≈ 1,000):**
  * **58%:** Aspiring producers aiming for careers (Alex).
  * **25%:** Hobbyists and casual creators (Annie).
  * **10%:** Full-time professional producers.
  * **7%:** Beginners.

## Slide 06: The Solution — Find the Passage, Not Just the Song
* **Category Tag:** 05. THE SOLUTION
* **Headline:** Find the passage, not just the song.
* **Value Proposition:** A passage-indexed discovery platform connecting independent producers directly to timestamped musical sections across public streaming catalogs.
* **Core Product Capabilities:**
  1. **Acoustic Filters:** Multi-tag acoustic search (instrument, texture, timbre, dynamic context).
  2. **Passage Results:** Candidate list of timestamped segments across diverse songs matching the selected tags.
  3. **Direct Cue + Loop:** Instant playhead jump via YouTube Player API (`seekTo`) and seamless auto-loop playback of the selected 4–30s passage.

## Slide 07: System Architecture — Interaction Pipeline & Technical Scope
* **Category Tag:** 05. SYSTEM ARCHITECTURE
* **Headline:** Interaction Pipeline & Technical Scope
* **Interaction Pipeline:**
  * `Web UI` (Client Interface) → `Metadata Query` → `Timestamp Resolution` → `YouTube Embedded Player (IFrame)`.
* **System Components:**
  * **Client Frontend:** Segmented waveform visualizer, acoustic filter selector, loop controls.
  * **Metadata Backend:** PostgreSQL database storing video links, song titles, artists, segment start/end timestamps, and tag hierarchies.
  * **Playback Engine:** Third-party streaming via YouTube IFrame API (zero media hosting costs, copyright compliant playback).
* **Implementation Status:**
  * *Current (Midterm 1):* Curated acoustic tagging and timestamp metadata.
  * *Planned (Midterm 2):* Automated MIR indexing evaluation (Essentia timbral classifiers).
* **Technical Caveats & Boundary Limits:**
  * Server-side compliant audio ingestion for automated MIR remains an open research question.
  * No original audio hosting; users clear sampling rights independently.

## Slide 08: Comparative Analysis & Strategic SWOT Overview
* **Category Tag:** 06. COMPARATIVE ANALYSIS & SWOT
* **Headline:** Competitive Positioning & Strategic SWOT Overview
* **Competitor Positioning:**
  * **Splice:** Curated loop packs (isolated pre-cut samples).
  * **Samplette:** YouTube digging based on Discogs metadata (full-track only).
  * **Tracklib:** Pre-cleared master recording catalog + basic looping.
  * **Sononym:** Local disk sample organizer (requires local files).
  * **Cyanite.ai:** Enterprise B2B sync intelligence (audio analysis API).
  * **Sample Browser:** Cross-catalog passage-level retrieval and timestamp auditioning.
* **Strategic SWOT Overview:**
  * **Strengths (S):** Sub-track granularity, direct timestamp cueing, zero audio hosting overhead.
  * **Weaknesses (W):** Cold-start catalog challenge, third-party stream dependency, unresolved automated MIR ingest.
  * **Opportunities (O):** Overcoming commercial sample pack fatigue, future DAW plugin integration (VST/AU), label archival partnerships.
  * **Threats (T):** Streaming API shifts/restrictions, incumbent feature creep, sample clearance friction.

## Slide 09: Customer Validation, Business Model & Roadmap
* **Category Tag:** 07. CUSTOMER VALIDATION, BUSINESS MODEL & ROADMAP
* **Headline:** Engineering Roadmap & Validation Hypotheses
* **3-Stage Engineering Roadmap:**
  1. **Stage 1: Validate (Midterm 1–2):** 10–15 direct semi-structured interviews with bedroom producers investigating workflow friction and digging habits.
  2. **Stage 2: Prototype (Midterm 2):** Functional wireframing, UML structural/behavioral models, and interactive prototype with mock passage retrieval.
  3. **Stage 3: Evaluate (Exam Milestone):** Empirical evaluation of passage retrieval speed vs. traditional digging; measure reduction in manual scrubbing.
* **Research Hypotheses (To Investigate in M2):**
  * **H1 (Scrubbing Pain):** $\ge 70\%$ of producers report scrubbing full tracks as a primary friction point.
  * **H2 (Tool Gap):** Existing market tools fail for intra-track acoustic passage discovery.
  * **H3 (Time Target):** Passage-level cueing reduces discovery time by $\ge 50\%$.
* **Potential Business Model (To Be Validated):**
  * **Free Community Tier:** Web-based passage discovery, public tagging, basic loop preview.
  * **Pro Creator Tier:** Timbral MIR similarity matching, DAW marker exports (MIDI/cue points), unlimited crate saving.
* **Key Takeaway:** Sample Browser explores the missing link between discovering a recording and finding the exact passage worth using.

## Slide 10 (Appendix): Strategic SWOT Analysis (Detailed Reference Matrix)
* **Category Tag:** APPENDIX · Q&A REFERENCE
* **Headline:** Strategic SWOT Analysis (Report Section 2.4, Table 3)
* **Detailed Breakdown:**
  * **Strengths (S):**
    * *Sub-Track Granularity:* Indexes at 2–16 bar interval level, designed to reduce manual scrubbing.
    * *Explainable Discovery:* Transparent acoustic descriptors rather than opaque black-box recommendations.
    * *No Original Audio Hosting:* Uses compliant YouTube IFrame streaming without media storage overhead.
    * *Contextual Playback:* Audition passages within original arrangements and dynamics.
  * **Weaknesses (W):**
    * *Cold-Start Catalog Challenge:* Platform utility in early stages relies heavily on pre-tagged passage volume.
    * *Third-Party Dependency:* Vulnerable to YouTube video takedowns, regional geo-blocks, or API policy changes.
    * *No Direct Audio Export:* Users must acquire source audio externally under API terms.
  * **Opportunities (O):**
    * *Sample Pack Fatigue:* Producer backlash against overused commercial sample libraries (Splice).
    * *DAW Plugin Integration:* Potential to port interface into embedded VST/AU inside Ableton or FL Studio.
    * *Catalog Rights Monetization:* Partnership pathways with archival labels to monetize dormant back-catalogs.
  * **Threats (T):**
    * *API Policy Lockdowns:* Risk of streaming providers restricting embedded player functionality.
    * *Incumbent Expansion:* Established tools (Tracklib, Samplette) expanding into segment-level tagging.
    * *Copyright Uncertainties:* Legal clearance requirements for archival recordings in commercial releases.

## Slide 11 (Appendix): Formal Problem Statement & Comparative Tool Evaluation Matrix
* **Category Tag:** APPENDIX · Q&A REFERENCE
* **Headline:** Formal Problem Statement & Evaluation Matrix
* **Verbatim Formal Problem Statement (Report Section 2.1):**
  > "Independent music producers lack an efficient way to discover and locate specific musical passages within full-length catalog recordings based on acoustic references, because contemporary streaming search interfaces index music exclusively at the whole-track metadata level, forcing producers into tedious, manual scrubbing that disrupts the creative workflow."
* **Comparative Tool Matrix (Report Table 2):**

| Platform | Index Granularity | Query Paradigm | Catalog Type | Workflow Role |
| :--- | :--- | :--- | :--- | :--- |
| **Splice** | Isolated samples | Text / Metadata | Curated proprietary | Ready-made sound packs |
| **Samplette** | Full-track | Random / Discogs | Public (YouTube) | Full-record digging |
| **Tracklib** | Track + Bar loops | Metadata / Mood | Pre-cleared master | Licensing marketplace |
| **Sononym** | Local sample files | Audio similarity | Local user disk | Sample library organizer |
| **Cyanite.ai** | Track & Segment | Audio similarity | Enterprise B2B | Sync intelligence API |
| **Sample Browser** | **Passage (4–30s)** | **Acoustic descriptors** | **Public (YouTube)** | **Cross-catalog discovery** |
