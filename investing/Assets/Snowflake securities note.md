---
aliases: [SNOW stock, Snowflake securities, Snowflake stock]
tags: [securities, software, ai, usa]
ticker: SNOW
---
#securities

Snowflake securities — NYSE: SNOW, single-class common since July 3, 2025 (all Class B super-voting shares eliminated; Class A renamed common stock). Equity-market note for [[Snowflake]]: the May 27, 2026 Q1 FY27 print converted a two-year consumption-derate story into an enterprise-AI control-plane rerating — +36.5% in one session on reaccelerated growth and raised guides — against a balance sheet whose live question is dilution (stock comp plus converts), not credit.

---

## Quick stats

| Metric | Value |
|--------|-------|
| Exchange / ticker | NYSE: SNOW |
| Share structure | Single-class common (Class B eliminated Jul 3, 2025) |
| Close (2026-06-11) | $240.39 |
| Market cap | ~$83B (~346M weighted shares) |
| IPO | Sept 16, 2020 at $120 — largest software IPO at the time |
| All-time high | $401.89 (Nov 2021) |
| Debt | $2.3B convertible senior notes (FY2025 issuance; $195.5M capped calls); no agency ratings disclosed |

---

## Price

![[snow-vs-pltr-ddog-mdb-price-chart.png]]
*SNOW (blue) vs [[Palantir]], [[Datadog]], [[MongoDB]], normalized from June 2024. PLTR's +450-800% band is the GAAP-profitability premium the rest of the cohort lacks. The data-infrastructure trio — SNOW, DDOG, MDB — visibly co-moves, but the Jun-13 Gate-11 validation (Correlation and cluster structure, below) shows that co-movement is a slice of broad software beta, not a separable cluster. SNOW's late-May 2026 vertical is the Q1 FY27 repricing. Log y-axis (normalized returns).*

| Date | Print | Note |
|---|---|---|
| Sept 16, 2020 | IPO $120 | Largest software IPO at the time |
| Nov 2021 | $401.89 | All-time high |
| 2022-2024 | ~$110-230 range | Consumption-slowdown derate |
| May 27, 2026 | $175.26 | Last close before the Q1 FY27 print |
| May 28, 2026 | $239.20 | +36.5% — Q1 FY27 reacceleration (+33% revenue, raised guides, $6B [[Amazon\|AWS]] commitment) |
| Jun 1, 2026 | $280.16 | Post-print closing high |
| Jun 11, 2026 | $240.39 | Settled; ~$83B market cap |

Prices from local `prices_long` closes (4 PM ET).

---

## Correlation and cluster structure

SNOW/[[Datadog|DDOG]]/[[MongoDB|MDB]] surfaced as a separate grouping ("Cluster 2") inside the Jun-12 [[AI SaaS Disruption]] run, so on Jun 13 the trio was validated as its own candidate cohort (`scripts/cluster_configs/snow.yaml`, primary SNOW) against the full Gate-11 suite. The verdict: real but not distinct — a coherent slice of high-multiple software beta, not a separable "consumption data-infra" factor.

![[snow-cluster-dendrogram-1y.png]]
*1Y hierarchical clustering (avg linkage on 1−|corr|). SNOW/DDOG/MDB (blue, right) fuse only at ~0.43-0.46 and then join the seat-software complex (CRM/[[ServiceNow|NOW]]/[[Workday|WDAY]]/[[Atlassian|TEAM]]/[[IGV]], green) at ~0.49 — tighter than where the supposed consumption-infra peers attach ([[Cloudflare|NET]] joins at ~0.58; Elastic (ESTC) sits inside the seat-software cluster). The trio is closer to broad software than to its own thesis.*

| Diagnostic | Value | Reading |
|---|---|---|
| Intra-cohort correlation (1Y) | 0.553 | Moderate — below the 0.6 "coherent sub-sector" bar |
| PC1 explained variance | 70.2% | High, but mechanical at N=3 |
| Random-basket p-value | 0.0026 | PASS — more cohesive than a random 3-pick (null mean 0.16) |
| Holdout stability (test/train) | 0.87 | STABLE — factor structure durable across regimes (loadings corr 0.91) |
| Threshold-scan clean width | 0.00 | FAIL — never a clean standalone cluster at any threshold |

The two failing-vs-passing diagnostics are the whole story: the co-movement is real (permutation) and regime-durable (holdout), but there is no threshold where {SNOW, DDOG, MDB} clusters cleanly — tight enough to exclude seat-software (≤0.45) and the trio doesn't cohere; loose enough to bind it (≥0.50) and CRM/NOW/WDAY/TEAM/ESTC contaminate. The Jun-12 "Cluster 2" was a leftover artifact of a seat-heavy universe (the seat names fused into Cluster 1 first, dropping the trio out together). This is the [[Mag 7 cluster|Mag 7]] signature — passes the random-basket null, killed by zero threshold width.

Legacy pairwise correlations from the actor note: [[IGV]] 0.68, [[XLK]] 0.60, [[SMH]] 0.53, [[SPY]] 0.54. Read-through: SNOW trades as long-duration / high-multiple software beta — co-moving with DDOG/MDB and the wider software complex — not as a distinct data-infrastructure factor.

---

## Dilution mechanics

The equity question is supply, not solvency: $1,599.5M of stock-based compensation in FY2026 (34% of revenue, down from 41-42% the two prior years) plus $2.3B of converts. Weighted average shares grew 332.7M (FY2025) → 337.5M (FY2026) → 345.4M (Q1 FY27) — a ~2-3%/yr drift that GAAP results show and non-GAAP results hide. Full mechanism: the GAAP/SBC wedge section in [[Snowflake]].

---

## Related

### Parent
- [[Snowflake]] — actor note (strategy, financials, the GAAP/SBC wedge)

### Peers / cluster
- [[Datadog]], [[MongoDB]] — co-move with SNOW, but validated as a non-distinct grouping (boundary-dependent; see Correlation and cluster structure)
- [[Palantir]] — profitability-premium contrast
- [[AI SaaS Disruption]] — validated cohort and diagnostics

### Concepts
- [[Data catalog disruption]] — standards-war read-through: SNOW as the cleanest public beneficiary via leading [[Open Semantic Interchange]] (the standard-setter/serving-owner leg of the agentic-control-plane rerating)
- [[Revenue per GW]] — where SNOW's dual-basis margin display got audited

*Created 2026-06-12 (compliance backfill).*
