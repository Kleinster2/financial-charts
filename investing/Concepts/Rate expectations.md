---
aliases: [Fed rate expectations, rate path, implied rate path, FedWatch]
---
#concept #rates #macro #fed

**Rate expectations** — What the futures market prices for the path of the [[Federal Reserve]]'s policy rate. Derived from [[Fed Funds futures (ZQ)]] and [[SOFR futures (SR3)]] on the [[CME Group|CME]]. The market's real-time bet on how many cuts or hikes are coming, and when.

---

## Synthesis

As of Mar 2026, the market prices a slow, shallow easing cycle — ~57bp over 21 months to a terminal rate around 3.07%. No single FOMC meeting commands >50% cut probability. This is a "grudging grind" narrative: the Fed will ease, but only because the economy softens enough to justify it, not because inflation is beaten or the Fed wants to get ahead of a downturn. The lack of front-loading distinguishes this from Dec 2023's pivot repricing, when the market briefly priced 6+ cuts. The SR3 curve turning upward past 2027 suggests term premium is reasserting — the market doesn't believe the terminal rate is permanently low. Key risk: if tariff-driven inflation reignites (see [[2026 Iran conflict market impact]], [[Inflation expectations]]), the entire curve reprices higher and the ~2 cuts evaporate.

The risk in that synthesis fired on May 12, 2026 — see [[#May 12 2026 CPI shock — regime break]] below. The ~57bp implied easing has effectively evaporated; the curve now prices net tightening of ~6-9bp through mid-2027 before a small easing back to ~3.70% by Dec 2027.

---

## May 12 2026 CPI shock — regime break

The April CPI release on May 12 2026 produced the cleanest regime break in the implied rate path since the Dec 2023 pivot — in the opposite direction.

### What changed

| Reading | Actual | Consensus | Prior month | Spread |
|---------|--------|-----------|-------------|--------|
| Headline CPI MoM | +0.6% | +0.6% | +0.9% | in line |
| Headline CPI YoY | +3.8% | +3.7% | — | +10bp hot |
| Core CPI MoM | +0.4% | — | — | hot |
| Core CPI YoY | +2.8% | +2.7% | — | +10bp hot |

The 3.8% YoY headline print is the highest reading since May 2023. Energy drove more than 40% of the monthly rise — connecting the inflation print directly to the [[2026 Strait of Hormuz crisis]] and the [[Brent crude]] / [[WTI]] re-rating since March. Core at 2.8% YoY is moving in the wrong direction, weakening the case for any Fed easing in the near term.

### Rate path response

Same-session repricing was sharp. Implied probability of any 2026 Fed rate cut collapsed to roughly 5%; implied probability of a 2026 hike rose to roughly 22%. The full Fed Funds futures curve repriced higher across all maturities — see the updated table in [[#Current implied path]] below.

The shift in framing is what matters more than the magnitude of any single contract move:

- Mar 2026 baseline: curve sloped down to a terminal of 3.07% (~57bp implied easing)
- May 13 2026 snapshot: curve sloped up to a hump near 3.85% by mid-2027 before easing back to 3.70% by Dec 2027 (~6bp net tightening, then ~9bp partial reversal — call it zero net easing over the futures horizon)
- No single FOMC meeting now prices any cut with probability above 8%

In effect, the "slow grind lower" narrative has been replaced by "hike-bias hold." The Fed is no longer credibly easing on the futures curve.

### Why the print broke the curve

Three things were already in tension before May 12:

- The [[2026 Strait of Hormuz crisis]] had pushed oil into a sustained higher band through April and May, feeding headline inflation directly
- Core services inflation had been running above 3% on a 3-month annualized basis since February
- The Fed's March SEP still projected two 25bp cuts in 2026 — wider than the futures market's two cuts but in the same direction

The CPI print collapsed the Fed-vs-market gap by pulling the futures market to the Fed's hawk side rather than the other way around. With energy now structurally repricing inflation through the year-on-year base, the bar for any 2026 cut is a sharp labour-market weakening or a Hormuz resolution — neither of which is currently visible in the data.

### Cross-asset read-through (May 12)

The session captured the regime break across rate-sensitive assets:

| Channel | Move | Read |
|---------|------|------|
| US 10Y [[Treasuries\|Treasury]] yield | climbed (per US News) | duration repricing |
| [[Nasdaq]] Composite | -1.94% | rate-sensitive equity selloff |
| [[Russell 2000]] | -2.34% | small-cap rate beta |
| [[Qualcomm]] (QCOM) | -11.5% | biggest single-day chip drop since 2020 — profit-take on May 11 AI rally |
| [[Copper]] | $14,000/ton (record near) | inflation hedge plus AI-grid demand |
| [[Ero Copper]] (ERO) | +10.1% | copper rally pass-through |
| [[Venture Global]] (VG) | +14.2% | [[LNG]] / energy beneficiary |

The split is informative: the print penalized rate-sensitive tech beta while bidding hard-asset inflation hedges. That is the cross-asset signature of a curve that has lost its easing prior, not a generalized risk-off.

### Sources

- US Bureau of Labor Statistics — [Consumer Price Index Summary, April 2026 release (May 12)](https://www.bls.gov/news.release/cpi.nr0.htm)
- US News — [April CPI Rises More Than Expected; Bond Yields Climb](https://money.usnews.com/investing/news/articles/2026-05-12/april-cpi-rises-more-than-expected-bond-yields-climb) (May 12)
- US News — [Inflation Hits 3.8%, Highest Level Since 2023, as Energy Costs Surge](https://www.usnews.com/news/national-news/articles/2026-05-12/inflation-hits-3-8-highest-level-since-2023-as-energy-costs-surge) (May 12)
- 24/7 Wall St — [Rate Cut Odds Just Collapsed to 5%](https://247wallst.com/investing/2026/05/12/rate-cut-odds-just-collapsed-to-5-history-says-this-is-when-record-highs-get-tested/) (May 12)
- CNBC — [Qualcomm drops 11% as chip stocks pull back from record AI-driven rally](https://www.cnbc.com/2026/05/12/qualcomm-chip-stocks-record-ai.html) (May 12)
- Bloomberg — [Copper Rallies Above $14,000 a Ton, Nearing Fresh All-Time High](https://www.bloomberg.com/news/articles/2026-05-12/copper-rallies-above-14-000-a-ton-nearing-fresh-all-time-high) (May 12)

---

## Current implied path

![[fed-rate-expectations.png]]
*Fed Funds futures (ZQ, monthly) + 3M SOFR futures (SR3, quarterly). Snapshot as of May 13, 2026. Updated via `fed_rate_expectations.py`.*

| Metric | Value |
|--------|-------|
| Current target range | 3.50%–3.75% |
| Current effective rate | 3.635% |
| Curve peak | ~3.845% (Jun-Jul 2027) |
| Implied terminal rate | ~3.695% (Dec 2027) |
| Total implied easing through Dec 2027 | -6bp (~zero net easing) |
| Net move to curve peak | +21bp (hike-bias hold) |
| Curve shape | Hump — slight tightening through mid-2027, partial easing back |

### Key contract months (May 13, 2026 snapshot)

| Contract | Month | Implied Rate | Change from now |
|----------|-------|-------------|-----------------|
| ZQK26 | May 2026 | 3.635% | — |
| ZQM26 | Jun 2026 | 3.630% | -0.5bp |
| ZQU26 | Sep 2026 | 3.635% | 0bp |
| ZQZ26 | Dec 2026 | 3.715% | +8bp |
| ZQM27 | Jun 2027 | 3.845% | +21bp |
| ZQZ27 | Dec 2027 | 3.695% | +6bp |

For comparison, the March 2026 baseline (pre-CPI-shock) is captured in [[#May 12 2026 CPI shock — regime break]] above.

---

## FOMC meeting probabilities

![[fed-fomc-probabilities.png|697]]
*Implied probability of a 25bp cut at each FOMC meeting. Approximation — ZQ contracts reflect month-average rates, not precise post-meeting levels. CME FedWatch uses intra-month weighting for higher precision. Snapshot as of May 13, 2026.*

After the May 12 CPI shock, no FOMC meeting in 2026 or H1 2027 prices any cut probability above 8%. The highest implied cut probability is Sep 22 2027 at ~8%, with Oct 27 2027 at ~6% and Jul 28 2027 at ~4%. Several intermediate meetings price small implied hike steps (cut-probability of 0% with positive contract spreads). Cumulative implied cuts across the meeting schedule is -9bp — effectively zero. This is what a "hike-bias hold" curve looks like at the meeting level: the market is not betting on the Fed easing, and is leaving open the option of one hike if the inflation print path stays hot.

The contrast with the March 2026 baseline is the point: in March, the highest meeting probability was Jul 29 2026 at ~28%, with easing distributed across many meetings. The "slow grind lower" pricing has now been removed entirely.

---

## Kalshi policy overlay (May 19, 2026)

[[Kalshi]]'s [[Federal Reserve|Fed]] policy markets provide a second market-implied view alongside the [[Fed Funds futures (ZQ)|ZQ]] strip. The signal is the same as the post-CPI futures curve: no near-term cut, high probability of no 2026 cuts, and a small but nonzero hike tail.

| Market | Last | Bid / ask | Read |
|---|---:|---:|---|
| June FOMC no change | 97c | 96c / 97c | June hold is the base case. |
| June 25 bp cut | 3c | 2c / 3c | Cut pricing is basically residual. |
| June 25 bp hike | 2c | 1c / 2c | Hike tail exists but is not central. |
| July FOMC no change | 92c | 91c / 92c | No-change expectation extends through July. |
| Dec 2026 upper bound above 3.50% | 68c | 64c / 68c | Market leans against substantial year-end easing. |
| 2026 cut count: zero cuts | 64.8c | 63.2c / 64.9c | The modal 2026 path is no further easing. |
| 2026 cut count: one cut | 18.5c | 18.4c / 18.5c | One cut is the main alternative. |
| 2026 cut count: two cuts | 11.6c | 10.1c / 11.7c | The March-style two-cut path is now a low-probability outcome. |

The useful distinction is that [[Kalshi]] expresses the path as event probabilities while [[Fed Funds futures (ZQ)]] expresses it as a continuous rate curve. Both are pointing at the same regime: the [[Federal Reserve]] is priced as pinned by [[Inflation]], not preparing to ease into a growth scare.

*Sources: [[Kalshi]] API series KXFEDDECISION, KXFED, and KXRATECUTCOUNT, read May 19, 2026: https://external-api.kalshi.com/trade-api/v2/markets?limit=1000&series_ticker=KXFEDDECISION, https://external-api.kalshi.com/trade-api/v2/markets?limit=1000&series_ticker=KXFED, and https://external-api.kalshi.com/trade-api/v2/markets?limit=1000&series_ticker=KXRATECUTCOUNT*

---

## How it works

[[Fed Funds futures (ZQ)]] settle at the monthly average effective fed funds rate. Price = 100 minus implied rate. A ZQ contract at 96.36 implies a 3.64% average rate for that month. Available monthly, ~21 months forward. For full contract mechanics (settlement, day-7 boundary handling for FOMC meetings, convexity bias), see the instrument note.

[[SOFR futures (SR3)]] price 3-month compounded [[SOFR]]. Same math (100 minus price). Extend further out (~2+ years) but represent the secured overnight rate rather than the fed funds rate. The two strips track closely because SOFR sits near the bottom of the fed funds target range under normal repo conditions — but can diverge during quarter-end repo stress.

Meeting-level probabilities — if the ZQ contract *before* an FOMC meeting implies rate X, and the contract *after* implies rate Y, the drop (X - Y) divided by 0.25 gives the probability of a 25bp cut. This is a simplification — true [[CME Group|CME FedWatch]] methodology weights by the number of days before/after the meeting within the month.

---

## Interpretation

The curve tells you what's priced. When the implied path diverges from Fed dot plots or economic data, that's where the trade is:

- Curve steeper than dots — market more dovish than Fed. If the Fed delivers, rates positions rally. If Fed pushes back, short-end sells off. See [[Steepener trade]].
- Curve flatter than dots — market sees fewer cuts than Fed projects. Usually means inflation sticky or economy resilient.
- Front-end flat, back-end steep — no imminent cuts priced, but eventual easing expected. Shape of the curve in Mar 2026.
- Curve hump — small near-term tightening priced before partial easing back. Shape of the curve in May 2026 after the CPI shock. The Fed's own dot plot is now substantially more dovish than the futures market; if the dot plot survives the June SEP update without revision higher, the gap between Fed projection and market pricing widens further.
- Sharp step between months — a specific FOMC meeting is expected to deliver.

---

## Tooling

```bash
# Snapshot: implied rate path chart + table
python scripts/fed_rate_expectations.py

# FOMC meeting probabilities
python scripts/fed_rate_expectations.py --mode fomc

# How a specific contract's implied rate has shifted over time
python scripts/fed_rate_expectations.py --mode history --history-contract ZQZ26.CBT

# Table only (no chart)
python scripts/fed_rate_expectations.py --table --no-chart

# Persist the ZQ + SR3 strip to the database (rate_futures_daily table)
python scripts/update_rate_futures.py                  # daily incremental append
python scripts/update_rate_futures.py --backfill       # full 2y per-contract history
```

Data source: [[CME Group|CME]] via yfinance. ZQ contracts on CBOT, SR3 on CME. Snapshot reads pull live from yfinance; persisted history lives in `rate_futures_daily` (long format: Date, contract, root, delivery_year, delivery_month, price, implied_rate) as of May 2026. See [[Fed Funds futures (ZQ)#Historical reconstruction]] for query examples. SR3 historical coverage is limited because yfinance returns snapshot-only data for SR3 contracts — daily SR3 history accumulates going forward from the persistence-script start date.

---

## Related

- [[Fed Funds futures (ZQ)]] — primary instrument the implied path is built from
- [[SOFR futures (SR3)]] — companion instrument extending the curve out 2-3 years
- [[Federal Reserve]] — the institution setting the rate
- [[Jerome Powell]] — current Fed chair
- [[SOFR]] — secured overnight rate, closely tracks effective fed funds
- [[Steepener trade]] — directional bet on the yield curve shape
- [[Inflation expectations]] — the other side of the dual mandate
- [[Inflation]] — the level the Fed is responding to
- [[Treasuries]] — rates flow through to all duration assets
- [[Fed pivot December 2023]] — last major repricing of the rate path
- [[Fed independence]] — political risk to the rate-setting process
- [[CME Group]] — exchange where these futures trade
- [[2026 Strait of Hormuz crisis]] — the energy shock feeding the headline CPI print
- [[2026 recession risk]] — the alternative path that would bring cuts back
- [[Term premium]] — the part of the curve above expected short rates
