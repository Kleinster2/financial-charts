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

## PC1 factor — the cohort's common driver

PC1 is the synthetic "space pure-play factor" — daily returns projected onto the first principal component of the 7-name cohort. Computing it directly answers two questions: what does the factor look like as a price series, and when did the cohort consolidate from a loose collection of names into a single-factor basket.

Run via `python scripts/chart_pc1_component.py`. Three outputs.

### PC1 vs equal-weighted basket vs benchmarks

![[space-pureplays-pc1-index.png]]
*PC1 factor (blue) tracks an equal-weighted basket (pink) almost identically (0.999 correlation). Both materially outperform [[SPY]] and [[ITA]] over the Jan 2024 → May 8 2026 window.*

The 0.999 PC1-vs-equal-weighted correlation is the cleanest evidence that the cohort really is a single factor. Sophisticated PCA weighting adds essentially nothing over naive 1/N equal-weighting — anyone trying to express this thesis can capture all of PC1's signal with a simple equal-weighted basket of the 7 names.

### PC1 vs individual cohort members

![[space-pureplays-pc1-vs-members.png]]
*PC1 factor (black) overlaid on each of the 7 cohort members. The factor sits roughly in the middle of the cohort's dispersion band — pulled toward whichever names happen to be moving on any given session.*

PC1 loadings ranked by magnitude (full Jan 2024 → May 2026 window):

| Ticker | Loading | Read |
|---|---|---|
| [[Intuitive Machines\|LUNR]] | 0.468 | Highest — most central name to the factor |
| [[AST SpaceMobile\|ASTS]] | 0.398 | High loading |
| [[Spire Global\|SPIR]] | 0.381 | High |
| [[BlackSky\|BKSY]] | 0.378 | High |
| [[Redwire\|RDW]] | 0.351 | Mid-pack |
| [[Rocket Lab\|RKLB]] | 0.350 | Mid-pack despite being the cohort's biggest name by market cap |
| [[Planet Labs\|PL]] | 0.298 | Lowest — most idiosyncratic, least factor-driven |

The LUNR-as-most-central finding is counterintuitive. RKLB is the obvious "biggest name" and the natural anchor by market cap and revenue scale — but RKLB has a heavier idiosyncratic component (Neutron debut binary, Q1 print catalysts) that makes its return path *less* aligned with the broad-cohort factor than LUNR's. LUNR's catalyst path ([[NASA]] [[CLPS]] contracts, lunar communications) sits more squarely inside the Golden-Dome / SpaceX-IPO / war-premium thesis chain that drives the basket. PL at the other end of the spectrum is the constellation-data business model whose revenue cycle ([[NGA]] commercial-imagery contract cadence) decouples from the basket's catalyst chain.

### Cohort cohesion over time — rolling PC1 explained variance

![[space-pureplays-pc1-rolling-variance.png]]
*Rolling 60-day PC1 explained variance, Jan 2025 → May 2026. The cohort flipped regime in mid-to-late November 2025 — PC1 variance jumped from ~50% (loose, multi-factor cohort) to ~68% (single-factor basket) in approximately two weeks, and has held that level since. Latest reading: 70.27%.*

The shape of this chart is the analytical centerpiece. Three regimes:

| Period | PC1 var | Read |
|--------|---------|------|
| Jan-Sep 2025 | 40-50% | Loose cohort. Names trade on idiosyncratic catalysts; no dominant common factor. Equal-weighted basket exposure adds little over single-name selection. |
| Oct-Nov 2025 | 50-55% | Gradual cohesion. PC1 variance rises slowly; cohort beginning to be treated as a basket. |
| Nov 2025 - May 2026 | 65-72% | Single-factor cohort. PC1 dominates. The cohort now trades as one signal. Basket expressions capture most of the cohesion. |

### What caused the November 2025 regime shift

Three concurrent catalysts in October-December 2025 collectively recast the cohort from "seven independent stories" into "the Golden Dome + SpaceX-IPO proxy basket":

1. WSJ reports [[SpaceX]] $2B [[Golden Dome]] satellite-tracking contract (late October 2025). First concrete linkage of [[SpaceX]] to the [[Golden Dome]] program at a publicly known dollar figure. Established the framing that the entire pure-play space cohort was a Golden Dome-adjacent investment thesis.
2. [[Donald Trump|Trump]] executive order to boost the space sector (late 2025). Industrial-policy signal that the administration would treat space as a strategic priority, with regulatory and contracting tailwinds for the cohort.
3. November 29, 2025: USSF awarded first space-based interceptor (SBI) prototype contracts to [[Northrop Grumman]], [[Lockheed Martin]], [[Anduril]], and True Anomaly — $10M each. First formal start of the [[Golden Dome]] interceptor competition. Made the multi-billion-dollar production-contract pipeline (~$1.8-3.4B/year per the prize structure) a calculable near-term TAM rather than a hypothetical.

The rapid follow-on through December reinforced the regime: $151B SHIELD multi-vendor IDIQ awarded with 2,100 awardees (Dec 2025), [[Elon Musk|Musk]] confirms 2026 SpaceX IPO as "accurate" (Dec 11 2025), and [[NVIDIA]] $5B Intel partnership (Jan 2026) anchored adjacent tech-defense flows.

The PC1 variance jump is the equity-market expression of "institutional capital decided this is a basket, not a list of names." Before Nov 2025, the cohort moved on idiosyncratic news (a single name's earnings, a single contract win). After Nov 2025, the cohort moves on cohort-level catalysts (SpaceX IPO timing, Golden Dome contract awards, war-premium repricing). The May 8 2026 basket rally is the most extreme example of the post-regime-shift dynamic — every name participated despite no shared earnings catalyst because the cohort *is* the unit now.

The fact that PC1 explained variance has held in the 65-72% band for six months without reverting argues the regime change is durable, not a momentary squeeze. Watch for: PC1 variance dipping back below 60% would signal the basket is fragmenting again (single-name catalysts re-asserting); PC1 variance pushing above 75% would signal further consolidation (basket trading dominating completely).

*Sources: [SatNews — USSF awards initial Golden Dome prototype contracts](https://news.satnews.com/2025/12/01/ussf-awards-initial-golden-dome-prototype-contracts-signaling-strategic-shift-to-space-based-defense/); [Breaking Defense — Space Force awards first SBI prototype contracts](https://breakingdefense.com/2025/11/golden-dome-space-force-awards-first-space-based-boost-phase-interceptor-prototype-contracts/); [CNBC — Musk says SpaceX 2026 IPO report 'accurate'](https://www.cnbc.com/2025/12/11/musk-says-spacex-report-of-2026-ipo-is-accurate.html); [Benzinga — Space stocks Trump executive order](https://www.benzinga.com/news/space/25/12/49590418/); local `scripts/chart_pc1_component.py` Nov 2025-May 2026 rolling PC1 series.*

---

## May 8 2026 — factor vs idiosyncratic decomposition

Worked example of how PC1 decomposes a specific session. For each name on May 8, project its actual return into a factor component (PC1 loading × PC1 score for the day) and an idiosyncratic residual. Tells us which names participated as the factor predicted and which moved more or less.

Run via `python scripts/may8_factor_decomposition.py`. PC1 score on May 8: 0.473 (high — the factor itself had a big day).

| Ticker | Actual | Factor (predicted) | Idiosyncratic | Idio share | Read |
|---|---|---|---|---|---|
| [[Rocket Lab\|RKLB]] | +34.2% | +20.3% | +11.6pp | 37% | Q1 print + Motiv + Golden Dome SBI catalyst layered on top of basket factor |
| [[BlackSky\|BKSY]] | +22.4% | +14.7% | +6.7pp | 32% | Bounce off the May 7 -25% selloff; technical idiosyncratic recovery |
| [[Redwire\|RDW]] | +20.3% | +21.7% | -1.1pp | 5% | Almost pure factor participation; nearly perfect basket fit |
| [[Intuitive Machines\|LUNR]] | +20.2% | +22.4% | -1.8pp | 8% | Pure factor participation; the canonical "moved exactly as the factor predicted" name |
| [[AST SpaceMobile\|ASTS]] | +14.8% | +20.1% | -4.4pp | 20% | Factor-aligned but under-performed; FCC+Falcon 9 catalysts didn't add residual alpha |
| [[Spire Global\|SPIR]] | +14.6% | +18.6% | -3.4pp | 17% | Slight underperformance — consistent with SPIR's data-business PC2-positive sleeve |
| [[Planet Labs\|PL]] | +10.8% | +18.3% | -6.4pp | 28% | Biggest underperformance; PL has the lowest factor coupling (PC1 loading 0.30) AND was idiosyncratically weak |

Basket equal-weighted move: +19.4%. Factor model predicted the basket would rise ~+20% on May 8 given the PC1 score, and that's almost exactly what the equal-weighted basket delivered. The dispersion within the basket (+10.8% to +34.2%, a 23pp spread) was wider than the factor predicts — most of that cross-sectional spread is idiosyncratic.

Three structural reads from the decomposition:

1. RKLB's +34% was approximately 60% factor / 40% idiosyncratic. The "right" base case for a Rocket Lab earnings beat layered on top of basket participation would have been ~+20% — that's what an equal-weighted-basket holder captured. The additional +11.6pp is the unique Rocket Lab Q1 / Motiv / Golden Dome catalyst stack. A trader expressing the cohort thesis via basket exposure captured the +20% factor move; a trader expressing the thesis via RKLB single-name captured the additional Q1-print alpha.
2. RDW and LUNR are pure-factor-participation names on May 8. Their actual moves (+20.3%, +20.2%) matched their factor-implied moves (+21.7%, +22.4%) to within 2pp. They had no idiosyncratic news; they simply rode the basket. This is the canonical pattern for "factor exposure as the dominant return component."
3. PL's underperformance (-6.4pp idiosyncratic) compounds its already-low PC1 loading (0.30 — lowest in the cohort). PL is consistently the cohort's weakest factor participant — both in cumulative return (lowest in the basket at ~+800% vs RKLB ~+1700%) and in single-day factor matching. That argues PL is the closest thing the cohort has to a "structural laggard" — useful information for thinking about within-basket pair trades.

The narrow window decomposition validates the broader factor framework: the basket factor is real and predictive, and the within-cluster dispersion on any given day is driven by idiosyncratic name-specific catalysts (RKLB's earnings, BKSY's bounce, PL's underperformance) layered on top of the common factor.

---

## Factor decomposition — what's left after stripping out SPY / IWM / ITA

The cluster validation diagnostic confirms the cohort trades together (intra-correlation 0.62, PC1 67%). The next question is harder: *is the cohort just leveraged small-cap defense beta, or is there a genuine pure-play factor that doesn't show up in existing tradeable exposures?*

Run via `python scripts/cluster_deep_dive.py`. Regression of equal-weighted basket returns on [[SPY]] + [[IWM]] + [[ITA]] over the trailing 1Y (134 observations through 2026-05-07):

| Metric | Value |
|---|---|
| R² (variance explained by SPY / IWM / ITA) | 40.4% |
| Residual variance (pure-play factor) | **59.6%** |
| Annualized alpha | +58.4% |

Beta loadings:

| Factor | Beta | Read |
|---|---|---|
| [[SPY]] | -0.12 | Essentially zero or slightly negative — the cohort does NOT move with broad market |
| [[IWM]] | +2.15 | Heavy small-cap beta — these names are small-cap by definition |
| [[ITA]] | +0.70 | Moderate defense beta — Golden Dome exposure routes through here partially |

The 59.6% residual variance is the load-bearing finding. After stripping out *all* tradeable benchmark exposure (broad market + small-cap + defense), nearly 60% of the cohort's daily-return variance remains unexplained — and that residual is the "space pure-play factor" itself. The cohort is NOT a slice of [[IWM]] + [[ITA]]; it has a distinct factor that doesn't trade as a single tradeable instrument and therefore the 7-name basket is the only way to express it.

Per-name R² to SPY / IWM / ITA:

| Ticker | R² | Residual (name-specific + cohort factor) |
|---|---|---|
| RKLB | 43.3% | 56.7% — most benchmark-exposed name |
| LUNR | 31.0% | 69.0% |
| SPIR | 28.2% | 71.8% |
| ASTS | 27.6% | 72.4% |
| RDW | 26.8% | 73.2% |
| BKSY | 23.9% | 76.1% |
| PL | 17.0% | 83.0% — most idiosyncratic name, lowest benchmark coupling |

The PL R² of only 17% confirms again that Planet Labs is the cohort's most independent name — its return path is 83% name-specific or cohort-specific, almost nothing comes from broad market or defense beta. PL is the cleanest "pure space-data business" expression.

The +58% annualized alpha is the trailing-year reading and will mean-revert; alpha at this level is a feature of the post-Nov-2025 regime shift, not a permanent return premium. The structural argument is about the *residual variance* (59.6% pure-play factor share), not the alpha — the residual share is what tells you the cohort identity is durable beyond benchmark leverage.

---

## PC2 sub-structure — data businesses vs hardware businesses

PC1 explains 67% of cohort variance (the "everyone moves together" factor). PC2 explains an additional 8.9% — modest, but the *loadings* reveal a clean structural split between two sleeves within the cohort.

PC2 loadings (positive vs negative is the relevant axis — these are the second-eigenvector weights):

| Ticker | PC2 loading | Sleeve |
|---|---|---|
| SPIR | +0.78 | Data sleeve (most extreme — canonical) |
| PL | +0.23 | Data sleeve |
| BKSY | +0.17 | Data sleeve |
| ASTS | -0.22 | Hardware sleeve |
| RKLB | -0.23 | Hardware sleeve |
| LUNR | -0.28 | Hardware sleeve |
| RDW | -0.35 | Hardware sleeve |

The split is essentially "data businesses vs hardware/launch businesses":

| Sleeve | Names | Business model |
|---|---|---|
| Data (PC2 positive) | [[Spire Global\|SPIR]], [[Planet Labs\|PL]], [[BlackSky\|BKSY]] | Sell space-derived data (RF, weather, imagery) — software-margin profile, recurring revenue, no launch-cycle risk |
| Hardware (PC2 negative) | [[Rocket Lab\|RKLB]], [[Redwire\|RDW]], [[Intuitive Machines\|LUNR]], [[AST SpaceMobile\|ASTS]] | Build / launch / operate physical assets — hardware-margin profile, capex-heavy, binary launch-cycle risk |

This is the analytical justification for the "soft cluster" finding when we first looked at it (the RDW-PL pairwise correlation of 0.49 was the loosest in the matrix). PC2 captures the residual after the common factor — and the residual is precisely the data-vs-hardware divide. SPIR's +0.78 loading is anomalously high, which makes SPIR the canonical data-sleeve expression (whatever pure-RF-data-business-trading-on-its-own-catalyst-path means, SPIR is its purest form).

Investment relevance: PC2 is the natural pair-trade axis within the cohort. Long the data sleeve / short the hardware sleeve is a play on "software-margin economics over hardware-margin economics" within space; the reverse is a play on "launch-cycle + Golden Dome production contracts over data-business multiples." Neither direction is endorsed here — flagging the structure, not the trade.

---

## Missing-name screen — does the cohort have the right boundary?

The validated 7-name cohort is the candidate set defined a priori. The boundary test: are there other tickers in the local universe that *also* belong in the cluster but were excluded?

Run via `cluster_deep_dive.py`. Average correlation to the validated 7-name cohort over the trailing 1Y:

| Candidate | Actor | Avg corr | Verdict |
|---|---|---|---|
| [[Kratos]] (KTOS) | Defense-tech: drones, missiles, hypersonic | 0.523 | JOIN cluster (above 0.50 threshold) |
| [[AeroVironment]] (AVAV) | UAS, loitering munitions | 0.485 | MAYBE (just below threshold) |
| [[Iridium Communications]] (IRDM) | Satellite communications (large-cap) | 0.312 | Exclude — different beta profile |
| [[Destiny Tech100]] (DXYZ) | SpaceX proxy + closed-end private-tech basket | 0.280 | Exclude — confirms DXYZ is NOT a clean space-pure-play proxy despite the Friday May 8 +21% move |
| [[Momentus]] (MNTS) | Orbital transfer micro-cap | 0.118 | Exclude — too idiosyncratic |
| KARO | (not in local DB) | — | — |
| SIDU | (Sidus Space — micro-cap) | — | (not in local DB) |

The most surprising finding is [[Kratos]] (KTOS) at 0.523 — Kratos is conventionally classified as a defense-tech name (drones, missiles, ground systems), not space. But its return profile correlates with the space pure-play cohort more than any of the other tested candidates. Plausible explanation: Kratos has substantial space-segment exposure (target drones, hypersonic systems, satellite servicing experiments) that traders implicitly bucket alongside the pure-play cohort, and the broader "Golden Dome / defense-tech / non-prime defense" theme bridges the two categories.

[[Destiny Tech100]] (DXYZ) at 0.28 is the most diagnostic exclusion. DXYZ was up +21.3% on May 8 alongside the cohort, so the casual read might be "DXYZ is the public SpaceX proxy + space cohort member." The full-year correlation says otherwise — DXYZ trades on its own private-tech-basket NAV dynamics most of the time, and only co-moves with the space cohort on specific SpaceX-IPO catalyst days. DXYZ is a tactical-event-co-mover, not a structural cluster member.

Decision on KTOS: not added to the validated cohort yet, because (a) KTOS's primary classification is defense-tech, not space pure-play, and (b) including it would broaden the cluster identity from "space pure-plays" to "Golden-Dome-tied small-mid-cap defense-tech," which changes the analytical proposition. AVAV at 0.485 reinforces this — the second-highest correlation is also a defense-tech name. See the falsified-hypothesis section below for the test of whether the broader Golden-Dome-thematic super-cluster actually exists.

---

## Minimum-name expressions — what's the smallest basket that replicates the factor?

If the cohort's value is its single-factor structure (PC1 = ~68% of variance, PC1 ≈ equal-weighted basket at 0.999 correlation), the natural follow-on question is: do you need all 7 names to capture the factor, or does a tighter 2- or 3-name subset deliver essentially the same exposure with less complexity?

Run via `python scripts/cluster_subset_optimization.py`. Tested every 2-name and 3-name subset against the full equal-weighted basket. Diagnostic: correlation of subset returns to basket returns + annualized tracking error.

### Top 5 2-name subsets

| Pair | Correlation to basket | Tracking error |
|---|---|---|
| LUNR + BKSY | 0.9422 | 35.5% |
| BKSY + ASTS | 0.9367 | 34.9% |
| RKLB + BKSY | 0.9365 | 33.3% |
| RKLB + SPIR | 0.9301 | 32.7% |
| LUNR + ASTS | 0.9292 | 37.7% |

LUNR + BKSY is the cleanest 2-name expression — lunar/space-services + earth observation captures 94% of the basket's daily-return variance. Notably:

- BKSY appears in 3 of the top 5 pairs, making it the most consistent factor anchor in the cohort
- LUNR is the second most-frequent (highest PC1 loading, as established earlier)
- Initial intuition that RDW + LUNR would be a clean expression turned out to be wrong — that pair is 4-5th tier (0.926 correlation), not best. RDW's PC1 loading is mid-pack and its idiosyncratic SHIELD-task-order catalyst path makes it a less stable factor proxy than BKSY

### Bottom 3 2-name subsets (worst factor proxies)

| Pair | Correlation to basket | Why |
|---|---|---|
| SPIR + PL | 0.8660 | Both in the data sleeve (PC2 positive); high mutual correlation but lower cohort coupling |
| BKSY + PL | 0.8999 | Also both data-leaning |
| BKSY + SPIR | 0.9018 | Same data-sleeve issue |

The worst proxies are all combinations of data-sleeve names — confirming the PC2 sub-structure. Picking two PC2-positive names gives you the worst factor expression because you concentrate one sub-cluster and underweight the other.

### Top 5 3-name subsets

| Triple | Correlation to basket | Tracking error |
|---|---|---|
| LUNR + BKSY + ASTS | 0.9671 | 25.8% |
| RDW + LUNR + BKSY | 0.9661 | 26.0% |
| RKLB + LUNR + BKSY | 0.9618 | 26.6% |
| RKLB + LUNR + SPIR | 0.9605 | 25.3% |
| RKLB + BKSY + ASTS | 0.9602 | 25.9% |

LUNR + BKSY + ASTS is the cleanest 3-name expression — lunar + earth observation + sat-comms covers the basket factor at 96.7% correlation. Each name picks up a distinct part of the cohort signal (LUNR = lunar / space services factor anchor, BKSY = earth observation, ASTS = sat-comms / consumer space). The 3-name basket cuts tracking error from 35.5% (2-name) to 25.8% — a meaningful improvement that justifies the third name.

The notable absence of RKLB from the top-correlation 3-name subset is the most interesting finding. RKLB is the cohort's biggest market-cap name and the canonical bellwether — but its idiosyncratic component (Neutron-debut binary, Q1 print catalysts) makes it a *less* clean factor proxy than other names. For factor-exposure purposes, RKLB carries more name-specific noise than its peers; for single-name-alpha purposes, RKLB is the cohort's best single-stock catalyst stack. The right expression depends on which kind of exposure the buyer wants.

### Practical implication

A 2-name LUNR + BKSY basket captures 94% of the cohort factor with two-name simplicity. A 3-name LUNR + BKSY + ASTS basket captures 96.7%. The remaining 3-4% of factor variance requires holding the full 7-name basket. The cost-benefit tradeoff depends on whether the user wants the cleanest possible factor exposure (7 names) or operational simplicity (3 names captures essentially everything).

For pair trades or hedges that need factor exposure but want to minimize position count, LUNR + BKSY + ASTS is the right answer. For position-sizing tests of the cluster thesis at single-name granularity, the full 7-name basket remains optimal.

---

## LUNR + BKSY robustness — is the outperformance consistent, or is it a 1Y artifact?

The trailing 1Y comparison (above) showed LUNR + BKSY beat the 7-name basket by 76pp on cumulative simple return. The natural follow-up: is that outperformance real across windows, or concentrated in the recent period?

Lookback comparison (annualized Sharpe + cumulative simple return):

| Window | LUNR+BKSY Sharpe | Basket Sharpe | LUNR+BKSY cum | Basket cum |
|---|---|---|---|---|
| 3M (Feb-May 2026) | 1.91 | 1.47 | +69.0% | +39.8% |
| 6M (Nov 2025-May 2026) | 1.84 | 1.61 | +165.4% | +107.7% |
| 1Y (May 2025-May 2026) | 1.74 | 1.43 | +246.8% | +134.4% |
| 2Y (May 2024-May 2026) | 1.35 | 1.33 | +242.3% | +178.1% |

LUNR + BKSY outperformed the full basket on cumulative return AND Sharpe across all four lookback windows. The Sharpe gap narrows from +0.44 (3M) to +0.02 (2Y) as the window expands, but the cumulative-return gap holds at ~64pp across 1Y and 2Y. The outperformance is robust over time, not concentrated in any single quarter.

Rolling 60-day diagnostic:

| Metric | Value |
|---|---|
| % of rolling 60-day windows with LUNR+BKSY > basket | 77.8% |
| Best 60-day spread (LUNR+BKSY over basket) | +26.2% (window ending 2025-09-30) |
| Worst 60-day spread | -8.6% (window ending 2025-12-11) |
| Average 60-day spread | +7.8% |

77.8% of 60-day rolling windows had LUNR+BKSY outperforming — a strong majority but not universal. The single worst window (ending Dec 11 2025) is the regime-shift period when [[Rocket Lab|RKLB]] led the post-drawdown rally on the [[Golden Dome]] SBI announcement (Nov 29) + [[SpaceX IPO 2026|SpaceX IPO]] confirmation (Dec 11). That window saw the cohort's complement names (especially RKLB) rally harder than LUNR/BKSY. The structural read: LUNR+BKSY underperforms specifically when the cohort's biggest single-name catalysts land on names *outside* the pair, but outperforms in all other regimes.

![[lunr-bksy-robustness-vs-complement.png]]
*Top: cumulative simple return for LUNR+BKSY (blue), full 7-name basket (black), and 5-name complement (red dashed). Bottom: rolling 60-day spread of LUNR+BKSY vs full basket — blue shading where pair outperformed, red where it underperformed.*

---

## Complement test — the 5 names WITHOUT LUNR/BKSY

The cleanest test of "does LUNR+BKSY actually capture the cohort's best returns" is the complement: build a 5-name basket of everything EXCEPT LUNR and BKSY (RKLB, RDW, ASTS, SPIR, PL), and compare. 1Y window:

| Metric | LUNR+BKSY (2) | Full basket (7) | Complement (5) |
|---|---|---|---|
| Cumulative return | +246.8% | +134.4% | +100.5% |
| Annualized vol | 103.1% | 86.0% | 82.9% |
| Sharpe (rf=0) | 1.74 | 1.43 | 1.21 |
| Max drawdown | -47.3% | -42.4% | -41.1% |
| Best single day | +20.9% | +17.7% | +17.1% |
| Worst single day | -15.8% | -11.2% | -10.2% |

Clean monotonic ordering: LUNR+BKSY > Full 7 > Complement (5) on cumulative return AND Sharpe.

The complement basket (RKLB+RDW+ASTS+SPIR+PL) underperformed the full basket by 34pp cumulative and the LUNR+BKSY pair by 146pp. Sharpe is also lower (1.21 vs 1.43 full vs 1.74 pair). This directly confirms that LUNR and BKSY are the Sharpe-enhancing names in the cohort — removing them from the basket drops both return and risk-adjusted return materially.

Per-name 1Y cumulative return, ranked:

| Rank | Ticker | 1Y return | In LUNR+BKSY? |
|---|---|---|---|
| 1 | LUNR | +266.0% | yes |
| 2 | PL | +241.9% | complement |
| 3 | BKSY | +228.5% | yes |
| 4 | RKLB | +202.4% | complement |
| 5 | ASTS | +61.8% | complement |
| 6 | SPIR | +56.3% | complement |
| 7 | RDW | +23.8% | complement |

LUNR (#1) and BKSY (#3) are both top-quartile individual performers. PL is the cohort's #2 performer but is in the complement basket — confirming that the "factor-clean pair" selection captured the cohort's best-by-cumulative-return names imperfectly. PL has the LOWEST PC1 loading (0.30) — its high cumulative return came from idiosyncratic catalysts ([[NGA EOCL contract|NGA contract]] expansion, Pelican-3 constellation launches) rather than basket-factor exposure. The optimization for "factor-tracking" passed over PL because PL doesn't track the factor cleanly, even though it delivered top returns.

Three structural reads:

1. Factor-clean is NOT the same as alpha-clean. LUNR+BKSY captures 94% of the factor (per minimum-name analysis above) AND happens to include the cohort's #1 and #3 cumulative-return names. That dual fit is not coincidental but it's not guaranteed either — PL is the counter-example, a high-return name with low factor-loading. The fact that the factor-tracking pair captured 2 of the 3 top return names is a feature of the current cohort dynamics, not a universal property of factor-tracking.
2. The complement basket's drag is mostly in three names — ASTS, SPIR, RDW. The cohort's three weakest performers (all returning below 65% over 1Y) drag the 7-name basket down meaningfully relative to the LUNR+BKSY concentrated pair. For someone deciding whether to add the complement names to a LUNR+BKSY core position, the question is whether those three names' future return profiles will improve (catch-up trade) or whether they're structurally lagging (factor exposure dilution).
3. The LUNR+BKSY pair's outperformance is not just two strong names being lucky — it's a Sharpe-enhancement effect that holds across all four lookback windows. The complement basket's Sharpe (1.21) is meaningfully below both the pair (1.74) and the full basket (1.43). LUNR and BKSY are doing real work in lifting the cohort's risk-adjusted return.

The cleanest practical conclusion: if expressing the space pure-play factor as a tradeable position, the LUNR+BKSY 2-name pair has been a better expression than the full 7-name basket across all tested windows AND has been better than holding the cohort minus those two names. The 5-name complement basket is the worst of the three options.

This finding sharpens the cluster-validation framework. The standard validation asks "does the cohort cluster as a single factor?" — answered yes. The deeper question is "within a validated cluster, which sub-set captures the most factor return per unit of risk?" — answered LUNR+BKSY. Both questions matter for actual trading expression of the thesis.

---

## How Space pure-plays compares to other validated clusters

The cohort's intra-correlation 0.624 and PC1 67.2% are meaningful diagnostics in absolute terms — but the deeper question is how they rank among the vault's other validated clusters. Putting [[Space pure-plays]] on the same diagnostic axis as the canonical Semiconductors children + Boutique Advisory cohort:

| Cluster | Vault note | Avg intra-corr | Tightness verdict |
|---|---|---|---|
| WFE oligopolists | [[Sectors/WFE\|WFE]] | 0.83 | Tightest validated cluster in the vault — same customers, same capex cycle |
| US Memory | [[Sectors/US Memory\|US Memory]] | 0.70 | Tight — MU/SNDK/WDC trade as cyclical memory exposure |
| Semiconductor Materials | (sub-concept) | 0.65 | Tight — Japan/Korea chokepoints |
| Space pure-plays | [[Space pure-plays]] | 0.624 | Moderately tight — between US Memory and AI Compute |
| AI Compute | [[Sectors/AI Compute\|AI Compute]] | 0.58 | Moderately tight — TSMC + NVDA/AMD as foundry-customer cluster |
| Korea Memory | [[Sectors/Korea Memory\|Korea Memory]] | 0.53 | Moderate — SK Hynix + Samsung HBM-dominant |
| Sensors | (sub) | 0.50 | Moderate — image sensors + MEMS |
| Semiconductor Test | (sub) | 0.46 | Moderate — narrower than WFE |
| Memory (overall) | [[Sectors/Memory\|Memory]] | 0.38 | Loose — splits into US/Korea sub-clusters |
| Connectivity | (sub) | 0.34 | Loose — Broadcom/Qualcomm/Marvell less coupled |
| Korea AI chips | (sub) | 0.30 | Loose — emerging Korean accelerator names |

Space pure-plays at 0.624 sits in the "moderately tight" band — tighter than the AI Compute foundry-customer cluster (0.58), tighter than both memory regional clusters (0.50 / 0.53), but materially less tight than WFE (0.83) or US Memory (0.70). The verdict is "real cluster with meaningful internal cohesion, but not the vault's tightest factor."

The 1Y PC1 explained variance (67%) is also moderately strong compared to the canonical semi clusters where PC1 figures are published — WFE's PC1 likely sits in the 75-85% band given its 0.83 avg correlation; Space pure-plays' 67% is consistent with its 0.62 intra-correlation. The diagnostic numbers align (tighter average correlation generally implies higher PC1 variance share).

Important caveat: cluster-validation methodology has not been uniform across vault notes. Some clusters used a 1Y window, others used longer or unspecified windows. The Semiconductors hub's avg-correlation table (cited above) is the most recent canonical reference, from the May 9 2026 sector-internal-correlation diagnostic. For a fully rigorous cross-cohort comparison, re-running `cluster_analysis.py` with the same window-end + same threshold on every cohort would be the next step — that work is deferred for now.

Three observations from the ranking:

1. The space pure-plays cohort is denser than the AI hyperscaler-customer cluster ([[AI Compute]]) despite [[AI Compute]] being widely treated as the canonical AI-trade. The two clusters serve different theses (Golden Dome / SpaceX-IPO for space; foundry-AI capex for AI Compute) and the math says space has tighter internal cohesion.
2. The cohort's [[#Pre/post Nov 2025 regime — quantifying the structural shift|post-regime intra-correlation of 0.656]] (Dec 2025-May 2026) would bump Space pure-plays above US Memory (0.70 average) if the post-regime period were extrapolated forward. The current 1Y average is dragged down by pre-regime months; the structural read is that current cohesion is in the "tight" rather than "moderately tight" band.
3. Vault clusters cluster (meta-observation): the validated cohorts span 0.30-0.83 intra-correlation, with most semi clusters in the 0.50-0.70 band. Space pure-plays falls within the canonical-cluster range — it's a comparable analytical object, not an outlier. The vault's cluster framework generalizes to a thematic basket outside semis.

---

## Pre/post Nov 2025 regime — quantifying the structural shift

The rolling PC1 chart showed a step-function shift in cohort cohesion in mid-to-late November 2025. The natural follow-up: run full cluster validation on each sub-period separately and quantify exactly how much the cohort changed.

Run via `python scripts/cohort_regime_and_events.py`. Pre-regime window: Nov 12 2024 - Oct 31 2025 (81 observations). Post-regime window: Dec 1 2025 - May 8 2026 (110 observations).

| Diagnostic | Pre-regime | Post-regime | Change |
|---|---|---|---|
| Intra-cluster avg correlation | 0.466 | 0.656 | +0.191 |
| Intra-correlation range | [0.06, 0.68] | [0.50, 0.79] | Floor lifted from 0.06 to 0.50 |
| PC1 explained variance | 51.9% | 71.2% | +19.3pp |
| PC2 explained variance | 21.2% | 7.9% | -13.3pp |
| Cumulative log return | +19.0% (11 months) | +83.2% (5 months) | ~9x annualized acceleration |

The PC2 collapse from 21.2% to 7.9% is the most analytically important finding. Pre-regime, the cohort had a clear two-factor structure — PC1 captured the common direction (52% of variance) and PC2 captured the data-vs-hardware sub-structure (21%). Post-regime, PC2 collapsed to 8% — the secondary factor essentially disappeared. Translation: pre-regime, the data sleeve ([[Spire Global\|SPIR]]/[[Planet Labs\|PL]]/[[BlackSky\|BKSY]]) and hardware sleeve ([[Rocket Lab\|RKLB]]/[[Redwire\|RDW]]/[[Intuitive Machines\|LUNR]]/[[AST SpaceMobile\|ASTS]]) traded as distinguishable sub-cohorts; post-regime, they collapsed into a single basket.

The intra-correlation floor lifting from 0.06 to 0.50 is also structurally important. Pre-regime, the minimum pairwise correlation was effectively zero — at least one pair of names had no relationship. Post-regime, every pair correlates at 0.50+. There are no more "uncorrelated" pairs within the cohort.

Three structural reads from the regime change:

1. The cohort identity was constructed in Nov-Dec 2025, not gradually accumulated. The 60-day vol regime check (below) confirms that the cohort's volatility didn't change — only its internal correlation structure did. That's the signature of a *narrative regime change* (institutional capital re-categorizing the names as a single basket) rather than a *fundamental regime change* (the underlying businesses becoming more similar). The businesses didn't change; the way the market trades them changed.
2. The data-vs-hardware PC2 sub-structure was a pre-regime feature, not a post-regime feature. Anyone reading the PC2 analysis as "this is how the cohort fundamentally splits" should adjust — PC2 has weakened materially since the regime shift. The data sleeve / hardware sleeve framing remains useful for *characterizing* the cohort but the spread between them has compressed significantly. The PC2 pair-trade Sharpe of 0.23 (per backtest below) reflects this compression — the spread is realized but episodic, dominated by pre-regime variance.
3. The post-regime cumulative-return acceleration (+19% over 11 months → +83% over 5 months) implies the cohort isn't just trading more correlated — it's also trading more bullishly. The same November 2025 catalysts that lifted PC1 variance also lifted the absolute return path. The factor became more coherent AND more upward-sloped at the same time, suggesting institutional flow into the basket was net positive in addition to becoming more correlated.

The cleanest summary: the cohort is structurally a different equity basket post-Nov 2025 than it was before. Cluster validation diagnostics on the post-regime window are the load-bearing references for current investment decisions; pre-regime diagnostics are historical context.

---

## Best Sharpe 2-name pair — diversification beats factor-tracking

The minimum-name expression analysis (above) optimized for *factor-tracking correlation to the full basket*. A different objective — *maximum Sharpe ratio* — yields a different optimal pair. Running the same 21-pair enumeration optimized for Sharpe over the trailing 1Y:

| Rank | Pair | Sharpe | Cum return | Vol | Basket correlation |
|---|---|---|---|---|---|
| 1 | RKLB + PL | 2.03 | +221.5% | 82.7% | 0.908 |
| 2 | LUNR + PL | 2.01 | +253.7% | 90.6% | 0.909 |
| 3 | BKSY + PL | 1.89 | +235.1% | 92.0% | 0.896 |
| 4 | RKLB + LUNR | 1.78 | +232.7% | 97.0% | 0.923 |
| 5 | LUNR + BKSY | 1.74 | +246.8% | 103.1% | 0.939 (the factor-tracking optimum) |
| ... | ... | ... | ... | ... | ... |
| 19 | ASTS + SPIR | 0.71 | +59.0% | 93.5% | 0.909 |
| 20 | RDW + ASTS | 0.51 | +41.5% | 97.4% | 0.906 |
| 21 | RDW + SPIR | 0.51 | +39.1% | 93.7% | 0.906 |

The top-Sharpe pair is RKLB + PL (2.03), not LUNR + BKSY (1.74, ranked 5th). The three highest-Sharpe pairs all include [[Planet Labs|PL]]. The structural reason: PL has the lowest PC1 loading (0.30) and the lowest basket correlation in its pairs (~0.91) — which means its returns are the most independent from the factor names' returns. PL paired with high-loading names provides idiosyncratic diversification that reduces overall vol while preserving cumulative return.

The bottom-Sharpe pairs are all RDW combinations (RDW+SPIR, RDW+ASTS) plus ASTS+SPIR. These are the cohort's three weakest individual performers paired together — concentrated weakness with no diversifying counterweight.

The implication is that there are at least three different "optimal 2-name pairs" depending on the optimization objective:

| Objective | Optimal pair | Headline metric |
|---|---|---|
| Maximum factor-tracking correlation | LUNR + BKSY | 0.9422 correlation to basket |
| Maximum cumulative return | LUNR + PL | +253.7% cum return |
| Maximum Sharpe ratio | RKLB + PL | 2.03 Sharpe |

A trader expressing the cohort thesis can pick the pair that matches their objective. The factor-clean LUNR+BKSY pair is the right answer for "I want maximum factor exposure with minimum tracking error." But RKLB+PL is the right answer for "I want the highest risk-adjusted return on this thesis." LUNR+PL is the right answer for "I want the highest cumulative return on the thesis."

PL's presence in two of the three optima (and high ranking on the third) makes it the most analytically interesting individual name in the cohort. PL doesn't track the factor, but it consistently improves whatever portfolio it joins through idiosyncratic diversification.

---

## Event-study decomposition — what drove the basket on specific days

The May 8 factor decomposition (above) applied the framework to a single session. Running the same decomposition for a set of key catalyst days across the 1Y window reveals which events were factor-driven vs idiosyncratic.

PC1 score quantifies the magnitude of the basket factor on a given day; basket return is the equal-weighted average. Both can be positive (cohort rallies, factor up) or negative (cohort sells off, factor down).

| Date | Basket % | PC1 score | Catalyst |
|---|---|---|---|
| 2026-05-08 | +19.4% | +0.473 | RKLB Q1 + Motiv + Golden Dome SBI (basket rally) |
| 2025-12-11 | +9.0% | +0.204 | Musk confirms 2026 SpaceX IPO 'accurate' |
| 2026-03-25 | +8.7% | +0.218 | SpaceX IPO filing reportedly imminent (The Information) |
| 2026-04-10 | +5.5% | +0.142 | Anthropic Managed Agents selloff (SaaS shock — cohort rallied counter to SaaS) |
| 2025-11-17 | -3.6% | -0.099 | Cohort drawdown trough |
| 2025-12-01 | -4.6% | -0.127 | USSF Golden Dome SBI awards (already priced in) |
| 2026-02-27 | -5.7% | -0.156 | Iran war / Operation Epic Fury kicks off |
| 2026-05-07 | -10.3% | -0.289 | Cohort drawdown the day before RKLB earnings |

Three readings from the event-study table:

1. The SpaceX IPO confirmation day (Dec 11) produced a +9% basket move and PC1 +0.20 — a strong factor-driven up day. Compare to the Golden Dome SBI awards day (Dec 1) which produced -4.6% — already priced in by the late-October leak. The cohort didn't rally on the formal contract announcements; it rallied on the framework signals before them and on confirmations like the SpaceX IPO that opened a fresh narrative.
2. The Anthropic Managed Agents selloff day (Apr 10) is the most interesting cross-asset signal. SaaS cratered that day (Cloudflare and Akamai both -13-17% on Anthropic's Managed Agents launch); space cohort RALLIED +5.5%. The cohort was decoupled from the SaaS-disruption narrative — it traded as its own factor unrelated to the AI-eats-SaaS story. The cleanest evidence that space pure-plays don't trade as a SaaS proxy or AI-infrastructure proxy.
3. Iran war kickoff (Feb 27 2026) drove the cohort -5.7% — risk-off pricing across the basket. But the war became a structural tailwind over March-April via the defense-repricing channel (per [[2026 Iran conflict defense repricing|Iran conflict defense repricing]] vault note). The initial reaction was sell-the-news; the structural impact was bullish.

Largest +PC1 days reveal name-specific idiosyncratic spikes:

| Date | Basket % | Standout name (large idiosyncratic) |
|---|---|---|
| 2026-05-08 | +19.4% | RKLB +15.7pp idio (Q1 print) |
| 2025-12-19 | +15.7% | LUNR +19.4pp idio (likely IM-2 / lunar mission news) |
| 2026-04-02 | +12.2% | SPIR +7.6pp / PL +7.7pp idio (data-sleeve session) |
| 2026-04-16 | +11.7% | PL +7.1pp idio (NGA contract or constellation news) |
| 2026-01-27 | +11.3% | RDW +18.0pp idio (likely SHIELD IDIQ inclusion announcement Jan 27) |

The pattern: on big factor-up days, one or two names typically carry significant idiosyncratic alpha layered on top of the factor. The names doing the idiosyncratic heavy-lifting rotate — RKLB on May 8, LUNR on Dec 19, RDW on Jan 27, PL on Apr 2 / Apr 16. No single name is the cohort's "permanent alpha generator"; the catalyst rotation is part of what makes the cohort tradeable as a basket. The basket captures the factor; any individual name's positioning bets on which one will be the next idiosyncratic-alpha generator.

---

## Vol regime — has volatility tightened alongside correlation?

Correlation has tightened materially over time (3Y intra-correlation 0.48 → YTD 0.64). The natural question: did volatility tighten alongside, or has the cohort just become more *correlated* without becoming less *volatile*?

Run via `python scripts/cohort_extras.py`. 60-day annualized vol comparison (May 7 2025 vs May 8 2026):

| Series | 1Y ago | Latest | Change |
|---|---|---|---|
| Basket (equal-weighted 7) | ~94% | ~91% | -3pp (essentially unchanged) |
| Individual names (latest) | — | 102-121% | All names in the 100-120% annualized vol band |
| [[SPY]] | 33.6% | 15.0% | -18.6pp |
| [[IWM]] (small-cap) | 32.9% | 21.1% | -11.8pp |

![[space-pureplays-vol-regime.png]]
*Rolling 60-day annualized vol — basket (blue) vs SPY (grey) and IWM (orange). The basket stays in the 80-100% vol band; broad markets are much lower.*

The finding is clean and analytically valuable: cohort volatility has NOT tightened. Basket vol stayed roughly stable around 85-95% while broad-market and small-cap-ETF vols fell materially. The cohesion improvement is purely in the direction of correlated co-movement, not in damping of individual-name volatility.

Structural implication: the cohort is becoming a *cleaner expression of the same high-vol exposure* over time, not a *lower-vol product*. Anyone holding the basket gets ~90% annualized vol — that's the cost of holding the factor at face value. The right comparison isn't "is this less risky now than before" (no) but "is the volatility delivering more factor signal per unit of vol" (yes — because correlation rose, less of the basket's vol is now diversifiable noise).

This also reframes the SPY beta finding from the factor decomposition. Basket vol 91% vs SPY vol 15% means the basket is approximately 6x as volatile as the market — but the SPY beta is only -0.12. The cohort's daily-return variance is not coming from broad market exposure; it's coming from the pure-play factor + cohort-specific dispersion. Vol regime confirms that interpretation: the basket is high-vol *despite* having near-zero SPY beta.

---

## Minimum-name expression as a tradeable position — LUNR + BKSY drawdown profile

Subset analysis (above) showed LUNR + BKSY captures 94% of the cohort factor with a 2-name basket. The next test: does the 2-name expression deliver as a tradeable position, or only as a tracking proxy?

1Y comparison (May 8 2025 → May 8 2026, daily-rebalanced equal-weighted):

| Metric | LUNR + BKSY (2-name) | Full 7-name basket |
|---|---|---|
| Cumulative return (simple) | +196.1% | +120.1% |
| Cumulative log return | +108.6% | +78.9% |
| Annualized vol | 101.8% | 86.0% |
| Annualized Sharpe (rf=0) | 1.54 | 1.33 |
| Max drawdown | -47.3% | -42.4% |
| Best single day | +20.9% | +17.7% |
| Worst single day | -15.8% | -11.2% |
| % positive sessions | 55.7% | 55.7% |
| Days to recover from max DD | 49 | 46 |
| Max drawdown trough | 2025-11-17 | 2025-11-20 |

![[lunr-bksy-vs-basket-drawdown.png]]
*Drawdown profile — LUNR+BKSY (blue) vs full 7-name basket (red dashed). The 2-name basket has a slightly deeper max DD (-47.3% vs -42.4%) but a similar recovery profile.*

Three findings:

1. The 2-name basket OUTPERFORMED the 7-name basket on cumulative return (+196% vs +120% simple). LUNR + BKSY isn't just a tracking proxy — it's a leveraged factor expression that captured more cumulative return than the broader cohort. Both names happen to have above-average individual returns AND their pair has effective beta-to-cohort > 1.
2. Sharpe ratio is higher for the 2-name expression (1.54 vs 1.33). Risk-adjusted return is better for LUNR + BKSY because the cumulative return premium more than compensates for the modestly higher vol (102% vs 86% annualized). The drawdown penalty (-47% vs -42%) is real but small.
3. Max drawdown trough dates (Nov 17-20 2025) line up directly with the rolling PC1 variance regime-shift window. The cohort had a sharp ~45% drawdown in mid-November 2025, then rallied through the regime change. The Nov 17-20 trough is when the cohort bottomed; the Nov 20-Dec 5 rally is when PC1 variance jumped from ~55% to ~68%. That sequence — sharp drawdown into a regime shift toward higher correlation — is structurally important: cohort cohesion increased *coming out of* the drawdown, not at peak prices.

Practical implication: for users who want the cohort factor as a tradeable position with minimum position count, LUNR + BKSY equal-weighted is the cleanest expression. The trade has captured all of the cohort's cumulative return and then some, with comparable drawdown characteristics. Tracking error against the full basket is 35.5% annualized (per minimum-name expression analysis above) — that's the cost of the simpler position. For pure-factor exposure with minimum tracking error, the full 7-name basket remains optimal; for *return-maximizing factor exposure*, the 2-name pair has been the better trade over the trailing year.

This is the strongest possible answer to "what's the minimum factor expression?" — not just "the smallest basket that tracks the factor," but "the smallest basket that captures most of the factor and outperformed the full basket on cumulative return." LUNR + BKSY satisfies both.

---

## PC2 pair-trade backtest — data sleeve vs hardware sleeve

PC2 captured 9% of cohort variance and revealed a clean data-businesses-vs-hardware-businesses split. The natural test: has the realized return spread between sleeves actually matched the PC2 implication?

Long data sleeve ([[Spire Global\|SPIR]] + [[Planet Labs\|PL]] + [[BlackSky\|BKSY]], equal-weighted) and short hardware sleeve ([[Rocket Lab\|RKLB]] + [[Redwire\|RDW]] + [[Intuitive Machines\|LUNR]] + [[AST SpaceMobile\|ASTS]], equal-weighted). 1Y window through May 8 2026:

| Metric | Value |
|---|---|
| Data sleeve cumulative return | +132.3% |
| Hardware sleeve cumulative return | +111.3% |
| Long data / short hardware log-spread | +9.5% over 1Y |
| Spread annualized vol | 58.4% |
| Spread Sharpe | 0.23 |

The data sleeve outperformed hardware by ~21pp on a cumulative-return basis, and the long-data/short-hardware spread captured +9.5% in log terms (modestly positive realized return). Volatility is high (58% annualized) and the Sharpe is only 0.23 — this is not a high-quality risk-adjusted trade. The spread is dominated by occasional large movements rather than steady directional drift.

Notable spread events:

- Best 30-day data outperformance: window ending 2026-04-10 (+48.8% cumulative log-spread). This is the [[Anthropic Managed Agents selloff April 2026]] period when SaaS-like recurring-revenue businesses rallied as agentic-AI infrastructure plays while hardware/launch names lagged on Neutron-uncertainty and capital-markets pressure
- Worst 30-day data window (hardware outperformed): ending 2026-01-06 (-29.5% cumulative log-spread). Hardware/launch names rallied on the SpaceX-IPO-anticipation runup that began late December 2025 while data names lagged on Q4 print uncertainty

The implication for trading the PC2 axis: the spread is real and directional but episodic. It's not a "permanent risk premium" pair trade — it's more like a "regime indicator" where data outperforms when AI-recurring-revenue narratives dominate and hardware outperforms when launch-IPO-Golden-Dome narratives dominate. The PC2 axis tracks which thematic narrative is in the driver's seat on a given month.

Better expression of the cluster: rather than trade PC2 as a pair, monitor it as a *macro indicator* of which thematic sub-narrative is dominating cohort attention. When the PC2 spread is widening toward data, AI-narrative is dominant; when widening toward hardware, launch / Golden Dome / SpaceX-IPO narrative is dominant. The May 8 basket rally was a hardware-narrative session (all names up, but RKLB +34% / RDW +20% / LUNR +20% / ASTS +15% led the move, with data names PL +11% / SPIR +15% / BKSY +22% participating but trailing). PC2 spread on May 8: data sleeve = +16.2% avg, hardware sleeve = +22.4% avg → -6.2% pair-spread (hardware-favoring session).

---

## Tested hypothesis — Golden Dome defense-tech super-cluster (falsified)

The KTOS finding raised a natural question: is there a broader "Golden Dome defense-tech" cluster that the space pure-plays are a sub-cluster of? If so, the right vault structure would be a parent Golden-Dome-thematic cluster note with two children (space pure-plays + defense-tech mid-caps). Test config: `scripts/cluster_configs/ktos.yaml` with candidate cohort KTOS / AVAV / [[Mercury Systems\|MRCY]] / [[BWXT]] / [[Heico\|HEI]], controls = defense primes + space pure-plays + ETFs.

Result: hypothesis falsified. The proposed 5-name defense-tech mid-cap cluster does NOT cohere as a single tradeable factor.

| Diagnostic | Result | Read |
|---|---|---|
| Intra-cluster avg correlation (1Y) | 0.491 | Just below the 0.50 weak-cohesion threshold |
| Range | 0.225 - 0.650 | Wide — HEI is the clear outlier (HEI-AVAV 0.22) |
| Cluster vs ETF intra-advantage | -0.039 | Negative — the cohort correlates MORE with broad ETFs than with itself |
| Hierarchical clustering @ 0.5 threshold | Splits into 3 sub-clusters | KTOS+AVAV / MRCY+BWXT+SPY+IWM / HEI singleton |
| PC1 explained variance | 59.8% | Below space pure-plays' 67% |

The negative intra-advantage vs ETFs (-0.039) is the falsification — the candidate cohort has lower internal correlation than its correlation to broad-market benchmarks. By definition, the cohort is not a real cluster; it's a slice of broad-market exposure with elevated cross-correlation.

The hierarchical clustering reveals the underlying structure:

- [[Kratos]] + [[AeroVironment]] (KTOS+AVAV) form a tight 2-name micro-cluster (0.65 pairwise correlation). This is the "UAS / loitering munitions / drone-defense" pair. Could be a legitimate cluster if expanded with additional UAS / drone-defense names — but 2 names is too small to define a vault-level cohort without more candidates.
- [[Mercury Systems]] + [[BWXT]] cluster with [[SPY]] and [[IWM]] rather than with each other. Translation: these names trade as small-cap-defense-electronics beta, not as a coherent thematic basket. They're conventionally classified as defense-tech but their daily-return profile is closer to "leveraged broad-market" than to "Golden Dome thematic."
- [[Heico]] is a singleton. Aerospace components + commercial aerospace exposure decouple it from the rest of the defense-tech candidates. HEI is its own thing.

The vault implication is that the [[Space pure-plays]] cohort is NOT a sub-cluster of a broader Golden-Dome-thematic super-cluster. There is no such super-cluster. The space pure-plays are the cleanest equity expression of the Golden Dome theme that exists; the defense-tech mid-caps trade on their own (mostly non-thematic) factor exposures.

This sharpens the [[Space pure-plays]] thesis: the cohort isn't "one slice of a larger defense theme" — it's the *only* defensible thematic cluster on the public side of the Golden Dome story. Anyone trying to express the Golden Dome thesis via mid-cap defense-tech is reaching for a basket that doesn't cohere as a factor.

The KTOS-AVAV micro-cluster remains a candidate for separate validation as a "UAS / drone-defense" cohort if more candidates are added. Follow-up test: with KTOS-AVAV as the candidate pair plus the same 6 defense-tech extras (MRCY, BWXT, HEI, LDOS, PSN, CACI) as potential additions:

| Candidate | Avg corr to KTOS-AVAV | Verdict |
|---|---|---|
| KTOS-AVAV pair correlation | 0.638 (intra) | Real micro-cluster |
| [[Mercury Systems\|MRCY]] | 0.543 | Below pair-internal — adding it loosens cluster |
| [[BWXT]] | 0.492 | Loosens cluster |
| [[Leidos\|LDOS]] | 0.382 | Far below |
| [[CACI]] | 0.359 | Far below |
| [[Parsons\|PSN]] | 0.293 | Far below |
| [[Heico\|HEI]] | 0.291 | Far below |

The KTOS-AVAV pair vs adjacent benchmarks:

| Reference | Pair avg correlation |
|---|---|
| [[ITA]] (aerospace + defense ETF) | 0.536 |
| [[LHX]] (closest defense prime) | 0.453 |
| [[IWM]] (small-cap) | 0.411 |
| [[SPY]] | 0.354 |
| [[LMT]] / [[RTX]] / [[NOC]] | 0.30-0.35 |

Verdict on the UAS micro-cluster: KTOS-AVAV is a genuine 2-name micro-cluster (intra 0.638, separated from defense primes by +0.20 to +0.30, separated from broad market by +0.25-0.30). However, *adding any of the 6 tested defense-tech extras would loosen the cluster, not strengthen it* — MRCY at 0.543 is the closest extension candidate but adds noise relative to the pair's own 0.638 internal correlation. The micro-cluster is *real but small* — too small (2 names) to merit a full vault cohort note under current scope, but worth tracking as a candidate for expansion if pure-play UAS / loitering-munitions names like Karman Holdings (KRMN, when in local DB) or Red Cat Holdings (RCAT) become more liquid.

For now, the structural read is that the KTOS-AVAV pair is the only defensible UAS-defense-tech micro-cluster — and it is genuinely distinct from both the space pure-plays cluster (KTOS-pair-to-space-cohort avg correlation was 0.428 per Golden Dome test) and from the defense-prime cluster (avg correlation 0.30-0.35). The pair sits in its own thematic space.

*Diagnostic source: `scripts/cluster_configs/ktos.yaml` + `python scripts/cluster_analysis.py --primary KTOS` (May 10, 2026); UAS micro-cluster follow-up via `scripts/cohort_extras.py`.*

---

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
