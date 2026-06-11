---
aliases: [AI power IPPs, AI-power independent power producers, Merchant power AI cohort]
---
#concept #power #ai #cohort

**AI-power IPPs** — the four US merchant/independent power producers the market trades as one AI-electricity factor: [[Vistra]] (VST), [[Constellation Energy]] (CEG), [[NRG Energy]] (NRG), and [[Talen Energy]] (TLN). Each owns dispatchable generation (nuclear and gas) in ERCOT/PJM and has converted it into hyperscaler power deals; the tape prices them as a single trade.

> [!success] Cluster status: validated cohort (Jun 10, 2026)
> Intra-correlation 0.773 (1y), PC1 82.99%, join topology complete at 0.245, holdout ratio 0.91 STABLE, threshold-stable width 0.25 (intact, zero contamination, [0.25, 0.50]). Permutation tests (cleaned stock-only null, 10,000 draws, Phipson-Smyth): random-basket p = 0.0001 on both intra-correlation and PC1 (cohort beat all 10,000 draws; null mean 0.137, 99th pct 0.359); vol-matched basket p = 0.0001 on both (null mean 0.165) — the factor is not shared beta/vol. Definition date 2026-06-10 (forward ledger).

---

## Synthesis

This is the rare thematic basket that is also a statistical fact. The four names share 0.773 average pairwise correlation over the trailing year, a single factor explains 83% of their joint variance with near-equal loadings, and the structure survives weekly-return cross-checks, a temporal holdout, and every clustering threshold from 0.25 to 0.50 without admitting a single outside name. More telling than the level is the vintage: rolling tightness shows the factor forming in 2025 — average intra-correlation jumped from ~0.51 (2024) to ~0.81 (2025) — which is precisely the year the hyperscaler-PPA wave hit ([[Constellation Energy]]-[[Microsoft]] TMI restart, [[Talen Energy]]-[[Amazon]] co-location expansion, [[Vistra]]-[[Meta]] 2.6 GW nuclear deal, [[NRG Energy]]'s [[GE Vernova]] gas program). The market did not discover an old factor; it manufactured a new one out of the [[Power constraints]] story. The boundary findings matter as much as the cohort: regulated utilities (DUK/SO/AEP) cluster with XLU and not with the IPPs — this is not a utilities trade — and the equipment complex (GEV/ETN/PWR) is the nearest neighbor but only joins at distances above 0.55. The unresolved question is whether a factor born in one narrative year survives a demand repricing: on June 10, 2026 the adjacent equipment names fell 6-8% as a bloc on rate and AI-capex anxiety, the first stress test of whether the IPP factor decouples (contracted megawatt-hours) or follows (same narrative beta).

## The cohort

| Member | Fleet anchor | AI-demand deal |
|--------|-------------|----------------|
| [[Vistra]] | Comanche Peak nuclear (2 reactors, 2.4 GW, ERCOT) + gas; 4 reactors total | [[Meta]] 2.6 GW 20-year nuclear deal (Jan 2026); [[xAI]] a potential Texas customer; best-performing S&P 500 stock of 2024 |
| [[Constellation Energy]] | Largest US power producer (~55 GW, post-[[Calpine]]) | [[Microsoft]] TMI Unit 1 restart — 20-yr, 835 MW PPA (Crane Clean Energy Center); regulatory friction on new DC deals (Mar 2026) |
| [[NRG Energy]] | ERCOT/East gas fleet + Reliant retail | Up to 5.4 GW new CCGT with [[GE Vernova]]/Kiewit (1.2 GW 7HA slots; in service 2029-2032); DC developer LOIs |
| [[Talen Energy]] | [[Susquehanna]] nuclear (~2.5 GW, PA) | [[Amazon]] behind-the-meter co-location, 960 MW — the largest nuclear-DC deal |

Cohort surfaced empirically as the tightest block (0.773 intra) in the [[Solaris Energy Infrastructure]] speed-to-power panel run the same day. Config: `scripts/cluster_configs/ai_power_ipp.yaml`.

## Cluster validation

![[ai-power-ipp-cluster-dendrogram-1y.png]]
*Hierarchical clustering (average linkage, 1-|corr|, cut 0.4): the four IPPs form one clean cluster; regulated utilities cluster separately with XLU; nuclear fuel (CCJ/UEC) and grid equipment (GEV/ETN/PWR) are distinct blocks. The cohort is not a utilities, fuel-cycle, or equipment trade.*

### Headline diagnostics

| Diagnostic (1y to 2026-06-10) | Value | Read |
|---|---|---|
| Intra-cohort avg correlation | 0.773 (pairwise range 0.734-0.815) | Far above the 0.6 cluster bar |
| PC1 explained variance | 82.99% (PC2 6.7%) | One-factor cohort |
| Weekly cross-check | 0.647 intra, PC1 73.7% | Holds on weekly returns — not an async-close artifact |
| Holdout (2y temporal split) | Train 0.846/88.5% → test 0.773/83.0%; ratio 0.91; loadings corr 0.90 | STABLE — durable across regimes (caveat: train half only 58 obs from TLN's relisting history) |
| Threshold scan | Intact, zero contamination across [0.25, 0.50]; width 0.25 | ROBUST — boundary not threshold-sensitive; equipment names join only at ≥0.55 |
| Permutation p (random-basket, 10k, Phipson-Smyth) | 0.0001 intra / 0.0001 PC1 (null mean 0.137 / 37.9%; 99th pct 0.359 / 53.0%) | Beat all 10,000 draws — floor p-value |
| Permutation p (vol-matched basket, 10k) | 0.0001 intra / 0.0001 PC1 (null mean 0.165 / 39.0%) | Cohesion exceeds same-vol random baskets — not shared beta/vol |

### Join distance topology

| Step | Left | Right | Distance (1-\|corr\|) | Members |
|------|------|-------|----------------------|---------|
| 1 | VST | TLN | 0.185 | VST+TLN |
| 2 | CEG | VST+TLN | 0.221 | CEG+VST+TLN |
| 3 | NRG | CEG+VST+TLN | 0.245 | NRG+CEG+VST+TLN |

All four join below 0.25 — no stragglers, no satellite structure. At threshold 0.20 the cohort splits into a VST+TLN core (the two pure nuclear-co-location stories) with CEG/NRG one step out.

### PC1 index weights

![[ai-power-ipp-cluster-pca-1y.png]]
*PCA scree and PC1 loadings on the candidate cohort: one dominant factor, near-equal loadings.*

| Member | PC1 loading | Loading weight | Ann vol | Raw PC1-mimic weight |
|--------|-------------|----------------|---------|----------------------|
| VST | 0.514 | 25.71% | 51.13% | 25.37% |
| CEG | 0.497 | 24.86% | 49.54% | 25.32% |
| NRG | 0.491 | 24.56% | 46.27% | 26.77% |
| TLN | 0.497 | 24.87% | 55.65% | 22.54% |

An equal-weight basket is effectively the factor — no member dominates, and vol-scaling barely moves the weights.

### Historical tightness evolution

![[ai-power-ipp-cluster-rolling-tightness-90d.png]]
*Rolling 90-day tightness: the factor emerges in 2025 — a factor with a birthday.*

| Year | Avg corr | PC1 | Core corr | Satellite corr | Final join distance |
|------|----------|-----|-----------|----------------|---------------------|
| 2024 | 0.505 | 63.2% | 0.415 | 0.585 | 0.541 |
| 2025 | 0.810 | 85.8% | 0.770 | 0.851 | 0.222 |
| 2026 | 0.773 | 83.0% | 0.747 | 0.802 | 0.250 |

Latest 90d: avg corr 0.768, PC1 82.6%, final join distance 0.260. The 2024→2025 jump (+0.305 in average correlation) dates the factor's creation to the PPA wave.

### Correlation structure

![[ai-power-ipp-cluster-correlation-1y.png]]
*1-year pairwise correlations across the 16-name panel: the IPP block is the deepest-blue square; regulated utilities correlate with each other and XLU but only ~0.4-0.5 with the IPPs.*

Full numerics: `investing/attachments/ai-power-ipp-cluster-results.txt`, `-holdout.txt`, `-threshold-scan.txt`.

## Boundary findings

- Not regulated utilities: DUK/SO/AEP cluster with XLU, away from the cohort. Rate-base economics and merchant AI-PPA economics price differently.
- Not the fuel cycle: [[Cameco|CCJ]]/UEC form their own pair — uranium trades supply/contracting cycles, not PPA announcements (both fell harder than the IPPs in the June 10 risk-off).
- Nearest neighbor, still distinct: grid equipment (GEV/ETN/PWR) joins only above 0.55 — same narrative, different cash-flow mechanics (orders vs contracted megawatt-hours).
- [[Vistra]]'s own sector-correlation table (XLK 0.70) shows the cohort's deeper truth: these trade as technology-demand derivatives, not as utilities.

## What to watch

- Factor integrity under stress — does the cohort stay tight in drawdowns (shared repricing) or disperse (idiosyncratic contract value)? June 10, 2026's power risk-off is the live test; re-run the config after the episode settles.
- New PPA prints — each hyperscaler deal (counterparty, $/MWh where disclosed, tenor) re-rates the whole block; the factor is a deal-flow expectation machine.
- Regulatory friction — [[Constellation Energy]]'s March 2026 friction on new DC deals; FERC/state treatment of behind-the-meter co-location (the Talen-Amazon precedent) and the PJM BYOG proposals flagged in all four member notes decide how much fleet monetizes at AI prices.
- Gas-turbine delivery slots — NRG's 2029-2032 CCGT schedule depends on [[GE Vernova]] 7HA availability; slot slippage converts growth stories back into merchant-power stories.
- Cohort membership drift — candidates knocking on the boundary (restart/SMR names, [[Calpine]]-adjacent assets inside CEG); re-test before adding any name to the basket.

## Related

- [[Power constraints]] — the scarcity the cohort monetizes
- [[Nuclear power for AI]] — the nuclear-PPA thread (TMI, Susquehanna)
- [[Firm power]] — why dispatchable fleets capture the AI premium
- [[Vistra]] / [[Constellation Energy]] / [[NRG Energy]] / [[Talen Energy]] — members
- [[Solaris Energy Infrastructure]] — adjacent speed-to-power name (statistically distinct; its panel surfaced this cohort)
- [[Hyperscaler capex]] — the demand side
- [[BYOP]] — policy risk channel (PJM BYOG proposals)
- [[Energy and Utilities]] — sector hub
- [[Power equipment complex]] — the contrast case: equipment co-moves but is boundary-dependent vs industrials (Jun 2026 test); the IPP factor is the standalone trade

*Created 2026-06-10. Validation artifacts in `investing/attachments/ai-power-ipp-cluster-*`; config `scripts/cluster_configs/ai_power_ipp.yaml`.*
