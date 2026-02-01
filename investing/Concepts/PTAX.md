---
aliases: [PTAX rate, BCB fixing, Brazilian FX fixing]
---
#concept #fx #brazil #benchmark

**PTAX** — The official USD/BRL exchange rate published daily by [[Banco Central do Brasil|BCB]]. Used as fixing rate for FX derivatives, futures settlement, and financial contracts. Calculated from dealer surveys, not transaction data.

---

## Definition

PTAX is the BRL/USD exchange rate (BRL per 1 USD) announced by BCB at approximately 1:15 PM São Paulo time. Published as both bid and offer rates.

| Feature | Detail |
|---------|--------|
| Expression | BRL per 1 USD |
| Publication | ~1:15 PM São Paulo time |
| Administrator | [[Banco Central do Brasil|BCB]] |
| Regulatory basis | Circular 3506/2010, updated by Circular 3537/2011 |

---

## Methodology (post-July 2011)

### Four daily surveys

BCB conducts four surveys of authorized FX dealers each business day:

| Survey | Time (São Paulo) |
|--------|------------------|
| 1 | 10:00 AM |
| 2 | 11:00 AM |
| 3 | 12:00 PM (noon) |
| 4 | 1:00 PM |

### Survey mechanics

1. BCB contacts dealers at random 2-minute interval within 10-minute window starting on the hour
2. Dealers provide current bid and ask prices reflecting market conditions
3. BCB discards two highest and two lowest quotes (both bid and ask)
4. Calculates arithmetic average of remaining quotes
5. Derives bid/ask midpoint
6. Applies 0.0004 spread to midpoint:
   - **Bid** = midpoint − 0.0004
   - **Offer** = midpoint + 0.0004

### Publication

Final PTAX published "immediately" after last 1:00 PM survey is processed — typically around 1:15 PM. No formal deadline, but BCB commits to immediate release.

---

## Historical evolution

| Period | Methodology |
|--------|-------------|
| Pre-1990 | Administered rates set by BCB |
| 1990-1992 | Free market rates (Resolution 1690/1990) |
| 1992-2011 | Volume-weighted average of all interbank trades |
| 2011-present | Dealer survey method (Circular 3506/2010) |

The 2011 change moved from transaction-based to survey-based methodology, making PTAX more resilient to thin trading or manipulation.

---

## Use in financial markets

### NDF settlement

| Market | Fixing | Settlement |
|--------|--------|------------|
| **Onshore** | PTAX offer rate, T-1 | T |
| **Offshore** | PTAX offer rate, T-2 | T |

NDFs reference PTAX as the official rate for cash settlement.

### Futures settlement

[[B3]] Brazilian Real futures (6L at CME) settle at reciprocal of PTAX offer rate on last business day of month.

### [[Cupom cambial]] calculation

DDI (dirty cupom) uses previous day's PTAX in calculation, creating "gap risk" from overnight FX movements. This is why FRC (clean cupom) structures exist.

### Corporate contracts

Many USD-linked contracts in Brazil reference PTAX:
- Import/export invoicing
- USD-indexed debt
- Cross-currency swap valuations
- Transfer pricing

---

## PTAX vs spot market

| Aspect | PTAX | Spot market |
|--------|------|-------------|
| Source | Dealer survey | Actual transactions |
| Timing | Four daily fixings | Continuous |
| Manipulation risk | Lower (survey, trimmed mean) | Potentially higher |
| Use | Official fixing, derivatives | Immediate execution |

PTAX may diverge slightly from spot market at fixing time due to methodology differences.

---

## BCB intervention context

When BCB intervenes in FX markets, PTAX reflects intervention impact:
- **Spot sales** — direct PTAX impact
- **Swap cambial** — affects [[Cupom cambial]], indirect PTAX impact via arbitrage
- **Casadão** — targets cupom without direct PTAX impact

---

## Data access

BCB publishes historical PTAX data through:
- BCB Open Data Portal
- BCB Time Series Management System (SGS)
- Daily bulletins

Free access to full historical series.

---

## Related

- [[Banco Central do Brasil]] — administrator
- [[Cupom cambial]] — uses PTAX in DDI calculation
- [[B3]] — futures reference PTAX for settlement
- [[Cross-currency swaps]] — valuations reference PTAX
- [[Brazil]] — market context
- [[US dollar]] — counter currency
