---
aliases: [Financial data providers, Financial data and index providers, Data toll roads, Index and ratings providers, Financial information services]
tags: [concept, financials, data, market-structure, cluster-validation]
---

# Financial data providers

The capital markets' "data toll roads" — [[S&P Global]] (SPGI), [[Moody's]] (MCO), [[MSCI]] (MSCI), [[FactSet]] (FDS), [[Thomson Reuters]] (TRI), [[RELX]] (RELX), [[Morningstar]] (MORN). Index licensing, credit ratings, analytics, and data terminals, priced on assets-under-management and seats rather than transaction volume — the recurring-subscription side of market infrastructure. This note owns the cohort's cluster validation, and it closes the loop from the [[Exchange operators]] falsification: the two exchanges that "left" the exchange factor ([[Intercontinental Exchange]], [[Nasdaq]]) land here.

> [!success] Cluster status: validated — a distinct data factor that absorbs the data-pivoted exchanges (June 2026)
> The seven data providers form a real cluster: intra-corr 0.607 (0.701 on weekly returns, correcting for the London/Toronto listings), PC1 66.5%, rejecting the independence, random-basket and vol-matched nulls at the 0.0001 floor. It is overwhelmingly distinct from the transaction/volatility exchanges ([[CME Group]]/[[CBOE]], intra-advantage +0.554 — the widest business-model gap in the cohort batch) and from broad financials (+0.337). The defining finding: the cluster's natural membership extends to [[Nasdaq]] (joins from threshold 0.40) and [[Intercontinental Exchange]] (from 0.55) — the data-pivoted exchanges are members of the data factor, not the exchange factor. This is the constructive counterpart to [[Exchange operators]]: "exchanges" failed to cluster precisely because ICE and Nasdaq defected to this cohort, which validates with them in it. Cohesion is off its 2024–25 peak (holdout WEAKENED 0.82) but the factor structure is durable (loadings correlation 0.91). See below.

The cohort is bound by a shared revenue model, not a sector label: recurring, contractual, price-escalating subscriptions to indices, ratings, and analytics. That is why it draws in [[Nasdaq]] (index + anti-financial-crime SaaS + market data) and [[Intercontinental Exchange]] (ICE Data Services, mortgage technology) while excluding the transaction venues whose revenue scales with volume.

## Cluster validation

### Diagnostics summary

| Diagnostic | Value | Read |
|---|---|---|
| Intra-cluster corr (1Y) | 0.607 [0.425–0.885] | Single factor; weekly 0.701 (async-corrected) |
| PC1 explained variance | 66.5% (PC2 11.0%) | Dominant-factor; weekly 75.0% |
| Random-basket p (10k) | 0.0001 | Beats random 7-picks at the floor |
| Vol-matched p (10k) | 0.0001 | Real factor, not shared vol |
| Holdout ratio (2Y split) | 0.82 — WEAKENED | Train 0.744 / test 0.607; loadings corr 0.91 (durable structure, off the 2024–25 peak) |
| Threshold clean band | 0.00 | [[Nasdaq]] joins from 0.40, [[Intercontinental Exchange]] from 0.55 — the cohort extends, it does not fragment |
| Intra-adv vs derivatives ([[CME Group]]/[[CBOE]]) | +0.554 | Overwhelmingly distinct — data is not transaction/volatility |
| Intra-adv vs ICE/NDAQ | +0.096 | Not distinct — they are members |
| Intra-adv vs [[SPY]]/[[XLF]] | +0.337 | Distinct from broad financials |

1Y daily log returns through 2026-06-12, threshold 0.5. Cross-region cohort ([[RELX]] London, [[Thomson Reuters]] Toronto/NYSE) — the weekly cross-check (0.701 vs daily 0.607) is the better co-movement estimate. Config: `scripts/cluster_configs/financial_data.yaml`; registry row 2026-06-14. Terminology: [[Cohort, cluster, basket]].

### Boundary — the cluster absorbs the data-pivoted exchanges

![[financial-data-cluster-dendrogram-1y.png]]
*Hierarchical clustering at 0.5. The seven data providers cluster together with [[Nasdaq]]; [[Intercontinental Exchange]] sits on the boundary (joins at 0.55); the transaction exchanges [[CME Group]]/[[CBOE]] form a cold, separate pair, and the market ETFs a third cluster. The split is business-model, not sector: ICE and Nasdaq trade as data companies.*

The threshold scan returns zero clean width — but the contaminant is [[Nasdaq]] (from 0.40), then [[Intercontinental Exchange]] (from 0.55), not a foreign sector. The cohort cannot be isolated from NDAQ because NDAQ belongs in it. This is the same "extends, not fragments" signature as the [[Defense IT Services|KBR boundary]], and the mirror image of [[Exchange operators]], where the same two names contaminated the exchange cohort from the other side.

### Topology — a ratings/index core and two satellite pairs

| Join step | Names | Distance (1-\|corr\|) | Read |
|---|---|---|---|
| 1 | SPGI + MCO | 0.115 | The ratings/index core — S&P Global / Moody's, the tightest pair |
| 2 | FDS + MORN | 0.240 | Analytics / data-terminal pair (FactSet / Morningstar) |
| 3 | + MSCI | 0.287 | MSCI joins the ratings/index core |
| 4 | TRI + RELX | 0.374 | Diversified info-services pair (Thomson Reuters / RELX) |
| 5 | (FDS+MORN) + (MSCI+SPGI+MCO) | 0.404 | Analytics joins the core |
| 6 | + (TRI+RELX) | 0.453 | The diversified names join last — the loosest members |

The tight core is [[S&P Global]] + [[Moody's]] (0.115), with [[MSCI]] adjacent — the index/ratings oligopoly. [[FactSet]]/[[Morningstar]] (analytics) and [[Thomson Reuters]]/[[RELX]] (diversified legal/news/scientific information) attach as satellite pairs; TRI and RELX join last (0.453), the least-pure members given their non-financial revenue.

### PC1 index weights

![[financial-data-cluster-pca-1y.png]]
*PCA scree and PC1 loadings. PC1 explains 66.5% with positive, fairly even loadings (0.35–0.42); [[S&P Global]] and [[Moody's]] load highest, [[RELX]]/[[Thomson Reuters]] lowest (their diversified revenue dilutes the financial-data factor).*

| Ticker | PC1 loading | Loading weight | Ann vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| SPGI | 0.417 | 15.8% | 29.7% | 18.0% |
| MCO | 0.405 | 15.3% | 27.6% | 18.8% |
| MSCI | 0.355 | 13.4% | 28.1% | 16.2% |
| FDS | 0.380 | 14.4% | 43.9% | 11.1% |
| TRI | 0.353 | 13.3% | 46.8% | 9.7% |
| RELX | 0.350 | 13.3% | 34.0% | 13.2% |
| MORN | 0.382 | 14.5% | 37.5% | 13.1% |

The PC1-mimic basket concentrates in the low-volatility bellwethers [[Moody's]] (18.8%) and [[S&P Global]] (18.0%) and underweights the high-vol diversified names [[Thomson Reuters]] (9.7%, 47% vol) — to reproduce the standardized data factor in raw returns you lean on the calm ratings duopoly.

### Distinctness

![[financial-data-cluster-correlation-1y.png]]
*1Y pairwise correlation heatmap. The data block (plus NDAQ) is uniformly warm; the derivatives pair CME/CBOE is cold against it (group-pair correlation 0.052) — the cleanest separation in the heatmap.*

### Historical tightness evolution

![[financial-data-cluster-rolling-tightness-90d.png]]
*Rolling 90-day cohesion. The cluster is durable — a 2023 peak (0.688), a 2024 trough (0.509), and a recovery into 2025–26 — never breaking below ~0.51. The recurring-revenue factor is structurally persistent, with regime-driven amplitude.*

| Window | Avg intra-corr | PC1 | Final join distance |
|---|---|---|---|
| 2023 | 0.688 | 73.4% | 0.375 |
| 2024 | 0.509 | 58.3% | 0.558 |
| 2025 | 0.651 | 70.8% | 0.488 |
| Latest 90d | 0.588 | 65.1% | 0.490 |

*Durable factor, regime amplitude: the 0.91 loadings correlation across the holdout split confirms the same factor structure persists; the WEAKENED ratio (0.82) reflects that the 2024–25 window was unusually tight (0.744), not that the cohort is fragmenting.*

### The read-through

- A real, investable data-toll-road factor. Recurring subscription revenue (index licensing, ratings, analytics, terminals) is its own return factor, distinct from broad financials (+0.337) and from transaction exchanges (+0.554). The tradeable core is [[S&P Global]]/[[Moody's]]/[[MSCI]]; [[FactSet]]/[[Morningstar]] and [[Thomson Reuters]]/[[RELX]] are satellite legs.
- This cohort is [[Nasdaq]] and [[Intercontinental Exchange]]'s home. They cluster here, not with the exchanges — the constructive answer to why [[Exchange operators]] falsified. A position thesis on "exchanges" should split: CME/CBOE on the transaction factor, ICE/NDAQ on this data factor.
- The derivatives gap is the cleanest split in the batch. Cohort-vs-CME/CBOE correlation is 0.052; data and transaction venues share a regulator and a customer base but essentially no return factor.

Method and terminology: `docs/cluster-validation.md`, [[Cohort, cluster, basket]], [[Vault cluster taxonomy]]. Post-definition OOS re-validation is queued for the next quarterly pass (definition date 2026-06-14).

## Related

- [[Exchange operators]] — the falsified sibling; ICE and Nasdaq's defection to this cohort is why "exchanges" is not a cluster
- [[Vault cluster taxonomy]] — cross-cohort comparison and verdict thresholds
- [[S&P Global]], [[Moody's]], [[MSCI]], [[FactSet]], [[Thomson Reuters]], [[RELX]], [[Morningstar]] — the seven members
- [[Cohort, cluster, basket]] — terminology

*Created 2026-06-14.*
