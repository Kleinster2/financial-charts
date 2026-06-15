---
aliases: [TKO securities note, TKO securities, TKO stock, TKO Group Holdings stock, TKO shares]
tags: [asset, equity, media, entertainment, sports, usa]
---

# TKO securities

TKO is [[TKO Group Holdings]]'s [[NYSE]]-listed Class A common stock, the trading line for the combined [[UFC]] + [[WWE]] sports and entertainment company since the September 2023 merger that folded UFC into the listed WWE entity and renamed it TKO. The business, media-rights strategy, operations, and financials live in [[TKO Group Holdings]]; this note carries the instrument — the Up-C share structure and control, the listing lineage, the price record, and the peer comparison.

## Quick stats

| Metric | Value |
|---|---|
| NYSE ticker | TKO (since Sep 12 2023) |
| Predecessor listing | WWE on [[NYSE]] — IPO Oct 19 1999 as WWF ($17.00/share), renamed WWE 2002, renamed TKO at the Sep 2023 merger |
| Issuer | [[TKO Group Holdings]], Inc. (Delaware) |
| SEC CIK | 0001973266 (10-K / 10-Q / 8-K domestic filer) |
| Structure | Up-C; Class A (public) + Class B ([[Endeavor]]) |
| Class A shares | 74.96M (Mar 31 2026) |
| Class B shares | 116.16M (Mar 31 2026, [[Endeavor]]) |
| Shares outstanding | ~191.13M |
| Jun 12 2026 close | $203.36 |
| Market cap | ~$38.9B (Jun 12 2026) |
| Control | [[Endeavor]] ~61.7%, itself [[Silver Lake]]-controlled since Mar 2025 |
| Dividend | $3.12/yr, 1.53% yield (initiated Q1 2025, doubled Sep 2025) |
| Buyback | $2.0B authorization (incl. $800M accelerated repurchase) |
| Beta / P/E | 0.62 / ~75x |

## Listing lineage — one continuous NYSE series

The price history runs back to October 19, 1999, but that is WWE's listing, not a separate IPO. World Wrestling Federation Entertainment went public on the [[NYSE]] at $17.00/share under ticker WWF, renamed WWE in 2002 after the World Wide Fund for Nature trademark dispute. When [[Endeavor]] merged UFC into the public WWE company in September 2023, the same legal entity was simply renamed TKO and kept WWE's NYSE listing — so the series is one continuous listing, not a shell stitch. Closes before September 2023 should be read as WWE. Pulled with split/dividend adjustment, the 1999 IPO shows as ~$10.54 rather than the actual $17.00 offer.

## Share structure and control

TKO uses an Up-C (umbrella partnership C-corporation) structure. TKO Group Holdings, Inc. — the public company — holds a controlling interest in TKO Operating Company, LLC (OpCo). Public holders own Class A common stock, which carries economic interest and one vote. [[Endeavor]] holds Class B common stock — votes but minimal PubCo economics — paired one-for-one with OpCo common units that carry the economic interest and are exchangeable into Class A. Endeavor's ~116M Class B shares and matching units represent roughly 61.7% of the combined economic interest, so public Class A holders take economic exposure without control. This differs from a founder-supervote [[Dual-class shares|dual-class]] setup: the second class here is the Up-C exchange mechanism, not a 10-votes-per-share control class.

Control sits one level up. [[Endeavor]] — [[Ariel Emanuel]]'s entertainment group — was taken private by [[Silver Lake]] in a deal that closed March 2025, so TKO's ultimate controller is now Silver Lake through Endeavor. Ariel Emanuel is TKO's Executive Chair.

The controlling stake rose because TKO paid in its own equity for assets: on February 28 2025 TKO acquired [[IMG]], [[On Location]], and [[Professional Bull Riders]] from [[Endeavor]] in an all-equity transaction valued at ~$3.25B, issuing new Class B shares and OpCo units to Endeavor. That moved TKO from a pure UFC + WWE combat-and-entertainment company toward a broader sports-rights, hospitality, and live-experiences platform (business detail in [[TKO Group Holdings]]).

## Price record and peer comparison

![[tko-vs-fwonk-vs-lyv-price-chart.png]]
*TKO (blue) vs LYV ([[Live Nation]]) and FWONK (Formula One Group, a [[Liberty Media]] tracking stock), normalized to TKO's first post-merger trading day (Sep 12 2023). TKO had the deepest early drawdown — about -25% to its early-2024 trough — then re-rated to finish neck-and-neck with Live Nation, both roughly doubling; the Formula One line lagged badly.*

| Series | Read since the merger (Sep 12 2023 → Jun 12 2026) |
|---|---|
| TKO | +108% ($97.62 → $203.36); worst start, strongest finish after the media-rights re-rating |
| LYV ([[Live Nation]]) | +111% ($81.65 → $172.51); live-events peer, dead-heat with TKO |
| FWONK ([[Liberty Media]] Formula One Group) | +31% ($67.87 → $88.93); live-sports-rights peer, the clear laggard |

Despite the high-multiple growth narrative (~75x earnings), TKO's market beta is low at 0.62. Long-dated, contracted media-rights revenue — the UFC and WWE TV/streaming deals — makes the cash flows relatively insensitive to the cycle, which is the structural distinction from more discretionary live-entertainment names like Live Nation. But the peer set is analogy, not a validated cluster — the formal cohort test below falsifies it: TKO does not trade as part of a live-sports/entertainment factor.

## Cluster validation

> [!failure] Cluster status: falsified (Jun 2026)
> Intra-cluster correlation 0.27 (weekly 0.34), PC1 51.5% explained variance. Hierarchical clustering returns all singletons — the only cluster below threshold is the SPY/XLC/XLY ETF block. The random-basket null is NOT rejected (p 0.17): TKO/LYV/FWONK cohesion is indistinguishable from a random 3-pick of comparable names. "Live sports and entertainment rights" is a label, not a return factor — TKO is a [[TKO Group Holdings#Sector correlation|sector orphan]].

The candidate cohort TKO + LYV ([[Live Nation]]) + FWONK ([[Liberty Media]] Formula One Group), tested against a live-sports control (MSG Sports, MSG Entertainment and Manchester United — MSGS/MSGE/MANU), a media control ([[Netflix]], [[Warner Bros Discovery]], Fox), and broad benchmarks (SPY, XLC, XLY), does not trade as one factor. The three names join only at distance 0.675 (TKO+FWONK) and 0.755 (LYV) — both above any reasonable cut — and the only group that clusters is the market-beta ETF block.

![[tko-cluster-dendrogram-1y.png]]
*Hierarchical clustering (1Y, 1−|corr|). TKO, LYV and FWONK are singletons; the sole sub-0.5 cluster is SPY/XLC/XLY (orange). The candidate cohort never forms.*

| Diagnostic | Value | Read |
|---|---|---|
| Intra-corr (1Y daily) | 0.27 | below the 0.50 floor |
| Intra-corr (weekly) | 0.34 | still below floor — not an async artifact (all US-listed) |
| PC1 explained variance | 51.5% | large PC2 (26%) + PC3 (22%) — three near-independent names |
| Hierarchical clustering (0.5) | all singletons | only SPY/XLC/XLY cluster |
| Intra-advantage vs ETFs | −0.01 | the cohesion is just market beta |
| Intra-advantage vs live-sports (MSGS/MSGE/MANU) | −0.01 | no distinct rights factor |
| Intra-advantage vs media (NFLX/WBD/FOXA) | +0.13 | only modestly distinct from streaming |
| Random-basket null | p 0.17 (PC1 0.20) | FAILS — indistinguishable from a random pick |
| Threshold scan | zero stable width | BOUNDARY-DEPENDENT |
| Holdout (2y train/test) | ratio 0.54 | REGIME-DEPENDENT (loadings corr −0.59) |

The negative intra-advantage versus both the ETFs (−0.01) and the live-sports control (−0.01) is the decisive number: TKO/LYV/FWONK correlate no more with each other than with SPY or with MSG / Manchester United, so what little they share is broad market beta, not a "live entertainment" factor. The grouping had a brief moment of cohesion — rolling tightness spiked to 0.46 in 2025 (holdout train half 0.51) before decohering to 0.27 with the factor structure flipping (PC1 loadings correlation −0.59) — regime-dependent noise, not a durable cluster. The economic read matches the [[TKO Group Holdings#Sector correlation|sector-orphan]] finding: TKO's contracted UFC/WWE media-rights cash flows give it a return profile shared with nothing else listed. It is a single-name exposure, not a basket member. Full diagnostics: `scripts/cluster_configs/tko.yaml`; registry row 2026-06-14.

## Related

- [[TKO Group Holdings]] — issuer (UFC + WWE business, media-rights strategy, financials)
- [[UFC]] — core combat-sports asset
- [[WWE]] — core sports-entertainment asset; the NYSE listing lineage
- [[Endeavor]] — controlling shareholder (~61.7%), seller of the Feb 2025 sports assets
- [[Silver Lake]] — controls Endeavor, and thus TKO, since March 2025
- [[Ariel Emanuel]] — Executive Chair
- [[Live Nation]] — LYV, live-events peer in the chart
- [[Liberty Media]] — FWONK (Formula One Group), live-sports-rights peer in the chart
- [[IMG]], [[On Location]], [[Professional Bull Riders]] — assets acquired from Endeavor (Feb 2025)
- [[NYSE]] — listing venue
- [[Dual-class shares]] — related control-structure concept

---

*Created 2026-06-14. Price from canonical `prices_long` (Jun 12 2026 close, $203.36). Class A 74.96M / Class B 116.16M shares as of Mar 31 2026 from TKO's FY2026 Q1 10-Q (SEC CIK 0001973266); ~191.13M total, market cap ~$38.9B. Dividend $3.12/yr (1.53% yield), beta 0.62, P/E ~75x from StockAnalysis (Jun 2026). Acquisition ~$3.25B, closed Feb 28 2025, from TKO 8-K / company release. Endeavor stake ~61.7% from 2026 filings; Silver Lake take-private of Endeavor closed Mar 2025. Instrument note — issuer fundamentals live in [[TKO Group Holdings]].*
