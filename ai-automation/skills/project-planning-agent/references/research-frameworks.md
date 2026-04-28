# Research Frameworks

Reference frameworks for conducting each of the 9 research documents in Phase 2.
Load this file when you need structured guidance for a specific research area.

---

## Market Research Framework

**Goal:** Determine whether a real, accessible market exists.

### Key Dimensions

| Dimension | Questions to Answer |
|-----------|-------------------|
| Market size | TAM / SAM / SOM — even rough estimates help |
| Growth trend | Is this market growing, stable, or shrinking? |
| Timing | Why now? What's changed recently? |
| Demand signals | Are people actively searching for, buying, or asking about this? |
| Entry barriers | How hard is it for a new entrant to gain a foothold? |

### Confidence Markers

- **High confidence:** Direct data (sales figures, search volume, industry reports)
- **Medium confidence:** Proxy data (related market size, competitor revenue estimates)
- **Low confidence:** Inference from anecdote, forums, or single data points

---

## Competitor Research Framework

**Goal:** Map who already exists, what they do well, and where the gaps are.

### Competitor Types

| Type | Description |
|------|-------------|
| Direct | Solves the exact same problem for the same user |
| Indirect | Solves the same problem differently (e.g., spreadsheet vs. app) |
| Substitute | User uses this instead (e.g., manual process, hiring someone) |
| Emerging | New entrants building toward the same space |

### Analysis Dimensions

For each competitor, capture:
- Target user
- Core value proposition
- Pricing model
- Key strengths (what users love)
- Key weaknesses (what users complain about)
- Positioning gap (what they don't address)

### Gap Analysis Output

Summarize with: "The gap this project can fill is _____ because no current competitor ___."

---

## User Research Framework

**Goal:** Define who the user is with precision, and what they actually need.

### User Dimensions

| Dimension | Questions |
|-----------|-----------|
| Demographics | Age, role, industry, company size (if B2B) |
| Goals | What are they trying to achieve? |
| Pain points | What frustrates them about the current situation? |
| Workarounds | What do they do today instead of using your solution? |
| Trigger | What event causes them to look for a solution? |
| Success | How do they know the problem is solved? |

### Persona Template

```
Name: [Persona name]
Role: [Job title or life situation]
Goals: [2–3 primary goals relevant to this problem]
Pain points: [2–3 specific frustrations]
Current workaround: [What they use today]
Trigger: [What makes them look for a new solution]
```

---

## Problem Research Framework

**Goal:** Understand the root cause, severity, and frequency of the problem.

### Problem Depth Questions

1. **Root cause:** Why does this problem exist? Is it a process gap, a tool gap, or a knowledge gap?
2. **Severity:** How painful is the problem on a scale of 1–10? Does it cost money, time, or emotional wellbeing?
3. **Frequency:** How often does the problem occur? Daily / weekly / occasionally / rarely?
4. **Urgency:** Does the user need to solve this now, or can they tolerate it indefinitely?
5. **Scope:** Is this problem unique to a niche, or is it widespread?

### Problem Statement Format

> When [user] tries to [goal], they experience [problem] because [root cause], which causes [negative outcome]. This happens [frequency] and is [severity] severity.

---

## Keyword Research Framework

**Goal:** Validate search demand and identify the content and SEO landscape.

### Keyword Categories

| Category | Description | Example |
|----------|-------------|---------|
| Problem-aware | User describes the pain | "how to track freelance invoices" |
| Solution-aware | User knows a solution type exists | "freelance invoice software" |
| Brand-aware | User knows specific products | "FreshBooks alternative" |
| Comparison | User is evaluating options | "best invoice tools for freelancers" |

### Metrics to Estimate

- **Search volume:** High (>10k/mo) / Medium (1k–10k) / Low (<1k)
- **Competition:** High / Medium / Low (based on existing content quality)
- **Intent:** Informational / Commercial / Transactional

### Content Gap Signal

The best SEO opportunity is a high-volume, commercial-intent keyword with low-quality
existing content (thin articles, poor UX, no clear answer).

---

## Monetization Research Framework

**Goal:** Identify revenue models that fit the project and validate willingness to pay.

### Revenue Model Options

| Model | Best For | Risk |
|-------|---------|------|
| Subscription (SaaS) | Ongoing value, habit-forming products | Churn |
| One-time purchase | Tools, templates, digital products | No recurring revenue |
| Freemium | High-volume consumer products | Free-to-paid conversion rate |
| Usage-based | API, infrastructure, high-variance usage | Revenue unpredictability |
| Marketplace fee | Two-sided platforms | Needs both sides simultaneously |
| Affiliate | Content sites, review platforms | Dependent on third-party programs |
| Advertising | High-traffic media / content | Privacy concerns, low CPM |
| Services / consulting | B2B tools with implementation needs | Doesn't scale |

### First Revenue Experiment

Before building a full billing system, document the simplest experiment to validate
willingness to pay:

> "The first revenue experiment is: offer [X] to [Y users] for [$Z] via [Stripe / Gumroad / manual invoice]. If [N] people pay, we have validated the model."

---

## Technical Research Framework

**Goal:** Assess feasibility, complexity, and integration requirements.

### Feasibility Dimensions

| Dimension | Questions |
|-----------|-----------|
| Core functionality | Can the primary feature be built with standard tools? |
| Integrations | What third-party APIs or services are required? |
| Data model | How complex is the data structure? Any tricky relationships? |
| Scale requirements | What traffic/data volume does MVP need to handle? |
| Security requirements | Does this handle PII, payments, or sensitive data? |
| Build time estimate | How long for a solo developer to reach MVP? |

### Complexity Signal Table

| Signal | Adds Complexity |
|--------|----------------|
| Real-time features | Yes (WebSockets, polling) |
| Payment processing | Yes (Stripe integration, PCI compliance) |
| File uploads | Moderate (storage, processing) |
| Email delivery | Moderate (ESP, deliverability) |
| Third-party OAuth | Moderate (multiple providers add risk) |
| AI/ML inference | High (latency, cost, reliability) |
| Mobile support | High (separate codebase or React Native) |
| Multi-tenancy | High (data isolation, permissions) |

---

## Opportunity Summary Framework

**Goal:** Synthesize all 8 research documents into a single go/no-go recommendation.

### Scoring Matrix

Rate each dimension 1–5 after completing research:

| Dimension | Score (1–5) | Weight |
|-----------|------------|--------|
| Market exists and is accessible | | 20% |
| Problem is real and urgent | | 20% |
| Clear differentiation from competitors | | 15% |
| User is well-defined and reachable | | 15% |
| Technical feasibility at MVP | | 15% |
| Viable monetization path | | 15% |

**Weighted score = Σ(score × weight)**

### Recommendation Thresholds

| Weighted Score | Recommendation |
|---------------|----------------|
| 4.0–5.0 | **Proceed** — strong signal, build the MVP |
| 3.0–3.9 | **Refine** — viable but needs scope/audience/approach adjustment |
| 1.0–2.9 | **Pause** — significant risk; validate assumptions before investing further |

Present the recommendation honestly. A "Pause" is not a failure — it prevents a worse one.
