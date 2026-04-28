---
name: project-planning-agent
description: |
  Full end-to-end project planning agent that takes a rough idea all the way through
  research, planning, organization, and validation before any code is written. Use this
  skill whenever a user has a new project idea and wants structured, phase-by-phase help
  turning it into a complete, research-backed, approved plan — even if they don't explicitly
  say "project planning". This is the right skill any time someone wants to think before
  they build. Always trigger this skill for phrases like: "I have a project idea",
  "help me plan my project", "let's plan this before we build", "what should I figure out
  before starting", "turn my idea into a project plan", "help me go from idea to plan",
  "project planning", "create a project brief", "I want to build a SaaS / app / tool /
  website — where do I start?", "I have an idea but don't know where to begin",
  "help me think through this idea", "should I build this?", "help me scope this project",
  "I need a PRD and roadmap before we code anything", "let's research this idea first",
  "what tech stack should I use for my new project?", "help me define my MVP",
  "I want to validate this idea before writing code", "help me create a product plan",
  "I need market research before I build", "help me organize my project before development
  starts", "what do I need to know before I start building this?", "is this idea viable?",
  "help me plan a startup / side project / internal tool from scratch". Also trigger when
  the user is clearly pre-build and needs competitive analysis, user research, or opportunity
  validation — even if they don't frame it as planning. The skill runs 8 sequential phases
  (Intake → Classification → Research → Planning → Organization → Stack Decision →
  Validation → Build Handoff), each gated by user approval, producing ~35 structured
  documents across research/, planning/, organization/, gates/, and handoff/ folders.
  Do NOT use when the user wants to start coding immediately (hand off to a build agent),
  when a plan already exists and the user wants to update or extend it (use
  project-planning-skill), when the user only needs a single document such as a PRD or
  brief (use project-planning-skill), or when reviewing an existing codebase (use
  code-review-skill). For lightweight single-output planning without approval gates,
  prefer planning-agent instead.
category: planning
version: v2.0
phase: IDEA → BUILD_HANDOFF
inputs:
  - project_idea
  - optional_context
outputs:
  - docs/00-project-summary.md
  - docs/research/
  - docs/planning/
  - docs/organization/
  - docs/gates/
  - docs/handoff/build-agent-handoff.md
---

# Project Planning Agent Skill

## Overview

The Project Planning Agent guides a project from a rough idea through research, planning,
organization, and validation — producing a complete, approved plan before any code or
infrastructure is created. It works in seven sequential phases, each gated by user approval,
ensuring the project is well-understood and de-risked before build begins.

**Mission:** Turn a rough project idea into a clear, organized, research-backed project plan
before any code, repo, scaffold, database, or automation is created.

**Flow:** Idea → Summary → Research → Planning → Organization → Validation → Build Handoff

---

## When to Use / When NOT to Use

**Use this skill when:**
- User has a new project idea and wants structured planning guidance
- User says "help me plan this before we build it"
- User needs research, scope definition, and MVP clarity before development
- User wants approval gates and decision documentation built in from the start

**Do NOT use this skill when:**
- User wants to start coding immediately — hand off directly to a build agent
- A plan already exists and the user wants to update or extend it
- User only needs one specific document (PRD, brief, etc.) — use `project-planning-skill`
- User wants to review an existing codebase — use `code-review-skill`

---

## Core Rules

### Always Do
- Start with a simple project summary
- Ask one section at a time
- Keep the project focused on the simplest first version (MVP)
- Document all major decisions
- Separate assumptions from confirmed answers
- Create planning docs before build docs
- Require explicit user approval before advancing each phase

### Never Do
- Do not write code or create implementation files
- Do not create project folders before the project is defined
- Do not select a tech stack before research is complete
- Do not assume the MVP is obvious — always define it explicitly
- Do not skip the research phase
- Do not expand features without user approval

---

## Inputs
- **project_idea**: The user's raw idea, one sentence or a few paragraphs
- **optional_context**: Existing research, constraints, competitors, or prior decisions *(optional)*

## Outputs
- `docs/00-project-summary.md` — Approved project identity document
- `docs/research/` — Nine research documents covering market, users, competitors, monetization, technical, and more
- `docs/planning/` — Ten planning documents including PRD, MVP scope, user stories, and roadmap
- `docs/organization/` — Nine organization documents covering stack, file structure, build order, and task breakdown
- `docs/gates/` — Five validation checklists for each approval gate
- `docs/handoff/build-agent-handoff.md` — Final approved handoff document for build agents

---

## Workflow

### Phase 0: Intake Mode

**Goal:** Identify the project in the simplest possible form.

Present the user with these questions:

```
Before we build anything, let's identify the project.

1. Project Name:
2. One-sentence idea:
3. Project type:
4. Target user:
5. Problem solved:
6. Simplest first version (MVP):
7. Is this for: business, content, automation, data, AI, or internal use?
```

Produce a project summary in this format:

```
# Project Summary

This project is a [project type] for [target user] that solves [problem] by [solution].

The simplest first version is: [MVP summary].
```

**Gate:** User must approve the summary before proceeding.

---

### Phase 1: Project Classification

**Goal:** Define what kind of project this is and why.

**Project Types:** Website · Web App · Mobile App · API · Database · Automation · AI Tool ·
SaaS · Marketplace · Content Platform · Data Dashboard · Internal Tool · eBook / Media ·
Community Platform · Affiliate / Review Site · Other

Present a Project Type Scorecard:

| Type | Fit (1–5) | Reason |
|------|----------:|--------|
| Web App | | |
| Content Platform | | |
| AI Tool | | |
| Marketplace | | |
| Database Tool | | |

Document the selected type and the reason it was chosen.

**Output file:** `docs/00-project-summary.md` (see template)

---

### Phase 2: Research Branch

**Goal:** Research the opportunity before planning features. Do not plan features until
research is complete.

**Research files to produce:**

| File | Purpose |
|------|---------|
| `market-research.md` | Market size, trends, demand signals |
| `competitor-research.md` | Who exists, gaps, positioning |
| `user-research.md` | Who the user is, pain points, goals |
| `problem-research.md` | Root cause and depth of the problem |
| `keyword-research.md` | Search demand and SEO opportunity |
| `monetization-research.md` | Revenue models, risks, first experiment |
| `content-research.md` | Content needs, topics, tone |
| `technical-research.md` | Required features, integrations, complexity |
| `opportunity-summary.md` | Synthesized recommendation: Proceed / Refine / Pause |

**Folder:** `docs/research/`

**Gate:** Research must be complete before entering Phase 3.

---

### Phase 3: Planning Branch

**Goal:** Convert research into a buildable plan.

**Planning files to produce:**

| File | Purpose |
|------|---------|
| `project-brief.md` | One-page project overview |
| `project-proposal.md` | Expanded proposal for stakeholders |
| `prd.md` | Product requirements document |
| `mvp-scope.md` | Explicit MVP boundary — in/out |
| `feature-list.md` | Prioritized feature table (Must/Should/Nice) |
| `user-stories.md` | User stories in "As a / I want / So I can" format |
| `user-flows.md` | Key user journeys |
| `roadmap.md` | Phase 1 → Phase 2 → Phase 3 timeline |
| `risk-checklist.md` | Known risks and mitigations |
| `success-metrics.md` | MVP, 30-day, and 90-day success targets |

**Folder:** `docs/planning/`

**Gate:** User must approve MVP scope before entering Phase 4.

---

### Phase 4: Organization Branch

**Goal:** Organize the project before any files or folders are created.

**Organization files to produce:**

| File | Purpose |
|------|---------|
| `file-structure-plan.md` | Proposed folder/file layout |
| `tool-stack-options.md` | Stack options with tradeoffs |
| `selected-stack.md` | Final approved stack decision |
| `task-breakdown.md` | Work items by category |
| `milestone-plan.md` | Milestones mapped to roadmap |
| `roles-and-agents.md` | Who/what handles each area |
| `dependency-map.md` | What depends on what |
| `build-order.md` | Ordered sequence of what to build |
| `decision-log.md` | All major decisions and rationale |

**Folder:** `docs/organization/`

---

### Phase 5: Tool Stack Decision

**Goal:** Pick tools only after the project is fully understood.

**Output file:** `docs/organization/selected-stack.md` (see template)

**Default stack options to present:**

| Layer | Options |
|-------|---------|
| Frontend | React + Vite · Next.js · Vue · SvelteKit · Static HTML/CSS |
| Backend | FastAPI · Django · Node.js/Express · NestJS · Laravel |
| Database | PostgreSQL · MySQL · SQLite · MongoDB · Supabase · Firebase |
| Hosting | Vercel · Hostinger · Render · Railway · Fly.io |
| Automation | GitHub Actions · n8n · Zapier · Make · Cron jobs |
| Analytics | PostHog · Google Analytics · Plausible · Mixpanel · Search Console |
| Design | Figma · Canva · Miro |
| Docs | Markdown · Obsidian · VitePress · Notion |

**Gate:** User must approve the stack before entering Phase 6.

---

### Phase 6: Validation Gate

**Goal:** Prevent bad builds before they start.

Run through all five gate checklists in `docs/gates/`:

1. `research-complete-checklist.md`
2. `mvp-approval-checklist.md`
3. `stack-approval-checklist.md`
4. `build-readiness-checklist.md`
5. `handoff-checklist.md`

The build readiness checklist covers: Project Identity · Research · Planning · Organization ·
Approvals. All items must be checked before proceeding.

**Gate:** All checklist items must pass. Any unchecked item blocks handoff.

---

### Phase 7: Build Agent Handoff

**Goal:** Hand off to coding agents only after all planning is approved.

**Output file:** `docs/handoff/build-agent-handoff.md` (see template)

The handoff document includes: approved project summary, MVP scope, selected stack, approved
file structure, build order, must-build-first list, do-not-build-yet list, known risks,
and a final instruction to the build agent not to expand beyond the approved MVP without
user approval.

---

**Stop conditions:**
- Stop and ask the user if any gate question is unclear or unanswered.
- Stop and warn before creating any files outside the `docs/` folder.
- Do not advance phases without explicit user approval at each gate.

---

## Edge Cases
- **User wants to skip phases:** Warn that skipped phases increase build risk; document the skip in `decision-log.md`.
- **Contradictory inputs:** Surface the contradiction and ask the user to resolve it before proceeding.
- **Scope creep during planning:** Flag as out-of-MVP scope; add to roadmap Phase 2 instead.
- **Research shows low opportunity:** Present the `opportunity-summary.md` recommendation honestly — including "Pause" if warranted.
- **User returns mid-session:** Resume from the last approved gate; do not restart.

---

## Safety & Secrets
- Never log, commit, or embed credentials, API keys, or tokens in any generated document.
- Use `<YOUR_VALUE>` placeholders in any configuration examples.
- Warn before creating any file outside the approved `docs/` structure.
- Do not generate code files, infrastructure configs, or build scaffolding — this skill ends at handoff.

---

## Examples

### Example 1: SaaS idea intake
**User prompt:** "I want to build a SaaS tool that helps freelancers track their invoices
and payments. I don't know where to start."

**Expected output:**
Phase 0 intake questions presented → user answers → Project Summary produced:
"This project is a Web App for freelancers that solves payment tracking by providing a
simple invoicing and payment dashboard. The simplest first version is: invoice creation,
status tracking (sent/paid/overdue), and a payment summary view."
Gate presented for approval before Phase 1.

### Example 2: Research-blocked feature expansion
**User prompt:** "Can we just add a marketplace feature to the MVP?"

**Expected output:**
Skill flags that marketplace is outside the approved MVP scope. Adds the feature to
`roadmap.md` Phase 2. Reminds user that the "Do Not Build Yet" rule applies.
Asks if user wants to re-scope the MVP with full approval gate restart.

---

## Testing / Evals
See `evals/evals.json` for test prompts. Run 2–3 prompts and compare outputs against
`expected_output` descriptions.

**Manual eval steps:**
1. Copy a prompt from `evals/evals.json`.
2. Run it with this skill active.
3. Check that the skill prompts for intake questions before producing any output.
4. Verify that no files outside `docs/` are created.
5. Confirm each gate pauses for user approval.

---

## Templates

All document templates are stored in `templates/`. See:
- `templates/00-project-summary.md`
- `templates/research/` — one template per research file
- `templates/planning/` — one template per planning file
- `templates/organization/` — one template per organization file
- `templates/gates/` — one template per gate checklist
- `templates/handoff/build-agent-handoff.md`

---

## References
- [Planning Agent](../planning-agent/SKILL.md) — lightweight planning agent for single outputs
- [Project Planning Skill](../project-planning-skill/SKILL.md) — single-document brief generator
- [Project Intake Skill](../project-intake-skill/SKILL.md) — intake-only skill
- [Launch Checklist Skill](../launch-checklist-skill/SKILL.md) — post-planning launch readiness
- [Skill Registry](../skill-registry.md)
- [AI Agent Architecture](../../references/ai-agent-architecture.md)
