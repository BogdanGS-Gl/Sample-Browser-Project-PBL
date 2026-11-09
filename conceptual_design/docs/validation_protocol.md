# Sample Browser — Revised Problem, Solution, Hypotheses & Customer Validation Protocol

**Course:** FAF.PCAS25.1 (Problem-Based Learning) — Pre-Midterm 2 Alignment  
**Team 16:** Bogdan Glavan, Andrei Simon, Nikita Creciun, Leonid Tiscenco, Mihai-Constantin Sîrghii  
**Mentor:** Prof. Elena Graur  
**Date:** November 7, 2026  

---

## 1. Revised Problem Description & Formal Problem Statement

### 1.1. Problem Context & Who Experiences It
Independent music producers and beatmakers working in sample-based genres (hip-hop, boom-bap, lo-fi, electronic, neo-soul, experimental) rely on discovering short musical passages (typically 2 to 8 bars, or 4 to 30 seconds) inside existing recordings. According to Tracklib's Producer Survey ($N = 1,107$), aspiring producers (58%) and hobbyists (25%) make up the vast majority of creators, and per the UK Musicians' Census, over half (53%) sustain their livelihood through employment outside music. Because most independent producers create music in limited spare time, hours lost to repetitive manual searching directly reduce the time available for actual arrangement and sound design.

### 1.2. Core Structural Bottlenecks
While pre-curated loop libraries (e.g., Splice) offer isolated sounds, they suffer from severe **sample fatigue**—millions of creators draw from the same recognizable packs—and require paid subscriptions. Consequently, independent producers frequently turn to vast public streaming catalogs (primarily YouTube and discovery overlays such as Samplette.io) to dig for obscure, authentic recordings. However, digging across full-length recordings exposes two operational bottlenecks:

1. **Sub-Track Structural Blindness (The Whole-Track Metadata Bottleneck):**  
   Streaming platforms index recordings exclusively at the whole-track level (Title, Artist, Global Genre, Year). Yet a producer rarely samples an entire song; they look for a localized, **structurally isolated passage**—such as an unlayered 4-bar intro, a clean drum break, or a solo electric piano progression without vocals or heavy percussion bleeding over it. Without sub-track structural indexing, producers must manually click and scrub the playhead across dozens of 3-to-6 minute recordings just to check if a usable, isolated moment exists.
2. **Ambiguity of Unstructured Text Queries & Bookmarking Friction:**  
   When producers try to search for specific sounds using arbitrary text descriptions, subjective mood or texture keywords yield inconsistent results because listeners interpret free-form adjectives differently. Furthermore, when producers do stumble upon promising 10-second passages while digging online, standard browser bookmarks and YouTube playlists only save the whole video URL—forcing creators to re-scrub tracks weeks later to remember which exact timestamp or instrument caught their ear.

### 1.3. Formal Problem Statement
> *"Independent music producers digging for samples across public streaming catalogs (such as YouTube and Samplette) waste significant time manually scrubbing through full-length recordings, because existing platforms index metadata exclusively at the whole-track level and provide no visibility into where short, structurally isolated passages (such as vocal-free instrumental sections or clean drum breaks) occur within a song."*

---

## 2. Revised Solution Proposal

### 2.1. Core Concept & Legal/Technical Boundaries
**Sample Browser** is a web-based sub-track discovery and sample-bookmarking platform built on top of public streaming video via the **YouTube IFrame Player API**.  
To remain 100% compliant with YouTube Developer Policies (Section III.E) and eliminate media hosting costs:
* The platform **does not download, host, extract, cache, or algorithmically process audio/video streams** on backend servers.
* Our PostgreSQL database stores **only lightweight metadata pointers**: YouTube Video IDs, sub-track segment timestamps (`start_time`, `end_time`, constrained to 4–60 seconds), and structured passage tags submitted and curated by users.
* All playback happens strictly client-side inside the official embedded YouTube player using synchronized timestamp seeking (`player.seekTo(start_time)`) and automated interval looping.

### 2.2. Two-Tier Tagging Taxonomy (Resolving Tag Subjectivity)
To prevent database pollution and subjective disagreements over vague descriptions while still supporting expressive browsing, Sample Browser replaces arbitrary free-text input with a **Two-Tier Tagging System**:

1. **Tier 1 — Primary Preset Objective Tags (Mandatory, High Search Priority):**  
   Selected in 2–3 clicks from a strictly controlled, pre-written taxonomy describing verifiable musical facts about the timestamped segment:
   * **Isolation / Layering Status:** `[No Vocals]`, `[No Drums / Melodic Only]`, `[Isolated Drum Break]`, `[Solo Instrument]`, `[Vocal Phrase / Acapella]`
   * **Instrumentation Present:** `[Electric Piano / Rhodes]`, `[Acoustic Piano]`, `[Guitar]`, `[Bass]`, `[Brass / Sax]`, `[Flute / Winds]`, `[Strings]`, `[Synth / Pad]`, `[Percussion / Drums]`
   * **Structural Section / Function:** `[Intro]`, `[Break / Bridge]`, `[Solo Section]`, `[Outro]`, `[Chord Loop]`, `[One-Shot / Hit]`
2. **Tier 2 — Secondary Contextual Tags (Optional, Lower Search Priority, Moderated):**  
   Curated descriptor chips for style/texture (inspired by RateYourMusic and Splice categories, e.g., `[Lo-Fi / Dusty]`, `[Syncopated / Swing]`, `[Jazz-Fusion]`, `[Dark / Minor]`).
   * Secondary tags are visually collapsed so they never clutter the primary interface.
   * Because any tag in Sample Browser is paired with **instant audio playback of the exact timestamped segment**, any subjective ambiguity is immediately resolved by auditioning the 10-second loop in one click.

### 2.3. Core User Workflows (Search, Berrypicking & Personal Crates)
1. **Direct Passage Auditioning & Auto-Loop:**  
   When a track loads, its timeline displays highlighted segment markers (`0:00–0:12 [Intro | Rhodes | No Drums]`). Clicking a marker jumps the embedded player straight to `start_time` and loops the passage until `end_time`.
2. **Seed-Passage ("Berrypicking") Recommendations:**  
   Rather than forcing users to invent text queries from scratch, a producer listening to a highlighted segment can select the tags present on that segment (e.g., `[Guitar] + [No Vocals] + [Break]`) and immediately receive a feed of **specific segments inside other songs** that share those exact preset tags—jumping straight to the matching timestamp in the next track.
3. **Personal Cloud Crates & Community Tagging:**  
   While crate-digging, producers can mark `Start / End` timestamps on any YouTube track, attach preset tags, and save the segment into their **Personal Cloud Crate** (solving their own bookmarking chaos without downloading gigabytes of full songs). Saved segments can be kept private or published to the community catalog with contributor attribution and moderation rules.

### 2.4. Updated Value Proposition Canvas (VPC)

| Customer Profile (Independent Music Producer) | Value Map (Sample Browser) |
| :--- | :--- |
| **Customer Jobs:**<br>• Digging across full-length recordings on YouTube/Samplette for unique sample material.<br>• Locating clean, unlayered 4–8 bar sections (breaks, intros, solos) suitable for chopping.<br>• Organizing and revisiting candidate sample moments discovered during digging sessions. | **Products & Services:**<br>• Web-based sub-track passage browser interfacing with YouTube IFrame API.<br>• Two-Tier Tagging System (Objective Preset Structural/Instrument tags + Secondary descriptors).<br>• Timestamped Personal Cloud Crates and seed-passage recommendation feed. |
| **Pains:**<br>• Wasting time manually scrubbing through 5-minute tracks whose sections don't match search goals.<br>• Losing track of exact timestamps and instruments inside bookmarked YouTube videos or playlists.<br>• Sample fatigue and subscription costs of overused commercial loop packs (Splice). | **Pain Relievers:**<br>• One-click playhead jumping (`seekTo`) and auto-looping of pre-marked 4–30s segments.<br>• Preset `[No Drums]`, `[No Vocals]`, and `[Solo Instrument]` tags exposing clean sections instantly.<br>• Cloud timestamp bookmarking that saves the exact interval and instrument notes without local disk clutter. |
| **Gains:**<br>• Discovering obscure, authentic musical passages faster.<br>• Smooth "berrypicking" navigation from one inspiring segment directly to similar segments in other songs.<br>• Instant audio verification of whether a tagged passage fits the current beat idea. | **Gain Creators:**<br>• Tag-intersection recommendations linking directly to sub-track cue points across songs.<br>• Immediate audio context alongside tags to eliminate descriptive ambiguity.<br>• Zero-cost web access over public streaming links without hosting or downloading files. |

### 2.5. Single-Sentence Value Proposition
> *"For independent music producers who lose time scrubbing through full-length tracks on YouTube to find usable sample sections, Sample Browser is a passage-level discovery and bookmarking platform that connects creators directly to timestamped, auto-looped musical intervals categorized by objective structural and instrumental preset tags."*

---

## 3. Customer Validation Hypotheses (Midterm 2)

All four hypotheses are formulated around **observable user behaviors, workflow pains, and real preferences** so that they can be directly confirmed or refuted through qualitative interviews (prior to building the final software).

| ID | Category | Hypothesis Statement | Validation Criteria (Confirmed If...) | Invalidation Criteria & Pivot Trigger (Refuted If...) |
| :--- | :--- | :--- | :--- | :--- |
| **H1** | **Problem Hypothesis**<br>*(Sub-Track Scrubbing & Isolation Friction)* | When hunting for samples in full-length recordings (e.g., on YouTube or Samplette), producers spend substantial time listening to and manually scrubbing through songs whose sections do not match their structural goals (such as finding a clean instrumental passage without vocals or heavy drums), frequently abandoning otherwise promising tracks. | $\ge 60\%$ of interviewed sampling producers describe manual playhead scrubbing and the lack of clean/isolated sections as a recurring reason for slow digging sessions or abandoning candidate songs. | Producers report that finding the right timestamp inside a song takes negligible effort, or that they simply grab any layered section and rely on DAW AI stem-separation without caring about clean sections. |
| **H2** | **Search & Tagging Hypothesis**<br>*(Preset Objective Tags + Audio Context & Berrypicking)* | Producers rely primarily on objective categories (instruments, section type/breaks, tempo) while distrusting standalone subjective mood/texture tags—and find it easier to discover samples by branching out from the tags of a specific audio segment they are currently hearing (*berrypicking*) rather than inventing text queries from scratch. | Producers confirm they prioritize instrument/structural filters, complain that vague mood/vibe tags on existing platforms are unreliable without immediate audio preview, and naturally search by following chains of related songs/samples. | Producers report that free-form text search or random browsing without tags is completely sufficient for their workflow. |
| **H3** | **Curation & Contribution Hypothesis**<br>*(Timestamp Bookmarking vs. Gatekeeping)* | Producers who save candidate songs online struggle to keep track of specific sub-track timestamps and reasons for saving them, and are willing to tag and share song sections using fast preset categories as part of organizing their own sample library (rather than keeping all discovered sources strictly private). | Producers confirm they currently save links/playlists/files in disorganized ways, want sub-track timestamp notes, and share (or are open to sharing) sample sources because originality lies in *how* a sample is flipped rather than hiding the source song. | **Contingency Pivot Trigger:** If producers strongly want timestamp bookmarking & tagging *for themselves* but refuse to share tags publicly (gatekeeping), we execute a planned soft pivot to a **Personal Crate-Digging & Bookmarking Workspace** (like a tag-powered *chop-stop / sampledigging* alternative). |
| **H4** | **Target Segment Hypothesis**<br>*(Unlicensed Public Catalogs vs. Curated Libraries)* | Small-scale and independent producers do not sample purely for commercial releases and actively prefer digging in unlicensed public full-track catalogs (YouTube, Samplette) over paid pre-curated libraries (Splice, Tracklib) due to cost, catalog variety, and commercial loop fatigue. | Independent/hobbyist respondents confirm they regularly sample from YouTube/public streams for practice, beat battles, or underground releases without being deterred by sample clearance. | Respondents exclusively use royalty-free packs (Splice) and refuse to touch YouTube recordings due to copyright fear. |

---

## 4. Customer Interview Questions & Traceability Guide

**Target Duration:** 15–20 minutes per interview  
**Format:** Semi-structured voice/video call (Discord / Telegram / Zoom) or in-person session  
**Methodological Rule (*The Mom Test*):** Ask about **past behaviors and concrete recent episodes** first. Do NOT pitch our solution at the start of the call.

### Block 1: Producer Background & Screening (Context)
1. **[BK]** How would you describe the main genres of music you make, and what inspires your production style?
2. **[BK + H4]** Do you currently release music under an alias, collaborate with artists, or make beats primarily for personal enjoyment, practice, or underground communities?
3. **[Screening]** When making a track, how much do you rely on sampling existing recordings versus composing from scratch with virtual instruments (VSTs) or hardware? Roughly how many samples did you use on your last sampled track, and why did you choose them?
   * *(If respondent rarely/never samples: ask briefly what holds them back from sampling—time, difficulty, or stylistic preference—and conclude or treat as control group).*

### Block 2: Unlicensed Song Digging vs. Pre-Curated Libraries (Testing H4)
4. **[H4]** Do you mostly use pre-curated royalty-free sample libraries (like Splice or Looperman), or do you prefer sampling directly from original full-length songs (on YouTube, Samplette, Tracklib, vinyl)?
   * *Follow-up 4a:* What makes you choose one over the other—is it convenience, cost, sound uniqueness/fatigue, or something else?
   * *Follow-up 4b:* Which free or paid tools/sites do you use most often to find samples? Has sample licensing/copyright ever been an issue for the music you make, or does it not affect your releases?

### Block 3: Last Concrete Digging Session & Inside-Track Scrubbing (Testing H1)
5. **[H1]** Think about the **last specific time** you searched for a sample inside full-length songs online. What kind of sound or musical part were you looking for, and how long did you spend searching before you felt you spent enough time?
   * *Follow-up 5a:* Roughly how many tracks did you click through and preview before you found one you actually used?
6. **[H1]** When you click on an unfamiliar 3-to-6 minute song on YouTube or Samplette, how do you actually scan through the track to find the exact 4-to-8 bar section you want?
   * *Follow-up 6a:* Have you recently found a song with a great sound or instrument, but ended up skipping it because the section wasn't usable? What ruined that section for you (e.g., vocals/drums overlapping, tempo shifts)?
   * *Follow-up 6b:* Do you specifically hunt for clean, isolated sections in a song (like an intro, break, or solo), or do you use AI stem separation in your DAW on any part of the song? Why?

### Block 4: Tag Reliability, Audio Context & Berrypicking (Testing H2)
7. **[H2]** What was the last sound you searched for using text keywords or category filters, and how did you describe it? How often do you find a good sample from a single text search query?
   * *Follow-up 7a:* When browsing platforms that use tags or filters (like Splice, Tracklib, Samplette, or RYM), which categories do you actually trust and rely on (e.g., instruments, BPM, song sections), and which tags do you avoid or find confusing/inaccurate (e.g., mood or texture words)?
8. **[H2]** Think of the last time you needed another sample to go with one you already had (or wanted to find more samples similar to one you just heard). How did you go about finding it?
   * *Probe (only if it doesn't come up):* Did anything about the first sample guide where or how you looked next?
   * *Follow-up 8a:* Think of the last time you picked a sound or a song because of how it was labelled—a mood, a genre, or an instrument. Did it match what you expected once you heard it?

### Block 5: Personal Sample Storage, Timestamps & Community Contribution (Testing H3)
9. **[H3]** Do you keep a personal library, playlist, or folder where you save songs or samples you discovered for future projects? Do you store them locally on your drive or online (e.g., YouTube playlists, bookmarks, sites like *chop-stop* / *sampledigging*)?
   * *Follow-up 9a:* How do you categorize what you save? When you come back to a saved full-length song weeks later, how do you remember **which exact timestamp** had the sample and **why** you saved it?
10. **[H3]** Have you ever shared your sample finds, digging playlists, or song sources with other producers, or do you prefer to keep your found songs private?
    * *Follow-up 10a (Past Gatekeeping Check):* Have you ever found a rare song or sample and intentionally avoided telling anyone its title until you finished and released your beat, so nobody else would flip it first?
    * *Follow-up 10b:* If you had a fast way to bookmark exact song sections (`Start–End` timestamps) with preset instrument/section tags for your own online library while digging, would you leave those tagged sections public to help build a community catalog (with credit on your profile), or keep them private? Why?

---

## 5. Interview Methodology, Recruitment & Preparation Plan

### 5.1. Target Sample & Recruitment Channels
* **Target Sample Size:** **$N \approx 20$ video interviews** (~4 interviews conducted per team member), backed up by a **supplementary Google Forms quantitative survey** to cross-validate findings across a broader pool of music makers.
* **Language & Eligibility:** Interviews may be conducted in **any language** (English, Romanian, Russian) with music artists and producers (including personal acquaintances/peers, provided strict neutrality and non-biased *Mom Test* questioning are maintained).
* **Inclusion Criteria:** Music artists, independent beatmakers, and music producers (hobbyists, aspiring career producers, and sound designers) working in DAWs (FL Studio, Ableton Live, Logic Pro, MPC, etc.).
* **Where We Will Recruit Interviewees (4 Channels):**
  1. **Known Contacts, Local University & Chișinău Artist Network (5–6 participants):** Unbiased interviews with fellow UTM/FCIM student producers, local Chișinău musicians, and acquaintances who make music (conducted via video call or in person).
  2. **Direct Instagram Outreach ("Shot in the Dark" DMs to Independent Music Artists & Beatmakers) (5–6 participants):** Reaching out via Instagram DMs to independent beatmakers, underground artists, and reel creators posting studio/sampling clips.
  3. **Dedicated Sampling & Beat-Battle Discord Communities (5–6 participants):** Active producers in *Samplette / Crate-Digging Discord channels*, *Kenny Beats / Beat Battle communities*, *r/makinghiphop Discord*, *Lo-Fi Hip-Hop producer servers*, and *Stones Throw Beat Battles (STBB)*.
  4. **Small YouTube / SoundCloud "Sample Flip" Creators & Regional Telegram Producer Chats (3–4 participants):** Producers actively posting sample-based beats (`"samplette flip"`, `"youtube sample beat"`) who list their Discord, Instagram, or Telegram handles.

### 5.2. Standard Outreach Message Template
> *"Hey [Name]! Listened to your recent beat in [Server/Channel] — really liked your sample selection. I’m a computer science student working with a small university team researching how independent producers dig for samples and navigate full songs online. We’re not selling anything — just doing quick 15-minute voice chats on Discord with producers to understand real crate-digging habits and frustrations. Would you be open to a quick 15-min chat today or tomorrow?"*

### 5.3. Interview Execution & Documentation Protocol
1. **Team Roles per Call:**
   * **Lead Interviewer:** Conducts the conversation naturally, asks follow-up "Why?" questions, avoids leading the witness.
   * **Note-Taker / Scribe:** Records timestamps, writes down verbatim quotes mapped to H1–H4, and captures required visual evidence.
2. **Evidence Collection (Per PBL Guideline Requirements):**
   * Request explicit verbal permission at the start of the call to record audio (for accurate quote transcription) and take a screenshot of the call window (or photo if in-person) as empirical proof for the Midterm 2 report.
3. **Post-Interview Coding Sheet:**
   * Immediately after each interview, fill out a standardized 1-page summary card recording: Participant ID, Producer Segment, DAW/Genres, Key Quotes for H1–H4, and Hypothesis Status (`Validated` / `Partially Validated` / `Invalidated`).
