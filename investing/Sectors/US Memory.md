---
aliases: [American memory]
---
#sector #memory #semiconductor #usa

# US Memory

US-based memory companies. Trades as a distinct cluster (0.50 correlation) separate from Korea Memory.

![[us-memory-sector-chart.png]]
*SNDK massively outperforming since Feb 2025 spinoff (+1700%). MU and WDC more correlated with each other than with SNDK.*

---

## Key actors

| Company | Focus | Position |
|---------|-------|----------|
| [[Micron]] | DRAM + NAND + HBM | \#3 DRAM, \#4 NAND, \#3 HBM |
| [[SanDisk]] | NAND (pure-play) | \#5 NAND, spun from WDC Feb 2025 |
| [[Western Digital]] | HDD (post-spinoff) | Former memory, now storage |

---

## Correlation structure

| Metric | Value | Interpretation |
|--------|-------|----------------|
| Avg correlation | 0.50 | Moderate (valid sector) |
| Range | 0.39 - 0.70 | WDC-SNDK to MU-WDC |
| vs [[Korea Memory]] | 0.09-0.21 | Weak (separate cluster) |
| Period | 2024-01 to present | |

### Matched-methodology re-run (May 2026)

Run via `scripts/cluster_configs/us_memory.yaml` with parameters matched to other vault cohorts (1Y window through 2026-05-07, threshold 0.5). The 1Y matched-methodology numbers are materially tighter than the prior 2024-2026 reading:

| Metric | Value (1Y matched) |
|---|---|
| Avg intra-cluster correlation | 0.696 |
| Pairwise range | 0.655-0.754 |
| PC1 explained variance | 79.72% |
| Verdict | Validated |

The cohort has tightened from the original published 0.50 to 0.696 over the past year — driven by the memory shortage cycle pulling all three names (MU, SNDK, WDC) onto the same demand-driven factor. Even MU-SNDK (0.42 historical) is now well above 0.50. See [[Vault cluster taxonomy]] for cross-cohort context.

### Stability across windows

| Window | Obs | Intra-corr | PC1 | Vs SPY | Gap |
|---|---|---|---|---|---|
| YTD 2026 | 83 | 0.722 | 82.5% | 0.489 | +0.233 |
| 1Y | 131 | 0.697 | 81.5% | 0.485 | +0.213 |
| 2Y | 151 | 0.743 | 84.1% | 0.621 | +0.122 |
| 3Y | 151 | 0.743 | 84.1% | 0.621 | +0.122 |

Slightly loosened from 0.743 (3Y) to 0.697 (1Y) but then re-tightened to 0.722 (YTD). The cluster is essentially stable in the 0.70 band. Gap to SPY widened significantly recently (0.122 at 3Y → 0.213 at 1Y → 0.233 YTD) — the cohort has been decoupling from broad-market beta over the past year as the memory shortage cycle drives differentiated returns.

### PC2 / PC3 sub-structure

PC2 captures 11.8% of variance:

| Ticker | PC2 loading | Read |
|---|---|---|
| [[Western Digital\|WDC]] | +0.81 | Post-spinoff HDD-focused entity |
| [[Micron\|MU]] | +0.12 | Diversified DRAM + NAND + HBM |
| [[SanDisk\|SNDK]] | -0.58 | NAND pure-play (Feb 2025 spinoff from WDC) |

PC2 separates WDC and SNDK on opposite sides despite their shared origin — the Feb 2025 spinoff effectively split a single company into two structurally distinct businesses that now trade on opposite PC2 sleeves. MU sits in the middle as the integrated player.

PC3 captures 6.7% of variance:

| Ticker | PC3 loading |
|---|---|
| MU | +0.87 |
| SNDK | -0.33 |
| WDC | -0.37 |

PC3 isolates MU from the spinoff pair — MU's diversified DRAM/NAND/HBM exposure trades differently from the more narrow WDC (HDD) and SNDK (NAND) businesses.

### Factor decomposition

| Benchmarks | R² | Residual factor |
|---|---|---|
| SOXX only | 54.8% | 45.2% |
| SOXX + SMH | 54.8% | 45.2% (SMH adds nothing) |
| SOXX + SMH + SPY | 55.5% | 44.5% |

44.5% residual factor after benchmarks — meaningfully higher than [[WFE]] (22%) or [[AI Compute]] (22%), comparable to [[Defense primes basket|Defense primes]] (36%) and lower than [[Space pure-plays]] (59.6%). US Memory has a genuine cohort-specific factor — the memory cycle is real and not fully captured by broad semis ETFs.

### Subset optimization (1Y)

| Pair | Intra-corr | Tracking corr | Sharpe | Cum % |
|---|---|---|---|---|
| SNDK + WDC | 0.648 | 0.981 | 4.30 | +420.5% |
| MU + SNDK | 0.762 | 0.972 | 3.97 | +370.0% |
| MU + WDC | 0.682 | 0.955 | 3.49 | +202.0% |

The SNDK+WDC pair has the highest Sharpe (4.30) AND highest cumulative return (+420.5%). The Feb 2025 spinoff pair has been the cohort's standout trade. Different pattern from larger cohorts where factor-tracking and Sharpe-optimal diverge — here both objectives concentrate on SNDK pairs because SNDK is dominating the cohort by every measure.

### Per-name 1Y cumulative return

| Ticker | 1Y return |
|---|---|
| [[SanDisk\|SNDK]] | +710.0% |
| [[Western Digital\|WDC]] | +234.5% |
| [[Micron\|MU]] | +172.7% |

SNDK's +710% 1Y is one of the most extreme single-name returns in any tested cohort. Driven by the Feb 2025 spinoff pricing + NAND-cycle inflection. SNDK has the highest PC1 loading (0.747) AND the highest return — same pattern as AMD in AI Compute. At N=3 the cohort's biggest mover anchors the factor and drives all subset returns.

Pairwise detail:
| Pair | Correlation |
|------|-------------|
| MU - WDC | 0.70 |
| MU - SNDK | 0.42 |
| WDC - SNDK | 0.39 |

US Memory moves with US market sentiment, not Korean memory peers.

---

## Characteristics

| Factor | US Memory | vs Korea Memory |
|--------|-----------|-----------------|
| HBM exposure | Micron \#3 (catching up) | SK Hynix \#1, Samsung \#2 |
| NAND strength | SanDisk pure-play | Kioxia JV partner |
| Geopolitical | CHIPS Act beneficiary | Export control risk |
| Currency | USD | KRW exposure |

---

## Investment angle

Why separate from Korea Memory:
- Different currency exposure
- Different policy tailwinds (CHIPS Act vs Korean industrial policy)
- Different HBM positioning (lagging vs leading)
- Correlation data confirms distinct trading behavior

For portfolio construction: US Memory and Korea Memory are separate bets, not interchangeable "memory exposure."

---

## Related

### Parent
- [[Memory]] — parent sector

### Sister
- [[Korea Memory]] — Korean memory cluster

### Actors
- [[Micron]] — US memory champion
- [[SanDisk]] — NAND pure-play
- [[Western Digital]] — former memory (now HDD)

### Context
- [[CHIPS Act]] — policy tailwind
- [[Memory shortage 2025-2026]] — cycle driver

*Created 2026-01-30*
