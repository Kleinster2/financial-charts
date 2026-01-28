#concept #derivatives #options #trading #primer

**Derivatives primer** — foundational options, futures, and volatility concepts for trading and risk management. Understanding derivatives helps evaluate hedging strategies, market positioning, and volatility dynamics.

> **Key insight:** Derivatives are zero-sum — every winner has a loser. They transfer risk, they don't eliminate it. The question is always: who is on the other side, and why?

---

## What are derivatives?

Contracts whose value derives from an underlying asset.

| Type | Underlying | Use |
|------|------------|-----|
| **Options** | Stocks, ETFs, indices | Hedging, speculation, income |
| **Futures** | [[Commodities]], indices, rates | Hedging, speculation |
| **Swaps** | Interest rates, currencies | Risk management |
| **Forwards** | Currencies, commodities | Custom hedging |

---

## Options basics

**Right, not obligation** to buy (call) or sell (put) at a set price.

| Term | Definition |
|------|------------|
| **Call** | Right to buy |
| **Put** | Right to sell |
| **Strike** | Price at which you can buy/sell |
| **Premium** | Price paid for the option |
| **Expiration** | When option expires |
| **Exercise** | Use the option |

### Call option example

```
Buy AAPL $200 Call for $5, expiring in 30 days

If AAPL at $220 at expiration:
  Exercise: Buy at $200, worth $220 = $20 value
  Profit: $20 − $5 premium = $15

If AAPL at $190 at expiration:
  Don't exercise (would lose money)
  Loss: $5 premium (maximum loss)
```

### Put option example

```
Buy AAPL $200 Put for $5

If AAPL at $180:
  Exercise: Sell at $200, worth $180 = $20 value
  Profit: $20 − $5 = $15

If AAPL at $210:
  Don't exercise
  Loss: $5 premium
```

---

## Option moneyness

| Status | Call | Put |
|--------|------|-----|
| **In-the-money (ITM)** | Stock > Strike | Stock < Strike |
| **At-the-money (ATM)** | Stock ≈ Strike | Stock ≈ Strike |
| **Out-of-the-money (OTM)** | Stock < Strike | Stock > Strike |

ITM options have intrinsic value. OTM options have only time value.

---

## Option value components

```
Option Price = Intrinsic Value + Time Value

Intrinsic: How much option is worth if exercised now
Time Value: Extra value from time remaining + volatility
```

| Component | Call intrinsic | Put intrinsic |
|-----------|----------------|---------------|
| Formula | max(Stock − Strike, 0) | max(Strike − Stock, 0) |

**Time value:** Decays as expiration approaches (theta). Higher with more time, higher volatility.

---

## The Greeks

Measure how option prices change with different factors.

| Greek | Measures sensitivity to | Range |
|-------|------------------------|-------|
| **Delta (Δ)** | Underlying price | 0 to 1 (calls), −1 to 0 (puts) |
| **Gamma (Γ)** | Change in delta | Highest ATM |
| **Theta (Θ)** | Time decay | Negative for long options |
| **Vega (ν)** | Volatility | Positive for long options |
| **Rho (ρ)** | Interest rates | Usually minor |

### Delta

```
Delta = 0.50: Option moves $0.50 for every $1 move in stock
```

| Option | Typical delta |
|--------|---------------|
| Deep ITM call | ~1.0 |
| ATM call | ~0.50 |
| OTM call | ~0.20 |
| ATM put | ~−0.50 |

**Delta as probability:** Rough approximation of probability option expires ITM.

### Gamma

Rate of change of delta. Highest for ATM options near expiration.

**Gamma risk:** Near expiration, ATM options have explosive gamma. Small moves in stock cause large swings in delta.

### Theta

Time decay — options lose value each day.

```
ATM option loses most theta value
Theta accelerates near expiration
```

**Theta as rent:** Option buyers pay theta. Option sellers collect it.

### Vega

Sensitivity to implied volatility.

```
If vega = 0.10 and IV rises 1%:
  Option price increases $0.10
```

Long options benefit from rising IV. Short options suffer.

---

## Implied volatility (IV)

Market's expectation of future volatility, derived from option prices.

```
Higher IV → Higher option prices
Lower IV → Lower option prices
```

### IV vs realized volatility

| Concept | Definition |
|---------|------------|
| **Implied vol (IV)** | Expected future vol (from option prices) |
| **Realized vol (RV)** | Actual historical vol |
| **Variance premium** | IV − RV (usually positive) |

**IV typically > RV:** Options systematically overpriced. This is why option selling strategies exist.

### VIX

[[CBOE]] Volatility Index — implied vol of S&P 500 options.

| VIX level | Market regime |
|-----------|---------------|
| <15 | Low vol, complacent |
| 15-20 | Normal |
| 20-30 | Elevated fear |
| >30 | High fear, crisis |

**VIX spikes:** Fast during selloffs, slow to decline. "Takes stairs up, elevator down."

---

## Volatility surface

IV varies by strike and expiration.

### Volatility smile/skew

| Pattern | Shape | Cause |
|---------|-------|-------|
| **Skew** | OTM puts > ATM > OTM calls | Crash protection demand |
| **Smile** | Both OTM puts and calls > ATM | Fat tails expected |
| **Flat** | Same IV across strikes | Rare |

**Equity skew:** Puts typically more expensive than calls (crash protection).

### Term structure

| Pattern | Shape | Implication |
|---------|-------|-------------|
| **Contango** | Near-term < long-term IV | Normal, calm markets |
| **Backwardation** | Near-term > long-term IV | Fear, expecting near-term move |

---

## Common option strategies

### Directional

| Strategy | Structure | View |
|----------|-----------|------|
| **Long call** | Buy call | Bullish |
| **Long put** | Buy put | Bearish |
| **Call spread** | Buy call, sell higher call | Moderately bullish |
| **Put spread** | Buy put, sell lower put | Moderately bearish |

### Income/Neutral

| Strategy | Structure | View |
|----------|-----------|------|
| **Covered call** | Own stock, sell call | Neutral/mildly bullish |
| **Cash-secured put** | Sell put, hold cash | Neutral/mildly bullish |
| **Iron condor** | Sell OTM put spread + call spread | Range-bound |
| **Straddle** | Buy ATM call + put | Big move expected |
| **Strangle** | Buy OTM call + put | Big move expected (cheaper) |

### Volatility

| Strategy | Structure | Vol view |
|----------|-----------|----------|
| **Long straddle** | Buy call + put | Long vol |
| **Short straddle** | Sell call + put | Short vol |
| **Calendar spread** | Sell near, buy far | Vol term structure |

---

## Put-call parity

Fundamental relationship between puts, calls, stock, and bonds.

```
Call − Put = Stock − PV(Strike)

Or rearranged:
Stock + Put = Call + PV(Strike)
```

**Arbitrage enforces this.** If violated, traders exploit until restored.

---

## Futures basics

**Obligation** (not right) to buy/sell at set price on future date.

| Feature | Options | Futures |
|---------|---------|---------|
| Obligation | No | Yes |
| Premium | Paid upfront | No (margin only) |
| Daily settlement | No | Yes (mark-to-market) |
| Leverage | Limited to premium | High (margin ~5-10%) |

### Futures pricing

```
Futures Price = Spot × (1 + r − d)^t

r = risk-free rate
d = dividend yield
t = time to expiration
```

### Contango vs backwardation

| Term | Futures vs Spot | Cause |
|------|-----------------|-------|
| **Contango** | Futures > Spot | Storage costs, financing |
| **Backwardation** | Futures < Spot | Supply shortage, convenience yield |

**Roll yield:** In contango, rolling futures loses money (buy high, sell low). In backwardation, rolling gains.

---

## Margin and leverage

### Futures margin

| Type | Purpose |
|------|---------|
| **Initial margin** | Required to open position |
| **Maintenance margin** | Minimum to keep position |
| **Variation margin** | Daily P&L settlement |

**Leverage:** $10,000 margin controls $100,000 notional = 10x leverage.

### Options margin

- **Buying options:** Pay premium, no margin
- **Selling options:** Margin required (potential loss large)

---

## Hedging with derivatives

### Portfolio hedging

| Hedge | Protection | Cost |
|-------|------------|------|
| **Buy puts** | Downside protection | Premium |
| **Collar** | Buy puts, sell calls | Reduced (give up upside) |
| **Futures short** | Full hedge | Opportunity cost |

### Delta hedging

Market makers stay delta-neutral by adjusting stock position as delta changes.

```
If short call with delta 0.50:
  Buy 50 shares per contract to hedge
  As stock moves, rebalance
```

---

## Greeks risk management

| Risk | Greek | Hedge |
|------|-------|-------|
| Price | Delta | Stock or options |
| Convexity | Gamma | Options only |
| Time | Theta | Nothing (pay or collect) |
| Vol | Vega | Options at different strikes/dates |

**Gamma-theta tradeoff:** Long gamma (benefit from moves) costs theta. Short gamma (collect theta) risks big moves.

---

## Market microstructure

### Bid-ask spread

| Wide spread | Narrow spread |
|-------------|---------------|
| Illiquid options | Liquid options |
| Far OTM | ATM |
| Long-dated | Near-dated |

**Cost:** Crossing spread is transaction cost. Market makers profit from spread.

### Open interest and volume

| Metric | Definition | Use |
|--------|------------|-----|
| **Volume** | Contracts traded today | Activity |
| **Open interest** | Contracts outstanding | Positioning |

Rising OI + rising price = new longs entering.
Falling OI + falling price = longs exiting.

---

## Options flow and positioning

### Max pain

Strike where most options expire worthless. Theory: market gravitates here.

### Gamma exposure (GEX)

Aggregate gamma of market makers. When GEX high:
- MMs delta hedge by buying dips, selling rips
- Suppresses volatility

When GEX low or negative:
- MMs hedge same direction as market
- Amplifies moves

### Put/call ratio

| Ratio | Interpretation |
|-------|----------------|
| High (>1.0) | Bearish sentiment (contrarian bullish) |
| Low (<0.7) | Bullish sentiment (contrarian bearish) |

---

## Key metrics for investors

| Metric | What it measures |
|--------|------------------|
| **VIX** | Market fear gauge |
| **Skew** | Tail risk pricing |
| **Term structure** | Near vs far vol expectations |
| **Put/call ratio** | Sentiment |
| **GEX** | Dealer positioning |
| **IV rank/percentile** | Vol relative to history |

---

## Related

- [[VIX]] — volatility index
- [[Volatility]] — vol concepts
- [[Options flow]] — positioning data
- [[Hedging]] — risk management
- [[Market microstructure]] — trading mechanics
