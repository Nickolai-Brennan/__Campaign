# Stats Visualization Agent — Workflows

## Participating Workflows

### WF-03: data-analysis
- **Role**: Receives analysis report to understand available metrics; prepares visualization requirements
- **Receives from**: data-analysis-agent (analysis report)
- **Produces**: Visualization requirements list
- **Hands off to**: orchestrator-agent (ready for WF-05)

### WF-05: dashboard-build
- **Role**: Designs chart specs, dashboard layout, and data-binding requirements
- **Receives from**: orchestrator-agent (analysis report, model spec if applicable)
- **Produces**: Chart spec YAML, dashboard layout spec, accessibility report
- **Hands off to**: frontend-dashboard-agent

## Integration Points

| System / Agent | Integration Type | Notes |
|---|---|---|
| orchestrator-agent | Receives task assignment | Entry point for WF-05 |
| data-analysis-agent | Receives analysis report | Source of all metrics and findings |
| model-development-agent | Receives model spec | Drives model performance charts |
| frontend-dashboard-agent | Sends chart and layout specs | Direct downstream consumer |

## Handoff Protocol

### Receiving a task
1. Read the handoff_notes from the upstream agent
2. Validate that all required inputs are present
3. If inputs are missing, surface the gap to the orchestrator before proceeding

### Completing a task
1. Produce all required outputs in the standard YAML format
2. Write output to `docs/agent-outputs/stats-visualization-agent/`
3. Set `next_agent` and populate `handoff_notes`
4. Notify orchestrator of completion


## References
- [Agent Definition](AGENT.md)
- [Global AI Instructions](../../instructions/global-ai-instructions.md)
- [Agent Registry](../agent-registry.md)
