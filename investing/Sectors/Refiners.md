---
aliases: [Refiners, US refiners, Refining, Refiner cohort, Oil refiners]
tags: [sector, energy, oil-gas, refining, cluster-validation]
---

# Refiners

> [!warning] Cluster status: validated cohesion, durable — but = the refiners ETF (CRAK) and only weakly distinct from crude (Jun 2026)
> The US refiners ([[Valero|VLO]]/[[Marathon Petroleum|MPC]]/[[Phillips 66|PSX]]/[[PBF Energy|PBF]]/[[Delek US|DK]]/[[HF Sinclair|DINO]]) trade as one tight, durable factor — intra-corr 0.765 (weekly 0.787), PC1 80.5%, rejecting the random-basket AND vol-matched nulls at the 0.0001 floor, holdout STABLE 0.88. But unlike oilfield services, refiners do NOT decouple from crude: they sit as a sub-block inside the crude/energy cluster (the refiners ETF CRAK joins from threshold 0.30, the oil majors from 0.45), only +0.193 distinct from the majors. The crack-spread/downstream-margin offset is a partial wedge, not a separate factor — refiners are CRAK-replicable energy beta. The asymmetric leg of the energy value chain: services ([[Oilfield services]]) decouples from crude, refiners stay attached. Own CRAK.

The downstream leg of the energy value chain. Refiners buy crude and sell products (gasoline, diesel, jet); their margin is the crack spread, which can widen when crude falls — so in principle they carry a partial hedge against the crude factor that drives the [[Oil and gas equity beta|integrated majors and E&P]]. In the tape that hedge is real but second-order: refiners co-move tightly with each other (one crack-spread/refining-margin factor) yet still trade inside the broad crude/energy complex, joining the majors just below the dendrogram cut. They are distinct from oilfield services (a different value-chain leg entirely) but not from crude beta the way services is.

## Cluster validation

The candidate cohort is the six US refiners — [[Valero|VLO]], [[Marathon Petroleum|MPC]], [[Phillips 66|PSX]], [[PBF Energy|PBF]], [[Delek US|DK]], [[HF Sinclair|DINO]] — tested against the oil majors ([[Oil and gas equity beta|XOM/CVX/COP/EOG]]), oilfield services ([[Oilfield services|SLB/HAL/BKR]]), and benchmarks (CRAK refiners ETF, XLE energy, USO crude, SPY). 1Y window through 2026-06-18, threshold 0.5. Terminology: [[Cohort, cluster, basket]].

### Diagnostics summary

| Diagnostic | Value | Read |
|---|---|---|
| Intra-cluster corr (1Y) | 0.765 [0.676–0.858] | tight; weekly 0.787 (synchronous, all US) |
| PC1 explained variance | 80.5% | strong single factor (weekly 82.3%) |
| Independence null p | 0.0001 | series co-move |
| Random-basket null p | 0.0001 | beats a random 6-pick at the floor |
| Vol-matched null p | 0.0001 (PC1 0.0001) | a real refining-margin factor, not just shared vol (PBF/DK run 55–65% vol) |
| Holdout (2Y split) | STABLE 0.88 | durable (train 0.869 → test 0.764; loadings corr 0.87) |
| Threshold clean width | 0.00 | CRAK inside from 0.30, majors from 0.45 — embedded in crude/energy |
| Intra-adv vs oil majors (XOM/CVX/COP/EOG) | +0.193 | weakly distinct — crack spread is a partial offset, not a separate factor |
| Intra-adv vs oilfield services (SLB/HAL/BKR) | +0.403 | sharply distinct — a different value-chain leg |
| Intra-adv vs ETFs (CRAK/XLE/USO/SPY) | +0.323 | distinct from XLE/USO/market in the average, but CRAK sits inside |

All US-listed (synchronous). Config: `scripts/cluster_configs/vlo.yaml`; registry row 2026-06-19.

### Boundary — a sub-block inside the crude/energy cluster

![[refiners-cluster-dendrogram-1y.png]]
*Hierarchical clustering at 0.5. The six refiners + the refiners ETF CRAK form a tight sub-branch, but it merges with the oil majors (with XLE inside) and crude (USO) into one green crude/energy cluster at ~0.49 — just below the cut. Only oilfield services (BKR/SLB/HAL, orange) stands apart as its own pole. [[SPY]] is separate.*

The threshold scan never isolates the refiners as a clean cluster: CRAK contaminates from threshold 0.30, and the oil majors from 0.45. So the zero width is the "real but embedded" kind (high intra + nulls rejected), and the embedding is in the crude/energy complex itself. This is the structural contrast with [[Oilfield services]]: services split off into its own dendrogram cluster (+0.254, the capex cycle decouples from crude), whereas refiners stay attached to the majors (+0.193, merging at ~0.49). The crack-spread offset gives refiners a partial own-factor — captured by CRAK — but not the clean separation services achieves. Sharply distinct, though, from services (+0.403): the two downstream-adjacent legs do not trade together.

### Topology — a homogeneous block; PSX trades with the pure refiners

Reading the candidate cohort by join distance (average linkage, 1−|corr|):

| Join step | Names | Distance (1-\|corr\|) | Read |
|---|---|---|---|
| 1 | VLO + MPC | 0.142 | tightest pair (the two largest independents) |
| 2 | PSX + (VLO+MPC) | 0.161 | Phillips 66 joins early despite its midstream/chemicals |
| 3 | DINO + core | 0.229 | HF Sinclair joins |
| 4 | PBF + DK | 0.242 | the smaller, higher-vol pair |
| 5 | (PBF+DK) + core | 0.266 | cohort closes below 0.27 |

All six join below distance 0.27 (correlation above 0.73) — a homogeneous block. [[Valero]]+[[Marathon Petroleum]] are the tightest pair; notably [[Phillips 66]] (the most diversified, with large midstream + chemicals) still joins the pure refiners early (0.161), so its refining leg dominates its return factor. [[PBF Energy]] and [[Delek US]] (the smaller, higher-vol names) form their own pair before joining.

### PC1 index weights

![[refiners-cluster-pca-1y.png]]
*PCA on the candidate cohort. PC1 explains 80.5% (weekly 82.3%) with near-identical loadings (0.39–0.42) — a clean single factor.*

| Ticker | PC1 loading | Loading weight | Ann vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| VLO | 0.421 | 17.2% | 36.6% | 19.0% |
| MPC | 0.417 | 17.0% | 34.4% | 20.1% |
| PSX | 0.410 | 16.8% | 31.5% | 21.6% |
| PBF | 0.402 | 16.4% | 65.4% | 10.2% |
| DK | 0.390 | 15.9% | 54.9% | 11.7% |
| DINO | 0.408 | 16.7% | 38.9% | 17.4% |

Near-equal loadings — the six are interchangeable expressions of one refining-margin factor. But the raw PC1-mimic weights diverge sharply on volatility: the lower-vol majors-scale refiners ([[Phillips 66]] 21.6%, [[Marathon Petroleum]] 20.1%) carry roughly double the investable weight of the high-vol small-caps ([[PBF Energy]] 10.2%, [[Delek US]] 11.7%) — the same factor, but PBF/DK need far less notional to reproduce the standardized shock.

### Distinctness — = CRAK, weakly distinct from crude, sharply distinct from services

![[refiners-cluster-correlation-1y.png]]
*1Y pairwise correlation heatmap. The refiner block is uniformly hot and just as hot against CRAK; warm against the majors/XLE/USO; cooler against oilfield services and cool against SPY.*

Two numbers define the cohort. +0.193 versus the oil majors: refiners have a partial own-factor (the crack spread), but they remain inside the crude/energy complex — weakly distinct, not a separable pole. And CRAK sitting inside the cohort from threshold 0.30: the partial own-factor is exactly what the refiners ETF captures. So the investable read is CRAK — it holds these names and tracks the refining-margin factor; a bespoke six-name basket adds nothing. The one clean separation is from oilfield services (+0.403): refiners and services are adjacent in the value chain but trade as distinct factors (refining margin vs activity/capex cycle). Distinct from [[SPY]] (low market beta).

### Historical tightness evolution

![[refiners-cluster-rolling-tightness-90d.png]]
*Rolling 90-day cohesion, 2021–2026. Durably tight — 0.78–0.85 most years, with a 2025 peak (0.85) and a 2026 easing (0.74).*

| Year | Avg intra-corr | PC1 |
|---|---|---|
| 2021 | 0.798 | 83.2% |
| 2022 | 0.791 | 82.6% |
| 2023 | 0.793 | 82.9% |
| 2024 | 0.781 | 81.9% |
| 2025 | 0.846 | 87.3% |
| 2026 | 0.737 | 78.3% |

Latest 90-day reading: intra 0.786, PC1 82.3%. The refining-margin factor is durably tight (holdout STABLE 0.88, more durable than oilfield services' 0.74) — refiners share one crack-spread/throughput cycle and a near-identical product slate, so they do not decohere. The 2026 easing (0.74) tracks crack spreads normalizing from the 2022–23 highs. The durability without distinctness is the signature: a real, persistent factor that is nonetheless CRAK / energy beta, not a separable basket.

## Related

- [[Oil and gas equity beta]] — the crude pole (= XLE); refiners merge with it at ~0.49 (only +0.193 distinct)
- [[Oilfield services]] — the services pole (= OIH); sharply distinct from refiners (+0.403); the value-chain leg that DOES decouple from crude
- [[Valero]], [[Marathon Petroleum]], [[Phillips 66]] — the large independents + integrated-downstream
- [[PBF Energy]], [[Delek US]], [[HF Sinclair]] — the smaller / mid-cap refiners
- [[Gulf Coast refiners]] — the USGC heavy-crude complex (the Venezuela-return thesis sub-angle)
- [[Refining slate rigidity]] — why slate configuration constrains crude substitution
- [[Oil]] — the crude input; products are the output (the crack spread between them is the factor)
- [[Energy and Utilities]] — the broad sector hub
- [[Vault cluster taxonomy]] — cross-cohort meta-analysis

---

*Created 2026-06-19. 1Y daily log returns through 2026-06-18; config `scripts/cluster_configs/vlo.yaml`; registry row 2026-06-19. Cluster validation is structure, not a performance ranking — see `docs/cluster-validation.md`.*
