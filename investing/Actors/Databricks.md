---
aliases: []
---
#actor #ai #data #usa #private

**Databricks** — [[Data lakehouse]] + AI. $134B valuation. $4.8B ARR. IPO expected 2026. "Fastest enterprise software growth."

---

## Why Databricks matters

Largest private enterprise software company, AI infrastructure critical:

| Metric | Value |
|--------|-------|
| Valuation | $134B (Dec 2025) |
| ARR | $4.8B |
| Growth | 55% YoY |
| IPO | Expected early 2026 |

---

## Cap table / Investors

| Round | Date | Amount | Valuation |
|-------|------|--------|-----------|
| Series A | 2013 | $14M | — |
| Series B | 2014 | $33M | — |
| Series C | 2016 | $60M | — |
| Series D | 2017 | $140M | — |
| Series E | 2019 | $250M | $2.75B |
| Series F | 2019 | $400M | $6.2B |
| Series G | 2021 | $1B | $28B |
| Series H | 2023 | $500M | $43B |
| Series I | 2024 | $500M | $55B |
| Series J | Aug 2025 | — | $100B |
| Series L | Dec 2025 | $4B+ | $134B |
| Total | | $10B+ | |

Source: [Databricks / PRNewswire, Dec 16 2025](https://www.prnewswire.com/news-releases/databricks-grows-55-yoy-surpasses-4-8b-revenue-run-rate-and-is-raising-4b-series-l-at-134b-valuation-302643445.html); [Reuters via Investing.com, Dec 16 2025](https://www.investing.com/news/stock-market-news/data-analytics-firm-databricks-valued-at-134-billion-in-latest-funding-round-4410737).

Key investors:

| Investor | Notes |
|----------|-------|
| [[a16z]] | Multiple rounds |
| [[Insight Partners]] | Series L lead |
| [[Thrive Capital]] | Growth |
| [[Tiger Global]] | Growth |
| [[Blackstone]] | Growth |
| [[Fidelity]] | Crossover |
| [[T. Rowe Price]] | Crossover |
| JPMorgan Asset Management | Growth |
| [[Franklin Templeton]] | Growth |

Total raised: $10B+

---

## Revenue breakdown

$4.8B ARR composition:

| Product | ARR |
|---------|-----|
| Data Warehousing | $1B+ |
| AI Products | $1B+ |
| Core Platform | Rest |

FCF positive over last 12 months.

---

## Customer base

60%+ of Fortune 500:
- adidas
- [[AT&T]]
- Bayer
- [[Block]]
- [[Mastercard]]
- [[Rivian]]
- [[Unilever]]

20,000+ organizations worldwide.

---

## Acquisitions

### Neon (May 2025)

| Detail | Value |
|--------|-------|
| [[Target]] | [[Neon]] |
| Price | ~$1B |
| What | Serverless [[Postgres]] |
| Rationale | [[AI agents]] need simple DB provisioning |

Why it matters: 80%+ of Neon databases created by [[AI agents]]. Databricks + Neon = complete data platform for AI applications.

Post-acquisition: Neon cut prices 15-25% (compute), storage from $1.75 to $0.35/GB-month.

---

## AI strategy

Model integration deals:
- [[Anthropic]] — multi-hundred million
- [[OpenAI]] — multi-hundred million
- Models available within Databricks products

AI products:
- Lakebase (system of record)
- Databricks Apps (user experience)
- Agent Bricks (multi-agent systems)
- [[Neon]] — serverless [[Postgres]] (acquired)

---

## Open governance & standards

Databricks' answer to the catalog/semantic layer is the mirror image of [[Snowflake]]'s standard-setting — absorb governance into the platform and open-source the interface so no standalone vendor owns it:

- Unity Catalog — its governance/catalog layer for data, ML and AI assets, fully open-sourced June 4, 2024 (Data + AI Summit) on the OpenAPI spec with an open-source server, multi-format and multi-engine. The warehouse-pulls-the-catalog-inward move that erodes standalone catalog vendors; also named as a future export source for Google's [[Open Knowledge Format]].
- Tabular — announced the same day (June 4, 2024), Databricks acquired the team behind Apache Iceberg (the open table format) for a reported $1–2 billion, the open-table-format leg of the [[Snowflake]] rivalry.
- [[Open Semantic Interchange]] — Databricks is a member of [[Snowflake]]'s OSI semantic-model consortium; like the catalog incumbents, it joined the standard rather than fight it.

Read-through: Databricks and [[Snowflake]] are converging on the same play from opposite origins (lakehouse vs warehouse) — pull governance and semantics into the platform, commoditize the interchange (open-source or consortium), and compete on the serving layer. Both screen as warehouse-side beneficiaries in [[Data catalog disruption]], where the value released by commoditizing standalone catalogs accrues to whoever owns the data-plus-serving plane.

---

## IPO outlook

Expected early 2026:
- CEO Ali Ghodsi: "Still deciding when"
- Likely [[Nasdaq]] listing
- Traditional IPO expected
- Would be one of largest tech IPOs

---

## Competitive landscape

| Company | Focus | Databricks vs |
|---------|-------|---------------|
| [[Snowflake]] | Data warehouse | Lakehouse = unified |
| [[Palantir]] | AI applications | More infrastructure |
| AWS/Azure/GCP | Cloud data | Multi-cloud |

Databricks = [[Switzerland]] of data (runs on all clouds).

---

## Founding

Apache Spark origins:
- Founded 2013
- Founders created Apache Spark at Berkeley
- Open-source roots
- Ali Ghodsi (CEO)

---

## Investment case

Bull:
- $134B but still growing 55%
- AI infrastructure essential
- Model-agnostic (Anthropic, OpenAI)
- FCF positive
- IPO catalyst

Bear:
- Valuation requires perfection
- Cloud provider competition
- Snowflake competition
- Public market reception unknown

---

## Quick stats

| Metric | Value |
|--------|-------|
| Ticker | Private (IPO 2026) |
| Valuation | $134B |
| ARR | $4.8B |
| Growth | 55% YoY |
| CEO | Ali Ghodsi |

*Updated 2026-01-01*

---

## Related

- [[Neon]] — acquired (serverless [[Postgres]], $1B)
- [[Data catalog disruption]] — warehouse-side beneficiary thesis (Unity Catalog OSS + OSI membership)
- [[Open Semantic Interchange]] — the semantic-model consortium Databricks joined
- [[Snowflake]] — competitor (data warehouse)
- [[Palantir]] — competitor (AI applications)
- [[Anthropic]] — partner (models on platform)
- [[OpenAI]] — partner (models on platform)
- [[Supabase]] — competitor ([[Postgres]] BaaS)
- [[a16z]] — investor
- [[Tiger Global]] — investor
- [[Blackstone]] — investor
