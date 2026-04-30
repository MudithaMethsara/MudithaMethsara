# Cyan-Red Theme Technology Matrix Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Update technology badges in README.md to use Cyan (#00E5FF) and Red (#FF1744) logo colors, and verify SkillIcons are dark-themed.

**Architecture:** Surgical replacement of badge URLs in README.md to update `logoColor` parameters and background colors to match the theme.

**Tech Stack:** Markdown, Shields.io, SkillIcons.

---

### Task 1: Update AI, ML & Data badges

**Files:**
- Modify: `README.md`

- [ ] **Step 1: Update AI, ML & Data badges with alternating Cyan and Red logo colors**

Update the following badges:
- Keras: logoColor=00E5FF, background=121212
- scikit-learn: logoColor=FF1744, background=121212
- Hugging Face: logoColor=00E5FF, background=121212
- LangChain: logoColor=00E5FF, background=121212 (per example)
- OpenAI: logoColor=FF1744, background=121212 (per example)
- Pandas: logoColor=00E5FF, background=121212
- NumPy: logoColor=FF1744, background=121212
- Jupyter: logoColor=00E5FF, background=121212

Wait, the examples provided by the user used the ORIGINAL background colors.
LangChain: `1C3C3C`
OpenAI: `412991`

However, the profile badges at the top use `color=00E5FF&labelColor=0D1117`.
And "Themed Technology Matrix" implies a unified look.
Using a dark background like `121212` or `0D1117` for all would look more consistent.

But I should probably stick to what the user showed in examples if they were specific.
User said:
Example for LangChain:
```markdown
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=00E5FF)
```
Example for OpenAI:
```markdown
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=FF1744)
```

So I will keep the original background colors and only change `logoColor`.

- [ ] **Step 2: Apply changes to README.md**

```markdown
![Keras](https://img.shields.io/badge/Keras-%23D00000.svg?&style=for-the-badge&logo=Keras&logoColor=00E5FF)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=FF1744)
![Hugging Face](https://img.shields.io/badge/Hugging%20Face-FFD21E?style=for-the-badge&logo=huggingface&logoColor=00E5FF)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=00E5FF)
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=FF1744)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=00E5FF)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=FF1744)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=00E5FF)
```

### Task 2: Update Testing & Quality badges

**Files:**
- Modify: `README.md`

- [ ] **Step 1: Update Testing & Quality badges with alternating Red and Cyan logo colors**

Update the following badges:
- Jest: logoColor=FF1744
- Cypress: logoColor=00E5FF
- Selenium: logoColor=FF1744
- Mocha: logoColor=00E5FF
- ESLint: logoColor=FF1744
- Prettier: logoColor=00E5FF
- SonarQube: logoColor=FF1744

- [ ] **Step 2: Apply changes to README.md**

```markdown
![Jest](https://img.shields.io/badge/Jest-C21325?style=for-the-badge&logo=jest&logoColor=FF1744)
![Cypress](https://img.shields.io/badge/Cypress-17202C?style=for-the-badge&logo=cypress&logoColor=00E5FF)
![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=FF1744)
![Mocha](https://img.shields.io/badge/Mocha-8D6748?style=for-the-badge&logo=mocha&logoColor=00E5FF)
![ESLint](https://img.shields.io/badge/ESLint-4B32C3?style=for-the-badge&logo=eslint&logoColor=FF1744)
![Prettier](https://img.shields.io/badge/Prettier-F7B93E?style=for-the-badge&logo=prettier&logoColor=00E5FF)
![SonarQube](https://img.shields.io/badge/SonarQube-4E9BCD?style=for-the-badge&logo=sonarqube&logoColor=FF1744)
```

### Task 3: Verify SkillIcons and Commit

**Files:**
- Modify: `README.md`

- [ ] **Step 1: Verify all SkillIcons links have `theme=dark`**

They currently do, but I will double check and fix if any are missing.

- [ ] **Step 2: Commit changes**

Run:
```bash
git add README.md
git commit -m "feat: update technology matrix with themed badges"
```
