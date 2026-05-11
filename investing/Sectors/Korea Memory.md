---
aliases: [Korean memory]
---
#sector #memory #semiconductor #korea

# Korea Memory

Korean memory giants. Trades as a distinct cluster (0.56 correlation) separate from US Memory. Dominates HBM.

![[korea-memory-sector-chart.png]]
*SK Hynix outperforming Samsung — HBM leadership driving divergence. Both trade distinctly from US memory peers.*

---

## Key actors

| Company | Focus | Position |
|---------|-------|----------|
| [[Samsung]] | DRAM + NAND + HBM | \#1 DRAM, \#1 NAND, \#2 HBM |
| [[SK Hynix]] | DRAM + NAND + HBM | \#2 DRAM, \#2 NAND (via Solidigm), \#1 HBM |

---

## Correlation structure

| Metric | Value | Interpretation |
|--------|-------|----------------|
| Avg correlation | 0.53 | Moderate (valid sector) |
| vs Korea ETF (EWY) | 0.30-0.38 | Country factor present |
| vs [[US Memory]] | 0.09-0.21 | Weak (separate cluster) |
| Period | 2024-01 to present | |

### Matched-methodology re-run (May 2026)

Run via `scripts/cluster_configs/korea_memory.yaml` with parameters matched to other vault cohorts (1Y window through 2026-05-07, threshold 0.5). The Samsung-SK Hynix pair has tightened materially:

| Metric | Value (1Y matched) |
|---|---|
| Pair correlation (Samsung-SK Hynix) | 0.756 |
| PC1 explained variance | 87.82% (trivially high at N=2) |
| vs [[US Memory]] cohort | 0.094 (cluster intra-advantage +0.66) |
| Verdict | Validated as pair |

The pair-only N=2 structure means PC2/PC3 analysis isn't informative (PCA at N=2 is just the bivariate correlation). The 0.756 reading is meaningful directionally — Samsung and SK Hynix have decoupled materially from US memory peers and now trade as a tight 2-name HBM-leadership pair. See [[Vault cluster taxonomy]] for cross-cohort context.

### Stability across windows — TIGHTENING

| Window | Obs | Pair corr | PC1 | Vs SPY | Gap |
|---|---|---|---|---|---|
| YTD 2026 | 75 | 0.861 | 93.3% | -0.048 | +0.909 |
| 1Y | 116 | 0.757 | 88.4% | -0.037 | +0.793 |
| 2Y | 165 | 0.733 | 87.3% | +0.080 | +0.653 |
| 3Y | 256 | 0.707 | 86.2% | +0.096 | +0.612 |

The Samsung-SK Hynix pair has been tightening monotonically: 0.707 (3Y) → 0.733 (2Y) → 0.757 (1Y) → 0.861 (YTD). Same tightening trajectory as [[Space pure-plays]] but at higher absolute levels. The Korean memory pair has decoupled from SPY entirely — vs-SPY correlation is essentially zero (-0.05 YTD).

### Factor decomposition — the unique vault finding

| Benchmarks | R² | Residual factor |
|---|---|---|
| EWY only | 1.6% | 98.4% |
| EWY + SOXX | 2.3% | 97.7% |
| EWY + SOXX + SMH + SPY | 4.3% | 95.7% |

Korea Memory's 95.7% residual factor share is the highest of any tested cohort in the vault — well above [[Space pure-plays]] (59.6%). The pair is essentially unexplained by any benchmark, including EWY (the Korean equity ETF supposedly capturing Korean country factor).

Important caveat: the high residual share at N=2 partly reflects the pair-correlation being the factor itself. At N=2 PCA captures the bivariate relationship; there's no "common cohort factor across multiple names" interpretation in the same sense as larger cohorts. But the structural finding remains: Samsung-SK Hynix is uncorrelated with broad benchmarks AND uncorrelated with Korean country factor. The HBM-leadership story drives the pair's returns independently of any tradable index.

### Per-name 1Y cumulative return

The pair has divergent individual returns but tight daily co-movement — see existing "HBM dominance" section above for the SK Hynix outperformance driven by NVIDIA preferred supplier status.

### Why advanced patterns don't apply at N=2

The Korea Memory cohort is the smallest in the validated set. Several framework diagnostics aren't informative at N=2:

- PC2 / PC3 sub-structure: there are only 2 dimensions; PC1 captures 88% and PC2 captures the residual 12%, but interpretation is just "what's left after the pair correlation"
- Hierarchical clustering: trivially groups the 2 names together
- Subset optimization: only 1 pair possible (which IS the cohort)
- Swiss-Army-knife pattern: not meaningful at N=2

The pair is best understood as a validated micro-cluster (in the same category as the [[UAS defense micro-cluster|KTOS-AVAV pair]]) rather than a full cohort. The advanced patterns codified in [[Vault cluster taxonomy]] require N≥3 to apply meaningfully.

Pairwise detail:
| Pair | Correlation |
|------|-------------|
| Samsung - SK Hynix | 0.57 |
| Samsung - EWY | 0.30 |
| SK Hynix - EWY | 0.38 |

Korea Memory moves with Korean market/won, not US memory peers.

---

## HBM dominance

| Company | HBM Position | Notes |
|---------|--------------|-------|
| [[SK Hynix]] | \#1 | NVIDIA preferred supplier |
| [[Samsung]] | \#2 | Catching up, yield issues |
| [[Micron]] | \#3 | Distant third |

Korea controls ~95% of HBM production — the premium AI memory product.

---

## Characteristics

| Factor | Korea Memory | vs US Memory |
|--------|--------------|--------------|
| HBM exposure | Dominant (\#1, \#2) | Micron catching up (\#3) |
| Scale | Samsung largest memory co globally | Micron smaller |
| Currency | KRW exposure | USD |
| Geopolitical | China exposure risk | CHIPS Act tailwind |

---

## Investment angle

Why separate from US Memory:
- HBM leadership (SK Hynix \#1, Samsung \#2)
- KRW currency exposure
- Different risk profile (China proximity)
- Correlation data confirms distinct trading behavior

The [[Short TSMC long Korea]] thesis captures this — Korea memory is a distinct geographic/sector bet.

---

## Related

### Parent
- [[Memory]] — parent sector

### Sister
- [[US Memory]] — American memory cluster

### Actors
- [[SK Hynix]] — HBM leader
- [[Samsung]] — scale leader

### Context
- [[Memory shortage 2025-2026]] — cycle driver
- [[HBM]] — premium product (Korea dominates)
- [[Short TSMC long Korea]] — thesis

*Created 2026-01-30*
