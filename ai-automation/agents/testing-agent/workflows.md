# Testing Agent — Workflows

## Participating Workflows

### WF-08: testing-validation
- **Role**: Designs test strategy, test cases, coverage targets, and QA checklists across all layers
- **Receives from**: orchestrator-agent (OpenAPI spec, service interfaces, component hierarchy, DDL, model spec)
- **Produces**: Test plan, test case library, coverage targets, QA checklist, security test scenarios
- **Hands off to**: orchestrator-agent (QA sign-off triggers WF-09)

## Integration Points

| System / Agent | Integration Type | Notes |
|---|---|---|
| orchestrator-agent | Receives task assignment; returns QA sign-off | Entry point for WF-08; triggers WF-09 on completion |
| api-agent | Receives OpenAPI spec | Contract tests derived from spec |
| backend-agent | Receives service interfaces | Unit and integration tests derived from interfaces |
| frontend-dashboard-agent | Receives component hierarchy | UI test cases derived from components |
| database-agent | Receives DDL scripts | Migration and constraint tests |
| model-development-agent | Receives model spec | Model evaluation tests |

## Handoff Protocol

### Receiving a task
1. Read the handoff_notes from the upstream agent
2. Validate that all required inputs are present
3. If inputs are missing, surface the gap to the orchestrator before proceeding

### Completing a task
1. Produce all required outputs in the standard YAML format
2. Write output to `docs/agent-outputs/testing-agent/`
3. Set `next_agent` and populate `handoff_notes`
4. Notify orchestrator of completion


## References
- [Agent Definition](AGENT.md)
- [Global AI Instructions](../../instructions/global-ai-instructions.md)
- [Agent Registry](../agent-registry.md)
