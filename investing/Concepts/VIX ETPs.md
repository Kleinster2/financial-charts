# VIX ETPs

Exchange-traded products that provide exposure to VIX futures, not spot VIX. The roll mechanics create structural decay (contango) or tailwinds (backwardation) that dominate returns over time.

## Key products

| Ticker | Type | Exposure | Notes |
|--------|------|----------|-------|
| **VXX** | ETN | 1x short-term futures | iPath, most liquid, ~50-70% annual decay |
| **UVXY** | ETF | 1.5x short-term futures | ProShares, leveraged decay |
| **VIXY** | ETF | 1x short-term futures | ProShares version of VXX |
| **SVXY** | ETF | -0.5x short-term futures | Inverse, profits from contango |
| **VXZ** | ETN | 1x medium-term futures | Less decay, less vol spike capture |

## Term structure mechanics

**Contango** (~80% of time): Futures > spot. Long products bleed as they roll into more expensive contracts. Short products profit.

**Backwardation** (fear spikes): Spot > futures. Long products spike. Short products get crushed.

The VIX term structure chart shows this directly:
- ^VIX below ^VIX3M/^VIX6M = contango = VXX bleeding
- ^VIX above ^VIX3M/^VIX6M = backwardation = VXX spiking

## Why you can't just short VXX

The decay is obvious, so why isn't shorting free money?

1. **Borrow cost** — 20-50%+ annualized, eats the edge
2. **Margin requirements** — brokers require high margin for short vol
3. **Left tail blowups** — VXX can spike 50-100%+ in days (March 2020: tripled)
4. **Infinite loss** — short positions have unlimited risk

## Volmageddon (Feb 5, 2018)

The day the short-vol trade blew up:

- VIX spiked from 17 to 37 after-hours (doubled)
- XIV (2x inverse VIX ETN) lost 90%+ and liquidated
- Credit Suisse terminated the product
- Retail traders who shorted VXX got margin called at the top
- ~$2B in losses in a single session

The structural problem: inverse VIX products had to buy VIX futures to rebalance as VIX rose, creating a feedback loop that accelerated the spike.

## Use cases

**Hedging**: Buy VXX/UVXY as portfolio insurance before known risk events. Accept the decay as cost of insurance.

**Speculation**: Trade around vol spikes. Long into fear, short after vol normalizes.

**Carry harvesting**: Short VXX or long SVXY to collect contango decay. Works until it doesn't — requires strict risk management and willingness to take losses during spikes.

## Structural issues

- **ETN credit risk** — VXX is a Barclays note, not an ETF. You're exposed to issuer default.
- **Tracking error** — products track futures, not spot VIX. Correlation breaks during fast moves.
- **Rebalancing drag** — leveraged products rebalance daily, creating path-dependent returns.
- **Liquidity gaps** — options on these products can have wide spreads during stress.

## Related

- [[VIX]] — the underlying index
- [[Carry trade]] — same risk profile as short vol
- [[Risk-on risk-off]] — vol regime context
