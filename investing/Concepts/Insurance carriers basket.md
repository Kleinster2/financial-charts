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
