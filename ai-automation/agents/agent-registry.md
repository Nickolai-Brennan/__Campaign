# Agent Registry

## Overview

All agents in this registry follow the standard four-file structure:
- `AGENT.md` — canonical definition, capabilities, I/O, operating instructions
- `prompt.md` — system prompt used to initialize the agent
- `rules.md` — domain rules, error handling, safety constraints, Do/Don't checklist
- `workflows.md` — workflow participation, integration points, handoff protocol

Output from each agent is saved to `docs/agent-outputs/<agent-name>/` and formatted using the shared YAML output template (see any `AGENT.md`).

---

## Core Agents

| Agent | Directory | Role |
|---|---|---|
| Orchestrator Agent | `orchestrator-agent/` | Entry point for all workflows; routes work, manages handoffs, synthesizes status |
| Project Planner Agent | `project-planner-agent/` | Converts requirements into project brief, roadmap, milestones, risk register |

## Data Agents

| Agent | Directory | Role |
|---|---|---|
| Data Cleanup Agent | `data-cleanup-agent/` | Cleans, normalizes, deduplicates, and validates raw datasets |
| Data Analysis Agent | `data-analysis-agent/` | Analyzes datasets; extracts insights, statistics, and patterns |

## Development Agents

| Agent | Directory | Role |
|---|---|---|
| Model Development Agent | `model-development-agent/` | Designs scoring/ML model specs, feature engineering, evaluation plans |
| Stats Visualization Agent | `stats-visualization-agent/` | Designs chart specs, dashboard layouts, visualization recommendations |

## Infrastructure Agents

| Agent | Directory | Role |
|---|---|---|
| API Agent | `api-agent/` | Designs REST/GraphQL contracts, OpenAPI specs, service boundaries |
| Frontend Dashboard Agent | `frontend-dashboard-agent/` | Designs UI component plans, page layouts, state management |
| Backend Agent | `backend-agent/` | Designs service architecture, business logic, data access patterns |
| Database Agent | `database-agent/` | Designs DB schemas, DDL SQL, ERDs, indexes, migration strategies |

## Support Agents

| Agent | Directory | Role |
|---|---|---|
| Documentation Agent | `documentation-agent/` | Generates READMEs, API refs, runbooks, architecture docs |
| Testing Agent | `testing-agent/` | Plans test strategy, test cases, coverage targets, QA checklists |
| Marketing Agent | `marketing-agent/` | Plans marketing strategy, messaging, content calendar, campaigns |
| Repo Maintenance Agent | `repo-maintenance-agent/` | Maintains repo health, changelogs, CI/CD hygiene |

---

## Typical Workflow Sequence

```
orchestrator-agent
  → project-planner-agent   (WF-00)
  → data-cleanup-agent      (WF-02)
  → data-analysis-agent     (WF-03)
  → model-development-agent (WF-04)  [if ML needed]
  → database-agent          (WF-07)
  → api-agent               (WF-06)
  → backend-agent           (WF-06)
  → stats-visualization-agent (WF-05)
  → frontend-dashboard-agent  (WF-05)
  → testing-agent           (WF-08)
  → documentation-agent     (WF-09)
  → repo-maintenance-agent  (WF-10)
  → marketing-agent         (WF-10)
  → orchestrator-agent      (sign-off)
```

Agents may run in parallel when there are no dependencies between them. See individual `workflows.md` files for exact integration points.
