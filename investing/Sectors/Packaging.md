---
aliases: [Packaging, Packaging materials, Containers and packaging, Packaging sector]
tags: [sector, materials, packaging, cluster-validation]
---

# Packaging

> [!warning] Cluster status: NOT a distinct factor — packaging is materials beta (= [[XLB]]) that fragments by substrate; [[Ball|BALL]] (metal cans) decouples, and only the same-substrate containerboard pair [[International Paper|IP]]+[[Packaging Corp|PKG]] coheres (marginally distinct) (Jun 2026)
> The four listed packaging names ([[International Paper|IP]]/[[Packaging Corp|PKG]]/[[Ball|BALL]]/[[Amcor|AMCR]]) cohere only loosely (intra 0.546, at the floor) and are NOT distinct from broad materials: a −0.031 intra-advantage vs the materials ETF [[XLB]] (the cohort correlates with XLB about as much as with itself). They beat the random-basket null (p 0.0005 — real materials co-movement) but the threshold scan is boundary-dependent and the factor structure is unstable across regimes (holdout loadings-corr 0.35). The label fragments by substrate: [[Ball|BALL]] (metal beverage cans — aluminum cost, beverage volumes) is the decoupler (joins last at 0.52, lowest PC1 loading); [[Amcor|AMCR]] (flexible plastics — resin, consumer/healthcare) attaches loosely; only the containerboard pair [[International Paper|IP]]+[[Packaging Corp|PKG]] (box volumes + OCC pricing) is tight (0.71) and marginally distinct from [[XLB]] (+0.122). Distinct from the consumer staples it serves ([[XLP]] +0.232) but not from broad materials. Own [[XLB]]. See below.

The label that spans three substrates. "Packaging" groups four companies on three different materials with three different demand and cost drivers: corrugated containerboard ([[International Paper|IP]]/[[Packaging Corp|PKG]] — e-commerce/industrial box volumes, old-corrugated-container input costs), metal beverage cans ([[Ball|BALL]] — beverage volumes, aluminum), and flexible/rigid plastics ([[Amcor|AMCR]] — consumer-staples/healthcare volumes, resin). The market prices these apart, so the only tight co-movement is within a substrate (the IP+PKG containerboard pair), and the broad "packaging" cohort resolves to the materials ETF [[XLB]].

## Sector performance

![[packaging-performance.png]]
*Normalized total return since 2019 vs the materials ETF [[XLB]]. The containerboard names ([[International Paper|IP]]/[[Packaging Corp|PKG]]) and [[Amcor|AMCR]] move loosely together while [[Ball|BALL]] (metal cans) takes its own beverage/aluminum-driven path; [[XLB]] threads through. The dispersion across substrates — and the absence of a single "packaging" line apart from XLB — is the fragmented / ETF-replicable verdict.*

## Cluster validation

The candidate cohort is the four listed packaging names — [[International Paper|IP]], [[Packaging Corp|PKG]], [[Ball|BALL]], [[Amcor|AMCR]] — tested against the materials ETF ([[XLB]] — the key benchmark), broad industrials ([[XLI]]), consumer staples ([[XLP]], the end-market), and the market ([[SPY]]). 1Y window through 2026-06-22 (199 obs); threshold 0.5. Smurfit WestRock (SW) is not in the DB. Config: `scripts/cluster_configs/packaging.yaml`; registry row 2026-06-23. Terminology: [[Cohort, cluster, basket]].

### Diagnostics summary

| Diagnostic | Value | Read |
|---|---|---|
| Intra-corr (1Y) | 0.546 (4-name) / 0.613 (ex-BALL) / 0.711 (IP+PKG pair) | At the floor; only the containerboard pair is tight |
| PC1 explained variance | 65.0% | Moderate; 35% idiosyncratic |
| Random-basket null p | 0.0005 | Real co-movement — materials beta |
| Holdout (2Y split) | STRENGTHENING 1.10, loadings-corr 0.35 | Cohesion up but factor structure unstable |
| Threshold stable width | 0.00 | [[XLB]]/[[XLI]]/[[SPY]] contaminate from 0.55 |
| Intra-adv vs [[XLB]] (materials) | −0.031 (4-name) / +0.007 (ex-BALL) / +0.122 (IP+PKG) | = materials; only the containerboard pair edges distinct |
| Intra-adv vs industrials ([[XLI]]) | +0.063 | ≈ zero |
| Intra-adv vs staples ([[XLP]]) | +0.232 | Distinct from the end-market it serves |
| Intra-adv vs market (SPY) | +0.235 | Distinct from the market, not from materials |

### Boundary — the paper/flexible names cluster, metal cans split off

![[packaging-cluster-dendrogram-1y.png]]
*Hierarchical clustering at 0.5. [[International Paper|IP]]/[[Packaging Corp|PKG]]/[[Amcor|AMCR]] form one cluster (paper + flexible) and [[Ball|BALL]] (metal cans) is a singleton, while the broad ETFs [[XLB]]/[[XLI]]/[[SPY]] form their own block and [[XLP]] (staples) sits apart. There is no single packaging cluster distinct from materials — the substrate split is visible, and the ETFs contaminate the cohort from 0.55.*

The threshold scan returns no clean band, and the 4-name intra-advantage over [[XLB]] is negative — the ETF-replicable signature. The packaging names co-move on a shared materials/industrial-demand beta that [[XLB]] already prices; they do not out-cohere it.

### Topology — a containerboard pair, a flexible satellite, a metal-can decoupler

Reading the candidate cohort by join distance (average linkage, 1−|corr|):

| Join step | Names | Distance (1-\|corr\|) | Read |
|---|---|---|---|
| 1 | IP + PKG | 0.289 | the containerboard pair (corr 0.71) — the tight core |
| 2 | AMCR + (IP+PKG) | 0.437 | [[Amcor\|AMCR]] (flexible plastics) attaches as a satellite |
| 3 | BALL + core | 0.521 | [[Ball\|BALL]] (metal cans) joins last, above the cut — the substrate decoupler |

The cohesion lives in the same-substrate pair [[International Paper|IP]]+[[Packaging Corp|PKG]] (0.71) — both pure containerboard, sharing box volumes and OCC pricing. [[Amcor|AMCR]] (flexible) attaches loosely; [[Ball|BALL]] (beverage cans, an aluminum/beverage-volume story) decouples. The containerboard pair carries a +0.122 intra-advantage over [[XLB]] — a marginal distinct sub-pair (the [[Off-price retail|TJX+ROST]] pattern), but below the robust threshold, so not carved out as a separate cohort.

### PC1 index weights

![[packaging-cluster-pca-1y.png]]
*PCA on the candidate cohort. PC1 explains 65.0%; [[International Paper|IP]]/[[Packaging Corp|PKG]] load highest, [[Ball|BALL]] lowest (the decoupler). [[International Paper|IP]] carries the highest vol (44%) on its operational/restructuring noise.*

| Ticker | PC1 loading | Loading weight | Ann vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| IP | 0.525 | 26.30% | 44.47% | 18.58% |
| PKG | 0.518 | 25.93% | 27.75% | 29.35% |
| BALL | 0.450 | 22.53% | 26.07% | 27.16% |
| AMCR | 0.504 | 25.23% | 31.82% | 24.91% |

### Distinctness — = materials, distinct only from the staples end-market

![[packaging-cluster-correlation-1y.png]]
*1Y pairwise correlation heatmap. [[International Paper|IP]]–[[Packaging Corp|PKG]] run warm (0.71); [[Ball|BALL]] is the coolest to the others (0.44–0.54). The cohort is about as warm to [[XLB]] (0.58) as to itself.*

The decisive number is the −0.031 intra-advantage vs [[XLB]] for the four names (and +0.007 even ex-BALL) — they are materials beta, not a distinct packaging factor. The one genuinely positive read is +0.232 vs consumer staples [[XLP]]: packaging is a materials/industrial-cyclical, NOT the defensive staples sector it supplies — a useful distinction, but it points to [[XLB]], not to an ownable packaging basket. Only the containerboard pair IP+PKG (+0.122) edges distinct, and marginally.

### Historical tightness evolution

![[packaging-cluster-rolling-tightness-90d.png]]
*Rolling 90-day cohesion since 2019 — never tight, oscillating 0.32–0.58 with no durable peak. Unlike the validated pairs, the packaging label has not held together as a factor in any regime, because the substrates move on different drivers; the cohesion that appears is shared materials-cyclical beta, not a packaging factor.*

| Year | Avg intra-corr | PC1 |
|---|---|---|
| 2019 | 0.344 | 55.4% |
| 2020 | 0.579 | 69.0% |
| 2021 | 0.529 | 65.6% |
| 2022 | 0.438 | 59.4% |
| 2023 | 0.578 | 69.1% |
| 2024 | 0.324 | 50.3% |
| 2025 | 0.474 | 60.8% |
| 2026 | 0.550 | 66.5% |

## Where this sits in the campaign

Packaging joins the fragmented-by-driver set — a label spanning sub-segments the market prices apart, like [[Alcohol and spirits|alcohol]] (beer vs spirits), [[Building products]] (HVAC vs housing-products), and [[Chemicals]] (commodity vs gases). Here the split is by substrate: containerboard, metal cans, and flexible plastics, each on its own volume and input-cost cycle, so only the same-substrate containerboard pair coheres. As a whole it is ETF-replicable (= [[XLB]]); the only distinct structure is the marginal IP+PKG sub-pair. The contrast with the same week's [[Construction aggregates|aggregates]] duopoly is the lesson: aggregates are one homogeneous product (a distinct 0.88 factor), packaging is three different products under one label (materials beta).

## Related

- [[International Paper]], [[Packaging Corp]] — the containerboard pair (the tight core); [[Ball]] — metal cans (the substrate decoupler); [[Amcor]] — flexible plastics (loose satellite)
- [[XLB]] — the materials ETF the cohort resolves to (own this); [[XLP]] — consumer staples, the end-market it is distinct from
- [[Construction aggregates]] — the same-week homogeneous-duopoly contrast (distinct); [[Alcohol and spirits]], [[Building products]] — fellow fragment-by-sub-segment labels
- [[Vault cluster taxonomy]] — cross-cohort meta-analysis; [[Cohort, cluster, basket]] — terminology

---

*Created 2026-06-23. 1Y daily log returns through 2026-06-22; config `scripts/cluster_configs/packaging.yaml`; registry row 2026-06-23. Cluster validation is structure, not a performance ranking — see `docs/cluster-validation.md`.*
