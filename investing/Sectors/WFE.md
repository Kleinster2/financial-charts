---
aliases: [Wafer Fab Equipment, Semiconductor Equipment, Semi Equipment]
---
#sector #semiconductor #equipment

# WFE

Wafer fab equipment — the picks and shovels of semiconductors. Tightest sector correlation (0.70) due to shared customers and capex cycles.

![[wfe-sector-chart.png]]
*LRCX outperforming, but all four move together. AMAT-LRCX especially tight (0.90 correlation).*

---

## Key actors

| Company | Focus | Position |
|---------|-------|----------|
| [[ASML]] | Lithography (EUV monopoly) | Irreplaceable, highest margins |
| [[Applied Materials]] | Deposition, etch, CMP | Broadest portfolio |
| [[Lam Research]] | Etch, deposition | Memory + logic |
| [[KLA]] | Inspection, metrology | Quality control |

---

## Correlation structure

| Metric | Value | Interpretation |
|--------|-------|----------------|
| Avg correlation | 0.70 | Strong (tightest semi cluster) |
| Range | 0.54 - 0.90 | KLA pairs to AMAT-LRCX |
| Period | 2024-01 to present | |

### Matched-methodology re-run (May 2026)

Run via `scripts/cluster_configs/wfe_quartet.yaml` with parameters matched to other vault cohorts (1Y window through 2026-05-07, threshold 0.5). Diagnostic values:

| Metric | Value (1Y matched) |
|---|---|
| Avg intra-cluster correlation | 0.804 |
| Pairwise range | 0.740-0.857 |
| PC1 explained variance | 85.33% |
| Verdict | Validated (tightest cohort in vault — oligopoly limit) |

WFE represents the structural ceiling for vault cluster validation — 4 oligopolists serving the same 3-4 leading-edge foundry customers on the same capex cycle. The constraint structure isn't replicable for thematic-basket cohorts, which is why no other vault cluster reaches 0.80+ intra-correlation. See [[Vault cluster taxonomy]] for cross-cohort context.

### Stability across windows

| Window | Obs | Intra-corr | PC1 | Vs SPY | Gap |
|---|---|---|---|---|---|
| YTD 2026 | 88 | 0.831 | 87.7% | 0.685 | +0.145 |
| 1Y | 136 | 0.786 | 85.0% | 0.643 | +0.143 |
| 2Y | 192 | 0.842 | 88.6% | 0.674 | +0.169 |
| 3Y | 296 | 0.842 | 88.6% | 0.678 | +0.164 |

Remarkably stable across the full 3Y history — intra-corr 0.79-0.84 throughout. Cluster identity is structurally durable (same customers, same capex cycle). Most stable cohort in the vault alongside [[Crypto-to-AI]].

### PC2 sub-structure — ASML as the cohort's outlier

PC2 captures 6.5% of variance:

| Ticker | PC2 loading | Read |
|---|---|---|
| [[ASML]] | +0.77 | Lithography (EUV monopoly) — different process step |
| [[Lam Research\|LRCX]] | +0.15 | Etch + deposition |
| [[Applied Materials\|AMAT]] | -0.17 | Deposition + etch |
| [[KLA\|KLAC]] | -0.60 | Inspection + metrology — different process step |

PC2 separates ASML (lithography) and KLAC (inspection) from AMAT and LRCX (deposition/etch). Single-outlier-on-each-end structure capturing the process-step diversification within WFE. ASML's EUV monopoly and KLAC's inspection/metrology niche are the two structurally distinct businesses.

### PC3 — KLAC vs LRCX+AMAT

PC3 captures 5.0% of variance:

| Ticker | PC3 loading |
|---|---|
| KLAC | +0.62 |
| ASML | +0.46 |
| AMAT | -0.48 |
| LRCX | -0.43 |

PC3 isolates KLAC + ASML (metrology + lithography) from LRCX + AMAT (etch + deposition).

### Factor decomposition

Regressing equal-weighted WFE basket against semis benchmarks:

| Benchmarks | R² | Residual factor |
|---|---|---|
| SOXX only | 75.9% | 24.1% |
| SOXX + SMH | 77.9% | 22.1% |
| SOXX + SMH + SPY | 78.2% | 21.8% |

22% residual factor after stripping out broad semis ETFs. WFE has its own factor beyond what SOXX captures, but at a much smaller share than [[Space pure-plays]] (59.6%) or [[Defense primes basket|Defense primes]] (36%). The WFE basket is closely tied to semis benchmarks because WFE IS a major weight in SOXX/SMH.

### Subset optimization (1Y)

All 6 pairs cluster tightly with track ≥0.965, intra-corr ≥0.70, and Sharpe ≥1.8:

| Pair | Intra-corr | Tracking corr | Sharpe | Cum % |
|---|---|---|---|---|
| ASML + LRCX | 0.780 | 0.966 | 2.30 | +77.1% |
| AMAT + LRCX | 0.869 | 0.975 | 2.12 | +79.4% |
| ASML + AMAT | 0.735 | 0.971 | 2.11 | +64.6% |
| KLAC + LRCX | 0.811 | 0.978 | 2.03 | +73.3% |
| ASML + KLAC | 0.703 | 0.965 | 1.99 | +59.0% |
| AMAT + KLAC | 0.819 | 0.970 | 1.81 | +61.1% |

Any 2-name subset works for WFE — pairs are uniformly tight and high-Sharpe. The cohort doesn't have the "factor-tracking ≠ Sharpe-optimal" tension observed in other cohorts; WFE is structurally too tight for the patterns to emerge.

### Per-name 1Y cumulative return

| Ticker | 1Y return |
|---|---|
| [[Lam Research\|LRCX]] | +93.0% |
| [[Applied Materials\|AMAT]] | +66.8% |
| [[ASML]] | +62.4% |
| [[KLA\|KLAC]] | +55.5% |

Tight range (+55% to +93%) — all four oligopolists captured the AI-capex tailwind without single-name divergence. Different signature from [[Space pure-plays]] (large dispersion) and [[Crypto-to-AI]] (large dispersion).

Pairwise detail:
| Pair | Correlation |
|------|-------------|
| AMAT - LRCX | 0.90 | Near-identical exposure |
| ASML - AMAT | 0.82 | |
| ASML - LRCX | 0.81 | |
| AMAT - KLAC | 0.54 | KLA slightly different |
| ASML - KLAC | 0.55 | |
| LRCX - KLAC | 0.55 | |

Note: AMAT-LRCX at 0.90 is one of the highest correlations in semis. KLA is slightly differentiated (inspection vs deposition/etch).

---

## Why this cluster is tight

1. Same customers — TSMC, Samsung, Intel, Micron all buy from same vendors
2. Same capex cycle — Equipment orders track fab buildout plans
3. Oligopoly structure — Limited competition, coordinated pricing
4. Long lead times — 12-18 month backlogs create visibility

---

## Sector economics

| Metric | Value |
|--------|-------|
| Gross margins | 45-55% |
| Book-to-bill | >1.1x = bullish signal |
| Capex intensity | Low (design, not fabs) |
| Cyclicality | Medium (backlog smooths) |

---

## Investment thesis

[[Long WFE]] — Leveraged bet on semiconductor capex without picking chip winners.

| Bull | Bear |
|------|------|
| AI driving capex boom | Cyclical peak risk |
| EUV upgrade cycle | China restrictions limit TAM |
| Oligopoly pricing | Customer concentration |
| Backlog visibility | Long-cycle inventory risk |

---

## Related

### Parent
- [[Semiconductors]] — parent sector

### Sister clusters
- [[AI Compute]] — customers (TSMC)
- [[Memory]] — customers (Samsung, SK Hynix, Micron)

### Actors
- [[ASML]] — EUV monopoly
- [[Applied Materials]] — broadest portfolio
- [[Lam Research]] — etch leader
- [[KLA]] — inspection/metrology

### Theses
- [[Long WFE]] — equipment leverage thesis

### Context
- [[Export controls]] — China restrictions on EUV
- [[CHIPS Act]] — US fab buildout = equipment demand

*Created 2026-01-30*
