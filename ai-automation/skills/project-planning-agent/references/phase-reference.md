# Phase Reference — Quick Cheat Sheet

Complete reference for all 8 phases, their inputs, outputs, and gate criteria.
Load this file when you need a fast lookup during an active planning session.

---

## Phase 0: Intake Mode

**Goal:** Identify the project in the simplest possible form.

**Intake questions:**
1. Project Name
2. One-sentence idea
3. Project type (rough guess)
4. Target user
5. Problem solved
6. Simplest first version (MVP)
7. Primary use: business / content / automation / data / AI / internal

**Summary template:**
> This project is a [project type] for [target user] that solves [problem] by [solution].
> The simplest first version is: [MVP summary].

**Gate:** User approves summary → advance to Phase 1.

---

## Phase 1: Project Classification

**Goal:** Confirm and document the project type with a scored rationale.

**Output:** `docs/00-project-summary.md`

**Project types to score:**
Website · Web App · Mobile App · API · Database · Automation · AI Tool · SaaS ·
Marketplace · Content Platform · Data Dashboard · Internal Tool · eBook / Media ·
Community Platform · Affiliate / Review Site · Other

**Scorecard format:**

| Type | Fit (1–5) | Reason |
|------|----------:|--------|

**Gate:** User approves classification → advance to Phase 2.

---

## Phase 2: Research Branch

**Goal:** Research the opportunity before planning any features.

**Output folder:** `docs/research/`

**Files (in order):**

| # | File | Core question |
|---|------|--------------|
| 1 | `market-research.md` | Is there a real market? |
| 2 | `competitor-research.md` | Who already exists, and where are the gaps? |
| 3 | `user-research.md` | Who exactly is the user, and what do they need? |
| 4 | `problem-research.md` | Is the problem real, urgent, and frequent? |
| 5 | `keyword-research.md` | Is there search demand? What do people look for? |
| 6 | `monetization-research.md` | How does this make money, and is that realistic? |
| 7 | `content-research.md` | What content is needed to attract and retain users? |
| 8 | `technical-research.md` | Is this technically feasible at MVP scale? |
| 9 | `opportunity-summary.md` | **Proceed / Refine / Pause** |

**Gate:** All 9 files complete + user approves opportunity summary → advance to Phase 3.

---

## Phase 3: Planning Branch

**Goal:** Convert research into a buildable plan.

**Output folder:** `docs/planning/`

**Files (in order):**

| # | File | Purpose |
|---|------|---------|
| 1 | `project-brief.md` | One-page project overview |
| 2 | `project-proposal.md` | Expanded proposal for stakeholders |
| 3 | `prd.md` | Full product requirements document |
| 4 | `mvp-scope.md` | Explicit in/out boundary for MVP |
| 5 | `feature-list.md` | Prioritized feature table (Must/Should/Nice) |
| 6 | `user-stories.md` | As a / I want / So I can format |
| 7 | `user-flows.md` | Key user journeys step by step |
| 8 | `roadmap.md` | Phase 1 → 2 → 3 timeline |
| 9 | `risk-checklist.md` | Known risks and mitigations |
| 10 | `success-metrics.md` | MVP, 30-day, and 90-day targets |

**Gate:** User approves MVP scope → advance to Phase 4.

---

## Phase 4: Organization Branch

**Goal:** Organize the project structure before any files or folders are created.

**Output folder:** `docs/organization/`

**Files:**

| # | File | Purpose |
|---|------|---------|
| 1 | `file-structure-plan.md` | Proposed folder/file layout |
| 2 | `tool-stack-options.md` | Stack options with tradeoffs |
| 3 | `selected-stack.md` | Final approved stack decision |
| 4 | `task-breakdown.md` | Work items by category |
| 5 | `milestone-plan.md` | Milestones mapped to roadmap |
| 6 | `roles-and-agents.md` | Who/what handles each area |
| 7 | `dependency-map.md` | What depends on what |
| 8 | `build-order.md` | Ordered sequence of what to build |
| 9 | `decision-log.md` | All major decisions and rationale |

**Gate:** User approves organization plan → advance to Phase 5.

---

## Phase 5: Tool Stack Decision

**Goal:** Select the technology stack only after the project is fully understood.

**Output:** `docs/organization/selected-stack.md` (extends Phase 4 file 3)

**Default options by layer:**

| Layer | Options |
|-------|---------|
| Frontend | React + Vite · Next.js · Vue · SvelteKit · Static HTML/CSS |
| Backend | FastAPI · Django · Node.js/Express · NestJS · Laravel |
| Database | PostgreSQL · MySQL · SQLite · MongoDB · Supabase · Firebase |
| Hosting | Vercel · Hostinger · Render · Railway · Fly.io |
| Automation | GitHub Actions · n8n · Zapier · Make · Cron jobs |
| Analytics | PostHog · Google Analytics · Plausible · Mixpanel |
| Design | Figma · Canva · Miro |
| Docs | Markdown · Obsidian · VitePress · Notion |

**Gate:** User approves stack → advance to Phase 6.

---

## Phase 6: Validation Gate

**Goal:** Confirm all planning is complete and the project is ready to build.

**Output folder:** `docs/gates/`

**Checklists:**

| # | File | Focus |
|---|------|-------|
| 1 | `research-complete-checklist.md` | All research done and reviewed |
| 2 | `mvp-approval-checklist.md` | MVP scope is clear and approved |
| 3 | `stack-approval-checklist.md` | Stack is selected and justified |
| 4 | `build-readiness-checklist.md` | Full readiness across all categories |
| 5 | `handoff-checklist.md` | Handoff document is ready |

**Gate:** All checklist items checked with no blockers → advance to Phase 7.

---

## Phase 7: Build Agent Handoff

**Goal:** Hand off approved, complete plan to coding agents.

**Output:** `docs/handoff/build-agent-handoff.md`

**Handoff document includes:**
- Approved project summary
- MVP scope (in/out lists)
- Selected stack
- Approved file structure
- Build order
- Must-build-first list
- Do-not-build-yet list
- Known risks
- Final instruction to the build agent

**Final rule:** The build agent must not expand beyond the approved MVP without explicit
user approval. Any new feature requests go back to the planning agent.
