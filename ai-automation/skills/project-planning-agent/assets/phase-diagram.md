# Project Planning Agent — Phase Flow Diagram

Visual reference for the 8-phase workflow. Use this to orient users and track progress.

## Phase Flow

```
┌─────────────────────────────────────────────────────────────────────┐
│                    PROJECT PLANNING AGENT                           │
│                  Idea → Research → Plan → Build                     │
└─────────────────────────────────────────────────────────────────────┘

  [User Input: Raw Idea]
         │
         ▼
  ┌─────────────┐
  │  PHASE 0    │  Intake Mode
  │  INTAKE     │  → 7 intake questions
  │             │  → Project Summary drafted
  └──────┬──────┘
         │  🔒 GATE: User approves summary
         ▼
  ┌─────────────┐
  │  PHASE 1    │  Project Classification
  │  CLASSIFY   │  → Project Type Scorecard
  │             │  → 00-project-summary.md saved
  └──────┬──────┘
         │  🔒 GATE: User approves classification
         ▼
  ┌─────────────┐
  │  PHASE 2    │  Research Branch (9 documents)
  │  RESEARCH   │  market · competitors · users · problem
  │             │  keywords · monetization · content · tech
  └──────┬──────┘  opportunity-summary (Proceed/Refine/Pause)
         │  🔒 GATE: Research complete + opportunity approved
         ▼
  ┌─────────────┐
  │  PHASE 3    │  Planning Branch (10 documents)
  │  PLANNING   │  brief · proposal · PRD · MVP scope
  │             │  features · user stories · flows · roadmap
  └──────┬──────┘  risks · success metrics
         │  🔒 GATE: User approves MVP scope
         ▼
  ┌─────────────┐
  │  PHASE 4    │  Organization Branch (9 documents)
  │  ORGANIZE   │  file structure · stack options · task breakdown
  │             │  milestones · roles · dependencies · build order
  └──────┬──────┘  decision log
         │  🔒 GATE: User approves organization plan
         ▼
  ┌─────────────┐
  │  PHASE 5    │  Tool Stack Decision
  │  STACK      │  → tool-stack-options.md
  │             │  → selected-stack.md
  └──────┬──────┘
         │  🔒 GATE: User approves stack
         ▼
  ┌─────────────┐
  │  PHASE 6    │  Validation Gate (5 checklists)
  │  VALIDATE   │  research-complete · mvp-approval · stack-approval
  │             │  build-readiness · handoff
  └──────┬──────┘
         │  🔒 GATE: All checklist items pass
         ▼
  ┌─────────────┐
  │  PHASE 7    │  Build Agent Handoff
  │  HANDOFF    │  → build-agent-handoff.md
  │             │  (Hands off to coding agents)
  └─────────────┘

         ✅ PLANNING COMPLETE — BUILD CAN BEGIN
```

## Document Count by Phase

| Phase | Documents Produced | Folder |
|-------|--------------------|--------|
| 0–1 | 1 (project summary) | `docs/` |
| 2 | 9 (research) | `docs/research/` |
| 3 | 10 (planning) | `docs/planning/` |
| 4–5 | 9 (organization + stack) | `docs/organization/` |
| 6 | 5 (gate checklists) | `docs/gates/` |
| 7 | 1 (handoff) | `docs/handoff/` |
| **Total** | **35** | |

## Gate Legend

| Symbol | Meaning |
|--------|---------|
| 🔒 | Hard gate — requires explicit user approval before advancing |
| ✅ | Gate passed — phase complete |
| ⏳ | Gate pending — waiting for user input |
| 🚫 | Gate blocked — unresolved issue must be fixed first |

## Stop Conditions

The skill stops and waits for user input whenever:
- A gate question is presented
- A contradiction in requirements is surfaced
- An opportunity-summary recommends "Pause"
- A file would be created outside `docs/`
- A request is made to skip a phase
