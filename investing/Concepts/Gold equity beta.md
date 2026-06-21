---
aliases: [Gold equity beta, Gold miner cohort, Gold mining cluster, Gold miners factor, Senior gold miners basket]
tags: [concept, commodities, metals, mining, gold, cluster-validation]
---

# Gold equity beta

Whether the listed gold miners trade as one factor — and if so, what that factor actually is. The cohort is six liquid North American gold producers: [[Newmont]] (NEM), [[Barrick Gold]] (B), [[Agnico Eagle]] (AEM), [[Kinross Gold]] (KGC), [[Alamos Gold]] (AGI), [[B2Gold]] (BTG). The validation answers yes, they cohere — very tightly and durably — but the factor binding them is the gold price itself, captured by the [[Gold]] metal ([[GLD]]) and the GDX miners ETF. This is the campaign's second commodity-beta cohort after [[Copper equity beta]], and it replicates the copper law with two twists: the cohort is tighter and more durable than copper (a raging gold bull is unifying the miners), and the operating-leverage premium over the metal is larger.

> [!warning] Cluster status: validated cohesion, but it is the gold price — ETF-replicable (June 2026)
> The six gold miners are an exceptionally tight, durable, single-factor cohort: intra-corr 0.861 (weekly 0.892 — synchronous North American listings, so the daily is already clean), PC1 88.4%, and they reject the independence, random-basket and vol-matched nulls all at the 0.0001 floor. But the cohesion is commodity beta, not a distinct equity factor. The cohort is barely distinct from the gold price itself ([[Gold]]/[[GLD]], +0.070 intra-advantage) and has a negative advantage versus the miner ETFs (GDX/GDXJ, -0.057) — it correlates more with its own ETF than with itself. It never forms a clean cluster at any threshold: GLD, GDX and GDXJ contaminate from 0.20, the broad market (SPY) from 0.55. Holdout STABLE and strengthening (ratio 1.05 — 0.810 in 2024-25 rising to 0.850 in 2025-26 as the gold bull tightened the group). The verdict is the gold analogue of [[Copper equity beta]]: a real cohort that a single ETF (GDX) replicates, with no separable gold-equity factor over the metal — only a thin, bull-amplified operating-leverage premium. See below.

A commodity cohort coheres trivially, which is exactly why cohesion settles nothing here. Every member is levered to one exogenous price (gold), so they are guaranteed to co-move and to crush the random-basket and vol-matched nulls — that is necessary but uninformative. The only question that carries information is distinctness: does the gold-equity complex trade as something separable from the gold price and the gold-miner ETF? It does not. The miners add an operating-leverage premium over the flat metal — in the trailing year they returned roughly twice gold (GDX +49.6% versus GLD +23.8%, with [[Barrick Gold]] +96.5% and [[Newmont]] +72.3% on company-specific leverage) — but that premium is amplified gold beta, not a separate factor, and GDX captures it in full. Own GDX for leveraged gold-equity beta or GLD for the unlevered metal; choosing [[Barrick Gold]] over [[B2Gold]] is a bet on cost curve, jurisdiction, and turnaround, not on a distinct factor.

## Cluster validation

Procedure: `scripts/cluster_analysis.py --config scripts/cluster_configs/gold_equity_beta.yaml`, with `cluster_permutation_test.py --null all`, `cluster_threshold_scan.py`, and `cluster_holdout_test.py --window 2y`. Standard in `docs/cluster-validation.md`. Data note: Barrick is ticker B (renamed from GOLD to Barrick Mining, May 2025); the DB ticker GOLD now maps to an unrelated "Gold.com" series and is not used here.

### Headline numbers (1Y, 2025-06-13 to 2026-06-12)

| Diagnostic | Result | Interpretation |
|---|---|---|
| Avg intra-cluster correlation | 0.861 (weekly 0.892) | Very tight cohesion |
| PC1 explained variance | 88.4% (weekly 91.0%) | Dominant single factor |
| Tightest pair | AEM-KGC = 0.938 | Two Canada-weighted seniors |
| Loosest pair | NEM-BTG = 0.766 | Senior vs jurisdiction-heavy intermediate |
| Cluster vs gold metal (GLD) | 0.791 (+0.070) | Barely distinct from the metal — leverage premium only |
| Cluster vs miner ETFs (GDX/GDXJ) | 0.918 (-0.057) | Negative advantage — the cohort IS GDX |
| Cluster vs market (SPY) | 0.444 (+0.417) | Distinct from broad market — a partial diversifier |
| Independence / random-basket / vol-matched nulls | all p 0.0001 | Reject at the floor (trivial commodity cohesion) |
| Threshold scan | boundary-dependent | GLD/GDX/GDXJ contaminate from 0.20 |
| 2y holdout | STABLE, ratio 1.05 | Durable and strengthening into the gold bull |

![[gold-equity-beta-cluster-correlation-1y.png]]
*1Y correlation matrix: uniformly high (0.77-0.94) across the six producers; no internal block structure — a single gold factor.*

### Hierarchical clustering and join distances

The six miners form one tight cluster with no internal split, but it is not a clean island: the gold metal and the miner ETFs sit directly on top of it and join at the very first thresholds.

![[gold-equity-beta-cluster-dendrogram-1y.png]]

| Step | Left | Right | Distance (1-\|corr\|) | Members |
|---|---|---|---|---|
| 1 | AEM | KGC | 0.065 | AEM+KGC |
| 2 | NEM | B | 0.099 | NEM+B |
| 3 | AEM+KGC | NEM+B | 0.107 | four seniors |
| 4 | AGI | (seniors) | 0.135 | +Alamos |
| 5 | BTG | (cohort) | 0.191 | all six |

Final join distance 0.191 — the whole cohort unifies at a very short distance, but the threshold scan returns no stable width: GLD, GDX and GDXJ contaminate from threshold 0.20. BOUNDARY-DEPENDENT — there is no threshold at which the miners are an island separable from the gold complex.

![[gold-equity-beta-cluster-threshold-scan.png]]

### PC1 index weights

PCA is run on standardized daily log returns. Raw PC1-mimic weight scales the PC1 loading by inverse realized volatility.

| Member | PC1 loading | Loading weight | Ann vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| NEM | 0.409 | 16.71% | 52.34% | 17.41% |
| B | 0.410 | 16.73% | 50.78% | 17.97% |
| AEM | 0.419 | 17.13% | 49.40% | 18.91% |
| KGC | 0.418 | 17.07% | 57.76% | 16.12% |
| AGI | 0.405 | 16.55% | 58.80% | 15.34% |
| BTG | 0.387 | 15.81% | 60.49% | 14.26% |

![[gold-equity-beta-cluster-pca-1y.png]]
*Balanced loadings (0.39-0.42) — every name is the gold factor. Note the ~50-60% annualized vols: gold miners run at roughly twice the vol of the [[Copper equity beta|copper miners]], the leverage that makes the equity move ~2x the metal.*

### Permutation nulls

![[gold-equity-beta-cluster-permutation.png]]

A commodity cohort is guaranteed to crush these nulls, which is why they are necessary but uninformative here. Against 10,000 random six-name baskets (random-basket null mean intra 0.165) and 10,000 volatility-matched baskets (vol-matched null mean 0.170, pool 272 names), the cohort's 0.861 rejects at the 0.0001 floor on both. The rejection confirms the miners co-move far more than chance, but it says nothing about distinctness — copper rejected at the same floor and was still just the copper price. The informative diagnostics are the threshold scan and the intra-advantage versus the metal, not the nulls.

### Historical tightness evolution

![[gold-equity-beta-cluster-rolling-tightness-90d.png]]

| Year | Avg corr | PC1 | Final join distance |
|---|---|---|---|
| 2021 | 0.819 | 84.9% | 0.207 |
| 2022 | 0.744 | 78.7% | 0.308 |
| 2023 | 0.751 | 79.4% | 0.292 |
| 2024 | 0.750 | 79.3% | 0.297 |
| 2025 | 0.804 | 83.7% | 0.225 |
| 2026 | 0.853 | 87.8% | 0.199 |

This is a durable cluster, and it is tightening rather than newly formed or eroding. Cohesion held in the 0.74-0.82 band through 2021-2024 and has climbed to 0.85 (PC1 88%) in 2026 as the gold bull (gold above $5,000/oz) pulled every miner up on the same price. That is the mirror image of [[Copper equity beta]], whose holdout WEAKENED (0.82) as copper names diverged — a commodity-equity cohort tightens when its underlying makes a strong directional move and loosens when the metal chops.

---

## What the verdict means

Gold is the second confirmation of the commodity-beta law that [[Copper equity beta]] set: the listed miners of a single commodity form a real, tight, durable cohort, but the cohort is the commodity trade and a single ETF replicates it. Three reads specific to gold:
- It IS gold beta, levered. The cohort correlates 0.791 with [[GLD]] and has a negative advantage versus GDX (-0.057). There is no separable gold-equity factor — only leverage. GDX is the cohort.
- The leverage premium is larger than copper's (+0.070 vs +0.033) and is amplified by the bull. Gold miners carry higher cost-leverage, and in a rising-gold regime that leverage shows: the miners returned ~2x the metal this year. But leverage is amplitude on the same factor, not a new factor — it lives in GDX, which returned +49.6% vs GLD's +23.8%.
- Stock selection is idiosyncratic, not factor exposure. The 1Y return spread is enormous despite 0.86 correlation — [[Barrick Gold]] +96.5% (copper-growth re-rating, ticker change) versus [[B2Gold]] +14.5% (Mali jurisdiction discount). Picking within the cohort is a bet on cost curve, jurisdiction, and company-specific catalysts, not on the gold factor, which you get more cleanly from GDX.

---

## Trade implications

| Trade | Verdict |
|---|---|
| Long gold-miner basket | Equivalent to long GDX — leveraged gold-equity beta with name concentration |
| Long miners / short GLD | Captures the +0.070 leverage premium over the metal — real but thin, and regime-dependent (bull-amplified) |
| Long miners / short GDX | Near-zero net exposure — the cohort IS GDX (-0.057 advantage) |
| GDX vs GLD | The only clean expression of the leverage decision: GDX for levered equity beta, GLD for the unlevered metal |
| Pair trades within the cohort | Idiosyncratic cost-curve / jurisdiction / catalyst bets (Barrick copper growth, B2Gold Mali risk) — not factor exposures |
| Long gold complex / short SPY | A partial diversifier (+0.417 vs SPY) but not market-neutral — gold equities carry real risk-on beta |

---

## Related

### Member actors
- [[Newmont]] — largest gold miner, most central PC1 name
- [[Barrick Gold]] — #2, growing into a gold-copper major (ticker B since May 2025)
- [[Agnico Eagle]] — Canada-weighted senior, tightest pair with Kinross
- [[Kinross Gold]] — senior, higher West Africa jurisdiction risk
- [[Alamos Gold]] — Canadian intermediate
- [[B2Gold]] — intermediate, the cohort's loosest member (Mali concentration)

### Adjacent concept notes
- [[Copper equity beta]] — the first commodity-beta cohort; gold replicates its law
- [[Precious metals royalties]] — the capital-light gold sibling (FNV/WPM/RGLD/OR); same verdict (= gold/GDX), confirming the commodity-beta law is model-agnostic
- [[Silver equity beta]] — the silver-miner sibling; does not even separate from THESE gold miners (−0.041 vs GDX) — gold and silver mining are one precious-metals complex, silver the higher-beta expression
- [[Lithium equity beta]] — the third commodity-beta cohort; the loosest of the family (no spot instrument, cross-region noise)
- [[Uranium equity beta]] — the fourth; tight + STABLE like gold (both sustained bulls), but the equities sit far from spot (+0.180 wedge vs gold's +0.070)
- [[Steel and aluminum equity beta]] — the processed-metal control case: "metals" splits into two factors (steel, aluminum), confirming the family is granular to a single commodity
- [[Gold]] — the underlying metal and macro driver
- [[Gold mining consolidation]] — the sector M&A backdrop (record prices funding deals)
- [[Vault cluster taxonomy]] — the cross-cohort map

### Methodology
- `docs/cluster-validation.md`
