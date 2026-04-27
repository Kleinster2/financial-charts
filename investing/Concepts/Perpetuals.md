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

When the perpetual trades above the underlying (longs dominate), longs pay shorts. When it trades below (shorts dominate), shorts pay longs. This creates arbitrage incentives that pull the contract price back toward the index. Rates typically reset every 8 hours.

For a structurally-upward asset like the [[S&P 500]], the crowd is almost always net long, which means longs are almost always paying. Typical ranges:

| Market condition | Funding rate (per 8h) | Annualized drag |
|------------------|-----------------------|-----------------|
| Calm / neutral | ~0.01% | ~1.1% |
| Bullish / euphoric | 0.1%+ | 13%+ |
| Panic (shorts dominate) | Negative (shorts pay longs) | Rare, temporary |

The funding rate is effectively a variable financing cost — analogous to margin interest on a leveraged stock position or the roll cost on CME futures, but market-driven rather than fixed. For short-term tactical trades (catching weekend geopolitical news), the cost is negligible. For buy-and-hold, cumulative drag could run several percentage points annually. A serious long-term holder would compare total cost (funding + spread) against SPY on margin or E-mini futures roll costs.

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

## Perps vs ETFs: not the same product

Perpetuals cannot compete with an [[S&P 500]] ETF for long-term holding:

| Vehicle | Annual cost | Use case |
|---------|------------|----------|
| SPY / VOO / IVV | 0.03-0.09% expense ratio | Buy-and-hold |
| S&P 500 perp | ~1-13% funding drag (variable) | Trading / tactical |

Even in calm markets, the perp costs 10-30x more than the ETF. In a melt-up, funding spikes can destroy the return differential entirely. Perps are a trading instrument, not a savings vehicle.

Perps compete on a different axis — access and flexibility, not cost:
- Non-US investors without US brokerage access
- Users in sanctioned jurisdictions or without banking rails
- Traders who need 24/7 exposure or want to hedge weekend gap risk
- Leverage without broker approval

The closest traditional analog is the CFD (contract for difference): similarly leveraged, carries overnight financing costs, and is banned in the US but popular globally. Perps are effectively decentralized CFDs with stablecoin settlement and no counterparty broker.

Where perps may matter most to traditional investors is as a price discovery signal. The [[S&P 500]] officially prices 6.5 hours a day, five days a week. The perp prices 24/7 — making it a real-time sentiment indicator for how the market should open. CME E-mini futures resume Sunday evening but don't trade all weekend. When [[Ras Laffan]] gets hit on a Saturday evening, the perp reprices within minutes — a market-priced view on what the event means for US equities, hours before futures reopen. For macro traders and risk managers, the signal value may exceed the trading value.

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
- [[Century Bond]] — 100-year corporate bonds; closest fixed-income analog to perpetual issuer financing

### Cross-vault
*Note: this page covers crypto perpetual futures contracts. The historical sovereign perpetual bonds — also instruments that "never expire" — are a different asset class with a four-century history.*
- [History: British Consols](obsidian://open?vault=history&file=04%20-%20Early%20Modern%2FBritish%20Consols) — perpetual sovereign bond, 1751-2015
- [History: French Rentes](obsidian://open?vault=history&file=04%20-%20Early%20Modern%2FFrench%20Rentes) — perpetual sovereign annuity, 1522-1958

*Source: Bloomberg, Mar 18, 2026*
