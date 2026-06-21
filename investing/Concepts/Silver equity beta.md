---
aliases: [Silver equity beta, Silver miners, Silver miner cohort, Silver mining cluster]
tags: [concept, commodities, metals, silver, mining, cluster-validation]
---

# Silver equity beta

Whether the listed silver miners trade as one factor — and if so, what it is. The cohort is five primary silver miners: [[Pan American Silver]] (PAAS), [[Hecla Mining]] (HL), [[Coeur Mining]] (CDE), [[Fortuna Mining]] (FSM), [[First Majestic Silver]] (AG). The validation answers yes, very tightly — but the factor is not even silver-specific: the silver miners are one precious-metals-mining complex with the gold miners. This is the campaign's cleanest commodity-beta result, extending the law one rung from "miners = their own metal" to "precious-metals miners = one metals-mining complex."

> [!warning] Cluster status: validated cohesion, but it is the precious-metals complex — silver miners don't even separate from gold miners (June 2026)
> The five silver miners are an exceptionally tight, durable, single-factor cohort: intra-corr 0.821 (weekly 0.837), PC1 85.8%, rejecting the independence, random-basket and vol-matched nulls all at the 0.0001 floor, holdout STRENGTHENING (1.11 — tightening into the 2025-26 precious-metals bull). But it is commodity beta, not a distinct equity factor — and not even distinct from gold. The decisive numbers: a ~zero +0.008 intra-advantage versus the silver complex ([[SIL]]/SLV — they ARE the silver price), and a NEGATIVE −0.041 versus the gold miners ([[GDX]]) — the silver miners correlate with gold miners MORE than with each other. The threshold scan never isolates them: [[SIL]] and [[GDX]] both contaminate from 0.20 (the tightest cut), SLV from 0.30. So gold and silver mining are ONE factor, captured equally by GDX, SIL, or SLV; the silver names are simply its higher-beta (56-75% annualized vol) expression. The gold/silver/royalty cohorts all collapse into the same trade. See below.

The monetary-metals trade is one trade. Silver is a hybrid — roughly half its demand is industrial (solar, electronics) on top of its precious-metal/monetary role — so one might expect the silver miners to carry a silver-specific factor distinct from gold. They do not. Their daily returns are dominated by the gold/silver price (which themselves co-move tightly through the gold/silver ratio), and they are higher-beta versions of the same precious-metals-mining move that drives [[Gold equity beta|the gold miners]]. There is no separable silver-equity factor over the metal, and no separable silver-mining factor over precious-metals mining.

## Cluster validation

### Diagnostics summary

| Diagnostic | Value | Read |
|---|---|---|
| Intra-cluster corr (1Y) | 0.821 [0.716–0.879] | Very tight; weekly 0.837 (synchronous) |
| PC1 explained variance | 85.8% | A near-pure single factor (weekly 87.0%) |
| Independence null p (10k) | 0.0001 | Series co-move |
| Random-basket null p (10k) | 0.0001 | Floor — but a commodity cohort should crush this |
| Vol-matched null p (10k) | 0.0001 | Real beyond shared vol — still trivial for one-price names |
| Holdout (2Y split) | STRENGTHENING 1.11 | train 0.741 → test 0.821 — tightening into the precious-metals bull |
| Threshold clean width | 0.00 | SIL + GDX contaminate from 0.20, SLV from 0.30 — never isolates |
| Intra-adv vs silver complex (SIL/SLV) | +0.008 | ≈zero — the miners are the silver price / silver-miners ETF |
| Intra-adv vs gold miners (GDX) | −0.041 | NEGATIVE — correlate with gold miners more than themselves |
| Intra-adv vs market (SPY) | +0.400 | Not market beta (it is precious-metals beta) |

1Y daily log returns through 2026-06-18, threshold 0.5. All North American listings — synchronous. Config: `scripts/cluster_configs/silver_equity_beta.yaml`; registry row 2026-06-21. Terminology: [[Cohort, cluster, basket]].

### Boundary — never a clean cluster; gold miners join at the tightest cut

![[silver-equity-beta-cluster-dendrogram-1y.png]]
*Hierarchical clustering at 0.5. The five silver miners cluster with [[SIL]] (silver miners ETF), SLV (the metal), AND [[GDX]] (gold miners) — the entire precious-metals-mining complex is one cluster; only SPY stays out.*

The threshold scan returns zero clean width, and the contamination order is the whole story — what the silver miners cannot be distinguished from, tightest-first:

| Threshold | Joins the cohort cluster | Read |
|---|---|---|
| 0.20 | SIL, GDX | The silver-miners ETF AND the gold miners — both at the tightest cut |
| 0.30 | + SLV | The silver price itself joins |
| 0.35–0.50 | (precious-metals complex intact) | One metals-mining cluster |

[[SIL]] and [[GDX]] both joining at 0.20 — the very first threshold — is the most complete ETF-embedding in the campaign, tied with [[Precious metals royalties|royalties]]: the silver miners are inside their own ETF and the gold-miners ETF simultaneously. There is no threshold at which they stand alone.

### Topology — a tight tree, no outlier

Reading the candidate cohort by join distance (average linkage, 1−|corr|):

| Join step | Names | Distance (1-\|corr\|) | Read |
|---|---|---|---|
| 1 | PAAS + AG | 0.121 | the tightest pair (corr 0.88) |
| 2 | HL + CDE | 0.149 | the second pair |
| 3 | (PAAS+AG) + (HL+CDE) | 0.155 | the core fuses |
| 4 | FSM + core | 0.224 | Fortuna joins (its growing gold/West-Africa weighting makes it loosest) |

All five close by 0.224 — an exceptionally tight tree, no satellite. The internal cohesion is real and high; it is the external boundary that fails (gold miners inside from 0.20).

### PC1 index weights

![[silver-equity-beta-cluster-pca-1y.png]]
*PCA scree and PC1 loadings. PC1 explains 85.8% with a tiny tail — a clean single factor, as expected when one (precious-metals) price drives every name. Loadings near-uniform (0.43–0.46).*

| Ticker | PC1 loading | Loading weight | Ann vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| Pan American (PAAS) | 0.457 | 20.4% | 56.0% | 24.1% |
| Hecla (HL) | 0.444 | 19.9% | 72.9% | 18.0% |
| Coeur (CDE) | 0.446 | 20.0% | 72.3% | 18.2% |
| Fortuna (FSM) | 0.427 | 19.1% | 58.7% | 21.5% |
| First Majestic (AG) | 0.461 | 20.6% | 74.5% | 18.2% |

The vols are extreme (56–75% annualized — the highest-beta of the precious-metals cohorts; silver moves more than gold and the miners lever it). But the PC1-mimic basket is just a worse-tracking SIL — the ETF already holds these names.

### Distinctness — it is the precious-metals trade, regardless of metal

![[silver-equity-beta-cluster-correlation-1y.png]]
*1Y pairwise correlation heatmap. The silver-miner block is uniformly warm — but no warmer than its correlation to SIL, SLV, and GDX. There is no silver-equity factor that sits apart from precious-metals mining.*

The intra-advantage numbers make the verdict quantitative: +0.008 versus the silver complex (SIL/SLV), −0.041 versus the gold miners (GDX), +0.400 versus the market. A distinct silver factor would beat both the metal and the gold miners; the silver miners beat neither — they correlate with gold miners marginally more than with each other. So precious-metals mining is one factor: own [[GDX]] for the lower-beta version, [[SIL]] (or the silver names) for the higher-beta version, or SLV/GLD for the unlevered metal. The silver/gold distinction is a beta choice, not a factor choice.

### Historical tightness evolution

![[silver-equity-beta-cluster-rolling-tightness-90d.png]]
*Rolling 90-day cohesion, 2020–2026. Durably tight — 0.69 to 0.87 across the period, tightening to 0.869 in the 2026 precious-metals bull (latest 90-day 0.891). The precious-metals factor is always on; it varies in strength with the metal cycle, not in existence.*

| Year | Avg intra-corr | PC1 |
|---|---|---|
| 2020 | 0.821 | 85.7% |
| 2022 | 0.827 | 86.3% |
| 2023 | 0.709 | 76.9% |
| 2024 | 0.779 | 82.3% |
| 2025 | 0.690 | 75.5% |
| 2026 | 0.869 | 89.6% |

*Durable, tightening in metal bulls (2020-22, 2026) and easing in the lulls (2023, 2025). The holdout STRENGTHENING reading (1.11) reflects the 2025-26 precious-metals surge tightening the group — the same bull-amplification seen in [[Gold equity beta|gold]].*

### The read-through

- The silver miners are one factor, and that factor is precious-metals mining — not even silver-specific. Own [[GDX]]/[[SIL]] for the levered equity beta or SLV/GLD for the metal; a hand-picked silver basket is a higher-beta, worse-tracking SIL. There is no separable silver-equity factor (+0.008 over the metal) and none over gold mining (−0.041 vs GDX).
- Gold and silver mining are one complex. SIL and GDX both contaminate from 0.20 — the gold/silver split is a beta choice (silver higher-beta), not a different trade. This extends the commodity-beta law: single mined metals = their commodity ETF (copper, steel), but the monetary metals (gold, silver, royalties) collapse into one precious-metals-mining complex.
- Highest beta in the family. At 56–75% annualized vol the silver miners are the most volatile precious-metals expression — useful for sizing the same trade, not for diversifying it.

Method and terminology: `docs/cluster-validation.md`, [[Cohort, cluster, basket]], [[Vault cluster taxonomy]]. Post-definition OOS re-validation queued for the next quarterly pass (definition date 2026-06-21).

## Related

- [[Gold equity beta]] — the sibling precious-metals cohort; the silver miners do not separate from it (−0.041 vs GDX) — one complex
- [[Precious metals royalties]] — the capital-light precious-metals sibling; also = gold/GDX (model-agnostic)
- [[Copper equity beta]], [[Lithium equity beta]], [[Uranium equity beta]], [[Steel and aluminum equity beta]] — the commodity-beta family; silver is the highest-beta and the least metal-specific
- [[Pan American Silver]], [[Hecla Mining]], [[Coeur Mining]], [[Fortuna Mining]], [[First Majestic Silver]] — the cohort members
- [[SIL]] — silver-miners ETF; [[Silver]] — the metal (SLV); [[GDX]] — gold miners (the cohort cannot be distinguished from it)
- [[Vault cluster taxonomy]] — cross-cohort comparison
- [[Cohort, cluster, basket]] — terminology

*Created 2026-06-21.*
