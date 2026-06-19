---
aliases: [Wafer Fab Equipment, Semiconductor Equipment, Semi Equipment]
tags: [sector, semiconductor, equipment, cluster-validation]
---

# WFE

> [!success] Cluster status: validated — the vault's tightest cohort (the structural ceiling), but ETF-embedded (Jun 2026)
> The four wafer-fab-equipment oligopolists ([[ASML]]/[[Applied Materials|AMAT]]/[[KLA|KLAC]]/[[Lam Research|LRCX]]) are the tightest validated cohort in the campaign. Intra-corr 0.819 (weekly 0.793), PC1 86.5%; all four join below distance 0.22; rejects the random-basket AND vol-matched nulls at the 0.0001 floor; holdout STABLE 0.91; durable 0.82–0.91 every year since 2020. But the cohort never isolates as a clean island — it IS a major weight in the semiconductor ETFs, so SMH/SOXX/XLK contaminate the cluster from threshold 0.30 (stable width 0.00) and the intra-advantage over those ETFs is only +0.077. A real, exceptionally durable, vol-matched-robust factor whose basket is replicated by SMH/SOXX. See "Cluster validation" below.

Wafer fab equipment — the picks and shovels of semiconductors. The tightest sector correlation in the vault (intra-corr 0.82) because the four names share the same handful of leading-edge customers and one shared capex cycle.

![[wfe-sector-chart.png]]
*LRCX outperforming, but all four move together — AMAT-LRCX is the tightest pair.*

---

## Key actors

| Company | Focus | Position |
|---------|-------|----------|
| [[ASML]] | Lithography (EUV monopoly) | Irreplaceable, highest margins |
| [[Applied Materials]] | Deposition, etch, CMP | Broadest portfolio |
| [[Lam Research]] | Etch, deposition | Memory + logic |
| [[KLA]] | Inspection, metrology | Quality control |

---

## Cluster validation

The candidate cohort is the four wafer-fab-equipment oligopolists — [[ASML]], [[Applied Materials|AMAT]], [[KLA|KLAC]], [[Lam Research|LRCX]] — tested against the rest of the AI-capex chain (AI-compute peers NVDA/TSM/MU, fabless AMD/AVGO, hyperscaler buyers MSFT/GOOGL/AMZN/META) and the semiconductor + market ETFs (SMH/SOXX/XLK/SPY). Refreshed 2026-06-19 on a 1Y window through 2026-06-18, threshold 0.5. Terminology: [[Cohort, cluster, basket]].

### Diagnostics summary

| Diagnostic | Value | Read |
|---|---|---|
| Intra-cluster corr (1Y) | 0.819 [0.759–0.872] | very tight; weekly 0.793 |
| PC1 explained variance | 86.5% | strong single factor (weekly 84.5%) |
| Independence null p | 0.0001 | series co-move |
| Random-basket null p | 0.0001 (PC1 0.0001) | rejects at the floor — a real factor |
| Vol-matched null p | 0.0001 (PC1 0.0001) | not just shared semis beta/vol |
| Holdout (2Y split) | STABLE 0.91 | durable (train 0.899 → test 0.821; loadings corr 0.79) |
| Threshold clean width | 0.00 [0.25 point] | EMBEDDED — SMH/SOXX/XLK contaminate from 0.30 |
| Intra-adv vs AI-capex peers (NVDA/TSM/MU) | +0.211 | distinct from compute/memory |
| Intra-adv vs fabless (AMD/AVGO) | +0.273 | distinct from chip designers |
| Intra-adv vs semis ETFs (SMH/SOXX/XLK/SPY) | +0.077 | NOT distinct — the cohort is the ETF |

1Y daily log returns through 2026-06-18, threshold 0.5. All US-listed/synchronous. Config: `scripts/cluster_configs/wfe_quartet.yaml`; registry row 2026-06-19. This is the structural-ceiling reference for the campaign — no thematic-basket cohort is expected to exceed WFE's tightness, because the four-oligopolists-one-capex-cycle constraint isn't replicable.

### Boundary — a tight core embedded in the semis-ETF complex

![[wfe-quartet-cluster-dendrogram-1y.png]]
*Hierarchical clustering at 0.5. The four WFE names form the tight core (joining 0.13–0.22), but they sit inside one cluster with the semiconductor ETFs SMH/SOXX/XLK and the rest of the AI-capex chain (NVDA/TSM/MU/AMD/AVGO). SMH+SOXX are the single tightest pair on the chart. The mega-cap software/internet buyers (MSFT/GOOGL/AMZN/META) split off separately.*

The threshold scan keeps the WFE quartet intact only at the single point 0.25 (stable width 0.00). From 0.30 the semiconductor ETFs (SMH/SOXX/XLK) plus TSM join the cluster, and by 0.45 the whole AI-capex chain (NVDA/TSM/MU/AMD/AVGO) is inside it. That is the "real but embedded" signature: the four names genuinely co-move (intra 0.82) but they constitute a large slice of SMH/SOXX, so the ETFs are inseparable from the cohort. The cohort is distinct from the AI-compute peers (+0.211) and the fabless designers (+0.273), but only +0.077 from the semis ETFs — the basket is replicable by SMH/SOXX.

### Topology — a homogeneous four-name block

Reading the candidate cohort by join distance (average linkage, 1−|corr|):

| Join step | Names | Distance (1-\|corr\|) | Read |
|---|---|---|---|
| 1 | AMAT + LRCX | 0.128 | tightest pair (corr 0.87) |
| 2 | KLAC + (AMAT+LRCX) | 0.153 | KLA joins the etch/deposition core |
| 3 | ASML + (KLAC+AMAT+LRCX) | 0.217 | lithography joins last; cohort closes below 0.22 |

All four join below distance 0.22 (correlation above 0.78) — a homogeneous block with no core/satellite split. [[Applied Materials]] and [[Lam Research]] are the tightest pair (the deposition/etch overlap); [[KLA]] joins the etch/deposition core; [[ASML]] (lithography, the most differentiated process step) joins last but still inside 0.22. Same customers, one capex cycle.

### PC1 index weights

![[wfe-quartet-cluster-pca-1y.png]]
*PCA on the cohort. PC1 explains 86.5% with near-identical loadings (0.48–0.51) — a clean single factor.*

| Ticker | PC1 loading | Loading weight | Ann vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| ASML | 0.483 | 24.2% | 44.8% | 27.9% |
| AMAT | 0.505 | 25.3% | 52.4% | 24.9% |
| KLAC | 0.499 | 25.0% | 54.2% | 23.9% |
| LRCX | 0.512 | 25.6% | 56.9% | 23.3% |

Near-equal loadings — the four are interchangeable expressions of one WFE factor. The lower-volatility [[ASML]] takes the largest raw PC1-mimic weight (27.9%) despite joining the tree last, because it needs more notional to reproduce the standardized common shock; the higher-vol [[Lam Research]] takes the smallest. Tight trading core (AMAT/LRCX/KLAC) vs PC1-replication weight (ASML-heavy) disagree, as expected when realized vols differ.

### Distinctness — embedded in the semis ETFs

![[wfe-quartet-cluster-correlation-1y.png]]
*1Y pairwise correlation heatmap. The WFE block is uniformly hot and so are the semiconductor ETFs (SMH/SOXX); the cohort runs warm against the whole AI-capex chain and cool only against the hyperscaler buyers and SPY.*

The defining number is the +0.077 intra-advantage over the semiconductor ETFs: WFE is a major constituent of SMH and SOXX, so the cohort cannot separate from them at any normal threshold. It is genuinely distinct from the AI-compute peers (+0.211 vs NVDA/TSM/MU — the equipment cycle is not the compute cycle), from the fabless designers (+0.273 vs AMD/AVGO), and overwhelmingly from the hyperscaler buyers (+0.572). The investable read: own SMH or SOXX for the WFE factor — a bespoke four-name basket adds almost nothing over the liquid ETF, which is the [[Vault cluster taxonomy|cross-cohort]] "real but embedded" verdict (the same shape as [[Mega banks basket|mega banks]] = XLF or the commodity-equity cohorts = their sector ETF).

### Statistical falsification

| Test | Result | Verdict |
|---|---|---|
| Random-basket null (10k) | p 0.0001 (intra + PC1) | rejects at the floor |
| Vol-matched null (10k) | p 0.0001 (intra + PC1); null mean intra 0.18 | rejects — cohesion exceeds same-vol baskets |
| Holdout (2Y temporal split) | ratio 0.91; train 0.899 → test 0.821; loadings corr 0.79 | STABLE across regimes |
| Threshold scan (0.20–0.70) | stable [0.25] only, width 0.00 | EMBEDDED (ETFs contaminate from 0.30) |

The vol-matched pass matters: WFE clears random baskets of comparably volatile names, so the cohesion is a real equipment-cycle factor, not just shared high semis beta. The only "failure" is the threshold scan's zero width — but per the [[Vault cluster taxonomy]] reading of zero-width, high-intra + stable-holdout is the embedded-factor pattern (real co-movement that never separates from a parent complex), not a falsification.

### Historical tightness evolution

![[wfe-quartet-cluster-rolling-tightness-90d.png]]
*Rolling 90-day cohesion, 2020–2026. Exceptionally durable — 0.82–0.91 every single year, the most structurally stable cohort in the campaign alongside [[Crypto-to-AI]].*

| Year | Avg intra-corr | PC1 |
|---|---|---|
| 2020 | 0.823 | 86.8% |
| 2021 | 0.843 | 88.3% |
| 2022 | 0.914 | 93.5% |
| 2023 | 0.854 | 89.1% |
| 2024 | 0.869 | 90.2% |
| 2025 | 0.839 | 87.9% |
| 2026 | 0.827 | 87.0% |

Latest 90-day reading: intra 0.862, PC1 89.6%. WFE never leaves the 0.82–0.91 band across six years, including the 2022 rate shock (where it actually peaked at 0.914 as the whole capex complex sold off together). That durability is the tell of a structural factor — four oligopolists on one capex cycle do not decohere — and it is what makes WFE the campaign's upper-bound reference.

### Sub-structure and factor share

PC2 (6.5%) and PC3 (4.0%) carry the only within-cohort sub-structure, and it is the persistent process-step split: [[ASML]] (lithography/EUV) and [[KLA]] (inspection/metrology) are the two most differentiated businesses, [[Applied Materials|AMAT]] and [[Lam Research|LRCX]] (deposition/etch) the overlapping pair. The sub-structure is small (PC1 absorbs 86.5%) — a single-factor cohort with a faint process-step second axis. Against the broad semis ETFs the cohort retains roughly a fifth of its variance as a WFE-specific residual factor (May 2026 deep-dive: ~22% residual after SOXX/SMH), far below pure-play cohorts like [[Space pure-plays]] (59.6%) — because WFE *is* the semis-ETF core rather than a slice orthogonal to it. Any two-name subset tracks the full basket tightly, and the 1Y return dispersion is narrow (all four captured the AI-capex tailwind without single-name divergence), unlike the wide dispersion in [[Space pure-plays]] or [[Crypto-to-AI]].

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

[[Long WFE]] — Leveraged bet on semiconductor capex without picking chip winners. Note the cluster-validation caveat: because the WFE quartet is embedded in SMH/SOXX (intra-advantage only +0.077), the liquid semis ETF expresses the same factor — a bespoke four-name basket adds little over SMH/SOXX.

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

### Cluster framework
- [[Vault cluster taxonomy]] — cross-cohort meta-analysis (WFE is the tightness ceiling)
- [[Cohort, cluster, basket]] — terminology

*Created 2026-01-30. Cluster validation refreshed 2026-06-19 (1Y window through 2026-06-18; config `scripts/cluster_configs/wfe_quartet.yaml`; registry row 2026-06-19). The 2026-06-19 refresh also corrected an un-back-adjusted [[KLA]] 10-for-1 split (Jun 2026) that had temporarily collapsed the cohort. Cluster validation is structure, not a performance ranking — see `docs/cluster-validation.md`.*
