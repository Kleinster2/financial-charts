#concept #finance #datacenter #ai

The capital stack behind AI buildout. Hyperscalers need $100Bs — private credit and PE are filling the gap.

---

## The financing gap

| Metric | Value |
|--------|-------|
| 2025 hyperscaler AI capex | ~$300B |
| 2026 projected | $620B |
| Morgan Stanley DC spend by 2028 | $3T |
| Power infrastructure needed | $2.6T (44GW gap) |
| **Total external financing needed** | **$1.5T** |
| Private credit by 2028 | $800B |
| AI debt raised per quarter | ~$100B |

**Problem:** Even hyperscalers don't want this on balance sheet. Enter private capital.

**2026 IG issuance (JPMorgan forecast):**

| Metric | 2026E |
|--------|-------|
| Total IG issuance | **$1.81T** (record) |
| Tech sector | $252B (+61% YoY) |
| TMT total | $400B |
| M&A-related | $182B (+21%) |

Tech alone forecast to borrow $252B in investment-grade bonds — AI capex the primary driver.

**Scale (Oct 2025):** UBS strategist Matthew Mish: "raises eyebrows for anyone that has seen credit cycles."

---

## Why off-balance-sheet?

**Hyperscaler motivations:**
- Preserve debt capacity for M&A
- Avoid earnings volatility from construction
- Share risk on massive capex
- Maintain credit ratings
- Focus on operations, not real estate

**Financier motivations:**
- Stable, long-term cash flows
- Hyperscaler credit quality
- Tangible collateral (GPUs, buildings)
- Infrastructure-like returns
- Growing market

---

## Deal structures

### Sale-leaseback
- Hyperscaler sells data center to PE
- Leases it back long-term
- Gets cash, removes asset from balance sheet
- PE gets stable rental income

### Joint ventures
- PE finances construction (60-80%)
- Hyperscaler operates and anchors capacity
- Shared ownership
- Example: Meta-Blue Owl Hyperion (80/20)

### GPU financing
- Lender finances GPU purchases
- GPUs serve as collateral
- 75% of AI cloud spend = GPUs
- Hardware retains value 3-5 years

### Construction financing
- Banks/PE fund data center construction
- Take-out financing upon completion
- Example: JPMorgan $2.3B for Crusoe

---

## Key players

### Private equity / Alternative asset managers

| Firm | AUM | AI infra exposure |
|------|-----|-------------------|
| [[Blue Owl]] | $273B | $34B digital infra, Meta $27B deal |
| **Blackstone** | $1T+ | QTS acquisition, major DC portfolio |
| **KKR** | $550B+ | Infrastructure, data centers |
| **Brookfield** | $900B+ | Infrastructure focus |
| **DigitalBridge** | $80B+ | Pure-play digital infra |
| **Apollo** | $650B+ | Growing DC exposure |

### Data center REITs

| REIT | Focus |
|------|-------|
| Equinix (EQIX) | Colocation, interconnection |
| Digital Realty (DLR) | Wholesale, hyperscale |
| QTS (Blackstone) | Private, hyperscale |

### Banks (construction/bridge)

| Bank | Role | Notable |
|------|------|---------|
| [[Morgan Stanley]] | Arranger, junk bonds | Meta $27B+, TeraWulf, Cipher, Applied Digital |
| [[JPMorgan]] | Construction, SRT | Crusoe $2.3B |
| [[Goldman Sachs]] | Underwriting, SRT | |
| [[Citigroup]] | SRT | |
| [[Bank of America]] | Underwriting | |

**Jan 2026:** Banks exploring [[Significant risk transfer]] (SRTs) to offload concentrated data center exposure. See section below.

---

## Major deals (2024-2025)

| Deal | Size | Structure | Parties |
|------|------|-----------|---------|
| **Meta (Oct 2025)** | **$60B** | $30B SPV + $30B bonds | Blue Owl, Morgan Stanley |
| **xAI Colossus** | **$20B** | SPV (chip lease) | Valor Equity, Apollo, Nvidia |
| **Crusoe Abilene** | $15B | JV | Blue Owl, Crusoe |
| **CoreWeave** | $7.5B | Debt | Blackstone, others |
| **Oracle Michigan** | ~$10B | Fell through | Blue Owl pulled out |

**Meta deal (Oct 2025):**
- $30B SPV via Morgan Stanley — **largest private capital deal ever**
- $30B corporate bonds — **largest IG offering of 2025**
- Off-balance-sheet portion sits with Blue Owl

**xAI deal:**
- $20B SPV led by Valor Equity Partners + Apollo
- Nvidia provides equity + chips
- xAI commitment: **5-year lease only** — nothing else on balance sheet

---

## GPU-as-collateral thesis

**Why GPUs work as collateral:**
- 75% of AI cloud spend → GPUs
- Retain value for 3-5 years
- Liquid secondary market developing
- Known depreciation curve (unlike software)
- Hyperscaler demand = price floor

**Risks:**
- Technology obsolescence (Blackwell → Rubin)
- Demand cycle could turn
- Resale market still maturing

---

## Risks for financiers

| Risk | Mitigation |
|------|------------|
| **Demand cycle** | Long-term hyperscaler contracts |
| **Technology obsolescence** | Short financing terms, residual buffers |
| **Construction delays** | Experienced developers, milestone funding |
| **Power availability** | Site selection, [[Power constraints]] due diligence |
| **Interest rates** | Floating rate pass-through, hedging |
| **Concentration** | Diversification across hyperscalers |

### The dot-com comparison

| Era | How it was financed | What happened |
|-----|---------------------|---------------|
| **Dot-com (2000)** | Equity | Burst had limited economic impact |
| **AI (2025)** | Debt (off-balance-sheet) | TBD — but credit cycles hit harder |

**UBS warning:** "During the dot-com era, most of the growth was financed with equity not debt. So when it burst, the impact in the economy was manageable. Now, there's a rapid growth of capex in AI firms driven by debt and it's starting to be kept off balance sheet."

**Off-balance-sheet history:**
- 2001: Enron collapse — SPVs hid liabilities
- 2008: Banks moved mortgages off-balance-sheet before crisis
- 2025: Tech companies using SPVs for AI infrastructure

See [[AI infrastructure financing risk]] for deeper analysis.

---

## Bank concentration risk (Jan 2026)

**Banks becoming overexposed to small group of AI borrowers:**

| Signal | Detail |
|--------|--------|
| [[Oracle]] CDS spike | Banks/lenders driving credit protection surge |
| Concentrated lending | Few hyperscalers = few borrowers |
| SRT exploration | Morgan Stanley considering offload |

**Response: Significant risk transfers**

Banks exploring [[Significant risk transfer]] to hedge:
- Sell credit-linked notes to institutional investors
- Transfer first-loss/mezzanine risk
- Free balance sheet for more lending
- Data-center SRTs still nascent

| Bank | SRT Status |
|------|------------|
| [[Morgan Stanley]] | Exploring (data center portfolio) |
| [[JPMorgan]] | Marketed 2025 |
| [[Citigroup]] | Marketed 2025 |
| [[Goldman Sachs]] | Marketed 2025 |

**Market growth:** Global SRT sales +11% annually through 2027.

**Implication:** Banks want to keep financing AI, but want to lay off credit risk. Creates new asset class for credit investors.

---

## Oracle deal collapse — lessons

**Blue Owl pulled out of ~$10B Oracle Michigan deal:**
- Concerns over Oracle's rising debt
- AI spending aggressive vs balance sheet
- Shows financier discipline
- Not all deals get done

**Implication:** Credit quality matters. PE won't finance everyone.

---

## Investment implications

**Direct plays:**
- [[Blue Owl]] (OWL) — largest AI infra financier
- Blackstone (BX) — diversified but big DC exposure
- DigitalBridge (DBRG) — pure-play digital infra
- Data center REITs (EQIX, DLR)

**Indirect beneficiaries:**
- Hyperscalers with off-balance-sheet capacity
- Construction/engineering firms
- Power providers ([[Constellation Energy]], [[Vistra]])

**Who loses:**
- Hyperscalers who can't access financing (weaker credit)
- Smaller AI companies competing for limited capital

---

## For theses

**Cross-cutting:**
- [[AI hyperscalers]] — financing enables buildout
- [[Power constraints]] — capital alone isn't enough, need power
- [[Long memory]], [[Long TSMC]] — financing enables GPU/chip demand

**New angle:** Long PE/alternative managers as AI infrastructure enablers

---

*Updated 2026-01-15*

Sources:
- [Bloomberg - How AI Companies Are Keeping Debt Off Their Balance Sheets](https://www.bloomberg.com/news/articles/2025-10-31/meta-xai-starting-trend-for-billions-in-off-balance-sheet-debt) (Oct 31, 2025)
- Morgan Stanley research

## Related

- [[AI infrastructure financing risk]] — counterpoint (circular flows, cascade risk)
- [[Blue Owl]] — financier ($34B digital infra, Meta $27B deal)
- [[Blackstone]] — financier (QTS, CoreWeave $7.5B)
- [[Brookfield]] — financier (infrastructure focus)
- [[DigitalBridge]] — financier (pure-play digital infra)
- [[CoreWeave]] — borrower (Blackstone debt)
- [[Crusoe Energy]] — borrower (JPMorgan $2.3B)
- [[Equinix]] — REIT (colocation, interconnection)
- [[Digital Realty]] — REIT (wholesale, hyperscale)
- [[Constellation Energy]] — beneficiary (power for DCs)
- [[Vistra]] — beneficiary (power for DCs)
- [[Power constraints]] — limitation (capital alone isn't enough)
- [[Significant risk transfer]] — banks offloading AI infrastructure credit risk
- [[Applied Digital]] — junk bond issuer (Morgan Stanley)
- [[TeraWulf]] — junk bond issuer (Morgan Stanley)
- [[Cipher Mining]] — junk bond issuer (Morgan Stanley)
