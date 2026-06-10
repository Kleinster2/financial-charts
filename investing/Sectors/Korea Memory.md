---
aliases: [Korean memory]
---
#sector #memory #semiconductor #korea

# Korea Memory

> [!success] Cluster status: validated micro-cluster (Jun 2026)
> Pair correlation 0.756, PC1 87.82%, random-basket p = 0.0031, threshold-stable width 0.45. [[Samsung]] / [[SK Hynix]] form a clean two-name [[Memory|memory]] pair at distance 0.244, with strong separation from [[US Memory]], [[EWY]], and semiconductor ETFs. Re-validated Jun 10 2026 against the cleaned stock-only null (10,000 permutations, Phipson-Smyth; pair correlation 0.731 on the refreshed window, holdout ratio 1.36 STRENGTHENING).

Korean [[Memory|memory]] giants. Trades as a distinct micro-cluster separate from [[US Memory]]. Dominates [[HBM]].

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

## Cluster validation

Run via `scripts/cluster_configs/korea_memory.yaml` with parameters matched to other vault cohorts (1Y window through 2026-05-07, threshold 0.5; refreshed diagnostic files dated Jun. 7 2026). The Samsung-SK Hynix pair is a validated micro-cluster: the N=2 structure makes advanced sub-cluster diagnostics less meaningful than in larger cohorts, but the boundary result is clean and robust.

![[korea-memory-cluster-20260607-correlation-1y.png]]
*1Y correlation heatmap: Samsung / SK Hynix are tight internally and weakly correlated with US memory, EWY, and broad semiconductor ETFs.*

![[korea-memory-cluster-20260607-dendrogram-1y.png]]
*Dendrogram: Samsung and SK Hynix form their own branch at distance 0.244 and stay uncontaminated across the threshold scan.*

![[korea-memory-cluster-20260607-pca-1y.png]]
*PCA diagnostic: PC1 explains 87.82% of standardized daily-return variance; at N=2 this is the pair correlation expressed as a common factor.*

![[korea-memory-cluster-20260607-rolling-tightness-90d.png]]
*Rolling tightness: latest 90-day avg correlation is 0.862 and PC1 is 93.1%, confirming a sharply strengthening pair.*

### Headline diagnostics

| Metric | Value (1Y matched) |
|---|---|
| Pair correlation (Samsung-SK Hynix) | 0.756 |
| PC1 explained variance | 87.82% (trivially high at N=2) |
| vs [[US Memory]] cohort | 0.094 (cluster intra-advantage +0.66) |
| Random-basket p-value | 0.006 |
| Threshold-stable width | 0.45 (robust) |
| Verdict | Validated micro-cluster |

The pair-only N=2 structure means PC2/PC3 analysis isn't informative (PCA at N=2 is just the bivariate correlation). The 0.756 reading is meaningful directionally — Samsung and SK Hynix have decoupled materially from US memory peers and now trade as a tight 2-name HBM-leadership pair. See [[Vault cluster taxonomy]] for cross-cohort context.

### Join distance topology

Candidate-only average-linkage topology, with distance measured as `1-|corr|`:

| Step | Left | Right | Distance (1-\|corr\|) | Members |
|---|---|---|---:|---|
| 1 | [[Samsung\|005930.KS]] | [[SK Hynix\|000660.KS]] | 0.244 | 005930.KS + 000660.KS |

Topology and PC1-mimic composition point to the same structure: a two-name HBM-leadership pair, not a broader Korea-equity or semiconductor-ETF branch.

### PC1 index weights

| Ticker | PC1 loading | Loading weight | Ann vol | Raw PC1-mimic weight |
|---|---:|---:|---:|---:|
| [[Samsung\|005930.KS]] | 0.707 | 50.00% | 57.92% | 55.21% |
| [[SK Hynix\|000660.KS]] | 0.707 | 50.00% | 71.40% | 44.79% |

PC1 loading weights are mechanically equal at N=2. Raw PC1-mimic weight tilts toward Samsung because lower realized volatility requires more Samsung notional to replicate the standardized pair factor.

### Historical tightness evolution

| Year | Avg corr | PC1 | Final join distance |
|---|---:|---:|---:|
| 2020 | 0.654 | 82.7% | 0.346 |
| 2021 | 0.657 | 82.9% | 0.343 |
| 2022 | 0.729 | 86.5% | 0.271 |
| 2023 | 0.653 | 82.6% | 0.347 |
| 2024 | 0.517 | 75.8% | 0.483 |
| 2025 | 0.433 | 71.6% | 0.567 |
| 2026 | 0.801 | 90.0% | 0.199 |
| Latest 90D | 0.862 | 93.1% | 0.138 |

Historical read: structurally durable and strengthening. The pair weakened in 2024-2025 as Samsung lagged SK Hynix's HBM execution, then snapped tighter in 2026 as both names became pulled into the same HBM scarcity / Korea macro-upgrade factor.

### Stability across windows — TIGHTENING

| Window | Obs | Pair corr | PC1 | Vs SPY | Intra-SPY gap |
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

## Macro pass-through

The Korea Memory cluster has become large enough to move [[South Korea]]'s national forecast. First-quarter 2026 semiconductor exports reached $78.5bn, up 139% year over year, with the acceleration concentrated in memory demand tied to AI servers. On May 28, 2026, the [[Bank of Korea]] raised its 2026 GDP forecast to 2.6% from 2.0% and attributed +0.7 percentage points of growth to stronger semiconductor and IT exports, more than offsetting the -0.4 percentage-point drag from the [[2026 Iran conflict market impact|Iran-war]] energy shock.

That confirms the cluster's distinct behavior in the correlation work above. [[Samsung]] and [[SK Hynix]] are no longer just country beta or generic memory cyclicals; they are the domestic growth engine strong enough to affect monetary-policy arithmetic. The trade still carries KRW, energy, and China proximity risk, but the upside driver is now explicitly macro-recognized HBM scarcity.

*Sources: [[Financial Times|FT]], "AI boom outweighs Iran war pain, Korean central bank chief says," May 28 2026: https://www.ft.com/content/2d1c6dbb-aef5-4f08-bc5a-20c0aa3c1149; Bank of Korea, "Economic Outlook (May 2026)": https://www.bok.or.kr/eng/bbs/E0000634/view.do?depth=400423&menuNo=400423&nttId=10098207&programType=newsDataEng&relate=Y; Aju Press report citing Ministry of Trade, Industry and Energy Q1 export data, May 6 2026: https://www.ajupress.com/view/20260506170570667.*

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

### Jun. 5 2026 global memory selloff

FT's Jun. 5 [[Nasdaq semiconductor selloff June 2026]] linked the US chip drawdown to Korea memory as well: SK Hynix fell 10% and Samsung Electronics fell 6% in the article's reported tape. The local vault database did not have Jun. 5 Korea closes available during ingestion, so those figures remain FT-attributed rather than locally verified.

The point for this note is transmission. The same HBM scarcity that made Korea Memory a macro-recognized growth engine also makes it part of the global AI-duration trade when US rates reprice higher and investors question the near-term AI-capex financing window.

*Source: [FT](https://www.ft.com/content/2929bbd3-1f71-4424-a577-f016c3c65603), Jun. 5 2026.*

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
