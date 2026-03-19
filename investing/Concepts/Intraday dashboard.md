---
aliases:
  - intraday dashboard
  - intraday charts
tags:
  - concept
  - dashboard
  - intraday
---

# Intraday dashboard

30-minute candle charts across all tracked assets. ETF data from yfinance (US market hours only), [[Hyperliquid]] [[Perpetuals|perp]] data 24/7. Updated via `fetch_hourly_candles.py` and `fetch_hyperliquid.py`. 30-day rolling window.

---

## Equity indices (14 days, normalized)

![[equity-indices-intraday.png]]
*SPY (blue), QQQ (pink), IWM (green), DIA (orange). Small caps ([[IWM]]) hit hardest during the [[2026 Iran conflict market impact|Iran conflict]] — down -5.5% vs QQQ -2.9%. Classic risk-off dispersion: duration-sensitive small caps sell off more than large-cap tech and blue chips.*

---

## Cross-asset risk regime (14 days, normalized)

![[cross-asset-intraday.png]]
*S&P 500 (blue), Gold (pink), WTI Oil (green). The Iran conflict in one chart: oil +29%, equities -3%, gold -5%. Oil is the direct crisis asset; equities selling on growth fears; gold initially bid as safe haven then selling off on margin calls and Ras Laffan supply shock repricing (gold mines in Gulf region at risk).*

---

## SPY vs QQQ (14 days, normalized)

![[spy-vs-qqq-intraday.png]]
*Growth vs broad market. QQQ outperforming SPY during the conflict — tech seen as more insulated from energy/supply chain disruption than the broader index which includes industrials and materials.*

---

## Commodity ETFs (14 days, normalized)

![[commodities-intraday.png]]
*WTI Oil (blue), Gold (pink), Silver (green), Natural Gas (orange). Oil is the dominant mover — everything else is noise by comparison during the [[2026 Iran conflict market impact|Iran conflict]]. Note the staircase pattern: ETFs only trade during market hours, so each step is a day's move.*

---

## 24/7 Commodity perps (14 days, normalized)

![[perps-commodities-24h.png]]
*[[Hyperliquid]] perpetuals — continuous 24/7 pricing. WTI (blue) +27%, Nat Gas (orange) +7.5%, Gold (pink) -6%, Silver (green) -6.5%, Copper (purple) -10%. The full dispersion is the insight: energy up on supply disruption, industrial metals down on demand destruction fears, precious metals selling off after initial safe-haven bid reversed. Compare to the staircase ETF chart above — the perps show what happened between the steps.*

---

## SPY intraday (14 days)

![[spy-intraday.png]]
*S&P 500 intraday price action. Each vertical cluster is a trading day. The gaps between clusters are overnight/weekend periods where only [[Hyperliquid]] perps have price data.*

---

## Oil 24/7 (14 days)

![[oil-24h-intraday.png]]
*WTI crude via [[Hyperliquid]] perp — continuous pricing including weekends and nights. The spike around Mar 9 was the initial [[2026 Iran conflict market impact|Hormuz closure]] reaction, priced in over the weekend before traditional markets opened Monday.*

---

## Gold 24/7 (14 days)

![[gold-24h-intraday.png]]
*Gold via [[Hyperliquid]] perp — continuous 24/7 pricing. Sharp selloff visible after the [[Ras Laffan]] strike (Mar 18 evening), with the perp repricing in real-time while [[GLD]] won't reflect it until next market open.*

---

## Perp vs ETF overlays

See [[Perpetuals dashboard]] for direct perp-vs-ETF comparison charts (USO vs HL:CL, GLD vs HL:GOLD, SLV vs HL:SILVER, SPY vs HL:SP500) and funding rate analysis.

---

## Data and refresh

| Asset class | Tickers | Source | Interval | Table |
|-------------|---------|--------|----------|-------|
| Equity indices | SPY, QQQ, IWM, DIA | yfinance | 30m | `intraday_candles` |
| Commodity ETFs | GLD, SLV, USO, UNG | yfinance | 30m | `intraday_candles` |
| Commodity perps | HL:CL, HL:GOLD, HL:SILVER, HL:NATGAS, HL:COPPER | Hyperliquid | 30m | `perp_candles` |
| Equity perps | HL:SP500 | Hyperliquid | 30m | `perp_candles` |
| Funding rates | all HL: tickers | Hyperliquid | hourly | `perp_funding_rates` |

```bash
python scripts/fetch_hourly_candles.py           # ETFs (auto-prunes >30 days)
python scripts/fetch_hyperliquid.py               # perps + funding + daily closes
```

Charts via `/api/chart/intraday?tickers=...&days=14&normalize=true`

---

## Related

- [[Perpetuals dashboard]] — perp vs ETF overlays, funding rates
- [[Perpetuals]] — instrument mechanics, cost analysis
- [[Hyperliquid]] — exchange infrastructure
- [[2026 Iran conflict market impact]] — the crisis driving current dispersion
