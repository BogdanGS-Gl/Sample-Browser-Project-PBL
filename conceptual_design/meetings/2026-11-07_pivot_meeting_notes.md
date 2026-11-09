# PBL Team 16 — Meeting Notes (Pre-Midterm 2 Pivot & Validation Prep)

**Project Name:** Better Spotify / Sample Browser  
**Course:** FAF.PCAS25.1 (Fall 2026)  
**Mentor:** Prof. Elena Graur  
**Date & Time:** November 6–7, 2026  
**Format:** Online Working Session (Telegram + Document Co-Editing)  
**Attendees:**  
- Bogdan Glavan (FAF-261) — Team Leader / Domain & Solution Architecture  
- Leonid Tiscenco (FAF-263) — Methodology, Audit & Hypothesis Structuring  
- Andrei Simon (FAF-261) — Initial Hypothesis & Interview Questionnaire Drafting  
- Nikita Creciun (FAF-263) — Problem Statement & SWOT Alignment  
- Mihai-Constantin Sîrghii (FAF-262) — Target Group & Persona Alignment  

---

## 1. Meeting Agenda
1. Review mentor feedback from Midterm 1 regarding logical gaps across Problem Statement, Solution Proposal, and Validation Hypotheses.
2. Resolve the internal architectural contradiction between the *Vocabulary Gap* literature in the Problem Description and the *Tag-Based Search* in the Solution Proposal.
3. Finalize technical and legal boundaries for YouTube integration (eliminating server-side audio processing in favor of timestamp/URL pointer indexing).
4. Review, critique, and refine Andrei and Bogdan's proposed hypotheses (`H1–H5`) and interview script (`Q1–Q10`).
5. Establish a contingency pivot strategy (Public Community Catalog vs. Personal Crate-Digging Workspace) based on upcoming interview results.
6. Define the interview methodology and producer recruitment plan prior to the next mentor meeting.

---

## 2. Key Discussions & Architectural Decisions

### 2.1. Eliminating Audio Processing & Resolving the "Vocabulary Gap" Contradiction
* **Issue Identified (Leonid):** In the Midterm 1 report, Section 2.1 argued at length that musicians cannot describe timbre in words and that human text tags are subjective (*The Vocabulary Gap*), which directly contradicted a solution relying on user-submitted text tags over YouTube videos (since YouTube API policies prohibit downloading audio for automated AI/MIR analysis).
* **Solution Proposal (Bogdan & Leonid):**
  * **Zero Audio Processing:** We completely drop any programmatic server-side audio analysis of YouTube videos. The database will store **only video URLs/IDs, sub-track timestamps (`start_time`, `end_time`), and structured tags**.
  * **Reframing the Problem Focus:** We shift the primary problem focus away from "inability to describe timbre in words" toward **Sub-Track Structural Blindness**—the fact that streaming platforms only index whole tracks, forcing producers to waste time manually scrubbing through 5-minute recordings to find short (4–30s), structurally clean sections (such as vocal-free instrumentals or isolated drum breaks).
  * **Two-Tier Tag Taxonomy:** To solve tag disagreement without AI audio analysis, we replace unconstrained free-text tagging with:
    1. **Primary Preset Objective Tags (Mandatory, High Priority):** Pre-written, verifiable categories selected in clicks—*Isolation* (`[No Vocals]`, `[No Drums]`, `[Isolated Drum Break]`, `[Solo Instrument]`), *Instrumentation* (`[Rhodes]`, `[Guitar]`, `[Bass]`, `[Strings]`, etc.), and *Section Role* (`[Intro]`, `[Break]`, `[Solo]`, `[Outro]`).
    2. **Secondary Contextual Tags (Optional, Lower Priority):** Moderated style/texture tags inspired by RateYourMusic and Splice, kept visually compact so they do not clutter the UI, and always paired with instant audio playback of the segment to remove ambiguity.

### 2.2. Contingency Pivot Strategy (Public Catalog vs. Personal Digging Workspace)
* **Discussion:** Leonid raised the risk of producer *gatekeeping* (producers hiding rare sample finds from competitors) and cold-start friction in manual crowdsourcing, proposing an alternative pivot toward a personal **"Crate-Digging & Auditioning Workspace"** (Smart Crates). Bogdan noted that while basic bookmarking tools exist (e.g., *sampledigging.online*, *chop-stop.com*), none allow structured sub-track tagging to remember *why* a section was saved without messy file-naming conventions. Bogdan also counter-argued that many producers do share sample sources (as seen on *WhoSampled* and community forums) because production originality comes from *how* a sample is flipped, not just the source.
* **Consensus Decision:** Keep the **Two-Tier Tagged Sample Browser** as our primary concept for the interviews, and test producer sharing vs. personal bookmarking directly via **Hypothesis H3**. If interviews show producers refuse to share tags publicly, we will execute a fast, documented Midterm 2 pivot to the **Personal Tagged Crate-Digging Workspace**.

### 2.3. Revision of Hypotheses (From H1–H5 to Falsifiable H1–H4)
* **H1 (Refined):** Shifted from an unverifiable claim about future app speed to a problem-focused hypothesis: *Sample hunting in full songs involves wasting time manually scrubbing through sections that do not match the producer's structural/isolation goals.* ( wording adjusted per Bogdan's feedback to say *"time"* rather than *"studio time"*).
* **H2 (Cut & Merged):** The previous hypothesis about attracting non-sampling beginners or winning users solely through "simpler UI" was dropped because it cannot be verified via oral interviews and contradicts our target group definition.
* **H2 (New — formerly H3):** Focused on *Objective vs. Subjective Tags & Berrypicking*: testing which tag categories producers actually trust vs. ignore, whether instant segment playback resolves tag ambiguity, and whether producers prefer finding related samples directly from tags on a sample page they are listening to (*berrypicking* model).
* **H3 (New — formerly H4):** Focused on *Personal Sample Organization, Timestamp Tracking & Willingness to Contribute*: verifying how producers currently store found samples/links, how they track timestamps, and whether preset tagging for their own library translates into public catalog sharing.
* **H4 (New — formerly H5):** Focused on *Target Segment Behavior*: verifying that small-scale/independent producers sample for non-commercial/creative purposes as well and prefer unlicensed full-track digging (YouTube/Samplette) over paid pre-curated libraries (Splice/Tracklib).

### 2.4. Revision of the Interview Guide (`Q1–Q10`)
* Split multi-part questions so interviewees answer one clear prompt at a time.
* Re-introduced a focused walkthrough of the **most recent full-track sample search session** (Q5–Q6) to anchor answers in real past behavior rather than generic speculation.
* Replaced trivial yes/no questions ("Does hearing a sample before downloading make a difference?") with specific questions on tag filtering behavior, berrypicking navigation, timestamp bookmarking, and sharing vs. gatekeeping.

---

## 3. Action Items Before Next Mentor Meeting

| Task | Owner(s) | Status |
| :--- | :--- | :--- |
| Draft initial hypotheses & producer-oriented interview questions | Andrei Simon & Bogdan Glavan | Completed |
| Methodological audit & synthesis of revised Problem, Solution, Hypotheses (H1–H4), and Interview Protocol | Leonid Tiscenco & Bogdan Glavan | Completed |
| Review final formatted document (`Sample_Browser_Revised_Framework_and_Interview_Protocol.md`) with all team members | All Team Members | Ready for Mentor Review |
| Present revised Problem Statement, Solution boundaries, Hypotheses, and Interview Guide to Prof. Elena Graur via MS Teams / next meeting for sign-off | All Team Members | Next Mentor Meeting |
| Conduct $N \approx 20$ video interviews (in English/Romanian/Russian across known musician contacts, Instagram artist DMs, Discord beat-battle servers, and YouTube sample-flip creators) + distribute backing Google Forms survey | All Team Members (~4 interviews each) | Pending Mentor Sign-Off |
