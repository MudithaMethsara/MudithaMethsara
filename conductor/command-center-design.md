# Design Spec: Elite Architect Command Center (Crimson Stealth)

**Date:** 2026-05-28
**Topic:** GitHub Profile & Portfolio Synchronization
**Goal:** Transform the GitHub profile and local portfolio into a unified, high-performance "Elite Architect" command center using a "Stealth Architect" (Matte Black & Deep Crimson) aesthetic.

## 1. Architecture & Unified Theming
- **Primary Identity:** "Muditha Methsara | RedWolf" will be used consistently across all headers and mission statements.
- **Color Palette:** 
  - Backgrounds: Matte Black/Charcoal (`#0D1117`, `#111111`)
  - Text: Off-white/Light Grey (`#E6E6E6`, `#CCCCCC`) for readability.
  - Accents/Borders: Deep Crimson (`#DC143C`, `#B22222`).
- **Typography:** `Orbitron` for headers (sci-fi/tech edge), `Inter` for body text (clean readability).
- **Social Links (Source of Truth):** Use links defined in the current `index.html` (e.g., X: `M_Methsara_RW`, Discord: `redwollff`).

## 2. Global CSS Overhaul (`style.css`)
- Migrate from light mode to a full dark mode theme.
- Replace bright red/pink gradients with dark, muted crimson gradients.
- Update card backgrounds (`--card-bg`) to dark translucent overlays (e.g., `rgba(20, 20, 20, 0.85)`).
- Implement solid crimson borders and muted crimson glow effects for hover states and emphasis.

## 3. Command Center Header & Terminal
- **Capsule Render Banner:** Update both `README.md` and `index.html` to use a Black-to-Crimson gradient. Text: `MUDITHAMETHSARA | REDWOLF`.
- **Terminal Sequence (Typing SVG & JS):**
  - Text updates: `System.init(User.REDWOLF);`, `Loading Elite Architect Profile...`, `> Deploying Infrastructure...`, `> Status: ONLINE`.
  - Color updates: Terminal text in light grey, `ONLINE` status in Deep Crimson.

## 4. The Arsenal Matrix (Tech Stack)
- **Skill Icons:** Append `&theme=dark` to all `skillicons.dev` URLs.
- **Custom Badges (Shields.io):** Standardize all custom badges (e.g., AI/ML tools, testing frameworks) to use a Matte Black background (`labelColor=0D1117`) and Deep Crimson accent (`color=DC143C`).

## 5. System Analytics & Metrics
- Update the themes for GitHub Readme Stats, Streak Stats, and Top Languages to match the dark/crimson aesthetic. Custom parameters will be used to enforce `#0D1117` backgrounds and `#DC143C` highlights.

## 6. Data Uplinks (Workflows)
- **YouTube:** Update `.github/workflows/youtube-workflow.yml` with the verified Channel ID: `UCRa-MY1B5RiaUF0hhGrDKFg`.
- **Blogs:** The Medium and Dev.to RSS feeds are currently returning 404s/errors. The workflow step pulling these feeds will be commented out to stabilize the CI/CD pipeline until valid RSS URLs are provided.

## 7. Migration & Rollback Strategy
- All changes are contained within the markdown, HTML, CSS, and workflow files. If the new theme is unsatisfactory, reverting the git commit will instantly restore the previous cyan/red and light-mode states.
