# Better Spotify / Sample Browser: Granular Audio Passage Discovery for Independent Music Producers

**Academic Project Report — Midterm 1 & Midterm 2 Architecture**  
**Course:** FAF.PCAS25.1 · Conceptual Design of a Software Application (Problem-Based Learning)  
**Institution:** Technical University of Moldova (UTM), Faculty of Computers, Informatics and Microelectronics (FCIM), Department of Software Engineering and Automatics  
**Location & Date:** Chișinău, Fall 2026  

**Project Supervision:**  
* **Mentor:** Prof. Elena Graur  

**Team 16 (FAF Students):**  
* Bogdan Glavan (FAF-261)  
* Andrei Simon (FAF-261)  
* Nikita Creciun (FAF-263)  
* Leonid Tiscenco (FAF-263)  
* Mihai-Constantin Sîrghii (FAF-262)  

---

# Abstract

The project **"Better Spotify / Sample Browser"** (hereinafter referred
to as **Sample Browser**) was developed by students Bogdan Glavan,
Andrei Simon, Nikita Creciun, Leonid Tiscenco, and Mihai-Constantin
Sîrghii, under the mentorship of Prof. Elena Graur at the Technical
University of Moldova, Faculty of Computers, Informatics and
Microelectronics. This report encapsulates the initial Conceptual Design
of a Software Application (PCAS) stage, covering problem definition,
domain analysis, methodological evolution, solution architecture, target
audience validation, and comparative benchmarking.

**Keywords:** Better Spotify, Sample Browser, Audio Sampling, Music
Information Retrieval (MIR), Granular Passage Discovery, Music Streaming
Architectures, Creator Workflow, Problem-Based Learning.

The primary objective of **Sample Browser** is to eliminate the
persistent workflow friction experienced by independent music producers
during sample crate-digging across streaming catalogs. Current digital
streaming platforms index musical compositions exclusively at the
whole-track metadata level, ignoring sub-track time boundaries.
Consequently, producers seeking specific localized musical textures—such
as isolated 4-bar rhythm breaks or distinct instrumental passages—must
scrub back and forth manually across long audio files, disrupting their
creative focus. To solve this, **Sample Browser** provides a specialized
discovery platform that interfaces with embedded streaming audio via the
YouTube IFrame API to segment, tag, and recommend localized audio
passages (4–30 seconds). By coupling a structured Two-Tier Tagging
System (objective structural presets and contextual descriptors) with
direct timestamp seeking and automatic loop auditioning, the system
transforms unstructured listening into a targeted creator utility.
Through a rigorous Problem-Based Learning methodology, this report
documents the team’s pivot from an unfeasible consumer streaming
overlay, establishes four verifiable validation hypotheses (H1–H4),
benchmarks market alternatives, and provides the architectural
foundation for subsequent systems modeling and empirical user
validation.

# Introduction

Streaming catalogs currently host over 250 million recordings, with
100,000 new tracks uploaded every single day . While casual listeners
enjoy endless background music, independent music producers hunting for
samples face an exhausting search process. Audio sampling underpins
roughly 17% of Billboard Hot 100 hits . Yet commercial streaming
platforms treat every song as an undifferentiated, continuous audio
file. Producers rarely sample entire songs. Instead, they search for
localized 4-bar drum breaks, clean keyboard progressions, or solo intros
without vocals.

Our project, **"Better Spotify / Sample Browser"** (hereinafter referred
to as **Sample Browser**), tackles this bottleneck directly. More than
half of active music makers work regular jobs outside the music
industry . They produce music during limited spare hours alongside
their day jobs. Spending entire evenings dragging playheads across long
recordings quickly drains creative energy. **Sample Browser** resolves
this issue by indexing, tagging, and recommending music at the passage
level (4 to 30 seconds), jumping creators straight to the cue points
they need.

The core objective of this research is to design and validate the
conceptual architecture of **Sample Browser**. The platform interfaces
with public embedded audio via the YouTube IFrame API to deliver
timestamped passage recommendations, avoiding media hosting costs and
copyright risks. Guided by the Problem-Based Learning (PBL) framework,
we grounded our engineering decisions in Music Information Retrieval
(MIR) literature, creator surveys, and platform policy
audits—specifically Spotify’s 2024–2026 developer restrictions on audio
feature endpoints .

The following chapters map out our research trajectory and conceptual
design. Chapter 2 details the problem analysis, documents our team’s
early methodological errors and iterative pivot, presents our solution
architecture, establishes target personas with testable validation
hypotheses (H1–H4), and benchmarks market alternatives alongside a
strategic SWOT matrix. Chapter 3 concludes the report with our roadmap
for Midterm 2.

# Midterm 1

The first milestone of this project focuses on identifying, scoping, and
analyzing an operational problem within modern music streaming and
digital production workflows. Guided by the Problem-Based Learning (PBL)
paradigm, this chapter documents the analytical foundation of our
project: crystallizing the problem description, performing an
industry-wide domain analysis, reflecting on early methodological
misconceptions and iterative pivots, defining the conceptual solution
architecture for **Sample Browser**, segmenting the target audience with
verifiable hypotheses, and performing a comparative benchmarking against
market alternatives.

## Problem Description and Problem Analysis

### Problem Description

Sampling and reference-based production fundamentally rely on
discovering specific musical textures, localized breaks, and unlayered
passages within existing recordings. However, modern digital audio
distribution channels treat musical works as single, undivided files,
creating persistent friction for creators.

#### Target Demographic and Creative Context

The demographic experiencing this problem comprises independent music
producers, beatmakers, and sound designers working in sample-intensive
and electronic genres (e.g., hip-hop, electronic, neo-soul, lofi, and
experimental music). According to Tracklib’s 2024 Producer Survey
($N = 1,107$), aspiring producers aiming to build a full-time career
constitute 58% of creators, while hobbyists (25%) and beginners (8%)
make up the majority of the remainder; full-time professionals represent
only 10% of the creator population .

Importantly, findings from the UK Musicians’ Census ($N \approx 6,000$)
reveal that 53% of active music makers must sustain their living through
employment outside the music industry . Independent creators therefore
operate with limited spare time alongside full-time jobs. Hours spent on
repetitive, non-creative manual search tasks directly diminish the
limited time available for actual sound design, arrangement, and
composition.

#### The Dual Bottleneck of Sample Discovery

When an independent producer auditions full-length recordings across
public streaming platforms to find sample material, they encounter two
structural bottlenecks, as visualized in
Figure 2.1:

1.  **Sub-Track Structural Blindness (The Whole-Track Metadata
    Bottleneck):** Streaming platforms (such as YouTube) and discovery
    overlays (such as Samplette.io) index recordings exclusively at the
    whole-track metadata level (Title, Artist, Global Genre, Year,
    overall BPM). Yet a music producer rarely samples an entire song;
    they search for a localized, **structurally isolated passage**—such
    as an unlayered 4-bar intro, a clean drum break, or a solo electric
    piano progression without vocals or heavy percussion bleeding over
    it. Without sub-track structural indexing, producers cannot see
    where usable moments occur, forcing them to manually click and scrub
    the playhead across dozens of 3-to-6 minute recordings just to check
    if an isolated section exists.

2.  **Ambiguity of Unconstrained Text Queries and Bookmarking
    Friction:** When producers attempt to search for specific sounds
    using arbitrary natural-language descriptions, subjective mood or
    texture keywords yield inconsistent results because listeners
    interpret free-form adjectives differently. In Music Information
    Retrieval (MIR) literature, Andersen and Knees  observed that
    musicians rely on subjective metaphors ("bright", "gritty",
    "hollow") and visual associations, while Zhang, Zhang, and Duan  and
    Kreković  demonstrated that complex mixed audio textures lack
    semantically agreed-upon free-text descriptors. Furthermore, as
    Flexer  demonstrated, low inter-rater agreement on perceptual music
    labels undermines arbitrary text tagging without auditory grounding.
    Coupled with the fact that standard browser bookmarks and YouTube
    playlists only save full-track URLs, creators face severe friction
    re-identifying specific 10-second passages and timestamps weeks
    later.

**Figure:** The Dual Bottlenecks of Sample Discovery in Streaming
Architectures.

![The Dual Bottlenecks of Sample Discovery in Streaming
Architectures.](images/problem_bottlenecks.png)

This repetitive audition-and-scrub cycle induces scrubbing fatigue and
destroys the producer’s creative flow state, a phenomenon analyzed by
Nash and Blackwell . While traditional "crate-digging" in physical
record stores historically celebrated serendipitous discovery ,
navigating flat, multi-million-track digital databases without temporal
indexing turns discovery into an exhausting manual audit.

#### Stakeholder Landscape

- **Primary Stakeholders (Independent Music Producers):** Benefit from
  direct, friction-free passage discovery, reducing audition time and
  preserving cognitive momentum during the creative process.

- **Secondary Stakeholders (Original Rights Holders and Catalog
  Artists):** Back-catalog recordings and obscure archival tracks gain
  renewed relevance, engagement, and potential licensing revenue when
  surfaced to active samplers.

- **Tertiary Stakeholders (Streaming Platforms and Audio Services):**
  Benefit from higher creator retention, transforming passive consumer
  players into active production and curation hubs.

#### Domain Relevance and Scale

Sampling is not a fringe artistic practice; it is foundational to modern
music production. Statistical industry analyses indicate that
approximately 17% of Billboard Hot 100 charting singles incorporate
sampled material . At the same time, Luminate and IFPI report that
global audio streaming catalogs expanded past 253 million tracks, with
over 106,000 new recordings uploaded daily . Without sub-track indexing,
this rapid expansion makes locating distinctive passages increasingly
difficult, burying valuable musical recordings behind rigid metadata
walls.

### Domain Analysis

#### Platform Recommendation Paradigms and Algorithmic Concentration

Modern streaming platforms categorize music at wildly differing levels
of granularity, primarily optimized for passive consumption rather than
creative exploration. Spotify—commanding 31.4% of global streaming
subscriptions —relies on black-box recommendation algorithms trained on
long-term user telemetry (skips, listening duration, playlist adds) ,
drawing on collaborative filtering frameworks popularized by platforms
such as Last.fm . To address discovery complaints, Spotify introduced
conversational AI tools, including its AI DJ (launched in beta in 2023
and updated with voice requests in 2025)  and AI Playlist
(prompt-to-playlist generation in 2024) . However, independent
evaluations highlight clear limitations: user audits identify recurrent
song loops and genre homogenization . Recommenders trained on historical
consumption inherently narrow catalog exposure: simulation studies prove
algorithmic confounding increases homogeneity while decreasing user
utility , with empirical consumer studies showing that algorithmic
nudging restricts diversity , and streaming audits confirming that
automated recommendations heavily concentrate within a small fraction of
catalog tracks .

Recent features such as Spotify’s SongDNA (powered by WhoSampled)
surface documented historical sample relationships and interpolations .
However, SongDNA is strictly retrospective: it exposes known connections
between existing hits rather than facilitating open, acoustic-similarity
search across unlinked catalog recordings.

In contrast to Spotify’s behavioral learning, alternative streaming
platforms emphasize immediate user controls. Deezer offers explicit
mood-based session filtering through Flow Moods (e.g., Chill, Focus,
Melancholy) . Yandex Music’s "My Wave" enables listeners to restrict
playback to instrumental tracks ("without words") or steer
recommendations toward unfamiliar artists via an explicit "Unfamiliar"
mode , while VK Music allows compound multi-parameter filtering . While
these immediate controls mitigate common listener frictions, they remain
restricted to whole-track playback and offer no visibility into
localized sub-track musical events.

#### Divergent Information-Seeking Objectives: Casual Listeners vs. Music Producers

Information-seeking behavior in musical domains differs fundamentally
based on user goals. In Information Science literature, Laplante and
Downie  categorize listener behavior into utilitarian needs (searching
for a known track or artist) and hedonic discovery (exploring moods,
serendipity, and emotional resonance), supported by diary studies on
everyday novel song encounters . Mainstream listeners accept whole-track
recommendations because their objective is continuous audio
accompaniment.

By comparison, music producers exhibit specialized, analytical retrieval
workflows. As demonstrated by Demetriou et al. , producers search for
sound as raw structural material rather than finished compositions. They
seek specific acoustic isolates: a 4-bar drum break, an unlayered
electric piano progression, or an isolated vocal timbre suitable for
rhythmic manipulation. Furthermore, physical crate-digging historically
carried profound social capital within hip-hop and electronic music
cultures . Producers prize obscurity—discovering recordings that few
others have heard or repurposed. In online ecosystems, producers even
co-opt search behavior through conventions such as "\[Artist\] Type
Beats", functioning as informal search engine optimization to locate
specific production aesthetics .

#### Catalog Saturation, The Generative AI Music Surge, and Audio LLM Limits

The challenge of locating obscure, high-quality sample material is
compounded by the unprecedented saturation of digital catalogs. In July
2026, streaming platform Deezer reported that AI-generated tracks
accounted for over 50% of its daily uploads, representing approximately
90,000 synthetic tracks uploaded each day . This synthetic flood drowns
out authentic archival recordings, making manual digging through new
releases increasingly frustrating.

At the same time, music creators exhibit notable resistance toward fully
autonomous generative music. In Tracklib’s 2024 Producer Survey
($N = 1,107$), 75% of producers reported that they do not use generative
AI, with 82.2% citing artistic reasons as their primary objection . This
resistance intensified in Tracklib’s 2025 survey of 1,734 music
creators: an overwhelming 82% opposed generating complete songs from
text prompts, while enthusiastically supporting assistive,
non-generative tools such as stem separation and intelligent search . As
producers expressed in field interviews with Andersen and Knees ,
creators welcome algorithmic assistance only when they retain ultimate
authorship: "I would like the machine to sit in the chair, as long as I
get to decide when it gets out."

Furthermore, modern Multimodal Audio-Language Models (audio-LLMs)
struggle to evaluate raw musical sound accurately. In a comprehensive
2025 benchmark evaluating 10,000 audio clips across speech,
environmental sound, and music, the leading foundation models achieved
only 60% question-answering accuracy . Similarly, the MuChoMusic
evaluation framework presented at ISMIR 2024 revealed that
audio-language models over-rely on linguistic cues within the text
prompt rather than truly extracting acoustic features from the audio
signal . Because text queries struggle to capture nuanced sonic
textures , fully automated, text-prompted discovery remains unreliable.
This underscores the necessity of human-in-the-loop, structured acoustic
tagging.

#### Current Producer Workflows and The Granularity Divide

Producers currently navigate this fragmented landscape using
disconnected tools that expose a fundamental structural divide:

- **Snippet Libraries (Splice, Looperman):** Splice—surpassing 350
  million downloads in 2024 —indexes short, pre-cut samples with
  timbre-matching tools (*Similar Sounds*, *Search with Sound*,
  *Describe a Sound*) . However, Splice operates strictly within a
  closed, proprietary sound pack catalog. Millions of producers draw
  from the identical pool of sounds, creating widespread "sample
  fatigue."

- **Pre-Cleared Sampling Catalogs (Tracklib):** Provides full master
  recordings cleared for legal sampling . Tracklib incorporates a
  bar-looping tool that slices playback into 1, 2, 4, or 8 bars and
  provides stem isolation . However, Tracklib categorizes records
  strictly by artist, genre, and BPM at the whole-track level; its
  looping tool functions only *after* the producer has already found and
  manually auditioned the song.

- **Randomized Streaming Digging (Samplette.io):** Interfaces with
  YouTube to deliver random obscure tracks filtered by style, BPM, and a
  custom view-count ceiling (e.g., serving only videos with under 10,000
  views) . While Samplette honors the crate-digger’s desire for
  obscurity, it indexes at the whole-track level: users must still scrub
  manually through every 4-minute video.

- **Enterprise Audio Intelligence (Cyanite.ai):** Offers
  state-of-the-art acoustic similarity search and multi-label
  classification via B2B APIs . However, Cyanite is tailored for
  sync-licensing agencies and catalog publishers rather than individual
  beatmakers, requiring enterprise contracts and capped at 30-second
  Spotify preview snippets .

This landscape reveals a critical market void: snippet libraries
describe isolated sounds in closed databases, while streaming platforms
describe whole songs with coarse metadata. No platform describes,
indexes, or recommends the internal, sub-track sections of published
musical compositions.

#### Platform API Constraints and Legal Realities

A critical dimension of domain analysis is the technical feasibility of
third-party audio analysis. In November 2024, Spotify initiated sweeping
restrictions on its Web API, formally deprecating public access to the
`Recommendations`, `Audio Features`, and `Audio Analysis` endpoints for
all newly registered applications . In February 2026, Spotify further
tightened development guidelines by restricting development mode to a
hard cap of 5 authorized test users, mandating Spotify Premium for
playback, and enforcing developer policies that explicitly prohibit
ingesting Spotify audio streams into external machine learning models .

Similarly, YouTube’s Developer Terms prohibit stripping audio,
background playback, or bypassing the graphical player interface.
Consequently, any viable third-party creator tool cannot rely on
unauthorized audio downloading or restricted Spotify endpoints; it must
operate strictly through compliant embedded streaming architectures
(such as the YouTube IFrame API).

### Project Evolution, Failures, and Mistake Analysis

In accordance with PBL principles, documenting false starts,
methodological misconceptions, and iterative course corrections is
essential for establishing sound engineering judgment. The project
originally began under the working title "Better Spotify" as an
alternative consumer streaming shell intended to counter algorithmic
bubbles through gesture-controlled queue flows and tag filters
(Figure 2.2) .

**Figure:** Early Research Evidence Map and Problem Brainstorming Canvas
on Milanote.

![Early Research Evidence Map and Problem Brainstorming Canvas
on Milanote.](images/milanote_map.png)

During iterative critique and mentor evaluation, this initial vision was
critically dismantled due to three systemic methodological flaws:

1.  **Misinterpreting Vocal User Complaints:** Negative app store
    reviews over-represented a vocal minority. In reality, over 80% of
    consumers are passive, lean-back listeners who easily bypass
    unappealing tracks by hitting "Next" with negligible cognitive
    effort.

2.  **Overlooking Platform Governance and API Lockdowns:** The concept
    assumed external control over proprietary streaming queues.
    Spotify’s updated 2024–2026 Developer Policy explicitly deprecated
    audio analysis endpoints and enforced strict playback boundaries,
    making a custom consumer playback shell legally and technically
    non-viable .

3.  **Targeting Casual Inconvenience over Mission-Critical Friction:**
    True product viability requires high stakes. While casual listeners
    face negligible switching friction, music producers operate under
    severe time constraints, where manual searching actively damages
    creative output.

Recognizing these systemic barriers, the team executed an intentional
pivot to **"Better Spotify / Sample Browser"** (hereinafter referred to
as **Sample Browser**). Shifting the target demographic from passive
consumers to sample-based creators transformed the product from an
unfeasible playback shell into an active creator utility, indexing music
at the passage level while operating strictly within compliant embedded
playback boundaries.

### Formal Problem Statement

> *"Independent music producers digging for samples across public
> streaming catalogs (such as YouTube and Samplette) waste significant
> time manually scrubbing through full-length recordings, because
> existing platforms index metadata exclusively at the whole-track level
> and provide no visibility into where short, structurally isolated
> passages (such as vocal-free instrumental sections or clean drum
> breaks) occur within a song."*

## Solution Proposal

To solve the identified problem, we propose **Sample Browser**, a
web-based sub-track discovery and sample-bookmarking platform that
shifts the atomic unit of music search from the entire composition to
the **sub-track musical passage**.

### System Architecture and Core Mechanics

Sample Browser functions as a zero-media-hosting, pointer-based
discovery workspace built directly on top of public streaming video via
the official **YouTube IFrame Player API**. To remain 100% compliant
with Section III.E of the YouTube Developer Policies and completely
eliminate bandwidth and hosting costs:

1.  The platform **does not download, host, extract, cache, or
    algorithmically process raw audio streams** on backend servers.

2.  The PostgreSQL database stores **only lightweight metadata
    pointers**: YouTube Video IDs, sub-track segment timestamps
    (`start_time`, `end_time`, constrained between 4 and 60 seconds),
    and structured passage tags submitted and curated by users.

3.  All audio playback and auditioning execute strictly client-side
    inside the official embedded YouTube player using synchronized
    timestamp seeking (`player.seekTo(start_time, true)`) and automated
    interval boundary looping.

**Figure:** Sample Browser Pointer-Based Architecture and YouTube IFrame
Interaction Pipeline.

![Sample Browser Pointer-Based Architecture and YouTube IFrame
Interaction Pipeline.](images/architecture_overview.png)

#### 1. Interactive Timeline and Segmented Visualizer

When a track is loaded into Sample Browser, the playback timeline
displays highlighted segment markers (e.g.,
`0:00–0:12 [Intro | Rhodes | No Drums]`) retrieved from our PostgreSQL
metadata store. Because embedded YouTube players execute inside a
sandboxed cross-origin ``<iframe>`` that denies access to raw PCM audio
buffers via the Web Audio API, the client UI does not attempt real-time
audio decoding. Instead, the interface visualizes pre-indexed segment
cue points delivered by the backend. Clicking a highlighted marker
directs the embedded player to jump instantly to `start_time` and
automatically loop playback upon reaching `end_time`, allowing producers
to audition the isolated passage in rhythm before deciding to chop or
sample.

#### 2. Two-Tier Tagging Taxonomy

To resolve the vocabulary gap and prevent database pollution without
requiring unfeasible AI audio decoding, Sample Browser replaces
arbitrary free-text input with a structured **Two-Tier Tagging System**:

1.  **Tier 1 — Primary Preset Objective Tags (Mandatory, High Search
    Priority):** Selected in 2–3 clicks from a strictly controlled,
    pre-written taxonomy describing verifiable musical facts about the
    timestamped segment:

    - *Isolation / Layering Status:* `[No Vocals]`,
      `[No Drums / Melodic Only]`, `[Isolated Drum Break]`,
      `[Solo Instrument]`, `[Vocal Phrase / Acapella]`.

    - *Instrumentation Present:* `[Electric Piano / Rhodes]`,
      `[Acoustic Piano]`, `[Guitar]`, `[Bass]`, `[Brass / Sax]`,
      `[Flute / Winds]`, `[Strings]`, `[Synth / Pad]`,
      `[Percussion / Drums]`.

    - *Structural Section / Function:* `[Intro]`, `[Break / Bridge]`,
      `[Solo Section]`, `[Outro]`, `[Chord Loop]`, `[One-Shot / Hit]`.

2.  **Tier 2 — Secondary Contextual Tags (Optional, Lower Priority,
    Moderated):** Curated descriptor chips for style and texture
    inspired by RateYourMusic and Splice categories (e.g.,
    `[Lo-Fi / Dusty]`, `[Syncopated / Swing]`, `[Jazz-Fusion]`,
    `[Dark / Minor]`). Secondary tags are visually collapsed so they
    never clutter the primary interface. Crucially, because every tag in
    Sample Browser is paired with **instant audio playback of the exact
    timestamped segment**, any subjective ambiguity is immediately
    resolved by auditioning the 10-second loop in one click.

#### 3. Seed-Passage ("Berrypicking") Navigation and Personal Cloud Crates

Figure 2.4 contrasts the traditional
crate-digging scrubbing cycle with the accelerated Sample Browser
workflow. To optimize creator discovery, the platform introduces two
interconnected mechanics:

- **Seed-Passage ("Berrypicking") Recommendations:** Rather than forcing
  creators to invent text search queries from scratch, a producer
  listening to a highlighted segment can select the tags present on that
  segment (e.g., `[Guitar] + [No Vocals] + [Break]`) and immediately
  receive a recommendation feed of specific segments inside other songs
  sharing those exact preset tags—jumping straight to the matching
  timestamp in the next track, operationalizing Bates’ information
  berrypicking model .

- **Personal Cloud Crates:** While digging across YouTube, producers can
  mark `Start` and `End` timestamps on any track, attach preset tags,
  and save the segment into their private Personal Cloud Crate. This
  eliminates bookmarking chaos and saves SSD disk space by storing
  lightweight metadata pointers rather than gigabytes of unorganized
  audio rips.

To formalize user interactions and guide subsequent system modeling, we
define three canonical User Stories with testable Acceptance Criteria:

**User Story 1 (Discovery):** As an aspiring bedroom producer, I want to
filter catalog recordings by localized objective preset tags (e.g.,
`[Solo Rhodes]` + `[No Drums]`) so that I can immediately discover
unlayered harmonic progressions without scrubbing through full albums.

- *Acceptance Criteria 1:* Query results return timestamped passage
  cards rather than undifferentiated whole tracks.

- *Acceptance Criteria 2:* Selecting a result positions the embedded
  player at the segment cue point within external player tolerances
  ($\le 1.5\text{--}2.0$s keyframe drift).

**User Story 2 (Auditioning):** As a beatmaker, I want candidate
passages to loop between defined temporal boundaries so that I can
evaluate their sampling potential without manually restarting playback.

- *Acceptance Criteria 1:* The player returns to the start timestamp
  upon reaching the segment endpoint.

**User Story 3 (Curation):** As an active crate-digger, I want to
bookmark specific 4-to-8 bar passages and attach acoustic descriptors
into my Personal Cloud Crate so that I can maintain an organized cloud
reference library without consuming local drive storage.

### Cold-Start Seeding and Asynchronous Curation Value

A central architectural concern in human-curated systems is the bootstrapping and scrubbing paradox: if automated audio processing is avoided, does User A still have to scrub through a 5-minute track to tag it for User B, and how does the platform deliver value when the database is initially sparse? Sample Browser addresses this through a three-layer strategy operating without any server-side audio decoding:

1. **Automated Text-Metadata Seeding (Zero Audio Processing):** To populate the initial catalog before user contributions scale, the ingestion pipeline extracts existing structured timestamps from YouTube video descriptions and chapter markers via the official YouTube Data API v3, cross-referencing them against track-level instrument credits from the public Discogs API (e.g., automatically identifying recordings credited with `Fender Rhodes`, `Tenor Saxophone`, or `Percussion`).
2. **Single-Player Utility First (Personal Cloud Crates):** Users are not recruited as unpaid crowdsourcing labor for strangers. Instead, producers mark `start_time` and `end_time` boundaries during their own active digging sessions to organize personal sample libraries, ensuring immediate single-player value so they never have to re-scrub a saved 5-minute video weeks later.
3. **Multi-Purpose Structural Reuse:** A single 5-minute composition typically contains multiple distinct musical passages (such as an unlayered electric guitar intro at `0:00–0:14` and an open drum break at `2:10–2:18`). Consequently, one producer's private bookmarking session creates persistent structural landmarks that other creators with entirely different sampling objectives can immediately reuse.


- *Acceptance Criteria 1:* Bookmarked timestamps and tags persist in the
  user’s private collection across sessions.

**Figure:** Workflow Comparison: Traditional Manual Scrubbing vs. Sample
Browser Granular Discovery.

![Workflow Comparison: Traditional Manual Scrubbing vs. Sample
Browser Granular Discovery.](images/before_after_workflow.png)

#### 4. Conceptual Interface Design

Figure 2.5 illustrates the conceptual user
interface design of Sample Browser. The interface features the embedded
track header, the segmented interactive timeline highlighting detected
passage boundaries, an acoustic preset filter panel, and a synchronized
passage feed.

**Figure:** Sample Browser Interface Wireframe: Embedded Player,
Segmented Timeline, and Passage Curation Drawer.

![Sample Browser Interface Wireframe: Embedded Player,
Segmented Timeline, and Passage Curation Drawer.](images/ui_concept_mockup.png)

### The Internal Architecture Debate: Crowdsourcing vs. Automated MIR

During conceptual design, a critical architectural debate emerged
between team members Leonid Tiscenco and Bogdan Glavan regarding data
ingestion and catalog scalability:

- **The Automated MIR and Subjectivity Dilemma (Leonid):** Leonid argued
  that relying entirely on crowdsourced manual tagging is vulnerable to
  severe cognitive fatigue, inconsistent labeling, and malicious data
  entry. Furthermore, musical perception is fundamentally
  subjective—what one user tags as "energetic soul," another labels
  "vintage pop," as demonstrated by Flexer  in studies of low
  inter-rater agreement for perceptual music similarity, threatening
  database coherence. Simultaneously, Section III.E of the YouTube
  Developer Policies legally prohibits downloading audio streams for
  server-side automated MIR analysis, and producer gatekeeping (hiding
  rare samples from competitors) creates a severe cold-start risk for
  public crowdsourcing.

- **The Curatorial Incentive and Audio Context Model (Bogdan):** Bogdan
  countered that producers already spend hours digging and organizing
  personal sample notes. By coupling passage tagging with a personal
  cloud bookmarking utility, producers gain immediate private utility
  from bookmarking passages. Furthermore, producers frequently reveal
  sample sources on platforms like WhoSampled  because production
  originality stems from how a sample is chopped, pitched, and mixed
  rather than the source itself. By pairing objective preset categories
  with instant audio segment playback, any subjective ambiguity is
  instantly clarified by listening.

- **The Architectural Synthesis and Contingency Pivot:** The team
  converged on the **Two-Tier Preset Taxonomy + Instant Audio Context**
  model over a pure pointer architecture. This completely eliminates
  illegal server-side audio downloads while preventing subjective tag
  anarchy. Furthermore, the team established a formal **contingency
  pivot trigger**: if upcoming field validation interviews reveal that
  producers refuse to share sample tags publicly due to gatekeeping, the
  team will execute an immediate, documented pivot to a **Personal
  Tagged Crate-Digging & Bookmarking Workspace** (differentiated from
  basic bookmarking sites like `chop-stop.com` and
  `sampledigging.online` by structured sub-track tagging that preserves
  why a section was saved).

### Value Proposition

To ensure clear product-market alignment, we structured the solution
against Alexander Osterwalder’s Value Proposition Canvas
(Table 2.1). The framework explicitly contrasts
independent producer workflows against the platform’s architectural
interventions:

|                                                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                       |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Customer Jobs:** $\bullet$ Crate-digging across streaming catalogs (YouTube/Samplette) for unique sample material. $\bullet$ Locating clean, unlayered 4–8 bar sections (breaks, intros, solos) suitable for chopping. $\bullet$ Organizing and revisiting candidate sample moments discovered during digging sessions.   | **Products & Services:** $\bullet$ Web-based sub-track passage browser interfacing with YouTube IFrame API. $\bullet$ Two-Tier Tagging System (Objective Preset Structural/Instrument tags + Secondary descriptors). $\bullet$ Timestamped Personal Cloud Crates and seed-passage recommendation feed.                                                |
| **Pains:** $\bullet$ Wasting time manually scrubbing through 5-minute tracks whose sections don’t match search goals. $\bullet$ Losing track of exact timestamps and instruments inside bookmarked YouTube videos or playlists. $\bullet$ Sample fatigue and subscription costs of overused commercial loop packs (Splice). | **Pain Relievers:** $\bullet$ One-click playhead jumping (`seekTo`) and auto-looping of pre-marked 4–30s segments. $\bullet$ Preset `[No Drums]`, `[No Vocals]`, and `[Solo Instrument]` tags exposing clean sections instantly. $\bullet$ Cloud timestamp bookmarking that saves the exact interval and instrument notes without local disk clutter. |
| **Gains:** $\bullet$ Discovering obscure, authentic musical passages faster. $\bullet$ Smooth "berrypicking" navigation from one inspiring segment directly to similar segments in other songs. $\bullet$ Instant audio verification of whether a tagged passage fits the current beat idea.                                | **Gain Creators:** $\bullet$ Tag-intersection recommendations linking directly to sub-track cue points across songs. $\bullet$ Immediate audio context alongside tags to eliminate descriptive ambiguity. $\bullet$ Zero-cost web access over public streaming links without hosting or downloading files.                                            |

Value Proposition Canvas Matrix for Sample Browser.

We summarize this value intervention into a single operational promise:

> **"For independent music producers who lose time scrubbing through
> full-length tracks on YouTube to find usable sample sections, Sample
> Browser is a passage-level discovery and bookmarking platform that
> connects creators directly to timestamped, auto-looped musical
> intervals categorized by objective structural and instrumental preset
> tags."**

## Target Group and Customer Validation

### Preliminary Business Model Hypotheses

To ensure alignment with sustainable product design principles, Sample
Browser defines a preliminary two-tier freemium model:

- **Free Community Tier:** Core web-based passage discovery, embedded
  player auditioning, public tagging, and personal cloud bookmarking.

- **Pro Creator Tier:** Advanced multi-tag intersection filtering,
  unlimited private Smart Crates, and DAW marker/timecode export
  (CUE/MIDI timecodes).

### Target Group Segmentation

Based on demographic and workflow analysis, our target market is
subdivided into three primary creator archetypes
(Table 2.2). In the Tracklib creator
survey, these three categories account for 93% of respondents (58%
aspiring career producers, 25% hobbyists, and 10% full-time sync
composers/sound designers). The remaining $\approx 7\text{--}8\%$ of
respondents in the survey represent absolute beginners who do not yet
use sample chopping or archival reference workflows, and are therefore
excluded from our core target archetypes.

| **Segment**                          | **Market Share**                 | **Primary Production Goal**                                                    | **Primary Pain Point**                                                    |
|:-------------------------------------|:---------------------------------|:-------------------------------------------------------------------------------|:--------------------------------------------------------------------------|
| **Aspiring Career Producers**        | $\approx 58\%$ (Tracklib survey) | Releasing original beats, building client portfolios, seeking unique identity. | Limited time alongside day jobs; fatigue from manual digging.             |
| **Hobbyists & Beatmakers**           | $\approx 25\%$                   | Evening/weekend beat-making, community beat battles (lofi/boom-bap).           | Frustration with repetitive commercial sample packs on Splice/Looperman.  |
| **Sync Composers & Sound Designers** | $\approx 10\%$                   | Sourcing distinct vintage textures and acoustic references for media scoring.  | Inability to search catalogs by specific timbral or solo instrument cues. |

Target Group Segmentation Matrix for Sample Browser.

### User Persona

To ground our architectural decisions in real creator workflows, we
synthesized the archetypal persona of **Alex "Kaelo" Miller** (22,
Bedroom Producer). Alex works full-time in technical support and
produces hip-hop and neo-soul in his spare time (8–12 hours a week)
using FL Studio and Ableton Live. Every weekend, he spends hours
crate-digging through obscure 1970s Japanese jazz-fusion and Brazilian
MPB recordings on YouTube.

His core friction captures the exact operational failure of current
streaming search interfaces:

> *"I find an incredible 6-minute jazz-fusion album on YouTube. I know
> there is a 4-bar Rhodes chord progression somewhere in track 4, but I
> spend 15 minutes scrubbing the playhead back and forth trying to
> isolate it without drums over it. By the time I locate it, my
> inspiration is gone."*

Alex does not need another algorithmic playlist or generic radio feed.
He wants to select an acoustic tag, jump straight to the unlayered
passage, and instantly audition five other recordings sharing that exact
sound.

**Persona 2: Annie Lee (20, Student Sound Designer / Hobbyist
Producer)** Annie is a media informatics student producing ambient
soundscapes and lofi tracks. She works in sporadic weekend sessions and
avoids commercial sample marketplaces due to repetitive, overused loops.
Her primary friction is finding coherent instrumental textures across
diverse world recordings. She needs a tool to rapidly audition isolated
acoustic passages in context without breaking her creative immersion.

### Customer Validation Hypotheses (Midterm 2 Roadmap)

In strict accordance with the PCAS course guideline rubric ("Define hypotheses about your solution's features and about your target groups"), all four validation hypotheses are explicitly partitioned into target group/problem hypotheses and solution feature hypotheses:

#### Category A: Target Group and Problem Hypotheses

- **H1 (Problem & Workflow Friction Hypothesis — Sub-Track Scrubbing & Isolation):** When hunting for samples in full-length recordings (e.g., on YouTube or Samplette), producers spend substantial time listening to and manually scrubbing through songs whose sections do not match their structural goals (such as finding a clean instrumental passage without vocals or heavy drums), frequently abandoning otherwise promising tracks. *Confirmed if* $\ge 60\%$ of interviewed sampling producers describe manual playhead scrubbing and the lack of clean/isolated sections as a recurring reason for slow digging sessions or abandoning candidate songs. *Refuted if* producers report that finding the right timestamp inside a song takes negligible effort, or that they simply grab any layered section and rely on DAW AI stem-separation without caring about clean sections.
- **H4 (Target Segment Hypothesis — Unlicensed Public Catalogs vs. Curated Libraries):** Small-scale and independent producers do not sample purely for commercial releases and actively prefer digging in unlicensed public full-track catalogs (YouTube, Samplette) over paid pre-curated libraries (Splice, Tracklib) due to cost, catalog variety, and commercial loop fatigue. *Confirmed if* independent/hobbyist respondents confirm they regularly sample from YouTube/public streams for practice, beat battles, or underground releases without being deterred by sample clearance. *Refuted if* respondents exclusively use royalty-free packs (Splice) and refuse to touch YouTube recordings due to copyright fear.

#### Category B: Solution Feature Hypotheses

- **H2 (Solution Feature Hypothesis — Two-Tier Preset Tags, Audio Context & Berrypicking Navigation):** Producers rely primarily on objective categories (instruments, section type/breaks, tempo) while distrusting standalone subjective mood/texture tags—and find it easier to discover samples by branching out from the tags of a specific audio segment they are currently hearing (*berrypicking*) rather than inventing text queries from scratch. *Confirmed if* producers prioritize instrument/structural filters, report that vague mood/vibe tags on existing platforms are unreliable without immediate audio preview, and naturally search by following associative chains of related tracks. *Refuted if* producers report that free-form text search or random browsing without tags is completely sufficient for their workflow.
- **H3 (Solution Feature Hypothesis — Timestamp Bookmarking Utility vs. Community Sharing / Gatekeeping):** Producers who save candidate songs online struggle to keep track of specific sub-track timestamps and reasons for saving them, and are willing to tag and share song sections using fast preset categories as part of organizing their own sample library (rather than keeping all discovered sources strictly private). *Contingency Pivot Trigger:* If producers strongly want timestamp bookmarking and tagging for themselves but refuse to share tags publicly due to gatekeeping, the team will execute a planned soft pivot to a **Personal Crate-Digging & Bookmarking Workspace** (differentiated from basic bookmarking sites like `chop-stop.com` and `sampledigging.online` by structured sub-track tagging).

### Customer Interview Protocol

For Midterm 2, the team has established a comprehensive 10-question
semi-structured interview protocol grounded in *The Mom Test*
methodology. In accordance with course validation guidelines, the team
will conduct recorded video interviews first, targeting a sample size of
$N \approx 20$ active music creators (~4 interviews per team member),
and back them up with a supplementary Google Forms quantitative survey
to cross-validate findings across a broader pool of music creators while
eliciting past operational behaviors rather than speculative opinions:

**Block 1: Producer Background & Screening (Context)**

1.  **\[BK\]** *"How would you describe the main genres of music you
    make, and what inspires your production style?"*

2.  **\[BK + H4\]** *"Do you currently release music under an alias,
    collaborate with artists, or make beats primarily for personal
    enjoyment, practice, or underground communities?"*

3.  **\[Screening\]** *"When making a track, how much do you rely on
    sampling existing recordings versus composing from scratch with
    virtual instruments (VSTs) or hardware? Roughly how many samples did
    you use on your last sampled track, and why did you choose them?"*

**Block 2: Unlicensed Song Digging vs. Pre-Curated Libraries (Testing
H4)**

1.  **\[H4\]** *"Do you mostly use pre-curated royalty-free sample
    libraries (like Splice or Looperman), or do you prefer sampling
    directly from original full-length songs (on YouTube, Samplette,
    Tracklib, vinyl)?"*

    - *Follow-up 4a:* What makes you choose one over the other—is it
      convenience, cost, sound uniqueness/fatigue, or something else?

    - *Follow-up 4b:* Which free or paid tools/sites do you use most
      often to find samples? Has sample licensing/copyright ever been an
      issue for the music you make, or does it not affect your releases?

**Block 3: Last Concrete Digging Session & Inside-Track Scrubbing
(Testing H1)**

1.  **\[H1\]** *"Think about the last specific time you searched for a
    sample inside full-length songs online. What kind of sound or
    musical part were you looking for, and how long did you spend
    searching before you felt you spent enough time?"*

    - *Follow-up 5a:* Roughly how many tracks did you click through and
      preview before you found one you actually used?

2.  **\[H1\]** *"When you click on an unfamiliar 3-to-6 minute song on
    YouTube or Samplette, how do you actually scan through the track to
    find the exact 4-to-8 bar section you want?"*

    - *Follow-up 6a:* Have you recently found a song with a great sound
      or instrument, but ended up skipping it because the section wasn’t
      usable? What ruined that section for you (e.g., vocals/drums
      overlapping, tempo shifts)?

    - *Follow-up 6b:* Do you specifically hunt for clean, isolated
      sections in a song (like an intro, break, or solo), or do you use
      AI stem separation in your DAW on any part of the song? Why?

**Block 4: Tag Reliability, Audio Context & Berrypicking (Testing H2)**

1.  **\[H2\]** *"What was the last sound you searched for using text
    keywords or category filters, and how did you describe it? How often
    do you find a good sample from a single text search query?"*

    - *Follow-up 7a:* When browsing platforms that use tags or filters
      (like Splice, Tracklib, Samplette, or RYM), which categories do
      you actually trust and rely on (e.g., instruments, BPM, song
      sections), and which tags do you avoid or find
      confusing/inaccurate (e.g., mood or texture words)?

2.  **\[H2\]** *"Think of the last time you needed another sample to
    go with one you already had (or wanted to find more samples similar
    to one you just heard). How did you go about finding it?"*

    - *Probe (only if it doesn't come up):* Did anything about the first
      sample guide where or how you looked next?

    - *Follow-up 8a:* Think of the last time you picked a sound or a
      song because of how it was labelled—a mood, a genre, or an
      instrument. Did it match what you expected once you heard it?

**Block 5: Personal Sample Storage, Timestamps & Community Contribution
(Testing H3)**

1.  **\[H3\]** *"Do you keep a personal library, playlist, or folder
    where you save songs or samples you discovered for future projects?
    Do you store them locally on your drive or online (e.g., YouTube
    playlists, bookmarks, sites like chop-stop / sampledigging)?"*

    - *Follow-up 9a:* How do you categorize what you save? When you come
      back to a saved full-length song weeks later, how do you remember
      which exact timestamp had the sample and why you saved it?

2.  **\[H3\]** *"Have you ever shared your sample finds, digging
    playlists, or song sources with other producers, or do you prefer to
    keep your found songs private?"*

    - *Follow-up 10a:* If you had a fast way to bookmark exact song
      sections (Start–End timestamps) with preset instrument/section
      tags for your own online library while digging, would you leave
      those tagged sections public to help build a community catalog
      (with credit on your profile), or keep them private? Why?

## Comparative Analysis and Strategic Evaluation

### Benchmarking Against Existing Solutions

To evaluate how Sample Browser positions itself within the current
creator landscape, it is benchmarked against representative tools across
the sample discovery workflow:

- **Splice:** The commercial market leader offering pre-cut, isolated
  royalty-free loops and one-shots with sound-matching and DAW plugin
  integration .

- **Samplette.io:** A web-based crate-digging interface applying
  metadata and geographical filters over YouTube’s catalog to surface
  obscure recordings .

- **Tracklib:** A commercial sampling marketplace offering full-length
  master recordings categorized by genre and BPM, with integrated
  licensing and bar-chopping tools .

- **Sononym:** A desktop-based sample librarian that uses machine
  learning to organize and search local audio files based on acoustic
  similarity (timbre, pitch, brightness).

- **Cyanite.ai:** A B2B enterprise audio intelligence platform offering
  text-to-audio and audio-to-audio similarity search with segment-level
  scoring for sync agencies and publishers .

| **Platform**              | **Index Granularity** | **Query Paradigm**        | **Catalog Type**           | **Isolation Focus**              | **Setup Friction / Cost**        |
|:--------------------------|:----------------------|:--------------------------|:---------------------------|:---------------------------------|:---------------------------------|
| **Splice**                | Individual loop       | Text / Sound Match        | Curated proprietary        | Pre-cut isolated loops           | High (Commercial subscription)   |
| **Samplette.io**          | Whole track           | Random / Discogs          | Public (YouTube)           | None (Full track)                | Zero (Web-based)                 |
| **Tracklib**              | Track + Bar loops     | Metadata / Mood           | Pre-cleared master ( 100k) | Partial (Stems on select tracks) | Low (Subscription + clearance)   |
| **Sononym**               | Local sample files    | Audio similarity          | Local user disk            | N/A (Short files only)           | High (Desktop install & license) |
| **Cyanite.ai**            | Track & Interval      | Text / Audio Reference    | Enterprise B2B             | Full mix (Segment scores)        | High (B2B API contract)          |
| **Sample Browser (Ours)** | **Passage (4–30s)**   | **Passage acoustic tags** | **Public (YouTube)**       | **Yes (Break/Solo tags)**        | **Zero (Web-based)**             |

Comparative Analysis: Sample Browser vs. Market Alternatives.

### SWOT Analysis

A comprehensive SWOT analysis evaluates the strategic positioning of
Sample Browser within the creator tooling ecosystem:

<table>
<caption>SWOT Analysis of Sample Browser.</caption>

<strong>STRENGTHS (S)</strong>
<strong>WEAKNESSES (W)</strong>

<strong>Sub-Track Granularity:</strong> Indexes at the 2–16 bar
interval level, designed to reduce manual scrubbing friction (validation
pending).
<strong>Explainable Discovery:</strong> Transparent acoustic
descriptors rather than opaque black-box recommendations.
<strong>Zero Hosting Overhead:</strong> Uses compliant YouTube
IFrame streaming, requiring no high-cost media storage.
<strong>Contextual Playback:</strong> Allows auditioning passages
within their original musical arrangement.

<strong>Cold-Start Catalog Challenge:</strong> Platform utility
in early stages relies heavily on initial pre-tagged passage
volume.
<strong>Third-Party Dependency:</strong> Vulnerable to YouTube
video takedowns, regional geo-blocks, or API embed policy
changes.
<strong>No Direct Audio Export:</strong> Cannot offer one-click
audio downloads under YouTube API terms; users must acquire source audio
externally.

<strong>OPPORTUNITIES (O)</strong>
<strong>THREATS (T)</strong>

<strong>Rising Sample Pack Fatigue:</strong> Growing producer
backlash against sterile, overused commercial sample libraries
(Splice) .
<strong>DAW Plugin Integration:</strong> Potential to port the
web interface into an embedded VST/AU plugin directly inside Ableton or
FL Studio.
<strong>Catalog Rights Monetization:</strong> Future partnership
pathways with archival labels to monetize dormant
back-catalogs.

<strong>API Policy Lockdowns:</strong> Risk of streaming
providers restricting embedded player functionality or iframe event
telemetry.
<strong>Market Incumbent Expansion:</strong> Established tools
(e.g., Tracklib or Samplette) expanding natively into segment-level
tagging.
<strong>Hardware Keyframe Drift:</strong> Hardware keyframe
latency in embedded players (seekTo drift) and third-party streaming API
policy modifications.
<strong>Copyright Uncertainties:</strong> Legal sensitivities
surrounding sample clearance for archival recordings in commercial
releases.

</table>

SWOT Analysis of Sample Browser.

### Analytical Synthesis

As demonstrated in
Table 2.3 and
Table 2.4, Sample Browser occupies a distinct,
unoccupied niche at the intersection of streaming discovery and music
production. While existing platforms force creators to choose between
pre-cut, overused commercial loops (Splice) or tedious, unstructured
digging across full-length tracks (Samplette, YouTube), Sample Browser
addresses this divide by delivering granular passage-level indexing
directly over the world’s largest public music catalog.

# Midterm 2: Empirical Validation and Systems Modeling

The second project milestone will transition **Sample Browser** from
conceptual problem analysis to empirical field validation and rigorous
software engineering modeling. This chapter establishes the verification
methodology, specifies operational system requirements, models
behavioral workflows using unified modeling language (UML) artifacts,
and maps the user experience architecture.

## Customer Validation and Empirical Findings

### Methodology and Participant Demographics

Empirical validation will prioritize qualitative depth by conducting
recorded video interviews first, targeting a sample size of $N \approx 20$
independent music artists, beatmakers, and producers (~4 interviews conducted
per team member). To cross-validate findings and measure the statistical
breadth of identified behaviors across a wider community of music makers,
these qualitative video interviews will be backed up by a supplementary
Google Forms quantitative survey.

Interviews may be conducted in any language (English, Romanian, Russian)
provided that the participant is an active music maker, artist, or producer.
When interviewing personal acquaintances or university peers, team members
will adhere strictly to neutral, non-leading *The Mom Test* questioning
principles to prevent confirmation bias. To ensure ecological validity,
participants will be recruited across aspiring career beatmakers ($>50\%$),
hobbyist creators, and sound designers.

Participant recruitment will be structured across four distinct operational
channels:

1.  **Known Musician Contacts, Local University & Chișinău Artist Network
    (5–6 participants):** Fellow student producers at the Technical
    University of Moldova (UTM/FCIM), local Chișinău musicians, and personal
    acquaintances who create music (conducted via recorded video call or in
    person under strict non-biased protocol).

2.  **Direct Instagram Outreach (5–6 participants):** Direct outreach
    ("shot in the dark" DMs) to independent beatmakers, underground music
    artists, and producers actively posting studio and sampling reels on
    Instagram.

3.  **Dedicated Sampling and Beat-Battle Discord Communities (5–6
    participants):** Active producers in Samplette / Crate-Digging Discord
    channels, Kenny Beats / Beat Battle communities, `r/makinghiphop` Discord,
    Lo-Fi Hip-Hop producer servers, and Stones Throw Beat Battles (STBB).

4.  **Small YouTube / SoundCloud "Sample Flip" Creators and Regional Telegram
    Chats (3–4 participants):** Independent producers posting sample-based
    beatmaking videos ("samplette flip", "youtube sample beat") and active
    participants in regional Telegram producer communities who list public
    contact handles.

Each interview will be executed by two team members (a Lead Interviewer and a
Note-Taker/Scribe) following the 10-question protocol ($Q1\text{--}Q10$)
grounded in *The Mom Test*. In strict accordance with the course guideline
directive (*"Record videos and make photos of these interviews to refer to
them when documenting your findings"*), verbal consent will be obtained to
record remote sessions (via Google Meet / Zoom with screen shares) and log
verbatim quotes. Post-interview responses will be synthesized into
standardized 1-page coding cards evaluating hypothesis validation status.

### Qualitative Interview Insights

Transcripts from qualitative customer development sessions are coded
thematically to evaluate hypotheses $H1$ through $H4$:

- **H1 (Scrubbing & Isolation Friction):** Evaluating whether manual
  scrubbing and the absence of clean intro/break sections represent the
  primary time sink during crate-digging, and whether modern DAW stem
  separation tools resolve or merely shift this friction.

- **H2 (Objective Preset Tags & Berrypicking):** Verifying whether
  producers prioritize objective structural/instrument tags over
  subjective mood labels, and whether browsing naturally follows
  associative seed-passage chains.

- **H3 (Curation & Contribution vs. Gatekeeping):** Assessing how
  producers organize discovered timestamps, and whether willingness to
  contribute to a community index is confirmed or triggers our
  contingency pivot to a **Personal Crate-Digging Workspace**.

- **H4 (Unlicensed Digging vs. Curated Libraries):** Confirming whether
  independent producers actively prefer digging across public full-track
  catalogs (YouTube, Samplette) due to cost and commercial loop fatigue
  on platforms like Splice.

### Task-Completion Evaluation (Wizard-of-Oz Testing)

To validate interface ergonomics and task-completion velocity prior to
full-scale software implementation, participants execute identical audio
retrieval tasks under two experimental conditions:

1.  **Baseline Condition:** Unstructured crate-digging across public
    streaming catalogs (manual scrubbing and external note-taking).

2.  **Prototype Condition (Wizard-of-Oz):** Retrieval using pre-indexed
    acoustic passage cards with direct timestamp seeking and automatic
    loop boundaries.

Metrics recorded include time-to-first-usable-passage, session
abandonment rate, and perceived cognitive friction measured via the
NASA-TLX assessment framework. The test explicitly evaluates interface
flow and perceived value without misattributing findings to automated
MIR algorithms.

## System Requirements Specification

### Functional Requirements

Based on creator workflows and the pointer-based YouTube IFrame
architecture, the functional boundaries of Sample Browser comprise:

- **FR-01 (Two-Tier Tag Filtering):** The system shall allow users to
  filter passage candidates using primary preset objective tags
  (isolation, instrumentation, and section role) with optional secondary
  contextual descriptor chips.

- **FR-02 (Sub-Track Passage Retrieval):** The system shall return
  localized 4–30 second segment cards with associated timestamps and
  preset and contextual tags rather than entire compositions.

- **FR-03 (Embedded Cue Synchronization):** The player shall interface
  with the client-side YouTube IFrame API to position the playhead
  directly at the designated passage cue point (`seekTo`) upon card
  selection.

- **FR-04 (Automated Boundary Looping):** The embedded player shall
  continuously loop playback between the defined segment start and end
  timestamps until paused or redirected.

- **FR-05 (Personal Cloud Crates & Passage Submission):** Authenticated
  users shall be able to bookmark timestamped passages into private
  cloud crates and propose tags for community catalog inclusion.

### Non-Functional Requirements

- **NFR-01 (Platform API Compliance):** The architecture shall strictly
  adhere to Section III.E of the YouTube Developer Policies by operating
  purely through embedded client-side playback, with zero raw audio
  stream downloading, scraping, or server-side media caching.

- **NFR-02 (Cue Seeking Latency):** Playhead positioning and buffer
  initialization shall execute within $\le 1.5$ seconds under standard
  broadband conditions, bounded by third-party iframe keyframe
  alignment.

- **NFR-03 (Backend API Response Time):** Metadata query latency for
  passage filtering and tag intersections shall not exceed $200$ ms for
  $95\%$ of requests.

## Structural and Behavioral UML Modeling

### UML Activity Diagrams

Activity models formalize the sequential and concurrent logic of the
system:

- **Discovery Flow:** Query submission $\rightarrow$ Tag intersection
  indexing $\rightarrow$ Candidate list rendering $\rightarrow$ User
  card selection $\rightarrow$ IFrame cue seeking $\rightarrow$ Loop
  listener loop activation.

- **Curation Pipeline:** User timestamp marking $\rightarrow$ Tag family
  assignment $\rightarrow$ Profanity and duplication filter
  $\rightarrow$ Persistence in PostgreSQL $\rightarrow$ Community appeal
  threshold verification.

### UML Use Case Modeling

The operational interactions involve three primary actors:

- **Music Producer:** Searches passages by acoustic tags, audits
  contextual loops, and exports timecode references.

- **Community Contributor:** Marks candidate intervals, assigns acoustic
  tags, and manages personal crates.

- **System Moderator / Admin:** Audits reported erroneous tags, resolves
  taxonomic collisions, and monitors ingestion health.

### UML Sequence Diagrams

Sequence diagrams model asynchronous message exchanges across system
boundaries, documenting the lifecycle of an acoustic search query, the
communication handshake with the embedded player sandbox, and error
recovery handling during stream unavailabilities.

## Visual Interface Design and Interaction Architecture

### Wireframes and Component Hierarchy

The interface architecture follows a progressive disclosure layout
designed for dark-mode studio environments. The component hierarchy
centers the interactive segmented timeline, flanked by persistent
acoustic filter drawers and a low-latency passage candidate drawer.

### High-Fidelity Mockups

High-fidelity designs reflect production-ready responsive layouts,
detailing active playing states, tag selection badges, waveform
segmentation highlights, and mobile companion views.

### User Flow Diagrams

User flow networks document navigational state transitions, delineating
paths between initial landing, query refinement, continuous auditioning
sessions, and private crate management.

# Conclusions

The Midterm 1 milestone established the conceptual and analytical
foundations of **Sample Browser**, resolving key product design
questions through a Problem-Based Learning framework. By discarding our
initial, unfeasible concept of an alternative consumer streaming shell,
we focused on a genuine workflow bottleneck: independent producers
losing hours scrubbing through long recordings to find isolated,
sample-worthy passages.

Our domain research confirmed that contemporary streaming platforms
index music strictly by whole-track metadata. This leaves creators
trapped between generic, overused loop libraries like Splice and
tedious, unstructured crate-digging across YouTube or Samplette.
**Sample Browser** bridges this divide. By dividing tracks into 4–30
second passages, assigning structured acoustic tags, and using the
YouTube IFrame API for compliant playback seeking and looping, our
architecture protects the producer’s creative focus.

This milestone yielded four tangible deliverables for our engineering
roadmap:

- **A validated problem definition** supported by academic MIR
  literature and empirical creator surveys (Tracklib, UK Musicians’
  Census).

- **A candid retrospective of project failures**, recording our team’s
  pivot away from vocal minority feedback, passive user habits, and
  closed API barriers.

- **Four falsifiable validation hypotheses (H1–H4)** paired with a
  semi-structured interview protocol for field testing.

- **A competitive and SWOT benchmark** clearly positioning our
  application against Splice, Samplette, Tracklib, Sononym, and Cyanite.

With the domain analysis and system concept established, our team is
prepared for Midterm 2. The next milestone will focus on validating our
hypotheses through $N \approx 20$ recorded video interviews with active music
creators (~4 per team member) backed by a supplementary quantitative survey,
formalizing software requirements through UML modeling
(Activity, Use Case, and Sequence Diagrams), and building interactive
interface wireframes.

99

A. Anderson et al. "Algorithmic Effects on Discovery Dynamics on
Spotify." In Proceedings of the 16th International AAAI Conference on
Web and Social Media (ICWSM 2022), 2022.

A. J. B. Chaney, B. M. Stewart, and E. Engelhardt. "How algorithmic
recommendations shape user behavior: Feedback loops in collaborative
filtering." ACM Transactions on Information Systems, 2018.

C. Nash and A. F. Blackwell. "Liveness and flow in notation use." In
Proceedings of the International Conference on New Interfaces for
Musical Expression (NIME 2012), pages 76–81, 2012.
<https://www.nime.org/proceedings/2012/nime2012_217.pdf>

Complete Music Update. "Musicians’ Census sets out the financial
challenges and career barriers faced by music-makers." September 11,
2023.
<https://completemusicupdate.com/musicians-census-sets-out-the-financial-challenges-and-career-barriers-faced-by-music-makers/>

Cyanite. "Cyanite Advanced Search: Smarter music discovery via API."
Company Blog, July 15, 2025.
<https://cyanite.ai/blog/advanced-search-api/>

Cyanite. "Advanced Search API Documentation." Retrieved October 2026.
<https://api-docs.cyanite.ai/docs/advanced-search/>

Cyanite. "Find Similar Tracks: Audio & Interval Similarity." API
Documentation, October 2026.
<https://api-docs.cyanite.ai/docs/similarity-search/>

Cyanite. "Free Text Search API Guide." Cyanite Documentation, 2026.
<https://api-docs.cyanite.ai/docs/free-text-search-guide/>

Cyanite. "Cyanite Getting Started Guide and API Specifications."
Technical Report, June 2024.
<https://cyanite.ai/wp-content/uploads/2024/06/CyaniteGettingStartedGuide120624.pdf>

Cyanite. "Music Analysis API: AI-powered tagging and search." October 6,
2025. <https://cyanite.ai/blog/music-analysis-api/>

Cyanite. "Similar song finder AI for music catalogs." January 12, 2026.
<https://cyanite.ai/blog/similar-song-finder-ai/>

G. Kreković. "Insights in habits and attitudes regarding programming
sound synthesizers: A quantitative study." In Proceedings of the 16th
Sound and Music Computing Conference (SMC 2019), 2019.
<https://smc2019.uma.es/articles/S4/S4_03_SMC2019_paper.pdf>

Help Musicians and Musicians’ Union. "UK Musicians’ Census: Financial
Insight Report (N=6,000)." London, UK, September 2023.
<https://static1.squarespace.com/static/6398a2cf26f9de4e45e94dd7/t/64fae3635773f313b194d963/1694163834806/MC23+Report+0923.pdf>

IFPI. "Global Music Report 2026: State of the Recorded Music Industry."
International Federation of the Phonographic Industry, London, UK, 2026.
<https://www.ifpi.org>

J. Baumann and C. Mendler-Dünner. "Algorithmic collective action in
recommender systems: Promoting songs by reordering playlists." In
Advances in Neural Information Processing Systems (NeurIPS 2024),
arXiv:2404.04269, 2024.

J. G. Schloss. "Making Beats: The Art of Sample-Based Hip-Hop (2nd
ed.)." Wesleyan University Press, Middletown, CT, 2014.

K. Andersen and P. Knees. "Conversations with expert users in music
retrieval and research challenges for creative MIR." In Proceedings of
the 17th International Society for Music Information Retrieval
Conference (ISMIR 2016), pages 122–128, 2016.
<https://archives.ismir.net/ismir2016/paper/000246.pdf>

M. J. Bates. "The design of browsing and berrypicking techniques for the
online search interface." Online Review, 13(5):407–424, 1989.
<https://www.emerald.com/oir/article/13/5/407/315058/The-design-of-browsing-and-berrypicking-techniques>

MIDiA Research. "Music Subscriber Market Shares Q4 2025/2026: The Chess
Board is Set." MIDiA Research, 2026. <https://www.midiaresearch.com>

Music Business Worldwide. "Music streaming platforms now host quarter of
a billion tracks: Luminate Catalog Report." January 14, 2026.
<https://www.musicbusinessworldwide.com/quarter-of-a-billion-tracks-now-sit-on-music-streaming-services-where-does-it-end/>

Music Business Worldwide. "Splice, which hit nearly 350m downloads in
2024, reveals the fastest-growing genres on its platform." January 23,
2025.
<https://www.musicbusinessworldwide.com/splice-which-hit-nearly-350m-downloads-in-2024-reveals-the-fastest-growing-genres-on-its-platform/>

MusicRadar. "Unlock instant inspiration with this browser-based YouTube
sample finder." MusicRadar Review, July 25, 2024.
<https://www.musicradar.com/news/samplette>

PNAS. "Disrupted routines anticipate musical exploration." Proceedings
of the National Academy of Sciences, 120(45), 2023.
<https://www.pnas.org/doi/10.1073/pnas.2306549121>

RouteNote. "Tracklib: The ultimate platform for music sampling."
RouteNote Radar, March 25, 2026.
<https://routenote.com/radar/tracklib-the-ultimate-platform-for-music-sampling/>

Samplette. "Samplette: Where music discovers you." Web-based
Crate-Digging Application, 2026. <https://samplette.io/>

Splice. "Introducing the Splice Sounds Plugin Beta." Splice Engineering
Blog, April 3, 2026.
<https://splice.com/blog/introducing-splice-sounds-plugin-beta/>

Splice. "Use Similar Sounds to find samples on Splice." Splice Blog,
December 1, 2022. <https://splice.com/blog/introducing-similar-sounds/>

Splice Help Center. "How to use Describe a Sound in the Splice Desktop
App." Knowledge Base, February 18, 2026.
<https://support.splice.com/en/articles/13764370-how-to-use-describe-a-sound-in-the-splice-desktop-app>

Splice Help Center. "How to use Search with Sound (Splice Sounds
Plugin)." Knowledge Base, August 7, 2026.
<https://support.splice.com/en/articles/13860589-how-to-use-search-with-sound-splice-sounds-plugin>

Spotify. "Spotify Developer Policy and Content Restrictions." May 15,
2025. <https://developer.spotify.com/policy>

Spotify Newsroom. "Meet SongDNA, a new beta feature that reveals the
creative connections behind your favorite tracks." March 24, 2026.
<https://newsroom.spotify.com/2026-03-24/songdna-announcement-beta/>

WhoSampled. "Exploring sample sources, cover songs, and musical
remixes." Community Music Database, 2026. <https://www.whosampled.com/>

Spotify Newsroom. "Three new ways to dive deeper into the music you
love." April 20, 2026.
<https://newsroom.spotify.com/2026-04-20/deeper-music-features-about-the-song-dj-songdna/>

Spotify Support. "SongDNA: Exploring song relationships and credits."
Support Article, 2026.
<https://support.spotify.com/us/artists/article/songdna/>

Spotify for Developers. "Changes to the Web API: Deprecation of
Recommendations and Audio Analysis Endpoints." Developer Blog, November
27, 2024.
<https://developer.spotify.com/blog/2024-11-27-changes-to-the-web-api>

Spotify for Developers. "February 2026 Web API Dev Mode Changes:
Migration Guide and Quota Limits." Developer Documentation, February
2026.
<https://developer.spotify.com/documentation/web-api/tutorials/february-2026-migration-guide>

Tracklib. "The State of Sampling 2022: Billboard Hot 100 Analysis."
December 13, 2022.
<https://www.tracklib.com/blog/state-of-sampling-2022>

Tracklib. "State of the Producer: 2024 Producer and AI Sampling Survey
(N=1,107)." Tracklib Research Report, August 2024.
<https://www.musikindustrin.se/wp/wp-content/uploads/2024/08/AI-music-production-survey-2024.pdf>

Tracklib Press. "Tracklib Catalog and Licensable Sound Library
Overview." Press Kit, 2026. <https://www.tracklib.com/press>

V. Ávila Torres and D. Beer. "Music streaming, cultural consumption and
the everyday routines of algorithm management: Exploring how trust and
objective setting shape everyday encounters with algorithmic systems."
Cultural Sociology, SAGE Publications, 2025.
<https://journals.sagepub.com/doi/10.1177/13675494251329239>

VICE. "Dusty but digital: How producers went from crate digging to
YouTube surfing." VICE Music, February 23, 2014.
<https://www.vice.com/en/article/dusty-but-digital-how-producers-went-from-crate-digging-to-youtube-surfing/>

Y. Zhang, Z. Zhang, and Z. Duan. "Sound search by text description or
vocal imitation? Evaluating semantic gaps in audio retrieval." In
Proceedings of Machine Learning Research, arXiv:1907.08661, 2019.
<https://arxiv.org/abs/1907.08661>

TechCrunch. "Music streamer Deezer says more than 50% of daily uploads
are AI-generated." TechCrunch Media, July 21, 2026.
<https://techcrunch.com/2026/07/21/music-streamer-deezer-says-more-than-50-of-daily-uploads-are-ai-generated/>

MusicTech. "82% of music producers oppose AI-generated music, new
Tracklib survey reveals." MusicTech Industry Report, February 18, 2025.
<https://musictech.com/news/industry/tracklib-producer-survey-ai-music-opposition-2025/>

B. Weck, I. Manco, E. Benetos, E. Quinton, G. Fazekas, and D. Bogdanov.
"MuChoMusic: Evaluating music understanding in multimodal audio-language
models." In Proceedings of the 25th International Society for Music
Information Retrieval Conference (ISMIR 2024), 2024.
<https://arxiv.org/abs/2408.01337>

S. Sakshi et al. "Evaluating multimodal audio-language foundation models
across complex acoustic benchmarks." arXiv preprint, arXiv:2501.08920,
2025. <https://arxiv.org/abs/2501.08920>

A. Laplante and J. S. Downie. "Everyday life music information-seeking
behaviour of young adults: An exploratory study." Journal of
Documentation, 62(5):581–600, 2006.
<https://doi.org/10.1108/00220410610688723>

A. Demetriou, A. J. Cunningham, and G. Tzanetakis. "How music producers
search for sound: Characterizing user intentions and retrieval workflows
in music production." In Audio Engineering Society Convention 144, 2018.
<https://www.aes.org/e-lib/browse.cfm?elib=19472>

S. J. Cunningham, D. Bainbridge, and D. McKay. "Finding new music: A
diary study of everyday encounters with novel songs." In Proceedings of
the 8th International Conference on Music Information Retrieval (ISMIR
2007), 2007. <https://archives.ismir.net/ismir2007/paper/000083.pdf>

A. Flexer. "On inter-rater agreement in audio music similarity." In
Proceedings of the 15th International Society for Music Information
Retrieval Conference (ISMIR 2014), 2014.
<https://archives.ismir.net/ismir2014/paper/000256.pdf>

Deezer Newsroom. "Get in touch with your feelings with Flow Moods."
Press Release, October 6, 2021.
<https://newsroom-deezer.com/2021/10/get-in-touch-with-your-feelings-with-flow-moods/>

Digital Music News. "Spotify AI DJ adds support for voice-based music
requests." Digital Music News, May 13, 2025.
<https://www.digitalmusicnews.com/2025/05/13/spotify-ai-dj-requests/>

TechRadar. "I dismissed Spotify’s AI DJ for years – here’s why I’m
finally warming up to the streaming giant’s most divisive feature."
TechRadar Audio, June 20, 2025.
<https://www.techradar.com/audio/spotify/i-dismissed-spotifys-ai-dj-for-years-heres-why-im-finally-warming-up-to-the-streaming-giants-most-divisive-feature>

TechRadar. "I used Spotify’s AI playlist feature for the first time in a
year, and it’s way better than I remember – but there’s still room for
improvement." TechRadar Audio, June 26, 2025.
<https://www.techradar.com/audio/spotify/i-used-spotifys-ai-playlist-feature-for-the-first-time-in-a-year-and-its-way-better-than-i-remember-but-theres-still-room-for-improvement>

Attack Magazine. "Reviewing Tracklib, a record store for sampling."
Attack Magazine Gear & Software, June 29, 2022.
<https://www.attackmagazine.com/reviews/gear-software/reviewing-tracklib-a-record-store-for-sampling/>

Music Business Worldwide. "Three quarters of music producers don’t use
AI, and 82% of those cite artistic reasons: Tracklib survey." Music
Business Worldwide, August 14, 2024.
<https://www.musicbusinessworldwide.com/three-quarters-of-music-producers-dont-use-ai-and-82-of-those-cite-artistic-reasons-tracklib-survey/>

Music Business Worldwide. "Tracklib expands beyond master recordings
with launch of royalty-free Sounds library." Music Business Worldwide,
April 16, 2024.
<https://www.musicbusinessworldwide.com/tracklib-sounds-launch-2024/>

MusicRadar. "Why type beats have taken over music production: How
beatmakers game search engines." MusicRadar Tech, March 14, 2023.
<https://www.musicradar.com/news/type-beat-music-production-culture/>

We Rave You. "Study reveals that YouTube leads the way in new music
discovery." Industry Studies, October 14, 2025.
<https://weraveyou.com/2025/10/study-reveals-that-youtube-leads-the-way-in-new-music-discovery/>

Last.fm. "How Last.fm recommendations and listening data work." Last.fm
Knowledge Base, 2024. <https://www.last.fm/about/track-recommendations>

Habr. "Yandex Music adds unfamiliar track and language controls to My
Wave stream \[In Russian\]." Habr News, March 16, 2023.
<https://habr.com/ru/news/722744/>

Habr. "VK Music updates algorithmic search and multi-factor stream
filters \[In Russian\]." Habr News, January 28, 2025.
<https://habr.com/ru/news/877420/>

I. Baracskay, D. J. Baracskay III, M. Iqbal, and B. P. Knijnenburg. "The
diversity of music recommender systems." In 27th International
Conference on Intelligent User Interfaces (IUI ’22 Companion), 2022.
<https://par.nsf.gov/servlets/purl/10402477>

J. Garcia-Gathright, B. St. Thomas, C. Hosey, Z. Nazari, and F. Diaz.
"Understanding and evaluating user satisfaction with music discovery."
In Proceedings of the 41st International ACM SIGIR Conference on
Research and Development in Information Retrieval, pp. 55–64, 2018.
<https://doi.org/10.1145/3209978.3210049>
