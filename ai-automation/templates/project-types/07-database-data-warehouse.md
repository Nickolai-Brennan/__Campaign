# Project Template — Database / Data Warehouse

Use this template when initializing a **Database / Data Warehouse** project (schema design, migrations, query layer). Answer every question and save the completed file as `PROJECT.md` at the root of your repository.

---

## Section 1: Project Type

**Primary Type**: Database / Data Warehouse  
**Secondary Types**: <!-- e.g. Data Pipeline, API -->

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

**3.1 — What specific problem does this database or data warehouse solve?**

> **Answer**:

**3.2 — What is the single most important outcome this project must deliver?**

> **Answer**:

**3.3 — List up to three secondary goals.**

1.
2.
3.

---

## Section 4: Audience

**4.1 — Who are the primary consumers of this data store?**
*(e.g. application services, data analysts, BI tools, data scientists)*

> **Answer**:

**4.2 — Who are secondary beneficiaries?**

> **Answer**:

**4.3 — Who are the stakeholders?**

> **Answer**:

**4.4 — What is the expected query or connection scale?**
*(e.g. "500 concurrent connections", "1,000 queries/sec")*

> **Answer**:

---

## Section 5: Technical Stack

**5.1 — What database engine(s) are used?**
*(e.g. PostgreSQL, MySQL, MongoDB, Cassandra, BigQuery, Snowflake, DuckDB)*

> **Answer**:

**5.2 — What query language or ORM is used?**
*(e.g. SQL, GraphQL, Prisma, SQLAlchemy, TypeORM)*

> **Answer**:

**5.3 — What migration tool is used?**
*(e.g. Flyway, Liquibase, Alembic, Prisma Migrate, Rails ActiveRecord, none)*

> **Answer**:

**5.4 — What data transformation layer is used, if any?**
*(e.g. dbt, Spark, stored procedures, none)*

> **Answer**:

**5.5 — What AI/ML models or vector search is used, if any?**
*(e.g. pgvector, Pinecone, Weaviate)*

> **Answer**:

**5.6 — What cloud or infrastructure platform hosts this data store?**
*(e.g. RDS, Cloud SQL, Supabase, PlanetScale, self-hosted)*

> **Answer**:

**5.7 — What CI/CD tooling is used for schema changes?**

> **Answer**:

**5.8 — How is access control handled?**
*(e.g. database roles, row-level security, VPC, IAM)*

> **Answer**:

---

## Section 6: Schema & Data Design

**6.1 — What is the primary data modeling approach?**
*(e.g. relational/3NF, star schema, wide table, document model, time-series, graph)*

> **Answer**:

**6.2 — What are the primary entities or tables?**

> **Answer**:

**6.3 — What indexing strategy is used?**
*(e.g. B-tree primary keys, composite indexes, full-text search, vector indexes)*

> **Answer**:

**6.4 — What partitioning or sharding strategy is used, if any?**

> **Answer**:

**6.5 — What backup and recovery strategy is in place?**
*(e.g. daily snapshots, WAL archiving, point-in-time recovery, RPO/RTO targets)*

> **Answer**:

**6.6 — What replication or high-availability setup is used?**
*(e.g. primary-replica, multi-region, active-active)*

> **Answer**:

---

## Section 7: Data Profile

**7.1 — What data enters the system (sources / loaders)?**

> **Answer**:

**7.2 — What data is read from the system (consumers / reports)?**

> **Answer**:

**7.3 — What is the data sensitivity level?**
Choose one: `public` · `internal` · `confidential` · `restricted`

> **Answer**:

**7.4 — Does the project handle PII or PHI?**
Choose one: `true` · `false`

> **Answer**:

**7.5 — What is the data retention and archival policy?**

> **Answer**:

**7.6 — What is the expected data volume?**
*(e.g. "500 GB initial, growing 10 GB/month", "5 TB warehouse")*

> **Answer**:

---

## Section 8: Architecture

**8.1 — Describe the high-level data architecture in 2–5 sentences.**

> **Answer**:

**8.2 — Is there an entity-relationship (ER) or data model diagram? Provide a link or file path.**

> **Answer**:

---

## Section 9: Constraints

**9.1 — What is the budget or cost target?**

> **Answer**:

**9.2 — What is the target delivery date or migration deadline?**

> **Answer**:

**9.3 — What compliance or regulatory requirements apply?**
*(e.g. GDPR right-to-erasure, HIPAA encryption at rest, SOC 2)*

> **Answer**:

**9.4 — What is the read/write performance SLA?**
*(e.g. "OLTP reads < 5 ms", "OLAP queries < 30 s")*

> **Answer**:

**9.5 — What is the availability / uptime target?**

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
| `schema/` or `migrations/` | Schema definitions and migration scripts |
| | |
| | |
