---
aliases: [Cable broadband, Cable, US cable broadband, Cable duopoly, Charter and Comcast]
tags: [sector, telecom, cable, broadband, cluster-validation]
---

# Cable broadband

> [!success] Cluster status: VALIDATED — a distinct cable-broadband pair ([[Charter Communications|CHTR]]+[[Comcast|CMCSA]]); the residential-broadband duopoly trades apart from the wireless carriers, the comms ETF, and the market, and no liquid ETF replicates it (Jun 2026)
> The two US cable operators cohere tightly (pair correlation 0.73, PC1 86%) and are genuinely distinct: +0.362 intra-advantage vs the wireless carriers ([[AT&T|T]]/[[Verizon|VZ]]/[[T-Mobile|TMUS]]), +0.348 vs the communications ETF [[XLC]], and +0.673 vs the market. They beat the random-basket null (p 0.0020), form their own cluster across a WIDE robust threshold band [0.30–0.60], and the pair is durable (holdout STABLE 1.07; correlated 0.6–0.8 every year since 2019). The distinctness is the [[Analog and auto-industrial semiconductors|index-rule escape]]: [[XLC]] is cap-weighted and ruled by [[Meta]]/[[Alphabet]], so it holds the cable names but tracks the mega-cap-internet factor, not cable. A 2-name distinct non-ETF factor — the cable analogue of the [[Card networks|V+MA]] duopoly. Own the pair; there is no cable ETF. See below.

The residential-broadband duopoly. [[Charter Communications|Charter]] (Spectrum) and [[Comcast]] (Xfinity) are the two US cable operators, and the market trades them as one factor because they share one driver: the residential-broadband subscriber book under a common three-front squeeze — video [[Cord-cutting|cord-cutting]], fixed-wireless competition ([[T-Mobile|T-Mobile]]/[[Verizon]] 5G home internet), and fiber overbuild. That driver is specific to cable: it is not the wireless carriers' spectrum/mobile economics, and it is invisible inside the [[Meta]]/[[Alphabet]]-dominated communications ETF. So the pair coheres and stays distinct.

## Sector performance

![[cable-performance.png]]
*Normalized total return since 2019 vs the wireless winner [[T-Mobile|TMUS]] and the communications ETF [[XLC]]. The cable pair ([[Charter Communications|CHTR]]/[[Comcast|CMCSA]]) moves together and DOWN — derated through the cord-cutting and broadband-pressure cycle (CHTR −25% on its Apr-2026 Q1 print alone) — while [[T-Mobile|TMUS]] (5G/fixed-wireless) and [[XLC]] (Meta/Alphabet-led) ran the other way. The two cable lines tracking each other apart from both benchmarks is the distinct-factor verdict made visible.*

## Cluster validation

The candidate cohort is the US cable-broadband pair — [[Charter Communications|CHTR]] and [[Comcast|CMCSA]] — tested against the wireless carriers ([[AT&T|T]]/[[Verizon|VZ]]/[[T-Mobile|TMUS]]), the communications-services ETF ([[XLC]]), satellite/wireless distribution ([[EchoStar|SATS]]), and the market ([[SPY]]). 1Y window through 2026-06-22 (199 obs); threshold 0.5. A pair test (ATUS/CABO not in the DB), the cable analogue of [[Card networks|V/MA]]. Config: `scripts/cluster_configs/cable.yaml`; registry row 2026-06-23. Terminology: [[Cohort, cluster, basket]].

### Diagnostics summary

| Diagnostic | Value | Read |
|---|---|---|
| Pair correlation (1Y) | 0.728 | Tight; durable 0.6–0.8 since 2019 |
| PC1 explained variance | 86.3% | High (degenerate for a clean pair) |
| Random-basket null p (10k) | 0.0020 | Real — 0.73 vs random 2-pick mean 0.14 |
| Holdout (2Y split) | STABLE 1.07 | Durable across regimes (train 0.68 → test 0.73) |
| Threshold stable width | 0.30 [0.30–0.60] | WIDE / ROBUST — clean cluster, boundary-insensitive |
| Intra-adv vs wireless telecom | +0.362 | Distinct from [[AT&T\|T]]/[[Verizon\|VZ]]/[[T-Mobile\|TMUS]] |
| Intra-adv vs comms ETF ([[XLC]]) | +0.348 | Distinct — XLC is Meta/Alphabet-ruled (index-rule) |
| Intra-adv vs market (SPY) | +0.673 | Low market beta — idiosyncratic sector |
| Intra-adv vs satellite ([[EchoStar\|SATS]]) | +0.704 | SATS near-orthogonal (corr 0.02) |

### Boundary — three distinct groups

![[cable-cluster-dendrogram-1y.png]]
*Hierarchical clustering at 0.5. Three clean groups: the cable pair [[Charter Communications|CHTR]]+[[Comcast|CMCSA]] (orange, join 0.27), the wireless carriers [[T-Mobile|TMUS]]/[[AT&T|T]]/[[Verizon|VZ]] (green), and [[XLC]]+[[SPY]] (red — the comms ETF tracks the market), with [[EchoStar|SATS]] a far singleton. The cable pair merges with the wireless cluster only at 0.63 and with XLC/SPY only at 0.86 — it is its own factor.*

The threshold scan returns a WIDE robust stable band [0.30–0.60] (width 0.30): the cable pair forms a clean, uncontaminated cluster across a broad range of cuts. Combined with the large positive intra-advantages over every control, that is the distinct-non-ETF-factor signature.

### Topology

Reading the candidate cohort by join distance (average linkage, 1−|corr|):

| Join step | Names | Distance (1-\|corr\|) | Read |
|---|---|---|---|
| 1 | CHTR + CMCSA | 0.272 | the cable-broadband pair (corr 0.728) — the only join |

### PC1 index weights

![[cable-cluster-pca-1y.png]]
*PCA on the pair. PC1 explains 86.3% — one shared cable factor. Loadings are equal (0.707 each, as for any clean pair); the raw mimic weights tilt to [[Comcast|CMCSA]] on its lower volatility (31.7% vs [[Charter Communications|CHTR]]'s 52.7% — CHTR carries the Cox-deal and broadband-loss idiosyncratic risk).*

| Ticker | PC1 loading | Loading weight | Ann vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| CHTR | 0.707 | 50.00% | 52.66% | 37.60% |
| CMCSA | 0.707 | 50.00% | 31.74% | 62.40% |

### Distinctness — apart from wireless, comms, and the market

![[cable-cluster-correlation-1y.png]]
*1Y pairwise correlation heatmap. [[Charter Communications|CHTR]]–[[Comcast|CMCSA]] run warm (0.73); both are cool to the wireless carriers (~0.37), the comms ETF (~0.38), and the market (~0.06), and near-zero to [[EchoStar|SATS]].*

The intra-advantages are large and positive against everything: +0.362 vs the wireless carriers (cable's broadband/video book is a different business from mobile/spectrum), +0.348 vs [[XLC]] (the [[Analog and auto-industrial semiconductors|index-rule]] escape — XLC is ruled by [[Meta]]/[[Alphabet]], so the cable names sit inside it but it tracks a different factor), +0.673 vs the market, and +0.704 vs [[EchoStar|SATS]] (satellite is the distressed wireless-buildout story, near-orthogonal at 0.02). No liquid ETF isolates the cable pair, so the basket is the only expression.

### Historical tightness evolution

![[cable-cluster-rolling-tightness-90d.png]]
*Rolling 90-day pair correlation since 2019. Durable at 0.6–0.8 throughout, with one dip to 0.40 in the 2021 broadband-boom divergence and a peak of 0.81 in 2023 as the cord-cutting / broadband-subscriber pressure hit both names together; latest 90-day 0.79. A persistent pair, tightening when the shared cable-specific pressure is loudest.*

| Year | Pair corr | PC1 |
|---|---|---|
| 2019 | 0.614 | 80.7% |
| 2021 | 0.396 | 69.8% |
| 2022 | 0.701 | 85.0% |
| 2023 | 0.806 | 90.3% |
| 2024 | 0.668 | 83.4% |
| 2025 | 0.708 | 85.4% |
| 2026 | 0.598 | 79.9% |

## Where this sits in the campaign

Cable broadband is a distinct non-ETF factor of the sub-group / pair type — the [[Card networks|V+MA]] and [[Self-storage REITs|PSA/EXR/CUBE]] pattern, where a tight homogeneous duopoly is genuinely distinct and no liquid ETF replicates it. It completes the communications map: the wireless carriers are their own cluster ([[Telecom]], = the carriers), the cap-weighted comms ETF [[XLC]] tracks [[Meta]]/[[Alphabet]] (a mega-cap-internet factor, not communications-distribution), and cable broadband stands apart as a third, ownable-only-as-a-basket factor. It is the clean counter-example to the session's China and hydrogen cohorts: where those resolved into their sector ETFs, cable escapes because its sole liquid ETF is ruled by an unrelated factor.

## Related

- [[Charter Communications]], [[Comcast]] — the cohort pair (the residential-broadband duopoly)
- [[AT&T]], [[Verizon]], [[T-Mobile]] — the wireless carriers the cable pair trades apart from (and the [[T-Mobile|FWA]] competition); [[Telecom]] — their cohort
- [[XLC]] — the comms ETF the pair is distinct from (Meta/Alphabet-ruled); [[EchoStar]] — satellite/wireless distribution (orthogonal)
- [[Cord-cutting]] — the shared video-decline driver; [[Cable broadband subscriber meltdown April 2026]] — the Q1-2026 broadband-loss event
- [[Card networks]] — the duopoly-pair analogue; [[Vault cluster taxonomy]] — cross-cohort meta-analysis; [[Cohort, cluster, basket]] — terminology

---

*Created 2026-06-23. 1Y daily log returns through 2026-06-22; config `scripts/cluster_configs/cable.yaml`; registry row 2026-06-23. Cluster validation is structure, not a performance ranking — see `docs/cluster-validation.md`.*
