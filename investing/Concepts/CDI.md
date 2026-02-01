---
aliases: [Certificado de Depósito Interbancário, DI rate, interbank deposit rate]
---
#concept #rates #brazil #benchmark

**CDI** (Certificado de Depósito Interbancário) — Brazil's primary floating rate benchmark. The average overnight interbank deposit rate, published daily by [[B3|CETIP]]. Tracks [[Selic]] closely. Used as reference for most Brazilian floating-rate debt.

---

## Definition

CDI is the average interest rate on one-day interbank deposit transactions between institutions of different financial groups ("extra-grupo"). Excludes same-group transactions ("intra-grupo").

| Feature | Detail |
|---------|--------|
| Calculation | Volume-weighted average of overnight interbank deposits |
| Day count | 252 business days (exponential) |
| Publication | Daily by CETIP (now [[B3]]) |
| Expression | Percentage per annum |

---

## Current level

| Date | CDI |
|------|-----|
| Jan 2026 | 14.90% |

Historical range: 6.39% (Sep 2018 low) to hyperinflation extremes (1,826,019% in Feb 1994).

---

## How it works

1. Two institutions agree on an overnight deposit rate
2. Transaction registered with CETIP
3. CETIP transfers CDI ownership, creates credit
4. Credit impacts institution's reserve account at [[Banco Central do Brasil|BCB]] same day
5. Transaction reverses next day — purchaser receives reserves + interest

Only extra-grupo (different financial groups) one-day transactions count toward the published rate.

---

## Relationship to Selic

| Rate | Definition | Relationship |
|------|------------|--------------|
| **Selic** | BCB policy rate; overnight rate on government securities repos | Target set by COPOM |
| **CDI** | Interbank deposit rate | Tracks Selic very closely |

CDI typically runs a few basis points below Selic target. The spread is minimal because both are overnight unsecured interbank rates.

---

## Use in financial instruments

### Floating-rate debt

Most Brazilian corporate debentures are CDI-linked:
- [[Scala Data Centers]]: CDI + 2.0-2.4%
- [[Aura Minerals]]: CDI + 1.60%

Structure: Quarterly payments based on accumulated CDI over the period.

### Investment funds

Brazilian fixed income funds benchmark against:
- **% do CDI** — e.g., fund returning "102% do CDI" beats the benchmark
- Standard for money market and fixed income fund performance

### Derivatives

| Contract | Exchange | Notes |
|----------|----------|-------|
| **DI futures** | [[B3]] | Most liquid interest rate derivative in LatAm |
| **DDI** | [[B3]] | [[Cupom cambial]] futures (uses CDI) |
| **FRC** | [[B3]] | Forward rate agreements |

DI futures curve extends out 10+ years, providing term structure for BRL rates.

---

## Cross-currency swap context

In a [[Cross-currency swaps|cross-currency swap]], the BRL leg typically references CDI:

```
Brazilian issuer:
- Issues: BRL debentures at CDI + spread
- Swap receive leg: CDI + spread (offsets coupon)
- Swap pay leg: USD rate + FX variation
- Result: Synthetic USD debt
```

The CDI receive leg exactly offsets the debenture coupon, leaving only USD exposure.

---

## Technical details

| Specification | Detail |
|---------------|--------|
| Administrator | B3 (formerly CETIP) |
| Calculation | Daily average of extra-grupo overnight transactions |
| Day count convention | Exponential, 252 business days/year |
| Publication time | End of business day |
| Historical data | Available from March 1986 |

---

## Related

- [[Selic]] — BCB policy rate, CDI tracks closely
- [[B3]] — exchange/clearinghouse, publishes CDI
- [[Cupom cambial]] — implied USD rate, uses CDI in calculation
- [[Cross-currency swaps]] — BRL leg references CDI
- [[Scala Data Centers]] — CDI-linked debentures
- [[Aura Minerals]] — CDI-linked debentures
- [[Brazil]] — market context
- [[Banco Central do Brasil]] — monetary policy
