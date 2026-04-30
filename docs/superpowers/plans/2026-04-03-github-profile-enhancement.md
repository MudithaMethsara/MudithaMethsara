# GitHub Profile Enhancement Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Transform the GitHub profile into a high-performance, visually stunning "Elite Architect" command center using a unified Cyan-Blue and Red theme.

**Architecture:** We will systematically update the README.md with new themed assets and reorganize the content into logical, high-impact modules. We'll also ensure all supporting workflows are optimized for this new aesthetic.

**Tech Stack:** Markdown, GitHub Actions, Shields.io, GitHub Readme Stats, Metrics, Capsule Render.

---

### Task 1: Update Header & Initial Terminal Setup

**Files:**
- Modify: `README.md`

- [ ] **Step 1: Update the main Capsule Render header**
Replace the top `<img ... />` with a new one that uses the Cyan-Red palette.

```markdown
<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=00E5FF,FF1744,000000&height=350&section=header&text=MATHIYA&fontSize=80&animation=fadeIn&fontAlignY=38&desc=🔥%20Elite%20Full-Stack%20Architect%20%7C%20Cyberpunk%20Dev%20%7C%20Innovation%20Engine%20🔥&descAlignY=65&descSize=22&fontColor=00E5FF&descColor=FF1744" />
</div>
```

- [ ] **Step 2: Update the Typing SVG with themed content**
Change colors and lines to match the "Elite Architect" vibe.

```markdown
<div align="center">
  
[![Typing SVG](https://readme-typing-svg.demolab.com?font=Orbitron&weight=800&size=38&duration=1500&pause=500&color=00E5FF&center=true&vCenter=true&multiline=true&width=1000&height=160&lines=System.init(User.MATHIYA)%3B;Loading+Elite+Developer+Profile...;%3E+Architecting+the+Future+of+Software;%3E+Mastering+AI+%2B+Web3+%2B+Cloud;%3E+Status:+ONLINE)] (https://git.io/typing-svg)

</div>
```

- [ ] **Step 3: Commit changes**
```bash
git add README.md
git commit -m "feat: update header and typing svg with cyan-red theme"
```

---

### Task 2: Re-theme Badges & Profile Status

**Files:**
- Modify: `README.md`

- [ ] **Step 1: Update Profile Badges with Cyan & Red theme**
Update `komarev` and `img.shields.io` badges.

```markdown
<div align="center">

![Profile Views](https://komarev.com/ghpvc/?username=Mathiyass&label=PROFILE+VIEWS&style=for-the-badge&color=00E5FF&labelColor=0D1117)
&nbsp;
![GitHub followers](https://img.shields.io/github/followers/Mathiyass?label=FOLLOWERS&style=for-the-badge&color=FF1744&labelColor=0D1117&logo=github)
&nbsp;
![GitHub stars](https://img.shields.io/github/stars/Mathiyass?label=TOTAL+STARS&style=for-the-badge&color=00E5FF&labelColor=0D1117&logo=github)
&nbsp;
![GitHub repos](https://img.shields.io/badge/dynamic/json?label=REPOS&style=for-the-badge&color=FF1744&labelColor=0D1117&logo=github&query=%24.public_repos&url=https://api.github.com/users/Mathiyass)

</div>
```

- [ ] **Step 2: Update Mission Critical Status content**
Refine the bio and trophy case theme.

- [ ] **Step 3: Commit changes**
```bash
git add README.md
git commit -m "feat: re-theme profile badges and status section"
```

---

### Task 3: Themed Technology Matrix

**Files:**
- Modify: `README.md`

- [ ] **Step 1: Update SkillIcons with themed colors**
Use the `theme=dark` and ensure the surrounding context matches.

- [ ] **Step 2: Update manually added technology badges**
Update `img.shields.io` badges for Keras, LangChain, etc., to use Cyan/Red colors.

```markdown
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=00E5FF)
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=FF1744)
```

- [ ] **Step 3: Commit changes**
```bash
git add README.md
git commit -m "feat: update technology matrix with themed badges"
```

---

### Task 4: System Analytics Overhaul

**Files:**
- Modify: `README.md`

- [ ] **Step 1: Update Streak Stats colors**
```markdown
<img src="https://streak-stats.demolab.com?user=Mathiyass&theme=tokyonight_duo&hide_border=true&background=0D1117&ring=FF1744&fire=00E5FF&currStreakLabel=00E5FF&sideLabels=FF1744" />
```

- [ ] **Step 2: Update GitHub Readme Stats colors**
```markdown
<img src="https://github-readme-stats.vercel.app/api?username=Mathiyass&show_icons=true&theme=tokyonight&hide_border=true&bg_color=0D1117&title_color=00E5FF&icon_color=FF1744&text_color=ffffff&rank_icon=github&include_all_commits=true&count_private=true" />
```

- [ ] **Step 3: Update Top Languages colors**
```markdown
<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=Mathiyass&layout=donut-vertical&theme=tokyonight&hide_border=true&bg_color=0D1117&title_color=00E5FF&text_color=ffffff&langs_count=10" />
```

- [ ] **Step 4: Commit changes**
```bash
git add README.md
git commit -m "feat: overhaul system analytics with themed stats"
```

---

### Task 5: Metrics Workflow Optimization

**Files:**
- Modify: `.github/workflows/metrics-workflow.yml`
- Modify: `README.md`

- [ ] **Step 1: Update metrics-workflow.yml for better colors**
Ensure the generated SVG will have Cyan/Red themes if the plugin supports it (Lowlighter metrics usually follow the base theme).

- [ ] **Step 2: Ensure 3D contribution graph is set to night-rainbow or similar high-contrast theme**

- [ ] **Step 3: Commit changes**
```bash
git add .github/workflows/metrics-workflow.yml README.md
git commit -m "chore: optimize metrics workflow for theme consistency"
```

---

### Task 6: Final Visual Polish & Footer

**Files:**
- Modify: `README.md`

- [ ] **Step 1: Update Spotify widget colors**
- [ ] **Step 2: Update Connect to the Grid section with unified badges**
- [ ] **Step 3: Update Footer with Capsule Render**

```markdown
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=00E5FF,FF1744,000000&height=150&section=footer&animation=fadeIn&fontColor=00E5FF" />
```

- [ ] **Step 4: Commit and Final Review**
```bash
git add README.md
git commit -m "feat: final visual polish and themed footer"
```
