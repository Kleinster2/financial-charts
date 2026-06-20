---
aliases: [Industrial distributors, MRO distributors, Industrial distribution, Distributors cohort]
tags: [sector, industrials, distribution, mro, cluster-validation]
---

# Industrial distributors

> [!warning] Cluster status: real cohesion but ETF-replicable (= XLI); the MRO core holds, but the cohort is mostly industrials beta and the HVAC distributor defects (Jun 2026)
> The industrial/MRO distributors ([[Grainger|GWW]]/[[Fastenal|FAST]]/[[MSC Industrial|MSM]]/[[Applied Industrial|AIT]], plus [[Watsco|WSO]]) cohere — intra-corr 0.512 (PC1 61.1%), rejecting the random-basket and vol-matched nulls — but the cohesion is shared late-cycle industrials beta, not a distinct distribution factor. The decisive number is a +0.062 intra-advantage versus [[XLI]] — barely positive — and the threshold scan never returns the cohort as a clean cluster (zero stable width). The four MRO distributors (GWW/FAST/MSM/AIT) do form a real sub-cluster (closing at 0.476), but [[Watsco|WSO]] defects entirely — it clusters with XLI/SPY because its driver is HVAC replacement (shared with the [[Building products]] HVAC pole), not generic MRO. Own [[XLI]]; the distributor basket adds little over the industrials ETF.

The distribution layer of the industrial economy. Grainger, Fastenal, MSC, and Applied Industrial sell the same maintenance-repair-operations consumables to the same factories, so they share the manufacturing/PMI cycle — but that is the industrials cycle XLI already prices, so their cohesion is mostly sector beta. Watsco is filed here by GICS but trades on a different driver (HVAC replacement), and the math puts it with the building-products HVAC names, not the MRO distributors.

## Cluster validation

The candidate cohort is five industrial/MRO distributors — [[Grainger|GWW]], [[Fastenal|FAST]], [[Watsco|WSO]], [[MSC Industrial|MSM]], [[Applied Industrial|AIT]] — tested against industrials (XLI) and market (SPY). 1Y window through 2026-06-18, threshold 0.5. Terminology: [[Cohort, cluster, basket]].

### Diagnostics summary

| Diagnostic | Value | Read |
|---|---|---|
| Intra-cluster corr (1Y) | 0.512 [0.418–0.579] | barely above the 0.50 floor; weekly 0.493 (below it) |
| PC1 explained variance | 61.1% | dominant-factor (the shared industrials cycle) |
| Independence null p | 0.0001 | series co-move |
| Random-basket null p | 0.0006 | real cohesion beyond a random 5-pick |
| Vol-matched null p | 0.0003 / 0.0007 | cohesion exceeds vol-matched baskets |
| Holdout (2Y split) | WEAKENED 0.74 | train 0.690 → test 0.512; loadings corr 0.59 |
| Threshold stable width | 0.00 (none) | never a clean cluster — XLI sits inside |
| Intra-adv vs ETFs (XLI/SPY) | +0.062 | barely distinct — mostly industrials beta |

All US-listed. Config: `scripts/cluster_configs/gww.yaml`; registry row 2026-06-20.

### Boundary — the MRO core clusters; WSO defects to XLI

![[distributors-cluster-dendrogram-1y.png]]
*Hierarchical clustering at 0.5. The four MRO distributors ([[Grainger|GWW]]/[[Fastenal|FAST]]/[[MSC Industrial|MSM]]/[[Applied Industrial|AIT]]) form one cluster; [[Watsco|WSO]] does NOT join them — it clusters with [[XLI]]/SPY, because HVAC distribution is a different driver. The industrials ETF sitting on the boundary (with WSO) is the mark of an ETF-replicable cohort.*

The threshold scan never isolates the cohort as a clean cluster (zero stable width) — XLI contaminates throughout, and WSO defects. With only a +0.062 intra-advantage over XLI, the conclusion is "real cohesion but ETF-replicable": the MRO distributors are a genuine sub-cluster, but it is barely distinguishable from broad industrials, so the practical expression is [[XLI]]. This is the [[Building products|building-products]] family of result (real, ETF-replicable) — and indeed [[Watsco|WSO]] belongs analytically with the building-products HVAC pole.

### Topology — a 4-name MRO core, WSO outside

Reading the candidate cohort by join distance (average linkage, 1−|corr|):

| Join step | Names | Distance (1-\|corr\|) | Read |
|---|---|---|---|
| 1 | GWW + FAST | 0.421 | the two largest MRO distributors |
| 2 | MSM + AIT | 0.430 | the metalworking/PT pair |
| 3 | (GWW+FAST) + (MSM+AIT) | 0.476 | the MRO core closes |
| 4 | WSO + core | 0.531 | the HVAC distributor joins last, above the 0.5 cut |

The MRO core (GWW/FAST/MSM/AIT) closes at 0.476 — a real sub-cluster — while [[Watsco|WSO]] joins only at 0.531 (above the cut). PC1 explains 61.1% with near-uniform loadings on the four MRO names; WSO carries the lowest loading.

### PC1 index weights

![[distributors-cluster-pca-1y.png]]
*PCA on the candidate cohort. PC1 explains 61.1% (weekly 60.1%) — the shared manufacturing/PMI cycle.*

| Ticker | PC1 loading | Loading weight | Ann vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| GWW | 0.461 | 20.6% | 23.7% | 23.7% |
| FAST | 0.443 | 19.8% | 26.2% | 20.5% |
| WSO | 0.416 | 18.6% | 32.8% | 15.4% |
| MSM | 0.453 | 20.3% | 27.8% | 19.8% |
| AIT | 0.462 | 20.7% | 27.3% | 20.6% |

The four MRO distributors load almost identically (~0.45–0.46); [[Watsco|WSO]] carries the lowest loading and the highest vol — consistent with it being the odd one out.

### Distinctness — = XLI

![[distributors-cluster-correlation-1y.png]]
*1Y pairwise correlation heatmap. A warm GWW/FAST/MSM/AIT block, but XLI is about as warm against them as they are against each other — and WSO is cooler.*

The +0.062 intra-advantage versus the ETFs is the verdict: the distributors track [[XLI]] almost as much as each other, so there is no distinct distribution factor beyond the industrials cycle. The MRO core is real but not separable from XLI, and WSO is a building-products/HVAC name. Own XLI for the exposure.

### Historical tightness evolution

![[distributors-cluster-rolling-tightness-90d.png]]
*Rolling 90-day cohesion, 2021–2026. Moderately cohesive, peaking in the 2022–23 rate shock (~0.69) and easing since — the industrials-cycle pattern.*

| Year | Avg intra-corr | PC1 |
|---|---|---|
| 2021 | 0.580 | 66.7% |
| 2022 | 0.645 | 71.7% |
| 2023 | 0.689 | 75.3% |
| 2024 | 0.575 | 66.1% |
| 2025 | 0.595 | 67.7% |
| 2026 | 0.548 | 64.1% |

Latest 90-day reading: intra 0.524, PC1 62.2%. The cohort tightened in the 2022–23 rate shock (all industrials sold off together) and has eased since — the same cyclical-beta pattern as [[Building products]], and the same conclusion: real cohesion, but it is the industrials cycle (XLI), not a distinct distributor factor.

## Related

- [[Building products]] — the sibling "real but = ETF" cohort; [[Watsco|WSO]] belongs with its HVAC pole
- [[Grainger]], [[Fastenal]], [[MSC Industrial]], [[Applied Industrial]] — the MRO core
- [[Watsco]] — the HVAC-distribution defector
- [[XLI]] — the industrials ETF the cohort resolves to
- [[Vault cluster taxonomy]] — cross-cohort meta-analysis
- [[Cohort, cluster, basket]] — terminology

---

*Created 2026-06-20. 1Y daily log returns through 2026-06-18; config `scripts/cluster_configs/gww.yaml`; registry row 2026-06-20. Cluster validation is structure, not a performance ranking — see `docs/cluster-validation.md`.*
