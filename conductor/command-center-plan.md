# Crimson Stealth Command Center Implementation Plan (TDD Mode)

> **For agentic workers:** REQUIRED SUB-SKILL: Use react-native-hifi:subagent-driven-development (recommended) or react-native-hifi:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.
> **TDD NOTE:** This plan follows Test-Driven Development. Every logic change starts with a failing test.

**Goal:** Transform the GitHub profile and local portfolio into a unified, high-performance "Elite Architect" command center with a Crimson Red and Black theme.

**Architecture:** Systematic overhaul of CSS and Markdown, synchronized through a shared "Stealth Architect" aesthetic, verified by unit tests for JS logic and manual checks for UI.

**Tech Stack:** HTML/CSS/JS, Jest (for testing), Markdown, GitHub Actions, Shields.io, Capsule Render.

---

### Task 0: Test Environment Setup

**Files:**
- Create: `package.json`
- Create: `tests/terminal.test.js`

- [ ] **Step 1: Initialize npm and install Jest**
```bash
npm init -y && npm install --save-dev jest
```

- [ ] **Step 2: Add test script to package.json**
```json
"scripts": { "test": "jest" }
```

- [ ] **Step 3: Create initial failing test for script.js**
We want to verify that the terminal sequence contains the correct new strings.

```javascript
// tests/terminal.test.js
const { terminalLines } = require('../script.js');
test('terminal lines match the new Elite Architect branding', () => {
  expect(terminalLines).toContain("System.init(User.REDWOLF);");
  expect(terminalLines).toContain("Loading Elite Architect Profile...");
});
```

---

### Task 1: Identity & Handles Sync (TDD)

**Files:**
- Modify: `script.js`
- Modify: `index.html`
- Modify: `README.md`

- [ ] **Step 1: Run the failing test**
Run: `npm test`
Expected: FAIL (script.js doesn't export terminalLines or has old strings).

- [ ] **Step 2: Update script.js to export and use new strings**
Export `terminalLines` for testing and update content.

```javascript
// script.js
const terminalLines = [
  "System.init(User.REDWOLF);",
  "Loading Elite Architect Profile...",
  "> Deploying Infrastructure...",
  "> Status: <span class='status-online'>ONLINE</span>"
];
if (typeof module !== 'undefined') module.exports = { terminalLines };
```

- [ ] **Step 3: Run the test again**
Run: `npm test`
Expected: PASS.

- [ ] **Step 4: Update README & index.html identity**
Update text to "Muditha Methsara | RedWolf" and sync X handle to `M_Methsara_RW`.

- [ ] **Step 5: Commit changes**
```bash
git add package.json script.js index.html README.md
git commit -m "feat: sync identity and handles with TDD verification"
```

---

### Task 2: Portfolio CSS Transformation (Dark Stealth)

**Files:**
- Modify: `style.css`

- [ ] **Step 1: Update CSS Variables to Crimson/Black**
```css
:root {
  --primary-red: #DC143C; /* Deep Crimson */
  --bg-color: #0D1117;    /* Matte Black */
  --card-bg: rgba(20, 20, 20, 0.9);
  --text-main: #E6E6E6;
  --text-muted: #8B8B8B;
}
```

- [ ] **Step 2: Visual Verification**
Check `index.html` for dark mode compliance.

- [ ] **Step 3: Commit CSS Overhaul**
```bash
git add style.css
git commit -m "feat: implement Crimson Stealth dark theme for portfolio"
```

---

### Task 3: Workflow Uplink Fixes

**Files:**
- Modify: `.github/workflows/youtube-workflow.yml`
- Modify: `.github/workflows/blog-post-workflow.yml`

- [ ] **Step 1: Update YouTube Channel ID**
Set to `UCRa-MY1B5RiaUF0hhGrDKFg`.

- [ ] **Step 2: Comment out failing blog feeds**
Stabilize the pipeline.

- [ ] **Step 3: Commit Workflow Fixes**
```bash
git add .github/workflows/
git commit -m "fix(ci): update youtube id and stabilize blog feeds"
```

---

### Task 4: README Visual Overhaul (Arsenal Matrix)

**Files:**
- Modify: `README.md`

- [ ] **Step 1: Re-theme Stats & Badges**
Update all `shields.io` and `skillicons.dev` URLs to use Dark/Crimson parameters.

- [ ] **Step 2: Final Verification & Cleanup**
```bash
npm test && git commit -m "chore: final visual polish and cleanup"
```
