---
aliases: [WFE quartet, Wafer fab equipment quartet, Semi equipment quartet, WFE]
tags: [basket/internal, semiconductor, equipment, ai]
---

# WFE quartet basket

> [!warning] Cluster status: validated high-cohesion sub-cluster; dendrogram boundary fragile (May 2026)
> Intra-cluster correlation 0.804, PC1 85.3% explained variance, and random-basket null rejected at p = 0.004 / 0.003 (intra-corr / PC1). The four-name WFE core is economically and statistically real, with stable holdout performance, but the clean dendrogram boundary is fragile: WFE is isolated only at a tight threshold (0.25) and joins the broader AI / semis / ETF block at looser 0.30-0.50 cuts. Treat this as the cleanest "leading-edge fab capex" factor core inside [[AI capex chain basket]], not as a standalone tree branch separable from semis ETFs at every threshold.

The four wafer fabrication equipment (WFE) leaders — ASML, Applied Materials, KLA, Lam Research — comprise the cleanest tight sub-basket inside the AI complex. They share end-market (every leading-edge fab is a customer of all four), share monopoly/duopoly positions in their respective tool segments, and report on synchronized quarterly capex commentary cycles. The 0.81 intra-correlation is among the tightest 4-name baskets in any sector tested.

---

## Constituents

4 names. Equal-weighted starting point; the loadings are essentially balanced.

| Ticker | Company | PC1 loading | Tool segment | Market position |
|--------|---------|-------------|--------------|-----------------|
| ASML | [[ASML]] | 0.479 | EUV / DUV lithography | Monopoly (EUV is sole-source for advanced nodes) |
| AMAT | [[Applied Materials]] | 0.505 | Deposition + etch + ion implant + inspection | Broadest WFE platform; near-duopoly across most tools |
| KLAC | [[KLA Corporation]] | 0.502 | Process control + metrology (yield) | Near-monopoly in advanced inspection |
| LRCX | [[Lam Research]] | 0.514 | Etch + deposition (memory + logic) | Near-duopoly with AMAT in dry etch + ALD |

Internal ticker proposal: WFE.

### Why this 4-name basket and not others

The 4 are the only WFE pure-plays at scale. Other tool vendors (Tokyo Electron, ASM International, Disco, Screen Holdings) are international and not in local DB; ASMI and TEL would likely cluster tightly with this quartet if tested. NVIDIA, AMD, AVGO are chip designers, not equipment vendors. TSM is the foundry customer. MU is memory.

### Excluded — and why

| Excluded | Why excluded |
|----------|--------------|
| Tokyo Electron, ASM International, Disco, Screen Holdings | International listings not in local DB; would likely cluster with WFE if added |
| [[NVIDIA]], [[AMD]], [[Broadcom]] | Fabless chip designers; clustering varies (NVDA in [[AI capex chain basket]], AMD/AVGO singletons) |
| [[TSMC]] | Foundry customer of WFE; clusters with the broader AICX |
| [[Micron]] | Memory; in AICX but not WFE |

---

## Cluster validation

Procedure: `scripts/cluster_analysis.py --config scripts/cluster_configs/wfe_quartet.yaml`. Standard in `docs/cluster-validation.md`.

### Headline numbers (1Y, 2025-04-30 to 2026-04-30)

| Diagnostic | Result | Interpretation |
|---|---|---|
| Avg intra-cluster correlation | 0.804 (range 0.74-0.86) | Strong cohesion; tightest 4-name basket in validation pass |
| Tightest pair | LRCX-AMAT = 0.86 | Etch/deposition complementarity |
| LRCX-KLAC = 0.85, AMAT-KLAC = 0.83 | All near-tightest | Inter-tool capex cycle synchronizes |
| Loosest pair | ASML-LRCX = 0.79 (still very tight) | EUV monopoly slightly decoupled from etch/deposition cycle |
| PC1 explained variance | 85.3% | Single dominant factor; equal-weighted basket ≈ factor |
| Hierarchical clustering | All 4 WFE names remain together, but threshold 0.30+ admits TSM / ETFs and threshold 0.40-0.50 admits broader AI-semi names | WFE is a tight sub-cluster inside the semis capex factor, not a clean isolated branch |
| Cluster vs hyperscalers (MSFT, GOOGL, AMZN, META) | 0.287 (+0.517 advantage) | Cleanly distinct from buyers |
| Cluster vs fabless (AMD, AVGO) | 0.492 (+0.312 advantage) | Distinct from non-AI-capex chip designers |
| Cluster vs broad ETFs (SMH, SOXX, XLK, SPY) | 0.718 (+0.085 advantage) | WFE IS the dominant factor inside SMH/SOXX |
| Random-basket null | p = 0.004 intra-corr; p = 0.003 PC1 | Cohesion is not a random four-name artifact |
| Temporal holdout | Test/train intra-corr ratio 0.87; PC1 loading correlation 0.758 | Durable but less tight than the older half |
| Threshold stability | Clean WFE-only assignment only at 0.25; stable-width 0.00 | Boundary-fragile; must be caveated |

### Required validation plots

![[wfe-quartet-cluster-correlation-1y.png]]

*One-year pairwise correlation heatmap. The candidate WFE block is uniformly high (0.74-0.86), with AMAT/LRCX/KLAC especially tight.*

![[wfe-quartet-cluster-dendrogram-1y.png]]

*Hierarchical clustering tree. The WFE four-name core stays together, but the nearby AI-semi / ETF names join quickly at looser thresholds, so the boundary is less clean than the intra-correlation alone implies.*

![[wfe-quartet-cluster-pca-1y.png]]

*PCA diagnostic. PC1 explains 85.3% of candidate-cohort variance, and all four loadings are positive and balanced (0.479-0.514), so an equal-weighted basket closely tracks the WFE factor.*

### Robustness diagnostics

| Test | Result | Read |
|---|---|---|
| Random-basket permutation | p = 0.004 for intra-corr; p = 0.003 for PC1 | Pass: the cohort is more cohesive than a random four-name basket from the same price universe |
| Holdout | Train intra-corr 0.927; test intra-corr 0.804; test/train ratio 0.87 | Pass with cooling: the factor remains durable in the newer half |
| Threshold scan | Clean WFE-only threshold only at 0.25; contamination begins at 0.30 | Caveat: the economic cluster is real, but dendrogram separability is threshold-sensitive |

![[wfe-quartet-cluster-permutation.png]]

![[wfe-quartet-cluster-holdout.png]]

![[wfe-quartet-cluster-threshold-scan.png]]

### Pairwise correlations (1Y)

|  | ASML | AMAT | KLAC | LRCX |
|---|---|---|---|---|
| ASML | — | 0.75 | 0.74 | 0.79 |
| AMAT | 0.75 | — | 0.83 | 0.86 |
| KLAC | 0.74 | 0.83 | — | 0.85 |
| LRCX | 0.79 | 0.86 | 0.85 | — |

The tightest 3-name sub-cluster within WFE is AMAT/KLAC/LRCX (avg 0.85) — these three are the US-listed WFE pure-plays and trade nearly as one. ASML is slightly looser due to EUV-specific dynamics (TSM customer concentration, EUV unit shipment cadence, China export-control news).

### PC1 index weights vs cluster topology

The topology and the investable PC1-mimic answer different questions. The dendrogram says AMAT/LRCX/KLAC are the tight trading core, with ASML joining later as the lithography-monopoly satellite. The raw PC1-mimic says ASML still needs the largest notional weight because the PCA is run on standardized returns and ASML has the lowest realized volatility.

| Step | Left | Right | Distance (1-\|corr\|) | Read |
|---:|---|---|---:|---|
| 1 | AMAT | LRCX | 0.142 | Tightest WFE pair |
| 2 | KLAC | AMAT+LRCX | 0.171 | KLAC joins the US semicap core |
| 3 | ASML | KLAC+AMAT+LRCX | 0.244 | ASML belongs, but as the later-joining EUV satellite |

| Ticker | PC1 loading | Normalized loading weight | Ann. vol | Raw PC1-mimic weight |
|---|---:|---:|---:|---:|
| ASML | 0.480 | 24.00% | 40.87% | 27.99% |
| AMAT | 0.506 | 25.30% | 48.59% | 24.81% |
| KLAC | 0.499 | 24.95% | 49.15% | 24.20% |
| LRCX | 0.515 | 25.75% | 53.35% | 23.00% |

Interpretation: for a cluster-purity sleeve, AMAT/LRCX/KLAC are the core. For a raw-return basket that best replicates the standardized PC1 factor, use the volatility-adjusted PC1-mimic weights: ASML 28.0%, AMAT 24.8%, KLAC 24.2%, LRCX 23.0%.

### Historical tightness evolution

![[wfe-quartet-cluster-rolling-tightness-90d.png]]

*Ninety-day rolling diagnostic through Jun. 5 2026. WFE has been structurally tight since 2021: avg intra-correlation and PC1 share usually sit above 0.80, while AMAT/LRCX/KLAC remain the tighter core. The main regime change is ASML's satellite behavior: ASML detached sharply in late 2025, then mostly rejoined by mid-2026.*

| Year | Avg corr median | PC1 median | Core corr median | ASML-to-core median | Final join distance median |
|---|---:|---:|---:|---:|---:|
| 2021 | 0.853 | 89.0% | 0.902 | 0.804 | 0.196 |
| 2022 | 0.874 | 90.6% | 0.923 | 0.824 | 0.176 |
| 2023 | 0.888 | 91.6% | 0.926 | 0.850 | 0.150 |
| 2024 | 0.835 | 87.8% | 0.897 | 0.770 | 0.230 |
| 2025 | 0.869 | 90.3% | 0.919 | 0.817 | 0.183 |
| 2026 | 0.820 | 86.5% | 0.843 | 0.799 | 0.205 |

| Date | Avg corr | PC1 | Core corr | ASML-to-core | Final join distance | Read |
|---|---:|---:|---:|---:|---:|---|
| 2025-06-18 | 0.921 | 94.1% | 0.953 | 0.889 | 0.111 | Peak WFE cohesion |
| 2025-12-31 | 0.746 | 81.1% | 0.825 | 0.667 | 0.333 | ASML detach; core stays intact |
| 2026-06-05 | 0.835 | 87.7% | 0.861 | 0.809 | 0.191 | Rejoined materially, still satellite |

Interpretation: WFE is not a newly formed cluster. It is a durable semicap factor with a persistent AMAT/LRCX/KLAC core and a recurring ASML satellite leg. Historical evolution supports keeping ASML in the factor basket, but it also validates treating ASML-specific EUV / China / shipment-cadence shocks as the main source of temporary decohesion.

---

## Why the cluster is so tight

Five mechanics converge to make WFE the tightest 4-name basket in the AI complex:

| Mechanic | Effect |
|---|---|
| Same end-market | Every leading-edge fab (TSMC, Samsung, Intel, SK Hynix) buys from all four |
| Synchronized capex cycle | Equipment orders move together — when fabs build, all four ship |
| No customer concentration risk | Each name has TSM, Samsung, Intel as anchor customers; no one customer can leave any of them |
| Monopoly/duopoly tool positions | ASML EUV monopoly; AMAT/KLAC/LRCX near-duopoly with very few credible alternatives |
| Quarterly capex commentary cycle | All four report on similar quarterly cadence; capex guides tend to move in same direction |

This is a textbook structural cluster — same business, same end-market, same cycle.

---

## YTD 2026 cohort tracking

![[wfe-quartet-basket-through-2026-06-05-price-chart.png]]

*ASML (blue, primary) vs AMAT, KLAC, LRCX normalized from 2025-12-31 through the Jun. 5 2026 close. The quartet still moves as one WFE factor, but the fresh tape now captures the Jun. 5 chip-equipment drawdown after the early-June peak; LRCX and AMAT remain the YTD leaders while ASML is the lower-beta EUV-monopoly leg.*

| Ticker | Start close (Dec. 31 2025) | Latest close (Jun. 5 2026) | YTD return |
|---|---:|---:|---:|
| ASML | $1,066.12 | $1,641.74 | +54.0% |
| AMAT | $256.67 | $453.01 | +76.5% |
| KLAC | $1,213.50 | $1,929.20 | +59.0% |
| LRCX | $170.98 | $303.28 | +77.4% |

---

## Trade implications

| Trade | Expression | Factor isolated |
|---|---|---|
| Long WFE factor (cleanest expression of "leading-edge fab capex") | Equal-weighted ASML + AMAT + KLAC + LRCX | Leading-edge fab buildout cycle |
| Long US-listed WFE only | AMAT + KLAC + LRCX (intra 0.85) | US WFE pure-play; avoids ASML/EUV-specific China exposure |
| Long WFE / short hyperscalers | WFE basket vs MSFT/GOOGL/AMZN/META | Suppliers benefit more than buyers from capex (+0.52 separation) |
| Long WFE / short fabless (AMD, AVGO) | Captures equipment cycle vs chip-design competition (+0.31) | Equipment exposure clean of fabless competitive dynamics |
| AVOID: long WFE / short SMH | WFE IS the dominant factor inside SMH (+0.09 marginal advantage) | Near-zero net exposure |
| Pair: long ASML / short LRCX | Captures EUV-monopoly vs etch-cycle differential | Limited usefulness; mostly noise |

The +0.52 separation from hyperscalers is the most important trade implication — same capex chain but the suppliers have cleaner factor exposure than the buyers.

---

## What could break the cluster

| Scenario | Effect on cluster |
|---|---|
| Hyperscaler capex pause | All 4 names re-rate together; cluster cohesion increases on the way down |
| Fab geographic shift (Arizona, Japan, Germany) | Cluster persists — same companies still equipping new fabs |
| China export-control escalation | ASML decouples (China-specific exposure); AMAT/KLAC/LRCX less affected |
| New WFE entrant gains share (unlikely given high barriers) | Affected segment (AMAT competitor for deposition?) decouples |
| Customer-side consolidation (e.g., TSMC absorbs Samsung WFE share) | Cluster cohesion increases — TSM dominance funnels equipment spend to single customer |
| AI training compute demand collapse | Cluster persists — WFE IS the cleanest equity expression of AI capex |

---

## Tracking

- Re-run validation quarterly: `python scripts/cluster_analysis.py --config scripts/cluster_configs/wfe_quartet.yaml`.
- Watch ASML's PC1 loading vs the AMAT/KLAC/LRCX 3-name tight core — China exposure or EUV unit cadence may pull ASML out.
- Watch for foreign WFE entries (Tokyo Electron, ASM International) — should likely join cluster if added to local DB.
- Cross-check vs [[AI capex chain basket]] — WFE is the tightest sub-cluster within AICX.

---

## Related

### Member actors

- [[ASML]] — EUV monopoly
- [[Applied Materials]] — broadest WFE platform
- [[KLA Corporation]] — process control / yield
- [[Lam Research]] — etch and deposition

### Adjacent concept notes

- [[AI capex chain basket]] — parent (7-name AICX that contains WFE quartet as the tightest sub-cluster)
- [[Foundry monopoly consolidation]] — TSM dominance is the customer-side factor that drives WFE
- [[Hyperscaler capex]] — demand-side narrative
- [[AI hyperscalers]] — failed cluster (the buyers); WFE is the constructive supplier-side answer
- [[Advanced packaging]] — adjacent CoWoS / SoIC capex story
- [[Semiconductors]] — sector hub

### Methodology

- `docs/cluster-validation.md` — standard procedure
- `scripts/cluster_analysis.py` — generalized cluster validation script
- `scripts/cluster_configs/wfe_quartet.yaml` — config for this cluster

*Created 2026-05-03 — thirteenth concept note created under the new cluster-validation standard; the tightest 4-name basket in the validation pass*
