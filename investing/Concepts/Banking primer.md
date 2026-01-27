#concept #banking #financials #primer

**Banking primer** — foundational banking business model and regulatory concepts for financial sector investing. Understanding banking helps evaluate NIM sensitivity, credit quality, and capital adequacy.

> **Key insight:** Banks borrow short and lend long. This maturity transformation is profitable but inherently risky. Every bank is a leveraged bet on credit quality and interest rates.

---

## How banks make money

```
Borrow cheap (deposits) → Lend expensive (loans) → Earn the spread
```

| Revenue source | Description | % of revenue |
|----------------|-------------|--------------|
| **Net interest income (NII)** | Spread between lending and borrowing rates | 50-70% |
| **Fee income** | Service charges, wealth management, cards | 20-40% |
| **Trading income** | Market making, proprietary | 5-20% (varies) |

---

## Net interest margin (NIM)

The core profitability metric.

```
NIM = (Interest Income − Interest Expense) / Average Earning Assets
```

| NIM level | Interpretation |
|-----------|----------------|
| >3.5% | Strong (community banks) |
| 2.5-3.5% | Typical |
| <2.5% | Compressed (low rate environment) |

### NIM drivers

| Factor | Impact on NIM |
|--------|---------------|
| **Loan yields** | Higher yields → higher NIM |
| **Deposit costs** | Higher costs → lower NIM |
| **Asset mix** | More loans vs securities → higher NIM |
| **Rate environment** | Rising rates usually help (with lag) |

### Asset sensitivity

| Type | When rates rise |
|------|-----------------|
| **Asset sensitive** | Assets reprice faster → NIM expands |
| **Liability sensitive** | Deposits reprice faster → NIM compresses |

Most banks are **asset sensitive** — benefit from rising rates (initially).

---

## Balance sheet structure

### Assets (what banks own)

| Asset | % of assets | Yield |
|-------|-------------|-------|
| **Loans** | 50-70% | Highest |
| **Securities** | 15-30% | Medium |
| **Cash/reserves** | 5-15% | Fed funds rate |
| **Other** | 5-10% | Varies |

### Loan portfolio

| Loan type | Risk | Yield |
|-----------|------|-------|
| **Commercial & Industrial (C&I)** | Medium | Medium |
| **Commercial Real Estate (CRE)** | Higher | Higher |
| **Residential mortgage** | Lower | Lower |
| **Consumer (cards, auto)** | Higher | Highest |

**CRE concentration:** Banks with >300% CRE/capital face extra scrutiny. Office exposure is 2024-26 concern.

### Liabilities (funding)

| Funding | Cost | Stability |
|---------|------|-----------|
| **Non-interest deposits** | Free | Sticky |
| **Interest-bearing deposits** | Low-medium | Less sticky |
| **CDs** | Medium | Locked |
| **Wholesale funding** | Higher | Hot money |
| **Borrowings (FHLB, Fed)** | Higher | Available |

**Deposit franchise:** Banks with large non-interest deposit bases have structural NIM advantage.

---

## Capital and leverage

Banks are highly leveraged. Regulations limit this.

### Capital ratios

```
Capital Ratio = Capital / Risk-Weighted Assets (RWA)
```

| Ratio | Minimum (large banks) | Well-capitalized |
|-------|----------------------|------------------|
| **CET1** | 4.5% + buffer | >10% |
| **Tier 1** | 6% | >8% |
| **Total capital** | 8% | >10% |
| **Leverage ratio** | 4% | >5% |

### Capital tiers

| Tier | Components |
|------|------------|
| **CET1 (Common Equity Tier 1)** | Common stock, retained earnings |
| **Tier 1** | CET1 + preferred stock |
| **Tier 2** | Subordinated debt, loan loss reserves |

### Risk-weighted assets

Not all assets are equal. Riskier assets require more capital.

| Asset | Risk weight |
|-------|-------------|
| Cash, Treasuries | 0% |
| Agency MBS | 20% |
| Residential mortgages | 50% |
| Commercial loans | 100% |
| High-risk assets | 150%+ |

**Why it matters:** $100 of Treasuries requires $0 capital. $100 of commercial loans requires $8+ capital.

---

## Credit quality

### Loan loss provisions

```
Provision for Credit Losses = Expected losses on loans
```

Expense that reduces earnings. Builds the **Allowance for Loan Losses (ALL)** on balance sheet.

| Metric | Formula | Meaning |
|--------|---------|---------|
| **Provision/Loans** | Provision / Avg loans | Current period expense |
| **ALL/Loans** | Allowance / Total loans | Reserve coverage |
| **NCO ratio** | Net charge-offs / Avg loans | Actual losses |

### Credit quality metrics

| Metric | Definition | Good level |
|--------|------------|------------|
| **NPL ratio** | Non-performing loans / Total loans | <1% |
| **NCO ratio** | Net charge-offs / Loans | <0.5% |
| **Coverage ratio** | ALL / NPLs | >100% |
| **Delinquency** | 30+ days past due | <2% |

### CECL accounting

Current Expected Credit Loss model (since 2020). Requires banks to reserve for **lifetime expected losses** upfront.

**Impact:** Front-loads provisions. More volatile earnings. Counter-cyclical reserves.

---

## Deposit franchise value

**Core deposits = competitive moat.**

| Deposit type | Value |
|--------------|-------|
| Non-interest checking | Highest (free funding) |
| Interest checking | High |
| Savings | Medium |
| Money market | Medium |
| CDs | Lower (rate-sensitive) |

### Deposit beta

How much deposit rates move when Fed moves.

```
Deposit Beta = Δ Deposit rate / Δ Fed funds rate
```

| Beta | Interpretation |
|------|----------------|
| 0.20 | Sticky deposits (good) |
| 0.50 | Average |
| 0.80+ | Hot money (bad) |

**Cycle dynamics:** Betas start low, rise over time as competition intensifies.

---

## Interest rate risk

### Duration mismatch

Assets (loans, bonds) have longer duration than liabilities (deposits).

| Risk | Scenario | Impact |
|------|----------|--------|
| **Rising rates** | Bond portfolio loses value | Unrealized losses |
| **Falling rates** | Loans reprice down faster | NIM compression |

### HTM vs AFS securities

| Classification | Accounting | Rate sensitivity |
|----------------|------------|------------------|
| **Held-to-maturity (HTM)** | Amortized cost | Losses hidden |
| **Available-for-sale (AFS)** | Mark-to-market (through equity) | Losses visible |

**SVB lesson:** Large HTM portfolios can hide massive unrealized losses. When forced to sell, losses crystallize.

### AOCI (Accumulated Other Comprehensive Income)

Unrealized gains/losses on AFS securities flow through AOCI (equity), not earnings.

**Tangible book value:** Includes AOCI. Shows economic reality. Regulatory capital excludes AOCI for most banks (loophole).

---

## Regulatory framework

### Key regulators

| Regulator | Jurisdiction |
|-----------|--------------|
| **Federal Reserve** | Bank holding companies, large banks |
| **OCC** | National banks |
| **FDIC** | Deposit insurance, state banks |
| **State regulators** | State-chartered banks |

### Basel III

International capital and liquidity standards.

| Requirement | Purpose |
|-------------|---------|
| **Capital ratios** | Absorb losses |
| **LCR (Liquidity Coverage)** | Survive 30-day stress |
| **NSFR (Net Stable Funding)** | Match funding to asset duration |

### Stress testing (CCAR/DFAST)

Annual Fed stress tests for large banks.

| Test | What it measures |
|------|------------------|
| **DFAST** | Capital adequacy under stress |
| **CCAR** | Capital planning, dividend/buyback capacity |

**Stress Capital Buffer (SCB):** Bank-specific buffer based on stress test results.

---

## Key bank metrics

### Profitability

| Metric | Formula | Good level |
|--------|---------|------------|
| **ROE** | Net income / Avg equity | >12% |
| **ROA** | Net income / Avg assets | >1.0% |
| **Efficiency ratio** | Non-interest expense / Revenue | <60% |
| **NIM** | Net interest income / Earning assets | >3.0% |

### Valuation

| Metric | Formula | Interpretation |
|--------|---------|----------------|
| **P/TBV** | Price / Tangible book value | <1x = trading below liquidation |
| **P/E** | Price / Earnings | 8-12x typical |

**P/TBV matters most.** Banks are balance sheet businesses. Book value = real equity.

---

## Business model variations

### Commercial banks

Focus on lending to businesses and consumers.

| Characteristics | Examples |
|-----------------|----------|
| NII-driven | JPMorgan, Bank of America |
| Deposit-funded | Wells Fargo |
| Branch networks | Regional banks |

### Investment banks

Focus on advisory, underwriting, trading.

| Characteristics | Examples |
|-----------------|----------|
| Fee-driven | Goldman Sachs, Morgan Stanley |
| Trading revenue | Goldman |
| Wealth management | Morgan Stanley |

### Universal banks

Combine commercial and investment banking.

| Examples | Mix |
|----------|-----|
| JPMorgan | ~60% commercial, ~40% investment |
| Bank of America | ~70% commercial |
| Citigroup | ~50/50 |

### Regional/community banks

Focus on local markets, relationship lending.

| Characteristics | Examples |
|-----------------|----------|
| Higher NIM | First Republic (was), Zions |
| CRE focus | Many regionals |
| Less diversified | Concentration risk |

---

## Bank risks

| Risk | Description | Mitigation |
|------|-------------|------------|
| **Credit risk** | Borrowers default | Underwriting, reserves |
| **Interest rate risk** | NIM compression | ALM hedging |
| **Liquidity risk** | Deposit flight | Liquidity buffers |
| **Operational risk** | Fraud, errors | Controls |
| **Concentration risk** | Too much in one area | Diversification |

### Bank run dynamics

```
Confidence lost → Depositors withdraw → Forced asset sales
      → Losses crystallize → More confidence lost → Spiral
```

**Deposit insurance:** FDIC covers $250K per depositor. Protects small depositors, not large.

**SVB/First Republic 2023:** Uninsured deposits fled. Even "safe" banks vulnerable if deposit base concentrated.

---

## Cycle dynamics

### Early cycle (recession)

- Provisions spike
- NPLs rise
- NIM pressures (Fed cutting)
- Stocks cheap on P/TBV

### Mid cycle (recovery)

- Provisions decline (reserve releases)
- Loan growth resumes
- NIM stable
- Stocks rerate

### Late cycle (expansion)

- Credit standards loosen
- Loan growth strong
- Competition intensifies
- Seeds of next cycle's losses planted

---

## Related

- [[Banks]] — sector overview
- [[JPMorgan Chase]] — largest US bank
- [[Monetary policy primer]] — rate environment
- [[Credit spreads]] — credit conditions
- [[FDIC]] — deposit insurance
- [[Basel III]] — capital rules
