---
aliases: [foreign exchange coupon, cupom sujo, cupom limpo, DDI, FRC]
---
#concept #fx #brazil #derivatives

**Cupom cambial** — The onshore USD interest rate implied by Brazilian interest rate and FX futures markets. Represents the dollar return from converting USD→BRL, earning [[CDI]], and hedging FX risk back to USD. Critical benchmark for corporate FX hedging costs.

---

## Definition

Cupom cambial measures what a dollar-based investor would earn by:
1. Converting USD to BRL at spot
2. Investing in BRL instruments (earning CDI)
3. Hedging currency risk via FX futures

Conceptually: the difference between domestic BRL rates and expected exchange rate depreciation.

**Higher cupom cambial** → greater attractiveness for foreign capital to enter Brazil.

---

## Calculation

### From covered interest parity

Under no-arbitrage, investing in BRL or USD should yield equivalent returns when hedged:

```
Cupom = [(1 + DI rate) / (1 + FX depreciation)] - 1
```

**Example:** If Selic = 15% and expected BRL depreciation = 5%:
```
Cupom = [(1.15 / 1.05) - 1] = 9.52% annually
```

### From futures prices

```
Cupom = [(Dollar Futures / Spot Dollar) - 1] × (360 / calendar days)
```

**Day count:** Dollar interest calculated on linear 360-day basis, distinct from DI convention (exponential, 252 business days).

---

## DDI vs FRC (Dirty vs Clean)

### DDI — Cupom Cambial Sujo (Dirty)

| Feature | Detail |
|---------|--------|
| Type | Futures contract on [[B3]] |
| Calculation | Uses previous day's PTAX rate |
| Exposure | Contains overnight FX variation ("gap risk") |
| Quote | Annual linear rate, 360-day basis |

**Gap risk:** The DDI includes exposure to FX movements between prior day's PTAX fixing and current day. This "dirty" element creates unwanted volatility for hedgers.

### FRC — Forward Rate Agreement de Cupom Cambial (Clean)

| Feature | Detail |
|---------|--------|
| Type | Structured product (BM&F, launched 2001) |
| Calculation | Combines two DDI contracts with opposite positions |
| Exposure | Removes prior-day FX variation |
| Quote | Forward cupom rates starting at future dates |

**Why "clean":** The FRC structure eliminates gap risk by netting the overnight FX exposure. More practical for hedging.

### Casado operation

Combines spot and futures positions to calculate clean cupom. Standard method for practitioners.

---

## Where it trades

**[[B3]] (Brasil, Bolsa, Balcão):**

| Contract | Description |
|----------|-------------|
| **DDI** | Cupom cambial futures (dirty) |
| **FRC** | Forward rate agreements (clean) |
| **DOL** | Dollar futures |
| **DI** | Interbank deposit rate futures |

B3 acts as central counterparty with daily mark-to-market. Settlement prices calculated via no-arbitrage formulas.

---

## Why it matters for corporate treasurers

### FX hedging cost benchmark

Brazilian companies with USD debt but BRL revenues use cupom cambial to evaluate hedging costs.

| Instrument | Liquidity | Notes |
|------------|-----------|-------|
| NDFs | High | Most common hedging tool |
| [[Cross-currency swaps]] | Up to 5 years | For longer-term debt |
| DDI/FRC | Exchange-traded | More standardized |

All derivatives in Brazil are net-settled in BRL — currency is not fully deliverable offshore.

### Funding arbitrage

A high cupom cambial incentivizes:
1. Banks borrow USD abroad (cheap)
2. Convert to BRL domestically
3. Invest at higher BRL rates
4. Hedge FX risk

This arbitrage provides USD liquidity to the Brazilian economy.

### Relationship to cross-currency swaps

| Component | Role |
|-----------|------|
| CDI rate | BRL leg of swap |
| Cupom cambial | Implied USD rate onshore |
| Differential | Swap cost for BRL issuer hedging to USD |

For [[Scala Data Centers]] issuing BRL debentures + swapping to USD: the swap receive leg (CDI) minus pay leg (cupom cambial equivalent + bank spread) determines all-in USD cost.

---

## Historical behavior

### Normal conditions

- Cupom cambial sits above US interest rates (reflecting Brazil's higher domestic rates)
- Futures typically in contango (higher than spot)
- Arbitrage keeps onshore/offshore dollar rates aligned

### Crisis dynamics

| Crisis | Behavior | Indicator |
|--------|----------|-----------|
| **2002** (Lula election) | Cupom spiked extreme; futures fell below spot (backwardation) | Convertibility risk premium |
| **2008** (GFC) | Sharp capital outflows; BCB intervened via spot, swaps, repos | Spot market illiquidity |
| **2015** (recession) | GDP fell 3.5%; elevated cupom reflecting country risk | Political + commodity shock |

**Key insight:** The spread between cupom cambial and US rates serves as a liquidity stress indicator for Brazilian FX markets.

### Current levels (early 2025)

| Metric | Approximate |
|--------|-------------|
| DI rate | 14-15% |
| Fed funds | 4.25-4.50% |
| Cupom spread over US rates | ~9-10% |

---

## BCB intervention mechanism

### Swap cambial (traditional)

| Party | Position |
|-------|----------|
| BCB | Sells USD exposure, receives DI |
| Banks | Earn FX variation, pay interest |

**Effect:** Raises cupom cambial. Used during BRL weakness to provide dollar liquidity.

### Swap cambial reverso (reverse)

BCB buys USD exposure, pays DI rate. Used during BRL strength to absorb dollar inflows.

### Casadão operation

Simultaneous reverse swap + spot USD sale:
- BCB buys $1B reverse swaps
- BCB sells $1B spot

**Effect:** Targets cupom cambial without changing net FX exposure. Compresses cupom without directly affecting spot rate.

**Transmission:** Swap sales raise cupom → higher cupom incentivizes banks to bring spot dollars into Brazil → creates indirect pressure on spot rates via arbitrage.

---

## Onshore vs offshore

| Market | Features |
|--------|----------|
| **Onshore** | CETIP registration, BRL settlement, PTAX fixing |
| **Offshore** | NDF market, USD settlement, no PTAX exposure |

BRL is not fully convertible — no liquid deliverable offshore market.

**Offshore BRL curve construction:**
1. Start with USD [[SOFR]] curve
2. Add USD/BRL offshore NDF
3. Apply DI on/offshore spread adjustment

**Crisis behavior:** Normally, onshore USD futures arbitrage perfectly with offshore NDFs. During crises, spreads emerge reflecting convertibility risk.

---

## Related

- [[Cross-currency swaps]] — uses cupom cambial as implied USD rate
- [[Cross-currency basis]] — related CIP deviation concept
- [[CDI]] — BRL floating rate benchmark
- [[B3]] — exchange for DDI/FRC contracts
- [[Banco Central do Brasil]] — swap intervention
- [[Scala Data Centers]] — uses swaps referencing cupom
- [[Brazil]] — market context
- [[PTAX]] — BCB reference rate for fixing
