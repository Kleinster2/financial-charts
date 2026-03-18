---
aliases:
  - perpetual futures
  - perps
  - perpetual swap
  - perpetual contract
tags:
  - concept
  - derivatives
  - crypto
  - stub
---

# Perpetuals

Perpetual futures (perps) are derivative contracts that function like futures but never expire. The holder maintains a leveraged long or short position indefinitely. A funding rate mechanism periodically charges traders on the more popular side to keep the contract price tethered to the underlying asset's spot price.

---

## Quick stats

| Metric | Value |
|--------|-------|
| Origin | Crypto markets (~2016, BitMEX) |
| Key platforms | [[Hyperliquid]], Binance, dYdX, GMX |
| Settlement | Typically stablecoins ([[USDC]], USDT) |
| Leverage | Up to 100x on some platforms |
| Regulation | Unregulated in the US |

---

## How funding rates work

When the perpetual trades above the underlying (longs dominate), longs pay shorts. When it trades below (shorts dominate), shorts pay longs. This creates arbitrage incentives that pull the contract price back toward the index.

---

## Beyond crypto (2025-2026)

[[Hyperliquid]]'s HIP-3 standard enabled third-party builders to deploy perpetuals tracking traditional assets — commodities, equity indices, pre-IPO stocks. [[trade.xyz]] emerged as the most prolific builder, creating commodity perps (oil, gold, silver) and the first officially licensed [[S&P 500]] perpetual (Mar 2026, with [[S&P Global]] data).

During the [[2026 Iran conflict market impact|Iran conflict]], commodity perpetuals on Hyperliquid served as weekend pricing windows when traditional markets were closed — the oil perp hit ~$500M daily volume.

---

## Related

- [[Hyperliquid]] — leading decentralized perps exchange
- [[trade.xyz]] — builder of commodity and equity perps
- [[Ventuals]] — pre-IPO perps on Hyperliquid
- [[S&P 500]] — first major index with officially licensed perp (Mar 2026)

*Source: Bloomberg, Mar 18, 2026*
