# Planning Checklists — Pre-Phase Verification

Use these checklists before entering each phase to confirm prerequisites are met.
These complement the gate checklists in `templates/gates/`.

---

## Pre-Phase 2 Checklist (Before Starting Research)

Confirm these are true before producing any research documents:

- [ ] Project name is defined and not generic ("My App" or "New Project" are not acceptable)
- [ ] One-sentence idea is clear and specific — someone unfamiliar could understand it
- [ ] Target user is a specific type of person, not "everyone" or "anyone"
- [ ] Problem statement describes a real pain, not just a desire for a feature
- [ ] MVP is scoped to the simplest thing that delivers value (not full vision)
- [ ] `docs/00-project-summary.md` has been created and user has approved it
- [ ] Project type classification is documented with a rationale

**Blocked?** Do not start research until all items above are checked. Go back to Phase 0/1.

---

## Pre-Phase 3 Checklist (Before Starting Planning)

Confirm these are true before producing any planning documents:

- [ ] All 9 research files exist in `docs/research/`
- [ ] `opportunity-summary.md` has a clear recommendation (Proceed / Refine / Pause)
- [ ] If recommendation is "Pause", user has explicitly acknowledged it and chosen to proceed
- [ ] If recommendation is "Refine", the refinement has been documented and agreed upon
- [ ] No critical unanswered questions remain in any research file
- [ ] User has approved the research phase and given go-ahead for planning

**Blocked?** Do not start planning until all research is done and approved.

---

## Pre-Phase 4 Checklist (Before Starting Organization)

Confirm these are true before producing any organization documents:

- [ ] All 10 planning files exist in `docs/planning/`
- [ ] `mvp-scope.md` has explicit "In Scope" and "Out of Scope" sections
- [ ] `prd.md` has at least 3 Must Have functional requirements
- [ ] `feature-list.md` is prioritized with Must / Should / Nice columns
- [ ] `user-stories.md` has at least 3 user stories
- [ ] `roadmap.md` has at least 2 phases defined
- [ ] User has explicitly approved the MVP scope

**Blocked?** Do not start organization until MVP scope is approved.

---

## Pre-Phase 5 Checklist (Before Stack Decision)

Confirm these are true before selecting the final stack:

- [ ] `file-structure-plan.md` exists and is reviewed
- [ ] `tool-stack-options.md` presents ≥2 options per layer
- [ ] `task-breakdown.md` is complete
- [ ] `build-order.md` is sequenced logically
- [ ] `dependency-map.md` shows no circular dependencies
- [ ] `decision-log.md` is being maintained

**Blocked?** Do not finalize stack until organization documents are complete.

---

## Pre-Phase 6 Checklist (Before Validation Gate)

Confirm these are true before running gate checklists:

- [ ] `selected-stack.md` is filled out and user has approved it
- [ ] All organization documents (9 files) are complete
- [ ] All planning documents (10 files) are complete
- [ ] All research documents (9 files) are complete
- [ ] `decision-log.md` records every major decision made
- [ ] No open contradictions between planning documents
- [ ] User has approved the stack

**Blocked?** Do not run gate checklists if any required document is missing or incomplete.

---

## Pre-Phase 7 Checklist (Before Build Handoff)

Confirm these are true before creating the handoff document:

- [ ] `research-complete-checklist.md` — all items checked
- [ ] `mvp-approval-checklist.md` — all items checked
- [ ] `stack-approval-checklist.md` — all items checked
- [ ] `build-readiness-checklist.md` — all items checked
- [ ] `handoff-checklist.md` — all items checked
- [ ] No checklist has any unresolved blocker items
- [ ] User has given final go-ahead for build handoff

**Blocked?** Any unchecked item in any gate checklist blocks the handoff.

---

## Document Completeness Criteria

A document is considered **complete** only if:

1. The file exists in the correct folder
2. All required sections are filled (no empty headers)
3. Placeholder text like "[TBD]" is resolved or explicitly marked as "Assumption — not yet validated"
4. The document has been presented to and acknowledged by the user

A document with empty sections is **not** complete, even if the file exists.

---

## Common Blockers and Resolutions

| Blocker | Resolution |
|---------|-----------|
| Target user is too broad ("small businesses") | Narrow to a specific role ("operations manager at a 5–50 person company") |
| MVP is too large (>3 months of solo dev work) | Cut to the single feature that delivers the core value |
| Competing priorities in the feature list | Use Must/Should/Nice scoring; Must items only for MVP |
| Tech stack decision is blocked by uncertainty | Document the uncertainty; pick the safer/simpler option for MVP |
| Research shows "Pause" but user wants to proceed | Document the risk explicitly in decision-log.md; user must acknowledge in writing |
| Scope creep during planning | Flag it, add to roadmap Phase 2, do not add to MVP without full gate restart |
