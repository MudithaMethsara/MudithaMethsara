# Design Spec: Elite Cyberpunk GitHub Profile Enhancement

## 1. Overview
Transform the GitHub profile into a high-performance, visually stunning "Elite Architect" command center using a unified **Cyan-Blue and Red** theme.

## 2. Visual Architecture
- **Theme Palette**: 
  - Cyan: `#00E5FF` (Primary/Link)
  - Red: `#FF1744` (Accent/Status)
  - Background: `#0D1117` (Deep Space)
- **Typography**: Space/Orbitron style (via SVGs).

## 3. Core Modules

### 3.1. Header: The Command Center
- **Capsule Render**: Custom waving header with "MATHIYA" in Cyan and Red glitch text.
- **Dynamic Typing SVG**: Rapid-fire terminal initialization commands.
- **Neon Divider**: Animated line across the full width.

### 3.2. Status: Neural Uplink
- **Profile Badges**: "For-the-badge" style with custom Cyan/Red/Dark colors.
- **Mission Critical Status**: A 2-column layout.
  - Left: "Neural Link Established" - Bio with "Cyber-Traveller" vibe.
  - Right: "Trophy Case" - Detailed achievements trophy grid.

### 3.3. Arsenal: Technology Matrix
- **Skill Icons**: Categorized grid (Frontend, Backend, Database, Cloud, AI) with theme-consistent icons.
- **Toolbox**: Language-specific stats and frameworks.

### 3.4. Intelligence: Real-time Analytics
- **Dynamic Stats**:
  - Streak Status (Cyan/Red themed).
  - GitHub Stats Card (Tokyonight variant with custom color overrides).
  - Language Dominance Donut.
  - Contribution Activity Graph (Area fill with Red/Cyan).
- **3D Calendar**: Isometric 3D view of the contribution grid.

### 3.5. Protocols: Visual Activity
- **Snake/Pacman**: Animated contribution grids moving through the commit history.
- **Metrics SVG**: Comprehensive breakdown of coding habits and deep repository analysis.

### 3.6. Dynamic Streams
- **YouTube Transmissions**: Auto-updating list of latest videos.
- **Neural Logs (Blog)**: Auto-updating list of latest blog posts.
- **Recent Activity**: Live feed of commits and PRs.

### 3.7. Audio/Visual Sync
- **Spotify Integration**: "Now Playing" widget with real-time tracking and theme-matched colors.

## 4. Workflows & Automation
- **`main.yml`**: Central orchestrator.
- **`metrics-workflow.yml`**: Lowlighter metrics generation.
- **`snake-workflow.yml`**: Path-finding snake/pacman animation generation.
- **`activity-workflow.yml`**: Recent network activity updates.
- **`youtube/blog workflows`**: Dynamic feed updates.

## 5. Success Criteria
- [ ] Profile looks cohesive and high-tech.
- [ ] No broken images or failed workflow links.
- [ ] Every section follows the Cyan & Red "Elite" palette.
- [ ] Fully responsive on desktop and mobile GitHub view.
