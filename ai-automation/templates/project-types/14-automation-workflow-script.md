# Project Template — Automation / Workflow / Script

Use this template when initializing an **Automation / Workflow / Script** project (recurring jobs, bots, glue code). Answer every question and save the completed file as `PROJECT.md` at the root of your repository.

---

## Section 1: Project Type

**Primary Type**: Automation / Workflow / Script  
**Secondary Types**: <!-- e.g. Data Pipeline, CLI Tool -->

---

## Section 2: Basic Identity

| Field | Value |
|-------|-------|
| **Project Name** | |
| **Tagline** (one sentence) | |
| **Version / Phase** | `prototype` · `mvp` · `production` |
| **Status** | `active` · `on-hold` · `archived` |
| **Owner / Team** | |
| **Created** | YYYY-MM-DD |
| **Last Updated** | YYYY-MM-DD |

---

## Section 3: Purpose

**3.1 — What manual or repetitive process does this automation replace or assist?**

> **Answer**:

**3.2 — What is the single most important outcome this automation must deliver?**

> **Answer**:

**3.3 — List up to three secondary goals.**

1.
2.
3.

---

## Section 4: Audience

**4.1 — Who benefits directly from this automation?**
*(e.g. engineering team, operations team, end customers)*

> **Answer**:

**4.2 — Who are secondary beneficiaries?**

> **Answer**:

**4.3 — Who are the stakeholders?**

> **Answer**:

**4.4 — What is the expected execution frequency or volume?**
*(e.g. "Runs hourly", "Triggered 500 times/day", "On every PR opened")*

> **Answer**:

---

## Section 5: Technical Stack

**5.1 — What programming language is used?**

> **Answer**:

**5.2 — What automation or workflow framework is used?**
*(e.g. GitHub Actions, n8n, Zapier, Make, Temporal, cron, shell script, Python script)*

> **Answer**:

**5.3 — What systems or APIs does this automation integrate with?**
*(e.g. Slack, GitHub, Jira, Salesforce, AWS, email)*

> **Answer**:

**5.4 — What databases or storage systems are used?**

> **Answer**:

**5.5 — What AI/ML models are used, if any?**

> **Answer**:

**5.6 — What cloud or infrastructure platforms run this automation?**
*(e.g. AWS Lambda, GitHub Actions runner, cron on VM, serverless)*

> **Answer**:

**5.7 — What CI/CD tooling is used?**

> **Answer**:

**5.8 — How are secrets and credentials managed?**
*(e.g. environment variables, secrets manager, `.env` file)*

> **Answer**:

---

## Section 6: Automation Design

**6.1 — What triggers this automation?**
*(e.g. scheduled cron, webhook event, file arrival, manual trigger, message queue)*

> **Answer**:

**6.2 — Describe the automation steps in order.**

1.
2.
3.

**6.3 — What is the error handling and retry strategy?**
*(e.g. retry up to 3 times with backoff, send alert on failure, log and continue)*

> **Answer**:

**6.4 — What happens if the automation fails partway through?**
*(e.g. idempotent — safe to re-run; rollback step; manual intervention required)*

> **Answer**:

**6.5 — How are results or outcomes communicated?**
*(e.g. Slack notification, email summary, log entry, database record)*

> **Answer**:

**6.6 — What monitoring and alerting is in place?**
*(e.g. execution logs, failure alerts, SLA dashboards)*

> **Answer**:

---

## Section 7: Data Profile

**7.1 — What data does this automation read (inputs)?**

> **Answer**:

**7.2 — What data does this automation write or produce (outputs)?**

> **Answer**:

**7.3 — What is the data sensitivity level?**
Choose one: `public` · `internal` · `confidential` · `restricted`

> **Answer**:

**7.4 — Does this automation handle PII or sensitive credentials?**
Choose one: `true` · `false`

> **Answer**:

**7.5 — What is the data retention policy for logs and outputs?**

> **Answer**:

---

## Section 8: Architecture

**8.1 — Describe the high-level automation architecture in 2–5 sentences.**

> **Answer**:

**8.2 — What architectural pattern does this automation follow?**
*(e.g. event-driven, scheduled batch, reactive, webhook-driven, polling)*

> **Answer**:

**8.3 — Is there a workflow or sequence diagram? Provide a link or file path.**

> **Answer**:

---

## Section 9: Constraints

**9.1 — What is the budget or cost target?**

> **Answer**:

**9.2 — What is the target delivery date?**

> **Answer**:

**9.3 — What compliance or regulatory requirements apply?**

> **Answer**:

**9.4 — What is the execution time SLA?**
*(e.g. "Must complete within 5 minutes of trigger", "Daily job finishes by 07:00 UTC")*

> **Answer**:

**9.5 — What is the reliability target?**
*(e.g. "≥ 99% successful executions per week")*

> **Answer**:

---

## Section 10: Success Criteria

- [ ]
- [ ]
- [ ]

---

## Section 11: Related Files

| File / URL | Purpose |
|------------|---------|
| `README.md` | Project overview |
| `.github/workflows/` | GitHub Actions workflow definitions (if applicable) |
| | |
| | |
