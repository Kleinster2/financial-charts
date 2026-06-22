---
aliases: [Hospital operators, Hospital chains, Acute-care hospitals, Hospital companies, Hospitals cohort]
tags: [sector, healthcare, hospitals, cluster-validation]
---

# Hospital operators

> [!warning] Cluster status: the core three (HCA/THC/UHS) is a distinct but moderate hospital-operator factor — notably uncorrelated with the payers, and not captured by any ETF; the full four-name cohort is dragged below the floor by the distressed [[Community Health Systems|CYH]] outlier (Jun 2026)
> The acute-care hospital operators ([[HCA Healthcare|HCA]]/[[Tenet Healthcare|THC]]/[[Universal Health Services|UHS]]/[[Community Health Systems|CYH]]) do not hold as one factor at four names — intra-corr 0.396, BELOW the 0.50 floor, no clean threshold band ("boundary-dependent / falsification candidate"), nulls rejected only weakly (random-basket 0.014, vol-matched 0.012) — because [[Community Health Systems|CYH]] (the distressed, heavily-levered small-cap) is a near-orthogonal outlier (corr 0.16-0.35, PC1 weight 9.8%, joins only at distance 0.773). Drop CYH and the core three are a distinct, moderately-robust factor: intra 0.566 (weekly 0.609), PC1 71.1%, rejecting all three nulls (random-basket 0.0023, vol-matched 0.0025), a WIDE separable band [0.50-0.70] (width 0.20), holdout WEAKENED 0.80 on level but loadings-corr 0.97 (structure intact, eroding amplitude). Two findings stand regardless: (1) hospital operators are NOT the "healthcare providers" ETF — [[IHF]] is payer-dominated and clusters with the managed-care names ([[UnitedHealth|UNH]]/[[Elevance Health|ELV]], fusing at 0.125), so the core carries a +0.304 intra-advantage over it and no liquid ETF cleanly captures the hospital factor; and (2) hospitals are nearly UNcorrelated with the payers (corr 0.085, +0.480 intra-advantage) — the providers-vs-payers counterparty split on medical-cost trend. Distinct from [[XLV]] (+0.355) and the market (+0.424) too. See below.

The provider side of the healthcare-cost equation. Hospital operators earn on admissions, acuity, and payer mix, and bear the labor-cost and policy (Medicaid/exchange) risk — the mirror image of the managed-care payers, who profit when medical costs fall. That counterparty relationship is the cohort's defining structural feature: the hospitals barely co-move with [[UnitedHealth|UNH]]/[[Elevance Health|ELV]]. The acute-care model is shared enough across [[HCA Healthcare|HCA]], [[Tenet Healthcare|THC]], and [[Universal Health Services|UHS]] to form a real factor, but it is only moderately tight and has loosened since 2023 as the operators' strategies diverged (Tenet's ambulatory shift, UHS's behavioral mix) and labor/policy pressures hit unevenly. [[Community Health Systems|CYH]], a distressed rural operator trading on balance-sheet survival, decoupled entirely.

## Sector performance

![[hospitals-performance.png]]
*Normalized total return since Jan 2023, the four operators vs broad healthcare [[XLV]]. The core three ([[HCA Healthcare|HCA]]/[[Tenet Healthcare|THC]]/[[Universal Health Services|UHS]]) compounded well ahead of XLV (the distinct, well-performing hospital factor), with [[Tenet Healthcare|THC]] the leader on its ambulatory-surgery re-rating; [[Community Health Systems|CYH]] is the visible outlier, roughly flat-to-down on its leverage/survival story — the divergence behind the four-name cohort failing while the core three hold.*

## Cluster validation

The candidate cohort is four US acute-care hospital operators — [[HCA Healthcare|HCA]] (the scale leader), [[Tenet Healthcare|THC]] (hospitals + USPI ambulatory surgery), [[Universal Health Services|UHS]] (acute + behavioral), [[Community Health Systems|CYH]] (distressed rural) — tested against the healthcare-providers ETF ([[IHF]]), broad healthcare ([[XLV]]), the managed-care payers ([[UnitedHealth|UNH]]/[[Elevance Health|ELV]]), and the market (SPY). 1Y window through 2026-06-18 (198 obs), threshold 0.5. Terminology: [[Cohort, cluster, basket]].

### Diagnostics summary (full four-name cohort)

| Diagnostic | Value | Read |
|---|---|---|
| Intra-cluster corr (1Y) | 0.396 [0.164–0.603] | BELOW the floor; weekly 0.540 (CYH depresses daily); core-3 is 0.566 |
| PC1 explained variance | 56.4% | Weak as four; CYH carries a big idiosyncratic PC2 (23%) |
| Independence null p (10k) | 0.0001 | Series co-move |
| Random-basket null p (10k) | 0.014 | Beats a random 4-pick only WEAKLY (CYH dilutes) |
| Vol-matched null p (10k) | 0.012 | Weak — not the 0.0001 of a tight cohort |
| Holdout (2Y split) | WEAKENED 0.70, loadings-corr 0.95 | train 0.568 → test 0.396; CYH's drag worsens |
| Threshold stable width | 0.00 (none) | Never a clean 4-name cluster — boundary-dependent |
| Intra-adv vs providers ETF (IHF) | +0.133 | IHF is payer-dominated (clusters with UNH/ELV) |
| Intra-adv vs broad healthcare (XLV) | +0.199 | Distinct from broad healthcare |
| Intra-adv vs payers (UNH/ELV) | +0.300 | Near-zero corr — the counterparty split |

Config: `scripts/cluster_configs/hospitals.yaml` (full), `sub_hospitals_core.yaml` (core-3); registry rows 2026-06-21.

### Boundary — the hospitals separate from the payer-dominated "providers" ETF

![[hospitals-cluster-dendrogram-1y.png]]
*Hierarchical clustering at 0.5. The hospital core {[[Tenet Healthcare|THC]]/[[HCA Healthcare|HCA]]/[[Universal Health Services|UHS]]} (orange) is its own cluster, entirely separate from {[[Elevance Health|ELV]]/[[IHF]]/[[UnitedHealth|UNH]]} (green) — note [[IHF]] fuses with [[UnitedHealth|UNH]] at just 0.125, the proof that the "healthcare providers" ETF is really a payer ETF. The two superclusters merge only at ~0.82 (the providers-vs-payers counterparty gap). [[Community Health Systems|CYH]] is a far outlier (joins at ~0.69); [[XLV]] and SPY sit apart.*

The full four-name threshold scan returns no clean band — the cohort never forms an uncontaminated single cluster, because [[Community Health Systems|CYH]] only joins at 0.773. That is a CYH-outlier artifact, not ETF contamination (the ETFs are on the other branch). The core-three sub-cohort resolves it (below).

### Topology — a three-name core and a distressed outlier

Reading the candidate cohort by join distance (average linkage, 1−|corr|):

| Join step | Names | Distance (1-\|corr\|) | Read |
|---|---|---|---|
| 1 | HCA + UHS | 0.397 | the scale/acute core (corr 0.60) |
| 2 | THC + (HCA+UHS) | 0.453 | Tenet joins — the core three close |
| 3 | CYH + core | 0.773 | [[Community Health Systems\|CYH]] joins last, far above the cut — the outlier |

The core three close by 0.453; [[Community Health Systems|CYH]] (corr 0.16-0.35 to the rest) only at 0.773. PC1 explains 56.4% as four, with a large PC2 (23.1%) that is the CYH idiosyncratic axis.

### PC1 index weights — CYH the low-weight outlier

![[hospitals-cluster-pca-1y.png]]
*PCA on the four-name cohort. The core three load evenly (0.54–0.56); [[Community Health Systems|CYH]] loads 0.30 and carries the smallest raw weight (9.8%) at the highest vol (56%) — structurally a satellite, not a core member.*

| Ticker | PC1 loading | Loading weight | Ann vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| HCA | 0.555 | 28.46% | 29.15% | 34.50% |
| THC | 0.559 | 28.66% | 38.48% | 26.33% |
| UHS | 0.537 | 27.53% | 33.08% | 29.41% |
| CYH | 0.300 | 15.35% | 55.60% | 9.76% |

### Distinctness — a real factor, and decidedly not the payers

![[hospitals-cluster-correlation-1y.png]]
*1Y pairwise correlation heatmap. The core three are warm (0.52–0.60); CYH is cool against everything; the payers (UNH/ELV) and IHF are cool against the hospitals (the counterparty separation); XLV mildly warm; SPY cool.*

The intra-advantage numbers (core three): +0.355 vs [[XLV]], +0.304 vs [[IHF]], +0.424 vs the market, and the standout +0.480 vs the payers ([[UnitedHealth|UNH]]/[[Elevance Health|ELV]], corr 0.085). The payer number is the structural signature — hospitals (providers) and managed care (payers) sit on opposite sides of the medical-cost-trend trade, so they barely co-move. And because [[IHF]], the only "healthcare providers" ETF, is payer-weighted, there is no liquid ETF that expresses the hospital-operator factor — the basket is the only way to own it.

### Historical tightness evolution — tight pre-2024, loosened since

![[hospitals-cluster-rolling-tightness-90d.png]]
*Rolling 90-day cohesion, 2021–2026 (four-name). The core was tight through 2021–23 (0.75–0.79 on the three-name basis) and loosened to 0.55–0.67 in 2024–26 as operator strategies diverged and labor/policy pressures hit unevenly; the four-name line sits lower throughout as CYH detaches.*

| Year | Core-3 avg intra-corr | Core-3 PC1 |
|---|---|---|
| 2021 | 0.751 | 83.4% |
| 2022 | 0.749 | 83.3% |
| 2023 | 0.785 | 85.7% |
| 2024 | 0.645 | 76.4% |
| 2025 | 0.668 | 78.0% |
| 2026 | 0.554 | 70.3% |

*The core-3 was a tight factor (0.75–0.79) through 2023, then loosened to ~0.55 by 2026 — which is why the holdout reads WEAKENED 0.80 even as the factor structure stays intact (loadings-corr 0.97). A real but moderate, currently-loosening hospital factor.*

### Sub-cohort — the core three (ex-CYH): the distinct factor

Dropping the [[Community Health Systems|CYH]] outlier isolates the tradeable factor — the [[Self-storage REITs|self-storage-big-3]] / [[IT services|IT-services-ex-Wipro]] pattern:

![[hospitals-core-cluster-dendrogram-1y.png]]
*Hierarchical clustering of the core three at 0.5. {HCA/THC/UHS} form one clean cluster, separate from the payer/IHF block and XLV — merging only at the top.*

| Diagnostic | Full 4 | Core 3 (ex-CYH) |
|---|---|---|
| Intra-corr (1Y) | 0.396 | 0.566 (weekly 0.609) |
| PC1 | 56.4% | 71.1% (weekly 74.1%) |
| Random-basket / vol-matched null | 0.014 / 0.012 (weak) | 0.0023 / 0.0025 (reject) |
| Threshold band | none (boundary-dependent) | [0.50–0.70] w0.20 (MODERATELY ROBUST) |
| Holdout | WEAKENED 0.70 | WEAKENED 0.80 (loadings-corr 0.97) |
| Intra-adv vs payers (UNH/ELV) | +0.300 | +0.480 |

The core three clear the distinctness bar — all nulls reject, a wide robust separable band, large intra-advantages over every control, and a durable factor structure (loadings-corr 0.97) — but only moderately: intra 0.566 sits in the partial band, and cohesion has loosened since 2023. A real, ownable-only-as-a-basket hospital factor, weaker than the campaign's tightest distinct cohorts. [[Community Health Systems|CYH]] is the distressed satellite — own the core, not the laggard.

## Where this sits in the healthcare map

Hospital operators complete the healthcare cluster map, and the pattern across it is consistent — the distinct healthcare factors are the ones with a driver no broad ETF prices:

- [[Drug distributors]] — distinct (the big-3 logistics oligopoly, +0.502 vs XLV, the campaign's most ETF-independent).
- [[Life science tools]] — distinct (the picks-and-shovels factor).
- Hospital operators (this note) — distinct in the core three (+0.355 vs XLV), and uniquely defined by being the counterparty to the payers (+0.480) — but moderate and loosening.
- [[Contract research organizations]] — falsified (shatters; the coherent CROs are absorbed into life-science tools).
- Managed care, biotech, pharma, medtech — ETF-replicable / their own prior tests.

The recurring healthcare lesson: XLV is a blend of unlike businesses (payers, providers, pharma, devices, tools), so several sub-sectors carry real, ETF-independent factors. Hospitals add the counterparty twist — distinct not only from XLV but from the payers who sit on the other side of the cost trade.

## Related

- [[HCA Healthcare]], [[Tenet Healthcare]], [[Universal Health Services]], [[Community Health Systems]] — the cohort members (HCA/THC/UHS the core; CYH the distressed outlier)
- [[UnitedHealth]], [[Elevance Health]] — the managed-care payers (counterparties, not peers; near-zero correlation)
- [[IHF]] — the payer-dominated "healthcare providers" ETF the hospitals separate from; [[XLV]] — broad healthcare
- [[Drug distributors]], [[Life science tools]], [[Contract research organizations]] — the other healthcare cluster tests
- [[Vault cluster taxonomy]] — cross-cohort meta-analysis
- [[Cohort, cluster, basket]] — terminology

---

*Created 2026-06-21. 1Y daily log returns through 2026-06-18; configs `scripts/cluster_configs/hospitals.yaml` + `sub_hospitals_core.yaml`; registry rows 2026-06-21. Cluster validation is structure, not a performance ranking — see `docs/cluster-validation.md`.*
