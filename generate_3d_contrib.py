import json
import os
import urllib.request
from datetime import datetime

def generate_isometric_svg():
    # 1. Fetch contribution calendar data
    url = "https://github-contributions-api.jogruber.de/v4/MudithaMethsara?y=last"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Python)"})
    
    try:
        with urllib.request.urlopen(req, timeout=8) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            contribs = data.get("contributions", [])
            total_contributions = data.get("total", {}).get("lastYear", sum(c.get("count", 0) for c in contribs))
    except Exception as e:
        print("API fallback:", e)
        contribs = [{"date": f"2026-{m:02d}-{d:02d}", "count": 0, "level": 0} for m in range(1, 13) for d in range(1, 29)]
        total_contributions = 66

    if not contribs:
        contribs = [{"date": "2026-01-01", "count": 0, "level": 0} for _ in range(365)]

    # 2. Compute statistics
    busiest_item = max(contribs, key=lambda x: x.get("count", 0)) if contribs else {"count": 0, "date": "2026-05-28"}
    busiest_count = busiest_item.get("count", 0)
    busiest_date_str = busiest_item.get("date", "")
    try:
        b_dt = datetime.strptime(busiest_date_str, "%Y-%m-%d")
        busiest_formatted = b_dt.strftime("%b %d")
    except Exception:
        busiest_formatted = busiest_date_str

    try:
        start_dt = datetime.strptime(contribs[0]["date"], "%Y-%m-%d").strftime("%b %d, %Y")
        end_dt = datetime.strptime(contribs[-1]["date"], "%Y-%m-%d").strftime("%b %d, %Y")
        range_str = f"{start_dt} – {end_dt}"
    except Exception:
        range_str = "Last 12 Months"

    # Streaks
    longest_streak = 0
    curr_streak = 0
    temp_streak = 0
    for c in contribs:
        if c.get("count", 0) > 0:
            temp_streak += 1
            if temp_streak > longest_streak:
                longest_streak = temp_streak
        else:
            temp_streak = 0

    for c in reversed(contribs):
        if c.get("count", 0) > 0:
            curr_streak += 1
        else:
            break

    # 3. Organize by weeks
    try:
        first_day_obj = datetime.strptime(contribs[0]["date"], "%Y-%m-%d")
        start_day_of_week = (first_day_obj.weekday() + 1) % 7  # 0=Sun, 6=Sat
    except Exception:
        start_day_of_week = 0

    grid = []
    current_week = []
    
    for _ in range(start_day_of_week):
        current_week.append(None)

    for item in contribs:
        current_week.append(item)
        if len(current_week) == 7:
            grid.append(current_week)
            current_week = []
    if current_week:
        while len(current_week) < 7:
            current_week.append(None)
        grid.append(current_week)

    # 4. Isometric Geometry Setup
    origin_x = 185
    origin_y = 150
    dx_w = 12.8
    dy_w = 3.6
    dx_d = -7.5
    dy_d = 4.2
    
    tile_w = 7.2
    tile_d = 4.0

    # Custom Palette on #2596be Ocean Cyan Background
    color_palette = {
        0: { # Base floor tile on #2596be
            "top": "#1F82A6",
            "left": "#1A6F8E",
            "right": "#145973",
            "stroke": "#2CA8D4",
            "base_height": 2.5
        },
        1: { # Level 1 - Light Lime Accent
            "top": "#D8F89D",
            "left": "#BEE674",
            "right": "#A6D657",
            "stroke": "#94C745",
            "base_height": 12
        },
        2: { # Level 2 - Brand Primary Lime
            "top": "#83CA16",
            "left": "#6EAD0E",
            "right": "#5C9308",
            "stroke": "#4C7D04",
            "base_height": 22
        },
        3: { # Level 3 - Bright Mint Emerald
            "top": "#34D399",
            "left": "#10B981",
            "right": "#059669",
            "stroke": "#047857",
            "base_height": 34
        },
        4: { # Level 4 - Crisp White / Mint Highlight
            "top": "#FFFFFF",
            "left": "#E0F2FE",
            "right": "#BAE6FD",
            "stroke": "#7DD3FC",
            "base_height": 46
        }
    }

    blocks_to_render = []

    for w, week_days in enumerate(grid):
        for d, day in enumerate(week_days):
            if day is None:
                continue

            count = day.get("count", 0)
            level = day.get("level", 0)
            if count > 0 and level == 0:
                level = 1
            if count >= 15:
                level = 4
            elif count >= 8:
                level = 3
            elif count >= 3:
                level = 2
            elif count >= 1:
                level = 1

            style = color_palette[level]
            if level == 0:
                h = style["base_height"]
            else:
                h = style["base_height"] + min(22, count * 1.6)

            bx = origin_x + (w * dx_w) + (d * dx_d)
            by = origin_y + (w * dy_w) + (d * dy_d)

            depth = by + (d * 2.0)

            blocks_to_render.append({
                "bx": bx,
                "by": by,
                "h": h,
                "level": level,
                "style": style,
                "count": count,
                "date": day["date"],
                "depth": depth
            })

    # Sort blocks by depth (back to front)
    blocks_to_render.sort(key=lambda b: b["depth"])

    cubes_svg = []
    for b in blocks_to_render:
        bx = b["bx"]
        by = b["by"]
        h = b["h"]
        style = b["style"]
        level = b["level"]

        vx0, vy0 = bx, by
        vx1, vy1 = bx + tile_w, by - tile_d
        vx2, vy2 = bx, by - (2 * tile_d)
        vx3, vy3 = bx - tile_w, by - tile_d

        # Elevated top vertices
        tx0, ty0 = vx0, vy0 - h
        tx1, ty1 = vx1, vy1 - h
        tx2, ty2 = vx2, vy2 - h
        tx3, ty3 = vx3, vy3 - h

        if level > 0:
            anim_class = "iso-active"
            anim_tag = f'''
        <animateTransform attributeName="transform" type="translate" values="0,0; 0,-3; 0,0" dur="{3.0 + (level * 0.4):.1f}s" repeatCount="indefinite" />'''
        else:
            anim_class = "iso-tile"
            anim_tag = ""

        cube_path = f'''    <g class="{anim_class}" data-date="{b['date']}" data-count="{b['count']}">{anim_tag}
      <!-- Left Facet -->
      <polygon points="{vx3:.2f},{vy3:.2f} {vx0:.2f},{vy0:.2f} {tx0:.2f},{ty0:.2f} {tx3:.2f},{ty3:.2f}" fill="{style['left']}" stroke="{style['stroke']}" stroke-width="0.35" />
      <!-- Right Facet -->
      <polygon points="{vx0:.2f},{vy0:.2f} {vx1:.2f},{vy1:.2f} {tx1:.2f},{ty1:.2f} {tx0:.2f},{ty0:.2f}" fill="{style['right']}" stroke="{style['stroke']}" stroke-width="0.35" />
      <!-- Top Diamond Facet -->
      <polygon points="{tx0:.2f},{ty0:.2f} {tx1:.2f},{ty1:.2f} {tx2:.2f},{ty2:.2f} {tx3:.2f},{ty3:.2f}" fill="{style['top']}" stroke="{style['stroke']}" stroke-width="0.35" />
    </g>'''
        cubes_svg.append(cube_path)

    cubes_str = "\n".join(cubes_svg)

    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 460" width="100%" height="100%">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@400;500;600;700&amp;display=swap');
      
      .canvas-bg {{ fill: #2596be; }}
      .card-bg {{ fill: #2596be; stroke: rgba(255, 255, 255, 0.25); stroke-width: 1; rx: 16px; }}
      .font-sans {{ font-family: 'Instrument Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }}
      
      .header-title {{ font-family: 'Instrument Sans', sans-serif; font-size: 15px; font-weight: 700; fill: #FFFFFF; letter-spacing: -0.2px; }}
      .header-sub {{ font-family: 'Instrument Sans', sans-serif; font-size: 12px; font-weight: 500; fill: #E0F2FE; }}
      
      .stat-big-lime {{ font-family: 'Instrument Sans', sans-serif; font-size: 34px; font-weight: 700; fill: #D8F89D; letter-spacing: -0.5px; line-height: 1; }}
      .stat-big-white {{ font-family: 'Instrument Sans', sans-serif; font-size: 34px; font-weight: 700; fill: #FFFFFF; letter-spacing: -0.5px; line-height: 1; }}
      
      .stat-title {{ font-family: 'Instrument Sans', sans-serif; font-size: 13.5px; font-weight: 600; fill: #FFFFFF; letter-spacing: -0.1px; }}
      .stat-muted {{ font-family: 'Instrument Sans', sans-serif; font-size: 11.5px; font-weight: 400; fill: #E0F2FE; }}
      .stat-label {{ font-family: 'Instrument Sans', sans-serif; font-size: 11px; font-weight: 600; fill: #E0F2FE; text-transform: uppercase; letter-spacing: 0.5px; opacity: 0.9; }}

      .legend-text {{ font-family: 'Instrument Sans', sans-serif; font-size: 11px; font-weight: 500; fill: #E0F2FE; }}

      .iso-active {{
        filter: drop-shadow(0 2px 6px rgba(0, 0, 0, 0.25));
      }}

      .iso-active:hover {{
        filter: brightness(1.25) drop-shadow(0 0 10px rgba(255, 255, 255, 0.6));
        cursor: pointer;
      }}
    </style>

    <pattern id="isoBgHatchBlue" width="12" height="12" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">
      <line x1="0" y1="0" x2="0" y2="12" stroke="#31A8D4" stroke-width="0.8" opacity="0.4" />
    </pattern>

    <filter id="cardShadowBlue" x="-2%" y="-2%" width="104%" height="106%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="8" stdDeviation="16" flood-color="#145973" flood-opacity="0.35" />
    </filter>
  </defs>

  <!-- Base Outer Background (#2596be) -->
  <rect width="960" height="460" fill="#2596be" rx="16" />

  <!-- Outer Card Frame (#2596be with subtle pattern) -->
  <g filter="url(#cardShadowBlue)">
    <rect x="15" y="15" width="930" height="430" class="card-bg" />
    <rect x="15" y="15" width="930" height="430" fill="url(#isoBgHatchBlue)" rx="16" />
  </g>

  <!-- Header Section -->
  <g transform="translate(42, 45)">
    <text x="0" y="0" class="header-title">{total_contributions} contributions in the last year</text>
    <text x="0" y="18" class="header-sub">{range_str}</text>
    
    <!-- Top Right 3D Isometric Mode Badge -->
    <g transform="translate(748, -8)">
      <rect x="0" y="0" width="126" height="28" rx="7" fill="rgba(19, 78, 99, 0.5)" stroke="rgba(255, 255, 255, 0.3)" stroke-width="1" />
      <circle cx="15" cy="14" r="3.5" fill="#D8F89D">
        <animate attributeName="opacity" values="1;0.35;1" dur="2.2s" repeatCount="indefinite" />
      </circle>
      <text x="26" y="18" font-family="'Instrument Sans', sans-serif" font-size="11" font-weight="600" fill="#FFFFFF">3D Isometric</text>
    </g>
  </g>

  <!-- ==================== TOP RIGHT STATS ==================== -->
  <!-- Metric 1: 1 Year Total -->
  <g transform="translate(580, 85)">
    <text x="0" y="0" class="stat-label">1 YEAR TOTAL</text>
    <text x="0" y="32" class="stat-big-white">{total_contributions}</text>
    <text x="65" y="22" class="stat-title">contributions</text>
    <text x="65" y="36" class="stat-muted">{range_str}</text>
  </g>

  <!-- Metric 2: Busiest Day -->
  <g transform="translate(580, 155)">
    <text x="0" y="0" class="stat-label">BUSIEST DAY</text>
    <text x="0" y="32" class="stat-big-lime">{busiest_count}</text>
    <text x="50" y="22" class="stat-title">contributions</text>
    <text x="50" y="36" class="stat-muted">{busiest_formatted}</text>
  </g>

  <!-- ==================== BOTTOM LEFT STATS ==================== -->
  <!-- Longest Streak -->
  <g transform="translate(42, 335)">
    <text x="0" y="0" class="stat-label">LONGEST STREAK</text>
    <text x="0" y="32" class="stat-big-white">{longest_streak}</text>
    <text x="32" y="22" class="stat-title">days</text>
    <text x="32" y="36" class="stat-muted">Peak consistency</text>
  </g>

  <!-- Current Streak -->
  <g transform="translate(42, 395)">
    <text x="0" y="0" class="stat-label">CURRENT STREAK</text>
    <text x="0" y="28" class="stat-big-lime">{curr_streak}</text>
    <text x="30" y="18" class="stat-title">days</text>
    <text x="30" y="32" class="stat-muted">Active streak</text>
  </g>

  <!-- ==================== 3D ISOMETRIC CALENDAR ==================== -->
  <g id="isometric-blocks">
{cubes_str}
  </g>

  <!-- Legend (Bottom Right) -->
  <g transform="translate(725, 415)">
    <text x="-40" y="10" class="legend-text">Less</text>
    <rect x="-8" y="0" width="10" height="10" rx="2" fill="#1F82A6" stroke="#2CA8D4" stroke-width="0.6" />
    <rect x="8" y="0" width="10" height="10" rx="2" fill="#D8F89D" stroke="#BEE674" stroke-width="0.6" />
    <rect x="24" y="0" width="10" height="10" rx="2" fill="#83CA16" stroke="#6EAD0E" stroke-width="0.6" />
    <rect x="40" y="0" width="10" height="10" rx="2" fill="#34D399" stroke="#10B981" stroke-width="0.6" />
    <rect x="56" y="0" width="10" height="10" rx="2" fill="#FFFFFF" stroke="#BAE6FD" stroke-width="0.6" />
    <text x="74" y="10" class="legend-text">More</text>
  </g>
</svg>'''

    output_path = "assets/isometric-contributions.svg"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg_content)

    print(f"Successfully generated {output_path} with #2596be background!")

if __name__ == "__main__":
    generate_isometric_svg()
