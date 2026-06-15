---
aliases: [Copper equity beta, Copper miner cohort, Copper mining cluster, Copper miners factor]
tags: [concept, commodities, metals, mining, cluster-validation]
---

# Copper equity beta

Whether the listed copper miners trade as one factor — and if so, what that factor actually is. The cohort is the six liquid North American copper names: [[Freeport-McMoRan]] (FCX), [[Southern Copper]] (SCCO), [[Teck Resources]] (TECK), [[Ero Copper]] (ERO), [[Ivanhoe Mines]] (IVN.TO), [[First Quantum Minerals]] (FM.TO). The validation answers yes, they cohere — tightly and durably — but the factor binding them is the copper price itself, fully captured by the [[Copper]] commodity and the COPX miners ETF. This is the campaign's first commodity-beta cohort, and it sets the pattern: a commodity cohort's cohesion is real but uninformative.

> [!warning] Cluster status: validated cohesion, but it is the copper price — ETF-replicable (June 2026)
> The six copper miners are a genuinely tight, durable, single-factor cohort: intra-corr 0.707 (weekly 0.771 — synchronous North American listings, so the daily is already clean), PC1 75.8%, and they reject the independence, random-basket and vol-matched nulls all at the 0.0001 floor. But the cohesion is trivial commodity beta and not a distinct factor. The cohort is barely distinct from the copper price itself ([[Copper]]/CPER, +0.033 intra-advantage) and has a negative advantage vs the miner ETFs (COPX/GDX, −0.044) — it correlates more with its own ETF than with itself. It never forms a clean cluster at any threshold: COPX (its own ETF) contaminates from 0.20, BHP from 0.25, the copper price (CPER) from 0.30, gold miners (GDX) from 0.35, and the broad market (SPY) from 0.45. Holdout WEAKENED (0.82 — an extreme 0.867 / PC1 89% in 2024–25, easing to 0.707 in 2025–26). The verdict is the commodity-beta analogue of [[Nuclear renaissance|nuclear/SMR]]: a real cohort that a single ETF (COPX) replicates, with no separable copper-equity factor over the metal. See below.

A commodity cohort coheres trivially, which is exactly why cohesion settles nothing here. Every member is levered to one exogenous price (copper), so they are guaranteed to co-move and to crush the random-basket and vol-matched nulls — that is necessary but uninformative. The only question that carries information is distinctness: does the copper-equity complex trade as something separable from the copper price and the copper ETF? It does not. The miners add a thin operating-leverage premium over the flat metal (+0.033 vs CPER) but are otherwise the copper trade, and at the equity level they bleed into diversified miners ([[BHP]]), gold miners (GDX), and broad risk-on (SPY).

## Cluster validation

### Diagnostics summary

| Diagnostic | Value | Read |
|---|---|---|
| Intra-cluster corr (1Y) | 0.707 [0.529–0.822] | Tight; weekly 0.771 (synchronous, clean) |
| PC1 explained variance | 75.8% | Strong single factor (weekly 81.1%) |
| Independence null p (10k) | 0.0001 | Series co-move |
| Random-basket null p (10k) | 0.0001 | Floor — but a commodity cohort should crush this |
| Vol-matched null p (10k) | 0.0001 | Real beyond shared vol — still trivial for one-price names |
| Holdout (2Y split) | WEAKENED 0.82 | 0.867 (2024–25) → 0.707 (2025–26) |
| Threshold clean width | 0.00 | Never separates from COPX / CPER / GDX / SPY |
| Intra-adv vs copper price (CPER) | +0.033 | Barely an equity premium over the metal |
| Intra-adv vs miner ETFs (COPX/GDX) | −0.044 | Negative — correlates more with its own ETF |
| Intra-adv vs broad (BHP/SPY) | +0.052 | Bleeds into diversified mining + market |

1Y daily log returns through 2026-06-12, threshold 0.5. All members North American (NYSE/TSX) — synchronous, no async caveat. Config: `scripts/cluster_configs/copper_mining.yaml`; registry row 2026-06-14. Terminology: [[Cohort, cluster, basket]].

### Boundary — never a clean cluster, because it is the copper trade

![[copper-cluster-dendrogram-1y.png]]
*Hierarchical clustering at 0.5. The six miners cluster tightly — but so do COPX (the copper-miners ETF), CPER (the copper price), GDX (gold miners), BHP and SPY: everything merges into one cluster. The cohort cannot be isolated from its own ETF or the underlying metal.*

The threshold scan returns zero clean width, but the contamination order is the whole story — what the copper miners cannot be distinguished from, tightest-first:

| Threshold | Joins the cohort cluster | Read |
|---|---|---|
| 0.20 | COPX | The copper-miners ETF — the cohort *is* COPX |
| 0.25 | + BHP | Diversified major — copper-equity beta |
| 0.30 | + CPER | The copper price itself |
| 0.35 | + GDX | Gold miners — generic metals/miner beta |
| 0.45 | + SPY | The broad market — risk-on |

This is the ETF-replicable signature — the same shape as [[Nuclear renaissance|nuclear/SMR]] (URA/NLR) — but stronger: the copper miners are not just replicable by their sector ETF, they are barely separable from the underlying commodity (CPER joins at 0.30) and from gold miners and the market.

### Topology — a tight core, FCX the diversified satellite

| Join step | Names | Distance (1-\|corr\|) | Read |
|---|---|---|---|
| 1 | SCCO + TECK | 0.178 | Tightest pair (corr 0.82) |
| 2 | ERO + FM.TO | 0.211 | Second pair |
| 3 | (SCCO+TECK) + (ERO+FM.TO) | 0.228 | The pure-copper core merges |
| 4 | IVN.TO + core | 0.290 | Ivanhoe joins |
| 5 | FCX + rest | 0.387 | Freeport last — most diversified (gold/moly), loosest member |

The six names form one tight tree (all joined by 0.387, well inside 0.5). [[Freeport-McMoRan]] is the satellite — its gold and molybdenum exposure makes it the loosest member (pairwise 0.53–0.67), while the pure-copper names ([[Southern Copper]], [[Teck Resources]], [[Ero Copper]], [[First Quantum Minerals]]) form the 0.82-tight core. The internal structure is real; it is the external boundary that fails.

### PC1 index weights

![[copper-cluster-pca-1y.png]]
*PCA scree and PC1 loadings. PC1 explains 75.8% with a small tail (PC2 8.3%) — a clean single factor, as expected when one commodity price drives every name. Loadings are near-uniform (0.36–0.43); [[Freeport-McMoRan]] carries the lowest (0.361 — the diversified satellite).*

| Ticker | PC1 loading | Loading weight | Ann vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| Freeport-McMoRan (FCX) | 0.361 | 14.8% | 56.7% | 14.7% |
| Southern Copper (SCCO) | 0.434 | 17.7% | 56.4% | 17.7% |
| Teck Resources (TECK) | 0.416 | 17.0% | 47.6% | 20.2% |
| Ero Copper (ERO) | 0.416 | 17.0% | 65.5% | 14.7% |
| Ivanhoe Mines (IVN.TO) | 0.392 | 16.0% | 61.7% | 14.7% |
| First Quantum (FM.TO) | 0.426 | 17.4% | 54.3% | 18.1% |

The lower-vol [[Teck Resources]] takes the largest raw PC1-mimic weight (20.2%) — it needs more notional to reproduce the standardized copper-price shock. But the practical point is that the PC1-mimic basket is just a worse-tracking COPX: the ETF already holds these names at scale and capitalization weight.

### Distinctness — it is the copper price

![[copper-cluster-correlation-1y.png]]
*1Y pairwise correlation heatmap. The miner block is uniformly warm — but no warmer than the block's correlation to CPER (the copper price) and COPX (the miners ETF). There is no copper-equity factor that sits apart from the metal.*

The intra-advantage numbers make the verdict quantitative: +0.033 vs the copper price (CPER), −0.044 vs the miner ETFs (COPX/GDX), +0.052 vs diversified mining and the market (BHP/SPY). A copper-equity factor distinct from copper would show a clearly positive advantage vs CPER; +0.033 says the miners are levered copper and almost nothing else. The thin positive premium is operating leverage and jurisdiction risk (Grasberg, Cobre Panamá, DRC), which is idiosyncratic single-name noise, not a shared separable factor.

### Historical tightness evolution

![[copper-cluster-rolling-tightness-90d.png]]
*Rolling 90-day cohesion, 2021–2026. Durably tight — 0.53 to 0.74 across the period, dipping only in the 2024 macro lull and re-tightening to 0.785 latest. The copper-price factor is always on; it varies in strength with the commodity cycle, not in existence.*

| Window | Avg intra-corr | PC1 | Final join distance |
|---|---|---|---|
| 2022 | 0.693 | 74.7% | 0.368 |
| 2024 | 0.531 | 62.7% | 0.688 |
| 2025 | 0.736 | 78.4% | 0.405 |
| 2026 | 0.734 | 77.9% | 0.383 |

*Durable, not regime-dependent in existence: the cohort is a real cluster in every year, tightening and loosening with the copper cycle. The holdout WEAKENED reading (0.82) reflects the 2024–25 half being exceptionally tight (0.867) rather than the cohort breaking — the factor persists, it merely normalized off a peak.*

### The read-through

- The copper miners are one factor, and that factor is copper. Own COPX for the levered equity beta or CPER for the unlevered metal; a hand-picked basket of single names is a worse-tracking COPX. There is no separable copper-equity factor to harvest (+0.033 over the price).
- Cohesion proves nothing for a commodity cohort. Passing the random-basket and vol-matched nulls at the floor is guaranteed when every member is levered to one exogenous price — the meaningful tests are the threshold scan (it bleeds into COPX/CPER/GDX/SPY) and the intra-advantage vs the metal (negligible).
- Single-name selection is idiosyncrasy, not factor. The only reasons to pick [[Southern Copper]] over [[First Quantum Minerals]] are cost curve, jurisdiction, and growth (Cobre Panamá, Kamoa-Kakula, Grasberg) — operating-leverage and political risk on top of the same copper beta, not a different trade.
- It bleeds into the broader metals/risk complex. Distinct neither from gold miners (GDX, joins at 0.35) nor the market (SPY, 0.45) — in a commodity/risk-on regime, copper miners are a high-beta expression of the same move.

Method and terminology: `docs/cluster-validation.md`, [[Cohort, cluster, basket]], [[Vault cluster taxonomy]]. Post-definition OOS re-validation queued for the next quarterly pass (definition date 2026-06-14).

## Related

- [[Sectors/Copper Mining]] — the sector hub (producers, supply/demand, geography); this note is the cluster-validation companion
- [[Copper]] — the commodity (price, CPER, forecasts) the cohort cannot be distinguished from
- [[Copper for AI]] — the demand thesis
- [[Freeport-McMoRan]], [[Southern Copper]], [[Teck Resources]], [[Ero Copper]], [[Ivanhoe Mines]], [[First Quantum Minerals]] — the cohort members
- [[BHP]] — diversified major (control); the copper miners are not distinct from it
- [[Nuclear renaissance]] — the other validated-but-ETF-replicable cohort (same shape, commodity vs theme)
- [[Gold equity beta]] — the sibling commodity-beta cohort; gold replicates this note's law (real, ETF-replicable, = the metal) but is tighter and bull-strengthening where copper weakened
- [[Vault cluster taxonomy]] — cross-cohort comparison
- [[Cohort, cluster, basket]] — terminology

*Created 2026-06-14.*
