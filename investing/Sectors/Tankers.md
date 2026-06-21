---
aliases: [Tankers, Tanker equities, Crude tankers, Tanker cohort, Tanker stocks, Tanker cluster]
tags: [sector, industrials, shipping, tankers, cluster-validation]
---

# Tankers

> [!success] Cluster status: VALIDATED — a distinct, very tight tanker-equity factor; no liquid equity ETF prices it (Jun 2026)
> The listed crude/product tanker owners ([[Frontline|FRO]]/[[Scorpio Tankers|STNG]]/[[International Seaways|INSW]]/[[DHT Holdings|DHT]]/[[Teekay Tankers|TNK]]) trade as one of the campaign's tightest factors — intra-corr 0.795, PC1 83.7% — rejecting the random-basket and vol-matched nulls at the 0.0001 floor, with a STABLE 2Y holdout (ratio 0.95). The decisive distinctness number is a +0.483 intra-advantage versus the ETF group ([[BOAT]]/[[SEA]]/[[XLE]]/SPY) — the second-largest in the whole campaign behind [[Drug distributors]] (+0.502) — and a clean, contamination-free cluster across thresholds 0.30–0.45 (stable width 0.15, WIDE). The broad-shipping ETFs [[BOAT]]/[[SEA]] absorb the basket only at the looser 0.50 cut, because they hold tankers diluted with dry bulk, container, and LNG; the pure crude/product-tanker basket is tighter and separates below 0.45. Crucially, the only direct public tanker instrument, [[BWET]], is a freight-futures commodity pool that prices the rate itself, not the equities — so no liquid equity ETF replicates this factor. This is the eighth genuinely distinct non-ETF factor in the campaign, and by robustness it ranks near the very top (tighter than every Tier-1 cohort except [[Residential REITs]]).

The freight-rate pure-play, in equity form. Crude and product tanker owners are levered operating plays on the seaborne-oil freight cycle: their earnings are spot-rate (TD3C VLCC, Suezmax, MR product) times a fleet they own, so when rates spike the equities move as one. That shared driver — the tanker spot rate — is now directly nameable and even separately tradeable via the [[BWET]] freight-futures ETF, which lets this cohort make the campaign's law unusually concrete: the driver is a commodity, and the equity basket is a distinct, levered factor expressing it that no equity ETF isolates. [[BOAT]] and [[SEA]] are the nearest equity proxies, but they blend tankers with dry bulk, containerships, and LNG carriers — different rate cycles — so the pure-tanker basket out-coheres them and separates at tighter thresholds.

## Sector performance

![[tankers-performance.png]]
*Normalized total return since Jan 2023, the five tankers vs the broad-shipping ETF [[BOAT]]. The cohort moves as one and on its own tanker-rate cycle, visibly decoupled from BOAT (diluted with dry-bulk/container/LNG) — the +0.483 distinctness made visible.*

## Cluster validation

The candidate cohort is five US-listed crude/product tanker owners — [[Frontline|FRO]], [[Scorpio Tankers|STNG]], [[International Seaways|INSW]], [[DHT Holdings|DHT]], [[Teekay Tankers|TNK]] — tested against the broad-shipping ETFs ([[BOAT]]/[[SEA]]), energy ([[XLE]]), and market (SPY). 1Y window through 2026-06-18, threshold 0.5. Terminology: [[Cohort, cluster, basket]].

### Diagnostics summary

| Diagnostic | Value | Read |
|---|---|---|
| Intra-cluster corr (1Y) | 0.795 [0.692–0.888] | among the campaign's tightest; weekly 0.789 (async-close robust) |
| PC1 explained variance | 83.7% | a dominant single factor (weekly 83.2%) |
| Independence null p | 0.0001 | series co-move |
| Random-basket null p | 0.0001 | far beyond a random 5-pick (null mean 0.163, 99th 0.389) |
| Vol-matched null p | 0.0001 / 0.0001 | cohesion exceeds vol-matched baskets (null mean 0.170) — not just shared vol/beta |
| Holdout (2Y split) | STABLE 0.95 | train 0.833 → test 0.795; PC1 loadings corr 0.93 (same factor) |
| Threshold stable width | 0.15 [0.30–0.45] | WIDE; a clean cluster below the BOAT/SEA-contamination cut |
| Intra-adv vs ETFs (BOAT/SEA/XLE/SPY) | +0.483 | 2nd-largest in the campaign; no liquid equity ETF prices the factor |

All US-listed. Config: `scripts/cluster_configs/fro.yaml`; registry row 2026-06-20.

### Boundary — tankers separate from broad-shipping ETFs below 0.45; energy/market apart throughout

![[tankers-cluster-dendrogram-1y.png]]
*Hierarchical clustering at 0.5. At this cut the five tankers absorb the broad-shipping ETFs [[BOAT]]/[[SEA]] (Cluster 1), because those ETFs are partly tanker; energy [[XLE]] and the market (SPY) form their own separate clusters throughout. The threshold scan shows the five tankers form a clean cluster WITHOUT BOAT/SEA across 0.30–0.45 (stable width 0.15). That tankers never join XLE or SPY is the key negative: this is not energy beta or market beta.*

The threshold scan returns the cohort as a clean, contamination-free cluster across [0.30–0.45] (stable width 0.15, WIDE — matching [[Trucking and LTL|trucking]] and [[Solid waste|waste]]); [[BOAT]]/[[SEA]] join only at the 0.50 cut and above, never XLE or SPY. Combined with the +0.483 intra-advantage over the ETF group and a STABLE 0.95 holdout, this is a VALIDATED, distinct factor. The structural parallel is [[Solid waste]] (whose ETF EVX is diluted by smaller environmental names): the only tradeable proxies are diluted, so the concentrated basket strictly out-coheres them — except here the dilution is by other shipping segments rather than by smaller peers.

### Topology — a crude core (two pairs) and the product-tanker name joining last

Reading the candidate cohort by join distance (average linkage, 1−|corr|):

| Join step | Names | Distance (1-\|corr\|) | Read |
|---|---|---|---|
| 1 | INSW + TNK | 0.112 | the tightest pair — crude/product mid-size, spot-heavy |
| 2 | FRO + DHT | 0.154 | the VLCC crude pair |
| 3 | (INSW+TNK) + (FRO+DHT) | 0.190 | the crude/mixed core fuses |
| 4 | STNG + core | 0.255 | the product-tanker name joins last |

The cohort is a crude core that closes very tight — INSW+TNK at 0.112 and FRO+DHT at 0.154 fuse at 0.190 — with [[Scorpio Tankers|STNG]] joining last at 0.255. STNG is the product-tanker (clean/refined) name, and clean-product freight rates run on a partly different cycle from dirty-crude rates, so it is the most differentiated member while still well inside the cluster. PC1 explains 83.7% with a tiny PC2 (7.1%) — a near-pure single factor.

### PC1 index weights — a flat, balanced factor

![[tankers-cluster-pca-1y.png]]
*PCA on the candidate cohort. PC1 explains 83.7% (weekly 83.2%) with near-equal loadings (0.42–0.46) — the signature of a single common driver rather than one name carrying the factor.*

| Ticker | PC1 loading | Loading weight | Ann vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| FRO | 0.447 | 20.0% | 42.0% | 17.8% |
| STNG | 0.424 | 19.0% | 37.8% | 18.7% |
| INSW | 0.462 | 20.7% | 36.2% | 21.3% |
| DHT | 0.443 | 19.8% | 34.2% | 21.6% |
| TNK | 0.458 | 20.5% | 37.2% | 20.5% |

Loadings are flat (0.42–0.46): no single name dominates the factor. On a vol-adjusted (inverse-volatility) PC1-mimic, the highest-vol name [[Frontline|FRO]] (42% annualized) gets the smallest raw weight (17.8%) and the steadier [[DHT Holdings|DHT]]/[[International Seaways|INSW]] the largest (~21.5%) — the index re-weights toward the lower-vol expressions of the same factor.

### Distinctness — the driver is a commodity ([[BWET]]); the equity basket is the distinct factor

![[tankers-cluster-correlation-1y.png]]
*1Y pairwise correlation heatmap. A uniformly warm five-name block (0.69–0.89), warmest at INSW/TNK and FRO/DHT; the ETFs cooler against it, energy ([[XLE]]) and the market cooler still.*

The intra-advantage versus the ETF group is +0.483 — second only to [[Drug distributors]] in the entire campaign. The nuance that makes tankers an unusually clean illustration of the campaign's law: the shared driver is directly identifiable and itself tradeable. [[BWET]] (Breakwave Tanker Shipping ETF) is a commodity pool holding near-dated tanker freight futures (TD3C VLCC, TD20 Suezmax) — it prices the freight rate itself, and it did +836% in the [[2026 Strait of Hormuz crisis]] when [[Baltic Exchange]] TD3C printed all-time highs. But BWET is the commodity, not the equities: the listed owners are levered operating plays on that rate, carrying balance-sheet leverage, fleet/NAV, spot-vs-charter mix, dividend policy, and equity-market beta that an FFA lacks (the BWET note records BWET rising 7% to an all-time high on a day oil fell 14% — the equities do not behave that way). So the rate has a liquid instrument; the equity factor does not. [[BOAT]]/[[SEA]] are equity ETFs but broad-shipping, diluting tankers with dry bulk, container, and LNG. Own the basket for the distinct tanker-equity factor; own [[BWET]] for the rate (with its commodity-pool mean-reversion and 3.50% carry); the two are different exposures.

### Historical tightness evolution — persistent across six years

![[tankers-cluster-rolling-tightness-90d.png]]
*Rolling 90-day cohesion, 2020–2026. Consistently high (0.69–0.82), loosest in 2022 and tightest in 2025–26; the factor has been durable across the COVID demand shock, the 2022 rate divergence, and the 2026 Hormuz spike.*

| Year | Avg intra-corr | PC1 |
|---|---|---|
| 2020 | 0.791 | 83.3% |
| 2021 | 0.733 | 78.7% |
| 2022 | 0.692 | 75.6% |
| 2023 | 0.732 | 78.7% |
| 2024 | 0.722 | 77.9% |
| 2025 | 0.818 | 85.4% |
| 2026 | 0.810 | 84.8% |

Latest 90-day reading: intra 0.804, PC1 84.4% (core 0.821, satellite 0.780). Cohesion dipped to 0.692 in 2022 — when product-tanker (clean) and crude (dirty) rate cycles diverged on the post-invasion refined-product rerouting — and re-tightened to 0.82 in 2025 and through the 2026 Hormuz spike, when every crude-tanker name moved on the same TD3C signal. The holdout is STABLE (0.95) and the PC1 loading structure is preserved across the split (loadings corr 0.93): a durable factor, not a one-window artifact.

## Related

- [[BWET]] — the tanker freight-rate instrument (FFA commodity pool); the driver, not the equity factor
- [[BOAT]], [[SEA]] — the broad-shipping equity ETFs the cohort out-coheres and separates from
- [[Frontline]], [[Scorpio Tankers]], [[International Seaways]], [[DHT Holdings]], [[Teekay Tankers]] — the cohort members
- [[XLE]] — energy ETF; tankers never cluster with it (not energy beta)
- [[Shipping]] — sector hub
- [[Baltic Exchange]], [[VLCC]] — the freight-rate index and dominant vessel class driving the factor
- [[2026 Strait of Hormuz crisis]], [[Hormuz Permanent Risk Premium]] — the recent rate-spike episode the cohort moved on
- [[Drug distributors]], [[Solid waste]], [[Residential REITs]], [[Trucking and LTL]] — the comparable Tier-1 distinct factors (tankers ranks near the top by robustness)
- [[Vault cluster taxonomy]] — cross-cohort meta-analysis
- [[Cohort, cluster, basket]] — terminology

---

*Created 2026-06-20. 1Y daily log returns through 2026-06-18; config `scripts/cluster_configs/fro.yaml`; registry row 2026-06-20. Cluster validation is structure, not a performance ranking — see `docs/cluster-validation.md`.*
