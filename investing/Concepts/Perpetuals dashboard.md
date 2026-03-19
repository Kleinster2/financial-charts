---
aliases:
  - perps dashboard
  - intraday dashboard
  - Hyperliquid dashboard
tags:
  - concept
  - dashboard
  - crypto
  - intraday
---

# Perpetuals dashboard

Live comparison of [[Hyperliquid]] [[Perpetuals|perpetual]] contracts against their ETF counterparts. The perps trade 24/7; the ETFs only during US market hours. The gaps — nights, weekends — are where the perp data has unique signal value, especially during the [[2026 Iran conflict market impact|Iran conflict]] when weekend events moved markets before traditional venues could price them.

---

## Oil: USO vs HL:CL (14 days, normalized)

![[uso-vs-hl-cl-intraday.png]]
*WTI crude oil — [[USO]] ETF (blue) vs [[Hyperliquid]] perpetual (pink). The perp reacts in real-time to weekend events while USO sits flat until Monday open. Note the spike around Mar 9: the perp priced in the Iran escalation over the weekend, then USO gapped up to catch it on Monday. [[trade.xyz]] oil perp hit ~$500M daily volume during the conflict.*

---

## Gold: GLD vs HL:GOLD (14 days, normalized)

![[gld-vs-hl-gold-intraday.png]]
*Gold — [[GLD]] ETF (blue) vs Hyperliquid perpetual (pink). Same pattern: continuous perp vs stepwise ETF. Gold sold off sharply after the [[Ras Laffan]] strike (Mar 18 evening) — the perp shows real-time repricing while GLD won't reflect it until next market open.*

---

## Silver: SLV vs HL:SILVER (14 days, normalized)

![[slv-vs-hl-silver-intraday.png]]
*Silver — [[SLV]] ETF (blue) vs Hyperliquid perpetual (pink).*

---

## S&P 500: SPY vs HL:SP500 (3 days, normalized)

![[spy-vs-hl-sp500-intraday.png]]
*[[S&P 500]] — SPY ETF (blue) vs Hyperliquid perpetual (pink). The S&P 500 perp launched Mar 18, 2026 — first officially licensed [[S&P 500]] derivative on a decentralized platform, using [[S&P Global]] index data. Limited history, but the overnight/weekend divergences will accumulate. This is the chart to watch for Monday-open prediction signals.*

---

## Funding rates: Oil, Gold, Silver (14 days, bps/hour)

![[perp-funding-rates.png]]
*Hourly funding rates in basis points. Positive = longs pay shorts (bullish crowding). Negative = shorts pay longs (bearish crowding). HL:CL shows the most volatility — funding flips frequently as traders reposition around Iran conflict news. HL:GOLD relatively stable near zero. See [[Perpetuals]] for how funding rates function as a carry cost.*

---

## How to read these charts

The perp line is always denser than the ETF line because it has 24/7 data points vs ~7 hours/day for ETFs. Key patterns to watch:

- Weekend divergence: perp moves while ETF is flat → Monday gap prediction
- Overnight divergence: same pattern, smaller scale, every night
- Convergence speed: how quickly does the ETF "catch up" to the perp's overnight move? Faster convergence = perp is a reliable leading indicator
- Funding rate regime: sustained positive funding = crowded longs, potential for painful unwind

---

## Data sources and refresh

| Data | Source | Table | Refresh |
|------|--------|-------|---------|
| ETF 30m candles | yfinance | `intraday_candles` | `python scripts/fetch_hourly_candles.py` |
| Perp 30m candles | [[Hyperliquid]] API | `perp_candles` | `python scripts/fetch_hyperliquid.py` |
| Funding rates | Hyperliquid API | `perp_funding_rates` | same as above |
| Daily closes | derived from perp candles | `prices_long` (HL: prefix) | same as above |

ETF data auto-prunes to 30 days. Perp data retained indefinitely. Charts generated via `/api/chart/intraday` endpoint.

---

## Chart API reference

```
# Price overlay (normalized)
/api/chart/intraday?tickers=USO,HL:CL&days=14&normalize=true&primary=USO

# Funding rates
/api/chart/intraday/funding?tickers=HL:CL,HL:GOLD&days=14

# Custom labels
&labels=USO:WTI%20(ETF),HL:CL:WTI%20(Perp)
```

---

## Related

- [[Perpetuals]] — instrument mechanics, funding rates, cost analysis
- [[Hyperliquid]] — exchange infrastructure, S&P 500 licensing deal
- [[trade.xyz]] — builder of the commodity and equity perps
- [[S&P 500]] — crypto-native derivatives section
- [[2026 Iran conflict market impact]] — the crisis that proved weekend price discovery value
