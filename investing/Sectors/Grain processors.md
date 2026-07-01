---
aliases: [Grain processors, Grain merchants, ADM and Bunge, Agri-processors, Crush margin]
tags: [sector, agriculture, agribusiness, grain, cluster-validation]
---

# Grain processors

> [!success] Cluster status: marginally VALIDATED — a distinct grain-processor pair ([[ADM]]+[[Bunge|BG]]); a durable, near-market-neutral crush-margin factor sharply distinct from the grain COMMODITY, but only marginally distinct from the agribusiness ETF [[MOO]] (Jun 2026)
> The two global grain merchants cohere at 0.68 (PC1 84%), durably (0.48–0.85 every year since 2019, holdout STABLE 0.85), and beat the random-basket null (p 0.0074 at 10k permutations). Two distinctness facts are sharp and one is marginal. Sharp: +0.507 intra-advantage vs the ag-commodity ETF [[DBA]] — the processors are NOT the long-grain trade; they earn on the crush/origination spread, which often moves inversely to grain prices (the [[Agricultural equipment|equity-vs-commodity split]] in its purest form). And +0.657 vs the market ([[SPY]]) — they correlate just 0.026 with the S&P, one of the most market-neutral cohorts in the campaign. Marginal: only +0.122 vs the agribusiness ETF [[MOO]], with a NARROW stable threshold band [0.35–0.40] before MOO contaminates at 0.45 — MOO holds [[ADM]]/[[Bunge|BG]] at top weight and mostly captures them. The net-lease-REIT verdict type: distinct, but barely, and only versus its sector ETF. The robust, ownable read is the crush-margin / market-neutral character. See below.

The crush-margin duopoly. [[ADM|Archer-Daniels-Midland]] and [[Bunge]] are the two listed global grain merchants — origination, storage, transport, and oilseed crushing — and the market trades them as one factor because they share one driver: the crush/processing spread and grain-origination margins across the global ag cycle. That driver is specific and unusual: it is largely uncorrelated with the equity market (a real-economy ag-margin cycle), and it is distinct from the grain commodity itself (a processor's spread can widen when grain prices fall). So the pair coheres and stays market-neutral — but because the agribusiness ETF [[MOO]] holds both at top weight, the distinctness over the ETF is only marginal.

## Sector performance

![[grain-performance.png]]
*Normalized total return since 2019 vs the agribusiness ETF [[MOO]] and the ag-commodity ETF [[DBA]]. [[ADM]] and [[Bunge|BG]] move together and roughly with [[MOO]] (which holds them), but clearly apart from [[DBA]] — the grain-equity / grain-commodity split made visible. The processors' market-neutral, spread-driven path is its own line.*

## Cluster validation

The candidate cohort is the grain-processor pair — [[ADM]] and [[Bunge|BG]] — tested against the agribusiness ETF ([[MOO]] — the key benchmark), the ag-commodity ETF ([[DBA]], grain futures), consumer staples ([[XLP]], the end-market), and the market ([[SPY]]). 1Y window through 2026-06-22 (199 obs); threshold 0.5. A pair test (INGR/DAR not in the DB). Config: `scripts/cluster_configs/grain.yaml`; registry row 2026-06-24. Terminology: [[Cohort, cluster, basket]].

### Diagnostics summary

| Diagnostic | Value | Read |
|---|---|---|
| Pair correlation (1Y) | 0.683 | Durable; weekly 0.711 |
| PC1 explained variance | 84.2% | One crush-margin factor |
| Random-basket null p | 0.0027 | Real — 0.68 vs random 2-pick mean 0.14 |
| Holdout (2Y split) | STABLE 0.85, loadings-corr 0.95 | Durable, stable structure |
| Threshold stable width | 0.05 [0.35–0.40] | NARROW — [[MOO]] contaminates from 0.45 |
| Intra-adv vs agribusiness ETF ([[MOO]]) | +0.122 | Marginal — MOO holds the pair at top weight |
| Intra-adv vs ag-commodity ([[DBA]]) | +0.507 | Sharp — processors ≠ the long-grain trade |
| Intra-adv vs staples ([[XLP]]) | +0.390 | Agribusiness, not defensive food |
| Intra-adv vs market (SPY) | +0.657 | Near-zero market correlation (0.026) |

### Boundary — distinct from the commodity and market, marginal vs the ETF

![[grain-cluster-dendrogram-1y.png]]
*Hierarchical clustering at 0.5. [[ADM]]+[[Bunge|BG]] cluster with the agribusiness ETF [[MOO]] (which holds them), while [[DBA]] (ag commodities), [[XLP]] (staples), and [[SPY]] (market) each stand apart. The pair is its own factor versus the commodity and the market, but [[MOO]] absorbs it at the 0.5 cut — the marginal-distinctness signature.*

The threshold scan returns a NARROW stable band [0.35–0.40] (width 0.05): [[ADM]]+[[Bunge|BG]] form a clean cluster only just below where [[MOO]] joins at 0.45. That, with the +0.122 intra-advantage over MOO, makes this the net-lease-REIT type — a real distinct factor, but the thinnest separation from its sector ETF. Against the ag commodity ([[DBA]], +0.507) and the market (+0.657) the separation is wide and unambiguous.

### Topology

Reading the candidate cohort by join distance (average linkage, 1−|corr|):

| Join step | Names | Distance (1-\|corr\|) | Read |
|---|---|---|---|
| 1 | ADM + BG | 0.317 | the grain-merchant pair (corr 0.683) — the only join |

### PC1 index weights

![[grain-cluster-pca-1y.png]]
*PCA on the pair. PC1 explains 84.2% — one shared crush-margin factor. Equal loadings (0.707), with near-identical low volatility (~27–30%) — these are stable, real-economy ag-margin names, not high-beta.*

| Ticker | PC1 loading | Loading weight | Ann vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| ADM | 0.707 | 50.00% | 26.93% | 52.88% |
| BG | 0.707 | 50.00% | 30.22% | 47.12% |

### Distinctness — the equity-vs-commodity split, and market-neutrality

![[grain-cluster-correlation-1y.png]]
*1Y pairwise correlation heatmap. [[ADM]]–[[Bunge|BG]] run warm (0.68); both are cool to [[DBA]] (0.18) and essentially uncorrelated with the market (0.03).*

The two robust distinctness numbers are the story. +0.507 vs [[DBA]]: the grain processors are an agribusiness-EQUITY factor (crush and origination margins), not the ag-COMMODITY trade — a processor's spread can widen as grain prices fall, so [[ADM]]/[[Bunge|BG]] correlate just 0.18 with grain futures. And +0.657 vs the market: with a 0.026 correlation to [[SPY]], this is among the most market-neutral cohorts in the campaign — a real-economy ag-margin cycle that runs largely independent of equity beta. The marginal number is vs [[MOO]] (+0.122): the agribusiness ETF holds both names at top weight, so it captures most of the factor, leaving only a thin distinct margin.

### Historical tightness evolution

![[grain-cluster-rolling-tightness-90d.png]]
*Rolling 90-day pair correlation since 2019 — durable at 0.48–0.85, tightening to 0.85 in the 2022 grain-price spike (the Ukraine-war food-security shock, when both names moved on one origination/crush story) and holding ~0.77 into 2026. A persistent crush-margin pair through the cycle.*

| Year | Pair corr | PC1 |
|---|---|---|
| 2019 | 0.603 | 80.2% |
| 2020 | 0.717 | 85.9% |
| 2021 | 0.635 | 81.8% |
| 2022 | 0.845 | 92.3% |
| 2023 | 0.742 | 87.1% |
| 2024 | 0.483 | 74.2% |
| 2025 | 0.766 | 88.3% |
| 2026 | 0.766 | 88.3% |

## Where this sits in the campaign

Grain processors are a marginally-distinct pair — the [[Net-lease REITs|net-lease]] type, where the factor clears the bar over its sector ETF only thinly (+0.122 vs [[MOO]], narrow band). What makes it interesting is the two sharp separations: it is the cleanest equity-vs-commodity split in the campaign (+0.507 vs [[DBA]] — the [[Agricultural equipment|ag-equipment lesson]] that agribusiness equities are not the crop trade, here in its purest form), and one of the most market-neutral cohorts (0.03 to SPY). It sits at the boundary between the distinct-pair set ([[Construction aggregates|aggregates]], [[Cable broadband|cable]]) and the MOO-replicable agribusiness names ([[Agricultural equipment]], [[Fertilizer producers]]) — distinct enough to own as a crush-margin / market-neutral expression, but mostly captured by [[MOO]] if all you want is the ag-equity beta.

## Related

- [[ADM]], [[Bunge]] — the cohort pair (the global grain merchants / crush duopoly)
- [[MOO]] — the agribusiness ETF that holds both at top weight (captures most of the factor); [[DBA]] — ag commodities, the grain trade the processors are distinct from; [[XLP]] — consumer staples (the end-market)
- [[Agricultural equipment]], [[Fertilizer producers]] — the MOO-replicable agribusiness cohorts; [[Construction aggregates]], [[Cable broadband]] — the cleanly-distinct pairs this sits just inside of
- [[Vault cluster taxonomy]] — cross-cohort meta-analysis; [[Cohort, cluster, basket]] — terminology

---

*Created 2026-06-24. 1Y daily log returns through 2026-06-22; config `scripts/cluster_configs/grain.yaml`; registry row 2026-06-24. Cluster validation is structure, not a performance ranking — see `docs/cluster-validation.md`.*
