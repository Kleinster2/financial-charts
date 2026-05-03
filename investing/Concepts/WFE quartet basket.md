---
aliases: [WFE quartet, Wafer fab equipment quartet, Semi equipment quartet, WFE]
tags: [basket/internal, semiconductor, equipment, ai]
---

# WFE quartet basket

> [!success] Cluster status: validated — tightest 4-name basket (May 2026)
> Intra-cluster correlation 0.804, PC1 85.3% explained variance. The tightest 4-name basket surfaced across the entire validation pass — pairwise correlations 0.74-0.86 across all 6 pairs, no exceptions. Cleaner expression of "leading-edge fab capex" than the broader [[AI capex chain basket]] (7-name AICX, intra-corr 0.61, PC1 66.3%). The four names share monopoly/duopoly market positions, identical end-market exposure (every leading-edge fab buys from all four), and synchronized capex cycles. See "Cluster validation" section below.

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
| Hierarchical clustering at 0.4 | All 4 cluster + NVDA, TSM, MU + broad semi ETFs (SMH, SOXX, XLK, SPY) | Broader AI/semi block formation |
| Cluster vs hyperscalers (MSFT, GOOGL, AMZN, META) | 0.287 (+0.517 advantage) | Cleanly distinct from buyers |
| Cluster vs fabless (AMD, AVGO) | 0.492 (+0.312 advantage) | Distinct from non-AI-capex chip designers |
| Cluster vs broad ETFs (SMH, SOXX, XLK, SPY) | 0.718 (+0.085 advantage) | WFE IS the dominant factor inside SMH/SOXX |

### Pairwise correlations (1Y)

|  | ASML | AMAT | KLAC | LRCX |
|---|---|---|---|---|
| ASML | — | 0.75 | 0.74 | 0.79 |
| AMAT | 0.75 | — | 0.83 | 0.86 |
| KLAC | 0.74 | 0.83 | — | 0.85 |
| LRCX | 0.79 | 0.86 | 0.85 | — |

The tightest 3-name sub-cluster within WFE is AMAT/KLAC/LRCX (avg 0.85) — these three are the US-listed WFE pure-plays and trade nearly as one. ASML is slightly looser due to EUV-specific dynamics (TSM customer concentration, EUV unit shipment cadence, China export-control news).

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

![[wfe-quartet-basket-2026ytd-price-chart.png]]

*ASML (blue, primary) vs AMAT, KLAC, LRCX normalized from 2025-12-31. Visual co-movement is striking — the four lines move as a tight band through the Feb-Mar drawdown and April recovery. AMAT/KLAC/LRCX especially track essentially together; ASML modestly divergent (EUV-specific dynamics).*

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
