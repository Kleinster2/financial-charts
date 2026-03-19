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

## Why perps over traditional futures

Perpetuals offer structural advantages over CME-style futures, particularly for non-US and retail participants:

- 24/7 trading — no market hours, no weekends off. During the [[2026 Iran conflict market impact|Iran conflict]], perps were the only way to express a view when CME/ICE were closed. Events on a Saturday night can be traded immediately, not Monday at 9:30 AM.
- Leverage without a broker — no futures account, no prime broker, no margin approval process, no KYC (for non-US users on decentralized platforms). Connect a wallet, post [[USDC]] collateral, trade. Democratizes access to leveraged index/commodity exposure.
- No expiration management — CME futures roll quarterly, requiring active position management and incurring roll costs. Perps run indefinitely.
- Stablecoin settlement — no USD banking rails needed. For non-US investors with limited dollar access, stablecoin-denominated positions bypass the traditional correspondent banking system entirely.
- DeFi composability — perp positions can theoretically serve as collateral in other DeFi protocols, creating capital efficiency that siloed traditional accounts cannot.

The cost: funding rates function as a carry cost. When the crowd is net long (typical for equity indices), longs pay shorts a periodic fee. Over time this erodes returns — it's the price of convenience and 24/7 access. And for assets like the [[S&P 500]] perpetual on [[Hyperliquid]], when all traditional markets are closed, the contract price is set by [[trade.xyz]]'s internal model rather than actual index data — a trust dependency that institutional participants will weigh carefully.

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
