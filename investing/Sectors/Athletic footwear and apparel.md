---
aliases: [Athleisure, Athletic apparel, Athletic footwear, Sportswear, Footwear brands, Athletic apparel cluster]
tags: [sector, consumer, apparel, footwear, cluster-validation]
---

# Athletic footwear and apparel

> [!failure] Cluster status: falsified — athletic footwear/apparel is retail-discretionary beta, not a distinct factor; it coheres only under a common consumer shock and shatters on brand-specific product cycles (Jun 2026)
> The athletic/lifestyle brands ([[Nike|NKE]]/[[Lululemon|LULU]]/[[Deckers|DECK]]/[[On Running|ONON]]/[[Under Armour|UAA]]/[[Crocs|CROX]]) do NOT trade as one factor. Intra-corr is 0.371 (below the 0.50 floor), PC1 only 47.7%, and the cohort never returns as a clean cluster at any threshold — at 0.50 only [[Deckers|DECK]]+[[On Running|ONON]] join, and even they sit just under the cut (0.493). The decisive number is a NEGATIVE −0.053 intra-advantage versus the retail/discretionary ETFs: the names track [[XRT]]/[[XLY]] more than each other, so there is no athleisure-specific factor beyond retail-discretionary beta. The cohort does beat the random-basket (p 0.0049) and vol-matched (p 0.0013) nulls — but only via that shared discretionary beta, which the ETF already prices. And the cohesion is not even stable: the 2Y holdout is REGIME-DEPENDENT (test/train ratio 0.60) — tight in 2024 (train 0.62 / PC1 69%) when a common consumer/rates shock dominated, shattered in 2025-26 (test 0.37 / PC1 48%) as brand-specific stories took over. Own [[XRT]] or [[XLY]] for the exposure; picking [[Nike|NKE]] over [[On Running|ONON]] is a single-brand bet, not a factor bet.

The purest brand-momentum sector. An athletic brand's value is its specific franchise heat and product cycle — [[Nike]]'s China reset and wholesale pullback, [[Lululemon]]'s North-American deceleration, [[Deckers]]' HOKA hypergrowth riding atop UGG, [[On Running]]'s premium-running ascent, [[Under Armour]]'s multi-year turnaround, [[Crocs]]' core-brand cash machine dragged by the HEYDUDE acquisition — and those run on brand-specific demand, not a shared "athleisure" factor. Beyond broad retail/consumer-discretionary beta (captured by [[XRT]] or [[XLY]]), there is nothing common to own. The product-cycle calendar is the anti-cluster: it makes every name a single-brand story, except in the windows when a macro consumer shock briefly synchronizes them.

## Sector performance

![[apparel-performance.png]]
*Normalized total return since Jan 2023 — the cohort vs [[XRT]] (the sector ETF it is tested against). See the cluster validation below for whether the cohort is distinct from or replicable by the ETF.*

## Cluster validation

The candidate cohort is six athletic/lifestyle footwear and apparel brands — [[Nike|NKE]], [[Lululemon|LULU]], [[Deckers|DECK]], [[On Running|ONON]], [[Under Armour|UAA]], [[Crocs|CROX]] — tested against broad apparel/accessories ([[Ralph Lauren|RL]]/[[Tapestry|TPR]]/[[VF Corp|VFC]]) and benchmarks (XRT SPDR retail, XLY consumer discretionary, SPY). 1Y window through 2026-06-18, threshold 0.5. Terminology: [[Cohort, cluster, basket]].

### Diagnostics summary

| Diagnostic | Value | Read |
|---|---|---|
| Intra-cluster corr (1Y) | 0.371 [0.296–0.507] | below the 0.50 floor; weekly 0.377 (no tighter on weekly returns) |
| PC1 explained variance | 47.7% | below 50%, with big PC2/PC3 (12.7%/12.1%) — genuinely multi-factor |
| Independence null p | 0.0001 | series co-move at all |
| Random-basket null p | 0.0049 | beats a random 6-pick — but via shared discretionary beta |
| Vol-matched null p | 0.0013 / 0.0024 | beats vol-matched baskets too — still just retail beta |
| Holdout (2Y split) | REGIME-DEPENDENT 0.60 | does NOT survive: train 0.620 → test 0.372; loadings corr 0.22 |
| Threshold clean width | 0.00 | never isolates as a clean cluster at any threshold |
| Intra-adv vs broad apparel (RL/TPR/VFC) | −0.024 | NOT distinct — athletic ≈ broad apparel |
| Intra-adv vs ETFs (XRT/XLY/SPY) | −0.053 | NEGATIVE — the names track the retail ETF more than each other |

All US-listed. Config: `scripts/cluster_configs/nke.yaml`; registry row 2026-06-20.

### Boundary — the cohort shatters; only DECK+ONON pair, and below the cut

![[apparel-cluster-dendrogram-1y.png]]
*Hierarchical clustering at 0.5. The cohort does not hold: only [[Deckers|DECK]]+[[On Running|ONON]] form a pair (premium performance running), and they join just under threshold at 0.493. [[Nike|NKE]], [[Lululemon|LULU]], [[Under Armour|UAA]], and [[Crocs|CROX]] are singletons; the broad-apparel controls [[Ralph Lauren|RL]] and [[VF Corp|VFC]] defect into the retail-ETF block (XRT/XLY/SPY). Six proposed names, no athleisure cluster.*

The threshold scan never returns the cohort as a clean single cluster (zero stable width). At 0.50 only the DECK+ONON pair forms; from 0.60 the contamination is the whole retail complex (RL, TPR, VFC, XRT, XLY) joining at once. This is the grade-2 falsification signature: the names beat random and vol-matched baskets, but only through shared retail/discretionary beta (negative intra-advantage versus the actual ETFs), with no athleisure-specific factor. The one micro-pair (DECK+ONON) is the two premium-running-footwear hypergrowth names — a real sub-story, but a pair sitting under the cut, not a constructive cluster.

### Topology — every name a singleton at 0.5; the cohort closes far above the cut

Reading the candidate cohort by join distance (average linkage, 1−|corr|):

| Join step | Names | Distance (1-\|corr\|) | Read |
|---|---|---|---|
| 1 | DECK + ONON | 0.493 | the only pair under 0.5 — premium performance running |
| 2 | LULU + (DECK+ONON) | 0.585 | above the cut |
| 3 | UAA + CROX | 0.623 | a second loose pair, above the cut |
| 4 | (LULU+DECK+ONON) + (UAA+CROX) | 0.635 | |
| 5 | NKE + rest | 0.667 | the cohort closes far above the cut; NKE is the loosest |

Only one join (DECK+ONON) sits under the 0.5 threshold — the cohort never forms as a whole. PC1 explains just 47.7% (vs >70% for a real cluster), with sizeable PC2 (12.7%) and PC3 (12.1%) — a genuinely multi-factor set, one factor per brand.

### PC1 index weights

![[apparel-cluster-pca-1y.png]]
*PCA on the candidate cohort. PC1 explains only 47.7% (weekly 48.2%) with large secondary components — a multi-factor cohort, the signature of a non-cluster.*

| Ticker | PC1 loading | Loading weight | Ann vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| NKE | 0.370 | 15.2% | 37.6% | 18.0% |
| LULU | 0.404 | 16.5% | 43.0% | 17.1% |
| DECK | 0.447 | 18.3% | 46.8% | 17.4% |
| ONON | 0.429 | 17.6% | 45.4% | 17.2% |
| UAA | 0.402 | 16.5% | 53.7% | 13.7% |
| CROX | 0.392 | 16.0% | 43.2% | 16.6% |

Loadings are middling and nearly uniform, but PC1 captures less than half the variance — there is no dominant common factor to weight. [[Deckers]] and [[On Running]] carry the highest loadings (consistent with their being the only pair that clusters), the higher-vol [[Under Armour]] the lowest weight.

### Distinctness — = the retail/discretionary ETFs, not distinct from broad apparel

![[apparel-cluster-correlation-1y.png]]
*1Y pairwise correlation heatmap. No uniformly-hot athletic block; the names are about as warm against XRT/XLY and against the broad-apparel trio (RL/TPR/VFC) as against each other.*

The decisive number is the −0.053 intra-advantage versus the ETFs: the athletic names correlate with [[XRT]]/[[XLY]] more than with one another, so there is no athleisure-specific factor beyond retail/consumer-discretionary beta. And −0.024 versus broad apparel — so athletic brands are not even separable from [[Ralph Lauren|RL]]/[[Tapestry|TPR]]/[[VF Corp|VFC]]; they are one retail complex. The investable read collapses to the ETF: own [[XRT]] (or [[XLY]]) for the exposure; choosing [[On Running|ONON]] over [[Nike|NKE]] is a pure single-brand momentum bet, not a factor bet.

### Historical tightness evolution

![[apparel-cluster-rolling-tightness-90d.png]]
*Rolling 90-day cohesion, 2023–2026. The cohort oscillates between ~0.33 (brand-specific, diverging) and ~0.60 (macro-shock, converging) — regime-dependent, never a stable cluster.*

| Year | Avg intra-corr | PC1 |
|---|---|---|
| 2023 | 0.612 | 67.8% |
| 2024 | 0.332 | 44.9% |
| 2025 | 0.588 | 66.1% |
| 2026 | 0.335 | 45.0% |

Latest 90-day reading: intra 0.400, PC1 50.6%. Unlike [[Biotech]] (durably loose ~0.42 every year), athletic apparel oscillates: it tightens to ~0.60 when a common consumer/rates shock dominates (2023, 2025, and the holdout's 2024 train half at 0.62) and shatters to ~0.33 when brand-specific product cycles take over (2024, 2026, the holdout's 2025-26 test half at 0.37). That is why the 2Y holdout reads REGIME-DEPENDENT (ratio 0.60, loadings corr only 0.22): the factor structure does not persist out of sample. The cohesion that exists is generic discretionary risk beta — the same thing [[XRT]] prices — switched on and off by the macro regime, not an apparel-specific driver. It is the brand-momentum analogue of the campaign's driver-divergence law: a label spanning names with divergent product cycles only rhymes under a shared shock, and here that shock is already in the ETF.

## Related

- [[Fashion]] — the broad apparel/fashion industry hub; this cohort is the quant cluster-validation of its "athletic" segment
- [[Biotech]] — the sibling falsification by idiosyncratic drivers (durably loose, where this one is regime-dependent)
- [[Nike]], [[Lululemon]], [[Deckers]], [[On Running]] — the higher-cohesion names (DECK+ONON the one pair)
- [[Under Armour]], [[Crocs]] — the loosest singletons
- [[Ralph Lauren]], [[Tapestry]], [[VF Corp]] — the broad-apparel control the cohort is not distinct from
- [[XRT]], [[XLY]] — the retail/discretionary ETFs the cohort resolves to (own these for the exposure)
- [[Vault cluster taxonomy]] — cross-cohort meta-analysis
- [[Cohort, cluster, basket]] — terminology

---

*Created 2026-06-20. 1Y daily log returns through 2026-06-18; config `scripts/cluster_configs/nke.yaml`; registry row 2026-06-20. Cluster validation is structure, not a performance ranking — see `docs/cluster-validation.md`.*
