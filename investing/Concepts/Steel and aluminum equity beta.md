---
aliases: [Steel and aluminum equity beta, Steel equity beta, Aluminum equity beta, Metals producer cohort, Steel aluminum cluster]
tags: [concept, commodities, metals, materials, steel, aluminum, cluster-validation]
---

# Steel and aluminum equity beta

Whether the listed processed-metal producers are one "metals" factor or two. The candidate is five US producers — three steel ([[Nucor]] NUE, [[Steel Dynamics]] STLD, [[Cleveland-Cliffs]] CLF) and two aluminum ([[Alcoa]] AA, [[Century Aluminum]] CENX). The answer is two: steel and aluminum split into separate factors. They share a real industrial-metals-cycle beta (the combined cohort rejects all three nulls), but they are not one cohort — the combined group is boundary-dependent, only 58% single-factor (with a 22% second component), and the dendrogram cleanly separates aluminum from steel at a cross-correlation of just 0.355. This is the processed-metal counterpart to the mined-metal family ([[Copper equity beta]], [[Gold equity beta]], [[Lithium equity beta]], [[Uranium equity beta]]), and its lesson is the family's organizing principle stated in the negative: a commodity-equity factor is granular to a single commodity, so a multi-commodity label has no single factor.

> [!warning] Cluster status: NOT one metals factor — two, split by commodity (aluminum robust, steel = the EAF pair) (June 2026)
> The combined five-name cohort rejects the random-basket (p 0.0007) and vol-matched (p 0.0001) nulls — there is a real shared industrial-metals beta — but it is not one factor. Intra-corr is only 0.474 (weekly 0.383), PC1 explains just 58.2% with a large 22.3% PC2 (the two-factor signature), the threshold scan is boundary-dependent, and the holdout is WEAKENED (ratio 0.70). At threshold 0.5 the dendrogram separates aluminum ([[Alcoa]]+[[Century Aluminum]]) from steel ([[Nucor]]/[[Steel Dynamics]]/[[Cleveland-Cliffs]]); they merge only at distance 0.645 (cross-corr 0.355). The two sub-factors are asymmetric: the aluminum pair (intra 0.686) is ROBUST (stable threshold width 0.20), while the steel trio (intra 0.640) is boundary-dependent — its robust core is the [[Nucor]]+[[Steel Dynamics]] electric-arc-furnace pair (0.845), with [[Cleveland-Cliffs]] (integrated blast furnace + captive iron ore, 71% vol) the loose satellite. Steel is ETF-replicable by SLX. See below.

The nulls reject because the five names genuinely share the industrial-metals cycle — tariffs, reshoring, construction and auto demand, and the 2025-26 metals rally lifted all of them (every member returned +92% to +221% on the year). But shared sector beta is not a single factor, and three diagnostics say so: the cross-correlation between the steel and aluminum sub-groups is only 0.355 (against 0.640 within steel and 0.686 within aluminum), PC2 carries a fifth of the variance, and the cohort has been loosening for years (combined intra 0.69 in 2021 to 0.46 in 2026) as the two metals' cycles diverged. This is the same shape as the [[AI interconnect]] optics/silicon result — a basket that clears the random-basket null purely by being two cohesive sub-pieces. The investable read is two factors, not one: own SLX for the steel-equity factor (or the [[Nucor]]/[[Steel Dynamics]] mini-mill core), and the [[Alcoa]]/[[Century Aluminum]] pair for the aluminum factor.

## Cluster validation

Procedure: `scripts/cluster_analysis.py --config scripts/cluster_configs/steel_aluminum.yaml`, with `cluster_permutation_test.py --null all`, `cluster_threshold_scan.py`, `cluster_holdout_test.py --window 2y`, and sub-cohort threshold scans (`sub_steel.yaml`, `sub_aluminum.yaml`). Standard in `docs/cluster-validation.md`. X (US Steel) is excluded — delisted into Nippon Steel, June 2025.

### Headline numbers (1Y, 2025-06-13 to 2026-06-12)

| Diagnostic | Result | Interpretation |
|---|---|---|
| Avg intra-cluster correlation | 0.474 (weekly 0.383) | Loose — a two-factor average, not one cohort |
| PC1 / PC2 explained variance | 58.2% / 22.3% | Two factors (steel, aluminum) |
| Steel sub-group intra | 0.640 | NUE+STLD 0.845 core, CLF the 0.53 satellite |
| Aluminum sub-group intra | 0.686 | AA+CENX |
| Steel vs aluminum cross-corr | 0.355 | Distinct — they merge only at distance 0.645 |
| Random-basket null | p 0.0007 | Rejects — real shared metals-cycle beta |
| Vol-matched null | p 0.0001 | Rejects — cohesion beyond shared vol (but two factors) |
| Threshold scan | boundary-dependent | SLX/XME/XLB/SPY contaminate from 0.45 |
| 2y holdout | WEAKENED (ratio 0.70) | Eroding as the two metals diverge |

![[steel-aluminum-cluster-correlation-1y.png]]
*1Y correlation matrix: two visible blocks — the NUE/STLD/CLF steel block and the AA/CENX aluminum block — with low cross-block correlation (~0.36).*

### Hierarchical clustering and join distances

The dendrogram builds two separate sub-clusters that only merge at a long distance, and the broad-market/sector ETFs join before the two metals unite into anything clean.

![[steel-aluminum-cluster-dendrogram-1y.png]]

| Step | Left | Right | Distance (1-\|corr\|) | Members |
|---|---|---|---|---|
| 1 | NUE | STLD | 0.155 | NUE+STLD (EAF steel pair) |
| 2 | AA | CENX | 0.314 | AA+CENX (aluminum pair) |
| 3 | CLF | NUE+STLD | 0.463 | steel trio |
| 4 | AA+CENX | steel trio | 0.645 | all five |

Final join distance 0.645 — steel and aluminum unite only at correlation ~0.355, and the threshold scan returns no stable width for the combined cohort: SLX, XME, XLB and SPY contaminate from threshold 0.45. BOUNDARY-DEPENDENT. The sub-cohort sweep is where the structure lives (below).

![[steel-aluminum-cluster-threshold-scan.png]]

### Sub-cohort robustness sweep

| Sub-cohort | Intra-corr | Stable width | Verdict |
|---|---|---|---|
| Aluminum (AA, CENX) | 0.686 | 0.20 [0.35-0.55] | ROBUST — a clean, distinct aluminum factor |
| Steel (NUE, STLD, CLF) | 0.640 | 0.00 (none) | Boundary-dependent — SLX and the market blur the trio |

Aluminum is the cleaner factor; steel's robust structure is really the [[Nucor]]+[[Steel Dynamics]] EAF pair, with [[Cleveland-Cliffs]] decoupling on iron-ore and auto-cycle dynamics. Configs `sub_steel.yaml`, `sub_aluminum.yaml`.

### PC1 index weights

PCA is run on standardized daily log returns. Raw PC1-mimic weight scales the PC1 loading by inverse realized volatility.

| Member | PC1 loading | Loading weight | Ann vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| NUE | 0.473 | 21.23% | 29.15% | 32.28% |
| STLD | 0.493 | 22.12% | 34.08% | 28.77% |
| CLF | 0.445 | 19.96% | 71.42% | 12.39% |
| AA | 0.439 | 19.69% | 57.08% | 15.29% |
| CENX | 0.379 | 17.00% | 66.81% | 11.28% |

![[steel-aluminum-cluster-pca-1y.png]]
*PC1 is the shared industrial-metals cycle; the low-vol mini-mills NUE/STLD dominate the inverse-vol-weighted index (61% combined), while a 22% PC2 carries the steel-vs-aluminum split that PC1 cannot.*

### Permutation nulls

![[steel-aluminum-cluster-permutation.png]]

The nulls reject — and that is exactly the trap the rest of the validation guards against. Against 10,000 random five-name baskets (null mean intra 0.151) and 10,000 vol-matched baskets (null mean 0.153), the cohort's 0.474 rejects at p 0.0007 and p 0.0001. But a five-name basket made of two cohesive sub-pairs will clear a random-basket test on shared sector beta alone; the rejection confirms the metals cycle is real, not that the five names are one factor. The threshold scan, the 22% PC2, and the 0.355 cross-correlation carry the "two factors" verdict — the same lesson as [[AI interconnect]].

### Historical tightness evolution

![[steel-aluminum-cluster-rolling-tightness-90d.png]]

| Year | Avg corr | PC1 | Final join distance |
|---|---|---|---|
| 2021 | 0.689 | 75.3% | 0.386 |
| 2022 | 0.675 | 74.1% | 0.406 |
| 2023 | 0.652 | 72.3% | 0.419 |
| 2024 | 0.569 | 65.6% | 0.500 |
| 2025 | 0.611 | 69.0% | 0.456 |
| 2026 | 0.460 | 57.2% | 0.662 |

This combined cohort is neither durable nor newly formed — it is steadily decohering. The steel and aluminum names co-moved more tightly in 2021-23 (combined intra ~0.65-0.69, when a single post-COVID industrial-restocking cycle drove both metals) and have pulled apart since (0.46 by 2026) as steel (tariffs, auto, construction) and aluminum (power costs, packaging, grid/EV) returned to separate cycles. The decohering trend is itself the evidence that "metals producers" was never one durable factor — it was a temporary co-movement of two.

---

## What the verdict means

Steel and aluminum is the family's control case: it shows what a commodity-equity cohort looks like when the label spans more than one commodity. Three reads:
- It is two factors, not one. Aluminum ([[Alcoa]]/[[Century Aluminum]]) is a robust standalone factor; steel's robust structure is the [[Nucor]]/[[Steel Dynamics]] EAF mini-mill pair. The cross-correlation (0.355) is shared industrial-metals beta, not a unifying factor.
- The mined-metal family principle, confirmed in the negative. Copper, gold, lithium, and uranium each validated as one cohort because each is one commodity; steel-plus-aluminum is two cohorts because it is two commodities. The granularity of a commodity-equity factor is the individual commodity — a "metals" sleeve is a portfolio of factors, not a factor.
- Within steel, process matters. The EAF mini-mills ([[Nucor]], [[Steel Dynamics]]) cohere tightly (0.845); the integrated, iron-ore-exposed [[Cleveland-Cliffs]] is the satellite, trading partly on iron-ore and auto-cycle dynamics — a within-steel split by production model.

---

## Trade implications

| Trade | Verdict |
|---|---|
| Long "metals producers" basket (all 5) | A two-factor blend, not a clean exposure — diluted by the 0.355 steel/aluminum cross |
| Long steel (SLX or NUE/STLD) | The steel-equity factor; SLX replicates it, the EAF pair is the robust core |
| Long aluminum (AA + CENX) | The robust, distinct aluminum factor (0.686, width 0.20) |
| Long steel / short aluminum | A real cross-commodity spread (cross-corr only 0.355) — two factors, genuinely separable |
| Long NUE/STLD / short CLF | Within-steel: EAF mini-mill vs integrated/iron-ore — a process-model bet |
| Pair trades within a sub-group | Idiosyncratic (CLF iron-ore leverage, CENX power costs) — not factor exposures |

---

## Related

### Member actors
- [[Nucor]] — largest US steelmaker, EAF mini-mill, low-vol PC anchor
- [[Steel Dynamics]] — EAF mini-mill, tight pair with Nucor (0.845)
- [[Cleveland-Cliffs]] — integrated blast furnace + iron ore, the loose steel satellite
- [[Alcoa]] — largest Western aluminum (alumina + aluminum)
- [[Century Aluminum]] — US primary aluminum smelter (power-cost levered), +221% on the year

### Adjacent concept notes
- [[Aluminum]] — the aluminum commodity
- [[Copper equity beta]] / [[Gold equity beta]] / [[Lithium equity beta]] / [[Uranium equity beta]] — the mined-metal family; each is one commodity = one cohort
- [[AI interconnect]] — the same "passes the nulls but is two sub-pieces" shape
- [[Fertilizer producers]] — the messier multi-commodity case: a loose ag-input cohort that splits (Mosaic defects) and is regime-unstable, where steel/aluminum split cleanly into two factors
- [[Vault cluster taxonomy]] — the cross-cohort map

### Methodology
- `docs/cluster-validation.md`
