---
aliases: [Theatrical exhibition, Movie theater stocks, Cinema exhibitors, Theatrical exhibition cluster, Movie exhibitor basket]
tags: [concept, media, exhibition, market-structure, cluster-validation]
---

# Theatrical exhibition

The listed US movie-theater names — [[AMC Entertainment]] (AMC), [[Cinemark]] (CNK), [[IMAX]] (IMAX). The hypothesis was that "theatrical exhibition" is a tradeable factor: three companies whose revenue all keys off the same box office should rise and fall on the same slate-and-attendance cycle. The data falsifies it. The three share an end-market but monetize it through structurally different models with different dominant risk drivers, so they do not trade as one factor — and the weak co-movement that did exist (the 2021 meme / COVID-reopening era) has faded as the box office normalized.

> [!failure] Cluster status: falsified — a shared end-market, not a shared factor (June 2026)
> The three exhibitor names do not trade as one factor: intra-corr 0.328 (below the 0.50 floor), PC1 only 55.5% with a large PC2 (27.6%), and hierarchical clustering never returns them as a clean cluster at any threshold (zero stable width). On the verified clean pool the random-basket null is thinly rejected (p 0.036, Jul 1 2026 re-run; the June 0.099 was against a fund-inflated null) while the June-vintage vol-matched null failed (0.108) — the thin co-movement is shared high-vol consumer beta, not an exhibitor factor; the zero threshold width and the structural mismatch of the three business models remain the decisive falsification. [[AMC Entertainment]] is a levered meme stock (71% annualized vol; correlates just 0.17 with [[IMAX]]), [[IMAX]] is an asset-light premium-format licensor, and [[Cinemark]] is the only clean operating exhibitor. Cohesion has declined steadily — 0.459 in 2021 to 0.328 in 2026 (holdout WEAKENED, ratio 0.81). See below.

A shared end-market is not a shared return factor. This is the theatrical mirror of the [[Exchange operators]] falsification, where a shared moat did not make a cluster: here the three names all depend on box-office revenue, but [[AMC Entertainment]]'s equity trades on retail flow and balance-sheet / dilution risk, [[IMAX]]'s on a royalty-like licensing stream, and [[Cinemark]]'s on operating exhibition economics. The box office is a common input; it is not a common factor.

## Cluster validation

### Diagnostics summary

| Diagnostic | Value | Read |
|---|---|---|
| Intra-cluster corr (1Y) | 0.328 [0.172–0.412] | Weak — below the 0.50 floor; weekly 0.299 |
| PC1 explained variance | 55.5% (PC2 27.6%) | Multi-factor, not a single-factor cluster |
| Independence null p (10k) | 0.0001 | The three do co-move (necessary, not sufficient) |
| Random-basket p (10k) | 0.036 (clean pool, Jul 1 2026; was 0.099 on the fund-inflated June pool) | Thin rejection — co-movement is shared beta, not an exhibitor factor |
| Vol-matched p (10k) | 0.108 | FAILS to reject — not a real shared factor |
| Threshold stable width | 0.00 — none | Never a clean cluster at any cut (0.20–0.70) |
| Holdout ratio (2Y split) | 0.81 — WEAKENED | Train 0.405 / test 0.328; loadings corr 0.64 |
| Intra-adv vs content supply (DIS/LION) | +0.100 | Barely distinct from the studios it depends on |
| Intra-adv vs out-of-home ([[Live Nation]]) | +0.225 | — |
| Intra-adv vs [[SPY]] / [[XLY]] | +0.153 | Only mildly distinct from discretionary beta |

1Y daily log returns through 2026-06-11, threshold 0.5. Config: `scripts/cluster_configs/amc.yaml`; registry row 2026-06-14. Terminology: [[Cohort, cluster, basket]].

### The decisive test — random-basket null

![[amc-cluster-permutation.png]]
*Permutation nulls (10,000 draws). The independence null is rejected (observed intra-corr 0.328 far exceeds the independence-null mean ~0), so the three are not unrelated. But against the random-basket null — random 3-picks from the 237-name pool of comparable US-listed stocks — the observed 0.328 sits below the 95th percentile (0.377), giving p 0.099. The cohort is no tighter than three random comparable names. That is the falsification: co-movement exists, but nothing a "theatrical exhibition" label explains beyond chance.*

### Boundary — three singletons, never a cluster

![[amc-cluster-dendrogram-1y.png]]
*Hierarchical clustering at 0.5. The three names do not form a cluster — each sits as its own singleton, alongside [[Live Nation]], [[Disney]], [[Lionsgate]] and the ETFs. [[Cinemark]] and [[IMAX]] are the closest pair but join only at distance 0.588; [[AMC Entertainment]] joins at 0.715 — both far beyond the 0.50 cut. The "exhibition" label does not map to a trading factor.*

The threshold scan is zero-width: the cohort never returns as a clean single cluster at any threshold from 0.20 to 0.70. At the working cuts (0.50–0.55) all three are singletons; only above 0.60 do [[Cinemark]] and [[IMAX]] pair up, and [[AMC Entertainment]] never joins below 0.70.

### Topology — one weak pair, plus AMC far out

| Join step | Names | Distance (1-\|corr\|) | Read |
|---|---|---|---|
| 1 | CNK + IMAX | 0.588 | The only sub-pair — and already above the 0.50 cut |
| 2 | AMC + (CNK+IMAX) | 0.715 | [[AMC Entertainment]] joins far out — the meme / levered outlier |

There is no core. The tightest link in the entire cohort (CNK–IMAX at 0.588) is looser than the *loosest* join inside a validated cluster like [[European rearmament]] (every member ≤ 0.273). [[AMC Entertainment]]'s 0.17 correlation with [[IMAX]] is the structural tell — a levered meme stock and an asset-light licensor are not the same trade.

### PC1 index weights

![[amc-cluster-pca-1y.png]]
*PCA scree and PC1 loadings. PC1 explains only 55.5% with a large PC2 (27.6%) — the signature of a multi-factor cohort, not a single-factor cluster. A one-factor basket misses nearly half the variance.*

| Ticker | PC1 loading | Loading weight | Ann vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| AMC | 0.531 | 30.8% | 71.1% | 20.5% |
| CNK | 0.652 | 37.8% | 41.2% | 43.4% |
| IMAX | 0.541 | 31.4% | 41.1% | 36.1% |

[[Cinemark]] carries the highest PC1 loading (0.652) — fitting, since it is the only pure operating exhibitor and sits between the other two (it correlates 0.40 with each). [[AMC Entertainment]]'s 71% annualized volatility (versus ~41% for the other two) means the inverse-vol mimic basket de-weights it sharply, but because PC1 captures only ~55% of variance the single-factor basket is not an informative trade here — the topology (no core) is the real structure.

### Distinctness

![[amc-cluster-correlation-1y.png]]
*1Y pairwise correlation heatmap. There is no warm block. [[Cinemark]] is mildly warm to both neighbors (0.40, 0.41), but [[AMC Entertainment]]–[[IMAX]] is cold (0.17), and the cohort is barely distinguishable from the content suppliers ([[Disney]], [[Lionsgate]]) it depends on (intra-advantage only +0.100).*

### Historical tightness evolution

![[amc-cluster-rolling-tightness-90d.png]]
*Rolling 90-day cohesion. Whatever weak co-movement existed peaked in the 2021–2023 window (~0.46–0.48, PC1 ~64–66%) — the meme-stock and COVID-reopening era when AMC's retail surge and a synchronized box-office recovery moved the names together — and has declined monotonically since as the box office normalized and each name's idiosyncratic driver reasserted.*

| Window | Avg intra-corr | PC1 | Final join distance |
|---|---|---|---|
| 2021 | 0.459 | 64.3% | 0.609 |
| 2023 | 0.476 | 65.6% | 0.627 |
| 2024 | 0.393 | 60.3% | 0.686 |
| Latest 90d | 0.355 | 57.6% | 0.727 |

*Fragmenting, not durable: the decline from the 2021–2023 peak is the signature of a cohort that was never a structural cluster, only a temporary co-movement under a common shock (meme flow + reopening). The 2Y holdout (WEAKENED, ratio 0.81, loadings corr 0.64) confirms the factor structure is eroding, not stabilizing.*

### The read-through

- Do not trade "movie theaters" as one basket. There is no single factor (intra 0.328, PC1 55%, zero threshold width, random-basket null not rejected). A long-exhibition sleeve holding all three is holding three unrelated risks.
- [[AMC Entertainment]] is its own animal. Its equity is a levered call on the film slate dominated by retail flow and dilution / balance-sheet risk (71% annualized vol); it correlates just 0.17 with [[IMAX]]. Treat it as a meme / special-situation, not a theatrical-exhibition proxy.
- [[IMAX]] is closer to a content/format licensor than an exhibitor. Asset-light, royalty-like revenue on premium screens — its return driver is premium-format adoption and the blockbuster slate, not theater operating economics.
- [[Cinemark]] is the cleanest box-office expression. The only pure operating exhibitor with a clean balance sheet; if you want exposure to theatrical attendance and exhibition economics, it is the single name, not the basket.
- The lesson generalizes the [[Exchange operators]] falsification. There a shared moat did not make a cluster; here a shared end-market does not either. A cluster is a shared return factor — not an industry, a moat, or a common revenue input.

Method and terminology: `docs/cluster-validation.md`, [[Cohort, cluster, basket]], [[Vault cluster taxonomy]]. Post-definition OOS re-validation is moot for a falsified cohort; the definition date (2026-06-14) is logged.

## Related

- [[Vault cluster taxonomy]] — cross-cohort comparison; this joins [[Mag 7 cluster]], [[Foundry monopoly consolidation|Foundry monopoly]] and [[Exchange operators]] as a documented falsification
- [[Exchange operators]] — the parallel falsification (a shared moat is not a cluster; here a shared end-market is not either)
- [[AMC Entertainment]], [[Cinemark]], [[IMAX]] — the three members, three different return-driver archetypes
- [[Live Nation]] — out-of-home / live-events control
- [[Disney]], [[Lionsgate]] — content-supply control (the studios the exhibitors depend on)
- [[Cohort, cluster, basket]] — terminology

*Created 2026-06-14.*
