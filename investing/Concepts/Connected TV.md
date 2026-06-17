---
aliases: [CTV, Connected Television, streaming TV platform, OTT TV]
---
#concept #streaming #media #advertising

**Connected TV** (CTV) — television content delivered over the internet to a TV screen, via smart-TV operating systems, streaming devices and dongles, and game consoles, as opposed to [[Linear TV|linear]] cable or [[Broadcast TV|broadcast]]. CTV is both a distribution layer and the fastest-growing digital-advertising surface: viewers watch streaming apps on the big screen, and whoever owns the operating system controls the home screen, the ad inventory, and the account relationship.

The platform layer is an oligopoly. [[Roku]] leads US viewing (~44% of US CTV viewing hours, per the [[Fox Corporation]]–Roku deal materials), ahead of [[Amazon]] Fire TV and [[Google]] TV; the smart-TV operating systems of [[Samsung]] (Tizen) and LG (webOS) hold the embedded-OS share, while [[Apple]] TV occupies a premium niche. Ownership of a CTV platform — the gateway between content and the living-room screen — is the strategic logic behind Fox's June 2026 agreement to acquire Roku, pairing Fox's sports/news content with Roku's distribution and ad stack.

## June 2026: the CTV gateway as acquisition target

Fox's agreement to buy Roku put a price on owning the CTV gateway. The market's verdict split the two stocks violently around the June 15 announcement:

![[roku-vs-foxa-deal-divergence.png]]

*ROKU (blue) and [[Fox Corporation|FOXA]] (red), normalized from May 1, 2026. The two tracked together through May; then on the June 12 leak ROKU spiked ~+16% toward the $160 offer while FOXA fell to ~−13.5% on the $8.3B of new debt and 152M new Class A shares funding the deal. The scissor is the cost of acquiring the CTV layer — the buyer pays up for the gateway, and its own equity wears the bill. See [[Roku]] and [[Merger Arbitrage]] for the deal-spread mechanics.*

## Cluster validation

> [!failure] Cluster status: falsified — "streaming/CTV" is not a tradeable factor (Jun 2026)
> The streaming/CTV equity complex ([[Roku|ROKU]], [[Netflix|NFLX]], [[Warner Bros Discovery|WBD]], [[Paramount Skydance|PSKY]], [[Disney|DIS]], [[Trade Desk|TTD]]) does not trade as one factor. Intra-corr is 0.186 (weekly 0.187), PC1 only 33%; the cohort fails the random-basket null (p 0.14) — its cohesion is statistically indistinguishable from a random 6-pick of comparable names. The decisive tell: the cohort correlates more with the market/sector ETFs (0.310) than with itself (0.186) — a negative −0.124 intra-advantage — and [[Roku]] itself clusters with [[SPY]]/XLC/XLY, not its supposed peers. The platform cohort the note names above ([[Amazon]], [[Google]], [[Samsung]], [[Apple]]) is untestable as a stock cluster — CTV is a small segment inside mega-cap conglomerates — so the test uses the streaming-stock complex the market actually buckets together. There is no streaming basket worth holding; the names are single-company subscriber/ad/content stories.

Going in, the question was whether "streaming" — the label that bundles content (SVOD), distribution (CTV platforms), and programmatic ad-tech — is a coherent trading factor. It is not. The business models are too disparate: [[Roku]]'s device/OS installed base and ad platform, [[Trade Desk]]'s demand-side programmatic spend, [[Netflix]]'s global SVOD subscriber engine, and the diversified legacy-media pivots of [[Disney]], [[Warner Bros Discovery]], and [[Paramount Skydance]] (each carrying parks, studios, or linear bundles). The one tight cluster in the universe is the cable control pair ([[Comcast|CMCSA]] + [[Charter Communications|CHTR]], 0.72) — old-media/broadband still coheres; streaming does not.

### Diagnostics summary

| Diagnostic | Value | Read |
|---|---|---|
| Intra-cluster corr (1Y) | 0.186 [−0.149, 0.370] | far below the 0.50 floor; weekly 0.187 |
| PC1 explained variance | 33.2% | weak; variance spread across PC2–PC6 |
| Independence null p | 0.0001 | the series co-move at all (necessary, not sufficient) |
| Random-basket null p | 0.138 (PC1 0.164) | NOT rejected — indistinguishable from a random 6-pick |
| Holdout (2Y split) | REGIME-DEPENDENT, ratio 0.54 | fails out-of-sample; loadings corr 0.34 |
| Threshold clean width | 0.00 | BOUNDARY-DEPENDENT — never a clean cluster; ETFs contaminate every cut |
| Intra-adv vs cable (CMCSA/CHTR) | +0.068 | barely distinct from cable |
| Intra-adv vs ETFs (XLC/XLY/SPY) | −0.124 | negative — closer to the market than to itself |

1Y daily log returns through 2026-06-15, threshold 0.5. Config: `scripts/cluster_configs/roku.yaml`; registry row 2026-06-17. Terminology: [[Cohort, cluster, basket]]. ([[Roku]]'s pending [[Fox Corporation]] acquisition decoupled it further in the final week, but the 6.5-year correlation is unmoved; going forward ROKU trades as [[Merger Arbitrage|merger-arb]], not streaming.)

### Boundary — the primary clusters with the market, not its peers

![[streaming-cluster-dendrogram-1y.png]]
*Hierarchical clustering at 0.5. The only sub-threshold cluster (green) is [[Roku]] + XLC + XLY + [[SPY]] — ROKU's nearest neighbors are the market and sector ETFs. [[Netflix]], [[Warner Bros Discovery]], [[Paramount Skydance]], [[Disney]], and [[Trade Desk]] all hang as separate high-distance branches; the cable pair ([[Comcast]] + [[Charter Communications]]) clusters on its own. No streaming factor.*

### Topology — loose pairs, then nothing

Reading the candidate cohort by join distance (average linkage, 1−|corr|):

| Join step | Names | Distance (1-\|corr\|) | Read |
|---|---|---|---|
| 1 | ROKU + DIS | 0.630 | the tightest intra-cohort join — still far above the 0.50 cut |
| 2 | WBD + PSKY | 0.689 | the legacy-media pair |
| 3 | TTD + (ROKU+DIS) | 0.722 | ad-tech attaches loosely |
| 4 | NFLX + above | 0.817 | Netflix joins higher still |
| 5 | (WBD+PSKY) + rest | 0.838 | the two halves merge only at 0.84 |

No intra-cohort join clears the 0.50 threshold — the first (ROKU+DIS) is already at 0.63, looser than ROKU's join to the ETF block.

### PC1 index weights

![[streaming-cluster-pca-1y.png]]
*PCA on the candidate cohort. PC1 explains only 33.2%, with a long PC2–PC6 tail — a multi-factor cohort, not a single shared driver.*

| Ticker | PC1 loading | Loading weight | Ann vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| [[Roku\|ROKU]] | 0.537 | 22.4% | 46.5% | 19.5% |
| [[Disney\|DIS]] | 0.455 | 19.0% | 26.2% | 29.5% |
| [[Paramount Skydance\|PSKY]] | 0.418 | 17.5% | 55.0% | 12.9% |
| [[Trade Desk\|TTD]] | 0.399 | 16.7% | 54.4% | 12.4% |
| [[Netflix\|NFLX]] | 0.304 | 12.7% | 34.6% | 14.9% |
| [[Warner Bros Discovery\|WBD]] | 0.280 | 11.7% | 43.6% | 10.9% |

The volatility spread (26–55%) is itself a tell — these are not comparable risk objects.

### Distinctness — closer to the market than to itself

![[streaming-cluster-correlation-1y.png]]
*1Y pairwise correlation heatmap. The cohort block is tepid (warmest cell ROKU–DIS at 0.37; NFLX–WBD is negative); the names run warmer against XLC/XLY/SPY than against each other.*

The negative −0.124 intra-advantage versus the ETFs is the cleanest statement of the result: a randomly assembled basket of comparable-cap names would cohere more than this "sector" does. The +0.068 edge over cable is within noise.

### Historical tightness evolution

![[streaming-cluster-rolling-tightness-90d.png]]
*Rolling 90-day cohesion, 2020–2026. Factor-like (~0.50) only in the 2020 COVID streaming boom and the 2022–23 rate-shock streaming selloff; fragmented to ~0.20–0.36 otherwise, and at its loosest (0.198) now.*

| Year | Avg intra-corr | PC1 |
|---|---|---|
| 2020 | 0.494 | 58.3% |
| 2021 | 0.231 | 37.8% |
| 2022 | 0.524 | 60.4% |
| 2023 | 0.513 | 59.8% |
| 2024 | 0.255 | 41.2% |
| 2025 | 0.361 | 49.0% |
| 2026 | 0.198 | 34.8% |

Streaming is the same shock-dependent pattern the [[Restaurants]] cohort shows: a factor only while a common shock dominates — the 2020 lockdown streaming surge and the 2022 profitability-reset selloff bound the names together; absent a shared shock, each reverts to its own subscriber, content, or ad-spend story.

## Quick stats

| Field | Value |
|-------|-------|
| What | Internet-delivered TV on a television screen |
| Displacing | [[Linear TV]], [[Broadcast TV]] |
| US platform leader | [[Roku]] (~44% of CTV viewing hours) |
| Monetization | Advertising — FAST channels, ad-supported streaming |
| Why it matters | The OS owner controls home screen, ad inventory, account data |

## Related

- [[Roku]] — US CTV platform leader
- [[Linear TV]] — the model CTV is displacing
- [[Cord-cutting]] — the secular shift enabling CTV
- [[TV market]] — broader market hub
- [[Platform economics]] — why owning the OS matters
- [[Fox Corporation]] — acquired into CTV via Roku (June 2026)

### Cross-vault
- [Technologies: Connected TV](obsidian://open?vault=technologies&file=Connected%20TV) — the delivery-stack (codecs, ABR, CDNs, smart-TV OSes) and the OS-as-gateway technology lens

---

*Created 2026-06-16*
