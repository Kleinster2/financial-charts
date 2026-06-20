---
aliases: [Rare earth equity beta, Rare earth miner cohort, Rare earth mining cluster, Rare earth equities, Critical minerals equity beta]
tags: [concept, commodities, metals, mining, rare-earths, critical-minerals, cluster-validation]
---

# Rare earth equity beta

Whether the listed rare-earth and [[Critical minerals|critical-mineral]] miners trade as one factor — and if so, what that factor actually is. The cohort is six liquid names spanning the Western rare-earth/magnet supply chain: [[MP Materials]] (MP), [[Lynas Rare Earths]] (LYC.AX), [[USA Rare Earth]] (USAR), [[Energy Fuels]] (UUUU), [[NioCorp Developments]] (NB), [[Critical Metals Corp]] (CRML). It is the sixth commodity-equity-beta cohort (after [[Copper equity beta|copper]], [[Gold equity beta|gold]], [[Lithium equity beta|lithium]], [[Uranium equity beta|uranium]], and [[Steel and aluminum equity beta|steel & aluminum]]) and the family's most extreme "no investable metal" case: rare earths have no spot price and no futures — pricing is opaque and [[China]]-controlled — so the equity complex plus the diluted [[REMX]] strategic-metals ETF is the only rare-earth exposure that exists. The validation returns a more interesting answer than the others: the names do cohere in the 1Y window, but the factor binding them was born in the 2025-26 [[China]] export-control shock, never forms a clean cluster, is captured by [[REMX]], and excludes [[Lynas Rare Earths|Lynas]] entirely. A shock-manufactured, ETF-replicable cohesion — not a distinct or durable factor.

> [!warning] Cluster status: validated cohesion, but it is a shock-born, ETF-replicable trade — not a distinct or durable factor (June 2026)
> The six rare-earth/critical-mineral names cohere in the 1Y window (intra-corr 0.511, PC1 63.2%) and reject the independence, random-basket and vol-matched nulls (0.0001 / 0.0003 / 0.0001) — so the co-movement is real, not shared high-vol noise. But three diagnostics deny it distinctness or durability. (1) Shock-born: the 2Y holdout splits train intra 0.120 (PC1 29.5%, some pairs negative) -> test 0.507 (PC1 62.8%), with a PC1-loadings correlation of only 0.35 — the older half had no factor at all; this one was manufactured by the 2025-26 [[China]] heavy-REE/magnet export controls and the [[MP Materials]]/Pentagon deal. The 90-day rolling cohesion tells the same story: 0.064 (2024) -> 0.229 (2025) -> 0.538 (2026). (2) ETF-replicable: a NEGATIVE intra-advantage versus both [[REMX]] (−0.016, the strategic-metals ETF) and [[XME]] (−0.049, broad mining) — the names track those ETFs as much as each other, and both sit inside the cluster; threshold stable width 0.00 (a falsification candidate as a clean cluster). (3) A geographic split: [[Lynas Rare Earths|LYC.AX]], the largest ex-[[China]] producer, is near-orthogonal to the five US names (pairwise 0.13–0.23, PC1 loading 0.131, joins only at 0.836) — even after the weekly async-close correction. Own [[REMX]] for the strategic-metals shock; there is no durable, separable rare-earth-equity factor. See below.

A shock-dependent cohort, not a structural one. The other commodity cohorts are durable: copper, gold and uranium are a real cluster in every year, tightening and loosening with the commodity cycle but always present. Rare earths are different — before 2026 the names were essentially uncorrelated single-stock development stories ([[MP Materials|MP]]'s Mountain Pass ramp, [[Lynas Rare Earths|Lynas]]'s Malaysia/Kalgoorlie build, [[NioCorp Developments|NioCorp]]'s Elk Creek financing, each on its own timeline). The 2025-26 weaponization of rare earths by [[China]] — heavy-REE and magnet export licensing, then the US response (the [[MP Materials]] DoD price-floor and equity deal, July 2025) — synchronized them into one "Western rare-earth independence" trade. That is a specific shared exogenous driver, which the campaign's [[Vault cluster taxonomy|regime-dependence law]] says CAN be distinctness; but here it fails the distinctness test anyway, because the liquid [[REMX]] ETF already holds exactly these names and prices the same shock.

## Cluster validation

### Diagnostics summary

| Diagnostic | Value | Read |
|---|---|---|
| Intra-cluster corr (1Y) | 0.511 [0.131–0.766] | At the floor; weekly 0.564 (higher — the async-close correction for Lynas) |
| PC1 explained variance | 63.2% | One factor in the window (weekly 64.7%) — but a recent one |
| Independence null p (10k) | 0.0001 | Series co-move |
| Random-basket null p (10k) | 0.0003 | Beats a random 6-pick (null mean 0.150) — but via the shock |
| Vol-matched null p (10k) | 0.0001 | Real beyond shared vol (null mean 0.216) — these are 66–170% vol names |
| Holdout (2Y split) | factor BIRTH | train 0.120 (PC1 29.5%) -> test 0.507 (PC1 62.8%); loadings corr 0.35 |
| Threshold clean width | 0.00 | Falsification candidate — never a clean 6-name cluster; REMX/XME contaminate |
| Intra-adv vs strategic-metals ETF (REMX) | −0.016 | Negative — correlates with REMX as much as itself |
| Intra-adv vs broad mining (XME) | −0.049 | Negative — bleeds into general metals/mining |
| Intra-adv vs market (SPY) | +0.214 | Distinct from the market, but that is only "not market beta" |

1Y daily log returns through 2026-06-18, threshold 0.5. [[Lynas Rare Earths|Lynas]] (LYC.AX) is ASX-native — async close, so its daily correlations understate and the weekly cross-check is the fair read. USAR/CRML are 2024-25 listings, so the 2Y holdout is history-limited. Config: `scripts/cluster_configs/rare_earth_equity_beta.yaml`; registry row 2026-06-20. Terminology: [[Cohort, cluster, basket]].

### Boundary — never a clean cluster; the US core, then the ETFs, then Lynas alone

![[rare-earth-equity-beta-cluster-dendrogram-1y.png]]
*Hierarchical clustering at 0.5. The five US names ([[MP Materials|MP]], [[USA Rare Earth|USAR]], [[Energy Fuels|UUUU]], [[NioCorp Developments|NB]], [[Critical Metals Corp|CRML]]) cluster with [[REMX]] and [[XME]] — the strategic-metals and mining ETFs sit inside the cohort. [[Lynas Rare Earths|LYC.AX]] is its own singleton, and SPY is separate. The full six-name cohort never forms one cluster.*

The threshold scan returns zero clean width — but the assignment table is the whole story. The five US names form an uncontaminated cluster only in a narrow 0.35–0.40 band; the ETFs join just above it, and Lynas never joins:

| Threshold | State | Read |
|---|---|---|
| 0.20–0.30 | the cohort is fragments (6 -> 4 subclusters) | even the US names are still partly singletons |
| 0.35–0.40 | US-5 form one clean cluster (Lynas out, no ETF) | the only window the core isolates — width ~0.05 |
| 0.45 | + [[REMX]], [[XME]] join | the strategic-metals and mining ETFs contaminate |
| 0.50–0.70 | ETFs embedded; Lynas still apart | ETF-replicable; never an intact 6-name cluster |

This is the copper-pattern signature (the ETF inside the cluster) with the added defect that the cohort is never intact as defined: [[Lynas Rare Earths|Lynas]] is a permanent outlier, so the threshold scan flags the six-name cohort a falsification candidate.

### Topology — a US core that closes late, Lynas a far outlier

| Join step | Names | Distance (1-\|corr\|) | Read |
|---|---|---|---|
| 1 | MP + USAR | 0.234 | the US producer/magnet pair (corr 0.77) |
| 2 | NB + (MP+USAR) | 0.294 | NioCorp joins |
| 3 | UUUU + core | 0.335 | Energy Fuels joins |
| 4 | CRML + core | 0.348 | the US-5 core closes |
| 5 | LYC.AX + core | 0.836 | Lynas joins only at the very end — the geographic outlier |

The US-5 core closes at 0.348 — looser than copper's 0.387-for-six but a real cluster — while [[Lynas Rare Earths|Lynas]] joins at 0.836, essentially unconnected. The US names share a single domestic driver (US strategic-minerals policy, DoD/DoE financing, tariff walls); Lynas, the established ex-China producer, trades on Malaysian/Australian operations, ASX flows, and a different investor base. PC1 explains 63.2% with a sizeable PC2 (16.0%) — the Lynas-vs-US axis.

### PC1 index weights — Lynas barely loads

![[rare-earth-equity-beta-cluster-pca-1y.png]]
*PCA scree and PC1 loadings. PC1 explains 63.2% with a large PC2 (16.0%, the Lynas axis). The five US names load 0.43–0.46; [[Lynas Rare Earths|Lynas]] loads 0.131 — it scarcely participates in the common factor.*

| Ticker | PC1 loading | Loading weight | Ann vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| MP Materials (MP) | 0.463 | 19.7% | 80.8% | 25.2% |
| Lynas (LYC.AX) | 0.131 | 5.6% | 59.8% | 9.6% |
| USA Rare Earth (USAR) | 0.459 | 19.5% | 122.0% | 16.5% |
| Energy Fuels (UUUU) | 0.432 | 18.4% | 99.3% | 19.1% |
| NioCorp (NB) | 0.436 | 18.6% | 108.6% | 17.7% |
| Critical Metals (CRML) | 0.426 | 18.2% | 158.7% | 11.8% |

The vols are extreme (60–159% annualized — these are small-cap, pre/early-production miners), which is exactly why the vol-matched null matters: the cohesion survives it, so it is not merely shared high-beta noise. [[MP Materials|MP]] — the only real US producer and the policy anchor — carries the top raw weight (25.2%); [[Lynas Rare Earths|Lynas]]'s tiny loading (and 9.6% weight) confirms it is barely in the factor.

### Distinctness — a shock the strategic-metals ETF already prices

![[rare-earth-equity-beta-cluster-correlation-1y.png]]
*1Y pairwise correlation heatmap. A warm US-5 block (0.61–0.77, warmest at MP/USAR) — but no warmer than that block's correlation to REMX and XME — and a cold [[Lynas Rare Earths|Lynas]] row/column (0.13–0.23 against everything). There is no rare-earth-equity factor that sits apart from the strategic-metals ETF.*

The intra-advantage numbers make the verdict quantitative: −0.016 versus [[REMX]] (the strategic-metals ETF), −0.049 versus [[XME]] (broad mining), +0.214 versus the market (SPY). A distinct rare-earth factor would show a clearly positive advantage versus REMX; −0.016 says the names are the strategic-metals ETF, which holds the exact constituents (the Western producers plus the Chinese majors and lithium names). The only positive number is versus SPY — the cohort is not the broad market — but "not market beta" is not distinctness. The specific China-weaponization driver is real, but [[REMX]] prices it directly.

### Historical tightness evolution — the factor was born in 2026

![[rare-earth-equity-beta-cluster-rolling-tightness-90d.png]]
*Rolling 90-day cohesion, 2024–2026. The opposite of copper's always-on factor: near-zero in 2024 (0.064, core corr −0.003), rising in 2025 (0.229), and only becoming a real cluster in 2026 (0.538) as the China export-control/Pentagon shock synchronized the names. The factor has a birthday.*

| Window | Avg intra-corr | PC1 | Core corr | Final join distance |
|---|---|---|---|---|
| 2024 | 0.064 | 26.4% | −0.003 | 0.909 |
| 2025 | 0.229 | 37.3% | 0.164 | 0.881 |
| 2026 | 0.538 | 66.4% | 0.486 | 0.851 |

*Regime-dependent in existence, not merely in strength. Copper's holdout WEAKENED reading meant a real factor normalizing off a peak; rare earths' holdout reads a 4.21 "strengthening" ratio that is actually factor birth — train intra 0.120 with a PC1-loadings correlation of only 0.35 versus the test half (the structures barely match). Even the US core was anti-correlated-to-flat (−0.003) in 2024. This is a trade that exists while the China shock is live, not a structural cohort.*

### The read-through

- The rare-earth equities are one trade only during the China shock — and that trade is [[REMX]]. Own the strategic-metals ETF for the Western-supply-independence theme; a hand-picked basket adds nothing (−0.016 intra-advantage) and inherits the same shock-dependence. There is no durable, separable rare-earth-equity factor.
- Cohesion here proves even less than for copper. Passing the nulls confirms the names co-move in the window, but the holdout shows the co-movement did not exist before 2026 — necessary, and not even durable, let alone distinct.
- Lynas is a different security. [[Lynas Rare Earths|LYC.AX]] is the one established ex-China producer, and it is near-orthogonal to the US names — a geographic/operational split (US policy beta vs Australian-Malaysian operations), the rare-earth analogue of how casinos split by jurisdiction.
- Single-name selection is idiosyncrasy on top of the shock. The reasons to pick [[MP Materials|MP]] (the only producer, DoD-backed) over [[Critical Metals Corp|CRML]] (Greenland development, 159% vol) are stage, jurisdiction, and balance sheet — single-stock risk, not a different factor.

Method and terminology: `docs/cluster-validation.md`, [[Cohort, cluster, basket]], [[Vault cluster taxonomy]]. Post-definition OOS re-validation queued for the next quarterly pass (definition date 2026-06-20).

## Related

- [[Rare earths]] — the commodity/geopolitics note (China dominance, reserves, diversification); this is its cluster-validation companion
- [[Rare earth leverage]] — China's dominance as a geopolitical weapon (the driver behind the 2026 shock)
- [[Critical minerals]] — the broader category (niobium, scandium, gallium, antimony) several members also touch
- [[MP Materials]], [[Lynas Rare Earths]], [[USA Rare Earth]], [[Energy Fuels]], [[NioCorp Developments]], [[Critical Metals Corp]] — the cohort members
- [[REMX]] — the strategic-metals ETF the cohort cannot be distinguished from
- [[XME]] — broad metals & mining control; the names bleed into it
- [[Copper equity beta]], [[Gold equity beta]], [[Lithium equity beta]], [[Uranium equity beta]], [[Steel and aluminum equity beta]] — the sibling commodity-beta cohorts; rare earths is the only shock-born one (no durable factor, no investable metal)
- [[China]] — dominant supplier/processor; the source of the 2025-26 export-control shock
- [[Vault cluster taxonomy]] — cross-cohort comparison
- [[Cohort, cluster, basket]] — terminology

*Created 2026-06-20. 1Y daily log returns through 2026-06-18; config `scripts/cluster_configs/rare_earth_equity_beta.yaml`; registry row 2026-06-20. Cluster validation is structure, not a performance ranking — see `docs/cluster-validation.md`.*
