# Repo Maintenance Agent — Workflows

## Participating Workflows

### WF-10: launch-review
- **Role**: Performs final repository health check; validates CI/CD, secret scan, dependency audit, changelog, and branch protection
- **Receives from**: orchestrator-agent (all prior workflow artifacts, documentation complete signal)
- **Produces**: Repo health report, updated changelog, CI/CD validation summary, launch go/no-go recommendation
- **Hands off to**: orchestrator-agent (health report feeds final launch readiness summary)

## Integration Points

| System / Agent | Integration Type | Notes |
|---|---|---|
| orchestrator-agent | Receives task assignment; returns health report | Central coordination point for WF-10 |
| documentation-agent | Receives documentation artifacts | Verifies docs are committed and linked in README |
| testing-agent | Receives QA sign-off artifact | Confirms testing gate passed before launch |
| All agents | Consumes all prior workflow outputs | Health check validates completeness of all artifacts |

## Handoff Protocol

### Receiving a task
1. Read the handoff_notes from the upstream agent
2. Validate that all required inputs are present
3. If inputs are missing, surface the gap to the orchestrator before proceeding

### Completing a task
1. Produce all required outputs in the standard YAML format
2. Write output to `docs/agent-outputs/repo-maintenance-agent/`
3. Set `next_agent` and populate `handoff_notes`
4. Notify orchestrator of completion


## References
- [Agent Definition](AGENT.md)
- [Global AI Instructions](../../instructions/global-ai-instructions.md)
- [Agent Registry](../agent-registry.md)
