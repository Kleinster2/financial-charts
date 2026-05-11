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
