---
aliases:
  - Ventuals Protocol
tags:
  - actor
  - private
  - defi
  - derivatives
---

# Ventuals

**Ventuals** is a decentralized derivatives protocol building perpetual futures markets on pre-IPO company valuations and thematic public stock indices, built on [[Hyperliquid]]'s HIP-3 orderbook standard. Incubated at [[Paradigm]].

## Synopsis

Ventuals attacks one of the biggest structural barriers in modern markets: the decade-long gap between when companies become transformative and when retail investors can access them. In the 1990s, companies IPO'd within a few years; today, firms like [[SpaceX]], [[OpenAI]], and [[Anthropic]] stay private for 10+ years, locking gains behind accredited-investor walls and opaque secondary markets. Ventuals creates synthetic perpetual contracts tied to these private valuations - no equity ownership, no accredited status required, just speculation on whether a company's total valuation goes up or down, settled in USDH (a dollar-pegged stablecoin on Hyperliquid).

The protocol also offers thematic index perps on public equities - baskets tracking semiconductors (SMH), robotics (BOTZ), nuclear (NLR), defense (SHLD), Mag 7 (MAGS), and more - with up to 20x leverage. Private company perps are capped at 3x leverage with tight open interest limits ($3-5M per market), reflecting the illiquidity and oracle complexity of pricing companies that don't trade on exchanges. The oracle uses a hybrid 50/50 blend of offchain data (secondary transactions, funding rounds, 409A valuations, mutual fund marks) and onchain trading data (8-hour EMA of mark prices). This is the hardest part of the design - private company price discovery is genuinely difficult, and the oracle's accuracy is the protocol's biggest risk factor.

Cumulative volume crossed $215M by mid-February 2026 with ~5,300 unique traders and $70K+ in fees since the October 2025 mainnet launch. Small numbers, but the product is live and growing - volume doubled in 17 days per The Defiant. DefiLlama shows annualized revenue around $353K. The team is lean (4-5 full-time) and builds from [[Paradigm]]'s SoHo office.

## Quick stats

| Metric | Value |
|--------|-------|
| **Founded** | 2024 |
| **HQ** | New York (Paradigm office, SoHo) |
| **Founders** | Alvin Hsia + sister (both ex-[[Airbnb]]) |
| **Team size** | 4-5 FT + part-time contributors |
| **Incubator** | [[Paradigm]] (EIR program, 2023) |
| **Chain** | [[Hyperliquid]] (HIP-3) |
| **Settlement** | USDH (dollar-pegged stablecoin) |
| **Cumulative volume** | ~$215M (as of mid-Feb 2026) |
| **Unique traders** | ~5,300 |
| **Fees generated** | $70K+ |
| **Annualized revenue** | ~$353K (DefiLlama) |
| **Mainnet launch** | October 2025 |
| **Token** | vHYPE (liquid staking derivative for HYPE) |

## Evolution

The story of Ventuals is the story of two siblings searching for the right idea in the right ecosystem.

- **2020:** Alvin Hsia and his sister leave [[Airbnb]] (where she spent six years on search engineering) to go full-time crypto. They'd built their technical foundation at Airbnb and wanted to apply it to a space with more greenfield opportunity.

- **2022:** Contracting phase - they work with several DeFi companies, learning the landscape and searching for ideas that could scale globally. This wasn't aimless; it was deliberate pattern-matching across the DeFi stack.

- **Early 2023:** Join [[Paradigm]] as Entrepreneurs in Residence. They build Shadow, an onchain data simulation platform that lands real paying customers (Pendle, Uniswap, OP Labs). Shadow proves they can ship and find product-market fit, but the TAM is too narrow. The realization that tooling wouldn't sustain their ambitions pushes them toward a bigger idea.

- **Early 2024:** Pivot to pre-IPO perpetuals - the thesis that private company valuations are a trillion-dollar asset class locked behind gatekeepers. They start building what becomes Ventuals. Around April 2024, they discover [[Hyperliquid]] while looking for a venue to trade assets unavailable elsewhere. The execution speed and UX impress them enough to make it their primary trading platform.

- **2024-2025:** [[Hyperliquid]] introduces HIP-3, a standard that lets builders deploy their own perpetual markets on Hyperliquid's orderbook infrastructure. This is the missing piece - HIP-3 gives Ventuals the infrastructure to create custom perp markets without building an entire exchange from scratch.

- **October 2025:** Mainnet launch. First markets: SpaceX, OpenAI, Anthropic perps (3x leverage, $3-5M OI caps). Also launches vHYPE, a liquid staking derivative for Hyperliquid's HYPE token, as a bootstrapping mechanism.

- **February 2026:** Volume surges past $215M cumulative. Platform adds thematic index perps (Mag 7, semiconductors, robotics, nuclear, defense, energy, biotech, infotech) with 20x leverage and $10M OI caps.

## Market design

### Private company perps

Traders speculate on total company valuations, divided by 1 billion for readability. A $420.69B SpaceX valuation = $420.69 per SPACEX contract. No equity ownership - purely synthetic.

| Market | Max leverage | OI cap |
|--------|-------------|--------|
| SPACEX | 3x | $5M |
| OPENAI | 3x | $5M |
| ANTHROPIC | 3x | $3M |

### Thematic index perps

Track public ETFs as sector proxies:

| Market | Tracks | Max leverage | OI cap |
|--------|--------|-------------|--------|
| MAG7 | MAGS ETF | 20x | $10M |
| SEMIS | SMH ETF | 20x | $10M |
| ROBOT | BOTZ ETF | 20x | $10M |
| NUCLEAR | NLR ETF | 20x | $10M |
| DEFENSE | SHLD ETF | 20x | $10M |
| ENERGY | XLE ETF | 20x | $10M |
| INFOTECH | XLK ETF | 20x | $10M |
| BIOTECH | XBI ETF | 20x | $10M |

### Oracle mechanics

The hybrid oracle is the most critical - and fragile - component:
- **Offchain (50%):** Verified secondary transactions, fundraising rounds, mutual fund marks, 409A valuations, peer comparisons
- **Onchain (50%):** 8-hour EMA of recent mark prices
- **Funding:** Hourly payments between longs and shorts to keep perp prices aligned with oracle. Uses a dampening multiplier (0.04575 on testnet) allowing wider divergence than crypto perps with real-time spot feeds
- **Mark price:** Unbiased reference for PnL and liquidations - prevents manipulation during volatility

### The oracle problem (vs [[Polymarket]])

[[Polymarket]]'s oracle is easy mode - binary events (did Trump win? did the Fed cut?) are publicly verifiable facts with no ambiguity. Ventuals' oracle is playing on hard mode: what's [[SpaceX]] worth *right now*? The answer depends on who you ask:

| Source | Implied valuation | Problem |
|--------|------------------|---------|
| Last funding round | Highest | Structured terms (liquidation prefs, ratchets) inflate headline numbers |
| Mutual fund marks | Conservative | Lagging, updated quarterly at best |
| Secondary sales ([[Forge Global]]) | Variable | Thin market, selection bias (sellers often bearish employees) |
| 409A valuation | Lowest | Deliberately conservative for tax purposes |

The "real" valuation is simultaneously all of these numbers. Ventuals blends them 50/50 with onchain trading data - but the onchain component is just other traders' guesses about the same opaque number. The circularity is structural.

**Why this matters:**

- **Manipulation surface:** On [[Polymarket]], you can't fake an election result. On Ventuals, anyone with knowledge of an upcoming secondary transaction can front-run the oracle update. The information asymmetry between insiders and public traders is structural, not incidental.
- **Stale pricing:** Private valuations update maybe quarterly. Between updates, the oracle is flying blind and the onchain component is pricing rumors and vibes. When a company raises a new round and the oracle jumps 15%, everyone on the wrong side gets liquidated by what's essentially a scheduled information event insiders knew about first.
- **No arbitrage anchor:** Crypto perps stay honest because if BTC-PERP diverges from BTC spot, arbitrageurs close the gap. There's no SpaceX spot market. If Ventuals' price drifts 20% from reality, there's no correction mechanism besides the next oracle update - which might be months away.
- **Funding rate distortion:** Hourly funding payments assume the oracle price is "truth" and penalize deviation from it. If the oracle is stale or wrong, funding payments tax traders for being *more correct* than the oracle.

The bull case despite all this: markets don't need perfect oracles - they need good enough ones. The stock market ran for decades on delayed, imperfect information. The 3x leverage cap and $3-5M OI limits suggest the team knows the oracle isn't battle-tested - they're deliberately keeping the blast radius small.

The real test is a major private market repricing. When the next AI winter hits and private lab valuations get cut 40-60% simultaneously, does the oracle keep up? Or do traders get trapped while it slowly catches up to reality? That's when you find out if it's a market or a casino.

## Investment case

### Bull
- **Massive TAM:** Private markets are a multi-trillion dollar asset class with virtually no retail access. If Ventuals becomes the [[Polymarket]] of private company speculation, the ceiling is high
- **Right ecosystem:** [[Hyperliquid]] is the fastest-growing perps DEX, and HIP-3 gives builders a credible orderbook infrastructure without building from scratch
- **[[Paradigm]] pedigree:** Incubated at one of crypto's most respected VCs, which provides credibility, office space, and network effects
- **Lean team, real traction:** 4-5 people generating $215M cumulative volume is capital-efficient

### Bear
- **Oracle risk is existential:** Private company valuations are inherently opaque and infrequently updated. A stale or manipulated oracle could blow up the system. The 50/50 onchain/offchain blend is a reasonable design, but "reasonable" isn't "battle-tested"
- **Tiny scale:** $215M cumulative volume and $353K annualized revenue is negligible. The $3-5M OI caps on private perps mean this is more demo than market
- **Regulatory target:** Synthetic equity derivatives on private companies screams [[SEC]] attention. No token offering protects against all risk, and the fact that it's DeFi doesn't make it immune
- **Liquidity chicken-and-egg:** Private perps need market makers willing to take the other side of illiquid, hard-to-hedge positions. The OI caps suggest this hasn't been solved yet
- **Competitor risk:** Jarsy, PreStocks, and others are also tokenizing pre-IPO access. First mover doesn't mean winner in DeFi

## Competitors

- **Jarsy** - tokenized pre-IPO stocks
- **PreStocks** - similar pre-IPO equity exposure
- **Ostium** - pool-based RWA perps (different model - Ventuals uses orderbook)

## Related

- [[Hyperliquid]] - underlying L1 and orderbook infrastructure
- [[Paradigm]] - incubator, EIR program
- [[SpaceX]] - flagship listed market
- [[OpenAI]] - listed market
- [[Anthropic]] - listed market
- [[Private Market Access]] - the broader landscape of retail private equity vehicles (closed-end funds, ETFs) that Ventuals competes with
- [[Private market secondaries]] - traditional secondary market for private shares
- [[Tokenized private shares]] - the crypto-native approach Ventuals belongs to
- [[Forge Global]] - traditional secondary marketplace
- [[Carta]] - cap table / private market infrastructure
- [[Derivatives primer]] - perpetual futures mechanics
