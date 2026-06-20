---
aliases: [Reinsurers and specialty P&C, Reinsurers, P&C reinsurers, Specialty P&C insurers, Bermuda reinsurers]
tags: [sector, financials, insurance, reinsurance, cluster-validation]
---

# Reinsurers and specialty P&C

> [!warning] Cluster status: real P&C-insurance cohesion but NOT a distinct factor — reinsurers do not separate from primary carriers; it is one P&C insurance complex (= KIE) (Jun 2026)
> The Bermuda reinsurers and specialty P&C insurers ([[RenaissanceRe|RNR]]/[[Everest Group|EG]]/[[Arch Capital|ACGL]]/[[Axis Capital|AXS]]/[[Markel|MKL]]/[[RLI]]) cohere moderately — intra-corr 0.565, PC1 64% — and beat the random-basket and vol-matched nulls (p 0.0002 / 0.0001), so there is real shared P&C-insurance beta. But there is NO distinct reinsurance/catastrophe factor. The decisive number is a NEGATIVE −0.034 intra-advantage versus the primary carriers ([[Travelers|TRV]]/[[Chubb|CB]]): the reinsurers correlate with primary P&C *more* than with each other. The threshold scan never isolates them (zero stable width) — the insurance ETF [[KIE]] and the primary carriers sit inside the cluster at every cut. So reinsurers/specialty are not a separable cat-cycle factor; they are part of one P&C insurance complex, owned through [[KIE]]. The cat cycle moves the whole complex (primaries included), not a reinsurance-only sub-factor.

The catastrophe cycle is not a separable factor. Reinsurers price catastrophe risk and the hard/soft reinsurance market, but those forces — cat losses, reinsurance and primary pricing, reserve development, and the bond/equity portfolios every insurer carries — move primary P&C carriers too. So the reinsurers don't carve out a distinct factor from [[Travelers|TRV]]/[[Chubb|CB]]; the whole P&C insurance complex trades together, and the cleanest expression is the broad insurance ETF [[KIE]], not a reinsurance basket.

## Cluster validation

The candidate cohort is six Bermuda reinsurers and specialty P&C insurers — [[RenaissanceRe|RNR]], [[Everest Group|EG]], [[Arch Capital|ACGL]], [[Axis Capital|AXS]], [[Markel|MKL]], [[RLI]] — tested against large primary P&C carriers ([[Travelers|TRV]]/[[Chubb|CB]]), the insurance ETF [[KIE]], and market (SPY). 1Y window through 2026-06-18, threshold 0.5. Terminology: [[Cohort, cluster, basket]].

### Diagnostics summary

| Diagnostic | Value | Read |
|---|---|---|
| Intra-cluster corr (1Y) | 0.565 [0.447–0.725] | above the 0.50 floor; weekly 0.527 |
| PC1 explained variance | 64.1% | a dominant P&C-insurance factor (weekly 61.6%) |
| Independence null p | 0.0001 | series co-move |
| Random-basket null p | 0.0002 | real cohesion — via shared P&C-insurance beta |
| Vol-matched null p | 0.0001 | beats vol-matched baskets too |
| Holdout (2Y split) | WEAKENED 0.77 | train 0.732 → test 0.565; loadings corr 0.18 (eroding) |
| Threshold stable width | 0.00 (none) | never isolates — KIE/primary carriers contaminate |
| Intra-adv vs primary carriers (TRV/CB) | −0.034 | NEGATIVE — reinsurers track primaries more than each other |
| Intra-adv vs ETFs (KIE/SPY) | +0.261 | tighter than KIE/market average, but KIE is never separable |

All US/Bermuda-listed. Config: `scripts/cluster_configs/rnr.yaml`; registry row 2026-06-20.

### Boundary — reinsurers, primary carriers, and KIE all in one cluster

![[reins-cluster-dendrogram-1y.png]]
*Hierarchical clustering at 0.5. The six reinsurers/specialty names cluster with the primary carriers ([[Travelers|TRV]]/[[Chubb|CB]]) and the insurance ETF [[KIE]] — the whole P&C insurance complex fuses; only SPY is apart. The primary carriers being inside the reinsurers' cluster (and the negative intra-advantage) is the mark of a non-distinct cohort.*

The negative intra-advantage versus the primary carriers is decisive: the reinsurers are not more cohesive among themselves than they are with TRV/CB, so there is no separable reinsurance factor. The threshold scan confirms it (zero stable width — KIE and the primaries contaminate at every cut). The cohort beats the random/vol-matched nulls only on shared P&C-insurance beta, which [[KIE]] already provides.

### Topology — a specialty core, MKL and RLI looser

Reading the candidate cohort by join distance (average linkage, 1−|corr|):

| Join step | Names | Distance (1-\|corr\|) | Read |
|---|---|---|---|
| 1 | ACGL + AXS | 0.275 | the Bermuda specialty pair — the tightest |
| 2 | RNR + (ACGL+AXS) | 0.365 | the cat reinsurer joins |
| 3 | EG + core | 0.391 | Everest joins |
| 4 | MKL + core | 0.450 | Markel (mini-Berkshire) joins, looser |
| 5 | RLI + core | 0.508 | the high-quality specialty primary joins just above the cut |

The Bermuda specialty/reinsurance names (ACGL/AXS/RNR/EG) form the core; [[Markel|MKL]] (its Ventures/equity-portfolio arm adds an idiosyncratic component) and [[RLI]] (a low-beta, disciplined specialty primary) are looser, with RLI joining only above the 0.5 cut. PC1 explains 64% — a P&C factor, but one shared with the primaries.

### PC1 index weights

![[reins-cluster-pca-1y.png]]
*PCA on the candidate cohort. PC1 explains 64.1% (weekly 61.6%) — the shared P&C-insurance factor.*

| Ticker | PC1 loading | Loading weight | Ann vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| RNR | 0.407 | 16.7% | 23.6% | 15.7% |
| EG | 0.400 | 16.4% | 24.9% | 14.6% |
| ACGL | 0.449 | 18.4% | 20.4% | 20.0% |
| AXS | 0.438 | 17.9% | 22.8% | 17.5% |
| MKL | 0.387 | 15.9% | 19.0% | 18.5% |
| RLI | 0.362 | 14.8% | 24.0% | 13.7% |

The Bermuda specialty names ([[Arch Capital|ACGL]]/[[Axis Capital|AXS]]) carry the highest loadings; [[RLI]] and [[Markel|MKL]] the lowest (the more idiosyncratic names).

### Distinctness — not distinct from primary P&C; = KIE

![[reins-cluster-correlation-1y.png]]
*1Y pairwise correlation heatmap. A moderately warm reinsurer block, but TRV/CB and KIE are about as warm against the reinsurers as the reinsurers are against each other — no distinct reinsurance block.*

The −0.034 intra-advantage versus the primary carriers is the verdict: reinsurance/specialty P&C is not a factor distinct from primary P&C. And while the cohort is +0.261 versus KIE/SPY on average, [[KIE]] sits inside the cluster (never separable) — KIE holds all of these names plus the primaries, so it IS the factor. The investable read: own [[KIE]] for the P&C-insurance complex; there is no separable reinsurance/cat-cycle basket to own.

### Historical tightness evolution

![[reins-cluster-rolling-tightness-90d.png]]
*Rolling 90-day cohesion, 2021–2026. Tightest in the 2021–22 hard-market window (~0.73), eroding to ~0.56 as the reinsurance cycle matured.*

| Year | Avg intra-corr | PC1 |
|---|---|---|
| 2021 | 0.734 | 77.9% |
| 2022 | 0.683 | 73.7% |
| 2023 | 0.632 | 69.4% |
| 2024 | 0.571 | 64.9% |
| 2025 | 0.685 | 73.9% |
| 2026 | 0.560 | 63.8% |

Latest 90-day reading: intra 0.555, PC1 63.7%. Cohesion peaked in the 2021–22 hard reinsurance market (when cat-pricing news moved the names together) and has eroded since (holdout WEAKENED 0.77) as the cycle matured — but even at its tightest it was shared P&C-insurance beta, not a separable reinsurance factor. Insurance is an ETF-replicable complex: alongside the [[Insurance brokers basket]] and primary [[P&C insurance carriers basket]] cohorts, reinsurers resolve to [[KIE]], not a distinct factor.

## Related

- [[P&C insurance carriers basket]], [[Insurance brokers basket]], [[Life insurers pair]], [[Title Insurance]] — the other insurance cohorts (all ETF-replicable)
- [[RenaissanceRe]], [[Everest Group]], [[Arch Capital]], [[Axis Capital]] — the Bermuda reinsurance/specialty core
- [[Markel]], [[RLI]] — the looser specialty names
- [[Travelers]], [[Chubb]] — the primary carriers the cohort isn't distinct from
- [[KIE]] — the insurance ETF the complex resolves to
- [[Vault cluster taxonomy]] — cross-cohort meta-analysis
- [[Cohort, cluster, basket]] — terminology

---

*Created 2026-06-20. 1Y daily log returns through 2026-06-18; config `scripts/cluster_configs/rnr.yaml`; registry row 2026-06-20. Cluster validation is structure, not a performance ranking — see `docs/cluster-validation.md`.*
