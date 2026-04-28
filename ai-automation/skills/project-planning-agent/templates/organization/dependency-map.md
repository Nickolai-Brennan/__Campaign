# Dependency Map

## Dependency Overview

```
[Project Summary]
      |
[Research] ──────────────────────────────┐
      |                                  |
[Planning] ←── opportunity-summary.md    |
      |                                  |
[Organization] ←── planning docs         |
      |                                  |
[Stack Decision] ←── technical-research  |
      |                                  |
[Build Readiness Gate]                   |
      |                                  |
[Build Agent Handoff] ←──────────────────┘
```

## File Dependencies

| File | Depends On |
|------|-----------|
| `prd.md` | `mvp-scope.md`, `user-stories.md` |
| `selected-stack.md` | `technical-research.md`, `tool-stack-options.md` |
| `build-order.md` | `selected-stack.md`, `task-breakdown.md` |
| `build-agent-handoff.md` | All of the above |

## External Dependencies

| Dependency | Type | Status |
|------------|------|--------|
| | Service / Library | Unknown |
