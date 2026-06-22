---
aliases: [Chemicals, Chemical industry, Chemicals cohort, Commodity chemicals, Industrial gases]
tags: [sector, materials, chemicals, cluster-validation]
---

# Chemicals

> [!failure] Cluster status: falsified — "chemicals" is not one factor; it splits into cyclical commodity chems and defensive industrial gases (Jun 2026)
> The chemicals names ([[Linde|LIN]]/[[Air Products|APD]]/[[Dow|DOW]]/[[LyondellBasell|LYB]]/[[Celanese|CE]]/[[Eastman Chemical|EMN]]) do NOT trade as one factor — intra-corr 0.462 (below the 0.50 floor), PC1 57%, and the threshold scan never returns a clean cluster. They do beat the random-basket and vol-matched nulls (p 0.0002 / 0.0001) — there is real shared materials/cyclical beta — but the +0.168 intra-advantage over [[XLB]] is delivered by a SPLIT, not a single factor: the commodity/petrochemical names [[Dow|DOW]]+[[LyondellBasell|LYB]] (join 0.117) + [[Celanese|CE]] form a tight cyclical pole, while the industrial gases [[Linde|LIN]] and [[Air Products|APD]] are each near-singletons that pair only at 0.520 (above the cut), and [[Eastman Chemical|EMN]] drifts to the materials ETF. Two opposite drivers under one label — cyclical petrochemical spreads vs defensive, contracted gas oligopoly — so there is no single "chemicals" factor; own the commodity-chem names and the gases separately.

The split-personality sector. "Chemicals" bundles two businesses with opposite economics: commodity/petrochemicals ([[Dow|DOW]], [[LyondellBasell|LYB]], [[Celanese|CE]]) live on ethylene/propylene spreads, oil, and global demand — deeply cyclical, high-vol — while industrial gases ([[Linde|LIN]], [[Air Products|APD]]) are contracted, oligopolistic, take-or-pay utilities of the materials world — defensive and low-vol. They share enough materials beta to beat a random basket, but they are not one factor; the gases barely even correlate with each other (Linde's quality compounding vs Air Products' project/activist troubles).

## Sector performance

![[chems-performance.png]]
*Normalized total return since Jan 2023 — the cohort vs [[XLB]] (the sector ETF it is tested against). See the cluster validation below for whether the cohort is distinct from or replicable by the ETF.*

## Cluster validation

The candidate cohort is six chemicals names spanning industrial gases and commodity/specialty chemicals — [[Linde|LIN]], [[Air Products|APD]], [[Dow|DOW]], [[LyondellBasell|LYB]], [[Celanese|CE]], [[Eastman Chemical|EMN]] — tested against the materials sector ETF (XLB) and market (SPY). 1Y window through 2026-06-18, threshold 0.5. Terminology: [[Cohort, cluster, basket]].

### Diagnostics summary

| Diagnostic | Value | Read |
|---|---|---|
| Intra-cluster corr (1Y) | 0.462 [0.205–0.883] | below the 0.50 floor; weekly 0.430 |
| PC1 explained variance | 56.5% | with big PC2 (19%) — the gases-vs-commodity axis |
| Independence null p | 0.0001 | series co-move |
| Random-basket null p | 0.0002 | beats a random 6-pick — via shared materials/cyclical beta |
| Vol-matched null p | 0.0001 | beats vol-matched baskets too |
| Holdout (2Y split) | WEAKENED 0.79 | train 0.587 → test 0.463; loadings corr 0.36 (unstable) |
| Threshold stable width | 0.00 (none) | never a clean single cluster |
| Intra-adv vs ETF (XLB/SPY) | +0.168 | positive — but delivered by a split, not one factor |

All US-listed. Config: `scripts/cluster_configs/lin.yaml`; registry row 2026-06-20.

### Boundary — commodity chems cluster; the gases are near-singletons

![[chems-cluster-dendrogram-1y.png]]
*Hierarchical clustering at 0.5. The commodity/petrochemical names [[Dow|DOW]]/[[LyondellBasell|LYB]]/[[Celanese|CE]] form a tight cluster; [[Eastman Chemical|EMN]] pairs with the materials ETF [[XLB]]; and the industrial gases [[Linde|LIN]] and [[Air Products|APD]] are separate singletons. Six proposed names, no single chemicals cluster — the label spans two opposite drivers.*

The threshold scan never returns the six as a clean cluster (zero stable width). The cohort beats the random/vol-matched nulls (shared materials beta is real), but it is a grade-2/driver-divergence falsification: the cohesion is a blend of a tight cyclical commodity-chem pole and a defensive gas pole that barely correlate. It is the materials analogue of [[Building products]] (real cohesion that splits by driver), but here the split is cyclical-vs-defensive rather than two end-markets.

### Topology — a commodity-chem core, the gases joining last

Reading the candidate cohort by join distance (average linkage, 1−|corr|):

| Join step | Names | Distance (1-\|corr\|) | Read |
|---|---|---|---|
| 1 | DOW + LYB | 0.117 | the commodity/petrochemical core (ethylene spreads) |
| 2 | CE + (DOW+LYB) | 0.284 | Celanese joins the cyclical pole |
| 3 | EMN + cyclical pole | 0.474 | Eastman joins, looser |
| 4 | LIN + APD | 0.520 | the industrial gases pair — only ABOVE the cut |
| 5 | gases + commodity pole | 0.680 | the two poles merge far above the cut |

The commodity-chem pole (DOW/LYB/CE) closes tightly at 0.284, but the industrial gases ([[Linde|LIN]]+[[Air Products|APD]]) join each other only at 0.520 — above the 0.5 cut — and the two poles bridge at 0.680. So the cohort is two factors, and the gas "pole" is barely a pole. PC1 (56.5%) is the shared materials beta; PC2 (19%) is the cyclical-vs-defensive split.

### PC1 index weights

![[chems-cluster-pca-1y.png]]
*PCA on the candidate cohort. PC1 explains 56.5% (weekly 54.3%); the commodity chems load high, the gases low — PC1 is mostly the cyclical pole.*

| Ticker | PC1 loading | Loading weight | Ann vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| LIN | 0.270 | 11.2% | 18.2% | 21.8% |
| APD | 0.331 | 13.8% | 26.1% | 18.7% |
| DOW | 0.472 | 19.6% | 46.2% | 15.1% |
| LYB | 0.451 | 18.8% | 45.4% | 14.7% |
| CE | 0.478 | 19.9% | 55.8% | 12.6% |
| EMN | 0.403 | 16.8% | 34.5% | 17.2% |

The commodity chems ([[Dow|DOW]]/[[LyondellBasell|LYB]]/[[Celanese|CE]]) carry the highest PC1 loadings (~0.45–0.48) — PC1 is mostly the cyclical-petrochemical factor — while [[Linde|LIN]] loads lowest (0.270, the defensive low-vol gas). Inverse-vol weighting flips it (the low-vol gases get the most index weight), underscoring that the two halves are different animals.

### Distinctness — beats the ETF only by splitting

![[chems-cluster-correlation-1y.png]]
*1Y pairwise correlation heatmap. A hot DOW/LYB/CE block; LIN and APD cool against everything (including each other); EMN intermediate.*

The +0.168 intra-advantage over [[XLB]] is real but misleading: it reflects a tight commodity-chem sub-cluster plus two defensive gases, not a single chemicals factor. XLB itself is dominated by [[Linde|LIN]] (its largest holding), so the gas leg is effectively the ETF while the commodity leg is the distinct-but-cyclical piece. The investable read: there is no "chemicals" factor — own the commodity/petrochemical names ([[Dow|DOW]]/[[LyondellBasell|LYB]]/[[Celanese|CE]]) for the cyclical spread bet and the gases ([[Linde|LIN]]/[[Air Products|APD]]) as separate defensive compounders.

### Historical tightness evolution

![[chems-cluster-rolling-tightness-90d.png]]
*Rolling 90-day cohesion, 2020–2026. Tight in the 2020 shock (0.76), then loosening to 0.42–0.64 as the cyclical and defensive halves diverged; 0.47 in 2026.*

| Year | Avg intra-corr | PC1 |
|---|---|---|
| 2020 | 0.764 | 80.5% |
| 2021 | 0.579 | 66.3% |
| 2022 | 0.633 | 69.7% |
| 2023 | 0.642 | 70.7% |
| 2024 | 0.423 | 55.2% |
| 2025 | 0.605 | 67.7% |
| 2026 | 0.465 | 57.4% |

Latest 90-day reading: intra 0.385, PC1 50.9%. Chemicals cohered in the 2020 macro shock (everything sold off together) and has loosened since as the cyclical commodity-chem and defensive industrial-gas halves diverged — the holdout's WEAKENED 0.79 confirms the factor structure does not persist. Like [[Building products]] and [[Steel and aluminum equity beta|steel & aluminum]], it is a materials label that splits by driver rather than trading as one factor.

## Related

- [[Building products]], [[Steel and aluminum equity beta]] — the other materials/industrial labels that split by driver
- [[Dow]], [[LyondellBasell]], [[Celanese]] — the cyclical commodity-chem pole
- [[Linde]], [[Air Products]] — the defensive industrial-gas names (near-singletons)
- [[Eastman Chemical]] — the specialty name that drifts to XLB
- [[XLB]] — the materials ETF (dominated by Linde)
- [[Vault cluster taxonomy]] — cross-cohort meta-analysis
- [[Cohort, cluster, basket]] — terminology

---

*Created 2026-06-20. 1Y daily log returns through 2026-06-18; config `scripts/cluster_configs/lin.yaml`; registry row 2026-06-20. Cluster validation is structure, not a performance ranking — see `docs/cluster-validation.md`.*
