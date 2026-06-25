---
aliases: [Building products, Building products makers, HVAC and building products, Building products cluster]
tags: [sector, industrials, building-products, hvac, housing, cluster-validation]
---

# Building products

> [!warning] Cluster status: real cohesion but NOT a distinct factor — "building products" is two ETF-embedded poles (HVAC = XLI, housing-products = XHB), bridged only by broad construction/cyclical beta (Jun 2026)
> The GICS building-products makers ([[Carrier Global|CARR]]/[[Trane Technologies|TT]]/[[Johnson Controls|JCI]]/[[Lennox|LII]]/[[Masco|MAS]]/[[Owens Corning|OC]]/[[Allegion|ALLE]]/[[A.O. Smith|AOS]]/[[Fortune Brands|FBIN]]) do cohere — intra-corr 0.524 (above the 0.50 floor), PC1 58%, and they beat the random-basket AND vol-matched nulls at the 0.0001 floor (real, not random). But it is NOT one factor. The cohort shatters cleanly into two poles that each collapse into a DIFFERENT sector ETF: the HVAC pole ([[Carrier Global|CARR]]/[[Trane Technologies|TT]]/[[Johnson Controls|JCI]]/[[Lennox|LII]], internal intra 0.637) clusters with [[XLI]]/SPY — commercial/industrial-construction beta — while the housing-products pole ([[Masco|MAS]]/[[Owens Corning|OC]]/[[Allegion|ALLE]]/[[A.O. Smith|AOS]]/[[Fortune Brands|FBIN]], internal intra 0.617) clusters with the homebuilders ETF [[XHB]] and the aggregates/homebuilder controls — residential R&R/housing beta. The decisive whole-cohort number is a NEGATIVE −0.056 intra-advantage versus the ETFs: the names track XLI/XHB more than each other. Own [[XLI]] for the HVAC exposure and [[XHB]] for the residential building-products exposure; there is no single "building products" factor to own — the label spans two end-markets.

The two-end-market sector. A building-products maker's demand comes from one of two very different places: commercial and institutional construction plus equipment replacement (the HVAC names — [[Carrier Global]], [[Trane Technologies]], [[Johnson Controls]], [[Lennox]]), or residential new-build and repair-and-remodel (the housing-products names — [[Masco]] paints/plumbing, [[Owens Corning]] insulation/roofing, [[Allegion]] locks, [[A.O. Smith]] water heaters, [[Fortune Brands]] cabinets/plumbing/security). Both are late-cycle and rate-sensitive, so the whole complex shares broad construction/cyclical beta — but the two end-markets turn on different drivers (non-residential capex and electrification vs housing starts and existing-home turnover), so the cohort is two factors, each already priced by a liquid ETF.

## Sector performance

![[building-products-performance.png]]
*Normalized total return since Jan 2023 — the cohort vs [[XHB]] (the sector ETF it is tested against). See the cluster validation below for whether the cohort is distinct from or replicable by the ETF.*

## Cluster validation

The candidate cohort is the nine GICS building-products manufacturers above, tested against construction materials/aggregates ([[Vulcan Materials|VMC]]/[[Martin Marietta|MLM]]), the demand-side homebuilders ([[D.R. Horton|DHI]]/[[Lennar|LEN]]), and benchmarks (XHB homebuilders ETF, XLI industrials, SPY). 1Y window through 2026-06-18, threshold 0.5. Terminology: [[Cohort, cluster, basket]].

### Diagnostics summary

| Diagnostic | Value | Read |
|---|---|---|
| Intra-cluster corr (1Y) | 0.524 [0.242–0.753] | just above the 0.50 floor; weekly 0.450 (looser) — a blend of two tighter poles |
| PC1 explained variance | 58.1% | dominant-factor with real sub-structure (PC2 14.5%) |
| Independence null p | 0.0001 | series co-move |
| Random-basket null p | 0.0001 | real cohesion — well beyond a random 9-pick |
| Vol-matched null p | 0.0001 / 0.0001 | cohesion exceeds vol-matched baskets — shared construction beta is real |
| Holdout (2Y split) | WEAKENED 0.82 | train 0.642 → test 0.523; loadings corr −0.37 (unstable factor structure) |
| Threshold clean width | 0.00 | never a clean single cluster — the ETFs sit inside each pole |
| Intra-adv vs materials (VMC/MLM) | +0.047 | barely distinct from aggregates |
| Intra-adv vs homebuilders (DHI/LEN) | +0.038 | barely distinct from the demand side |
| Intra-adv vs ETFs (XHB/XLI/SPY) | −0.056 | NEGATIVE — the names track XLI/XHB more than each other |

All US-listed. Config: `scripts/cluster_configs/carr.yaml`; registry row 2026-06-20.

### Boundary — two poles, each absorbed by its ETF

![[building-products-cluster-dendrogram-1y.png]]
*Hierarchical clustering at 0.5. The cohort splits into two clusters, and each absorbs ETFs/controls rather than standing alone: the HVAC pole ([[Carrier Global|CARR]]/[[Trane Technologies|TT]]/[[Johnson Controls|JCI]]/[[Lennox|LII]]) clusters with [[XLI]]/SPY (industrials beta); the housing-products pole ([[Masco|MAS]]/[[Owens Corning|OC]]/[[Allegion|ALLE]]/[[A.O. Smith|AOS]]/[[Fortune Brands|FBIN]]) clusters with the aggregates ([[Vulcan Materials|VMC]]/[[Martin Marietta|MLM]]), the homebuilders ([[D.R. Horton|DHI]]/[[Lennar|LEN]]), and the homebuilders ETF [[XHB]]. Nine proposed names, no single building-products cluster.*

The threshold scan never returns the cohort as a clean single cluster (zero stable width) — at every cut the relevant sector ETF sits inside. This is the "real-but-not-distinct" signature: strong null rejections (real cohesion) but a negative intra-advantage versus the ETFs and a clean shatter into two ETF-replicable poles. It is the building-products analogue of the [[Packaged food and beverages|packaged-food]] result (real defensive cohesion but = XLP, and it splits) — here the cohesion is cyclical-construction beta and it splits into two ETFs.

### Topology — two tight sub-poles that only bridge above the cut

Reading the candidate cohort by join distance (average linkage, 1−|corr|):

| Join step | Names | Distance (1-\|corr\|) | Read |
|---|---|---|---|
| 1 | CARR + LII | 0.247 | tightest HVAC pair |
| 2 | MAS + FBIN | 0.269 | tightest housing-products pair |
| 3 | TT + JCI | 0.291 | second HVAC pair |
| 6 | HVAC pole closes (CARR+LII+TT+JCI) | 0.409 | the four HVAC names form one sub-cluster |
| 7 | housing-products pole closes (OC+MAS+FBIN+ALLE+AOS) | 0.430 | the five housing names form the other |
| 8 | the two poles bridge | 0.557 | only above the 0.5 cut — two factors, not one |

The internal structure is unambiguous: two sub-poles that each close tightly (HVAC at 0.409, housing-products at 0.430) and only join each other at 0.557, above the threshold. PC1 explains 58% with a sizeable PC2 (14.5%) — and PC2 is exactly the HVAC-vs-housing axis.

### PC1 index weights

![[building-products-cluster-pca-1y.png]]
*PCA on the candidate cohort. PC1 explains 58.1% (weekly 51.7%); the loadings are near-uniform because PC1 is the shared construction/cyclical beta both poles ride, while PC2 (14.5%) separates HVAC from housing-products.*

| Ticker | PC1 loading | Loading weight | Ann vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| CARR | 0.341 | 11.4% | 38.5% | 9.8% |
| TT | 0.318 | 10.6% | 28.6% | 12.3% |
| JCI | 0.269 | 9.0% | 30.7% | 9.7% |
| LII | 0.373 | 12.5% | 37.3% | 11.1% |
| MAS | 0.347 | 11.6% | 33.5% | 11.5% |
| OC | 0.337 | 11.3% | 38.2% | 9.8% |
| ALLE | 0.306 | 10.2% | 26.6% | 12.7% |
| AOS | 0.363 | 12.2% | 26.2% | 15.4% |
| FBIN | 0.332 | 11.1% | 46.8% | 7.8% |

Near-uniform loadings confirm PC1 is broad construction beta, not a building-products-specific factor — every name loads ~0.3 because every name is cyclical/rate-sensitive. The distinction the cohort fails to make (HVAC vs housing-products) lives in PC2, not PC1.

### Sub-structure — both poles are real but each is ETF-embedded

Sub-cohort robustness check (`scripts/cluster_configs/sub_hvac.yaml`):

| Sub-pole | Members | Internal intra | vs the other pole | vs ETF | Read |
|---|---|---|---|---|---|
| HVAC | CARR/TT/JCI/LII | 0.637 | +0.194 | +0.056 (XLI) | real, distinctly tighter — but XLI sits inside (zero clean width) |
| Housing-products | MAS/OC/ALLE/AOS/FBIN | 0.617 | +0.194 | = XHB | clusters with XHB + aggregates + homebuilders |

The HVAC pole is genuinely tighter than the rest of the cohort (+0.194) — a real sub-cluster — but it is ETF-embedded: the threshold scan never isolates it from [[XLI]] (only +0.056 intra-advantage), so own XLI rather than a bespoke HVAC basket. The housing-products pole likewise sits with [[XHB]]. Both poles are "real but embedded" (the [[Sectors/WFE|WFE]]/[[Tower REITs|tower-REIT]] pattern), in two different ETFs.

### Distinctness — = XLI + XHB, not a building-products factor

![[building-products-cluster-correlation-1y.png]]
*1Y pairwise correlation heatmap. Two warm blocks (HVAC; housing-products) rather than one uniform building-products block, each about as warm against its ETF as internally.*

The −0.056 intra-advantage versus the ETFs is the verdict: the names correlate with [[XLI]]/[[XHB]] more than with one another, so there is no building-products-specific factor beyond the two underlying sector betas. And the cohort is barely distinct from the adjacent controls — +0.047 versus aggregates ([[Vulcan Materials|VMC]]/[[Martin Marietta|MLM]]) and +0.038 versus homebuilders ([[D.R. Horton|DHI]]/[[Lennar|LEN]]) — because the whole construction complex shares one cyclical/rate driver. The investable read: own [[XLI]] for HVAC/commercial-construction exposure and [[XHB]] for residential building products; a combined nine-name basket just blends the two.

### Historical tightness evolution

![[building-products-cluster-rolling-tightness-90d.png]]
*Rolling 90-day cohesion, 2021–2026. Moderately cohesive throughout, peaking in the 2022–23 rate shock (~0.69) and easing to ~0.49 in 2026 as the two end-markets diverged.*

| Year | Avg intra-corr | PC1 |
|---|---|---|
| 2021 | 0.597 | 64.3% |
| 2022 | 0.665 | 70.4% |
| 2023 | 0.693 | 73.0% |
| 2024 | 0.584 | 63.3% |
| 2025 | 0.608 | 65.4% |
| 2026 | 0.494 | 56.5% |

Latest 90-day reading: intra 0.548, PC1 60.2%. The complex tightened to a near-single-factor in the 2022–23 rate shock (all construction names sold off together on rates), then loosened as HVAC (commercial capex, data-center cooling, electrification) and residential building products (housing affordability, R&R) diverged — the holdout's WEAKENED 0.82 and the negative PC1-loadings correlation (−0.37) between halves capture that the factor structure is not stable. It is a moderately-cohesive cyclical complex that acts like one factor only under a common rate/macro shock, and otherwise resolves to its two ETF poles — the [[Building products#Sub-structure|HVAC]] and housing legs.

## Jun 24 2026 — the ROAD Act split the cohort along its two poles

The [[21st Century ROAD to Housing Act]] (passed Congress Jun 22-23) is a residential-housing catalyst, and the Jun 24 reaction split the cohort exactly along the HVAC-vs-housing-products line the cluster validation above found. The housing-products pole (= [[XHB]]) led: [[Fortune Brands|FBIN]] +9.8%, [[Owens Corning|OC]] +8.1%, [[Masco|MAS]] +6.6%, with [[A.O. Smith|AOS]] +4.8% and [[Allegion|ALLE]] +4.1%. The HVAC pole (= [[XLI]], commercial and industrial demand) barely participated — [[Lennox|LII]] +5.4% was the only HVAC name to feature, and [[Carrier Global]] / [[Trane Technologies]] / [[Johnson Controls]] did not. A residential-supply bill is an XHB-pole event, not an XLI-pole event — live confirmation of the cohort's "two end-markets, two ETFs" verdict. The biggest single mover was the distributor [[Builders FirstSource|BLDR]] +11.3% (not in this makers cohort), the most volume-levered name to new construction. All moves were +2 to +3.4σ on a flat [[SPY]]. Full reaction in [[21st Century ROAD to Housing Act]].

---

## Related

- [[21st Century ROAD to Housing Act]] — Jun 2026 catalyst that hit the housing-products pole
- [[Homebuilders]] — the demand-side cohort (housing starts); the housing-products pole clusters with it
- [[Carrier Global]], [[Trane Technologies]], [[Johnson Controls]], [[Lennox]] — the HVAC pole (= XLI)
- [[Masco]], [[Owens Corning]], [[Allegion]], [[A.O. Smith]], [[Fortune Brands]] — the housing-products pole (= XHB)
- [[Vulcan Materials]], [[Martin Marietta]] — the aggregates control the cohort is barely distinct from
- [[XLI]], [[XHB]] — the two ETFs the cohort resolves to
- [[Packaged food and beverages]] — the analogue (real cohesion, = sector ETF, splits)
- [[Vault cluster taxonomy]] — cross-cohort meta-analysis
- [[Cohort, cluster, basket]] — terminology

---

*Created 2026-06-20. 1Y daily log returns through 2026-06-18; config `scripts/cluster_configs/carr.yaml`; sub-cohort `scripts/cluster_configs/sub_hvac.yaml`; registry row 2026-06-20. Cluster validation is structure, not a performance ranking — see `docs/cluster-validation.md`.*
