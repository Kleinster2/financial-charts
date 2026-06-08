---
aliases: [Insurance carriers, US insurance carriers]
tags: [concept/cluster, insurance, financials]
---

# Insurance carriers basket

> [!warning] Cluster status: partial validation, splits into 2 sub-clusters (May 2026)
> Intra-cluster correlation 0.45 (range -0.09 to 0.81), PC1 53.4%. The 8-name combined cohort fails as a single cluster due to bimodal sub-structure: P&C carriers (PGR, CB, TRV, ALL, HIG) form a tight 5-name cluster (intra 0.64, PC1 71.6%) — see [[P&C insurance carriers basket]] for the validated sub-cluster. Life insurers (MET, PRU) form a separate 2-name pair (correlation 0.69). AIG is a singleton (specialty + complex restructuring history). Cluster correlation between P&C and Life: only 0.26 — different factors despite the shared "insurance carrier" label. See "Cluster validation" section below.

The 8-name US insurance carrier cohort splits cleanly into P&C carriers (5-name validated tight cluster) + life insurers (2-name pair) + AIG (singleton). The "insurance carriers" framing groups them by license type but the equity returns reflect different underlying drivers (cat losses + commercial pricing for P&C; long-duration interest-rate exposure + mortality assumptions for life).

---

## Constituents

8 candidates split into 3 sub-cohorts.

| Sub-cohort | Members | Correlation | Note |
|---|---|---|---|
| P&C carriers | [[Progressive]] (PGR), [[Chubb]] (CB), [[Travelers]] (TRV), [[Allstate]] (ALL), [[Hartford Financial]] (HIG) | Intra 0.64 — VALIDATED → see [[P&C insurance carriers basket]] | Cat losses + commercial pricing factor |
| Life insurers | [[MetLife]] (MET), [[Prudential Financial]] (PRU) | 0.69 (single pair) — VALIDATED → see [[Life insurers pair]] | Long-duration rate exposure + mortality (BUT: equity returns are uncorrelated with long bonds at daily horizon) |
| Specialty / restructured | [[AIG]] | Singleton | Diversified specialty + complex post-2008 restructuring |

The P&C and Life sub-cohorts trade as completely separate factors (0.26 cross-cluster correlation). AIG sits alone — too idiosyncratic for either group.

---

## Cluster validation

Procedure: `scripts/cluster_analysis.py --config scripts/cluster_configs/ins_carriers.yaml`. Standard in `docs/cluster-validation.md`.

### Headline numbers (1Y, 2025-04-30 to 2026-04-30)

| Diagnostic | Result | Interpretation |
|---|---|---|
| Avg intra-cluster correlation (8-name) | 0.45 (range -0.09 to 0.81) | Wildly bimodal — wide range is the falsification signal |
| 5-name P&C tight core intra | 0.64 | Validated as own cluster |
| 2-name life pair (MET-PRU) | 0.69 | Validated as own pair |
| AIG vs everything else | -0.09 to 0.53 | Singleton |
| PC1 explained variance (8-name) | 53.4% | Just above multi-factor floor; PC1 is essentially the P&C factor |
| Hierarchical clustering at 0.4 | P&C cluster (5 names) + Life pair (MET, PRU) + AIG singleton | Three groups |
| Cluster vs insurance brokers | 0.37 (+0.09) | Carriers and brokers are partly correlated (same end market) |
| Cluster vs banks | 0.25 (+0.20) | Distinct from banks |
| Cluster vs broad ETFs | 0.28 (+0.17) | Insurance has lower equity-market beta than financials in general |

### What the math reveals

- **P&C carriers cluster cleanly** (intra 0.64, see [[P&C insurance carriers basket]]). Same business model: underwriting cycle + cat losses + commercial pricing. Distinct from broad market (low beta).
- Life insurers (MET, PRU) cluster as a pair (0.69). Long-duration interest-rate exposure dominates; trades on rate curve.
- AIG is a singleton. Specialty mix + complex post-2008 restructuring history + variable-annuity legacy = unique idiosyncratic factor.
- Cross-sub-cohort correlations are weak: P&C vs Life ~0.26; AIG vs P&C ~0.30-0.50; AIG vs Life ~0.40-0.50. The "insurance carrier" label does not translate to a shared trading factor.

---

## Trade implications

| Trade | Expression | Factor isolated |
|---|---|---|
| Long P&C insurance | See [[P&C insurance carriers basket]] | P&C underwriting cycle |
| Long life insurance | MET + PRU pair | Long-duration rate exposure |
| AVOID: long insurance carriers basket (8 names) | Dilutes 3 unrelated factors | No clean exposure |
| Pair: P&C vs Life | PC1 of P&C / PC1 of Life | Underwriting vs rate-curve factor differential |
| Pair: P&C vs insurance brokers | See [[P&C insurance carriers basket]] vs [[Insurance brokers basket]] | Manufacturing vs distribution economics |

---

## Cluster validation compliance addendum (2026-06-07)

Generated from `scripts/cluster_configs/ins_carriers.yaml` using `scripts/cluster_analysis.py` methodology. The 1Y diagnostic window is 2025-05-01 to 2026-04-30 (171 observations); the rolling history starts at `2020-01-01` where data are available.

### Required validation plots

![[ins-carriers-cluster-correlation-1y.png]]

*One-year correlation heatmap for the `Insurance carriers` validation universe.*

![[ins-carriers-cluster-dendrogram-1y.png]]

*Hierarchical clustering tree using average linkage on distance `1-|corr|`.*

![[ins-carriers-cluster-pca-1y.png]]

*PCA diagnostic for the candidate cohort; PC1 explains 53.4% of standardized daily-return variance.*

### PC1 index weights vs cluster topology

The topology table answers which names join the tree first or last. The raw PC1-mimic table answers which raw-return weights best replicate the standardized common factor after realized-volatility scaling. These are deliberately different readings of the same cluster.

| Step | Left | Right | Distance (1-\|corr\|) | Read |
|---|---|---|---|---|
| 1 | TRV | HIG | 0.187 | Tightest merge |
| 2 | MET | PRU | 0.313 | Candidate cohort merge step |
| 3 | PGR | ALL | 0.314 | Candidate cohort merge step |
| 4 | CB | TRV+HIG | 0.335 | Candidate cohort merge step |
| 5 | PGR+ALL | CB+TRV+HIG | 0.400 | Candidate cohort merge step |
| 6 | AIG | MET+PRU | 0.570 | Candidate cohort merge step |
| 7 | PGR+ALL+CB+TRV+HIG | AIG+MET+PRU | 0.690 | Final cohort join / loosest boundary |

| Ticker | PC1 loading | Normalized loading weight | Ann. vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| PGR | 0.339 | 12.21% | 25.01% | 10.27% |
| CB | 0.384 | 13.81% | 18.21% | 15.96% |
| TRV | 0.414 | 14.89% | 18.57% | 16.87% |
| ALL | 0.388 | 13.97% | 21.93% | 13.40% |
| MET | 0.283 | 10.18% | 23.82% | 9.00% |
| PRU | 0.218 | 7.86% | 23.29% | 7.10% |
| AIG | 0.323 | 11.65% | 24.30% | 10.08% |
| HIG | 0.429 | 15.44% | 18.75% | 17.32% |

Interpretation: use the dendrogram / join-distance topology to identify the tight core and later-joining members; use the Raw PC1-mimic weight column only for investable factor-replication sizing.

### Historical tightness evolution

![[ins-carriers-cluster-rolling-tightness-90d.png]]

*Ninety-day rolling tightness diagnostic: avg intra-correlation, PC1 share, core correlation, satellite-to-core correlation, and final candidate join distance.*

| Year | Avg corr median | PC1 median | Core corr median | Satellite-to-core median | Final join distance median |
|---|---|---|---|---|---|
| 2020 | 0.760 | 79.6% | 0.822 | 0.565 | 0.435 |
| 2021 | 0.493 | 59.0% | 0.592 | 0.324 | 0.765 |
| 2022 | 0.662 | 70.9% | 0.688 | 0.560 | 0.464 |
| 2023 | 0.593 | 65.5% | 0.655 | 0.396 | 0.606 |
| 2024 | 0.497 | 56.7% | 0.531 | 0.381 | 0.620 |
| 2025 | 0.675 | 71.9% | 0.699 | 0.607 | 0.429 |
| 2026 | 0.415 | 51.0% | 0.427 | 0.392 | 0.765 |

Latest 90D through 2026-04-30: avg corr 0.402, PC1 50.4%, core corr 0.411, satellite-to-core corr 0.374, final join distance 0.811.

Historical verdict: regime-dependent / fragmenting cluster; current rolling cohesion is below durable-cluster thresholds.

---

## Related

### Sub-clusters

- [[P&C insurance carriers basket]] — VALIDATED 5-name sub-cluster (PGR, CB, TRV, ALL, HIG)

### Member actors

- [[Progressive]] — P&C
- [[Chubb]] — P&C
- [[Travelers]] — P&C
- [[Allstate]] — P&C
- [[Hartford Financial]] — P&C
- [[MetLife]] — life
- [[Prudential Financial]] — life
- [[AIG]] — specialty / restructured

### Adjacent concept notes

- [[Insurance brokers basket]] — distribution-side cluster (carriers manufacture, brokers distribute)
- [[Insurance float]] — Buffett-era investment frame
- [[Reinsurance sidecars]] — adjacent reinsurance structure
- [[Insurance]] — sector hub

### Methodology

- `docs/cluster-validation.md` — standard procedure
- `scripts/cluster_analysis.py` — generalized cluster validation script
- `scripts/cluster_configs/ins_carriers.yaml` — config for this test
- `scripts/cluster_configs/pc_carriers.yaml` — config for the validated P&C sub-cluster

*Created 2026-05-03 — partial-validation parent note (P&C sub-cluster validated separately)*
