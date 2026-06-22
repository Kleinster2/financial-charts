---
aliases: [Packaged food and beverages, Packaged food, Food and beverages, Staples manufacturers, Food and beverage staples]
tags: [sector, consumer-staples, food, beverages, defensive, usa, cluster-validation]
---

# Packaged food and beverages

> [!warning] Cluster status: real cohesion but loose and not a distinct factor — it IS the broad staples complex (= XLP), and it splits food vs blue-chips (Jun 2026)
> The packaged-food + beverage staples ([[Coca-Cola|KO]]/[[PepsiCo|PEP]]/[[Mondelez|MDLZ]]/[[General Mills|GIS]]/[[Hershey|HSY]]/[[Kraft Heinz|KHC]]) co-move more than chance — intra-corr 0.493 (weekly 0.445), PC1 57.9%, rejecting the random-basket and vol-matched nulls at the floor — but they are not a distinct packaged-food factor. The cohort is only +0.042 distinct from household staples ([[Procter & Gamble|PG]]/[[Colgate-Palmolive|CL]]/[[Kimberly-Clark|KMB]]) and XLP sits inside it: consumer staples is ONE broad defensive complex (= XLP), not a separable food cohort. And it splits: the mid-cap packaged food (MDLZ/GIS/KHC) clusters apart from the mega-cap blue-chips (KO/PEP, which cluster with PG/CL + XLP), with [[Hershey|HSY]] an outlier. Holdout WEAKENED 0.74. Own XLP for the defensive-staples factor; there is no distinct packaged-food basket.

The defensive-staples test, and the third of the campaign's defensive trio. The hypothesis: do the packaged-food and beverage giants form their own factor, the way tobacco does? They do not. Consumer staples trades as one broad low-beta defensive complex — captured by XLP — within which food, beverages, and household products are sub-groups, not separable factors. The mega-cap branded blue-chips (Coca-Cola, PepsiCo, Procter & Gamble, Colgate) are the XLP core; the mid-cap packaged-food names (Mondelez, General Mills, Kraft Heinz) are a looser satellite, dragged by their own GLP-1-volume and private-label pressures.

## Sector performance

![[staples-food-performance.png]]
*Normalized total return since Jan 2023 — the cohort vs [[XLP]] (the sector ETF it is tested against). See the cluster validation below for whether the cohort is distinct from or replicable by the ETF.*

## Cluster validation

The candidate cohort is the six packaged-food + beverage staples — [[Coca-Cola|KO]], [[PepsiCo|PEP]] (beverages), [[Mondelez|MDLZ]], [[General Mills|GIS]], [[Hershey|HSY]], [[Kraft Heinz|KHC]] (packaged food) — tested against household-products staples ([[Procter & Gamble|PG]]/[[Colgate-Palmolive|CL]]/[[Kimberly-Clark|KMB]]) and benchmarks (XLP staples ETF, SPY). 1Y window through 2026-06-18, threshold 0.5. Terminology: [[Cohort, cluster, basket]].

### Diagnostics summary

| Diagnostic | Value | Read |
|---|---|---|
| Intra-cluster corr (1Y) | 0.493 [0.354–0.679] | loose — just below the 0.50 floor; weekly 0.445 |
| PC1 explained variance | 57.9% | moderate (PC2 13%); weekly 53.8% |
| Independence null p | 0.0001 | series co-move |
| Random-basket null p | 0.0001 | beats a random 6-pick — real defensive cohesion |
| Vol-matched null p | 0.0005 | rejects — real beyond shared low vol |
| Holdout (2Y split) | WEAKENED 0.74 | eroding (train 0.622 → test 0.459; loadings corr 0.93 — same structure, looser) |
| Threshold clean width | 0.00 | XLP + household contaminate from 0.55 — embedded in the staples complex |
| Intra-adv vs household staples (PG/CL/KMB) | +0.042 | NOT distinct — food/bev and household are one complex |
| Intra-adv vs ETFs (XLP/SPY) | +0.233 | distinct from SPY (low market beta), but XLP sits inside |

All US-listed (synchronous). Config: `scripts/cluster_configs/ko.yaml`; registry row 2026-06-19.

### Boundary — one staples complex (= XLP); the cohort splits food vs blue-chips

![[staples-food-cluster-dendrogram-1y.png]]
*Hierarchical clustering at 0.5. Orange: the mid-cap packaged food (MDLZ/GIS/KHC). Green: the mega-cap branded blue-chips — beverages KO/PEP + household PG/CL + the staples ETF XLP. The two merge only at ~0.51. [[Hershey|HSY]] and [[Kimberly-Clark|KMB]] are singletons; [[SPY]] is far apart. The proposed food/bev cohort does not hold — beverages cluster with household, not with packaged food.*

The threshold scan never isolates the cohort: below 0.55 it fragments (food vs blue-chip sub-groups), and at 0.55+ household (PG/CL/KMB) and XLP join — so the cohort is embedded in the broad staples complex. Two structural reads. First, consumer staples is ONE factor, not a packaged-food factor: the +0.042 intra-advantage versus household staples is negligible (KO/PEP literally cluster with PG/CL), and XLP is inside — the defensive-staples factor is XLP, full stop. Second, the cohort's internal line is not food-vs-beverage by category but mega-cap-blue-chip vs mid-cap-packaged-food: the largest, most defensive names (KO/PEP/PG/CL — the XLP core) cluster together, while the mid-cap food names (MDLZ/GIS/KHC) form a looser satellite carrying their own volume/margin pressures.

### Topology — a split cohort, HSY the outlier

Reading the candidate cohort by join distance (average linkage, 1−|corr|):

| Join step | Names | Distance (1-\|corr\|) | Read |
|---|---|---|---|
| 1 | GIS + KHC | 0.321 | packaged-food pair |
| 2 | MDLZ + (GIS+KHC) | 0.415 | the mid-cap food sub-group |
| 3 | KO + PEP | 0.461 | the beverage pair (separate) |
| 4 | (food) + (KO+PEP) | 0.518 | food and beverages merge ABOVE the 0.5 cut |
| 5 | HSY + rest | 0.578 | Hershey joins last — the outlier |

The cohort closes only at 0.578, and the food sub-group (MDLZ/GIS/KHC) joins the beverage pair (KO/PEP) only at 0.518 — above the threshold, so at 0.5 they are separate clusters. [[Hershey]] (the single-category confectioner) is the clearest outlier. Against the full set, [[Coca-Cola]] and [[PepsiCo]] cluster with household products and XLP, not with the packaged-food names.

### PC1 index weights

![[staples-food-cluster-pca-1y.png]]
*PCA on the cohort. PC1 explains 57.9% (weekly 53.8%) — a moderate factor with real sub-structure (PC2 13%), consistent with the food/blue-chip split.*

| Ticker | PC1 loading | Loading weight | Ann vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| KO | 0.390 | 16.0% | 17.6% | 20.7% |
| PEP | 0.414 | 17.0% | 21.9% | 17.6% |
| MDLZ | 0.439 | 18.0% | 22.5% | 18.2% |
| GIS | 0.424 | 17.4% | 24.7% | 16.0% |
| HSY | 0.356 | 14.6% | 27.4% | 12.1% |
| KHC | 0.420 | 17.2% | 25.1% | 15.5% |

The cohort is uniformly low-vol (18–27% annualized — the defensive profile). The lowest-vol [[Coca-Cola]] takes the largest raw PC1-mimic weight; the highest-vol [[Hershey]] (also the lowest PC1 loading, 0.356) the smallest — consistent with HSY being the cohort's outlier.

### Distinctness — = XLP, not distinct from household; the defensive trio

![[staples-food-cluster-correlation-1y.png]]
*1Y pairwise correlation heatmap. The cohort is warm against itself, just as warm against household staples and XLP, and cool against SPY.*

The decisive number is +0.042 versus household staples: packaged food/beverages correlate with PG/CL/KMB essentially as much as with each other, so there is no food-specific factor — it is the broad consumer-staples complex, captured by XLP. The +0.233 versus the ETFs reflects only distinctness from SPY (true low market beta, the defensive signature), not from XLP, which sits inside the cohort. This places staples in the campaign's defensive trio: [[Tobacco majors basket|tobacco]] is a genuinely distinct defensive factor (its own nicotine-industry cohesion, not = XLP); [[Regulated utilities]] is a real factor but = XLU; and consumer staples is = XLP and internally undifferentiated. Only tobacco escapes its sector ETF among the defensives.

### Historical tightness evolution

![[staples-food-cluster-rolling-tightness-90d.png]]
*Rolling 90-day cohesion, 2020–2026. Persistently loose — 0.49–0.69, never tight, easing to 0.49 in 2026.*

| Year | Avg intra-corr | PC1 |
|---|---|---|
| 2020 | 0.641 | 71.1% |
| 2021 | 0.591 | 66.7% |
| 2022 | 0.686 | 73.9% |
| 2023 | 0.581 | 65.3% |
| 2024 | 0.544 | 62.4% |
| 2025 | 0.575 | 64.9% |
| 2026 | 0.492 | 57.9% |

Latest 90-day reading: intra 0.476, PC1 56.5%. The cohort tightened only in the risk-off windows (2020 COVID, 2022 rate shock) when defensives moved as one, and is loose otherwise — never a tight cluster, because the names trade on idiosyncratic category dynamics (GLP-1 volume pressure on snacks/confection, private-label share, beverage pricing power) within a shared low-beta defensive wrapper. The factor that is durable is the broad staples complex (XLP), not this six-name carve-out.

## Related

- [[Consumer Staples]] — the broad sector hub (food/bev + household + retail); this cohort is its food/bev manufacturer core
- [[Tobacco majors basket]] — the distinct defensive (its own factor, not = an ETF) — the trio's exception
- [[Regulated utilities]] — the other ETF-replicable defensive (= XLU)
- [[Coca-Cola]], [[PepsiCo]] — the beverage blue-chips (cluster with household + XLP)
- [[Mondelez]], [[General Mills]], [[Kraft Heinz]] — the mid-cap packaged-food sub-group
- [[Hershey]] — the single-category confectioner (the cohort outlier)
- [[GLP-1 receptor agonists]] — the volume-pressure overhang on packaged food
- [[Vault cluster taxonomy]] — cross-cohort meta-analysis

---

*Created 2026-06-19. 1Y daily log returns through 2026-06-18; config `scripts/cluster_configs/ko.yaml`; registry row 2026-06-19. Cluster validation is structure, not a performance ranking — see `docs/cluster-validation.md`.*
