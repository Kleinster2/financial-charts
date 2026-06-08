---
aliases: [AICX, AI capex basket, AI semi capex chain, Hyperscaler supplier chain basket]
tags: [basket/internal, ai, semiconductor, infrastructure]
---

# AI capex chain basket

> [!success] Cluster status: validated (May 2026)
> Intra-cluster correlation 0.61, PC1 66.3% explained variance. Hierarchical clustering at 0.4 returns the 7 candidate names + broad semi ETFs as one block. Tightest sub-basket: WFE quartet (ASML, AMAT, KLAC, LRCX, intra-corr 0.81). See "Cluster validation" section below.

The mathematically-validated tradable cluster the [[AI hyperscalers]] thesis pointed at. Hyperscaler equity returns themselves do not co-move (intra-corr 0.29 — see [[AI hyperscalers]] for the falsified hyperscalers cluster section), but the SUPPLIERS the hyperscalers spend on do. This basket isolates the AI infrastructure capex factor at its tightest point: chip designers + leading-edge foundry + memory + wafer fabrication equipment.

Validated 2026-05-03 — intra-corr 0.61, PC1 66.3%, hierarchical clustering at 0.4 returns the seven names plus broad semi ETFs as a coherent block. The wafer fabrication equipment quartet (ASML, AMAT, KLAC, LRCX) is the tightest sub-basket in the entire AI complex (intra-corr 0.81, pairwise range 0.74-0.86).

---

## Constituents

Seven names. Equal-weighted starting point — refine to factor weights after first cycle of cluster behavior.

| Ticker | Company | Role in chain | PC1 loading | Why it belongs |
|--------|---------|---------------|-------------|----------------|
| NVDA | [[NVIDIA]] | Lead chip designer (GPU dominance) | 0.321 | Demand-side anchor of the entire AI capex cycle |
| TSM | [[TSMC]] | Leading-edge foundry (~90% advanced node share) | 0.374 | Single point of execution for almost every AI chip |
| ASML | [[ASML]] | EUV lithography monopoly | 0.365 | Required input for every leading-edge node — no alternative |
| AMAT | [[Applied Materials]] | Deposition / etch / inspection | 0.377 | Broadest WFE platform; leverage to every fab buildout |
| KLAC | [[KLA Corporation]] | Process control / metrology | 0.378 | Essential for yield improvement at advanced nodes |
| LRCX | [[Lam Research]] | Etch and deposition (memory + logic) | 0.394 | Memory ramp + logic capex both fund LRCX |
| MU | [[Micron]] | HBM memory (AI training stack input) | (joins via algorithmic clustering) | HBM is the memory bottleneck for training |

Total: 7 constituents. Internal ticker: AICX.

### YTD 2026 cohort tracking

![[aicx-basket-2026ytd-price-chart.png]]

*NVDA (blue, primary) vs MU, AMAT, LRCX, KLAC, ASML, TSM normalized from 2025-12-31. The visual confirms the math: all 7 names move together through the Feb-Mar drawdown and April recovery. Cohort spread reveals sub-thesis differentiation — MU leads at +85% YTD on HBM ramp; the WFE quartet (AMAT, LRCX, KLAC, ASML) is visually tight as a group at +35-55%; TSM lags at +5-10% reflecting Taiwan-risk overhang and its already-dominant index weight.*

### What is excluded — and why

| Excluded | Why excluded |
|----------|--------------|
| [[AMD]] | Singleton in cluster analysis — trades on NVDA-competitor narrative (share-take story), not the AI capex factor. Different business cycle. |
| [[Broadcom]] | Singleton in cluster analysis — diversified custom-silicon + VMware integration. AI accelerator exposure diluted by networking and software segments. |
| [[Intel]] / [[GlobalFoundries]] | Trail leading-edge foundry race; trade on idiosyncratic turnaround/maturity stories rather than AI-capex factor. See [[Foundry monopoly consolidation]] cluster validation section for the math. |
| [[Samsung]] | Korean listing (005930.KS), trades on Korean market beta + memory cycle that dominates the consolidated entity. |
| [[AI hyperscalers]] cohort (MSFT, GOOGL, AMZN, META, ORCL) | The buyers. Cohort failed cluster validation (intra-corr 0.29) — each has dominant idiosyncratic factor (cloud share, ad market, retail/cloud weighting, OpenAI partnership terms). |

The exclusions are not value judgments on the businesses — they are statistical findings. Each excluded name is its own factor.

---

## Jun 2026 Broadcom exclusion checkpoint

[[Broadcom]]'s Q2 FY26 reaction reinforces the exclusion rather than weakening it. The company printed $10.8B of AI semiconductor revenue and guided Q3 AI semiconductor revenue to $16.0B, but AVGO still fell 12.6% on Jun. 4 because the market wanted a larger raise to the 2027 AI-chip trajectory. That is a custom-silicon expectations event, not the same factor as the validated AICX supplier chain.

The useful basket read is dispersion. [[SMH]] fell 1.6%, [[NVIDIA]] rose 1.9%, [[Marvell]] rose 4.9%, [[AMD]] fell 3.6%, and [[Micron]] fell 7.7%. Broad semis did not move as one clean block around AVGO. Until AVGO re-enters the algorithmic cluster, Broadcom remains a singleton watch item adjacent to AICX rather than a constituent.

---

## Cluster validation

Procedure: `scripts/cluster_analysis.py --config scripts/cluster_configs/hyperscaler_suppliers.yaml`. Full standard in `docs/cluster-validation.md`.

### Headline numbers (1Y, 2025-04-30 to 2026-04-30)

| Diagnostic | Result | Interpretation |
|---|---|---|
| Avg intra-cluster correlation | 0.609 (range 0.43-0.86) | Strong cohesion |
| Tightest pairwise | LRCX-AMAT = 0.86 | WFE within itself = cleanest pair anywhere in the AI complex |
| WFE-quartet intra-corr | 0.81 (ASML, AMAT, KLAC, LRCX) | Tightest sub-basket of the validation pass |
| PC1 explained variance | 66.3% | Dominant single factor; equal-weighted basket ≈ factor |
| Hierarchical clustering at 0.4 | All 7 cluster + broad semi ETFs (SMH, SOXX, XLK, SPY) | Cluster validated; cluster IS the broad semi tape |
| Cluster vs hyperscalers | 0.305 (+0.30 advantage) | Cleanly separable from the buyers |
| Cluster vs other semis (INTC, QCOM) | 0.432 (+0.18 advantage) | Distinct from non-AI-capex semis |
| Cluster vs broad ETFs | 0.707 (-0.10 NEGATIVE) | Cluster IS the dominant factor in broad ETFs right now |

### Pairwise correlations (1Y)

|  | NVDA | AMD | AVGO | TSM | ASML | AMAT | KLAC | LRCX |
|---|---|---|---|---|---|---|---|---|
| NVDA | — | — | 0.60 | 0.67 | 0.53 | 0.48 | 0.51 | 0.54 |
| AMD | — | — | 0.47 | 0.58 | 0.43 | 0.52 | 0.53 | 0.55 |
| AVGO | 0.60 | 0.47 | — | 0.65 | 0.48 | 0.47 | 0.46 | 0.51 |
| TSM | 0.67 | 0.58 | 0.65 | — | 0.67 | 0.65 | 0.67 | 0.72 |
| ASML | 0.53 | 0.43 | 0.48 | 0.67 | — | 0.75 | 0.74 | 0.79 |
| AMAT | 0.48 | 0.52 | 0.47 | 0.65 | 0.75 | — | 0.83 | 0.86 |
| KLAC | 0.51 | 0.53 | 0.46 | 0.67 | 0.74 | 0.83 | — | 0.85 |
| LRCX | 0.54 | 0.55 | 0.51 | 0.72 | 0.79 | 0.86 | 0.85 | — |

The structure is visible directly in the matrix:
- WFE quartet (ASML/AMAT/KLAC/LRCX) corner is uniformly red — pairwise 0.74-0.86, the tightest 4×4 block.
- TSM bridges WFE to chip designers — equally correlated with WFE (0.65-0.72) and chip designers (0.65-0.67).
- NVDA, AMD, AVGO are looser among themselves (0.47-0.60) — chip designers don't all trade together.

---

## The WFE quartet — see dedicated note

ASML, AMAT, KLAC, LRCX are now formalized as their own sub-cluster note: see [[WFE quartet basket]] for full validation (intra-corr 0.81, PC1 85.3% — tightest 4-name basket in the validation pass), pairwise structure, and trade implications. Brief summary below; full analysis in the dedicated note.

ASML, AMAT, KLAC, LRCX are the cleanest cluster the validation pass has surfaced. Pairwise 0.74-0.86, intra-corr 0.81. Why it works:

| Mechanic | Effect |
|---|---|
| Same end-market | Every leading-edge fab (TSMC, Samsung, Intel) buys from all four |
| Capex cycle | Equipment capex moves together — when fabs build, all four ship |
| No customer concentration risk | TSMC is too big to leave any of them; replacement inventory + service revenue compound |
| Limited substitutes | ASML EUV is monopoly; AMAT/KLAC/LRCX near-duopoly with very few credible alternatives |
| Cycle synchronization | All four report capex commentary on similar quarterly cadence |

Trade expression: equal-weighted ASML/AMAT/KLAC/LRCX basket = cleanest single isolation of "leading-edge fab capex" available in public equity.

### Why each WFE name belongs

- [[ASML]] — EUV monopoly. Without ASML, no leading-edge node. Sole provider of the most expensive single tool in the fab ($150M+ EUV scanner).
- [[Applied Materials]] — Broadest WFE portfolio (deposition, etch, ion implant, inspection). Closest to a "buy WFE as a sector" trade in a single name.
- [[KLA Corporation]] — Process control and metrology. The yield-improvement layer — every node transition needs KLA tools to ramp efficiently.
- [[Lam Research]] — Etch and deposition. Memory ramp (HBM, DRAM, NAND) plus logic — dual exposure to AI accelerator capex and memory cycle.

---

## How this fits the broader AI capex thesis

The chain decomposes into three tightly-coupled layers:

```
Hyperscaler capex (NOT a cluster — see [[AI hyperscalers]])
    ↓
Chip designers — NVDA (anchor), AMD/AVGO/MRVL (singleton, off-factor)
    ↓
Leading-edge foundry — TSM (monopoly, AICX-correlated)
    ↓
Memory — MU/HBM (AICX-correlated), [[SK Hynix]] (Korean listing not in basket)
    ↓
Wafer fab equipment — ASML, AMAT, KLAC, LRCX (TIGHTEST SUB-BASKET)
```

The hyperscaler buyers don't co-move because they each have their own product cycle. But the single-purpose suppliers downstream of them DO, because they all ramp together when fab capacity expands.

---

## May 2026 allocator confirmation

The May 21, 2026 FT interview with [[James Anderson]] and [[Morgan Samet]] is useful because it reaches the same conclusion from portfolio construction rather than from the vault's cluster math. Anderson's argument is that AI has changed the platform economics of Big Tech: the buyers of infrastructure lose the old low-capex free-cash-flow profile, while suppliers with scarce hardware capacity keep pricing power. Samet's version is the customer-refusal test: right now hyperscalers cannot say no to the bottleneck suppliers.

That is exactly the distinction this basket formalizes. [[Microsoft]], [[Alphabet]], [[Amazon]], [[Meta]], and [[Oracle]] create the demand, but [[NVIDIA]], [[TSMC]], [[ASML]], [[Applied Materials]], [[KLA Corporation]], [[Lam Research]], and [[Micron]] form the tighter co-moving exposure. The FT source is not needed to prove the cluster; it is useful because it shows a long-duration growth investor explicitly rotating the narrative from platform owners to the hardware chain.

*Sources: [Financial Times — Big Tech software era is over, says top investor James Anderson](https://www.ft.com/content/9d2bd5b3-80c6-49b9-a04b-edc4162c9320), May 21 2026; [Reuters via Investing.com — ASML CEO sees tight supply](https://www.investing.com/news/stock-market-news/exclusiveasml-ceo-sees-tight-supply-in-booming-chip-market-as-ai-demand-soars-4701446), May 20 2026.*

---

## Trade implications

| Trade | Expression | Factor isolated |
|---|---|---|
| Long AI capex factor (broad) | Equal-weighted AICX basket (7 names) | AI infrastructure capex cycle |
| Long the tightest expression | Equal-weighted WFE quartet | Leading-edge fab buildout |
| Long monopoly | TSM directly (or via SMH where TSM is largest holding) | TSM-specific dominance |
| Pair: long AICX / short hyperscalers | AICX vs MSFT/GOOGL/AMZN/META basket | Suppliers benefit more than buyers from capex |
| Pair: long WFE / short fabless | ASML/AMAT/KLAC/LRCX vs NVDA/AMD | Equipment cycle vs chip-design competition |
| AVOID — long AICX vs short SMH | Cluster IS most of SMH's exposure | Captures ~10% noise, not factor |

The last row is the negative finding. The cluster correlates 0.71 with SMH/XLK — meaning AICX *is* the dominant factor inside the broad semi/tech ETF. The cleanest expression of "long AI capex" is the cluster itself or the WFE quartet, not a long/short vs SMH (which would be near-zero net exposure).

---

## What could break the cluster

| Scenario | Effect on AICX |
|---|---|
| Hyperscaler capex pause (revenue miss → guide cut) | All 7 names re-rate together; cluster cohesion increases on the way down |
| TSM-specific shock ([[Taiwan]] disruption) | Cluster fractures: TSM crashes, WFE may decouple if production shifts to Samsung/Intel |
| WFE customer concentration crack (e.g., TSMC sourcing from competitors) | Quartet co-movement loosens; ASML-monopoly position protected longer than AMAT/KLAC/LRCX |
| AI training compute demand collapse (LLM ROI thesis breaks) | Cluster persists during selloff — the math says AICX IS the AI-equity expression |
| Custom silicon win share (AVGO/MRVL/Marvell take from NVDA) | NVDA decouples from cluster; WFE/TSM continue (still need fab capacity) |

The first scenario (capex pause) is the most likely cluster-cohesion test in the next 6 months. Watch for hyperscaler Q3 2026 capex commentary.

---

## Tracking

- AICX index methodology to be added once `scripts/create_aicx_index.py` is written. Equal-weighted starting point; revisit after first full quarter of validated co-movement.
- Re-run cluster validation quarterly: `python scripts/cluster_analysis.py --config scripts/cluster_configs/hyperscaler_suppliers.yaml`.
- Watch for AMD/AVGO re-entry to the algorithmic cluster — would signal AI-capex factor broadening to include custom silicon.
- Watch for WFE quartet decohesion — would signal capex cycle topping or customer concentration crack.

---

## Cluster validation compliance addendum (2026-06-07)

Generated from `scripts/cluster_configs/hyperscaler_suppliers.yaml` using `scripts/cluster_analysis.py` methodology. The 1Y diagnostic window is 2025-05-01 to 2026-04-30 (171 observations); the rolling history starts at `2020-01-01` where data are available.

### Required validation plots

![[hyperscaler-suppliers-cluster-correlation-1y.png]]

*One-year correlation heatmap for the `Hyperscaler supplier chain` validation universe.*

![[hyperscaler-suppliers-cluster-dendrogram-1y.png]]

*Hierarchical clustering tree using average linkage on distance `1-|corr|`.*

![[hyperscaler-suppliers-cluster-pca-1y.png]]

*PCA diagnostic for the candidate cohort; PC1 explains 65.8% of standardized daily-return variance.*

### PC1 index weights vs cluster topology

The topology table answers which names join the tree first or last. The raw PC1-mimic table answers which raw-return weights best replicate the standardized common factor after realized-volatility scaling. These are deliberately different readings of the same cluster.

| Step | Left | Right | Distance (1-\|corr\|) | Read |
|---|---|---|---|---|
| 1 | AMAT | LRCX | 0.142 | Tightest merge |
| 2 | KLAC | AMAT+LRCX | 0.171 | Candidate cohort merge step |
| 3 | ASML | KLAC+AMAT+LRCX | 0.244 | Candidate cohort merge step |
| 4 | TSM | ASML+KLAC+AMAT+LRCX | 0.326 | Candidate cohort merge step |
| 5 | NVDA | AVGO | 0.419 | Candidate cohort merge step |
| 6 | TSM+ASML+KLAC+AMAT+LRCX | NVDA+AVGO | 0.478 | Candidate cohort merge step |
| 7 | AMD | TSM+ASML+KLAC+AMAT+LRCX+NVDA+AVGO | 0.486 | Final cohort join / loosest boundary |

| Ticker | PC1 loading | Normalized loading weight | Ann. vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| NVDA | 0.315 | 11.21% | 35.16% | 14.27% |
| AMD | 0.304 | 10.79% | 60.07% | 8.04% |
| AVGO | 0.303 | 10.78% | 45.03% | 10.72% |
| TSM | 0.376 | 13.35% | 36.57% | 16.35% |
| ASML | 0.366 | 13.00% | 40.87% | 14.24% |
| AMAT | 0.378 | 13.43% | 48.59% | 12.38% |
| KLAC | 0.377 | 13.40% | 49.15% | 12.21% |
| LRCX | 0.395 | 14.05% | 53.35% | 11.80% |

Interpretation: use the dendrogram / join-distance topology to identify the tight core and later-joining members; use the Raw PC1-mimic weight column only for investable factor-replication sizing.

### Historical tightness evolution

![[hyperscaler-suppliers-cluster-rolling-tightness-90d.png]]

*Ninety-day rolling tightness diagnostic: avg intra-correlation, PC1 share, core correlation, satellite-to-core correlation, and final candidate join distance.*

| Year | Avg corr median | PC1 median | Core corr median | Satellite-to-core median | Final join distance median |
|---|---|---|---|---|---|
| 2021 | 0.685 | 72.9% | 0.702 | 0.637 | 0.414 |
| 2022 | 0.767 | 79.8% | 0.773 | 0.740 | 0.308 |
| 2023 | 0.779 | 81.0% | 0.785 | 0.752 | 0.312 |
| 2024 | 0.671 | 71.7% | 0.682 | 0.640 | 0.415 |
| 2025 | 0.735 | 77.0% | 0.746 | 0.699 | 0.316 |
| 2026 | 0.628 | 68.1% | 0.648 | 0.565 | 0.474 |

Latest 90D through 2026-04-30: avg corr 0.619, PC1 67.5%, core corr 0.646, satellite-to-core corr 0.540, final join distance 0.497.

Historical verdict: structurally durable cluster; rolling cohesion has usually stayed in single-factor territory.

---

## Related

### Member actors

- [[NVIDIA]] — chip designer anchor
- [[TSMC]] — leading-edge foundry
- [[ASML]] — EUV monopoly
- [[Applied Materials]] — broad WFE platform
- [[KLA Corporation]] — process control / yield
- [[Lam Research]] — etch and deposition
- [[Micron]] — HBM memory

### Adjacent concept notes

- [[AI hyperscalers]] — the FAILED cluster (buyers don't co-move) that this basket is the constructive answer to
- [[Hyperscaler capex]] — capex narrative that drives AICX
- [[Foundry monopoly consolidation]] — falsified cluster (TSM has no peers); confirms TSM's central position in AICX
- [[Lingotto]] — Anderson/Samet source of May 2026 allocator confirmation
- [[Boutique advisory consolidation]] — adjacent VALIDATED cluster (different sector; same validation pattern)
- [[Alternative asset managers basket]] — adjacent VALIDATED cluster (different sector; tighter than boutique)
- [[Advanced packaging]] — CoWoS as foundry-side moat
- [[HBM]] — memory bottleneck driving MU inclusion
- [[AI Chip]] — broader sector hub
- [[Semiconductors]] — broader sector hub

### Excluded names (and why)

- [[AMD]] — singleton (NVDA-competitor narrative; off-factor)
- [[Broadcom]] — singleton (diversified)
- [[Intel]], [[GlobalFoundries]] — foundry standalones
- [[Samsung]] — Korean listing, memory beta dominates

### Methodology

- `docs/cluster-validation.md` — standard procedure
- `scripts/cluster_analysis.py` — generalized cluster validation script
- `scripts/cluster_configs/hyperscaler_suppliers.yaml` — config for this cluster

*Created 2026-05-03 — first concept note created under the new cluster-validation standard*
