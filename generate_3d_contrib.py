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

    color_palette = {
        0: { # Empty base tile
            "top": "#ECEEF0",
            "left": "#DDE1E6",
            "right": "#CCD1D9",
            "stroke": "#BFC5CE",
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
        3: { # Level 3 - Emerald Green
            "top": "#10B981",
            "left": "#0B9B6A",
            "right": "#067D55",
            "stroke": "#046644",
            "base_height": 34
        },
        4: { # Level 4 - Deep Forest
            "top": "#165E3E",
            "left": "#10472E",
            "right": "#0B3320",
            "stroke": "#082819",
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
      
      .canvas-bg {{ fill: #F7F7F8; }}
      .card-bg {{ fill: #ECEEF0; stroke: #E0E2E6; stroke-width: 1; rx: 16px; }}
      .font-sans {{ font-family: 'Instrument Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }}
      
      .header-title {{ font-family: 'Instrument Sans', sans-serif; font-size: 15px; font-weight: 700; fill: #121218; letter-spacing: -0.2px; }}
      .header-sub {{ font-family: 'Instrument Sans', sans-serif; font-size: 12px; font-weight: 400; fill: #61646B; }}
      
      .stat-big-lime {{ font-family: 'Instrument Sans', sans-serif; font-size: 34px; font-weight: 700; fill: #83CA16; letter-spacing: -0.5px; line-height: 1; }}
      .stat-big-green {{ font-family: 'Instrument Sans', sans-serif; font-size: 34px; font-weight: 700; fill: #165E3E; letter-spacing: -0.5px; line-height: 1; }}
      
      .stat-title {{ font-family: 'Instrument Sans', sans-serif; font-size: 13.5px; font-weight: 600; fill: #121218; letter-spacing: -0.1px; }}
      .stat-muted {{ font-family: 'Instrument Sans', sans-serif; font-size: 11.5px; font-weight: 400; fill: #61646B; }}
      .stat-label {{ font-family: 'Instrument Sans', sans-serif; font-size: 11px; font-weight: 600; fill: #555861; text-transform: uppercase; letter-spacing: 0.5px; }}

      .legend-text {{ font-family: 'Instrument Sans', sans-serif; font-size: 11px; font-weight: 500; fill: #61646B; }}

      .iso-active:hover {{
        filter: brightness(1.15) drop-shadow(0 4px 8px rgba(0,0,0,0.2));
        cursor: pointer;
      }}
    </style>

    <pattern id="isoBgHatch" width="12" height="12" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">
      <line x1="0" y1="0" x2="0" y2="12" stroke="#E5E7EB" stroke-width="0.8" opacity="0.6" />
    </pattern>

    <filter id="cardShadow" x="-2%" y="-2%" width="104%" height="106%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="4" stdDeviation="12" flood-color="#000000" flood-opacity="0.035" />
    </filter>
  </defs>

  <!-- Outer Card Frame -->
  <g filter="url(#cardShadow)">
    <rect x="15" y="15" width="930" height="430" class="card-bg" />
    <rect x="15" y="15" width="930" height="430" fill="url(#isoBgHatch)" rx="16" />
  </g>

  <!-- Header Section -->
  <g transform="translate(42, 45)">
    <text x="0" y="0" class="header-title">{total_contributions} contributions in the last year</text>
    <text x="0" y="18" class="header-sub">{range_str}</text>
    
    <!-- Top Right 3D Isometric Mode Badge -->
    <g transform="translate(748, -8)">
      <rect x="0" y="0" width="126" height="28" rx="7" fill="#121218" />
      <circle cx="15" cy="14" r="3.5" fill="#83CA16">
        <animate attributeName="opacity" values="1;0.35;1" dur="2.2s" repeatCount="indefinite" />
      </circle>
      <text x="26" y="18" font-family="'Instrument Sans', sans-serif" font-size="11" font-weight="600" fill="#FFFFFF">3D Isometric</text>
    </g>
  </g>

  <!-- ==================== TOP RIGHT STATS ==================== -->
  <!-- Metric 1: 1 Year Total -->
  <g transform="translate(580, 85)">
    <text x="0" y="0" class="stat-label">1 YEAR TOTAL</text>
    <text x="0" y="32" class="stat-big-green">{total_contributions}</text>
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
    <text x="0" y="32" class="stat-big-green">{longest_streak}</text>
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
    <rect x="-8" y="0" width="10" height="10" rx="2" fill="#ECEEF0" stroke="#CCD1D9" stroke-width="0.6" />
    <rect x="8" y="0" width="10" height="10" rx="2" fill="#D8F89D" stroke="#BEE674" stroke-width="0.6" />
    <rect x="24" y="0" width="10" height="10" rx="2" fill="#83CA16" stroke="#6EAD0E" stroke-width="0.6" />
    <rect x="40" y="0" width="10" height="10" rx="2" fill="#10B981" stroke="#0B9B6A" stroke-width="0.6" />
    <rect x="56" y="0" width="10" height="10" rx="2" fill="#165E3E" stroke="#10472E" stroke-width="0.6" />
    <text x="74" y="10" class="legend-text">More</text>
  </g>
</svg>'''

    output_path = "assets/isometric-contributions.svg"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg_content)

    print(f"Successfully generated {output_path} with smooth SVG animations and clean rendering!")

if __name__ == "__main__":
    generate_isometric_svg()
