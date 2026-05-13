---
aliases: [Fed Funds futures, ZQ, ZQ futures, 30-Day Fed Funds futures, fed funds futures]
tags: [product, instrument, futures, rates, cme, cbot]
---
#product #instrument #futures #rates

# Fed Funds futures (ZQ)

30-day cash-settled futures contract on the average daily effective Fed Funds rate. Listed by [[CBOT|CBOT (CME)]] under symbol **ZQ**, with one contract per delivery month going out roughly 36 months. The vault's primary translator between traded futures prices and the market-implied path for [[Federal Reserve|Fed]] policy — used by [[Rate expectations]] to read what the market is pricing for FOMC meetings.

---

## Contract specifications

| Spec | Value |
|------|-------|
| Symbol root | ZQ |
| Listing | [[CBOT]] (a [[CME Group]] designated contract market) |
| Underlying | Daily effective Fed Funds rate, monthly average |
| Contract size | $4,167 per basis point (= $5M × 30/360 × 0.01) |
| Tick size | 0.0025 (= $10.4175 per tick) for front month; 0.005 for back months |
| Settlement | Cash-settled to monthly arithmetic average of daily effective Fed Funds rate |
| Delivery month codes | F G H J K M N Q U V X Z (Jan–Dec) |
| Quote | 100 minus implied rate (e.g. 96.3650 → 3.6350%) |
| Listed depth | ~36 consecutive months |
| Trading hours | Sunday-Friday 17:00-16:00 CT (CME Globex) |
| First listing | October 1988 (CBOT) |

---

## Price-to-rate identity

The contract is quoted as 100 minus the implied annualized rate. The math is:

```
implied_rate (%) = 100 − futures_price
```

A ZQ contract trading at 96.3650 implies a 3.6350% average effective Fed Funds rate for the contract's delivery month. There is no curve fitting, no discount factor, no convexity adjustment in the quote itself — the price IS the rate, inverted. This is the same convention as Eurodollar futures (now retired) and [[SOFR futures (SR3)|SR3 SOFR futures]].

---

## What "monthly average" actually means

The ZQ contract settles to the arithmetic mean of the daily effective Fed Funds rate across every calendar day of the delivery month. The Fed's effective rate is published by the [[New York Fed]] each morning for the prior business day. Weekends and holidays carry the previous business day's rate. Two consequences:

1. A single ZQ contract reflects all FOMC actions in that month, weighted by the number of days each rate level prevailed. A meeting on day 6 of a 30-day month produces a 5-day pre-meeting rate and a 25-day post-meeting rate — both blended into the monthly average.
2. To isolate a single FOMC meeting, you compare the ZQ contract for the month before the meeting (clean pre-decision rate) with the ZQ contract for the month after (clean post-decision rate). This is the basis of the [[Rate expectations#FOMC meeting probabilities|FOMC probability calculation]] used in the vault.

The day-7 heuristic in [[Rate expectations]] handles the boundary case where the meeting is in the first week of a month: same-month ZQ already mostly reflects the decision, so pre = prior month, post = same month.

---

## Why the contract exists

The Fed Funds market is the overnight interbank lending market for reserve balances at the Fed. The effective rate (FFER, ticker `EFFR` from the NY Fed; database column `DFEDTARU` / `DFEDTARL` holds the target range) is the volume-weighted median of trades in that market. ZQ futures exist because:

- Banks and dealers hedging short-term funding need a liquid instrument to lock in a future Fed Funds rate
- Rate strategists need a way to price what the market expects from the Fed before each FOMC meeting
- Speculators want directional exposure to short-term US rates without dealing in repo or interest-rate swaps

The CME-published OIS curve and most rate-strategist models start from the ZQ strip.

---

## Reading the strip

The "ZQ strip" is the sequence of ZQ contracts ordered by delivery month (~36 months listed). When plotted as implied rate by month, it shows the market's expectation of the Fed Funds path. Common shapes:

| Strip shape | What it means |
|-------------|---------------|
| Downward-sloping | Market prices net easing (cuts > hikes over the strip) |
| Upward-sloping | Market prices net tightening |
| Flat | No net policy change priced |
| Hump (rises then falls) | Tightening first, then easing — typical late-cycle pattern |
| Step | A specific FOMC meeting is expected to deliver a definite move |

The strip's slope is not the same as the SR3 or 2Y Treasury slope. ZQ captures pure policy-rate expectations; longer-dated rates also embed [[Term premium]], credit/liquidity premia, and convexity adjustments.

---

## Relationship to SR3 SOFR futures

[[SOFR futures (SR3)|SR3 contracts]] price 3-month average SOFR, extending the rate-expectations curve out 2-3 years past where ZQ ends. The two track closely because [[SOFR]] sits at the bottom of the Fed Funds target range under normal repo conditions — but they can diverge when:

- SOFR spikes on quarter-end repo stress (Sept 2019, March 2020) — SR3 prices the spike, ZQ doesn't
- The Fed shifts the IOR / ON RRP rates relative to the target range — repricing SR3 vs ZQ
- Term premium reasserts at the back end of SR3 — ZQ doesn't extend that far

For a clean Fed-funds-only read, use ZQ. For 2-3 year ahead expectations, splice SR3 onto the back of the ZQ strip (the vault's `fed_rate_expectations.py` does exactly this — `download_zq_curve()` then `download_sr3_curve()` for the extension).

---

## Convexity and futures-vs-forward bias

Futures prices are not identical to forward rates because of the daily mark-to-market mechanism. A futures contract that drops in price (rates rise) generates a margin call now, while a forward only settles at maturity. For long-dated contracts, this creates a small convexity adjustment — the futures-implied rate runs slightly above the equivalent forward rate, with the gap growing with maturity and rate volatility.

For ZQ specifically, the convexity bias is small (front-month contracts settle within ~30 days, so the mark-to-market timing barely matters). For the longer-dated SR3 contracts the bias is meaningful and is what term-premium and OIS-curve models try to extract.

This is one of the simplifications the vault's `fed_rate_expectations.py` does not correct for — it treats the futures-implied rate as the rate directly. Fine for surfacing what the curve is pricing; not fine for trade sizing or for valuing long-dated rate derivatives.

---

## Where the vault uses ZQ

- [[Rate expectations]] — primary consumer. Builds the full implied path, calculates FOMC probabilities, generates `fed-rate-expectations.png` and `fed-fomc-probabilities.png`.
- [[Term premium]] — uses ZQ-implied expected short rates as the input that gets subtracted from the nominal Treasury yield to leave the residual (term premium).
- [[Steepener trade]] — directional bets on the ZQ strip slope.
- [[Federal Reserve]], [[Jerome Powell]] — sourced for market-implied response to Fed actions.

---

## Tooling

```bash
# Snapshot the strip and FOMC probabilities
python scripts/fed_rate_expectations.py

# Just the table (no chart)
python scripts/fed_rate_expectations.py --table --no-chart

# How a single contract's implied rate has shifted over time
python scripts/fed_rate_expectations.py --mode history --history-contract ZQZ26.CBT
```

Data: `yfinance` for ZQ contracts on CBOT. Database stores the Fed target range (`DFEDTARU` / `DFEDTARL` columns in `stock_prices_daily`) via FRED.

---

## Related

- [[CME Group]] — parent exchange operator
- [[CBOT]] — listing venue
- [[SOFR futures (SR3)]] — companion instrument for longer maturities
- [[Rate expectations]] — the concept this instrument feeds
- [[SOFR]] — underlying rate for SR3, related to Fed Funds via repo channel
- [[Federal Reserve]] — the institution setting the rate ZQ tracks
- [[Term premium]] — uses ZQ to decompose nominal yields
- [[New York Fed]] — publishes the daily effective Fed Funds rate
- [[Treasuries]] — duration assets whose pricing flows from ZQ + term premium
- [[Steepener trade]] — directional curve trade
