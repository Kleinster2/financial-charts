# Neon

#actor #startup #usa #database #acquired

**Neon** — Serverless Postgres startup. Founded 2022. **Acquired by [[Databricks]] for ~$1B (May 2025).** Pioneered separation of storage and compute for Postgres. 80%+ of databases created by [[AI agents]]. Key competitor to [[Supabase]] (DB-only vs full BaaS).

---

## Key facts

| Metric | Value |
|--------|-------|
| Founded | 2022 |
| HQ | San Francisco, CA |
| Status | **Acquired by Databricks (May 2025)** |
| Acquisition price | ~$1B |
| Total raised | $104M (pre-acquisition) |

---

## Funding history (pre-acquisition)

| Round | Date | Amount | Lead |
|-------|------|--------|------|
| Seed | 2022 | — | — |
| Series A | 2022 | — | — |
| Series B | 2023 | $46M | Menlo Ventures |
| Strategic | Aug 2024 | $25.6M | M12 ([[Microsoft]]) |

**Total raised: $104M**

### Key investors

| Investor | Notes |
|----------|-------|
| [[Menlo Ventures]] | Series B lead |
| M12 ([[Microsoft]]) | Strategic investment, Azure integration |
| [[Founders Fund]] | Participant |
| [[General Catalyst]] | Participant |
| [[Khosla Ventures]] | Participant |
| [[Snowflake]] Ventures | Participant |
| [[Databricks Ventures]] | Participant (pre-acquisition) |

---

## Product

### Core innovation

**Separation of storage and compute for Postgres** — Neon re-architected Postgres to enable:

| Feature | Benefit |
|---------|---------|
| Serverless scaling | Scale to zero, pay only for usage |
| Branching | Git-like database branches for dev/test |
| Instant provisioning | Spin up databases in seconds |
| Point-in-time recovery | Restore to any moment |

### Why it matters for AI

**80%+ of Neon databases created by [[AI agents]]** — AI coding tools (Bolt.new, [[Lovable]], [[Cursor]]) auto-provision Neon databases. This made Neon attractive to Databricks.

---

## Databricks acquisition (May 2025)

| Detail | Value |
|--------|-------|
| Acquirer | [[Databricks]] |
| Price | ~$1B |
| Date | May 2025 |
| Rationale | [[AI agents]] need simple database provisioning |

**Strategic logic:** Databricks (data lakehouse) + Neon (serverless Postgres) = complete data platform for AI applications. Neon's co-founders are among few who could re-architect Postgres from scratch.

### Post-acquisition changes

| Change | Detail |
|--------|--------|
| Compute costs | Down 15-25% |
| Storage pricing | $1.75 → $0.35/GB-month |
| Free tier | 50 → 100 CU-hours/month |

Databricks using scale to lower prices and drive adoption.

---

## Competitive positioning

| vs | Neon advantage | Neon disadvantage |
|----|----------------|-------------------|
| [[Supabase]] | Serverless scaling, branching | No auth/storage/realtime (DB-only) |
| [[PlanetScale]] | Postgres vs MySQL | Less sharding expertise |
| AWS RDS | Serverless, simpler | Less enterprise features |
| [[Aurora]] Serverless | True separation of storage/compute | AWS ecosystem lock-in |

**Key distinction:** Neon is DB-only; [[Supabase]] is full BaaS. Different use cases.

---

## Related

- [[Databricks]] — acquirer
- [[Supabase]] — competitor (full BaaS vs DB-only)
- [[PlanetScale]] — competitor (MySQL equivalent)
- [[Postgres]] — underlying technology
- [[Databases]] — sector context
- M12 / [[Microsoft]] — strategic investor

---

Sources:
- [Databricks acquisition announcement](https://www.databricks.com/company/newsroom/press-releases/databricks-agrees-acquire-neon-help-developers-deliver-ai-systems)
- [VentureBeat - Series B](https://venturebeat.com/data-infrastructure/neon-raises-46-million-to-advance-serverless-postgresql-database-for-the-ai-era/)
- [VentureBeat - Acquisition analysis](https://venturebeat.com/data-infrastructure/the-1-billion-database-bet-what-databricks-neon-acquisition-means-for-your-ai-strategy/)

*Created 2026-01-14*
