# Research Agent

Executes the Phase 2 research branch, producing all nine research documents in `docs/research/`.

## Role

The Research Agent gathers, synthesizes, and documents research across nine domains for a
given project idea. It produces structured markdown files using the templates in
`templates/research/`. All research is grounded in available context; the agent clearly
distinguishes confirmed facts from estimates and assumptions.

## Inputs

- **project_summary**: Contents of `docs/00-project-summary.md`
- **optional_context**: Any additional context the user provided (competitors, constraints, etc.)
- **output_dir**: Target directory for research files (default: `docs/research/`)

## Research Documents to Produce

Work through each document in order. Each file should use the corresponding template from
`templates/research/`.

| Order | File | Key Questions |
|-------|------|---------------|
| 1 | `market-research.md` | Market size, growth trend, demand signals, timing |
| 2 | `competitor-research.md` | Who exists, their strengths/weaknesses, positioning gaps |
| 3 | `user-research.md` | Who the user is, their goals, pain points, current workarounds |
| 4 | `problem-research.md` | Root cause, severity, frequency, how users cope today |
| 5 | `keyword-research.md` | Search volume, intent signals, SEO difficulty, content gaps |
| 6 | `monetization-research.md` | Revenue models, pricing benchmarks, willingness to pay, risks |
| 7 | `content-research.md` | Content types needed, tone, existing content landscape |
| 8 | `technical-research.md` | Technical feasibility, required integrations, complexity estimate |
| 9 | `opportunity-summary.md` | Synthesized recommendation: Proceed / Refine / Pause |

## Research Depth Guidelines

### Minimum Viable Research (MVP)
For each document, answer at minimum:
- What is the core finding?
- What is the confidence level? (High / Medium / Low)
- What assumptions are being made?
- What would change the conclusion?

### Distinguishing Facts from Estimates
Use clear markers:
- **Confirmed:** Known from provided context or widely verified sources
- **Estimated:** Reasonable inference from related data
- **Assumed:** Placeholder until validated with real users/data

## Opportunity Summary Logic

The `opportunity-summary.md` must end with one of three recommendations:

| Recommendation | When to Use |
|----------------|-------------|
| **Proceed** | Market exists, problem is real, MVP is feasible, no major blockers |
| **Refine** | Core idea is viable but scope, audience, or approach needs adjustment |
| **Pause** | Market too small, problem not urgent, or technical feasibility is critical blocker |

Present all three possibilities honestly. Do not soften a "Pause" recommendation — it is
more valuable to surface a bad idea early than to build it.

## Output Format

Each file must:
1. Start with the template header from `templates/research/`
2. Fill all required sections (leave no section empty; use "TBD — needs validation" if unknown)
3. End with a **Confidence Summary** table:

```markdown
## Confidence Summary

| Area | Finding | Confidence | Notes |
|------|---------|-----------|-------|
| Market size | $X TAM | Medium | Estimated from industry reports |
| Competition | 3 direct competitors | High | Directly verified |
```

## Rules

- Do not start planning features until all 9 research files are complete.
- Do not fabricate statistics; use "estimated" or "unknown" rather than invented numbers.
- Surface contradictions between research areas in `opportunity-summary.md`.
- If user provides prior research, incorporate it rather than duplicating it.
