---
aliases: [COMB ETF, GraniteShares Bloomberg Commodity Broad Strategy No K-1 ETF, GraniteShares Bloomberg Commodity Broad Strategy]
tags: [asset, etf, commodities]
ticker: COMB
---

# COMB

**COMB** is the GraniteShares Bloomberg Commodity Broad Strategy No K-1 ETF, a US-listed commodity futures ETF benchmarked against the [[Bloomberg Commodity Index]]. It is the closest Bloomberg-linked broad commodity proxy currently available in `market_data.db`.

---

## Quick stats

| Metric | Value |
|---|---|
| Ticker | COMB |
| Issuer | [[GraniteShares]] |
| Benchmark | [[Bloomberg Commodity Index]] |
| Exchange | [[NYSE]] Arca |
| Expense ratio | 0.25% |
| Structure | Commodity futures + short-term Treasury collateral |
| Tax form | 1099; no K-1 |
| Local data | 2017-07-14 to 2026-05-19 after latest refresh |

---

## Use Case

COMB is the practical charting proxy for BCOM in this repo. It is not the official BCOMTR index series, but it is benchmarked to BCOM, directly holds commodity futures contracts, and uses short-term Treasury bills as collateral. Use it when the question is broad Bloomberg-style commodity beta and official index history is unavailable locally.

![[comb-vs-dbc-vs-gsg-vs-pdbc-price-chart.png]]
*COMB vs [[DBC]], [[GSG]], and [[PDBC]] normalized since May 2021. COMB tracks the broad commodity move but lagged the more energy-heavy proxies during the 2021-2026 rally.*

---

## Related

- [[Bloomberg Commodity Index]] - benchmark
- [[Commodities]] - parent concept
- [[GraniteShares]] - issuer
- [[DBC]] - Invesco broad commodity ETF
- [[GSG]] - energy-heavy commodity benchmark proxy
- [[PDBC]] - Invesco K-1-free commodity ETF

---

Sources:
- [GraniteShares COMB product page](https://graniteshares.com/etfs/comb/)
