---
aliases: [Life insurers, MET-PRU pair, Life insurance basket]
tags: [basket/internal, insurance, life-insurance]
---

# Life insurers pair

> [!success] Cluster status: validated, with surprising rate-correlation finding (May 2026)
> Pairwise correlation 0.69. PC1 explains 84.4% of variance. The 2-name pair clusters cleanly (separate from P&C carriers, banks, brokers, and long-duration bond proxies). Most surprising finding: cluster correlation with long-duration bonds (TLT/IEF) is **-0.002** — essentially zero. Life insurers do NOT trade as long-duration rate proxies on a daily-return basis, contrary to common framing. They actually trade more like banks (0.51) and broad market (0.60) than like bonds. The "rate-curve sensitivity" thesis needs refinement. See "Cluster validation" section below.

The two largest US public life insurance-and-retirement-services companies — MetLife and Prudential Financial — form a tight 2-name pair. Surfaced as the second sub-cluster when the 8-name [[Insurance carriers basket]] split into P&C carriers + life insurers + AIG singleton. The pair shares similar business mixes (group benefits + retirement / variable annuities + asset management) and trades on similar drivers.

The most analytically important finding from the validation: life insurers' equity returns do NOT correlate with long-duration bond returns at the 1Y daily horizon, despite the common framing of life insurers as "long-duration rate proxies." The actual factor is closer to bank/financial-services beta + idiosyncratic underwriting/spread dynamics.

---

## Constituents

2 names. The smallest possible cluster.

| Ticker | Company | PC1 loading | Business mix |
|--------|---------|-------------|--------------|
| MET | [[MetLife]] | 0.707 | Group benefits + retirement + asset management; international (Asia, LatAm); reduced VA exposure post-Brighthouse spin |
| PRU | [[Prudential Financial]] | 0.707 | International (Japan-heavy via Gibraltar Life) + retirement + asset management (PGIM) |

PC1 loadings are necessarily 0.707 each (= 1/√2) for any 2-name standardized cohort.

Internal ticker proposal: LIFEINS.

### Excluded — and why

| Excluded | Why excluded |
|----------|--------------|
| [[AIG]] | Specialty + complex restructured business; singleton in [[Insurance carriers basket]] test |
| [[Lincoln National]] (LNC), [[Globe Life]] (GL), [[Brighthouse Financial]] (BHF), [[Equitable Holdings]] (EQH), [[Voya Financial]] (VOYA) | Smaller scale + different business mixes; not tested in this validation but candidates for an expanded life-insurer cluster test |
| [[Allstate]] (ALL), [[Hartford Financial]] (HIG) | Mixed P&C + benefits; cluster with P&C carriers (see [[P&C insurance carriers basket]]) |
| TLT, IEF (long-duration bond proxies) | -0.002 correlation with the cluster — life insurers do NOT trade as bond proxies (see surprising finding below) |

---

## Cluster validation

Procedure: `scripts/cluster_analysis.py --config scripts/cluster_configs/life_insurers.yaml`. Standard in `docs/cluster-validation.md`.

### Headline numbers (1Y, 2025-04-30 to 2026-04-30)

| Diagnostic | Result | Interpretation |
|---|---|---|
| Pairwise correlation MET-PRU | 0.688 | Strong cohesion |
| PC1 explained variance | 84.4% | Single-factor pair; ~16% idiosyncratic spread |
| Hierarchical clustering at 0.4 | MET+PRU cluster cleanly, separate from P&C, banks, brokers, bond proxies | Boundary clean |
| Cluster vs P&C carriers | 0.255 (+0.433 advantage) | Underwriting cycle (P&C) distinct from spread/rate (life) |
| Cluster vs insurance brokers | 0.236 (+0.452 advantage) | Manufacturing vs distribution |
| Cluster vs banks | 0.510 (+0.177 advantage) | Smallest separation — life insurers DO trade with bank factor partially |
| Cluster vs broad ETFs | 0.600 (+0.088 advantage) | Substantial broad-market beta |
| Cluster vs long-duration bond proxies (TLT, IEF) | -0.002 (+0.690 advantage) | The surprise: life insurers are essentially uncorrelated with long bonds |

### The surprising finding — life insurers are not long-duration proxies

Common market framing positions life insurers as "long-duration rate proxies" — they hold large fixed-income portfolios backing policy reserves, so theoretically benefit from higher rates (better reinvestment) and suffer from lower rates (lower spread). On the equity-return level, the math says this is not true at a daily horizon:

- TLT (20+ year Treasury ETF) and IEF (7-10 year Treasury ETF) cluster tightly with each other (correlation 0.91) but have essentially zero correlation with MET-PRU (-0.002).
- Life insurers trade more with broad market (0.60) and banks (0.51) than with long bonds (-0.00).

What this means: the equity returns of life insurers reflect:
1. Broad financial-services beta (rate-curve via banks, credit cycle)
2. Idiosyncratic life-insurance underwriting (mortality assumptions, longevity risk, lapse rates)
3. Variable annuity / spread-product earnings (sensitive to equity beta + rate level + lapse)
4. Asset management fees (PGIM at PRU; MetLife Investment Management at MET) — equity-AUM-driven
5. International exposure (Japan rates for PRU; emerging markets for MET)

Long-duration bond exposure shows up in BOOK VALUE / accounting capital but does not drive day-to-day equity returns. The "rate proxy" framing is true for the asset side but the equity behaves more like a financial-services beta name.

This has trade implications: pair trades between life insurers and TLT (long-duration bonds) do NOT capture rate exposure — they're essentially uncorrelated, so the pair captures noise. Pair against broad market (SPY) or banks (XLF) is more meaningful.

---

## YTD 2026 cohort tracking

![[life-insurers-basket-2026ytd-price-chart.png]]

*MET (blue, primary) vs PRU normalized from 2025-12-31. The pair tracks closely through Q1 2026 sentiment swings. The 16% idiosyncratic spread is visible at peaks/troughs but the path is consistent.*

---

## Trade implications

| Trade | Expression | Factor isolated |
|---|---|---|
| Long life insurance | Equal-weighted MET + PRU | Life insurance underwriting + spread products + financial-services beta |
| Solo MET or solo PRU | Either name alone | ~84% of the same factor; pick on relative valuation |
| Pair: long life insurers / short P&C carriers | Captures spread/rate vs underwriting-cycle differential (+0.43 separation) | Two different insurance business models |
| Pair: long life insurers / short banks | Captures life-spread vs deposit-NIM differential (+0.18) | Smaller separation; partial rate-curve overlap |
| AVOID: long life insurers / short TLT | -0.002 correlation — pair captures noise, not rate exposure | Common framing breaks |
| AVOID: long life insurers / short broad market | +0.09 marginal advantage; near-zero clean factor | Limited usefulness |

The cleanest opportunity is the +0.43 separation from P&C carriers — when the insurance complex re-rates on a sector-wide event, the underwriting-cycle (P&C) and spread/rate (life) responses diverge meaningfully.

---

## What could break the pair (or sharpen it)

| Scenario | Effect on cluster |
|---|---|
| Major rate-curve move (steep cuts or hikes) | Pair persists; cohesion likely increases as both reprice on rate path |
| Equity drawdown | Both names re-rate together (variable annuity + AUM exposure) |
| Major mortality / longevity event | Life-specific factor; pair persists, broader insurance complex decouples |
| MET or PRU acquired or restructured | Affected name decouples around event-noise periods |
| Japan rate normalization (Bank of Japan hike) | PRU decouples — Japan-heavy via Gibraltar Life; rate-cycle exposure is asymmetric |
| Variable annuity reform / lapse experience break | Affected name decouples around earnings event |

---

## Tracking

- Re-run validation quarterly: `python scripts/cluster_analysis.py --config scripts/cluster_configs/life_insurers.yaml`.
- Watch PRU-Japan exposure — BoJ rate moves are the biggest within-pair asymmetry.
- Watch correlation with TLT — if the relationship turns positive, the rate-proxy framing returns.
- Cross-check vs [[Insurance carriers basket]] — confirms life remains distinct from P&C.
- Consider expanding to a 5-6 name life-insurer basket (add LNC, EQH, VOYA, BHF) when data ingested — would strengthen factor isolation.

---

## Cluster validation compliance addendum (2026-06-07)

Generated from `scripts/cluster_configs/life_insurers.yaml` using `scripts/cluster_analysis.py` methodology. The 1Y diagnostic window is 2025-05-01 to 2026-04-30 (171 observations); the rolling history starts at `2020-01-01` where data are available.

### Required validation plots

![[life-insurers-cluster-correlation-1y.png]]

*One-year correlation heatmap for the `Life insurers pair` validation universe.*

![[life-insurers-cluster-dendrogram-1y.png]]

*Hierarchical clustering tree using average linkage on distance `1-|corr|`.*

![[life-insurers-cluster-pca-1y.png]]

*PCA diagnostic for the candidate cohort; PC1 explains 84.3% of standardized daily-return variance.*

### PC1 index weights vs cluster topology

The topology table answers which names join the tree first or last. The raw PC1-mimic table answers which raw-return weights best replicate the standardized common factor after realized-volatility scaling. These are deliberately different readings of the same cluster.

| Step | Left | Right | Distance (1-\|corr\|) | Read |
|---|---|---|---|---|
| 1 | MET | PRU | 0.313 | Final cohort join / loosest boundary |

| Ticker | PC1 loading | Normalized loading weight | Ann. vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| MET | 0.707 | 50.00% | 23.82% | 49.44% |
| PRU | 0.707 | 50.00% | 23.29% | 50.56% |

Interpretation: use the dendrogram / join-distance topology to identify the tight core and later-joining members; use the Raw PC1-mimic weight column only for investable factor-replication sizing.

### Historical tightness evolution

![[life-insurers-cluster-rolling-tightness-90d.png]]

*Ninety-day rolling tightness diagnostic: avg intra-correlation, PC1 share, core correlation, satellite-to-core correlation, and final candidate join distance.*

| Year | Avg corr median | PC1 median | Core corr median | Satellite-to-core median | Final join distance median |
|---|---|---|---|---|---|
| 2020 | 0.966 | 98.3% | 0.966 | n/a | 0.034 |
| 2021 | 0.875 | 93.7% | 0.875 | n/a | 0.125 |
| 2022 | 0.921 | 96.0% | 0.921 | n/a | 0.079 |
| 2023 | 0.874 | 93.7% | 0.874 | n/a | 0.126 |
| 2024 | 0.849 | 92.5% | 0.849 | n/a | 0.151 |
| 2025 | 0.897 | 94.9% | 0.897 | n/a | 0.103 |
| 2026 | 0.709 | 85.4% | 0.709 | n/a | 0.291 |

Latest 90D through 2026-04-30: avg corr 0.635, PC1 81.8%, core corr 0.635, satellite-to-core corr n/a, final join distance 0.365.

Historical verdict: structurally durable cluster; rolling cohesion has usually stayed in single-factor territory.

---

## Related

### Member actors

- [[MetLife]] — group benefits + retirement; reduced VA exposure post-Brighthouse spin
- [[Prudential Financial]] — Japan-heavy via Gibraltar Life; PGIM asset management

### Adjacent concept notes

- [[Insurance carriers basket]] — parent (8-name basket that splits into life pair + P&C cluster + AIG singleton)
- [[P&C insurance carriers basket]] — sibling cluster (different business model: underwriting cycle vs spread/rate)
- [[Insurance brokers basket]] — adjacent (distribution side)
- [[Insurance float]] — Buffett-era frame; relevant to asset side
- [[Reinsurance sidecars]] — adjacent reinsurance structure
- [[Insurance]] — sector hub

### Methodology

- `docs/cluster-validation.md` — standard procedure
- `scripts/cluster_analysis.py` — generalized cluster validation script
- `scripts/cluster_configs/life_insurers.yaml` — config for this cluster

*Created 2026-05-03 — fourteenth concept note created under the new cluster-validation standard; documents the surprising finding that life insurers are NOT long-duration bond proxies on a daily-return basis*
