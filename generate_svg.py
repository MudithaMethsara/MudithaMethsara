import base64
import os
import json
import hashlib
import urllib.request
from datetime import datetime

# ==============================================================================
# 1. Dynamic Calculations: Experience, Projects, & Happy Clients
# ==============================================================================

# A. Experience: Starts from 2022, automatically calculates based on current year
EXPERIENCE_START_YEAR = 2022
current_year = datetime.now().year
current_month = datetime.now().month
experience_years = max(1, current_year - EXPERIENCE_START_YEAR)
experience_str = f"{experience_years}"

# B. Projects Completed: Starts from 30, automatically increments (+1) per new repository
BASELINE_PROJECTS = 30
BASELINE_REPOS = 5  # Baseline public repos at project setup

project_count = BASELINE_PROJECTS
try:
    url = "https://api.github.com/users/MudithaMethsara"
    token = os.environ.get("GITHUB_TOKEN")
    headers = {"User-Agent": "Mozilla/5.0 (Python)"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=5) as response:
        user_data = json.loads(response.read().decode("utf-8"))
        current_repos = user_data.get("public_repos", BASELINE_REPOS)
        # Add 1 to baseline for each new repo created beyond baseline
        new_repos = max(0, current_repos - BASELINE_REPOS)
        project_count = BASELINE_PROJECTS + new_repos
except Exception as e:
    print(f"Note: Using baseline project count ({BASELINE_PROJECTS}) due to: {e}")

project_str = f"{project_count}+"

# C. Happy Clients: Starts from 40, automatically & deterministically adds +1 or +2 each month
CLIENTS_BASELINE = 40
CLIENTS_START_YEAR = 2026
CLIENTS_START_MONTH = 9  # Baseline month: September 2026

def calculate_happy_clients(cur_year, cur_month):
    total_months_elapsed = (cur_year - CLIENTS_START_YEAR) * 12 + (cur_month - CLIENTS_START_MONTH)
    if total_months_elapsed <= 0:
        return CLIENTS_BASELINE
    
    added = 0
    y = CLIENTS_START_YEAR
    m = CLIENTS_START_MONTH
    for _ in range(total_months_elapsed):
        m += 1
        if m > 12:
            m = 1
            y += 1
        # Deterministic pseudo-random seed per month (generates +1 or +2 consistently)
        seed = int(hashlib.md5(f"happy_clients_{y}_{m}".encode()).hexdigest(), 16)
        increment = 1 + (seed % 2)  # Either +1 or +2
        added += increment
    return CLIENTS_BASELINE + added

happy_clients_count = calculate_happy_clients(current_year, current_month)
happy_clients_str = f"{happy_clients_count}+"

print(f"Calculated Metrics -> Experience: {experience_str} yr | Projects: {project_str} | Happy Clients: {happy_clients_str}")

# ==============================================================================
# 2. Base64 Encode Profile Image
# ==============================================================================

img_path = "assets/profile.webp"
if not os.path.exists(img_path):
    img_path = os.path.join(os.path.dirname(__file__), "assets/profile.webp")

with open(img_path, "rb") as f:
    b64_img = base64.b64encode(f.read()).decode("utf-8")

# ==============================================================================
# 3. Construct SVG Banner Content
# ==============================================================================

svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 560" width="100%" height="100%">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@400;500;600;700&amp;family=Lora:ital,wght@0,400;0,500;0,600;1,400;1,500&amp;display=swap');
      
      .body-bg {{ fill: #F7F7F8; }}
      .card-bg {{ fill: #ECEEF0; stroke: #E0E2E6; stroke-width: 1; rx: 16px; }}
      .font-sans {{ font-family: 'Instrument Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }}
      .font-serif {{ font-family: 'Lora', Georgia, 'Times New Roman', serif; }}
      
      .hero-title {{ font-family: 'Lora', Georgia, 'Times New Roman', serif; font-size: 50px; font-weight: 500; font-style: normal; fill: #121218; letter-spacing: -1.2px; line-height: 1.12; }}
      .hero-title-muted {{ font-family: 'Lora', Georgia, 'Times New Roman', serif; font-weight: 500; font-style: normal; fill: #94979E; }}
      .hero-sub {{ font-family: 'Instrument Sans', sans-serif; font-size: 15px; font-weight: 400; fill: #61646B; }}
      
      .stat-val {{ font-family: 'Instrument Sans', sans-serif; font-size: 28px; font-weight: 700; fill: #121218; letter-spacing: -0.5px; }}
      .stat-lbl {{ font-family: 'Instrument Sans', sans-serif; font-size: 12px; font-weight: 400; fill: #555861; }}
      
      .float-card {{ fill: #14151B; stroke: rgba(255, 255, 255, 0.12); stroke-width: 1; rx: 14px; }}
      .float-sub {{ font-family: 'Instrument Sans', sans-serif; font-size: 10.5px; font-weight: 500; fill: #8A8E9B; text-transform: uppercase; letter-spacing: 0.5px; }}
      .float-title {{ font-family: 'Instrument Sans', sans-serif; font-size: 13.5px; font-weight: 600; fill: #FFFFFF; }}
      .float-desc {{ font-family: 'Instrument Sans', sans-serif; font-size: 11px; font-weight: 400; fill: #94979E; }}
      
      .tech-item {{ font-family: 'Instrument Sans', sans-serif; font-size: 13.5px; font-weight: 600; fill: #121218; letter-spacing: -0.2px; }}
    </style>

    <clipPath id="cardClip">
      <rect x="20" y="24" width="920" height="455" rx="16" />
    </clipPath>

    <filter id="photoGrayscale">
      <feColorMatrix type="matrix" values="0.33 0.33 0.33 0 0  0.33 0.33 0.33 0 0  0.33 0.33 0.33 0 0  0 0 0 1 0" />
      <feComponentTransfer>
        <feFuncR type="linear" slope="1.08" intercept="-0.04" />
        <feFuncG type="linear" slope="1.08" intercept="-0.04" />
        <feFuncB type="linear" slope="1.08" intercept="-0.04" />
      </feComponentTransfer>
    </filter>

    <pattern id="bgHatch" width="12" height="12" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">
      <line x1="0" y1="0" x2="0" y2="12" stroke="#E5E7EB" stroke-width="1.2" opacity="0.55" />
    </pattern>

    <filter id="cardShadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="8" stdDeviation="16" flood-color="#000000" flood-opacity="0.035" />
    </filter>

    <filter id="floatShadow" x="-10%" y="-10%" width="125%" height="130%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="12" stdDeviation="16" flood-color="#000000" flood-opacity="0.28" />
    </filter>

    <linearGradient id="fadeGradient" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ECEEF0" stop-opacity="1" />
      <stop offset="100%" stop-color="#ECEEF0" stop-opacity="0" />
    </linearGradient>
  </defs>

  <!-- Outer Canvas Pattern -->
  <rect width="960" height="560" fill="#F7F7F8" />
  <rect width="960" height="560" fill="url(#bgHatch)" />

  <!-- ==================== MAIN HERO CARD ==================== -->
  <!-- Background Card -->
  <g filter="url(#cardShadow)">
    <rect x="20" y="24" width="920" height="455" class="card-bg" />
  </g>

  <!-- Clipped Content Group -->
  <g clip-path="url(#cardClip)">
    <!-- Portrait Photo -->
    <image href="data:image/webp;base64,{b64_img}" x="450" y="24" width="490" height="455" preserveAspectRatio="xMidYMin slice" filter="url(#photoGrayscale)" />
    
    <!-- Soft Gradient Fade from Card Left to Portrait -->
    <rect x="390" y="24" width="170" height="455" fill="url(#fadeGradient)" opacity="0.95" />

    <!-- Left Hero Content -->
    <g transform="translate(60, 60)">
      <!-- Main Heading Line 1 -->
      <text x="0" y="52" class="hero-title">Build better</text>
      <!-- Main Heading Line 2: Serif 'Lora' font with normal upright style -->
      <text x="0" y="110" class="hero-title">software, <tspan class="hero-title-muted">faster</tspan></text>

      <!-- Subtitle -->
      <text x="0" y="166" class="hero-sub">I build scalable web applications, APIs, and full-stack</text>
      <text x="0" y="188" class="hero-sub">solutions for startups and enterprise teams.</text>

      <!-- Dynamic Metrics Row -->
      <g transform="translate(0, 305)">
        <!-- Metric 1: Automated Projects Completed -->
        <g transform="translate(0, 0)">
          <text x="0" y="0" class="stat-val">{project_str}</text>
          <text x="0" y="22" class="stat-lbl">Projects completed</text>
        </g>

        <!-- Metric 2: Automated Experience Years -->
        <g transform="translate(140, 0)">
          <text x="0" y="0" class="stat-val">{experience_str} <tspan font-size="18" font-weight="500" fill="#555861">yr</tspan></text>
          <text x="0" y="22" class="stat-lbl">Experience</text>
        </g>

        <!-- Metric 3: Automated Happy Clients -->
        <g transform="translate(250, 0)">
          <text x="0" y="0" class="stat-val">{happy_clients_str}</text>
          <text x="0" y="22" class="stat-lbl">Happy clients</text>
        </g>
      </g>
    </g>

    <!-- Floating Dark Card (Lower Right over Portrait) -->
    <g transform="translate(590, 325)" filter="url(#floatShadow)">
      <rect width="285" height="125" class="float-card" />
      
      <!-- Sub-label -->
      <text x="22" y="30" class="float-sub">Select project</text>
      
      <!-- Title with pulsing green status dot -->
      <g transform="translate(22, 54)">
        <circle cx="4" cy="-4" r="4" fill="#83CA16">
          <animate attributeName="opacity" values="1;0.4;1" dur="2s" repeatCount="indefinite" />
        </circle>
        <text x="16" y="0" class="float-title">Available for projects</text>
      </g>
      
      <!-- Description -->
      <text x="22" y="80" class="float-desc">Share a few details, and I'll get back</text>
      <text x="22" y="96" class="float-desc">with a clear direction.</text>

      <!-- Circular Arrow Button -->
      <g transform="translate(242, 85)">
        <circle cx="0" cy="0" r="15" fill="#FFFFFF" />
        <path d="M-4 4 L4 -4 M4 -4 H-1 M4 -4 V1" stroke="#121218" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" fill="none" />
      </g>
    </g>
  </g>

  <!-- ==================== BOTTOM TECH LOGO STRIP ==================== -->
  <g transform="translate(480, 520)">
    <!-- 1. Java -->
    <g transform="translate(-410, 0)">
      <g transform="translate(-10, -9) scale(0.85)">
        <path d="M18 8h1a4 4 0 0 1 0 8h-1" stroke="#121218" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" fill="none" />
        <path d="M2 8h16v9a4 4 0 0 1-4 4H6a4 4 0 0 1-4-4V8z" stroke="#121218" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" fill="none" />
        <path d="M6 1v3 M10 1v3 M14 1v3" stroke="#121218" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" fill="none" />
      </g>
      <text x="16" y="5" class="tech-item">Java</text>
    </g>

    <!-- 2. Python -->
    <g transform="translate(-310, 0)">
      <g transform="translate(-10, -9) scale(0.85)">
        <path d="M12 2H8a4 4 0 0 0-4 4v3a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2V7a2 2 0 0 0-2-2H6" stroke="#121218" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" fill="none" />
        <path d="M12 22h4a4 4 0 0 0 4-4v-3a2 2 0 0 0-2-2h-6a2 2 0 0 0-2 2v2a2 2 0 0 0 2 2h6" stroke="#121218" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" fill="none" />
        <circle cx="8" cy="6" r="1.2" fill="#121218" />
        <circle cx="16" cy="18" r="1.2" fill="#121218" />
      </g>
      <text x="16" y="5" class="tech-item">Python</text>
    </g>

    <!-- 3. Spring Boot -->
    <g transform="translate(-185, 0)">
      <g transform="translate(-10, -9) scale(0.85)">
        <circle cx="12" cy="12" r="9.5" stroke="#121218" stroke-width="1.8" fill="none" />
        <path d="M8 14c2-4 6-6 8-6-1 4-3 8-8 8z" stroke="#121218" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" fill="none" />
        <path d="M9 13l4-2" stroke="#121218" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" fill="none" />
      </g>
      <text x="16" y="5" class="tech-item">Spring Boot</text>
    </g>

    <!-- 4. PostgreSQL -->
    <g transform="translate(-30, 0)">
      <g transform="translate(-10, -9) scale(0.85)">
        <ellipse cx="12" cy="5" rx="9" ry="3" stroke="#121218" stroke-width="1.8" fill="none" />
        <path d="M21 12c0 1.66-4 3-9 3s-9-1.34-9-3" stroke="#121218" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" fill="none" />
        <path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5" stroke="#121218" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" fill="none" />
      </g>
      <text x="16" y="5" class="tech-item">PostgreSQL</text>
    </g>

    <!-- 5. Tailwind CSS -->
    <g transform="translate(125, 0)">
      <g transform="translate(-10, -9) scale(0.85)">
        <path d="M6 10c1.5-3 3.5-4 6-3 1.5.6 2.5 1.8 3.5 3 1.5 1.8 3 3 6.5 2 0 0-2 5-6 4-1.5-.4-2.5-1.6-3.5-2.8C10.5 11.4 9 10.2 6 10z" stroke="#121218" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" fill="none" />
        <path d="M2 17c1.5-3 3.5-4 6-3 1.5.6 2.5 1.8 3.5 3 1.5 1.8 3 3 6.5 2" stroke="#121218" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" fill="none" />
      </g>
      <text x="16" y="5" class="tech-item">Tailwind CSS</text>
    </g>

    <!-- 6. Docker -->
    <g transform="translate(270, 0)">
      <g transform="translate(-10, -9) scale(0.85)">
        <rect x="4.5" y="8.5" width="3" height="3" rx="0.5" stroke="#121218" stroke-width="1.8" fill="none" />
        <rect x="8.5" y="8.5" width="3" height="3" rx="0.5" stroke="#121218" stroke-width="1.8" fill="none" />
        <rect x="12.5" y="8.5" width="3" height="3" rx="0.5" stroke="#121218" stroke-width="1.8" fill="none" />
        <rect x="8.5" y="4.5" width="3" height="3" rx="0.5" stroke="#121218" stroke-width="1.8" fill="none" />
        <path d="M2 12.5h17a4 4 0 0 1 3 3.5c-.8 2.5-3.5 4.5-8 4.5-6.5 0-9.5-3-12-8z" stroke="#121218" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" fill="none" />
      </g>
      <text x="16" y="5" class="tech-item">Docker</text>
    </g>

    <!-- 7. Git & GitHub -->
    <g transform="translate(375, 0)">
      <g transform="translate(-10, -9) scale(0.85)">
        <circle cx="6" cy="6" r="2.5" stroke="#121218" stroke-width="1.8" fill="none" />
        <circle cx="6" cy="18" r="2.5" stroke="#121218" stroke-width="1.8" fill="none" />
        <circle cx="18" cy="9" r="2.5" stroke="#121218" stroke-width="1.8" fill="none" />
        <path d="M6 8.5v7" stroke="#121218" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" fill="none" />
        <path d="M6 12a4 4 0 0 0 4 4h2a4 4 0 0 0 4-4V11.5" stroke="#121218" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" fill="none" />
      </g>
      <text x="16" y="5" class="tech-item">Git &amp; GitHub</text>
    </g>
  </g>
</svg>'''

output_path = "assets/header.svg"
if not os.path.exists("assets"):
    os.makedirs("assets", exist_ok=True)

with open(output_path, "w", encoding="utf-8") as f:
    f.write(svg_content)

print(f"Successfully generated {output_path} with automated dynamic metrics: Projects={project_str}, Experience={experience_str} yr, Happy Clients={happy_clients_str}")
