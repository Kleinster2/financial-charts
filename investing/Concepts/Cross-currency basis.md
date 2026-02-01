---
aliases: [CIP violation, xccy basis, FX basis, cross-currency basis swap]
---
#concept #fx #macro #funding

**Cross-currency basis** — The deviation from covered interest parity (CIP) in FX swap markets. Measures how much synthetic dollar funding via FX swaps costs relative to direct dollar borrowing. A negative basis means dollar shortage; wider (more negative) = more stress.

---

## Definition

The cross-currency basis indicates the amount by which the interest paid to borrow one currency by swapping it against another differs from the cost of directly borrowing that currency in the cash market.

**Example:** If 3-month EUR/USD basis is -20bp, the forward FX swap prices as if euro rates were 20bp lower than actual — meaning synthetic USD funding via swaps costs 20bp more than direct USD borrowing.

**Key insight:** A non-zero basis violates CIP, which should equalize direct and synthetic funding costs. Pre-2008, CIP held almost perfectly. Since then, persistent negative basis = structural dollar shortage.

---

## Why it exists (CIP breakdown)

### What should happen (CIP)

Interest rate differential = forward premium/discount. If you can borrow in EUR at 3%, convert to USD, invest at 5%, and hedge FX risk via forward, the forward rate should exactly offset the 2% carry. No free lunch.

### What actually happens

Since 2007, the basis has been persistently negative for most currencies vs USD — you pay extra to get synthetic dollar funding. Multiple factors explain this:

| Factor | Mechanism |
|--------|-----------|
| **Hedging demand** | Non-US institutions (banks, insurers, pensions) buying USD assets and hedging FX risk creates one-way demand for USD in swap market |
| **Regulatory constraints** | Basel III increased balance sheet costs for arbitrage — banks can't exploit the gap profitably |
| **Counterparty risk awareness** | Post-GFC, funding markets price credit risk more carefully |
| **Dealer capacity limits** | Banks reduced market-making/arbitrage activity |
| **Reserve manager behavior** | EM central banks sometimes reduce USD supply when commodities fall |

**Borio et al. (BIS 2016):** The framework stresses the combination of hedging demand and tighter limits to arbitrage — CIP violations persist because arbitrageurs face capital constraints that make the trade uneconomical at current spreads.

---

## Historical patterns

### Pre-2008

CIP held tightly — basis near zero. Arbitrageurs quickly exploited any deviation.

### 2008 Global Financial Crisis

Lehman collapse triggered acute dollar shortage. Non-US banks couldn't roll dollar funding, rushed to FX swaps. Basis blew out to -150bp+ for EUR/USD. Fed swap lines eventually calmed markets.

### 2010-2019: The "new normal"

Basis persisted at -20 to -40bp for EUR/USD even as bank credit improved. Regulatory constraints (Basel III leverage ratio, supplementary leverage ratio) made arbitrage uneconomical.

### COVID-19 (March 2020)

Dash for dollars repeated 2008 dynamics:
- EUR/USD basis widened ~55bp from January levels
- Some EM currencies (MYR, PHP) widened 90bp
- Fed reactivated swap lines with 9 additional central banks
- Basis normalized by April after Fed intervention

### 2024-2025

Basis remains structurally negative but less extreme:
- EUR/USD: typically -10 to -25bp
- JPY/USD: wider due to BOJ policy divergence and carry trade hedging
- Narrowing trend as Eurozone current account surplus provides USD liquidity

---

## Drivers of widening/narrowing

### Widening (more negative)

| Factor | Why |
|--------|-----|
| **USD strength** | Flight to dollars increases swap demand |
| **VIX spike** | Risk-off = dollar shortage |
| **Fed tightening** | Relative policy divergence |
| **Quarter/year-end** | Banks reduce balance sheet for reporting |
| **EM stress** | Reserve managers sell USD → reduces swap supply |
| **Credit stress** | Counterparty concerns return |

### Narrowing (less negative)

| Factor | Why |
|--------|-----|
| **Fed swap lines** | Central bank USD provision |
| **Risk-on** | Less hedging demand |
| **Bank credit improvement** | Lower counterparty risk premium |
| **Current account surpluses** | Eurozone, Japan accumulate USD |

---

## BRL-specific dynamics

[[Brazilian real|BRL]] basis behavior differs from G10 currencies:

**Structural features:**
- BRL is non-deliverable — all FX derivatives settled in BRL onshore
- Large domestic derivatives market (BM&FBovespa) but limited cross-currency swap depth
- Offshore NDF market is primary vehicle for foreign investors
- BCB uses FX swaps (reverse basis trades) for intervention

**Why BRL basis matters more:**
- Higher volatility than G10 currencies
- Wider basis movements
- Affects broader set of economic agents (corporates, not just banks)

**Corporate hedging cost:**
- Brazilian companies borrowing in USD face higher hedging costs when basis widens
- A -50bp basis on a $1B loan = $5M additional annual cost
- During stress periods (2015, 2020), basis can spike 100bp+

**BCB swap intervention:**
- BCB takes long BRL, short USD position via swaps
- Profitable if BRL depreciates less than interest differential
- Effectively provides synthetic USD funding to market
- Different from classic intervention (doesn't use reserves)

---

## Corporate hedging implications

### The cost equation

Total hedging cost = interest rate differential + cross-currency basis

For a Brazilian company hedging USD debt:
- Selic: 12.25%
- USD rate: 4%
- Differential: ~825bp
- Basis: assume -50bp
- **True hedging cost: ~875bp**

### Accounting treatment

Under IFRS 9 / ASC 815, companies can exclude the currency basis spread from hedge effectiveness testing. This prevents P&L volatility from basis movements — but the economic cost remains.

### Strategic implications

| Situation | Implication |
|-----------|-------------|
| Basis widens | Delay hedging if possible |
| Basis narrows | Lock in favorable rates |
| Persistent wide basis | Consider natural hedges (USD revenues) |
| Quarter-end | Avoid rolling hedges at reporting dates |

---

## Key references

### Academic

**Du, Tepper, and Verdelhan (2018)** — "Deviations from Covered Interest Rate Parity," *Journal of Finance*. Seminal paper documenting CIP breakdown. Found 24bp average basis at 3-month, persistent across G10 currencies. Quarter-end effects point to regulatory cause.

### BIS/Policy

**Borio, McCauley, McGuire, and Sushko (2016)** — "Covered Interest Parity Lost: Understanding the Cross-Currency Basis," *BIS Quarterly Review*. Framework emphasizing hedging demand + limits to arbitrage. Companion working paper (BIS WP 590) provides technical details.

**FSB (2022)** — "US Dollar Funding and Emerging Market Economy Vulnerabilities." Documents how EM corporates face funding stress when basis widens.

**IMF (2020)** — "Strains in Offshore US Dollar Funding." Analysis of COVID-19 basis blowout and Fed response.

### Practitioner

**CME Group** — Launched EUR/USD Cross-Currency Basis futures (2025). Index (XEURBI) provides daily benchmark.

**Clarus FT** — Regular cross-currency swap market reviews with volume and maturity data.

---

## Investment implications

**As a stress indicator:**
- Basis widening precedes broader market stress
- Watch EUR/USD and JPY/USD basis for G10 signal
- EM basis moves faster and further

**Trading the basis directly:**
- CME futures enable direct basis exposure
- Historically mean-reverting after extreme moves
- Fed swap lines provide backstop (limits downside from short basis)

**For FX-exposed portfolios:**
- Hedging costs vary significantly with basis
- Quarter-end typically worst time to hedge
- Consider rolling hedges at month-end instead

---

## Related

### Concepts
- [[Carry trade]] — Basis affects hedge costs for carry positions
- [[US dollar]] — Dollar shortage drives basis
- [[Brazilian real]] — EM basis dynamics
- [[VIX]] — Risk-off correlation

### Institutions
- [[Federal Reserve]] — Swap lines as backstop
- [[Bank for International Settlements]] — Key research
- [[Banco Central do Brasil]] — FX swap intervention

### Events
- [[March 2020 liquidity crisis]] — Basis blowout example

---

*Created 2026-02-01.*
