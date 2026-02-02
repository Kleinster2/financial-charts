---
aliases: [CCS, XCCY, cross-currency basis swap, currency swap]
---
#concept #derivatives #fx #hedging

**Cross-currency swaps** — OTC derivatives exchanging principal and interest in one currency for another. Used by corporates to convert debt into synthetic foreign currency obligations, matching liability currency to revenue currency.

---

## Mechanics

### Basic structure

Two parties exchange:
1. **Initial principal** in different currencies (at spot rate)
2. **Periodic interest payments** (fixed or floating in each currency)
3. **Final principal** re-exchange (at original spot rate, not current)

Unlike FX forwards, cross-currency swaps involve actual exchange of principal and ongoing interest — not just a single future settlement.

### Corporate use case

A Brazilian company with USD revenues but BRL debt:

```
Issue BRL debentures → Enter cross-currency swap
                      ├─ Receive: BRL floating (CDI) → offsets debenture coupon
                      └─ Pay: USD fixed/floating + FX variation

Result: Synthetic USD debt
```

**Why not borrow USD directly?**
- EM currencies often have restricted USD access onshore
- Local currency markets are deeper/more liquid
- Regulatory constraints on foreign currency borrowing
- Swap achieves same economics with better execution

---

## Brazilian market specifics

### BRL characteristics

| Feature | Detail |
|---------|--------|
| **Non-deliverable** | BRL cannot physically leave Brazil; derivatives settle in BRL domestically or USD offshore |
| **Day count** | BUS 252 (252 business days/year vs standard 360/365) |
| **Structure** | Often zero-coupon (both legs pay at maturity) |
| **Benchmark** | [[CDI]] (Certificado de Depósito Interbancário) |

### Cupom cambial

The implied onshore USD interest rate, derived from:

```
Cupom cambial = BRL interest rate − FX forward premium
```

Represents the cost of synthetic USD funding in Brazil. When cupom cambial is attractive vs offshore USD rates, the BRL issuance + swap structure becomes compelling.

### Onshore vs offshore

| Market | Settlement | Registration | Users |
|--------|------------|--------------|-------|
| **Onshore** | BRL | [[B3]] (CETIP) | Brazilian corporates |
| **Offshore (NDF)** | USD | None required | Foreign investors |

Brazilian corporates like [[Scala Data Centers]] execute swaps onshore, registered with B3.

---

## Pricing

### Components

The all-in cost of a local currency bond + cross-currency swap includes:

1. **Credit spread on bond** — issuer's funding cost in local market
2. **Swap spread** — bank's margin for executing the swap
3. **Cross-currency basis** — market premium for accessing USD
4. **Counterparty credit charge** — bank's view of issuer creditworthiness

### Cross-currency basis

The basis represents supply/demand imbalance for USD funding globally:

| Condition | Basis | Implication |
|-----------|-------|-------------|
| **Negative basis** | USD at premium | Paying extra to access USD (typical for EM) |
| **Positive basis** | USD at discount | Rare; receiving premium to take USD |
| **Wider basis** | Stress periods | Dollar shortage (2008: EUR/USD basis hit -120bp) |

EM currencies like BRL typically trade at wider (more negative) basis than G10, reflecting:
- Country risk
- Dollar scarcity
- Regulatory constraints
- Liquidity premium

---

## Regulatory framework (Brazil)

### BCB requirements

| Regulation | Requirement |
|------------|-------------|
| **Resolution 277 (2022)** | All OTC derivatives registered at B3 within 2 business days |
| **Resolution 3824 (2009)** | Derivatives contracted abroad must be registered |
| **Sistema Cambio** | FX trades require confirmation in central bank system |
| **Retention** | Documentation kept 10 years |

### Tax treatment

| Tax | Rate | Condition |
|-----|------|-----------|
| **IOF** | 0% | Hedging derivatives (Decree 7,699/2012) |
| **IRPJ/CSLL** | 130% deduction | Infrastructure debentures (Law 14,801/2024) |
| **Hedge losses** | Deductible | PM 1,303 aligned foreign/domestic treatment |

The 0% IOF for hedging is critical — standard derivative IOF can be significant.

**May 2025 IOF changes:** Government attempted to raise IOF rates but faced immediate backlash; Legislative Decree 176 suspended increases.

---

## Counterparties

### Brazil swap dealers

Major banks providing cross-currency swaps to Brazilian corporates:

| Bank | Notes |
|------|-------|
| [[Itaú BBA]] | Largest private bank in LatAm, top-tier derivatives desk |
| [[Bradesco BBI]] | Major local player, frequent lead coordinator |
| [[Santander Brasil]] | Full-service investment bank |
| [[BTG Pactual]] | #1 in Institutional Investor LatAm rankings |
| [[UBS BB]] | JV with Banco do Brasil |
| [[MUFG]] | Active in larger deals |

Debenture coordinating banks typically also provide swaps — they already have credit exposure, understand cash flows, and bundle fees.

### ISDA framework

Swaps governed by ISDA Master Agreements with:
- **Netting provisions** — net exposures across multiple trades
- **Credit Support Annex (CSA)** — collateral requirements
- **Close-out netting** — crystallize value on default

---

## Risks

### Counterparty risk

Swap dealer defaults before maturity, leaving company unhedged at potentially unfavorable rates.

**Mitigation:**
- Multiple counterparties
- Systemically important banks (too big to fail)
- ISDA netting reduces gross exposure
- Collateralization via CSA

### Basis risk

Mismatch between hedge and underlying exposure:
- Different benchmarks (CDI vs SOFR)
- Reset timing differences
- Tenor mismatch between debt and swap

**Mitigation:**
- Match swap tenor to debt maturity
- Use basis swaps to align benchmarks
- Dynamic hedging (adjust over time)

### Mark-to-market volatility

Swap value fluctuates with:
- FX rates
- Interest rate differentials
- Credit spreads

Creates accounting volatility even if economic hedge is effective. May trigger collateral calls if MTM moves against company.

### Rollover risk

If swap tenor < debt tenor, must refinance swap at potentially worse terms.

**Mitigation:** Match tenors (Scala's 6-year swap matches 6-year debenture).

### Regulatory risk

- IOF rules can change rapidly
- BCB can intervene in FX markets
- New regulations may affect hedge deductibility

---

## Comparable transactions

### Scala Data Centers (Aug 2024)

| Term | Detail |
|------|--------|
| Debt | BRL 1.37B green debentures (SCLL14/SCLL24) |
| Swap | 6-year USD overlay |
| Rationale | Match USD hyperscaler contract revenues |
| Counterparties | Likely Bradesco BBI, Itaú BBA, Santander, UBS BB |

### Aura Minerals Almas (Oct 2024)

| Term | Detail |
|------|--------|
| Debt | BRL 1.0B debentures |
| Swap | Full cross-currency with [[Itaú]] |
| Receive | CDI + 1.60% |
| Pay | BRL/USD exchange variation |

### Structure rationale

Both companies have USD revenues (hyperscaler contracts for Scala, gold sales for Aura) but access deep BRL debenture markets. Swap converts to synthetic USD, creating natural hedge.

---

## Government support

### Eco Invest Brasil

Announced at COP28, [[IDB]]-backed platform providing:
- Full FX swaps for sustainable investment
- Credit lines for FX exposure
- Exchange rate devaluation liquidity

Aimed at reducing currency risk for green infrastructure investment in Brazil.

### Law 14,801/2024

New infrastructure debenture framework:
- 30% additional IRPJ/CSLL deduction on interest
- Zero WHT on foreign loans for priority projects
- Allows exchange rate variation clauses (with authorization)

---

## Related

- [[Lei 4131]] — Brazil's foreign capital law; swaps often hedge 4131 loan FX exposure
- [[Scala Data Centers]] — example: BRL debentures + USD swap
- [[Aura Minerals]] — comparable transaction
- [[CDI]] — Brazilian floating rate benchmark
- [[B3]] — derivatives registration
- [[Green bonds]] — often paired with swaps for EM issuers
- [[Basis trade]] — related arbitrage concept
- [[Interest rate swaps]] — single-currency cousin
- [[FX forwards]] — simpler hedging instrument
- [[Brazil]] — regulatory context
- [[Itaú BBA]] — major swap dealer
- [[Bradesco BBI]] — major swap dealer
- [[MUFG]] — international swap dealer
- [[IDB]] — Eco Invest Brasil sponsor
