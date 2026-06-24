---
aliases: [Coal miners, Coal mining, Coal producers, Coal, Met coal, Thermal coal]
tags: [sector, energy, materials, coal, mining, cluster-validation]
---

# Coal miners

> [!success] Cluster status: VALIDATED — a distinct coal-mining factor (BTU/AMR/HCC/METC/CNR); no liquid ETF replicates it (KOL was liquidated in 2020), so coal is the commodity-beta map's exception — ownable only as a basket, the [[Tankers|tankers pattern]] (Jun 2026)
> The US coal miners cohere as their own factor (6-name intra 0.563, ex-decoupler core 0.642, PC1 65%) and beat the random-basket null at p 0.00025, with a STABLE 0.95 holdout (durable since 2021). They are distinct from every available proxy: +0.115 (core +0.148) intra-advantage vs metals/mining [[XME]], +0.324 (core +0.419) vs energy [[XLE]], +0.381 vs steel [[Nucor|NUE]], +0.531 vs natural gas [[UNG]], and +0.463 vs the market. The key fact is structural scarcity: unlike every other mined commodity in the campaign — copper, gold, silver, lithium, uranium, steel, all of which resolve to a commodity ETF — coal has no listed ETF (VanEck's KOL was liquidated in 2020), so the cohort cannot collapse into one and stands as a distinct, basket-only factor. [[Alliance Resource Partners|ARLP]] (a thermal-coal MLP) is the decoupler; the met-coal core ([[Alpha Metallurgical Resources|AMR]]/[[Warrior Met Coal|HCC]]) and the diversified majors ([[Peabody Energy|BTU]]/[[Core Natural Resources|CNR]]) anchor the factor. Own the basket. See below.

The orphaned commodity. Coal is mined like the metals and burned like the fossil fuels, but it trades as neither: the seaborne coking-coal price (steel demand) and the thermal-coal price (power demand, with an AI-data-center-electricity tailwind) drive the miners together in a way that no broad ETF captures, because the dedicated vehicle that once did — VanEck's KOL coal ETF — was shut in 2020 at the nadir of ESG-driven divestment. The listed survivors ([[Peabody Energy|BTU]], [[Alpha Metallurgical Resources|AMR]], [[Warrior Met Coal|HCC]], [[Ramaco|METC]], [[Core Natural Resources|CNR]], [[Alliance Resource Partners|ARLP]]) are leaner, cash-generative, and co-move on coal-specific demand — so the basket is a real, distinct factor that can only be owned name-by-name.

## Sector performance

![[coal-performance.png]]
*Normalized total return since 2021 vs the metals/mining ETF [[XME]] (the closest available proxy — there is no coal ETF). The coal names move together on coal-specific demand and diverge from [[XME]]; the absence of any ETF that tracks them is exactly why the basket is a distinct factor rather than a collapse.*

## Cluster validation

The candidate cohort is the six listed US coal miners — [[Peabody Energy|BTU]], [[Alpha Metallurgical Resources|AMR]], [[Warrior Met Coal|HCC]], [[Alliance Resource Partners|ARLP]], [[Ramaco|METC]], [[Core Natural Resources|CNR]] — tested against steel ([[Nucor|NUE]], the met-coal demand link), natural gas ([[UNG]], the thermal competitor), metals/mining ([[XME]]), energy ([[XLE]]), and the market ([[SPY]]). 1Y window through 2026-06-22 (250 obs); threshold 0.5. No coal ETF exists (KOL liquidated 2020). Tickers ingested 2026-06-24 (ARCH/CEIX retired into [[Core Natural Resources|CNR]]). Config: `scripts/cluster_configs/coal.yaml`; registry row 2026-06-24. Terminology: [[Cohort, cluster, basket]].

### Diagnostics summary

| Diagnostic | Value | Read |
|---|---|---|
| Intra-corr (1Y) | 0.563 (6-name) / 0.642 (ex-ARLP core) | A real factor; [[Alliance Resource Partners\|ARLP]] the drag |
| PC1 explained variance | 64.7% | One coal factor |
| Random-basket null p | 0.00025 | Real — 0.56 vs random 6-pick mean 0.17 |
| Holdout (2Y split) | STABLE 0.95, loadings-corr 0.89 | Durable, stable structure |
| Threshold stable width | 0.10 [0.60–0.70] | Clean cohort; closest proxies stay out |
| Intra-adv vs metals/mining ([[XME]]) | +0.115 / +0.148 | Distinct from broad mining |
| Intra-adv vs energy ([[XLE]]) | +0.324 / +0.419 | Distinct from broad energy |
| Intra-adv vs steel ([[Nucor\|NUE]]) | +0.381 / +0.456 | Not just met-coal-to-steel beta |
| Intra-adv vs nat gas ([[UNG]]) | +0.531 | Thermal coal ≠ gas |
| Intra-adv vs market (SPY) | +0.463 / +0.527 | Strongly idiosyncratic |

### Boundary — coal forms its own cluster, every proxy stays out

![[coal-cluster-dendrogram-1y.png]]
*Hierarchical clustering at 0.5. The coal core [[Peabody Energy|BTU]]/[[Alpha Metallurgical Resources|AMR]]/[[Warrior Met Coal|HCC]]/[[Ramaco|METC]]/[[Core Natural Resources|CNR]] forms its own cluster; [[Alliance Resource Partners|ARLP]] (thermal MLP), [[Nucor|NUE]] (steel), [[UNG]] (gas), [[XLE]] (energy) are each singletons, and [[XME]] tracks the market. No proxy joins the coal cluster — the basket is its own factor.*

The threshold scan returns a stable band [0.60–0.70] where the cohort is a clean, uncontaminated cluster, and every control carries a positive intra-advantage. With no coal ETF in existence, there is nothing for the cohort to collapse into — the structural opposite of the same-week [[Infrastructure construction|buildout contractors]] (= PAVE) or [[Factory automation|automation]] (= XLI).

### Topology — a diversified pair and a met-coal pair

Reading the candidate cohort by join distance (average linkage, 1−|corr|):

| Join step | Names | Distance (1-\|corr\|) | Read |
|---|---|---|---|
| 1 | BTU + CNR | 0.195 | the diversified majors ([[Peabody Energy\|BTU]] + [[Core Natural Resources\|CNR]], corr 0.81) |
| 2 | AMR + HCC | 0.255 | the pure met-coal pair ([[Alpha Metallurgical Resources\|AMR]] + [[Warrior Met Coal\|HCC]], corr 0.75) |
| 3 | (BTU+CNR) + (AMR+HCC) | 0.294 | diversified and met cores fuse — one coal factor |
| 4 | METC + core | 0.489 | [[Ramaco\|METC]] attaches (looser — small-cap, rare-earth optionality) |
| 5 | ARLP + core | 0.595 | [[Alliance Resource Partners\|ARLP]] joins last — the thermal-MLP decoupler |

The factor has two tight anchors — the diversified majors ([[Peabody Energy|BTU]]+[[Core Natural Resources|CNR]], 0.81) and the pure met-coal pair ([[Alpha Metallurgical Resources|AMR]]+[[Warrior Met Coal|HCC]], 0.75) — that fuse into one coal cluster at 0.29. [[Ramaco|METC]] attaches more loosely (its [[Rare earth equity beta|Brook Mine rare-earth]] story adds idiosyncratic vol), and [[Alliance Resource Partners|ARLP]] (a stable thermal MLP, lowest correlation and lowest vol) is the decoupler — dropping it lifts the core to 0.642 and widens every distinctness margin.

### PC1 index weights

![[coal-cluster-pca-1y.png]]
*PCA on the candidate cohort. PC1 explains 64.7%; the diversified/met names ([[Peabody Energy|BTU]]/[[Alpha Metallurgical Resources|AMR]]/[[Warrior Met Coal|HCC]]/[[Core Natural Resources|CNR]]) load evenly (~0.43–0.46), [[Alliance Resource Partners|ARLP]] lowest (0.302, but lowest vol 23% — the stable MLP), [[Ramaco|METC]] high-vol (102% — the rare-earth-optionality name).*

| Ticker | PC1 loading | Loading weight | Ann vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| BTU | 0.446 | 18.41% | 60.41% | 15.41% |
| AMR | 0.433 | 17.88% | 61.11% | 14.79% |
| HCC | 0.433 | 17.86% | 55.64% | 16.23% |
| ARLP | 0.302 | 12.45% | 23.39% | 26.90% |
| METC | 0.349 | 14.38% | 102.40% | 7.10% |
| CNR | 0.461 | 19.02% | 49.12% | 19.58% |

### Distinctness — apart from steel, gas, energy, mining, and the market

![[coal-cluster-correlation-1y.png]]
*1Y pairwise correlation heatmap. The diversified/met core runs warm (0.67–0.81); [[Alliance Resource Partners|ARLP]] is the coolest (0.32–0.50). The cohort is only moderately tied to [[XME]] (~0.45) and weakly to [[Nucor|NUE]]/[[XLE]]/[[UNG]].*

Coal clears every proxy: +0.115 (core +0.148) vs the metals/mining ETF [[XME]] (the closest, since coal is mined — but the coal core still out-coheres it), +0.381 vs steel [[Nucor|NUE]] (met coal is more than a steel-demand derivative), +0.531 vs [[UNG]] (thermal coal and gas are substitutes, not co-movers), and +0.324 vs energy [[XLE]]. With no coal ETF to absorb it, the positive advantage over every available benchmark is the distinct-factor verdict.

### Historical tightness evolution

![[coal-cluster-rolling-tightness-90d.png]]
*Rolling 90-day cohesion since 2021 (the window the restructured/merged names share) — durable at 0.53–0.67, peaking 0.67 in the 2022 energy-crisis coal squeeze. A persistent coal factor through the cycle, consistent with the STABLE holdout.*

| Year | Avg intra-corr | PC1 |
|---|---|---|
| 2021 | 0.542 | 62.0% |
| 2022 | 0.670 | 72.6% |
| 2023 | 0.563 | 64.0% |
| 2024 | 0.535 | 62.2% |
| 2025 | 0.590 | 67.0% |
| 2026 | 0.530 | 63.0% |

## Where this sits in the campaign

Coal completes the campaign's commodity map as its exception. Every other mined or extracted commodity cohort resolved to a commodity ETF — copper to COPX, gold/silver to GDX/SIL, lithium to LIT, uranium to URA, steel to SLX — because a liquid ETF prices the same factor as its holdings (the index-rule collapse). Coal is the lone case with no ETF: VanEck's KOL was liquidated in 2020, so the miners co-move on a real, coal-specific demand factor that nothing absorbs, making them a distinct basket. It is the commodity-world analogue of [[Tankers]] and [[Cable broadband|cable]] — a genuine factor whose only expression is the names themselves. The split structure (a met-coal pair, a diversified pair, a thermal-MLP decoupler) echoes the within-sector substrate splits seen in [[Packaging]], but here the pieces still fuse into one coal factor rather than fragmenting.

## Related

- [[Peabody Energy]], [[Core Natural Resources]] — the diversified-major anchor; [[Alpha Metallurgical Resources]], [[Warrior Met Coal]], [[Ramaco]] — the met-coal core; [[Alliance Resource Partners]] — the thermal-MLP decoupler
- [[XME]] — metals/mining (the closest proxy, no coal ETF); [[XLE]] — energy; [[Nucor]] — steel (met-coal demand); [[UNG]] — natural gas (thermal competitor)
- [[Tankers]], [[Cable broadband]] — the same distinct-but-no-clean-ETF pattern; [[Rare earth equity beta]] — the critical-minerals link via [[Ramaco]]'s Brook Mine
- [[Vault cluster taxonomy]] — cross-cohort meta-analysis; [[Cohort, cluster, basket]] — terminology

---

*Created 2026-06-24. 1Y daily log returns through 2026-06-22; config `scripts/cluster_configs/coal.yaml`; registry row 2026-06-24. Cluster validation is structure, not a performance ranking — see `docs/cluster-validation.md`.*
