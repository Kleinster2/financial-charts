---
aliases: [Oil and gas equity beta, Oil majors cluster, Oil equity beta, Big oil cluster, Oil and gas majors cohort]
tags: [concept, cluster-validation, energy, oil-gas, commodity-beta]
---

# Oil and gas equity beta

> [!warning] Cluster status: validated cohesion, but it IS the energy ETF / crude (Jun 2026)
> The big-cap US oil & gas producers ([[ExxonMobil|XOM]]/[[Chevron|CVX]]/[[ConocoPhillips|COP]]/[[EOG Resources|EOG]]) are the tightest, most durable commodity-equity cohort the campaign has measured — intra-corr 0.80, PC1 85%, all nulls reject at the 0.0001 floor, holdout STABLE 0.97. But it is not a distinct factor: intra-advantage versus the energy ETF is only +0.04 (XLE/XOP/crude sit inside the cluster), so it is ETF-replicable — own XLE. Two structural findings: vertical integration does NOT break the commodity-beta law (integrated XOM/CVX and pure-E&P COP/EOG are inseparable, merging at 0.22), and the one genuinely distinct energy factor is oilfield services (SLB/HAL/BKR, +0.34). The fourth confirmation of the commodity-beta law after [[Copper equity beta]], [[Gold equity beta]], and [[Lithium equity beta]] — and its purest case.

The commodity-beta family's oil chapter, and the one that tests whether business model matters. The hypothesis going in: integrated majors ([[ExxonMobil]], [[Chevron]]) carry downstream refining and chemicals that partly hedge crude — refining margins widen when crude falls — so they might decouple from the crude-price factor that pure miners obey. They do not. The integrated majors trade as oil-equity beta indistinguishable from the pure E&P names, because the upstream crude exposure dominates the stock's factor and the downstream offset is second-order. What this cohort owns is the equity expression of the crude-price factor; the durable, *distinct* energy factor lives one step down the value chain, in oilfield services.

## Cluster validation

The candidate cohort is the four big-cap US oil & gas producers — [[ExxonMobil|XOM]], [[Chevron|CVX]] (integrated majors), [[ConocoPhillips|COP]], [[EOG Resources|EOG]] (large E&P) — tested against oilfield services (SLB/HAL/BKR), refiners (VLO/MPC/PSX), and benchmarks (XLE energy ETF, XOP E&P ETF, USO crude).

### Diagnostics summary

| Diagnostic | Value | Read |
|---|---|---|
| Intra-cluster corr (1Y) | 0.802 [0.754–0.853] | very tight; weekly 0.809 (synchronous) |
| PC1 explained variance | 85.2% | near-pure single factor (PC2 only 7.2%) |
| Independence null p | 0.0001 | series co-move |
| Random-basket null p | 0.0001 | beats a random 4-pick at the floor (guaranteed for a commodity cohort) |
| Holdout (2Y split) | STABLE 0.97 | durable across regimes |
| Threshold clean width | 0.00 | producers never isolate from XLE/XOP/crude — embedded, not dispersion |
| Intra-adv vs oilfield services | +0.339 | distinct — services is a separate (activity-cycle) factor |
| Intra-adv vs refiners | +0.171 | weakly distinct — downstream margins partly decouple |
| Intra-adv vs energy ETF (XLE/XOP/USO) | +0.041 | NOT distinct — the cohort IS the ETF / crude |

1Y daily log returns through 2026-06-12, threshold 0.5. All US-listed (synchronous). Config: `scripts/cluster_configs/xom.yaml`; registry row 2026-06-15. Terminology: [[Cohort, cluster, basket]].

### Boundary — producers = the ETF; only services split off

![[oil-majors-cluster-dendrogram-1y.png]]
*Hierarchical clustering at 0.5. Oilfield services (BKR/SLB/HAL, orange) is the one separate branch. Everything else collapses into one green block — producers, refiners, crude (USO), and the ETFs — with XLE sitting inside the XOM/CVX sub-branch and XOP inside the COP/EOG sub-branch. The cohort literally contains its own benchmark.*

The threshold scan never returns the 4-name producer cohort as a clean isolated cluster, because XLE, XOP and USO are inside it at every cut — the zero-width here is the "real but embedded" kind (high intra-corr + stable holdout), not a dispersion falsification. The only thing that separates is oilfield services, which forms its own cluster (join ~0.58 to the rest) and carries a +0.339 intra-advantage — a distinct activity/capex-cycle factor, not the spot-crude factor.

### Topology — integrated and E&P are inseparable

Reading the candidate cohort by join distance (average linkage, 1−|corr|):

| Join step | Names | Distance (1-\|corr\|) | Read |
|---|---|---|---|
| 1 | COP + EOG | 0.147 | E&P pair (corr 0.85) |
| 2 | XOM + CVX | 0.161 | integrated pair (corr 0.84) |
| 3 | (COP+EOG) + (XOM+CVX) | 0.219 | integrated and E&P merge — inseparable |

The integrated majors and the pure E&P names form their own pairs first, but merge at 0.219 (correlation ~0.78) — well below the 0.5 cut. Integration is a second-order distinction in the tape: XOM/CVX's downstream does not give them a different return factor than COP/EOG. This is the structural answer to the test the cohort was built for — business model does not split a commodity-equity cohort; the shared exogenous price does.

### PC1 index weights

![[oil-majors-cluster-pca-1y.png]]
*PCA on the candidate cohort. PC1 explains 85.2% with near-identical loadings (~0.50 each) and a tiny PC2 (7.2%) — a clean, equal-weighted single factor.*

| Ticker | PC1 loading | Loading weight | Ann vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| ExxonMobil (XOM) | 0.499 | 25.0% | 25.4% | 25.8% |
| Chevron (CVX) | 0.499 | 24.9% | 23.2% | 28.2% |
| ConocoPhillips (COP) | 0.507 | 25.4% | 30.5% | 21.8% |
| EOG Resources (EOG) | 0.495 | 24.8% | 26.9% | 24.2% |

The loadings are essentially identical — the four names are interchangeable expressions of one crude-price factor. The lower-vol [[Chevron]] takes a slightly larger raw PC1-mimic weight; the higher-vol [[ConocoPhillips]] a slightly smaller one.

### Distinctness — = XLE, distinct only from services

![[oil-majors-cluster-correlation-1y.png]]
*1Y pairwise correlation heatmap. The producer block is uniformly hot and just as hot against XLE/XOP/USO; oilfield services (SLB/HAL/BKR) is the cooler corner.*

The +0.041 intra-advantage versus the energy ETF is the decisive number: the producers correlate with XLE/XOP/crude essentially as much as with each other, so there is no producer-specific factor beyond energy-sector/crude beta — the smallest distinctness in the whole commodity-beta family (copper +0.033, gold +0.070, lithium ETF-replicable too), which makes oil the *purest* ETF-replicable case. Distinct from oilfield services (+0.339) and weakly from refiners (+0.171, whose crack-spread margins give them a partial offset). The investable read collapses to the ETF: own XLE for oil-equity beta or XOP for the higher-beta E&P tilt; picking [[ExxonMobil]] over [[ConocoPhillips]] is a company bet (asset base, capital return, Guyana vs Permian), not a factor bet.

### Historical tightness evolution

![[oil-majors-cluster-rolling-tightness-90d.png]]
*Rolling 90-day cohesion, 2020–2026. Exceptionally tight and durable — 0.79–0.86 every year, riding the 2020 collapse, the 2022 spike, and the 2024–26 range as one. The most structurally stable commodity-equity cohort measured.*

| Year | Avg intra-corr | PC1 |
|---|---|---|
| 2020 | 0.847 | 88.6% |
| 2021 | 0.856 | 89.2% |
| 2022 | 0.838 | 87.9% |
| 2023 | 0.837 | 87.8% |
| 2024 | 0.790 | 84.3% |
| 2025 | 0.837 | 87.8% |
| 2026 | 0.764 | 82.3% |

The cohort is more durable than copper (holdout 0.82) or lithium (0.77) and rivals gold — consistent with crude being the deepest, most liquid commodity with the most uniformly-levered producers. The slight 2026 easing (0.76) is the only softening in six years. As with every commodity cohort, the durability is uninformative for trading: cohesion is guaranteed when one exogenous price drives every member, which is exactly why the diagnostics that carry the verdict are the threshold scan (never isolates from XLE) and the +0.04 intra-advantage, not the null tests.

## Related

- [[Copper equity beta]], [[Gold equity beta]], [[Lithium equity beta]] — the commodity-beta family; oil is the fourth and purest ETF-replicable case
- [[Oil]] — the underlying commodity driver
- [[ExxonMobil]], [[Chevron]] — the integrated majors (tightest pairs)
- [[ConocoPhillips]], [[EOG Resources]] — the large-cap E&P members
- [[Oilfield services]] — the services/equipment leg one step down the value chain; the validated cohort behind this note's "+0.34 services" finding — a distinct activity/capex-cycle factor (= OIH), the crude pole's sibling in the energy value-chain split
- [[Refiners]] — the downstream leg (= CRAK); only weakly distinct from the majors (+0.193, the crack-spread offset partial), so unlike services it stays attached to the crude pole
- [[Energy and Utilities]] — the broad sector hub
- [[Vault cluster taxonomy]] — cross-cohort meta-analysis

---

*Created 2026-06-15. 1Y daily log returns through 2026-06-12; config `scripts/cluster_configs/xom.yaml`; registry row 2026-06-15. Cluster validation is structure, not a performance ranking — see `docs/cluster-validation.md`.*
