---
aliases: [Agricultural equipment, Ag equipment, Farm equipment, Farm machinery, Ag machinery, Agricultural machinery]
tags: [sector, industrial, agricultural-equipment, cluster-validation]
---

# Agricultural equipment

> [!warning] Cluster status: real cohesion but ETF-replicable — the farm-machinery majors co-move, but they ARE the agribusiness ETF [[MOO]] (which holds them) and are barely distinct from industrials [[XLI]]; not a separable factor (Jun 2026)
> The farm-machinery names ([[Deere|DE]]/[[AGCO]]/[[CNH Industrial|CNH]]/[[Lindsay|LNN]]) form a real but ETF-embedded cohort. The three majors cohere (DE/AGCO/CNH 0.68–0.74; cohort intra 0.600, weekly 0.586, PC1 70.4%) and reject all three nulls solidly (random-basket and vol-matched at 0.0004), with a durable factor structure (holdout loadings-corr 0.855). But there is no clean threshold band ("boundary-dependent"): [[MOO]] — the agribusiness ETF that holds [[Deere|DE]]/[[AGCO]]/[[CNH Industrial|CNH]] at top weight — contaminates the cluster from 0.45, so the majors never separate from it; and the cohort is only +0.057 over industrials [[XLI]] (barely tighter than the broad sector). Two clean reads: (1) ag equipment is an agribusiness-EQUITY / industrial factor, NOT the ag-commodity trade — [[DBA]] (crop futures) sits far apart (+0.379 vs the ag-complex average, which DBA drags down); and (2) [[Lindsay|LNN]] (irrigation, a different sub-segment) is the loose outlier (corr 0.42–0.56, joins at 0.501). Own [[MOO]] (or [[XLI]]); the bespoke basket adds little. See below.

The picks-and-shovels of farming that trade as agribusiness equity. [[Deere|DE]], [[AGCO]], and [[CNH Industrial|CNH]] sell tractors, combines, and precision-ag systems into a shared farm-income / ag-capex cycle (crop prices, farmer cash flow, fleet replacement), which gives them a genuine common factor. But that factor is exactly what the agribusiness ETF [[MOO]] is built on — the three majors are MOO's largest equity holdings — so they cannot separate from it, and as classified industrials they sit close to [[XLI]] too. The result is real cohesion with no distinct, ownable factor beyond the ETF.

## Sector performance

![[ag-equipment-performance.png]]
*Normalized total return since Jan 2023, the four names vs the agribusiness ETF [[MOO]]. The three majors ([[Deere|DE]]/[[AGCO]]/[[CNH Industrial|CNH]]) track MOO closely — because they ARE its top holdings — which is the ETF-replicable verdict made visible; [[Lindsay|LNN]] (irrigation) diverges on its own water/infrastructure story.*

## Cluster validation

The candidate cohort is four agricultural-equipment makers — [[Deere|DE]] (the diversified leader), [[AGCO]] (pure-play tractors/precision ag), [[CNH Industrial|CNH]] (Case IH/New Holland), [[Lindsay|LNN]] (irrigation) — tested against construction equipment ([[Caterpillar|CAT]]), industrials ([[XLI]]), the ag complex ([[MOO]] agribusiness equity, [[DBA]] crop futures), and the market (SPY). 1Y window through 2026-06-18 (198 obs), threshold 0.5. Terminology: [[Cohort, cluster, basket]].

### Diagnostics summary

| Diagnostic | Value | Read |
|---|---|---|
| Intra-cluster corr (1Y) | 0.600 [0.425–0.745] | Moderately tight; weekly 0.586; the 3 majors 0.68–0.74 |
| PC1 explained variance | 70.4% | A single factor (weekly 69.9%) |
| Independence null p (10k) | 0.0001 | Series co-move |
| Random-basket null p (10k) | 0.0004 | A real factor, beyond a random 4-pick |
| Vol-matched null p (10k) | 0.0004 | Real beyond shared vol |
| Holdout (2Y split) | WEAKENED 0.75; loadings-corr 0.855 | train 0.797 → test 0.600 — durable structure, eroding level |
| Threshold stable width | 0.00 (none) | MOO contaminates from 0.45 — never a clean standalone cluster |
| Intra-adv vs industrials (XLI) | +0.057 | ≈ industrials — barely tighter than the broad sector |
| Intra-adv vs construction (CAT) | +0.099 | Modestly distinct from construction equipment |
| Intra-adv vs ag complex (MOO/DBA) | +0.379 | Misleading average — DBA (futures) is far off; MOO captures them |

Config: `scripts/cluster_configs/ag_equipment.yaml`; registry row 2026-06-22.

### Boundary — the majors sit inside the agribusiness ETF

![[ag-equipment-cluster-dendrogram-1y.png]]
*Hierarchical clustering at 0.5. The three majors {[[Deere|DE]]/[[AGCO]]/[[CNH Industrial|CNH]]} cluster WITH [[MOO]] (green) — the agribusiness ETF holds them at top weight, joining at ~0.44. Construction [[Caterpillar|CAT]] sits with industrials [[XLI]]/SPY (orange); the ag and industrial blocks merge just above the cut (~0.53). [[Lindsay|LNN]] (irrigation) is a far outlier; [[DBA]] (crop futures) is further still — ag equipment is not the ag-commodity trade.*

The threshold scan returns no clean band — [[MOO]] joins the cohort's cluster from 0.45, so the majors never form an uncontaminated standalone cluster:

| Threshold | Joins the cohort cluster | Read |
|---|---|---|
| 0.45–0.50 | MOO | the agribusiness ETF contaminates immediately — it holds the majors |
| 0.55+ | (industrial/ag complex) | merges with XLI/CAT |

That MOO contaminates from 0.45 — combined with only +0.057 over XLI — is the ETF-replicable signature: the names are a real cohort, but the cohort IS the agribusiness/industrial ETF.

### Topology — three tight majors, an irrigation outlier

Reading the candidate cohort by join distance (average linkage, 1−|corr|):

| Join step | Names | Distance (1-\|corr\|) | Read |
|---|---|---|---|
| 1 | AGCO + CNH | 0.255 | the tightest pair (corr 0.74) — pure-play farm machinery |
| 2 | DE + (AGCO+CNH) | 0.320 | Deere joins — the majors core |
| 3 | LNN + core | 0.501 | [[Lindsay\|LNN]] (irrigation) joins last, at the cut — the outlier |

The three majors close by 0.320; [[Lindsay|LNN]] (corr 0.42–0.56) only at 0.501 — its irrigation/infrastructure mix decouples it from the tractor/combine cycle. PC1 explains 70.4%.

### PC1 index weights — an even cohort

![[ag-equipment-cluster-pca-1y.png]]
*PCA on the candidate cohort. PC1 explains 70.4% with fairly even loadings (0.43–0.54); [[Lindsay|LNN]] loads lowest (0.43). Vols are uniform (~30–37%).*

| Ticker | PC1 loading | Loading weight | Ann vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| DE | 0.499 | 25.03% | 30.59% | 26.79% |
| AGCO | 0.537 | 26.93% | 32.62% | 27.02% |
| CNH | 0.527 | 26.44% | 37.30% | 23.20% |
| LNN | 0.431 | 21.60% | 30.76% | 22.99% |

### Distinctness — captured by MOO, close to XLI, not the crop trade

![[ag-equipment-cluster-correlation-1y.png]]
*1Y pairwise correlation heatmap. The three majors run warm (0.68–0.74); [[Lindsay|LNN]] is cooler; the cohort runs warm against MOO and XLI and cold against DBA (crop futures).*

The intra-advantage numbers locate it: only +0.057 over industrials ([[XLI]]) — the names are essentially industrial beta — and +0.099 over construction ([[Caterpillar|CAT]]). The headline +0.379 over the "ag complex" is an artifact of averaging [[MOO]] (which holds and tracks the majors) with [[DBA]] (crop futures, nearly uncorrelated) — against MOO alone the cohort does not separate (MOO contaminates from 0.45). The structural read: ag equipment is agribusiness EQUITY — it moves with farm income and the ag-capex cycle that [[MOO]] prices, not with the crop-commodity price ([[DBA]]). There is no pure ag-equipment ETF, but [[MOO]] (agribusiness) and [[XLI]] (industrials) both capture the factor, so the basket adds little.

### Historical tightness evolution — moderately durable, cyclical

![[ag-equipment-cluster-rolling-tightness-90d.png]]
*Rolling 90-day cohesion, 2021–2026. Moderately durable — 0.51–0.73, dipping to 0.51 in 2024 and peaking at 0.73 in 2025 (the farm-downturn synchronization), currently 0.59. The factor is real and persistent; it just never separates from the agribusiness/industrial ETFs.*

| Year | Avg intra-corr | PC1 |
|---|---|---|
| 2021 | 0.608 | 71.0% |
| 2022 | 0.610 | 71.4% |
| 2023 | 0.646 | 74.3% |
| 2024 | 0.512 | 65.0% |
| 2025 | 0.726 | 79.8% |
| 2026 | 0.611 | 71.2% |

*Real and reasonably durable (0.51–0.73) — the farm-income cycle keeps the majors co-moving — but that is exactly the agribusiness factor [[MOO]] is built on.*

## Where this sits in the campaign

Agricultural equipment is another "real but ETF-embedded" industrial cohort:

- It is captured by [[MOO]] (agribusiness equity) the way [[WFE]] is captured by [[SMH]], the [[Mortgage REITs|mREITs]] by [[REM]], and the regional banks by KRE — a genuine factor that never separates from the ETF that holds it.
- The crop-vs-equity split is the instructive part: ag equipment moves on farm income / ag-capex (MOO), not on crop prices ([[DBA]]) — the same lesson as [[Fertilizer producers|fertilizers]] (ag-input equities ≠ the crop trade) and the broader commodity-equity-beta family.
- It contrasts with the campaign's distinct industrials ([[Railroads]], [[Solid waste]], [[Tankers]]), which carry a driver no sector ETF prices; ag equipment's driver (the ag-capex cycle) is exactly what MOO is built on.

## Related

- [[Deere]], [[AGCO]], [[CNH Industrial]], [[Lindsay]] — the cohort members (DE/AGCO/CNH the machinery core; LNN the irrigation outlier)
- [[MOO]] — the agribusiness ETF that holds and captures the majors (own this); [[XLI]] — industrials (the cohort is barely tighter); [[DBA]] — crop futures (ag equipment is NOT this); [[Caterpillar]] — construction-equipment comparison
- [[Fertilizer producers]] — the other ag-input cohort (also not the crop trade); [[Vault cluster taxonomy]] — cross-cohort meta-analysis
- [[Cohort, cluster, basket]] — terminology

---

*Created 2026-06-22. 1Y daily log returns through 2026-06-18; config `scripts/cluster_configs/ag_equipment.yaml`; registry row 2026-06-22. Cluster validation is structure, not a performance ranking — see `docs/cluster-validation.md`.*
