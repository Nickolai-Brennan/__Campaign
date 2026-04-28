# Project Types — Quick Reference

Reference guide for Phase 1 project classification. Use this when completing the
Project Type Scorecard in `docs/00-project-summary.md`.

## Type Definitions

| Type | What It Is | Typical Stack | Complexity |
|------|-----------|---------------|-----------|
| **Website** | Static or content-driven public site | HTML/CSS, Next.js, WordPress | Low |
| **Web App** | Interactive browser app with user accounts | React/Vue + backend API + DB | Medium |
| **Mobile App** | Native or cross-platform mobile app | React Native, Flutter, Swift | Medium–High |
| **API** | Programmatic interface for other systems | FastAPI, Node.js, REST/GraphQL | Medium |
| **Database** | Structured data storage and query layer | PostgreSQL, SQLite, Supabase | Medium |
| **Automation** | Scheduled or event-driven workflow | n8n, GitHub Actions, Zapier | Low–Medium |
| **AI Tool** | Model-driven generation or analysis | Python, OpenAI API, LangChain | Medium–High |
| **SaaS** | Subscription product with billing | Full stack + Stripe + auth | High |
| **Marketplace** | Two-sided platform (buyers + sellers) | Full stack + payments + trust | Very High |
| **Content Platform** | Publishing, blog, media site | CMS + SEO + CDN | Low–Medium |
| **Data Dashboard** | Metrics and visualization display | Python/JS + charting + data source | Medium |
| **Internal Tool** | Private productivity tool for a team | Low-code or simple full stack | Low–Medium |
| **eBook / Media** | Digital product or downloadable content | Gumroad, PDF, static delivery | Low |
| **Community Platform** | Forums, social, member-driven content | Circle, Discourse, custom | Medium–High |
| **Affiliate / Review Site** | SEO content + monetization via links | WordPress/Next.js + SEO | Low–Medium |

## Scoring Guide

When filling the Project Type Scorecard, score each type 1–5:

| Score | Meaning |
|-------|---------|
| 5 | Perfect fit — this is exactly what the project is |
| 4 | Strong fit — core characteristics match |
| 3 | Partial fit — some overlap but important differences |
| 2 | Weak fit — shares some features but fundamentally different |
| 1 | Not a fit — different category entirely |

**Rule:** Assign 5 to only one type. If two types score equally, pick the one that best
describes the primary value delivered to the user.

## Common Combinations

Some projects combine types. Document the primary type, then note the secondary:

| Primary | Secondary | Example |
|---------|-----------|---------|
| SaaS | Web App | A subscription task manager |
| Content Platform | Affiliate | A niche review blog with affiliate links |
| AI Tool | API | A text analysis API sold to developers |
| Internal Tool | Dashboard | A team metrics viewer |
| Marketplace | Web App | A freelancer booking platform |

## Complexity Signals

Upgrade complexity estimate if the project includes:
- User authentication and accounts → +1 level
- Payments or billing → +1 level
- Real-time features (chat, notifications) → +1 level
- Two or more user roles with different permissions → +1 level
- Third-party API integrations → +0.5 level
- Mobile support in addition to web → +1 level

Use complexity to anchor the MVP scope — higher complexity means a tighter MVP is needed.
