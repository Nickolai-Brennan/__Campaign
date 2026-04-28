# Agent Template

Use this template when creating a new agent. Copy each file into a new `<agent-name>/` directory under `ai-automation/agents/`, replace all `[PLACEHOLDER]` sections, and register the agent in `agent-registry.md`.

## Directory Structure

```
<agent-name>/
├── AGENT.md       — Canonical definition: purpose, capabilities, I/O, operating instructions
├── prompt.md      — System prompt used to initialize the agent in a session
├── rules.md       — Domain rules, error handling, safety constraints, Do/Don't checklist
└── workflows.md   — Workflow participation, integration points, handoff protocol
```

## Creation Steps

1. Create the agent directory: `ai-automation/agents/<agent-name>/`
2. Copy and fill in each of the four template files (see `ai-automation/templates/agent-template.md` for starters)
3. Define the YAML frontmatter in `AGENT.md` (name, phase, inputs, outputs)
4. Write the system prompt in `prompt.md` — this is what gets injected into the model context
5. Enumerate specific rules and error handling in `rules.md`
6. Document which workflows the agent participates in and its exact handoff points in `workflows.md`
7. Add the agent to `agent-registry.md`
8. Add an entry to the relevant `workflows.md` files for the workflows it joins

## Key Conventions

- **Output format**: Every agent must use the shared YAML output template (see any existing `AGENT.md`)
- **Output directory**: `docs/agent-outputs/<agent-name>/`
- **Next agent**: Always populate `next_agent` in output to enable orchestration
- **Secrets**: Never log, commit, or transmit credentials in any output or example
- **Confirmation**: Always warn before destructive operations and require explicit user sign-off
- **Style**: Imperative throughout; keep AGENT.md under 120 lines, other files under 100 lines
