# Project Template — DevOps / Infrastructure / IaC

Use this template when initializing a **DevOps / Infrastructure / IaC** project (CI/CD, containers, Terraform, Kubernetes). Answer every question and save the completed file as `PROJECT.md` at the root of your repository.

---

## Section 1: Project Type

**Primary Type**: DevOps / Infrastructure / IaC  
**Secondary Types**: <!-- e.g. Automation, API -->

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

**3.1 — What specific infrastructure or delivery problem does this project solve?**

> **Answer**:

**3.2 — What is the single most important outcome this project must deliver?**

> **Answer**:

**3.3 — List up to three secondary goals.**

1.
2.
3.

---

## Section 4: Audience

**4.1 — Who are the primary consumers of this infrastructure or pipeline?**
*(e.g. application development teams, platform engineers, operators)*

> **Answer**:

**4.2 — Who are secondary beneficiaries?**

> **Answer**:

**4.3 — Who are the stakeholders?**

> **Answer**:

**4.4 — What is the expected scale of workloads managed?**
*(e.g. "20 microservices", "500 VMs", "5 environments")*

> **Answer**:

---

## Section 5: Technical Stack

**5.1 — What IaC tool(s) are used?**
*(e.g. Terraform, Pulumi, AWS CDK, CloudFormation, Ansible, Helm)*

> **Answer**:

**5.2 — What container runtime or orchestration platform is used?**
*(e.g. Docker, Kubernetes, ECS, Nomad, none)*

> **Answer**:

**5.3 — What CI/CD platform is used?**
*(e.g. GitHub Actions, GitLab CI, Jenkins, CircleCI, Argo CD, Tekton)*

> **Answer**:

**5.4 — What cloud provider(s) are targeted?**
*(e.g. AWS, GCP, Azure, multi-cloud, on-premises)*

> **Answer**:

**5.5 — What observability stack is used?**
*(e.g. Prometheus + Grafana, Datadog, New Relic, CloudWatch, OpenTelemetry)*

> **Answer**:

**5.6 — What secret management solution is used?**
*(e.g. HashiCorp Vault, AWS Secrets Manager, Azure Key Vault, Doppler)*

> **Answer**:

**5.7 — What networking stack is used?**
*(e.g. VPC, service mesh like Istio/Linkerd, Ingress controller)*

> **Answer**:

**5.8 — What artifact registry is used?**
*(e.g. ECR, GCR, Docker Hub, Nexus, Artifactory)*

> **Answer**:

---

## Section 6: Infrastructure Design

**6.1 — What environments are managed?**
*(e.g. dev, staging, production; list and describe each)*

> **Answer**:

**6.2 — What deployment strategy is used?**
*(e.g. blue-green, canary, rolling update, feature flags)*

> **Answer**:

**6.3 — What is the state management strategy for IaC?**
*(e.g. Terraform remote state in S3 + DynamoDB lock, Pulumi Cloud)*

> **Answer**:

**6.4 — What is the GitOps or change management workflow?**
*(e.g. PR-based changes, plan/apply pipeline, manual approvals for production)*

> **Answer**:

**6.5 — What is the disaster recovery (DR) strategy?**
*(e.g. RTO target, RPO target, backup regions, runbooks)*

> **Answer**:

**6.6 — What compliance controls are enforced at the infrastructure level?**
*(e.g. policy-as-code with OPA/Conftest, AWS Config rules, required tags)*

> **Answer**:

---

## Section 7: Data Profile

**7.1 — What infrastructure state or configuration data is managed?**

> **Answer**:

**7.2 — What audit logs or telemetry does this project produce?**

> **Answer**:

**7.3 — What is the data sensitivity level?**
Choose one: `public` · `internal` · `confidential` · `restricted`

> **Answer**:

**7.4 — Does the infrastructure handle PII or PHI workloads?**
Choose one: `true` · `false`

> **Answer**:

**7.5 — What is the log retention policy?**

> **Answer**:

---

## Section 8: Architecture

**8.1 — Describe the high-level infrastructure architecture in 2–5 sentences.**

> **Answer**:

**8.2 — Is there an infrastructure or network diagram? Provide a link or file path.**

> **Answer**:

---

## Section 9: Constraints

**9.1 — What is the budget or cost target?**
*(Include cloud spend targets, e.g. "< $2,000/month")*

> **Answer**:

**9.2 — What is the target delivery date or rollout timeline?**

> **Answer**:

**9.3 — What compliance or regulatory requirements apply?**
*(e.g. SOC 2, ISO 27001, FedRAMP, HIPAA, PCI-DSS)*

> **Answer**:

**9.4 — What is the deployment frequency SLA?**
*(e.g. "Deploy to production multiple times/day", "Weekly release window")*

> **Answer**:

**9.5 — What is the uptime / availability target for managed services?**

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
| `terraform/` or `infra/` | IaC source files |
| `.github/workflows/` | CI/CD pipeline definitions |
| | |
| | |
