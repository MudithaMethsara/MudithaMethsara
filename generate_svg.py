import base64
import os
import json
import hashlib
import urllib.request
from datetime import datetime

# ==============================================================================
# 1. Dynamic Calculations: Experience, Projects, & Happy Clients
# ==============================================================================

EXPERIENCE_START_YEAR = 2022
current_year = datetime.now().year
current_month = datetime.now().month
experience_years = max(1, current_year - EXPERIENCE_START_YEAR)
experience_str = f"{experience_years}"

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
        new_repos = max(0, current_repos - BASELINE_REPOS)
        project_count = BASELINE_PROJECTS + new_repos
except Exception as e:
    print(f"Note: Using baseline project count ({BASELINE_PROJECTS}) due to: {e}")

project_str = f"{project_count}+"

CLIENTS_BASELINE = 40
CLIENTS_START_YEAR = 2026
CLIENTS_START_MONTH = 9

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
        seed = int(hashlib.md5(f"happy_clients_{y}_{m}".encode()).hexdigest(), 16)
        increment = 1 + (seed % 2)
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
# 3. Construct Unified Hero Card SVG (Single 12px Rounded Card - No Outer White Padding Box)
# ==============================================================================

svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" width="100%" height="100%">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@400;500;600;700&amp;family=Lora:ital,wght@0,400;0,500;0,600;1,400;1,500&amp;display=swap');
      
      .card-bg {{ fill: #ECEEF0; stroke: #D5D8DE; stroke-width: 1; }}
      .font-sans {{ font-family: 'Instrument Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }}
      .font-serif {{ font-family: 'Lora', Georgia, 'Times New Roman', serif; }}
      
      .hero-title {{ font-family: 'Lora', Georgia, 'Times New Roman', serif; font-size: 48px; font-weight: 500; font-style: normal; fill: #121218; letter-spacing: -1.2px; line-height: 1.12; }}
      .hero-title-muted {{ font-family: 'Lora', Georgia, 'Times New Roman', serif; font-weight: 500; font-style: normal; fill: #94979E; }}
      .hero-sub {{ font-family: 'Instrument Sans', sans-serif; font-size: 14.5px; font-weight: 400; fill: #61646B; }}
      
      .stat-val {{ font-family: 'Instrument Sans', sans-serif; font-size: 26px; font-weight: 700; fill: #121218; letter-spacing: -0.5px; }}
      .stat-lbl {{ font-family: 'Instrument Sans', sans-serif; font-size: 11.5px; font-weight: 400; fill: #555861; }}
      
      .float-card {{ fill: #14151B; stroke: rgba(255, 255, 255, 0.12); stroke-width: 1; rx: 12px; }}
      .float-sub {{ font-family: 'Instrument Sans', sans-serif; font-size: 10px; font-weight: 500; fill: #8A8E9B; text-transform: uppercase; letter-spacing: 0.5px; }}
      .float-title {{ font-family: 'Instrument Sans', sans-serif; font-size: 13px; font-weight: 600; fill: #FFFFFF; }}
      .float-desc {{ font-family: 'Instrument Sans', sans-serif; font-size: 10.5px; font-weight: 400; fill: #94979E; }}
      
      .tech-item {{ font-family: 'Instrument Sans', sans-serif; font-size: 13px; font-weight: 600; fill: #121218; letter-spacing: -0.2px; }}
    </style>

    <!-- Global 12px Corner Clip for the Entire Card -->
    <clipPath id="heroCardClip">
      <rect x="0" y="0" width="960" height="520" rx="12" />
    </clipPath>

    <filter id="photoGrayscale">
      <feColorMatrix type="matrix" values="0.33 0.33 0.33 0 0  0.33 0.33 0.33 0 0  0.33 0.33 0.33 0 0  0 0 0 1 0" />
      <feComponentTransfer>
        <feFuncR type="linear" slope="1.08" intercept="-0.04" />
        <feFuncG type="linear" slope="1.08" intercept="-0.04" />
        <feFuncB type="linear" slope="1.08" intercept="-0.04" />
      </feComponentTransfer>
    </filter>

    <pattern id="cardHatch" width="12" height="12" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">
      <line x1="0" y1="0" x2="0" y2="12" stroke="#E2E5E9" stroke-width="1.0" opacity="0.6" />
    </pattern>

    <filter id="floatShadow" x="-10%" y="-10%" width="125%" height="130%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="12" stdDeviation="16" flood-color="#000000" flood-opacity="0.32" />
    </filter>

    <linearGradient id="fadeGradient" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ECEEF0" stop-opacity="1" />
      <stop offset="100%" stop-color="#ECEEF0" stop-opacity="0" />
    </linearGradient>
  </defs>

  <!-- Unified Single Card Root Group (12px Radius) -->
  <g clip-path="url(#heroCardClip)">
    <!-- Base Card Surface -->
    <rect width="960" height="520" class="card-bg" rx="12" />
    <rect width="960" height="520" fill="url(#cardHatch)" rx="12" />

    <!-- Portrait Photo on Right Side -->
    <image href="data:image/webp;base64,{b64_img}" x="470" y="0" width="490" height="460" preserveAspectRatio="xMidYMin slice" filter="url(#photoGrayscale)" />
    
    <!-- Smooth Gradient Fade into Photo -->
    <rect x="400" y="0" width="180" height="460" fill="url(#fadeGradient)" opacity="0.96" />

    <!-- ==================== LEFT HERO CONTENT ==================== -->
    <g transform="translate(50, 48)">
      <!-- Main Heading Line 1 -->
      <text x="0" y="48" class="hero-title">Build better</text>
      <!-- Main Heading Line 2: Serif 'Lora' font with normal upright style -->
      <text x="0" y="104" class="hero-title">software, <tspan class="hero-title-muted">faster</tspan></text>

      <!-- Subtitle -->
      <text x="0" y="156" class="hero-sub">I build scalable web applications, APIs, and full-stack</text>
      <text x="0" y="176" class="hero-sub">solutions for startups and enterprise teams.</text>

      <!-- Dynamic Metrics Row -->
      <g transform="translate(0, 275)">
        <!-- Metric 1: Automated Projects Completed -->
        <g transform="translate(0, 0)">
          <text x="0" y="0" class="stat-val">{project_str}</text>
          <text x="0" y="20" class="stat-lbl">Projects completed</text>
        </g>

        <!-- Metric 2: Automated Experience Years -->
        <g transform="translate(140, 0)">
          <text x="0" y="0" class="stat-val">{experience_str} <tspan font-size="17" font-weight="500" fill="#555861">yr</tspan></text>
          <text x="0" y="20" class="stat-lbl">Experience</text>
        </g>

        <!-- Metric 3: Automated Happy Clients -->
        <g transform="translate(245, 0)">
          <text x="0" y="0" class="stat-val">{happy_clients_str}</text>
          <text x="0" y="20" class="stat-lbl">Happy clients</text>
        </g>
      </g>
    </g>

    <!-- Floating Dark Card (Lower Right over Portrait) -->
    <g transform="translate(600, 290)" filter="url(#floatShadow)">
      <rect width="280" height="120" rx="12" class="float-card" />
      
      <!-- Sub-label -->
      <text x="20" y="28" class="float-sub">Select project</text>
      
      <!-- Title with pulsing green status dot -->
      <g transform="translate(20, 50)">
        <circle cx="4" cy="-4" r="3.5" fill="#83CA16">
          <animate attributeName="opacity" values="1;0.4;1" dur="2s" repeatCount="indefinite" />
        </circle>
        <text x="15" y="0" class="float-title">Available for projects</text>
      </g>
      
      <!-- Description -->
      <text x="20" y="74" class="float-desc">Share a few details, and I'll get back</text>
      <text x="20" y="89" class="float-desc">with a clear direction.</text>

      <!-- Circular Arrow Button -->
      <g transform="translate(238, 80)">
        <circle cx="0" cy="0" r="14" fill="#FFFFFF" />
        <path d="M-3.5 3.5 L3.5 -3.5 M3.5 -3.5 H-1 M3.5 -3.5 V1" stroke="#121218" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" fill="none" />
      </g>
    </g>

    <!-- Bottom Footer Divider Line -->
    <line x1="0" y1="460" x2="960" y2="460" stroke="#DDE1E6" stroke-width="1" />

    <!-- ==================== INTEGRATED TECH LOGO STRIP ==================== -->
    <g transform="translate(480, 492)">
      <!-- 1. Java -->
      <g transform="translate(-410, 0)">
        <g transform="translate(-10, -9) scale(0.82)">
          <path d="M18 8h1a4 4 0 0 1 0 8h-1" stroke="#121218" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" fill="none" />
          <path d="M2 8h16v9a4 4 0 0 1-4 4H6a4 4 0 0 1-4-4V8z" stroke="#121218" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" fill="none" />
          <path d="M6 1v3 M10 1v3 M14 1v3" stroke="#121218" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" fill="none" />
        </g>
        <text x="14" y="5" class="tech-item">Java</text>
      </g>

      <!-- 2. Python -->
      <g transform="translate(-315, 0)">
        <g transform="translate(-10, -9) scale(0.82)">
          <path d="M12 2H8a4 4 0 0 0-4 4v3a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2V7a2 2 0 0 0-2-2H6" stroke="#121218" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" fill="none" />
          <path d="M12 22h4a4 4 0 0 0 4-4v-3a2 2 0 0 0-2-2h-6a2 2 0 0 0-2 2v2a2 2 0 0 0 2 2h6" stroke="#121218" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" fill="none" />
          <circle cx="8" cy="6" r="1.2" fill="#121218" />
          <circle cx="16" cy="18" r="1.2" fill="#121218" />
        </g>
        <text x="14" y="5" class="tech-item">Python</text>
      </g>

      <!-- 3. Spring Boot -->
      <g transform="translate(-195, 0)">
        <g transform="translate(-10, -9) scale(0.82)">
          <circle cx="12" cy="12" r="9.5" stroke="#121218" stroke-width="1.8" fill="none" />
          <path d="M8 14c2-4 6-6 8-6-1 4-3 8-8 8z" stroke="#121218" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" fill="none" />
          <path d="M9 13l4-2" stroke="#121218" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" fill="none" />
        </g>
        <text x="14" y="5" class="tech-item">Spring Boot</text>
      </g>

      <!-- 4. PostgreSQL -->
      <g transform="translate(-45, 0)">
        <g transform="translate(-10, -9) scale(0.82)">
          <ellipse cx="12" cy="5" rx="9" ry="3" stroke="#121218" stroke-width="1.8" fill="none" />
          <path d="M21 12c0 1.66-4 3-9 3s-9-1.34-9-3" stroke="#121218" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" fill="none" />
          <path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5" stroke="#121218" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" fill="none" />
        </g>
        <text x="14" y="5" class="tech-item">PostgreSQL</text>
      </g>

      <!-- 5. Tailwind CSS -->
      <g transform="translate(105, 0)">
        <g transform="translate(-10, -9) scale(0.82)">
          <path d="M6 10c1.5-3 3.5-4 6-3 1.5.6 2.5 1.8 3.5 3 1.5 1.8 3 3 6.5 2 0 0-2 5-6 4-1.5-.4-2.5-1.6-3.5-2.8C10.5 11.4 9 10.2 6 10z" stroke="#121218" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" fill="none" />
          <path d="M2 17c1.5-3 3.5-4 6-3 1.5.6 2.5 1.8 3.5 3 1.5 1.8 3 3 6.5 2" stroke="#121218" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" fill="none" />
        </g>
        <text x="14" y="5" class="tech-item">Tailwind CSS</text>
      </g>

      <!-- 6. Docker -->
      <g transform="translate(250, 0)">
        <g transform="translate(-10, -9) scale(0.82)">
          <rect x="4.5" y="8.5" width="3" height="3" rx="0.5" stroke="#121218" stroke-width="1.8" fill="none" />
          <rect x="8.5" y="8.5" width="3" height="3" rx="0.5" stroke="#121218" stroke-width="1.8" fill="none" />
          <rect x="12.5" y="8.5" width="3" height="3" rx="0.5" stroke="#121218" stroke-width="1.8" fill="none" />
          <rect x="8.5" y="4.5" width="3" height="3" rx="0.5" stroke="#121218" stroke-width="1.8" fill="none" />
          <path d="M2 12.5h17a4 4 0 0 1 3 3.5c-.8 2.5-3.5 4.5-8 4.5-6.5 0-9.5-3-12-8z" stroke="#121218" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" fill="none" />
        </g>
        <text x="14" y="5" class="tech-item">Docker</text>
      </g>

      <!-- 7. Git & GitHub -->
      <g transform="translate(355, 0)">
        <g transform="translate(-10, -9) scale(0.82)">
          <circle cx="6" cy="6" r="2.5" stroke="#121218" stroke-width="1.8" fill="none" />
          <circle cx="6" cy="18" r="2.5" stroke="#121218" stroke-width="1.8" fill="none" />
          <circle cx="18" cy="9" r="2.5" stroke="#121218" stroke-width="1.8" fill="none" />
          <path d="M6 8.5v7" stroke="#121218" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" fill="none" />
          <path d="M6 12a4 4 0 0 0 4 4h2a4 4 0 0 0 4-4V11.5" stroke="#121218" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" fill="none" />
        </g>
        <text x="14" y="5" class="tech-item">Git &amp; GitHub</text>
      </g>
    </g>
  </g>
</svg>'''

output_path = "assets/header.svg"
if not os.path.exists("assets"):
    os.makedirs("assets", exist_ok=True)

with open(output_path, "w", encoding="utf-8") as f:
    f.write(svg_content)

print(f"Successfully generated {output_path} as a single unified 12px rounded card!")
