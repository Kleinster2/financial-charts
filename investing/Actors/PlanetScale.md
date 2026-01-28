# PlanetScale

#actor #startup #private #usa #database

**PlanetScale** — Serverless MySQL platform built on Vitess. Founded 2018. **$1B valuation (Oct 2025), $105M raised.** Created Vitess (powers YouTube, [[Slack]], Square). Competitor to [[Neon]] (MySQL vs Postgres). Non-blocking schema changes, horizontal sharding.

---

## Key facts

| Metric | Value |
|--------|-------|
| Founded | 2018 |
| HQ | San Francisco, CA |
| Valuation | **$1B** (Oct 2025) |
| Total raised | $105M |
| Revenue | $3.9M (Oct 2024) |

---

## Financials

### Revenue

| Period | Revenue | Growth |
|--------|---------|--------|
| Oct 2023 | $1.9M | — |
| Oct 2024 | $3.9M | ~105% YoY |

Still early-stage revenue relative to valuation — growth-stage bet.

---

## Cap table

### Funding rounds

| Round | Date | Amount | Valuation | Lead |
|-------|------|--------|-----------|------|
| Series D | Oct 2025 | $80M | $1B | [[Insight Partners]], [[Kleiner Perkins]] |
| Series C | Nov 2021 | $50M | — | [[Kleiner Perkins]] |
| Earlier | 2018-2021 | $25M | — | Various |

**Total raised: $105M**

### Key investors

| Investor | Notes |
|----------|-------|
| [[Insight Partners]] | Series D co-lead |
| [[Kleiner Perkins]] | Series C, D |
| DIG Ventures | Early investor |
| Start Smart Labs | Early investor |
| [[a16z]] | Participant |

---

## Product

### Core technology: Vitess

PlanetScale is built on **Vitess**, an open-source MySQL sharding solution:

| Metric | Value |
|--------|-------|
| Origin | Created at YouTube (2010) |
| Users | YouTube, [[Slack]], Square, GitHub |
| Maintainer | PlanetScale team |

Vitess enables horizontal scaling of MySQL — critical for high-traffic applications.

### Key features

| Feature | Benefit |
|---------|---------|
| **Non-blocking schema changes** | Deploy schema updates without downtime |
| **Horizontal sharding** | Scale beyond single-node limits |
| **Branching** | Git-like workflow for database changes |
| **Serverless** | Scale to zero, usage-based pricing |

### MySQL vs Postgres

| Dimension | PlanetScale (MySQL) | [[Neon]]/[[Supabase]] (Postgres) |
|-----------|---------------------|----------------------------------|
| Ecosystem | Huge legacy install base | Growing, modern preference |
| Sharding | Vitess (proven at YouTube scale) | Less mature |
| JSON support | Weaker | Stronger (JSONB) |
| Extensions | Limited | Rich (pgvector, PostGIS, etc.) |

---

## Competitive landscape

| Competitor | Positioning |
|------------|-------------|
| [[Neon]] | Serverless Postgres (acquired by [[Databricks]]) |
| [[Supabase]] | Postgres BaaS (full stack) |
| AWS [[Aurora]] | Managed MySQL/Postgres |
| TiDB | Distributed MySQL-compatible |
| CockroachDB | Distributed Postgres-compatible |

**Key distinction:** PlanetScale is MySQL-native with Vitess sharding expertise. Best for teams committed to MySQL ecosystem.

---

## Challenges

| Challenge | Detail |
|-----------|--------|
| **Postgres momentum** | Developer preference shifting to Postgres |
| **Neon acquisition** | [[Databricks]] backing gives Neon scale advantages |
| **Revenue scale** | $3.9M revenue at $1B valuation = high multiple |
| **Free tier removal** | Removed free tier in 2024, caused community backlash |

---

## Related

- [[Neon]] — direct competitor (Postgres equivalent)
- [[Supabase]] — competitor (full BaaS)
- [[Databases]] — sector context
- [[Postgres]] — competing database technology
- [[Tom Preston-Werner]] — angel investor

---

Sources:
- [PitchBook - PlanetScale profile](https://pitchbook.com/profiles/company/234930-61)
- [TechCrunch - Series C](https://techcrunch.com/2021/11/16/planetscale-raises-50m-series-c/)
- [Getlatka - Revenue data](https://getlatka.com/companies/planetscale)

*Created 2026-01-14*
