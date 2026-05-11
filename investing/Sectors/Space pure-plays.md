---
aliases: [Space pure-play basket, Space cohort, Small-cap space, Public space pure-plays]
---
#sector #space #cluster #small-cap #public

# Space pure-plays

The tradeable public-equity cohort of small-cap space companies. Seven NASDAQ/NYSE names that listed 2020-2024 via SPAC or direct IPO, all operating as pure-play space businesses (launch + Space Systems, earth observation, communications, RF data, on-orbit hardware). Distinct from heritage defense primes ([[Lockheed Martin]], [[Northrop Grumman]], [[RTX]], [[L3Harris]]) which have space exposure embedded inside broader defense portfolios.

Mathematically validated as a single statistical cluster (intra-cluster avg correlation 0.624 over trailing 1Y, PC1 explained variance 67.96%, all 7 names grouped at hierarchical distance <0.5). The cohort is the right entry point for the "public-tradeable space sector" exposure — distinct from [[SpaceX|SpaceX private]], distinct from heritage defense primes.

---

## Members

| Ticker | Actor | Archetype | Business model |
|--------|-------|-----------|----------------|
| RKLB | [[Rocket Lab]] | Launch + Space Systems | Electron launches + spacecraft components + Golden Dome SBI work |
| RDW | [[Redwire]] | Space hardware + defense UAS | Components, solar arrays, robotics; Edge Autonomy UAS post-2025 |
| LUNR | [[Intuitive Machines]] | Lunar services | NASA CLPS; Earth-to-moon communications |
| BKSY | [[BlackSky]] | Earth observation (optical) | Real-time GEOINT for NGA + commercial |
| ASTS | [[AST SpaceMobile]] | Satellite-to-cell broadband | BlueBird constellation; carrier partnerships ~3B subscribers |
| SPIR | [[Spire Global]] | RF satellite data | Weather, IoT, aviation/maritime tracking |
| PL | [[Planet Labs]] | Earth observation (constellation) | Daily-revisit optical imagery + analytics |

Excluded from the validated cluster (different structural profile):
- [[Vast Space]], [[SpaceX]] — private, no public-equity participation
- [[Iridium Communications]] — large-cap satellite operator; trades on services-revenue cycle, not space-pure-play factor
- [[Maxar]] — taken private 2023
- [[EchoStar]] — satellite operator + spectrum holder; different beta profile
- [[Mynaric]], [[Sidus Space]] — micro-caps, not yet in local market_data.db universe

---

## Normalized return chart (Jan 2024 → May 8 2026)

![[rklb-vs-rdw-vs-lunr-vs-bksy-vs-asts-vs-spir-vs-pl-price-chart.png]]
*All 7 cluster members normalized. RKLB (blue) and ASTS (purple) lead at ~+1700-1900%; LUNR (green) ~+1100%; PL (brown) ~+800%; RDW (red) and BKSY (orange) ~+200-220%; SPIR (cyan) ~+110%. The basket moves together but cumulative return dispersion is ~17x — daily co-movement coexists with single-stock outcome variance.*

---

## Cluster validation diagnostic

Per CLAUDE.md Hard Gate 11. Config: `scripts/cluster_configs/rklb.yaml`. Run: `python scripts/cluster_analysis.py --primary RKLB`. Window: 1-year daily returns through 2026-05-07 (173 observations).

### Diagnostic summary

| Diagnostic | Value | Read |
|---|---|---|
| Intra-cluster avg correlation (1Y) | 0.624 | Tight; range 0.494-0.749 |
| Hierarchical clustering @ 0.5 threshold | All 7 names in single cluster | RKLB, RDW, LUNR, BKSY, ASTS, SPIR, PL |
| PC1 explained variance | 67.96% | One factor drives ~2/3 of variance |
| PC1 loadings | 0.35-0.40 across all 7 | Single common factor, no sub-cluster splits |

### Pairwise correlations (1Y)

| | RKLB | RDW | LUNR | BKSY | ASTS | SPIR | PL |
|---|---|---|---|---|---|---|---|
| RKLB | 1.00 | 0.69 | 0.75 | 0.69 | 0.74 | 0.53 | 0.62 |
| RDW | 0.69 | 1.00 | 0.64 | 0.63 | 0.69 | 0.53 | 0.49 |
| LUNR | 0.75 | 0.64 | 1.00 | 0.66 | 0.69 | 0.57 | 0.60 |
| BKSY | 0.69 | 0.63 | 0.66 | 1.00 | 0.66 | 0.63 | 0.64 |
| ASTS | 0.74 | 0.69 | 0.69 | 0.66 | 1.00 | 0.57 | 0.53 |
| SPIR | 0.53 | 0.53 | 0.57 | 0.63 | 0.57 | 1.00 | 0.55 |
| PL | 0.62 | 0.49 | 0.60 | 0.64 | 0.53 | 0.55 | 1.00 |

Tightest pairs: RKLB-LUNR (0.75) and RKLB-ASTS (0.74) — launch + space-systems alignment makes RKLB the cohort's center of gravity. Loosest: RDW-PL (0.49) — hardware vs pure-data businesses. SPIR is the cohort's outlier (lowest average correlation ~0.55) — the data-business model trades on its own catalyst path.

### Separation from controls

| Control group | Inter-group corr | Intra-cluster advantage |
|---|---|---|
| Defense primes (LMT, RTX, NOC, LHX) | 0.285 | +0.339 — NOT defense beta |
| Small-cap (IWM) | 0.509 | +0.115 — modest shared small-cap risk |
| Broad / sector ETFs (SPY, ITA, XAR) | 0.434 | +0.190 — clear separation |

The +0.339 separation from defense primes is the load-bearing finding. It empirically falsifies the easy framing "space pure-plays are just leveraged defense beta." Both cohorts participate in the same [[2026 Iran conflict defense repricing|war-premium]] tailwind and the same [[Golden Dome]] program, but they trade as distinct clusters with materially different daily factor exposure.

### Stability across windows

The 1Y diagnostic is the primary read, but cohort cohesion is increasing over time. Run via `python scripts/cluster_stability_check.py` (ends 2026-05-07):

| Window | Obs | Intra-cluster avg | Range | PC1 var | PC2 var | vs Defense | Gap |
|---|---|---|---|---|---|---|---|
| YTD 2026 | 65 | 0.636 | [0.51, 0.78] | 69.3% | 8.3% | 0.270 | +0.365 |
| 1Y | 135 | 0.607 | [0.50, 0.75] | 66.6% | 8.8% | 0.241 | +0.365 |
| 2Y | 180 | 0.551 | [0.29, 0.74] | 60.4% | 14.7% | 0.242 | +0.309 |
| 3Y | 263 | 0.482 | [0.26, 0.60] | 54.8% | 14.1% | 0.218 | +0.263 |

Three structural reads from the time-progression:

1. The cohort is tightening, not loosening. Intra-cluster average correlation rises monotonically from 0.48 (3Y) to 0.64 (YTD) — the "space pure-play factor" is structurally strengthening as the names mature, the float deepens, and basket-level flows compound. The May 8 single-session basket rally is consistent with a longer trend of the cohort consolidating as a tradeable single factor, not a one-off.
2. PC1 variance share rising and PC2 falling — same conclusion. 3Y has 54.8% / 14.1% on PC1/PC2 (two-factor structure); YTD has 69.3% / 8.3% (one-factor structure). The cohort is collapsing onto a single principal component, which is what you would expect if institutional flows and ETF-style basket trading are increasingly dominating the cohort's price dynamics relative to single-name fundamentals.
3. Separation from defense primes is durable across all windows. Gap to defense ranges +0.263 (3Y) to +0.365 (1Y/YTD) — the cluster has *always* traded distinctly from defense, and that separation is widening, not collapsing. The "leveraged defense beta" framing has never been an accurate description of this cohort, even in earlier windows where space-pure-plays were less individually coherent.

The 1Y window remains the recommended diagnostic because it (a) is the standard correlation lookback used across the [[WFE]] / [[AI Compute]] / [[US Memory]] cluster notes for cross-comparability and (b) captures enough trading days for meaningful PCA stability without diluting the recent regime shift. The YTD reading is included as a forward-looking pulse check; the 2Y and 3Y windows confirm direction-of-travel.

### Validation charts

![[space-pureplays-cluster-dendrogram-1y.png]]
*Hierarchical clustering dendrogram — all 7 space pure-plays cluster together at distance < 0.5, separated from defense primes, small-cap (IWM/SPY), and ETF controls.*

![[space-pureplays-cluster-correlation-1y.png]]
*1Y pairwise correlation heatmap across the full 14-ticker universe. The space-cluster block is visibly distinct from the defense + ETF blocks.*

![[space-pureplays-cluster-pca-1y.png]]
*PCA biplot — PC1 (67.96% variance) is the "space pure-play factor"; PC2 (8.57%) captures modest sub-structure (where SPIR's data-business idiosyncrasy shows up).*

---

## Why this cluster trades together

1. Shared funding-flow profile — all 7 names are small-cap (sub-$50B market cap), recent-IPO (2020-2024 listing), with high idiosyncratic vol (60-115%). They attract the same investor base (retail + small-cap-thematic funds + space-specialist managers) and lose/gain that base together. Daily flows move them in lockstep regardless of underlying business overlap.
2. Shared catalyst environment — [[SpaceX IPO 2026|SpaceX IPO]] anticipation, [[Golden Dome]] contract awards, [[2026 Iran conflict defense repricing|Iran-war defense-spending]] backdrop, [[Starlink]] launch-demand fundamentals — all apply to the cohort asymmetrically but to every name. When any single catalyst lands (e.g., RKLB Q1 record on May 7), the basket re-rates together.
3. Thin price discovery — small float + high short interest + retail-heavy ownership profile compounds basket co-movement. When one name moves, paired/basket trading expressions amplify the move across peers.
4. Structurally similar TAM frames — every name's TAM presentation references the [[Space Capital]] $36B Q1 2026 investment data, the $1T+ space economy by 2030 framing, and the [[Satellite primer|infrastructure-not-exploration]] thesis. Bullish narrative shifts move the whole cohort.

The cohort does NOT share execution risk. Business-model heterogeneity (launch + EO + comms + data + hardware) means an RKLB Neutron-flight slip is independent of ASTS BlueBird-deployment risk is independent of LUNR CLPS-contract execution. Co-movement is funding/sector-multiple, not fundamental-business-quality.

---

## Cohort economics

| Metric | Range across cohort |
|--------|---------------------|
| Market cap | $400M ([[BlackSky]]) to ~$45B ([[Rocket Lab]]) |
| Beta to SPY (120d) | 1.20 ([[Planet Labs]]) to 3.51 ([[Rocket Lab]] / [[IREN]] comparison range) |
| Idiosyncratic vol (60d) | 67% (RKLB) to 115% (SPIR) |
| Listing year | 2020 (LUNR via SPAC) to 2024 |
| Profitability | Pre-profit cohort-wide; one ([[Rocket Lab]] Q1 2026) has shown record gross margin |
| Backlog | RKLB $2.2B leads; remainder $100M-$500M typical |

---

## Active theses

| Thesis | Notes |
|--------|-------|
| Cohort multiple re-rates with [[SpaceX IPO 2026|SpaceX June 2026 IPO]] | The IPO sets the read-across cap for the basket multiple |
| [[Golden Dome]] production-contract phase | [[Rocket Lab]] + [[Raytheon]] SBI selection (May 8) is the first launch-tier prime to win at production scale |
| [[2026 Iran conflict defense repricing]] routes through cohort | War premium that drove March-April defense-prime outperformance is now reaching launch-tier names |
| Within-cluster dispersion offers single-name alpha | The 17x cumulative-return dispersion despite 0.62 correlation means basket exposure ≠ optimal exposure — single-name selection still matters |

---

## Events touching the cohort

- [[Space basket rally May 8 2026]] — Friday May 8 single-session basket rally, average +20.4%, range +10.8% to +34.2%
- [[Rocket Lab]] Q1 2026 print (May 7) — the catalyst for the basket move
- [[SpaceX IPO 2026]] — upcoming June 2026; sets the read-across cap

---

## Related

### Parent
- [[Sectors/Space|Space]] — sector hub (industry overview, all segments incl. private + heritage defense)

### Concepts
- [[Satellite primer]] — orbital mechanics + constellation economics
- [[Golden Dome]] — missile defense program; SBI contract channel for cohort
- [[Space data centers]] — emerging adjacent opportunity
- [[Iran conflict defense repricing]] — war-premium backdrop

### Adjacent cohorts (control groups in validation)
- Defense primes — [[Lockheed Martin]], [[RTX]], [[Northrop Grumman]], [[L3Harris]]
- Defense + space ETFs — [[ITA]], [[XAR]]

### Private comparables
- [[SpaceX]] — dominant private peer; IPO June 2026
- [[Vast Space]] — private, commercial space stations
- [[Firefly Aerospace]] — direct RKLB competitor; pre-IPO

---

*Created 2026-05-10 from May 8 basket-rally cluster validation. Cluster validation diagnostic migrated from [[Space basket rally May 8 2026]] event note (event keeps the dated narrative; cohort definition + diagnostic live here).*
