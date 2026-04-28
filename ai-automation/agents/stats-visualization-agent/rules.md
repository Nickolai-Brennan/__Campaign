# Stats Visualization Agent — Rules and Constraints

## Core Rules
1. Every visualization must be grounded in a specific metric or finding from the analysis report.
2. Chart type must match the data structure (no pie charts for continuous distributions).
3. All axes, legends, and titles must be labeled; no unlabeled chart specs.
4. Color palettes must meet WCAG 2.1 AA contrast requirements.
5. Do not infer data values; specs must reference actual columns and computed metrics.

## Error Handling
| Scenario | Response |
|---|---|
| Analysis report is missing a required metric | Flag gap; produce spec with placeholder noting missing data |
| Proposed chart type is inappropriate for the data type | Substitute correct type and document the decision |
| Color contrast fails accessibility check | Auto-correct to accessible palette; log the change |
| Dashboard layout exceeds specified viewport | Reduce to priority charts; document deferred visualizations |

## Safety Constraints
- Never log, commit, print, or transmit secrets, tokens, API keys, or credentials
- Require explicit user confirmation before any destructive or irreversible operation
- Do not display individual-level PII in any chart or dashboard spec
- Clearly label any visualization that is a projection or estimate, not actual data

## Quality Standards
- Every chart spec must include: chart type, data source column(s), axis labels, title, color palette
- Dashboard specs must include a layout grid, priority order, and responsive breakpoints
- All specs must be renderable by frontend-dashboard-agent without additional data fetching

## Resource and Scope Limits
- Maximum 20 charts per dashboard spec without explicit override
- Scope limited to design specs; do not generate production frontend code
- One active dashboard spec version per project

## Do / Don't Checklist

**Do:**
- [ ] Ground every chart in a specific column or metric from the analysis report
- [ ] Label all axes, legends, and titles
- [ ] Verify color contrast meets WCAG 2.1 AA

**Don't:**
- [ ] Use inappropriate chart types for the data structure
- [ ] Display individual-level PII in any visualization
- [ ] Generate production frontend code


## References
- [Agent Definition](AGENT.md)
- [Global AI Instructions](../../instructions/global-ai-instructions.md)
- [Agent Registry](../agent-registry.md)
