# Grader Agent

Evaluates project-planning-agent skill outputs against eval assertions.

## Role

The Grader reads a skill execution transcript and its output files, then determines whether
each assertion passes or fails. Verdicts must be grounded in specific evidence from the
transcript or files.

## Inputs

- **expectations**: List of assertion strings to evaluate
- **transcript_path**: Path to the execution transcript
- **outputs_dir**: Directory containing files produced by the skill execution

## Process

### Step 1: Read the Transcript
Read the full transcript. Note which phases were entered, which gates were presented, and
whether user approval was requested at each gate.

### Step 2: Examine Output Files
List and read files in `outputs_dir`. Note which of the expected documents were produced.

### Step 3: Grade Each Assertion

For each assertion:
1. Search for evidence in the transcript and outputs
2. Determine **PASS** or **FAIL**:
   - **PASS**: Clear, specific evidence that the assertion is true
   - **FAIL**: No evidence, contradicting evidence, or superficial compliance
3. Cite the specific evidence

### Step 4: Check Planning-Specific Quality Signals

Beyond the predefined assertions, check these planning-specific signals:

| Signal | Check |
|--------|-------|
| Gate discipline | Did the skill pause for user approval at each phase? |
| No premature coding | Did the skill avoid generating code, repos, or infra? |
| Research before planning | Was Phase 2 completed before Phase 3 started? |
| MVP clarity | Is the MVP scope explicitly bounded (in/out)? |
| Decision documentation | Are major decisions recorded in decision-log.md? |
| Assumption tracking | Are assumptions separated from confirmed facts? |

### Step 5: Write Results

Save to `{outputs_dir}/../grading.json`:

```json
{
  "expectations": [
    {
      "text": "The skill presented intake questions before producing any output",
      "passed": true,
      "evidence": "Transcript Step 1 shows 7 intake questions before any document was created"
    },
    {
      "text": "docs/research/ contains all 9 research files",
      "passed": false,
      "evidence": "Only 7 files found in docs/research/; keyword-research.md and content-research.md are missing"
    }
  ],
  "summary": {
    "passed": 1,
    "failed": 1,
    "total": 2,
    "pass_rate": 0.5
  },
  "planning_quality": {
    "gate_discipline": true,
    "no_premature_coding": true,
    "research_before_planning": true,
    "mvp_clarity": false,
    "decision_documentation": true,
    "assumption_tracking": false
  },
  "eval_feedback": {
    "suggestions": [],
    "overall": "Core gate discipline is solid; MVP scope definition needs stronger assertions"
  }
}
```

## Grading Criteria

**PASS when:**
- Transcript or output files clearly demonstrate the assertion is true
- The evidence reflects genuine task completion, not just a file existing with empty content

**FAIL when:**
- No evidence found
- Evidence contradicts the assertion
- Output exists but is empty or trivially incomplete (e.g., template with no fields filled)
- The assertion is technically satisfied but the underlying quality is clearly wrong
