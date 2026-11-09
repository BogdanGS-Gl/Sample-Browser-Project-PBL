#!/usr/bin/env python3
import os
import subprocess

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
OUT_DIR = os.path.join(PROJECT_ROOT, "report", "images")
os.makedirs(OUT_DIR, exist_ok=True)

def render_svg_to_png(svg_content, out_png_path, width, height):
    svg_path = out_png_path.replace('.png', '.svg')
    with open(svg_path, 'w', encoding='utf-8') as f:
        f.write(svg_content)
    
    cmd = ['inkscape', svg_path, '-o', out_png_path, f'--export-width={width}', f'--export-height={height}']
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Error rendering {out_png_path}: {res.stderr}")
        raise RuntimeError(f"Inkscape failed for {out_png_path}")
    print(f"Successfully generated {out_png_path} ({width}x{height})")

# =========================================================================
# 1. problem_bottlenecks.png (3900 x 2520)
# =========================================================================
def generate_problem_bottlenecks():
    w, h = 3900, 2520
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0F172A"/>
      <stop offset="100%" stop-color="#1E293B"/>
    </linearGradient>
    <linearGradient id="cardGrad1" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#1E293B"/>
      <stop offset="100%" stop-color="#0F172A"/>
    </linearGradient>
    <linearGradient id="redGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#EF4444"/>
      <stop offset="100%" stop-color="#DC2626"/>
    </linearGradient>
    <linearGradient id="amberGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#F59E0B"/>
      <stop offset="100%" stop-color="#D97706"/>
    </linearGradient>
    <linearGradient id="emeraldGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#10B981"/>
      <stop offset="100%" stop-color="#059669"/>
    </linearGradient>
  </defs>

  <!-- Background Canvas -->
  <rect width="{w}" height="{h}" fill="url(#bgGrad)"/>
  
  <!-- Subtle Grid Overlay -->
  <g opacity="0.05" stroke="#94A3B8" stroke-width="2">
    {''.join(f'<line x1="{x}" y1="0" x2="{x}" y2="{h}"/>' for x in range(0, w, 150))}
    {''.join(f'<line x1="0" y1="{y}" x2="{w}" y2="{y}"/>' for y in range(0, h, 150))}
  </g>

  <!-- Header Section -->
  <g transform="translate(150, 100)">
    <!-- Pill -->
    <rect x="0" y="0" width="760" height="56" rx="28" fill="#334155" stroke="#475569" stroke-width="2"/>
    <text x="380" y="36" fill="#38BDF8" font-family="Inter, DejaVu Sans, sans-serif" font-size="22" font-weight="700" text-anchor="middle" letter-spacing="3">STREAMING RETRIEVAL ANALYSIS • PROBLEM SPACE</text>
    
    <!-- Title -->
    <text x="0" y="140" fill="#F8FAFC" font-family="Inter, DejaVu Sans, sans-serif" font-size="64" font-weight="800" letter-spacing="-1">The Dual Bottlenecks of Sample Discovery in Streaming Architectures</text>
    <text x="0" y="200" fill="#94A3B8" font-family="Inter, DejaVu Sans, sans-serif" font-size="30" font-weight="400">Why Independent Music Producers Waste Significant Time During Manual Crate-Digging Across Full-Track Catalogs</text>
  </g>

  <!-- Two Main Columns -->
  <!-- Left Column: Bottleneck 1 -->
  <g transform="translate(150, 360)">
    <!-- Card Frame -->
    <rect width="1740" height="1620" rx="28" fill="url(#cardGrad1)" stroke="#334155" stroke-width="3"/>
    
    <!-- Top Accent Bar -->
    <rect x="0" y="0" width="1740" height="16" rx="8" fill="url(#redGrad)"/>

    <!-- Header Badge & Number -->
    <rect x="70" y="60" width="460" height="50" rx="12" fill="#7F1D1D" stroke="#EF4444" stroke-width="2"/>
    <text x="300" y="93" fill="#FCA5A5" font-family="Inter, DejaVu Sans, sans-serif" font-size="22" font-weight="700" text-anchor="middle" letter-spacing="2">STRUCTURAL LIMITATION • BOTTLENECK 01</text>
    
    <!-- Title -->
    <text x="70" y="170" fill="#F8FAFC" font-family="Inter, DejaVu Sans, sans-serif" font-size="44" font-weight="800">Sub-Track Structural Blindness (Whole-Track Indexing)</text>
    <text x="70" y="220" fill="#94A3B8" font-family="Inter, DejaVu Sans, sans-serif" font-size="26">Streaming platforms treat full recordings as undivided monolithic files, hiding usable passages.</text>

    <!-- Sub-Box 1: What Platforms Index -->
    <g transform="translate(70, 270)">
      <rect width="1600" height="340" rx="20" fill="#0F172A" stroke="#334155" stroke-width="2"/>
      <rect x="40" y="36" width="340" height="40" rx="8" fill="#1E293B"/>
      <text x="210" y="63" fill="#38BDF8" font-family="Inter, DejaVu Sans, sans-serif" font-size="19" font-weight="700" text-anchor="middle">STREAMING PLATFORM BEHAVIOR</text>
      
      <circle cx="60" cy="125" r="8" fill="#EF4444"/>
      <text x="85" y="132" fill="#E2E8F0" font-family="Inter, DejaVu Sans, sans-serif" font-size="24" font-weight="600">Indexes metadata exclusively at whole-track level:</text>
      <text x="85" y="165" fill="#94A3B8" font-family="Inter, DejaVu Sans, sans-serif" font-size="22">Title, Artist, Album, Global Genre, Release Year, and Global Track BPM (YouTube, Samplette, Spotify).</text>

      <circle cx="60" cy="225" r="8" fill="#EF4444"/>
      <text x="85" y="232" fill="#E2E8F0" font-family="Inter, DejaVu Sans, sans-serif" font-size="24" font-weight="600">Monolithic 3-to-6 minute audio containers:</text>
      <text x="85" y="265" fill="#94A3B8" font-family="Inter, DejaVu Sans, sans-serif" font-size="22">Zero indexing of internal section transitions, solo instruments, or localized rhythm breakdown boundaries.</text>
    </g>

    <!-- Sub-Box 2: What Producers Actually Need -->
    <g transform="translate(70, 650)">
      <rect width="1600" height="340" rx="20" fill="#0F172A" stroke="#334155" stroke-width="2"/>
      <rect x="40" y="36" width="350" height="40" rx="8" fill="#1E293B"/>
      <text x="215" y="63" fill="#10B981" font-family="Inter, DejaVu Sans, sans-serif" font-size="19" font-weight="700" text-anchor="middle">PRODUCER DISCOVERY REALITY</text>
      
      <circle cx="60" cy="125" r="8" fill="#10B981"/>
      <text x="85" y="132" fill="#E2E8F0" font-family="Inter, DejaVu Sans, sans-serif" font-size="24" font-weight="600">Producers rarely sample entire songs:</text>
      <text x="85" y="165" fill="#94A3B8" font-family="Inter, DejaVu Sans, sans-serif" font-size="22">They search for localized 4-to-30 second structural isolates (unlayered 2-to-8 bar intervals).</text>

      <circle cx="60" cy="225" r="8" fill="#10B981"/>
      <text x="85" y="232" fill="#E2E8F0" font-family="Inter, DejaVu Sans, sans-serif" font-size="24" font-weight="600">High-demand acoustic passage categories:</text>
      <text x="85" y="265" fill="#94A3B8" font-family="Inter, DejaVu Sans, sans-serif" font-size="22">Isolated drum breaks, solo Rhodes/piano intros without vocals, clean basslines, or unlayered horn riffs.</text>
    </g>

    <!-- Sub-Box 3: The Induced Friction -->
    <g transform="translate(70, 1030)">
      <rect width="1600" height="490" rx="20" fill="#18181B" stroke="#450A0A" stroke-width="2"/>
      <rect x="40" y="36" width="380" height="40" rx="8" fill="#7F1D1D"/>
      <text x="230" y="63" fill="#FCA5A5" font-family="Inter, DejaVu Sans, sans-serif" font-size="19" font-weight="700" text-anchor="middle">INDUCED WORKFLOW BOTTLENECK</text>
      
      <!-- Visual Timeline Diagram showing scrubbing chaos -->
      <g transform="translate(40, 105)">
        <rect width="1520" height="80" rx="14" fill="#0F172A" stroke="#334155" stroke-width="2"/>
        <text x="30" y="47" fill="#64748B" font-family="Inter, DejaVu Sans, sans-serif" font-size="20">0:00 (Track Start)</text>
        <text x="1480" y="47" fill="#64748B" font-family="Inter, DejaVu Sans, sans-serif" font-size="20" text-anchor="end">5:12 (Track End)</text>
        
        <!-- Scrubbing Arrows -->
        <path d="M 220 40 Q 380 15 540 40 Q 700 65 860 40 Q 1020 15 1180 40" fill="none" stroke="#EF4444" stroke-width="4" stroke-dasharray="10 8"/>
        <circle cx="220" cy="40" r="10" fill="#EF4444"/>
        <circle cx="540" cy="40" r="10" fill="#EF4444"/>
        <circle cx="860" cy="40" r="10" fill="#EF4444"/>
        <circle cx="1180" cy="40" r="10" fill="#EF4444"/>
        
        <!-- Hidden target -->
        <rect x="830" y="20" width="160" height="40" rx="8" fill="#10B981" opacity="0.3"/>
        <text x="910" y="46" fill="#A7F3D0" font-family="Inter, DejaVu Sans, sans-serif" font-size="16" font-weight="700" text-anchor="middle">Target Break (8s)</text>
      </g>

      <text x="40" y="240" fill="#F8FAFC" font-family="Inter, DejaVu Sans, sans-serif" font-size="26" font-weight="700">Repetitive Playhead Scrubbing &amp; Creative Fatigue:</text>
      <text x="40" y="280" fill="#CBD5E1" font-family="Inter, DejaVu Sans, sans-serif" font-size="23" font-weight="400">Producers must drag playheads back and forth through 50+ full songs per digging session.</text>
      <text x="40" y="320" fill="#CBD5E1" font-family="Inter, DejaVu Sans, sans-serif" font-size="23" font-weight="400">Section collisions (vocals or drums bleeding over a riff) ruin promising tracks after minutes of search.</text>
      
      <!-- Metrics Pill -->
      <rect x="40" y="370" width="1520" height="80" rx="16" fill="#27272A" stroke="#3F3F46" stroke-width="2"/>
      <text x="80" y="420" fill="#EF4444" font-family="Inter, DejaVu Sans, sans-serif" font-size="24" font-weight="800">CONSEQUENCE:</text>
      <text x="280" y="420" fill="#E2E8F0" font-family="Inter, DejaVu Sans, sans-serif" font-size="23" font-weight="600">15–25 min spent per single usable isolate • High session abandonment rate • Lost creative flow</text>
    </g>
  </g>

  <!-- Right Column: Bottleneck 2 -->
  <g transform="translate(2010, 360)">
    <!-- Card Frame -->
    <rect width="1740" height="1620" rx="28" fill="url(#cardGrad1)" stroke="#334155" stroke-width="3"/>
    
    <!-- Top Accent Bar -->
    <rect x="0" y="0" width="1740" height="16" rx="8" fill="url(#amberGrad)"/>

    <!-- Header Badge & Number -->
    <rect x="70" y="60" width="480" height="50" rx="12" fill="#78350F" stroke="#F59E0B" stroke-width="2"/>
    <text x="310" y="93" fill="#FDE68A" font-family="Inter, DejaVu Sans, sans-serif" font-size="22" font-weight="700" text-anchor="middle" letter-spacing="2">TAXONOMY &amp; STORAGE • BOTTLENECK 02</text>
    
    <!-- Title -->
    <text x="70" y="170" fill="#F8FAFC" font-family="Inter, DejaVu Sans, sans-serif" font-size="44" font-weight="800">Unconstrained Text Ambiguity &amp; Bookmarking Friction</text>
    <text x="70" y="220" fill="#94A3B8" font-family="Inter, DejaVu Sans, sans-serif" font-size="26">Subjective keywords fail across listeners, and full-track bookmarks cause timestamp amnesia.</text>

    <!-- Sub-Box 1: Subjective Text Failure -->
    <g transform="translate(70, 270)">
      <rect width="1600" height="340" rx="20" fill="#0F172A" stroke="#334155" stroke-width="2"/>
      <rect x="40" y="36" width="370" height="40" rx="8" fill="#1E293B"/>
      <text x="225" y="63" fill="#F59E0B" font-family="Inter, DejaVu Sans, sans-serif" font-size="19" font-weight="700" text-anchor="middle">SUBJECTIVE DESCRIPTOR AMBIGUITY</text>
      
      <circle cx="60" cy="125" r="8" fill="#F59E0B"/>
      <text x="85" y="132" fill="#E2E8F0" font-family="Inter, DejaVu Sans, sans-serif" font-size="24" font-weight="600">Musicians rely on subjective metaphors (Andersen &amp; Knees, 2016):</text>
      <text x="85" y="165" fill="#94A3B8" font-family="Inter, DejaVu Sans, sans-serif" font-size="22">Adjectives like "warm", "dusty", "hollow", "dark", or "vintage" have no agreed acoustic consensus.</text>

      <circle cx="60" cy="225" r="8" fill="#F59E0B"/>
      <text x="85" y="232" fill="#E2E8F0" font-family="Inter, DejaVu Sans, sans-serif" font-size="24" font-weight="600">Low inter-rater agreement on perceptual music labels (Flexer, 2014):</text>
      <text x="85" y="265" fill="#94A3B8" font-family="Inter, DejaVu Sans, sans-serif" font-size="22">Unconstrained free-text tags pollute databases and yield high query mismatch without auditory preview.</text>
    </g>

    <!-- Sub-Box 2: Bookmarking Failure -->
    <g transform="translate(70, 650)">
      <rect width="1600" height="340" rx="20" fill="#0F172A" stroke="#334155" stroke-width="2"/>
      <rect x="40" y="36" width="410" height="40" rx="8" fill="#1E293B"/>
      <text x="245" y="63" fill="#38BDF8" font-family="Inter, DejaVu Sans, sans-serif" font-size="19" font-weight="700" text-anchor="middle">SUB-TRACK BOOKMARKING AMNESIA</text>
      
      <circle cx="60" cy="125" r="8" fill="#38BDF8"/>
      <text x="85" y="132" fill="#E2E8F0" font-family="Inter, DejaVu Sans, sans-serif" font-size="24" font-weight="600">Standard web bookmarks and YouTube playlists save only full URLs:</text>
      <text x="85" y="165" fill="#94A3B8" font-family="Inter, DejaVu Sans, sans-serif" font-size="22">Zero native support for capturing start/end timestamps, loop intervals, or instrumental notes.</text>

      <circle cx="60" cy="225" r="8" fill="#38BDF8"/>
      <text x="85" y="232" fill="#E2E8F0" font-family="Inter, DejaVu Sans, sans-serif" font-size="24" font-weight="600">Returning to saved links requires recurring re-scrubbing overhead:</text>
      <text x="85" y="265" fill="#94A3B8" font-family="Inter, DejaVu Sans, sans-serif" font-size="22">Producers forget which timestamp contained the sample idea, wasting time re-auditioning whole songs.</text>
    </g>

    <!-- Sub-Box 3: The Storage & Curation Breakdown -->
    <g transform="translate(70, 1030)">
      <rect width="1600" height="490" rx="20" fill="#18181B" stroke="#451A03" stroke-width="2"/>
      <rect x="40" y="36" width="370" height="40" rx="8" fill="#78350F"/>
      <text x="225" y="63" fill="#FDE68A" font-family="Inter, DejaVu Sans, sans-serif" font-size="19" font-weight="700" text-anchor="middle">INDUCED WORKFLOW BOTTLENECK</text>
      
      <!-- Visual Bookmarking Chaos -->
      <g transform="translate(40, 105)">
        <rect width="1520" height="80" rx="14" fill="#0F172A" stroke="#334155" stroke-width="2"/>
        <text x="30" y="47" fill="#64748B" font-family="Inter, DejaVu Sans, sans-serif" font-size="20">Saved: youtube.com/watch?v=k9X... [Playlist: "Samples to Chop 2026"]</text>
        <rect x="1100" y="20" width="380" height="40" rx="8" fill="#EF4444" opacity="0.3"/>
        <text x="1290" y="47" fill="#FCA5A5" font-family="Inter, DejaVu Sans, sans-serif" font-size="18" font-weight="700" text-anchor="middle">⚠️ Timestamp / Notes Lost</text>
      </g>

      <text x="40" y="240" fill="#F8FAFC" font-family="Inter, DejaVu Sans, sans-serif" font-size="26" font-weight="700">Sub-Track Reference Loss &amp; Curation Friction:</text>
      <text x="40" y="280" fill="#CBD5E1" font-family="Inter, DejaVu Sans, sans-serif" font-size="23" font-weight="400">Producers maintain chaotic notes in text files or download gigabytes of raw rips to local SSDs.</text>
      <text x="40" y="320" fill="#CBD5E1" font-family="Inter, DejaVu Sans, sans-serif" font-size="23" font-weight="400">Without structured sub-track tagging, saved catalogs become dark, unsearchable archives.</text>
      
      <!-- Metrics Pill -->
      <rect x="40" y="370" width="1520" height="80" rx="16" fill="#27272A" stroke="#3F3F46" stroke-width="2"/>
      <text x="80" y="420" fill="#F59E0B" font-family="Inter, DejaVu Sans, sans-serif" font-size="24" font-weight="800">CONSEQUENCE:</text>
      <text x="280" y="420" fill="#E2E8F0" font-family="Inter, DejaVu Sans, sans-serif" font-size="23" font-weight="600">Disorganized sample archives • Lost creative momentum • Recurring scrubbing overhead</text>
    </g>
  </g>

  <!-- Bottom Banner: Sample Browser Solution Intervention -->
  <g transform="translate(150, 2040)">
    <rect width="3600" height="380" rx="28" fill="#0F172A" stroke="#10B981" stroke-width="4"/>
    
    <g transform="translate(60, 45)">
      <rect width="660" height="44" rx="10" fill="#064E3B"/>
      <text x="330" y="30" fill="#6EE7B7" font-family="Inter, DejaVu Sans, sans-serif" font-size="18" font-weight="800" text-anchor="middle" letter-spacing="3">SAMPLE BROWSER ARCHITECTURAL INTERVENTION</text>
      
      <text x="0" y="115" fill="#F8FAFC" font-family="Inter, DejaVu Sans, sans-serif" font-size="44" font-weight="800">Sub-Track Timestamp Indexing (4–60s) • Two-Tier Preset Tag Taxonomy • Instant Cue-Seeking &amp; Looping</text>
      <text x="0" y="170" fill="#94A3B8" font-family="Inter, DejaVu Sans, sans-serif" font-size="26">Shifts the atomic unit of music discovery from 5-minute monolithic songs to localized 4-to-30s musical passages.</text>
    </g>

    <!-- 3 Key Solution Highlights -->
    <g transform="translate(60, 245)">
      <rect x="0" y="0" width="1120" height="90" rx="16" fill="#1E293B" stroke="#334155" stroke-width="2"/>
      <text x="30" y="38" fill="#34D399" font-family="Inter, DejaVu Sans, sans-serif" font-size="22" font-weight="700">1. Granular Passage Pointers</text>
      <text x="30" y="68" fill="#94A3B8" font-family="Inter, DejaVu Sans, sans-serif" font-size="20">Jump directly to [start_time, end_time] cue points</text>

      <rect x="1170" y="0" width="1120" height="90" rx="16" fill="#1E293B" stroke="#334155" stroke-width="2"/>
      <text x="1200" y="38" fill="#34D399" font-family="Inter, DejaVu Sans, sans-serif" font-size="22" font-weight="700">2. Two-Tier Objective Presets</text>
      <text x="1200" y="68" fill="#94A3B8" font-family="Inter, DejaVu Sans, sans-serif" font-size="20">[No Vocals], [No Drums], [Rhodes] + Instant Audio Preview</text>

      <rect x="2340" y="0" width="1140" height="90" rx="16" fill="#1E293B" stroke="#334155" stroke-width="2"/>
      <text x="2370" y="38" fill="#34D399" font-family="Inter, DejaVu Sans, sans-serif" font-size="22" font-weight="700">3. Personal Cloud Crates</text>
      <text x="2370" y="68" fill="#94A3B8" font-family="Inter, DejaVu Sans, sans-serif" font-size="20">Single-player timestamp bookmarking without audio downloads</text>
    </g>
  </g>
</svg>'''
    render_svg_to_png(svg, f"{OUT_DIR}/problem_bottlenecks.png", w, h)
    # Also update problem_analysis.png if it exists
    render_svg_to_png(svg, f"{OUT_DIR}/problem_analysis.png", w, h)

# =========================================================================
# 2. architecture_overview.png (3900 x 2340)
# =========================================================================
def generate_architecture_overview():
    w, h = 3900, 2340
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">
  <defs>
    <linearGradient id="bgGrad2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0F172A"/>
      <stop offset="100%" stop-color="#1E293B"/>
    </linearGradient>
    <linearGradient id="boxGrad1" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#1E293B"/>
      <stop offset="100%" stop-color="#0F172A"/>
    </linearGradient>
  </defs>

  <rect width="{w}" height="{h}" fill="url(#bgGrad2)"/>
  
  <g opacity="0.05" stroke="#94A3B8" stroke-width="2">
    {''.join(f'<line x1="{x}" y1="0" x2="{x}" y2="{h}"/>' for x in range(0, w, 150))}
    {''.join(f'<line x1="0" y1="{y}" x2="{w}" y2="{y}"/>' for y in range(0, h, 150))}
  </g>

  <!-- Header -->
  <g transform="translate(150, 90)">
    <rect x="0" y="0" width="760" height="56" rx="28" fill="#334155" stroke="#475569" stroke-width="2"/>
    <text x="380" y="36" fill="#10B981" font-family="Inter, DejaVu Sans, sans-serif" font-size="22" font-weight="700" text-anchor="middle" letter-spacing="3">SYSTEM ARCHITECTURE • COMPLIANT POINTER MODEL</text>
    
    <text x="0" y="140" fill="#F8FAFC" font-family="Inter, DejaVu Sans, sans-serif" font-size="64" font-weight="800">Sample Browser: Zero-Media-Hosting Pointer Architecture</text>
    <text x="0" y="195" fill="#94A3B8" font-family="Inter, DejaVu Sans, sans-serif" font-size="28">100% YouTube API (ToS Section III.E) Compliant Client-Side Playback &amp; Sub-Track Metadata Indexing Pipeline</text>
  </g>

  <!-- 4 Main Architectural Columns -->
  <!-- Block 1: Client Web App (React) -->
  <g transform="translate(150, 340)">
    <rect width="840" height="1500" rx="24" fill="url(#boxGrad1)" stroke="#38BDF8" stroke-width="3"/>
    <rect x="0" y="0" width="840" height="16" rx="8" fill="#38BDF8"/>
    
    <rect x="50" y="50" width="300" height="44" rx="10" fill="#0C4A6E"/>
    <text x="200" y="79" fill="#7DD3FC" font-family="Inter, DejaVu Sans, sans-serif" font-size="20" font-weight="700" text-anchor="middle">CLIENT FRONTEND (SPA)</text>
    
    <text x="50" y="150" fill="#F8FAFC" font-family="Inter, DejaVu Sans, sans-serif" font-size="36" font-weight="800">Client Web Application</text>
    <text x="50" y="190" fill="#94A3B8" font-family="Inter, DejaVu Sans, sans-serif" font-size="22">React 19 + TypeScript + Tailwind CSS</text>

    <!-- Component Modules -->
    <g transform="translate(50, 240)">
      <!-- Item 1 -->
      <rect width="740" height="260" rx="18" fill="#0F172A" stroke="#334155" stroke-width="2"/>
      <text x="30" y="50" fill="#38BDF8" font-family="Inter, DejaVu Sans, sans-serif" font-size="26" font-weight="700">Interactive Segmented Timeline (4–60s)</text>
      <text x="30" y="90" fill="#CBD5E1" font-family="Inter, DejaVu Sans, sans-serif" font-size="21">Visual cue markers rendered from PostgreSQL metadata.</text>
      <text x="30" y="125" fill="#CBD5E1" font-family="Inter, DejaVu Sans, sans-serif" font-size="21">Direct timeline seeking &amp; boundary segment highlights.</text>
      <rect x="30" y="160" width="680" height="65" rx="10" fill="#1E293B"/>
      <text x="50" y="200" fill="#10B981" font-family="Inter, DejaVu Sans, sans-serif" font-size="18" font-weight="700">✓ Zero raw PCM audio decoding (sandboxed iframe safety)</text>
    </g>

    <g transform="translate(50, 530)">
      <!-- Item 2 -->
      <rect width="740" height="260" rx="18" fill="#0F172A" stroke="#334155" stroke-width="2"/>
      <text x="30" y="50" fill="#38BDF8" font-family="Inter, DejaVu Sans, sans-serif" font-size="26" font-weight="700">Two-Tier Tag Filter Matrix</text>
      <text x="30" y="90" fill="#CBD5E1" font-family="Inter, DejaVu Sans, sans-serif" font-size="21">Tier 1: Mandatory objective preset buttons (Isolation, Inst, Section).</text>
      <text x="30" y="125" fill="#CBD5E1" font-family="Inter, DejaVu Sans, sans-serif" font-size="21">Tier 2: Collapsible secondary contextual descriptor chips.</text>
      <rect x="30" y="160" width="680" height="65" rx="10" fill="#1E293B"/>
      <text x="50" y="200" fill="#38BDF8" font-family="Inter, DejaVu Sans, sans-serif" font-size="18" font-weight="700">✓ Instant 10s segment audio preview removes ambiguity</text>
    </g>

    <g transform="translate(50, 820)">
      <!-- Item 3 -->
      <rect width="740" height="260" rx="18" fill="#0F172A" stroke="#334155" stroke-width="2"/>
      <text x="30" y="50" fill="#38BDF8" font-family="Inter, DejaVu Sans, sans-serif" font-size="26" font-weight="700">Automated Boundary Audition Player</text>
      <text x="30" y="90" fill="#CBD5E1" font-family="Inter, DejaVu Sans, sans-serif" font-size="21">Client loop listener returns playhead to start_time at end_time.</text>
      <text x="30" y="125" fill="#CBD5E1" font-family="Inter, DejaVu Sans, sans-serif" font-size="21">Rough auditioning loop for evaluating musical sampling potential.</text>
      <rect x="30" y="160" width="680" height="65" rx="10" fill="#1E293B"/>
      <text x="50" y="200" fill="#F59E0B" font-family="Inter, DejaVu Sans, sans-serif" font-size="18" font-weight="700">⚡ Client buffer turnaround latency: ~100–300 ms</text>
    </g>

    <g transform="translate(50, 1110)">
      <!-- Item 4 -->
      <rect width="740" height="260" rx="18" fill="#0F172A" stroke="#334155" stroke-width="2"/>
      <text x="30" y="50" fill="#38BDF8" font-family="Inter, DejaVu Sans, sans-serif" font-size="26" font-weight="700">Personal Cloud Crates Manager</text>
      <text x="30" y="90" fill="#CBD5E1" font-family="Inter, DejaVu Sans, sans-serif" font-size="21">Single-player timestamp bookmarking utility while digging.</text>
      <text x="30" y="125" fill="#CBD5E1" font-family="Inter, DejaVu Sans, sans-serif" font-size="21">Stores sub-track cue points without consuming local drive storage.</text>
      <rect x="30" y="160" width="680" height="65" rx="10" fill="#1E293B"/>
      <text x="50" y="200" fill="#10B981" font-family="Inter, DejaVu Sans, sans-serif" font-size="18" font-weight="700">✓ Preserves "why" a sample was saved for future studio recall</text>
    </g>
  </g>

  <!-- Block 2: Audio Streaming Engine (YouTube IFrame API) -->
  <g transform="translate(1060, 340)">
    <rect width="840" height="1500" rx="24" fill="url(#boxGrad1)" stroke="#EF4444" stroke-width="3"/>
    <rect x="0" y="0" width="840" height="16" rx="8" fill="#EF4444"/>
    
    <rect x="50" y="50" width="360" height="44" rx="10" fill="#7F1D1D"/>
    <text x="230" y="79" fill="#FCA5A5" font-family="Inter, DejaVu Sans, sans-serif" font-size="20" font-weight="700" text-anchor="middle">OFFICIAL EXTERNAL STREAMING</text>
    
    <text x="50" y="150" fill="#F8FAFC" font-family="Inter, DejaVu Sans, sans-serif" font-size="36" font-weight="800">YouTube IFrame Engine</text>
    <text x="50" y="190" fill="#94A3B8" font-family="Inter, DejaVu Sans, sans-serif" font-size="22">Sandboxed Cross-Origin Client Playback</text>

    <g transform="translate(50, 240)">
      <rect width="740" height="340" rx="18" fill="#0F172A" stroke="#334155" stroke-width="2"/>
      <text x="30" y="50" fill="#EF4444" font-family="Inter, DejaVu Sans, sans-serif" font-size="26" font-weight="700">Strict ToS Section III.E Compliance</text>
      <text x="30" y="95" fill="#CBD5E1" font-family="Inter, DejaVu Sans, sans-serif" font-size="21">❌ ZERO audio scraping or stream downloading</text>
      <text x="30" y="135" fill="#CBD5E1" font-family="Inter, DejaVu Sans, sans-serif" font-size="21">❌ ZERO server-side media caching or raw PCM storage</text>
      <text x="30" y="175" fill="#CBD5E1" font-family="Inter, DejaVu Sans, sans-serif" font-size="21">❌ ZERO bypassing of graphical embedded player UI</text>
      <rect x="30" y="215" width="680" height="90" rx="10" fill="#450A0A"/>
      <text x="50" y="255" fill="#FCA5A5" font-family="Inter, DejaVu Sans, sans-serif" font-size="19" font-weight="700">LEGAL COMPLIANCE GUARANTEE:</text>
      <text x="50" y="285" fill="#FECACA" font-family="Inter, DejaVu Sans, sans-serif" font-size="18">Eliminates copyright infringement risks and bandwidth costs.</text>
    </g>

    <g transform="translate(50, 610)">
      <rect width="740" height="370" rx="18" fill="#0F172A" stroke="#334155" stroke-width="2"/>
      <text x="30" y="50" fill="#EF4444" font-family="Inter, DejaVu Sans, sans-serif" font-size="26" font-weight="700">Client-Side seekTo() Integration</text>
      <text x="30" y="95" fill="#CBD5E1" font-family="Inter, DejaVu Sans, sans-serif" font-size="21">Dispatched via official PostMessage / IFrame events:</text>
      <rect x="30" y="120" width="680" height="70" rx="10" fill="#1E293B"/>
      <text x="50" y="162" fill="#38BDF8" font-family="Inter, DejaVu Sans, sans-serif" font-size="22" font-weight="700">player.seekTo(start_time, true)</text>
      
      <text x="30" y="230" fill="#F8FAFC" font-family="Inter, DejaVu Sans, sans-serif" font-size="22" font-weight="700">Keyframe Drift Physical Constraints:</text>
      <text x="30" y="265" fill="#94A3B8" font-family="Inter, DejaVu Sans, sans-serif" font-size="20">Video GOP keyframe spacing induces 1.0–2.0s seek latency.</text>
      <text x="30" y="295" fill="#94A3B8" font-family="Inter, DejaVu Sans, sans-serif" font-size="20">Formally specified in Acceptance Criteria 2 &amp; NFR-02.</text>
      <rect x="30" y="315" width="680" height="35" rx="6" fill="#1E293B"/>
      <text x="45" y="338" fill="#10B981" font-family="Inter, DejaVu Sans, sans-serif" font-size="16" font-weight="600">✓ Evaluated via Wizard-of-Oz testing in Midterm 2 roadmap</text>
    </g>

    <g transform="translate(50, 1010)">
      <rect width="740" height="360" rx="18" fill="#0F172A" stroke="#334155" stroke-width="2"/>
      <text x="30" y="50" fill="#EF4444" font-family="Inter, DejaVu Sans, sans-serif" font-size="26" font-weight="700">Zero Bandwidth &amp; Hosting Footprint</text>
      <text x="30" y="95" fill="#CBD5E1" font-family="Inter, DejaVu Sans, sans-serif" font-size="21">Audio and video bits stream directly from Google CDN to user browser.</text>
      <text x="30" y="130" fill="#CBD5E1" font-family="Inter, DejaVu Sans, sans-serif" font-size="21">Platform operates with zero media egress / ingress server bills.</text>
      
      <rect x="30" y="170" width="680" height="150" rx="12" fill="#18181B" stroke="#27272A" stroke-width="2"/>
      <text x="50" y="210" fill="#E2E8F0" font-family="Inter, DejaVu Sans, sans-serif" font-size="20" font-weight="700">STREAMING SECURITY BOUNDARY:</text>
      <text x="50" y="245" fill="#94A3B8" font-family="Inter, DejaVu Sans, sans-serif" font-size="18">Sandboxed cross-origin iframe isolates authentication tokens</text>
      <text x="50" y="275" fill="#94A3B8" font-family="Inter, DejaVu Sans, sans-serif" font-size="18">and prevents unauthorized client-side audio rip injection.</text>
    </g>
  </g>

  <!-- Block 3: Backend API & PostgreSQL Store -->
  <g transform="translate(1970, 340)">
    <rect width="840" height="1500" rx="24" fill="url(#boxGrad1)" stroke="#10B981" stroke-width="3"/>
    <rect x="0" y="0" width="840" height="16" rx="8" fill="#10B981"/>
    
    <rect x="50" y="50" width="340" height="44" rx="10" fill="#064E3B"/>
    <text x="220" y="79" fill="#6EE7B7" font-family="Inter, DejaVu Sans, sans-serif" font-size="20" font-weight="700" text-anchor="middle">BACKEND SERVICES &amp; DATA</text>
    
    <text x="50" y="150" fill="#F8FAFC" font-family="Inter, DejaVu Sans, sans-serif" font-size="36" font-weight="800">Backend API &amp; Database</text>
    <text x="50" y="190" fill="#94A3B8" font-family="Inter, DejaVu Sans, sans-serif" font-size="22">FastAPI + Asyncpg + PostgreSQL 16</text>

    <g transform="translate(50, 240)">
      <rect width="740" height="340" rx="18" fill="#0F172A" stroke="#334155" stroke-width="2"/>
      <text x="30" y="50" fill="#10B981" font-family="Inter, DejaVu Sans, sans-serif" font-size="26" font-weight="700">Lightweight Pointer Schema</text>
      <text x="30" y="90" fill="#CBD5E1" font-family="Inter, DejaVu Sans, sans-serif" font-size="20">Zero audio payloads. Stored records consist strictly of pointers:</text>
      <rect x="30" y="115" width="680" height="180" rx="10" fill="#022C22" stroke="#065F46" stroke-width="2"/>
      <text x="50" y="155" fill="#A7F3D0" font-family="Inter, DejaVu Sans, sans-serif" font-size="18" font-weight="600">• video_id: VARCHAR(32) (YouTube video reference)</text>
      <text x="50" y="190" fill="#A7F3D0" font-family="Inter, DejaVu Sans, sans-serif" font-size="18" font-weight="600">• start_time / end_time: NUMERIC(6,2) (4s – 60s)</text>
      <text x="50" y="225" fill="#A7F3D0" font-family="Inter, DejaVu Sans, sans-serif" font-size="18" font-weight="600">• preset_tags: TEXT[] (Tier 1 Objective Presets)</text>
      <text x="50" y="260" fill="#A7F3D0" font-family="Inter, DejaVu Sans, sans-serif" font-size="18" font-weight="600">• context_tags: TEXT[] (Tier 2 Descriptors)</text>
    </g>

    <g transform="translate(50, 610)">
      <rect width="740" height="370" rx="18" fill="#0F172A" stroke="#334155" stroke-width="2"/>
      <text x="30" y="50" fill="#10B981" font-family="Inter, DejaVu Sans, sans-serif" font-size="26" font-weight="700">Tier 1 &amp; Tier 2 Taxonomy Store</text>
      <text x="30" y="90" fill="#CBD5E1" font-family="Inter, DejaVu Sans, sans-serif" font-size="21">Controlled enum validation prevents tag pollution:</text>
      <text x="30" y="125" fill="#94A3B8" font-family="Inter, DejaVu Sans, sans-serif" font-size="19">• Isolation: [No Vocals], [No Drums], [Solo Instrument]</text>
      <text x="30" y="155" fill="#94A3B8" font-family="Inter, DejaVu Sans, sans-serif" font-size="19">• Instruments: [Rhodes], [Piano], [Guitar], [Bass], [Brass]</text>
      <text x="30" y="185" fill="#94A3B8" font-family="Inter, DejaVu Sans, sans-serif" font-size="19">• Sections: [Intro], [Break], [Solo], [Outro], [Chord Loop]</text>
      
      <rect x="30" y="215" width="680" height="120" rx="10" fill="#1E293B"/>
      <text x="50" y="255" fill="#F59E0B" font-family="Inter, DejaVu Sans, sans-serif" font-size="19" font-weight="700">COMMUNITY MODERATION QUEUE:</text>
      <text x="50" y="285" fill="#CBD5E1" font-family="Inter, DejaVu Sans, sans-serif" font-size="18">Community tag appeals and erroneous timestamp flags</text>
      <text x="50" y="315" fill="#CBD5E1" font-family="Inter, DejaVu Sans, sans-serif" font-size="18">are audited via admin dashboard (NFR-03: latency &lt; 200ms).</text>
    </g>

    <g transform="translate(50, 1010)">
      <rect width="740" height="360" rx="18" fill="#0F172A" stroke="#334155" stroke-width="2"/>
      <text x="30" y="50" fill="#10B981" font-family="Inter, DejaVu Sans, sans-serif" font-size="26" font-weight="700">Single-Player &amp; Contingency Pivot</text>
      <text x="30" y="95" fill="#CBD5E1" font-family="Inter, DejaVu Sans, sans-serif" font-size="21">Private crate table isolation per user:</text>
      <text x="30" y="130" fill="#CBD5E1" font-family="Inter, DejaVu Sans, sans-serif" font-size="21">Producers maintain private smart crates without publishing.</text>
      
      <rect x="30" y="170" width="680" height="150" rx="12" fill="#064E3B" stroke="#059669" stroke-width="2"/>
      <text x="50" y="210" fill="#A7F3D0" font-family="Inter, DejaVu Sans, sans-serif" font-size="20" font-weight="700">CONTINGENCY PIVOT READINESS:</text>
      <text x="50" y="245" fill="#E2E8F0" font-family="Inter, DejaVu Sans, sans-serif" font-size="18">If H3 fails (gatekeeping), platform smoothly transitions</text>
      <text x="50" y="275" fill="#E2E8F0" font-family="Inter, DejaVu Sans, sans-serif" font-size="18">to 100% Personal Crate-Digging Workspace with zero code rewrite.</text>
    </g>
  </g>

  <!-- Block 4: Passage Match & Ranking Engine -->
  <g transform="translate(2880, 340)">
    <rect width="870" height="1500" rx="24" fill="url(#boxGrad1)" stroke="#F59E0B" stroke-width="3"/>
    <rect x="0" y="0" width="870" height="16" rx="8" fill="#F59E0B"/>
    
    <rect x="50" y="50" width="370" height="44" rx="10" fill="#78350F"/>
    <text x="235" y="79" fill="#FDE68A" font-family="Inter, DejaVu Sans, sans-serif" font-size="20" font-weight="700" text-anchor="middle">DISCOVERY &amp; COLD-START ENGINE</text>
    
    <text x="50" y="150" fill="#F8FAFC" font-family="Inter, DejaVu Sans, sans-serif" font-size="36" font-weight="800">Passage Ranking Engine</text>
    <text x="50" y="190" fill="#94A3B8" font-family="Inter, DejaVu Sans, sans-serif" font-size="22">Preset Intersection &amp; Berrypicking Feeds</text>

    <!-- Component Modules -->
    <g transform="translate(50, 240)">
      <rect width="770" height="340" rx="18" fill="#0F172A" stroke="#334155" stroke-width="2"/>
      <text x="30" y="50" fill="#F59E0B" font-family="Inter, DejaVu Sans, sans-serif" font-size="26" font-weight="700">Tier-1 Preset Overlap Matching</text>
      <text x="30" y="90" fill="#CBD5E1" font-family="Inter, DejaVu Sans, sans-serif" font-size="21">Replaces opaque black-box AI scores with explainable overlap:</text>
      <rect x="30" y="115" width="710" height="180" rx="10" fill="#1E293B"/>
      <text x="50" y="155" fill="#38BDF8" font-family="Inter, DejaVu Sans, sans-serif" font-size="20" font-weight="700">• Overlap Score = |Q_presets ∩ P_presets| / |Q_presets|</text>
      <text x="50" y="190" fill="#10B981" font-family="Inter, DejaVu Sans, sans-serif" font-size="19" font-weight="600">✓ 4/4 Match: Exact isolation + instrument + section match</text>
      <text x="50" y="225" fill="#FCD34D" font-family="Inter, DejaVu Sans, sans-serif" font-size="19" font-weight="600">✓ 3/4 Match: Instrument + isolation match across catalog</text>
      <text x="50" y="260" fill="#94A3B8" font-family="Inter, DejaVu Sans, sans-serif" font-size="17">Zero fake similarity percentages (no '98% AI Match' claims)</text>
    </g>

    <g transform="translate(50, 610)">
      <rect width="770" height="370" rx="18" fill="#0F172A" stroke="#334155" stroke-width="2"/>
      <text x="30" y="50" fill="#F59E0B" font-family="Inter, DejaVu Sans, sans-serif" font-size="26" font-weight="700">Seed-Passage Berrypicking</text>
      <text x="30" y="95" fill="#CBD5E1" font-family="Inter, DejaVu Sans, sans-serif" font-size="21">Operationalizes Bates' information berrypicking model:</text>
      <text x="30" y="130" fill="#94A3B8" font-family="Inter, DejaVu Sans, sans-serif" font-size="20">Users listen to a sample segment, click its preset chips,</text>
      <text x="30" y="160" fill="#94A3B8" font-family="Inter, DejaVu Sans, sans-serif" font-size="20">and immediately receive an associative recommendation feed</text>
      <text x="30" y="190" fill="#94A3B8" font-family="Inter, DejaVu Sans, sans-serif" font-size="20">of matching sub-track cue points in unfamiliar recordings.</text>
      
      <rect x="30" y="225" width="710" height="110" rx="10" fill="#18181B" stroke="#27272A" stroke-width="2"/>
      <text x="50" y="265" fill="#A7F3D0" font-family="Inter, DejaVu Sans, sans-serif" font-size="19" font-weight="700">FLOW STATE PRESERVATION:</text>
      <text x="50" y="295" fill="#E2E8F0" font-family="Inter, DejaVu Sans, sans-serif" font-size="18">No typing text queries from scratch; discovery follows active ears.</text>
    </g>

    <g transform="translate(50, 1010)">
      <rect width="770" height="360" rx="18" fill="#0F172A" stroke="#334155" stroke-width="2"/>
      <text x="30" y="50" fill="#F59E0B" font-family="Inter, DejaVu Sans, sans-serif" font-size="26" font-weight="700">Cold-Start Text Seeding Pipeline</text>
      <text x="30" y="95" fill="#CBD5E1" font-family="Inter, DejaVu Sans, sans-serif" font-size="21">Solves the cold-start catalog challenge with ZERO audio processing:</text>
      <rect x="30" y="125" width="710" height="190" rx="10" fill="#451A03" stroke="#B45309" stroke-width="2"/>
      <text x="50" y="165" fill="#FDE68A" font-family="Inter, DejaVu Sans, sans-serif" font-size="19" font-weight="700">1. YouTube Data API v3 Chapter Ingestion:</text>
      <text x="50" y="195" fill="#FEF3C7" font-family="Inter, DejaVu Sans, sans-serif" font-size="17">Extracts timestamps from video descriptions &amp; chapter markers</text>
      <text x="50" y="235" fill="#FDE68A" font-family="Inter, DejaVu Sans, sans-serif" font-size="19" font-weight="700">2. Discogs API Instrument Mapping:</text>
      <text x="50" y="265" fill="#FEF3C7" font-family="Inter, DejaVu Sans, sans-serif" font-size="17">Maps track musician credits (e.g., Rhodes, Saxophone, Bass) to presets</text>
      <text x="50" y="295" fill="#10B981" font-family="Inter, DejaVu Sans, sans-serif" font-size="16" font-weight="600">✓ Populates initial catalog landmarks prior to community scaling</text>
    </g>
  </g>

  <!-- Communication Connectors & Telemetry Banner -->
  <g transform="translate(150, 1900)">
    <rect width="3600" height="340" rx="24" fill="#0F172A" stroke="#334155" stroke-width="3"/>
    
    <g transform="translate(50, 40)">
      <rect width="450" height="40" rx="8" fill="#1E293B"/>
      <text x="225" y="27" fill="#38BDF8" font-family="Inter, DejaVu Sans, sans-serif" font-size="18" font-weight="700" text-anchor="middle">CROSS-BOUNDARY DATA PROTOCOLS</text>
      
      <text x="0" y="95" fill="#F8FAFC" font-family="Inter, DejaVu Sans, sans-serif" font-size="32" font-weight="800">Strict Compliance, Latency &amp; Cost Guarantees</text>
      <text x="0" y="135" fill="#94A3B8" font-family="Inter, DejaVu Sans, sans-serif" font-size="22">System engineering boundaries mapped to Course Guideline Non-Functional Requirements (NFR-01 to NFR-03).</text>
    </g>

    <!-- Metrics Grid -->
    <g transform="translate(50, 190)">
      <rect x="0" y="0" width="840" height="100" rx="14" fill="#1E293B" stroke="#334155" stroke-width="2"/>
      <text x="30" y="42" fill="#10B981" font-family="Inter, DejaVu Sans, sans-serif" font-size="22" font-weight="800">NFR-01: API Compliance</text>
      <text x="30" y="75" fill="#E2E8F0" font-family="Inter, DejaVu Sans, sans-serif" font-size="19">100% Embedded Playback • 0% Audio Scraped</text>

      <rect x="880" y="0" width="840" height="100" rx="14" fill="#1E293B" stroke="#334155" stroke-width="2"/>
      <text x="910" y="42" fill="#38BDF8" font-family="Inter, DejaVu Sans, sans-serif" font-size="22" font-weight="800">NFR-02: Playhead Latency</text>
      <text x="910" y="75" fill="#E2E8F0" font-family="Inter, DejaVu Sans, sans-serif" font-size="19">seekTo Positioning ≤ 1.5s (Keyframe Bounded)</text>

      <rect x="1760" y="0" width="840" height="100" rx="14" fill="#1E293B" stroke="#334155" stroke-width="2"/>
      <text x="1790" y="42" fill="#F59E0B" font-family="Inter, DejaVu Sans, sans-serif" font-size="22" font-weight="800">NFR-03: Metadata Latency</text>
      <text x="1790" y="75" fill="#E2E8F0" font-family="Inter, DejaVu Sans, sans-serif" font-size="19">FastAPI Query Latency &lt; 200ms (p95)</text>

      <rect x="2640" y="0" width="870" height="100" rx="14" fill="#1E293B" stroke="#334155" stroke-width="2"/>
      <text x="2670" y="42" fill="#34D399" font-family="Inter, DejaVu Sans, sans-serif" font-size="22" font-weight="800">Operational Overhead</text>
      <text x="2670" y="75" fill="#E2E8F0" font-family="Inter, DejaVu Sans, sans-serif" font-size="19">Zero Media Storage &amp; Bandwidth Egress Costs</text>
    </g>
  </g>
</svg>'''
    render_svg_to_png(svg, f"{OUT_DIR}/architecture_overview.png", w, h)
    render_svg_to_png(svg, f"{OUT_DIR}/concept.png", w, h)

# =========================================================================
# 3. before_after_workflow.png (3900 x 1860)
# =========================================================================
def generate_before_after():
    w, h = 3900, 1860
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">
  <defs>
    <linearGradient id="bgGrad3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0F172A"/>
      <stop offset="100%" stop-color="#1E293B"/>
    </linearGradient>
    <linearGradient id="boxGrad3" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#1E293B"/>
      <stop offset="100%" stop-color="#0F172A"/>
    </linearGradient>
  </defs>

  <rect width="{w}" height="{h}" fill="url(#bgGrad3)"/>
  
  <g opacity="0.05" stroke="#94A3B8" stroke-width="2">
    {''.join(f'<line x1="{x}" y1="0" x2="{x}" y2="{h}"/>' for x in range(0, w, 150))}
    {''.join(f'<line x1="0" y1="{y}" x2="{w}" y2="{y}"/>' for y in range(0, h, 150))}
  </g>

  <!-- Header -->
  <g transform="translate(150, 75)">
    <text x="0" y="55" fill="#F8FAFC" font-family="Inter, DejaVu Sans, sans-serif" font-size="52" font-weight="800">Workflow Comparison: Traditional Manual Scrubbing vs. Sample Browser Granular Discovery</text>
    <text x="0" y="105" fill="#94A3B8" font-family="Inter, DejaVu Sans, sans-serif" font-size="26">Eliminating Manual Scrubbing Fatigue and Context Loss Through Direct Sub-Track Cue-Point Auditioning</text>
  </g>

  <!-- TOP WORKFLOW: BEFORE (Traditional Manual Scrubbing) -->
  <g transform="translate(150, 230)">
    <rect width="3600" height="720" rx="24" fill="url(#boxGrad3)" stroke="#EF4444" stroke-width="3"/>
    <rect x="0" y="0" width="3600" height="14" rx="7" fill="#EF4444"/>
    
    <g transform="translate(60, 45)">
      <rect width="520" height="44" rx="10" fill="#7F1D1D"/>
      <text x="260" y="30" fill="#FCA5A5" font-family="Inter, DejaVu Sans, sans-serif" font-size="20" font-weight="800" text-anchor="middle" letter-spacing="2">BEFORE • TRADITIONAL WORKFLOW</text>
      
      <text x="560" y="32" fill="#F8FAFC" font-family="Inter, DejaVu Sans, sans-serif" font-size="34" font-weight="800">Manual Playhead Scrubbing Cycle (Status Quo)</text>
      
      <!-- Right Status Badge -->
      <rect x="2540" y="-8" width="940" height="52" rx="12" fill="#27272A" stroke="#EF4444" stroke-width="2"/>
      <text x="3010" y="27" fill="#FCA5A5" font-family="Inter, DejaVu Sans, sans-serif" font-size="20" font-weight="700" text-anchor="middle">STATUS QUO: High Scrubbing Fatigue • 15–25 min / Candidate</text>
    </g>

    <!-- 5 Steps Horizontal -->
    <g transform="translate(60, 130)">
      <!-- Step 1 -->
      <g transform="translate(0, 0)">
        <rect width="640" height="460" rx="18" fill="#0F172A" stroke="#334155" stroke-width="2"/>
        <rect x="30" y="30" width="120" height="36" rx="8" fill="#1E293B"/>
        <text x="90" y="55" fill="#EF4444" font-family="Inter, DejaVu Sans, sans-serif" font-size="18" font-weight="800" text-anchor="middle">STEP 01</text>
        <text x="30" y="115" fill="#F8FAFC" font-family="Inter, DejaVu Sans, sans-serif" font-size="28" font-weight="700">Find Whole Song</text>
        <text x="30" y="165" fill="#94A3B8" font-family="Inter, DejaVu Sans, sans-serif" font-size="21">Discovers full 3-to-6 min song on YouTube or Samplette.</text>
        <rect x="30" y="240" width="580" height="170" rx="12" fill="#18181B"/>
        <text x="50" y="285" fill="#E2E8F0" font-family="Inter, DejaVu Sans, sans-serif" font-size="19" font-weight="600">Initial Impression:</text>
        <text x="50" y="320" fill="#94A3B8" font-family="Inter, DejaVu Sans, sans-serif" font-size="18">Great artist name or album cover, but zero</text>
        <text x="50" y="350" fill="#94A3B8" font-family="Inter, DejaVu Sans, sans-serif" font-size="18">visibility into where sample moments hide.</text>
      </g>

      <!-- Arrow 1 -->
      <text x="675" y="240" fill="#EF4444" font-family="Inter, DejaVu Sans, sans-serif" font-size="44" font-weight="800">→</text>

      <!-- Step 2 -->
      <g transform="translate(710, 0)">
        <rect width="640" height="460" rx="18" fill="#0F172A" stroke="#334155" stroke-width="2"/>
        <rect x="30" y="30" width="120" height="36" rx="8" fill="#1E293B"/>
        <text x="90" y="55" fill="#EF4444" font-family="Inter, DejaVu Sans, sans-serif" font-size="18" font-weight="800" text-anchor="middle">STEP 02</text>
        <text x="30" y="115" fill="#F8FAFC" font-family="Inter, DejaVu Sans, sans-serif" font-size="28" font-weight="700">Manual Scrubbing</text>
        <text x="30" y="165" fill="#94A3B8" font-family="Inter, DejaVu Sans, sans-serif" font-size="21">Repeatedly drags playhead across flat video timeline.</text>
        <rect x="30" y="240" width="580" height="170" rx="12" fill="#450A0A"/>
        <text x="50" y="285" fill="#FCA5A5" font-family="Inter, DejaVu Sans, sans-serif" font-size="19" font-weight="600">The Scrubbing Sieve:</text>
        <text x="50" y="320" fill="#FECACA" font-family="Inter, DejaVu Sans, sans-serif" font-size="18">Clicks randomly at 0:45, 1:30, 2:40, 3:15</text>
        <text x="50" y="350" fill="#FECACA" font-family="Inter, DejaVu Sans, sans-serif" font-size="18">seeking clean instrument breaks.</text>
      </g>

      <!-- Arrow 2 -->
      <text x="1385" y="240" fill="#EF4444" font-family="Inter, DejaVu Sans, sans-serif" font-size="44" font-weight="800">→</text>

      <!-- Step 3 -->
      <g transform="translate(1420, 0)">
        <rect width="640" height="460" rx="18" fill="#0F172A" stroke="#334155" stroke-width="2"/>
        <rect x="30" y="30" width="120" height="36" rx="8" fill="#1E293B"/>
        <text x="90" y="55" fill="#EF4444" font-family="Inter, DejaVu Sans, sans-serif" font-size="18" font-weight="800" text-anchor="middle">STEP 03</text>
        <text x="30" y="115" fill="#F8FAFC" font-family="Inter, DejaVu Sans, sans-serif" font-size="28" font-weight="700">Section Collisions</text>
        <text x="30" y="165" fill="#94A3B8" font-family="Inter, DejaVu Sans, sans-serif" font-size="21">Encounters vocal bleeds, overlapping drums, or tempo shifts.</text>
        <rect x="30" y="240" width="580" height="170" rx="12" fill="#18181B"/>
        <text x="50" y="285" fill="#E2E8F0" font-family="Inter, DejaVu Sans, sans-serif" font-size="19" font-weight="600">Friction &amp; Abandonment:</text>
        <text x="50" y="320" fill="#94A3B8" font-family="Inter, DejaVu Sans, sans-serif" font-size="18">Beautiful chords ruined by drums.</text>
        <text x="50" y="350" fill="#94A3B8" font-family="Inter, DejaVu Sans, sans-serif" font-size="18">Track abandoned after 4–5 minutes of effort.</text>
      </g>

      <!-- Arrow 3 -->
      <text x="2095" y="240" fill="#EF4444" font-family="Inter, DejaVu Sans, sans-serif" font-size="44" font-weight="800">→</text>

      <!-- Step 4 -->
      <g transform="translate(2130, 0)">
        <rect width="640" height="460" rx="18" fill="#0F172A" stroke="#334155" stroke-width="2"/>
        <rect x="30" y="30" width="120" height="36" rx="8" fill="#1E293B"/>
        <text x="90" y="55" fill="#EF4444" font-family="Inter, DejaVu Sans, sans-serif" font-size="18" font-weight="800" text-anchor="middle">STEP 04</text>
        <text x="30" y="115" fill="#F8FAFC" font-family="Inter, DejaVu Sans, sans-serif" font-size="28" font-weight="700">Ad-Hoc Bookmarks</text>
        <text x="30" y="165" fill="#94A3B8" font-family="Inter, DejaVu Sans, sans-serif" font-size="21">Pastes full YouTube link into browser bookmarks or notepad.</text>
        <rect x="30" y="240" width="580" height="170" rx="12" fill="#18181B"/>
        <text x="50" y="285" fill="#E2E8F0" font-family="Inter, DejaVu Sans, sans-serif" font-size="19" font-weight="600">Storage Fragmentation:</text>
        <text x="50" y="320" fill="#94A3B8" font-family="Inter, DejaVu Sans, sans-serif" font-size="18">Saves whole link without cue point</text>
        <text x="50" y="350" fill="#94A3B8" font-family="Inter, DejaVu Sans, sans-serif" font-size="18">or instrument tags. Local disk clutter.</text>
      </g>

      <!-- Arrow 4 -->
      <text x="2805" y="240" fill="#EF4444" font-family="Inter, DejaVu Sans, sans-serif" font-size="44" font-weight="800">→</text>

      <!-- Step 5 -->
      <g transform="translate(2840, 0)">
        <rect width="640" height="460" rx="18" fill="#0F172A" stroke="#334155" stroke-width="2"/>
        <rect x="30" y="30" width="120" height="36" rx="8" fill="#1E293B"/>
        <text x="90" y="55" fill="#EF4444" font-family="Inter, DejaVu Sans, sans-serif" font-size="18" font-weight="800" text-anchor="middle">STEP 05</text>
        <text x="30" y="115" fill="#F8FAFC" font-family="Inter, DejaVu Sans, sans-serif" font-size="28" font-weight="700">Timestamp Amnesia</text>
        <text x="30" y="165" fill="#94A3B8" font-family="Inter, DejaVu Sans, sans-serif" font-size="21">Returns weeks later to produce; forgets which moment inspired.</text>
        <rect x="30" y="240" width="580" height="170" rx="12" fill="#450A0A"/>
        <text x="50" y="285" fill="#FCA5A5" font-family="Inter, DejaVu Sans, sans-serif" font-size="19" font-weight="600">Search Cycle Restarts:</text>
        <text x="50" y="320" fill="#FECACA" font-family="Inter, DejaVu Sans, sans-serif" font-size="18">Must re-scrub whole 5-minute song</text>
        <text x="50" y="350" fill="#FECACA" font-family="Inter, DejaVu Sans, sans-serif" font-size="18">all over again from scratch.</text>
      </g>
    </g>
  </g>

  <!-- BOTTOM WORKFLOW: AFTER (Sample Browser Granular Discovery) -->
  <g transform="translate(150, 1010)">
    <rect width="3600" height="720" rx="24" fill="url(#boxGrad3)" stroke="#10B981" stroke-width="3"/>
    <rect x="0" y="0" width="3600" height="14" rx="7" fill="#10B981"/>
    
    <g transform="translate(60, 45)">
      <rect width="520" height="44" rx="10" fill="#064E3B"/>
      <text x="260" y="30" fill="#6EE7B7" font-family="Inter, DejaVu Sans, sans-serif" font-size="20" font-weight="800" text-anchor="middle" letter-spacing="2">AFTER • SAMPLE BROWSER WORKFLOW</text>
      
      <text x="560" y="32" fill="#F8FAFC" font-family="Inter, DejaVu Sans, sans-serif" font-size="34" font-weight="800">Target Workflow: Direct Cue-Point Auditioning</text>
      
      <!-- Right Status Badge (NO unverified 15 seconds claim) -->
      <rect x="2540" y="-8" width="940" height="52" rx="12" fill="#064E3B" stroke="#10B981" stroke-width="2"/>
      <text x="3010" y="27" fill="#A7F3D0" font-family="Inter, DejaVu Sans, sans-serif" font-size="20" font-weight="700" text-anchor="middle">TARGET: Direct Cue-Point Auditioning • Zero Scrubbing</text>
    </g>

    <!-- 5 Steps Horizontal -->
    <g transform="translate(60, 130)">
      <!-- Step 1 -->
      <g transform="translate(0, 0)">
        <rect width="640" height="460" rx="18" fill="#0F172A" stroke="#334155" stroke-width="2"/>
        <rect x="30" y="30" width="120" height="36" rx="8" fill="#1E293B"/>
        <text x="90" y="55" fill="#10B981" font-family="Inter, DejaVu Sans, sans-serif" font-size="18" font-weight="800" text-anchor="middle">STEP 01</text>
        <text x="30" y="115" fill="#F8FAFC" font-family="Inter, DejaVu Sans, sans-serif" font-size="28" font-weight="700">Load Track &amp; Timeline</text>
        <text x="30" y="165" fill="#94A3B8" font-family="Inter, DejaVu Sans, sans-serif" font-size="21">Interactive timeline displays pre-marked 4–60s structural segments.</text>
        <rect x="30" y="240" width="580" height="170" rx="12" fill="#022C22"/>
        <text x="50" y="285" fill="#6EE7B7" font-family="Inter, DejaVu Sans, sans-serif" font-size="19" font-weight="600">Immediate Visual Orientation:</text>
        <text x="50" y="320" fill="#A7F3D0" font-family="Inter, DejaVu Sans, sans-serif" font-size="18">Pre-marked cue points highlight clean breaks</text>
        <text x="50" y="350" fill="#A7F3D0" font-family="Inter, DejaVu Sans, sans-serif" font-size="18">and unlayered intro chords on load.</text>
      </g>

      <!-- Arrow 1 -->
      <text x="675" y="240" fill="#10B981" font-family="Inter, DejaVu Sans, sans-serif" font-size="44" font-weight="800">→</text>

      <!-- Step 2 -->
      <g transform="translate(710, 0)">
        <rect width="640" height="460" rx="18" fill="#0F172A" stroke="#334155" stroke-width="2"/>
        <rect x="30" y="30" width="120" height="36" rx="8" fill="#1E293B"/>
        <text x="90" y="55" fill="#10B981" font-family="Inter, DejaVu Sans, sans-serif" font-size="18" font-weight="800" text-anchor="middle">STEP 02</text>
        <text x="30" y="115" fill="#F8FAFC" font-family="Inter, DejaVu Sans, sans-serif" font-size="28" font-weight="700">Inspect Preset Tags</text>
        <text x="30" y="165" fill="#94A3B8" font-family="Inter, DejaVu Sans, sans-serif" font-size="21">Clicks segment: [Rhodes] [No Drums] [Intro] in 1 click.</text>
        <rect x="30" y="240" width="580" height="170" rx="12" fill="#022C22"/>
        <text x="50" y="285" fill="#6EE7B7" font-family="Inter, DejaVu Sans, sans-serif" font-size="19" font-weight="600">Objective Verification:</text>
        <text x="50" y="320" fill="#A7F3D0" font-family="Inter, DejaVu Sans, sans-serif" font-size="18">Verifiable musical facts without vague words;</text>
        <text x="50" y="350" fill="#A7F3D0" font-family="Inter, DejaVu Sans, sans-serif" font-size="18">instant cue-point seeking to exact start_time.</text>
      </g>

      <!-- Arrow 2 -->
      <text x="1385" y="240" fill="#10B981" font-family="Inter, DejaVu Sans, sans-serif" font-size="44" font-weight="800">→</text>

      <!-- Step 3 -->
      <g transform="translate(1420, 0)">
        <rect width="640" height="460" rx="18" fill="#0F172A" stroke="#334155" stroke-width="2"/>
        <rect x="30" y="30" width="120" height="36" rx="8" fill="#1E293B"/>
        <text x="90" y="55" fill="#10B981" font-family="Inter, DejaVu Sans, sans-serif" font-size="18" font-weight="800" text-anchor="middle">STEP 03</text>
        <text x="30" y="115" fill="#F8FAFC" font-family="Inter, DejaVu Sans, sans-serif" font-size="28" font-weight="700">Berrypicking Filter</text>
        <text x="30" y="165" fill="#94A3B8" font-family="Inter, DejaVu Sans, sans-serif" font-size="21">Selects Tier-1 objective preset chips + optional context tags.</text>
        <rect x="30" y="240" width="580" height="170" rx="12" fill="#022C22"/>
        <text x="50" y="285" fill="#6EE7B7" font-family="Inter, DejaVu Sans, sans-serif" font-size="19" font-weight="600">Associative Discovery:</text>
        <text x="50" y="320" fill="#A7F3D0" font-family="Inter, DejaVu Sans, sans-serif" font-size="18">Branches from what the ears are hearing directly</text>
        <text x="50" y="350" fill="#A7F3D0" font-family="Inter, DejaVu Sans, sans-serif" font-size="18">to matching sections in catalog tracks.</text>
      </g>

      <!-- Arrow 3 -->
      <text x="2095" y="240" fill="#10B981" font-family="Inter, DejaVu Sans, sans-serif" font-size="44" font-weight="800">→</text>

      <!-- Step 4 -->
      <g transform="translate(2130, 0)">
        <rect width="640" height="460" rx="18" fill="#0F172A" stroke="#334155" stroke-width="2"/>
        <rect x="30" y="30" width="120" height="36" rx="8" fill="#1E293B"/>
        <text x="90" y="55" fill="#10B981" font-family="Inter, DejaVu Sans, sans-serif" font-size="18" font-weight="800" text-anchor="middle">STEP 04</text>
        <text x="30" y="115" fill="#F8FAFC" font-family="Inter, DejaVu Sans, sans-serif" font-size="28" font-weight="700">Cross-Match Feed</text>
        <text x="30" y="165" fill="#94A3B8" font-family="Inter, DejaVu Sans, sans-serif" font-size="21">Engine returns ranked segments sharing matching preset tags.</text>
        <rect x="30" y="240" width="580" height="170" rx="12" fill="#022C22"/>
        <text x="50" y="285" fill="#6EE7B7" font-family="Inter, DejaVu Sans, sans-serif" font-size="19" font-weight="600">Explainable Overlap:</text>
        <text x="50" y="320" fill="#A7F3D0" font-family="Inter, DejaVu Sans, sans-serif" font-size="18">"4/4 Preset Tags Match" cards returned</text>
        <text x="50" y="350" fill="#A7F3D0" font-family="Inter, DejaVu Sans, sans-serif" font-size="18">jumping directly to matching timestamps.</text>
      </g>

      <!-- Arrow 4 -->
      <text x="2805" y="240" fill="#10B981" font-family="Inter, DejaVu Sans, sans-serif" font-size="44" font-weight="800">→</text>

      <!-- Step 5 -->
      <g transform="translate(2840, 0)">
        <rect width="640" height="460" rx="18" fill="#0F172A" stroke="#334155" stroke-width="2"/>
        <rect x="30" y="30" width="120" height="36" rx="8" fill="#1E293B"/>
        <text x="90" y="55" fill="#10B981" font-family="Inter, DejaVu Sans, sans-serif" font-size="18" font-weight="800" text-anchor="middle">STEP 05</text>
        <text x="30" y="115" fill="#F8FAFC" font-family="Inter, DejaVu Sans, sans-serif" font-size="28" font-weight="700">Rough Audition &amp; Save</text>
        <text x="30" y="165" fill="#94A3B8" font-family="Inter, DejaVu Sans, sans-serif" font-size="21">Player seeks to start_time, loops interval, or saves to Cloud Crate.</text>
        <rect x="30" y="240" width="580" height="170" rx="12" fill="#064E3B"/>
        <text x="50" y="285" fill="#6EE7B7" font-family="Inter, DejaVu Sans, sans-serif" font-size="19" font-weight="600">Zero Storage Overhead:</text>
        <text x="50" y="320" fill="#A7F3D0" font-family="Inter, DejaVu Sans, sans-serif" font-size="18">Saves exact timestamp pointers and notes;</text>
        <text x="50" y="350" fill="#A7F3D0" font-family="Inter, DejaVu Sans, sans-serif" font-size="18">ready for immediate studio beat chopping.</text>
      </g>
    </g>
  </g>
</svg>'''
    render_svg_to_png(svg, f"{OUT_DIR}/before_after_workflow.png", w, h)
    render_svg_to_png(svg, f"{OUT_DIR}/after.png", w, h)
    render_svg_to_png(svg, f"{OUT_DIR}/before.png", w, h)

# =========================================================================
# 4. ui_concept_mockup.png (3900 x 2280) - MOST CRITICAL
# =========================================================================
def generate_ui_mockup():
    w, h = 3900, 2280
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">
  <defs>
    <linearGradient id="uiBg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0B0F19"/>
      <stop offset="100%" stop-color="#0F172A"/>
    </linearGradient>
    <linearGradient id="panelBg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#1E293B"/>
      <stop offset="100%" stop-color="#0F172A"/>
    </linearGradient>
    <linearGradient id="vidBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#18181B"/>
      <stop offset="100%" stop-color="#09090B"/>
    </linearGradient>
  </defs>

  <!-- Base UI Background -->
  <rect width="{w}" height="{h}" fill="url(#uiBg)"/>

  <!-- 1. Top Navigation Bar -->
  <g transform="translate(0, 0)">
    <rect width="{w}" height="130" fill="#0F172A" stroke="#1E293B" stroke-width="3"/>
    
    <!-- Logo -->
    <g transform="translate(80, 40)">
      <rect width="50" height="50" rx="12" fill="#10B981"/>
      <path d="M 18 15 L 18 35 L 35 25 Z" fill="#0F172A"/>
      <text x="70" y="38" fill="#F8FAFC" font-family="Inter, DejaVu Sans, sans-serif" font-size="34" font-weight="900" letter-spacing="-1">SAMPLE BROWSER</text>
      <rect x="400" y="8" width="100" height="34" rx="8" fill="#1E293B" stroke="#334155" stroke-width="1.5"/>
      <text x="450" y="31" fill="#10B981" font-family="Inter, DejaVu Sans, sans-serif" font-size="16" font-weight="800" text-anchor="middle">PRO v1.0</text>
    </g>

    <!-- Search Bar -->
    <g transform="translate(800, 32)">
      <rect width="1800" height="66" rx="16" fill="#1E293B" stroke="#334155" stroke-width="2"/>
      <text x="35" y="42" fill="#64748B" font-family="Inter, DejaVu Sans, sans-serif" font-size="24">🔍</text>
      <text x="80" y="42" fill="#E2E8F0" font-family="Inter, DejaVu Sans, sans-serif" font-size="22">Hiroshi Suzuki - Romance (1975)</text>
      <rect x="1560" y="10" width="220" height="46" rx="10" fill="#334155"/>
      <text x="1670" y="40" fill="#94A3B8" font-family="Inter, DejaVu Sans, sans-serif" font-size="18" font-weight="700" text-anchor="middle">PASTE YOUTUBE URL</text>
    </g>

    <!-- User & Crates Actions -->
    <g transform="translate(2850, 32)">
      <rect x="0" y="0" width="340" height="66" rx="16" fill="#1E293B" stroke="#10B981" stroke-width="2"/>
      <text x="35" y="42" fill="#10B981" font-family="Inter, DejaVu Sans, sans-serif" font-size="22">📂</text>
      <text x="75" y="42" fill="#F8FAFC" font-family="Inter, DejaVu Sans, sans-serif" font-size="20" font-weight="700">Personal Crates</text>
      <rect x="250" y="14" width="65" height="38" rx="8" fill="#064E3B"/>
      <text x="282" y="40" fill="#6EE7B7" font-family="Inter, DejaVu Sans, sans-serif" font-size="18" font-weight="800" text-anchor="middle">14</text>

      <!-- Profile -->
      <g transform="translate(390, 0)">
        <rect width="580" height="66" rx="16" fill="#1E293B" stroke="#334155" stroke-width="2"/>
        <circle cx="45" cy="33" r="22" fill="#0369A1"/>
        <text x="45" y="40" fill="#F0F9FF" font-family="Inter, DejaVu Sans, sans-serif" font-size="18" font-weight="800" text-anchor="middle">AM</text>
        <text x="85" y="32" fill="#F8FAFC" font-family="Inter, DejaVu Sans, sans-serif" font-size="20" font-weight="700">Alex "Kaelo" Miller</text>
        <text x="85" y="54" fill="#94A3B8" font-family="Inter, DejaVu Sans, sans-serif" font-size="16">Bedroom Producer (FL Studio)</text>
      </g>
    </g>
  </g>

  <!-- 2. Main Track Player & Segmented Timeline Area -->
  <g transform="translate(80, 165)">
    <!-- Container -->
    <rect width="3740" height="680" rx="24" fill="url(#panelBg)" stroke="#334155" stroke-width="3"/>

    <!-- Left: Embedded YouTube Video Player Box (16:9) -->
    <g transform="translate(50, 45)">
      <rect width="980" height="590" rx="18" fill="url(#vidBg)" stroke="#27272A" stroke-width="2"/>
      
      <!-- Video Content Mockup -->
      <!-- Album Art / Thumbnail Graphic -->
      <g opacity="0.6">
        <circle cx="490" cy="270" r="160" fill="#18181B" stroke="#27272A" stroke-width="12"/>
        <circle cx="490" cy="270" r="60" fill="#F59E0B" opacity="0.8"/>
        <circle cx="490" cy="270" r="15" fill="#000000"/>
      </g>
      
      <!-- Video Header -->
      <rect width="980" height="70" rx="18" fill="#000000" opacity="0.75"/>
      <text x="35" y="44" fill="#FFFFFF" font-family="Inter, DejaVu Sans, sans-serif" font-size="22" font-weight="700">Hiroshi Suzuki — Romance (Cat, 1975) [Full Album Track]</text>
      
      <!-- Center YouTube Play Icon -->
      <g transform="translate(435, 235)">
        <rect width="110" height="76" rx="22" fill="#FF0000" opacity="0.9"/>
        <path d="M 45 22 L 45 54 L 75 38 Z" fill="#FFFFFF"/>
      </g>

      <!-- Video Player Bottom Controls (YouTube IFrame UI compliance) -->
      <rect y="520" width="980" height="70" rx="18" fill="#000000" opacity="0.85"/>
      <text x="35" y="562" fill="#FFFFFF" font-family="Inter, DejaVu Sans, sans-serif" font-size="20">▶</text>
      <text x="75" y="562" fill="#FFFFFF" font-family="Inter, DejaVu Sans, sans-serif" font-size="20">❚❚</text>
      <text x="125" y="562" fill="#CBD5E1" font-family="Inter, DejaVu Sans, sans-serif" font-size="18">0:12 / 5:42</text>
      <rect x="250" y="552" width="560" height="6" rx="3" fill="#334155"/>
      <rect x="250" y="552" width="70" height="6" rx="3" fill="#FF0000"/>
      <circle cx="320" cy="555" r="8" fill="#FF0000"/>
      <text x="840" y="562" fill="#FFFFFF" font-family="Inter, DejaVu Sans, sans-serif" font-size="16" font-weight="700">HD</text>
      <text x="890" y="562" fill="#FF0000" font-family="Inter, DejaVu Sans, sans-serif" font-size="18" font-weight="900">YouTube</text>
    </g>

    <!-- Right: Track Metadata & Interactive Segmented Timeline Bar -->
    <g transform="translate(1080, 50)">
      <!-- Track Header -->
      <g>
        <rect x="0" y="0" width="220" height="38" rx="8" fill="#1E293B" stroke="#334155" stroke-width="1.5"/>
        <text x="110" y="25" fill="#38BDF8" font-family="Inter, DejaVu Sans, sans-serif" font-size="16" font-weight="700" text-anchor="middle">ACTIVE PLAYBACK SESSION</text>
        
        <text x="0" y="85" fill="#F8FAFC" font-family="Inter, DejaVu Sans, sans-serif" font-size="44" font-weight="800">Hiroshi Suzuki — Romance</text>
        <text x="0" y="125" fill="#94A3B8" font-family="Inter, DejaVu Sans, sans-serif" font-size="24">Album: Cat (1975, Columbia / Flying Disk) • Video ID: H169_k4V8aI • 8,420 views</text>
      </g>

      <!-- Segment Markers Heading -->
      <g transform="translate(0, 160)">
        <text x="0" y="25" fill="#CBD5E1" font-family="Inter, DejaVu Sans, sans-serif" font-size="22" font-weight="700">INTERACTIVE SEGMENTED TIMELINE (4–60s Cue Markers)</text>
        <text x="2590" y="25" fill="#94A3B8" font-family="Inter, DejaVu Sans, sans-serif" font-size="18" text-anchor="end">Total Track Duration: 05:42</text>
        
        <!-- FULL TRACK TIMELINE TRACK -->
        <g transform="translate(0, 45)">
          <!-- Base Track Bar -->
          <rect width="2590" height="90" rx="16" fill="#0B0F19" stroke="#334155" stroke-width="2"/>
          
          <!-- Subtle tick marks -->
          {''.join(f'<line x1="{x}" y1="75" x2="{x}" y2="85" stroke="#334155" stroke-width="2"/>' for x in range(0, 2600, 130))}
          
          <!-- SEGMENT 1 (ACTIVE LOOP): 0:00 - 0:18 (18s) -->
          <g>
            <rect x="0" y="0" width="230" height="90" rx="16" fill="#064E3B" stroke="#10B981" stroke-width="3"/>
            <rect x="10" y="12" width="210" height="30" rx="6" fill="#10B981"/>
            <text x="115" y="33" fill="#0F172A" font-family="Inter, DejaVu Sans, sans-serif" font-size="15" font-weight="900" text-anchor="middle">ACTIVE LOOP [0:00–0:18]</text>
            <text x="115" y="70" fill="#A7F3D0" font-family="Inter, DejaVu Sans, sans-serif" font-size="15" font-weight="700" text-anchor="middle">Rhodes Intro (No Drums)</text>
          </g>

          <!-- Playhead Marker -->
          <line x1="80" y1="-10" x2="80" y2="100" stroke="#FFFFFF" stroke-width="4"/>
          <circle cx="80" cy="-10" r="8" fill="#FFFFFF"/>

          <!-- SEGMENT 2: 1:15 - 1:35 (20s) -->
          <g transform="translate(560, 0)">
            <rect width="260" height="90" rx="14" fill="#0C4A6E" stroke="#0284C7" stroke-width="2"/>
            <text x="130" y="36" fill="#7DD3FC" font-family="Inter, DejaVu Sans, sans-serif" font-size="15" font-weight="800" text-anchor="middle">1:15 – 1:35 [20s]</text>
            <text x="130" y="68" fill="#BAE6FD" font-family="Inter, DejaVu Sans, sans-serif" font-size="15" font-weight="600" text-anchor="middle">Trombone Solo Break</text>
          </g>

          <!-- SEGMENT 3: 3:40 - 4:05 (25s) -->
          <g transform="translate(1660, 0)">
            <rect width="320" height="90" rx="14" fill="#3B0764" stroke="#9333EA" stroke-width="2"/>
            <text x="160" y="36" fill="#E9D5FF" font-family="Inter, DejaVu Sans, sans-serif" font-size="15" font-weight="800" text-anchor="middle">3:40 – 4:05 [25s]</text>
            <text x="160" y="68" fill="#F3E8FF" font-family="Inter, DejaVu Sans, sans-serif" font-size="15" font-weight="600" text-anchor="middle">Bassline + Drum Break Outro</text>
          </g>
        </g>
      </g>

      <!-- Player Controls Toolbar -->
      <g transform="translate(0, 325)">
        <rect width="2590" height="85" rx="16" fill="#0F172A" stroke="#334155" stroke-width="2"/>
        
        <!-- Play / Pause Buttons -->
        <g transform="translate(30, 18)">
          <rect width="180" height="50" rx="12" fill="#10B981"/>
          <text x="90" y="33" fill="#0F172A" font-family="Inter, DejaVu Sans, sans-serif" font-size="18" font-weight="800" text-anchor="middle">❚❚ PAUSE LOOP</text>
        </g>

        <!-- Loop Indicator Button -->
        <g transform="translate(230, 18)">
          <rect width="360" height="50" rx="12" fill="#1E293B" stroke="#10B981" stroke-width="2"/>
          <text x="180" y="33" fill="#10B981" font-family="Inter, DejaVu Sans, sans-serif" font-size="17" font-weight="700" text-anchor="middle">🔁 Boundary Looping: ON (0:00–0:18)</text>
        </g>

        <g transform="translate(610, 18)">
          <rect width="180" height="50" rx="12" fill="#1E293B" stroke="#334155" stroke-width="1.5"/>
          <text x="90" y="33" fill="#CBD5E1" font-family="Inter, DejaVu Sans, sans-serif" font-size="16" font-weight="600" text-anchor="middle">⏪ -5s Jump</text>
        </g>

        <g transform="translate(810, 18)">
          <rect width="180" height="50" rx="12" fill="#1E293B" stroke="#334155" stroke-width="1.5"/>
          <text x="90" y="33" fill="#CBD5E1" font-family="Inter, DejaVu Sans, sans-serif" font-size="16" font-weight="600" text-anchor="middle">⏩ +5s Jump</text>
        </g>

        <!-- Right: Cue Tolerance Note -->
        <text x="2540" y="50" fill="#94A3B8" font-family="Inter, DejaVu Sans, sans-serif" font-size="17" font-weight="500" text-anchor="end">IFrame seekTo latency: &lt; 1.2s • Rough Auditioning Loop Active</text>
      </g>

      <!-- Tagging and Crate Actions Bar -->
      <g transform="translate(0, 440)">
        <text x="0" y="30" fill="#CBD5E1" font-family="Inter, DejaVu Sans, sans-serif" font-size="20" font-weight="700">ACTIVE SEGMENT TAGS (0:00 – 0:18):</text>
        
        <!-- Tier 1 Objective Presets -->
        <g transform="translate(370, 0)">
          <rect x="0" y="0" width="220" height="46" rx="10" fill="#064E3B" stroke="#10B981" stroke-width="2"/>
          <text x="110" y="29" fill="#A7F3D0" font-family="Inter, DejaVu Sans, sans-serif" font-size="16" font-weight="800" text-anchor="middle">[Isolation: No Vocals]</text>

          <rect x="235" y="0" width="220" height="46" rx="10" fill="#064E3B" stroke="#10B981" stroke-width="2"/>
          <text x="345" y="29" fill="#A7F3D0" font-family="Inter, DejaVu Sans, sans-serif" font-size="16" font-weight="800" text-anchor="middle">[Isolation: No Drums]</text>

          <rect x="470" y="0" width="260" height="46" rx="10" fill="#064E3B" stroke="#10B981" stroke-width="2"/>
          <text x="600" y="29" fill="#A7F3D0" font-family="Inter, DejaVu Sans, sans-serif" font-size="16" font-weight="800" text-anchor="middle">[Inst: Rhodes Piano]</text>

          <rect x="745" y="0" width="180" height="46" rx="10" fill="#064E3B" stroke="#10B981" stroke-width="2"/>
          <text x="835" y="29" fill="#A7F3D0" font-family="Inter, DejaVu Sans, sans-serif" font-size="16" font-weight="800" text-anchor="middle">[Section: Intro]</text>

          <!-- Tier 2 Contextual Tags -->
          <rect x="940" y="0" width="180" height="46" rx="10" fill="#1E293B" stroke="#475569" stroke-width="1.5"/>
          <text x="1030" y="29" fill="#94A3B8" font-family="Inter, DejaVu Sans, sans-serif" font-size="16" font-weight="600" text-anchor="middle">[Lo-Fi / Dusty]</text>

          <rect x="1135" y="0" width="210" height="46" rx="10" fill="#1E293B" stroke="#475569" stroke-width="1.5"/>
          <text x="1240" y="29" fill="#94A3B8" font-family="Inter, DejaVu Sans, sans-serif" font-size="16" font-weight="600" text-anchor="middle">[1970s Jazz-Fusion]</text>
        </g>

        <!-- Right: Primary Save Crate Action -->
        <g transform="translate(1950, -5)">
          <rect width="640" height="56" rx="14" fill="#10B981" stroke="#34D399" stroke-width="2"/>
          <text x="320" y="36" fill="#0F172A" font-family="Inter, DejaVu Sans, sans-serif" font-size="20" font-weight="900" text-anchor="middle">＋ SAVE TO PERSONAL CLOUD CRATE</text>
        </g>
      </g>
    </g>
  </g>

  <!-- 3. Passage Recommendation Feed Below -->
  <g transform="translate(80, 885)">
    <!-- Section Container Header -->
    <g transform="translate(0, 0)">
      <rect x="0" y="0" width="560" height="40" rx="8" fill="#1E293B" stroke="#334155" stroke-width="1.5"/>
      <text x="280" y="26" fill="#F59E0B" font-family="Inter, DejaVu Sans, sans-serif" font-size="17" font-weight="800" text-anchor="middle">SEED-PASSAGE BERRYPICKING RECOMMENDATIONS</text>
      
      <!-- Critical Header Title replacing old fake similarity -->
      <text x="0" y="85" fill="#F8FAFC" font-family="Inter, DejaVu Sans, sans-serif" font-size="38" font-weight="800">MATCHING PASSAGES ACROSS CATALOG (Ranked by Preset Tag Overlap)</text>
      <text x="0" y="125" fill="#94A3B8" font-family="Inter, DejaVu Sans, sans-serif" font-size="22">Passages sharing [Rhodes Piano] + [No Vocals] + [No Drums] + [Intro] across public streaming catalog</text>
    </g>

    <!-- 4 Ranked Passage Cards -->
    <g transform="translate(0, 160)">
      <!-- Card 1 (4/4 Match) -->
      <g transform="translate(0, 0)">
        <rect width="3740" height="240" rx="20" fill="url(#panelBg)" stroke="#10B981" stroke-width="2.5"/>
        
        <!-- Left Thumbnail Placeholder -->
        <rect x="30" y="30" width="280" height="180" rx="14" fill="#022C22" stroke="#059669" stroke-width="2"/>
        <text x="170" y="110" fill="#10B981" font-family="Inter, DejaVu Sans, sans-serif" font-size="28" text-anchor="middle">▶</text>
        <text x="170" y="150" fill="#6EE7B7" font-family="Inter, DejaVu Sans, sans-serif" font-size="18" font-weight="700" text-anchor="middle">0:00 – 0:14 (14s)</text>

        <!-- Track Info -->
        <g transform="translate(340, 45)">
          <text x="0" y="35" fill="#F8FAFC" font-family="Inter, DejaVu Sans, sans-serif" font-size="32" font-weight="800">Ryo Fukui — Early Summer (Scenery, 1976)</text>
          <text x="0" y="75" fill="#94A3B8" font-family="Inter, DejaVu Sans, sans-serif" font-size="20">Catalog: Trio Records / YouTube ID: Hf69_k4V8aI • Segment Cue: 0:00–0:14</text>
          
          <!-- Tags -->
          <g transform="translate(0, 105)">
            <rect x="0" y="0" width="190" height="38" rx="8" fill="#064E3B"/>
            <text x="95" y="24" fill="#6EE7B7" font-family="Inter, DejaVu Sans, sans-serif" font-size="15" font-weight="700" text-anchor="middle">[Rhodes Piano]</text>

            <rect x="205" y="0" width="160" height="38" rx="8" fill="#064E3B"/>
            <text x="285" y="24" fill="#6EE7B7" font-family="Inter, DejaVu Sans, sans-serif" font-size="15" font-weight="700" text-anchor="middle">[No Vocals]</text>

            <rect x="380" y="0" width="160" height="38" rx="8" fill="#064E3B"/>
            <text x="460" y="24" fill="#6EE7B7" font-family="Inter, DejaVu Sans, sans-serif" font-size="15" font-weight="700" text-anchor="middle">[No Drums]</text>

            <rect x="555" y="0" width="140" height="38" rx="8" fill="#064E3B"/>
            <text x="625" y="24" fill="#6EE7B7" font-family="Inter, DejaVu Sans, sans-serif" font-size="15" font-weight="700" text-anchor="middle">[Intro Loop]</text>

            <rect x="710" y="0" width="170" height="38" rx="8" fill="#1E293B"/>
            <text x="795" y="24" fill="#94A3B8" font-family="Inter, DejaVu Sans, sans-serif" font-size="15" font-weight="600" text-anchor="middle">[Modal Jazz]</text>
          </g>
        </g>

        <!-- Right Match Badge & Audition Actions -->
        <g transform="translate(2950, 60)">
          <!-- Match Badge -->
          <rect width="360" height="52" rx="12" fill="#064E3B" stroke="#10B981" stroke-width="2"/>
          <text x="180" y="34" fill="#A7F3D0" font-family="Inter, DejaVu Sans, sans-serif" font-size="22" font-weight="900" text-anchor="middle">4/4 PRESET TAGS MATCH</text>

          <!-- Buttons -->
          <g transform="translate(390, 0)">
            <rect width="180" height="52" rx="12" fill="#10B981"/>
            <text x="90" y="33" fill="#0F172A" font-family="Inter, DejaVu Sans, sans-serif" font-size="18" font-weight="800" text-anchor="middle">▶ AUDITION</text>

            <rect x="200" y="0" width="160" height="52" rx="12" fill="#1E293B" stroke="#334155" stroke-width="1.5"/>
            <text x="280" y="33" fill="#CBD5E1" font-family="Inter, DejaVu Sans, sans-serif" font-size="18" font-weight="700" text-anchor="middle">＋ CRATE</text>
          </g>
        </g>
      </g>

      <!-- Card 2 (3/4 Match) -->
      <g transform="translate(0, 270)">
        <rect width="3740" height="240" rx="20" fill="url(#panelBg)" stroke="#334155" stroke-width="2"/>
        
        <rect x="30" y="30" width="280" height="180" rx="14" fill="#0F172A" stroke="#334155" stroke-width="2"/>
        <text x="170" y="110" fill="#38BDF8" font-family="Inter, DejaVu Sans, sans-serif" font-size="28" text-anchor="middle">▶</text>
        <text x="170" y="150" fill="#7DD3FC" font-family="Inter, DejaVu Sans, sans-serif" font-size="18" font-weight="700" text-anchor="middle">2:04 – 2:22 (18s)</text>

        <g transform="translate(340, 45)">
          <text x="0" y="35" fill="#F8FAFC" font-family="Inter, DejaVu Sans, sans-serif" font-size="32" font-weight="800">Jiro Inagaki &amp; Soul Media — Breeze (Funky Stuff, 1975)</text>
          <text x="0" y="75" fill="#94A3B8" font-family="Inter, DejaVu Sans, sans-serif" font-size="20">Catalog: Nippon Columbia / YouTube ID: mX78_q5Lk2P • Segment Cue: 2:04–2:22</text>
          
          <g transform="translate(0, 105)">
            <rect x="0" y="0" width="190" height="38" rx="8" fill="#064E3B"/>
            <text x="95" y="24" fill="#6EE7B7" font-family="Inter, DejaVu Sans, sans-serif" font-size="15" font-weight="700" text-anchor="middle">[Rhodes Piano]</text>

            <rect x="205" y="0" width="160" height="38" rx="8" fill="#064E3B"/>
            <text x="285" y="24" fill="#6EE7B7" font-family="Inter, DejaVu Sans, sans-serif" font-size="15" font-weight="700" text-anchor="middle">[No Vocals]</text>

            <rect x="380" y="0" width="180" height="38" rx="8" fill="#064E3B"/>
            <text x="470" y="24" fill="#6EE7B7" font-family="Inter, DejaVu Sans, sans-serif" font-size="15" font-weight="700" text-anchor="middle">[Solo Section]</text>

            <rect x="575" y="0" width="180" height="38" rx="8" fill="#1E293B"/>
            <text x="665" y="24" fill="#94A3B8" font-family="Inter, DejaVu Sans, sans-serif" font-size="15" font-weight="600" text-anchor="middle">[Jazz-Fusion]</text>
          </g>
        </g>

        <g transform="translate(2950, 60)">
          <rect width="360" height="52" rx="12" fill="#1E293B" stroke="#059669" stroke-width="2"/>
          <text x="180" y="34" fill="#6EE7B7" font-family="Inter, DejaVu Sans, sans-serif" font-size="22" font-weight="900" text-anchor="middle">3/4 PRESET TAGS MATCH</text>

          <g transform="translate(390, 0)">
            <rect width="180" height="52" rx="12" fill="#10B981"/>
            <text x="90" y="33" fill="#0F172A" font-family="Inter, DejaVu Sans, sans-serif" font-size="18" font-weight="800" text-anchor="middle">▶ AUDITION</text>

            <rect x="200" y="0" width="160" height="52" rx="12" fill="#1E293B" stroke="#334155" stroke-width="1.5"/>
            <text x="280" y="33" fill="#CBD5E1" font-family="Inter, DejaVu Sans, sans-serif" font-size="18" font-weight="700" text-anchor="middle">＋ CRATE</text>
          </g>
        </g>
      </g>

      <!-- Card 3 (3/4 Match) -->
      <g transform="translate(0, 540)">
        <rect width="3740" height="240" rx="20" fill="url(#panelBg)" stroke="#334155" stroke-width="2"/>
        
        <rect x="30" y="30" width="280" height="180" rx="14" fill="#0F172A" stroke="#334155" stroke-width="2"/>
        <text x="170" y="110" fill="#38BDF8" font-family="Inter, DejaVu Sans, sans-serif" font-size="28" text-anchor="middle">▶</text>
        <text x="170" y="150" fill="#7DD3FC" font-family="Inter, DejaVu Sans, sans-serif" font-size="18" font-weight="700" text-anchor="middle">0:00 – 0:16 (16s)</text>

        <g transform="translate(340, 45)">
          <text x="0" y="35" fill="#F8FAFC" font-family="Inter, DejaVu Sans, sans-serif" font-size="32" font-weight="800">Placebo — Humpty Dumpty (Ball of Eyes, 1971)</text>
          <text x="0" y="75" fill="#94A3B8" font-family="Inter, DejaVu Sans, sans-serif" font-size="20">Catalog: CBS Records / YouTube ID: pL90_v8Nw1K • Segment Cue: 0:00–0:16</text>
          
          <g transform="translate(0, 105)">
            <rect x="0" y="0" width="190" height="38" rx="8" fill="#064E3B"/>
            <text x="95" y="24" fill="#6EE7B7" font-family="Inter, DejaVu Sans, sans-serif" font-size="15" font-weight="700" text-anchor="middle">[Electric Piano]</text>

            <rect x="205" y="0" width="160" height="38" rx="8" fill="#064E3B"/>
            <text x="285" y="24" fill="#6EE7B7" font-family="Inter, DejaVu Sans, sans-serif" font-size="15" font-weight="700" text-anchor="middle">[No Vocals]</text>

            <rect x="380" y="0" width="160" height="38" rx="8" fill="#064E3B"/>
            <text x="460" y="24" fill="#6EE7B7" font-family="Inter, DejaVu Sans, sans-serif" font-size="15" font-weight="700" text-anchor="middle">[Intro Loop]</text>

            <rect x="555" y="0" width="220" height="38" rx="8" fill="#1E293B"/>
            <text x="665" y="24" fill="#94A3B8" font-family="Inter, DejaVu Sans, sans-serif" font-size="15" font-weight="600" text-anchor="middle">[Funk / Rare Groove]</text>
          </g>
        </g>

        <g transform="translate(2950, 60)">
          <rect width="360" height="52" rx="12" fill="#1E293B" stroke="#059669" stroke-width="2"/>
          <text x="180" y="34" fill="#6EE7B7" font-family="Inter, DejaVu Sans, sans-serif" font-size="22" font-weight="900" text-anchor="middle">3/4 PRESET TAGS MATCH</text>

          <g transform="translate(390, 0)">
            <rect width="180" height="52" rx="12" fill="#10B981"/>
            <text x="90" y="33" fill="#0F172A" font-family="Inter, DejaVu Sans, sans-serif" font-size="18" font-weight="800" text-anchor="middle">▶ AUDITION</text>

            <rect x="200" y="0" width="160" height="52" rx="12" fill="#1E293B" stroke="#334155" stroke-width="1.5"/>
            <text x="280" y="33" fill="#CBD5E1" font-family="Inter, DejaVu Sans, sans-serif" font-size="18" font-weight="700" text-anchor="middle">＋ CRATE</text>
          </g>
        </g>
      </g>

      <!-- Card 4 (3/4 Match) -->
      <g transform="translate(0, 810)">
        <rect width="3740" height="240" rx="20" fill="url(#panelBg)" stroke="#334155" stroke-width="2"/>
        
        <rect x="30" y="30" width="280" height="180" rx="14" fill="#0F172A" stroke="#334155" stroke-width="2"/>
        <text x="170" y="110" fill="#38BDF8" font-family="Inter, DejaVu Sans, sans-serif" font-size="28" text-anchor="middle">▶</text>
        <text x="170" y="150" fill="#7DD3FC" font-family="Inter, DejaVu Sans, sans-serif" font-size="18" font-weight="700" text-anchor="middle">3:12 – 3:30 (18s)</text>

        <g transform="translate(340, 45)">
          <text x="0" y="35" fill="#F8FAFC" font-family="Inter, DejaVu Sans, sans-serif" font-size="32" font-weight="800">Azymuth — Linha do Horizonte (Azymuth, 1975)</text>
          <text x="0" y="75" fill="#94A3B8" font-family="Inter, DejaVu Sans, sans-serif" font-size="20">Catalog: Som Livre / YouTube ID: zK88_w2Lm7Q • Segment Cue: 3:12–3:30</text>
          
          <g transform="translate(0, 105)">
            <rect x="0" y="0" width="190" height="38" rx="8" fill="#064E3B"/>
            <text x="95" y="24" fill="#6EE7B7" font-family="Inter, DejaVu Sans, sans-serif" font-size="15" font-weight="700" text-anchor="middle">[Rhodes Piano]</text>

            <rect x="205" y="0" width="160" height="38" rx="8" fill="#064E3B"/>
            <text x="285" y="24" fill="#6EE7B7" font-family="Inter, DejaVu Sans, sans-serif" font-size="15" font-weight="700" text-anchor="middle">[No Drums]</text>

            <rect x="380" y="0" width="180" height="38" rx="8" fill="#064E3B"/>
            <text x="470" y="24" fill="#6EE7B7" font-family="Inter, DejaVu Sans, sans-serif" font-size="15" font-weight="700" text-anchor="middle">[Bridge / Break]</text>

            <rect x="575" y="0" width="180" height="38" rx="8" fill="#1E293B"/>
            <text x="665" y="24" fill="#94A3B8" font-family="Inter, DejaVu Sans, sans-serif" font-size="15" font-weight="600" text-anchor="middle">[MPB / Fusion]</text>
          </g>
        </g>

        <g transform="translate(2950, 60)">
          <rect width="360" height="52" rx="12" fill="#1E293B" stroke="#059669" stroke-width="2"/>
          <text x="180" y="34" fill="#6EE7B7" font-family="Inter, DejaVu Sans, sans-serif" font-size="22" font-weight="900" text-anchor="middle">3/4 PRESET TAGS MATCH</text>

          <g transform="translate(390, 0)">
            <rect width="180" height="52" rx="12" fill="#10B981"/>
            <text x="90" y="33" fill="#0F172A" font-family="Inter, DejaVu Sans, sans-serif" font-size="18" font-weight="800" text-anchor="middle">▶ AUDITION</text>

            <rect x="200" y="0" width="160" height="52" rx="12" fill="#1E293B" stroke="#334155" stroke-width="1.5"/>
            <text x="280" y="33" fill="#CBD5E1" font-family="Inter, DejaVu Sans, sans-serif" font-size="18" font-weight="700" text-anchor="middle">＋ CRATE</text>
          </g>
        </g>
      </g>
    </g>
  </g>
</svg>'''
    render_svg_to_png(svg, f"{OUT_DIR}/ui_concept_mockup.png", w, h)

if __name__ == "__main__":
    print("Generating Figure 1: problem_bottlenecks.png...")
    generate_problem_bottlenecks()
    print("Generating Figure 3: architecture_overview.png...")
    generate_architecture_overview()
    print("Generating Figure 4: before_after_workflow.png...")
    generate_before_after()
    print("Generating Figure 5: ui_concept_mockup.png...")
    generate_ui_mockup()
    print("All diagrams generated successfully!")
