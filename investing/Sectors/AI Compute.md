---
aliases: [AI/Compute, AI Compute cluster]
---
#sector #semiconductor #ai #fabless

# AI Compute

TSMC + its largest AI/compute customers. Trades as a tight cluster (0.60 avg correlation) because TSMC's fate is tied to AI chip demand.

![[ai-compute-sector-chart.png]]
*TSM-NVDA track closely (0.69 correlation). AMD lagged but recovering — different competitive position despite same foundry.*

---

## Key actors

| Company | Role | Position |
|---------|------|----------|
| [[TSMC]] | Foundry | Manufactures for NVDA, AMD |
| [[NVIDIA]] | AI GPUs | \#1 TSMC customer, AI leader |
| [[AMD]] | CPUs + GPUs | \#2 TSMC customer, NVDA challenger |

---

## Correlation structure

| Metric | Value | Interpretation |
|--------|-------|----------------|
| Avg correlation | 0.61 | Strong (tight cluster) |
| Range | 0.56 - 0.69 | AMD-TSM to NVDA-TSM |
| vs Connectivity cluster | ~0.35 | Moderate separation |
| Period | 2024-01 to present | |

### Matched-methodology re-run (May 2026)

Run via `scripts/cluster_configs/ai_compute.yaml` with parameters matched to other vault cohorts (1Y window through 2026-05-07, threshold 0.5). Diagnostic values:

| Metric | Value (1Y matched) |
|---|---|
| Avg intra-cluster correlation | 0.600 |
| Pairwise range | 0.544-0.663 |
| PC1 explained variance | 73.37% |
| Verdict | Validated |

Despite [[AI Compute]] being the canonical AI trade, the cohort has lower intra-correlation than [[Space pure-plays]] (0.624) or [[Crypto-to-AI]] (0.691) at N=7. The TSMC-NVIDIA-AMD foundry-customer trio is tight on PC1 (73.37%) but small in cohort size — only 3 names. See [[Vault cluster taxonomy]] for cross-cohort context.

### Stability across windows

| Window | Obs | Intra-corr | PC1 | Vs SPY | Gap |
|---|---|---|---|---|---|
| YTD 2026 | 88 | 0.573 | 78.3% | 0.712 | -0.140 |
| 1Y | 136 | 0.571 | 77.5% | 0.667 | -0.096 |
| 2Y | 192 | 0.632 | 76.7% | 0.777 | -0.146 |
| 3Y | 296 | 0.636 | 77.2% | 0.752 | -0.117 |

Cohort has loosened from 0.636 (3Y) to 0.571 (1Y) — modest decoupling, possibly driven by AMD's idiosyncratic outperformance in the past year ([[#Per-name 1Y cumulative return|+191%]] vs TSM/NVDA at 33-60%). Gap to SPY is consistently negative (-0.10 to -0.15) — the cohort correlates MORE with SPY than with each other. This is structurally similar to the [[Mag 7 cluster|Mag 7]] failure pattern but at a smaller magnitude. AI Compute is a valid cluster but it's not strongly distinct from broad-market beta.

### PC2 / PC3 sub-structure

PC2 captures 15.7% of variance — material sub-structure for an N=3 cohort:

| Ticker | PC2 loading | Read |
|---|---|---|
| TSM | +0.66 | Foundry — manufacturing supplier |
| NVDA | +0.58 | AI dominant — locks TSMC capacity |
| AMD | -0.48 | Customer challenger — different competitive position |

PC2 cleanly separates AMD from TSM+NVDA. AMD is the cohort outlier — same end-market exposure (AI chips manufactured at TSM) but different competitive positioning (challenger to NVDA, smaller TSMC customer share). PC2 captures the "TSMC anchor pair" (TSM+NVDA) vs "TSMC challenger" (AMD) divide.

PC3 captures 6.7% of variance:

| Ticker | PC3 loading |
|---|---|
| NVDA | +0.75 |
| AMD | +0.00 |
| TSM | -0.66 |

PC3 separates NVDA from TSM. Both are tightly linked (TSM manufactures NVDA's chips) but trade on different cycles — NVDA on AI accelerator demand cycle, TSM on foundry capacity cycle.

### Factor decomposition

Regressing equal-weighted basket against semis + broad-market benchmarks:

| Benchmarks | R² | Residual factor |
|---|---|---|
| SOXX only | 66.3% | 33.7% |
| SOXX + SMH | 77.1% | 22.9% |
| SOXX + SMH + SPY + QQQ | 77.6% | 22.4% |

22% residual factor after stripping out the major benchmarks — same band as [[WFE]] (22%) but materially less than [[Space pure-plays]] (59.6%) or [[Defense primes basket|Defense primes]] (36%). AI Compute is heavily explained by SMH (beta +2.02 with SOXX in the mix) — the cohort is essentially leveraged semis-ETF exposure.

### Subset optimization (1Y)

All 3 pairs (only 3 possible at N=3):

| Pair | Intra-corr | Tracking corr | Sharpe | Cum % |
|---|---|---|---|---|
| TSM + AMD | 0.557 | 0.974 | 3.18 | +115.8% |
| NVDA + AMD | 0.524 | 0.971 | 2.91 | +96.9% |
| TSM + NVDA | 0.632 | 0.892 | 2.23 | +45.9% |

AMD pairs (TSM+AMD and NVDA+AMD) dominate by Sharpe — AMD's idiosyncratic +191% return diversified meaningfully with the other two names. The TSM+NVDA pair (the tightest by intra-corr) has the LOWEST cum return + Sharpe — confirming the cohort's factor-tracking ≠ return-maximizing pattern at N=3.

### Per-name 1Y cumulative return

| Ticker | 1Y return |
|---|---|
| [[AMD]] | +191.4% |
| [[TSMC\|TSM]] | +59.9% |
| [[NVIDIA\|NVDA]] | +33.1% |

AMD is the cohort's standout performer — +191% vs the other two at +33-60%. AMD's PC1 loading of 0.875 (highest in cohort) AND highest cumulative return is structurally different from the Swiss-Army-knife pattern in larger cohorts ([[Space pure-plays]] PL has lowest PC1 loading + 2nd-highest return). At N=3 the Swiss-Army-knife dynamic doesn't emerge — the cohort is too small for the diversification-via-low-PC1-loading benefit to appear.

Pairwise detail:
| Pair | Correlation |
|------|-------------|
| TSM - NVDA | 0.69 |
| TSM - AMD | 0.56 |
| NVDA - AMD | 0.57 |

TSMC's stock moves with its AI customers, not "foundry peers."

---

## Kalshi compute-rental pricing layer (May 20, 2026)

[[Kalshi]]'s end-of-May GPU hourly-price ladders are a noisy but useful sentiment layer for [[AI Compute]]. They are prediction-market contracts on whether rental prices clear specific thresholds, not observed cloud prices. The liquid signal is strongest in [[H100]] and weaker in [[H200]] / [[RTX 5090]]; [[A100]], [[B200]], and [[Nvidia RTX PRO 6000|RTX PRO 6000]] ladders had little or no usable open interest in this pull.

| Contract family | Cleanest ladder points | Read |
|---|---|---|
| [[H100]] SXM hourly compute | Monthly >$2.17/hr at 86c / 96c bid-ask and 96c last, with 2,278.03 aggregate active volume and 1,625.77 open interest; weekly $3.14 price-up strike at 85c / 87c but tiny volume. | Market is pricing [[H100]] rental above $2/hour as the base case. |
| [[H200]] hourly compute | Monthly >$2.74/hr at 70c / 100c bid-ask and 70c last; weekly $4.96 price-up strike at 12c / 27c with 199 volume. | Directionally tight month-end supply, but weekly momentum does not confirm a near-term jump. |
| [[RTX 5090]] hourly compute | Monthly >$0.67/hr at 50c / 79c bid-ask and 53c last; weekly $0.59 price-up strike at 88c / 99c with 150.19 volume and 142.11 open interest. | Consumer/prosumer compute remains bid; this is the cleanest non-data-center signal. |
| [[A100]] / [[B200]] / [[Nvidia RTX PRO 6000|RTX PRO 6000]] | [[A100]] and [[B200]] ladders showed little or no usable liquidity; [[Nvidia RTX PRO 6000|RTX PRO 6000]] returned no active API markets. | Do not use these for a durable pricing read yet. |

The useful read is scarcity, not valuation precision. Traders are not pricing a collapse in high-end [[NVIDIA]] compute rental rates even after the Blackwell transition. That supports the broader sector view that [[AI hyperscalers]] are still competing for constrained accelerator supply rather than entering a clean post-shortage phase. The biggest hole is [[B200]]: the prediction-market order book is not yet liquid enough to test whether [[Blackwell]] rental economics are clearing smoothly.

*Sources: [[Kalshi]] API series KXH100MON, KXH100W, KXH200MON, KXH200W, KXRTX5090MON, KXRTX5090W, KXA100MON, KXA100W, KXB200MON, KXB200W, KXRTXPRO6000MON, and KXRTXPRO6000W, read May 20, 2026.*

---

## Why this cluster exists

TSMC's revenue concentration:
- NVDA is TSMC's largest customer (~25% of revenue)
- AMD is \#2-3 customer
- AI/HPC is TSMC's highest-margin segment

Shared demand driver:
- All three benefit from AI infrastructure buildout
- [[AI hyperscalers]] capex flows to NVDA GPUs → manufactured by TSMC
- AMD taking share in AI → also manufactured by TSMC

The insight: "Foundry" isn't a sector. TSMC is effectively a levered bet on NVDA + AMD demand.

---

## vs other semi clusters

| Cluster | Correlation | Relationship |
|---------|-------------|--------------|
| [[WFE]] | ~0.55 | Equipment sells to TSMC |
| [[Connectivity]] | ~0.35 | Different end markets |
| [[US Memory]] | ~0.40 | Different supply chain |
| [[Korea Memory]] | ~0.25 | Geographic separation |

---

## Related

### Parent
- [[Semiconductors]] — parent sector

### Sister clusters
- [[Connectivity]] — AVGO, QCOM, MRVL cluster
- [[WFE]] — equipment suppliers

### Actors
- [[TSMC]] — foundry monopoly
- [[NVIDIA]] — AI GPU leader
- [[AMD]] — x86 + GPU challenger

### Context
- [[AI hyperscalers]] — demand driver
- [[Leading edge race]] — TSMC moat
- [[Kalshi]] — prediction-market layer for compute-price and AI-market expectations

*Created 2026-01-30*
