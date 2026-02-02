---
aliases: [gamma squeeze, dealer gamma, gamma hedging, delta hedging feedback]
---
#concept #options #market-structure #derivatives

**Gamma squeeze** — A feedback loop where options market makers (dealers) are forced to buy or sell the underlying asset to hedge their positions, amplifying price moves in both directions. Occurs when heavy call or put option buying creates large dealer short gamma positions.

> **Key insight:** Gamma squeezes work both ways. The same mechanics that drive parabolic rallies can reverse into violent crashes when sentiment shifts.

---

## Mechanics

### Delta and gamma basics

| Greek | Definition | Dealer impact |
|-------|------------|---------------|
| **Delta** | Option price sensitivity to underlying | Determines hedge ratio |
| **Gamma** | Rate of change of delta | Determines hedge adjustment frequency |

When dealers sell call options to customers, they are **short gamma** — meaning they must:
- **Buy** the underlying as price rises (delta increases)
- **Sell** the underlying as price falls (delta decreases)

This creates a feedback loop.

---

## The squeeze dynamic

### Rally phase (long underlying squeeze)

```
Customers buy calls → Dealers short calls → Dealers buy underlying to hedge
                                                           ↓
                                           Price rises → Delta increases
                                                           ↓
                              Dealers buy more underlying → Price rises further
                                                           ↓
                                                  Repeat (reflexive loop)
```

### Reversal phase (crash)

```
Price falls → Delta decreases → Dealers sell underlying to rebalance hedge
                                                           ↓
                                           Price falls further → Delta decreases more
                                                           ↓
                              Dealers sell more underlying → Price falls further
                                                           ↓
                                                  Repeat (reflexive loop)
```

---

## Conditions for gamma squeeze

| Condition | Why it matters |
|-----------|----------------|
| **Heavy call OI** | Large dealer short gamma position |
| **Near-the-money strikes** | Highest gamma = most hedging activity |
| **Short time to expiry** | Gamma increases as expiration approaches |
| **Low liquidity** | Hedging activity has outsized price impact |
| **Momentum/trend followers** | Amplify directional moves |

---

## Why it reverses violently

### Going up

- As calls go in-the-money, delta approaches 1.0
- Gamma decreases for deep ITM options
- Hedging pressure stabilizes (less need to buy more)

### Coming down

- As price falls, delta decreases rapidly
- Dealers must sell what they bought during rally
- If calls expire worthless, no remaining hedge needed
- All buying pressure disappears simultaneously

**Key point:** The buying that drove the rally was not fundamental demand — it was mechanical hedging. When hedging needs reverse, so does the price.

---

## Case study: [[Silver crash January 2026]]

### The setup

| Metric | Value |
|--------|-------|
| SLV call option OI | Record levels |
| SLV call volume | Exceeded QQQ (Nasdaq 100 ETF) |
| Silver peak | $121/oz |

### The unwind

| Event | Mechanic |
|-------|----------|
| Dollar rallies on [[Kevin Warsh]] news | Triggers profit-taking |
| Silver drops | Call deltas decrease |
| Dealers sell to rebalance | Accelerates decline |
| Calls go OTM | Delta approaches zero |
| Silver drops 26% in <20 hours | Largest single-day drop on record |

**Analyst observation:** "As we squeeze up, they have to mechanically keep buying more. And that would explain why we go up so fast, and down so fast." — Alexander Campbell, former Bridgewater commodities head

---

## Other notable gamma squeezes

| Event | Asset | Direction | Outcome |
|-------|-------|-----------|---------|
| **GameStop** (Jan 2021) | GME | Up then down | +1,600% then -90% |
| **AMC** (2021) | AMC | Up then down | Similar pattern |
| **Tesla** (2020) | TSLA | Up | Call buying drove rally to S&P inclusion |
| **Silver crash** (Jan 2026) | SLV | Down | 26% single-day drop |

---

## Market structure implications

### For investors

| Consideration | Detail |
|---------------|--------|
| Recognize momentum | Heavy call OI = potential squeeze setup |
| Beware reversals | Same mechanics work in reverse |
| Check option flow | Unusual call volume signals gamma dynamics |
| Size matters | Smaller markets (silver) more susceptible |

### For market stability

| Concern | Detail |
|---------|--------|
| Fragility | Options-driven markets can gap violently |
| Feedback loops | Hedging creates non-fundamental price moves |
| Liquidity illusion | Prices can move faster than fundamentals justify |

---

## Detecting gamma squeeze conditions

### Indicators

| Signal | Interpretation |
|--------|----------------|
| Call/put ratio spike | Heavy call buying = short gamma buildup |
| Rising OI + rising price | New positions driving move |
| Near-term expiry concentration | Gamma highest near expiration |
| Dealer positioning reports | Direct measure of gamma exposure |

### Red flags for reversal

| Signal | Interpretation |
|--------|----------------|
| Price gap down | Triggers dealer selling |
| Expiration approaching | Gamma effects intensify |
| Catalyst for profit-taking | Any reason for longs to exit |
| Declining call OI | Positions closing = hedges unwinding |

---

## Relationship to other concepts

| Concept | Connection |
|---------|------------|
| **Short squeeze** | Similar feedback loop, but via short covering |
| **Reflexivity** | Gamma squeeze is reflexivity via options |
| **Market microstructure** | Dealer hedging is market-making mechanics |
| **Volatility smile** | Gamma effects influence implied volatility |

---

## Mathematical note

Gamma (Γ) is highest when:
- Option is at-the-money (ATM)
- Time to expiration is short
- Implied volatility is low

```
Γ = N'(d₁) / (S × σ × √T)
```

Where N'(d₁) is the standard normal PDF. As T → 0 for ATM options, gamma spikes — explaining why expiration weeks often see violent moves in heavily-optioned stocks.

---

*Created 2026-02-01*

---

## Related

- [[Silver crash January 2026]] — case study (26% single-day drop)
- [[Options]] — underlying instrument
- [[Delta hedging]] — the hedging behavior that creates squeezes
- [[Market microstructure]] — broader context
- [[Reflexivity]] — Soros's theory applicable here
- [[Volatility]] — gamma squeezes create vol spikes
