---
aliases: [International Financial Reporting Standards, IFRS 10, IFRS consolidation, IFRS 9, IFRS 16, IFRS 17, IFRS 18]
---
#concept #accounting

# IFRS

International Financial Reporting Standards — the global accounting framework used in 140+ jurisdictions (not the US, which uses [[GAAP]]). Set by the IFRS Foundation / [[IASB]] (International Accounting Standards Board) in London.

This note covers the standards that matter most for equity and credit analysis, not accounting theory.

---

## IFRS 10: Consolidation

The standard most relevant to investing analysis. IFRS 10 requires a parent to consolidate a subsidiary when it has **control** — defined as three simultaneous conditions:

1. **Power** over the investee (voting rights or contractual arrangements)
2. **Exposure to variable returns** from involvement with the investee
3. **Ability to use power** to affect those returns

The critical threshold is typically >50% voting rights, though control can exist below 50% (de facto control) or not exist above 50% (if power is shared via a shareholders' agreement).

### De facto control (the <50% trap)

An investor can control an investee without majority voting rights when other shareholders are dispersed and passive. Key factors:

| Factor | What to look for |
|--------|-----------------|
| Voting concentration | Investor holds 35-49% while rest is fragmented retail |
| Board domination | Investor nominates all/most directors |
| Historical voting patterns | Investor's resolutions never challenged at AGMs |
| Contractual rights | Management agreements, veto rights, put/call options |
| Potential voting rights | Convertibles, warrants that could tip the balance |

**IFRS vs GAAP difference:** De facto control exists under IFRS but has no equivalent in US GAAP. This means an IFRS reporter can be forced to consolidate at a lower ownership threshold than a US GAAP reporter in an otherwise identical situation. US GAAP uses a two-tier model (VIE model + voting interest model) that does not recognize de facto control.

### Structured entities (off-balance-sheet risk)

IFRS 10 uses a single control model for all entities, including structured entities (SPVs, securitization vehicles, funds). Voting rights are not the dominant factor — instead look at:

- **Decision-making scope** — how much discretion does the manager/sponsor have?
- **Kick-out rights** — can other parties remove the decision-maker?
- **Remuneration structure** — fixed fee (agent) vs. performance-linked (principal)?
- **Residual interest exposure** — does the sponsor absorb tail risk?

A fund manager who earns only a market-rate fixed fee and can be removed by investors is an **agent** (no consolidation). A sponsor who absorbs first-loss risk, earns variable fees, and cannot be removed is a **principal** (consolidation required).

**Investment entity exception:** Entities qualifying as "investment entities" (e.g., PE funds, VC funds) measure subsidiaries at fair value through P&L instead of consolidating — even with 100% ownership. This is why [[Apollo]]'s fund entities do not consolidate portfolio companies.

### How JVs avoid consolidation

A 50/50 joint venture avoids consolidation because neither party has unilateral power — decisions require unanimous consent. Under IFRS 11, JVs are accounted for using the **equity method** (single-line P&L pickup, no balance sheet grossing). This is why companies prefer 50/50 structures — it keeps the JV's debt off the parent's balance sheet.

The moment one party gains effective control (through board seats, management contracts, or a tiebreaker mechanism), the JV must be consolidated.

### Why it matters for credit analysis

When consolidation is triggered, the subsidiary's entire balance sheet (all assets, all liabilities) gets absorbed line-by-line into the parent's financials. This can dramatically change leverage ratios, debt covenants, and credit metrics overnight — without any change in the underlying business.

### Raizen example

[[Shell]] holds 44% of [[Raizen]]. If Shell injected enough capital to cross 50%, IFRS 10 would require Shell to consolidate [[Raizen]]'s R$76.8B gross debt ($14.3B) onto its own balance sheet. This is a key reason Shell refuses to increase its stake — the accounting consequence outweighs the strategic benefit. See [[Brazil corporate bond rout February 2026]].

---

## IFRS 9: Financial Instruments (Expected Credit Losses)

Effective January 2018. Replaced IAS 39's "incurred loss" model (recognize losses only after a credit event) with a **forward-looking expected credit loss (ECL)** model. This is the single most important standard for bank analysis under IFRS.

### Three-stage impairment model

| Stage | Trigger | Provision | What it means |
|-------|---------|-----------|---------------|
| **Stage 1** | Performing (no significant deterioration) | 12-month ECL | Provision for defaults expected in next 12 months |
| **Stage 2** | Significant increase in credit risk (SICR) | Lifetime ECL | Provision for all expected defaults over loan life |
| **Stage 3** | Credit-impaired (default) | Lifetime ECL | Write-down, interest on net carrying amount |

The Stage 1 to Stage 2 transition is the critical cliff — provision jumps from 12-month to lifetime expected losses. Banks have substantial discretion in defining "significant increase in credit risk," which is where earnings management lives.

### What investors should watch

**Front-loading effect:** IFRS 9 forces banks to take provisions earlier. In a healthy economy, this drags reported earnings (more provisions on performing loans). But at the onset of a recession, the cliff-effect is smaller because provisions were already partially booked. [[ECB]] data shows provisions on performing loans are systematically higher under IFRS 9 than under prior standards.

**Procyclicality debate:** In theory, IFRS 9 should reduce procyclicality (provisions are already partially booked before a downturn). In practice, the Stage 1-to-2 migration during stress can still create a provision spike. Less-capitalized banks get hit harder because they have less buffer to absorb the front-loaded hit.

**Management discretion risk:** IFRS 9 requires forward-looking macroeconomic forecasts (GDP, unemployment, house prices) as inputs to ECL models. This gives management enormous latitude. Watch for:
- Overly optimistic macro scenarios
- Heavy weighting on base cases vs. downside scenarios
- Delayed Stage 2 migration (keeping loans in Stage 1 too long)
- Overlay adjustments (management can manually adjust model outputs)

**IFRS 9 vs US GAAP (CECL):** US banks adopted the Current Expected Credit Loss (CECL) model in 2020. CECL requires lifetime ECL from day one (no staging). This means US banks take a bigger upfront hit on origination but avoid the Stage 1-to-2 cliff. Cross-border bank comparisons must adjust for this difference.

### Empirical evidence

Research across 666 banks in 61 countries found that IFRS 9 adoption reduced bank risk, with the effect strongest for riskier banks. However, some studies found banks struggle to move loans from Stage 1 to Stage 2 early enough, meaning the standard has not fully solved the "too little, too late" provisioning problem.

---

## IFRS 16: Leases

Effective January 2019. Eliminated the operating/finance lease distinction for lessees. All leases >12 months with identifiable assets go on the balance sheet as a right-of-use (ROU) asset and corresponding lease liability.

### Balance sheet impact by sector

| Sector | Liability increase | Asset increase | Why |
|--------|--------------------|---------------|-----|
| Airlines | 15-25% | 15-20% | Aircraft leases |
| Retail / apparel | 15-25% | 15-20% | Store leases |
| Shipping / transport | 10-20% | 10-15% | Fleet leases |
| Telecom | 5-10% | 5-8% | Tower/site leases |
| Power / utilities | <2% | <1% | Own most assets |
| Financial services | <2% | <1% | Office leases only |

### How it changes key metrics

| Metric | Direction | Mechanism | Investor trap |
|--------|-----------|-----------|---------------|
| **EBITDA** | Up | Lease expense removed from opex, replaced by depreciation + interest (both excluded from EBITDA) | EBITDA looks better but cash flow unchanged |
| **Debt / equity** | Up | Lease liability added to numerator | Covenant breaches possible |
| **Debt / assets** | Up | Liabilities grow faster than assets (front-loaded interest) | Looks more leveraged |
| **Interest coverage** | Mixed | EBIT up (no lease expense) but interest up (lease interest) | Effects roughly cancel |
| **ROA** | Down | Same earnings, bigger asset base | Penalizes asset-heavy lessees |
| **EV/EBITDA** | Down | EV rises (more debt) and EBITDA rises, but EV effect dominates | Multiples compress vs. pre-IFRS 16 |

### What credit analysts must do

1. **Distinguish operational leverage from financial leverage** — IFRS 16 treats a 3-year copier lease the same as a 20-year aircraft lease. Strip short-term/low-value leases when assessing structural leverage.
2. **Adjust covenants** — many loan agreements were written pre-IFRS 16. Check if covenants use "frozen GAAP" (old definitions) or adopt the new standard.
3. **Compare like-for-like** — a retailer that owns its stores vs. one that leases will now show very different leverage ratios, even if economics are identical.
4. **US GAAP comparison:** ASC 842 (effective 2019 for public companies) is similar but retains the operating/finance lease distinction on the income statement. Operating leases under ASC 842 show a single straight-line expense, while IFRS 16 front-loads expense (higher interest early, declining over time). This creates a timing difference in expense recognition.

---

## IFRS 17: Insurance Contracts

Effective January 2023, replacing IFRS 4. The most significant overhaul of [[Insurance]] accounting in decades.

### Why it matters

Under IFRS 4, insurers could use almost any local accounting method. A [[Munich Re]] and a [[Prudential Financial]] equivalent in the UK were essentially incomparable. IFRS 17 imposes a single global measurement framework.

### Key mechanics

**General Model (Building Blocks Approach):** Insurance liabilities = present value of future cash flows + risk adjustment + Contractual Service Margin (CSM).

The **CSM** is the critical concept — it represents unearned profit locked inside the liability. If a contract is expected to be profitable at inception, the day-one gain is deferred into the CSM and released to revenue over the coverage period. This prevents front-loading of profit and creates a smoothing mechanism.

**Three measurement approaches:**

| Approach | Used for | Key feature |
|----------|----------|-------------|
| General Model (BBA) | Long-duration contracts (life, annuities) | CSM absorbs changes in estimates, released over time |
| Premium Allocation Approach (PAA) | Short-duration contracts (most P&C, <12 months) | Simplified — allocates premium over coverage period |
| Variable Fee Approach (VFA) | Participating contracts (with-profits, unit-linked) | CSM adjusts for changes in financial risk |

### What investors should watch

- **CSM as a leading indicator:** A growing CSM means the insurer is writing profitable new business. Declining CSM signals either unprofitable new contracts or unfavorable experience adjustments eating into deferred profit.
- **Revenue presentation:** IFRS 17 strips out investment components from revenue. Insurance revenue now reflects only the service provided, not cash collected. This makes revenue numbers smaller but more meaningful.
- **P&L volatility:** Changes in discount rates can create volatility. IFRS 17 allows companies to park discount rate effects in OCI (similar to IFRS 9 for debt securities), so watch whether insurers elect OCI or P&L treatment.
- **Transition effects:** Many insurers saw significant equity adjustments on transition (Jan 2023). Compare post-transition metrics to pre-transition with caution.

---

## IFRS vs GAAP: Comparability traps for investors

### Quick reference

| Dimension | IFRS | US GAAP | Investor impact |
|-----------|------|---------|-----------------|
| Jurisdictions | 140+ | US only | — |
| Framework | Principles-based (~50% more flexibility) | Rules-based | IFRS gives more latitude for management judgment |
| Inventory | **No LIFO** (FIFO, weighted avg only) | LIFO permitted | See below |
| Revenue | IFRS 15 (principles-based) | ASC 606 (rules-based, converged) | Largely aligned post-convergence |
| Leases | IFRS 16 (all on balance sheet) | ASC 842 (operating/finance distinction retained on P&L) | See IFRS 16 section |
| Consolidation | IFRS 10 (control model, de facto control) | ASC 810 (VIE model, no de facto control) | IFRS consolidates at lower ownership thresholds |
| R&D | Development costs **must be capitalized** when feasible | Expensed as incurred (except software under ASC 985-20) | See below |
| Goodwill | Impairment only (no amortization) | Impairment only (private cos can amortize over 10yr) | Aligned for public companies |
| Asset revaluation | Fair value option for PP&E/intangibles | Historical cost only (no upward revaluation) | IFRS can show higher asset values |
| Impairment reversal | Allowed (except goodwill) | **Never allowed** | IFRS earnings can recover; GAAP cannot |
| Cash flow classification | Flexible (interest can be operating or financing) | Interest paid = operating (mandatory) | IFRS operating cash flow can appear higher |

### Inventory: The LIFO trap

**Problem:** During inflation, a US company using LIFO reports higher COGS and lower earnings than an identical IFRS company using FIFO. The gap can be 10-15% of pre-tax income for commodity-heavy businesses.

**How to adjust:** US companies using LIFO must disclose a "LIFO reserve" in the footnotes. Add the LIFO reserve back to inventory (balance sheet) and add the year-over-year change in LIFO reserve to pre-tax income (P&L) to approximate FIFO results. Sectors most affected: oil refining, chemicals, industrials, retail.

### R&D capitalization: The pharma/tech trap

**Problem:** An IFRS pharma company capitalizes Phase III clinical trial costs (once technical feasibility is established), while a US GAAP peer expenses them immediately. The IFRS company shows higher near-term earnings and higher assets. But the capitalized amount must be amortized once the drug launches — so long-term earnings converge.

**How to adjust:** Look at the intangible asset schedule for "internally generated development costs." Subtract this from assets and add the amortization charge back to operating expenses to approximate GAAP treatment. Sectors most affected: pharma, software, automotive (EV platform development).

### Goodwill: Amortization vs impairment

Both IFRS and US GAAP currently use impairment-only for goodwill on public company financials. However, the IASB explored reintroducing amortization. As of 2025, no change has been enacted, but this remains an active discussion.

**The real trap:** IFRS allows reversal of impairment losses on all assets except goodwill. US GAAP prohibits all impairment reversals. An IFRS company that impaired an asset in a downturn can reverse it in a recovery, boosting earnings. A US GAAP company cannot.

### Pensions: The hidden divergence

| Element | IFRS (IAS 19R) | US GAAP (ASC 715) |
|---------|----------------|---------------------|
| Actuarial gains/losses | OCI only, **never recycled** to P&L | OCI initially, then **recycled** via corridor method |
| Expected return on plan assets | Not used — single **net interest** rate on net liability | Separate **expected return** assumption (can differ from discount rate) |
| Prior service costs | Immediate P&L recognition | OCI, then amortized to P&L over remaining service |

**Why this matters enormously:** Under US GAAP, companies set their own "expected return on plan assets" assumption. A 7.5% expected return vs. 6.0% can swing pension expense by hundreds of millions for large plans. [[Ford]] Motor and [[GM]] have historically counted 87-199% of their actual pension returns in net income through this mechanism. Under IFRS, using a single discount rate eliminates this lever entirely.

**The corridor method** (US GAAP only): Cumulative actuarial gains/losses in OCI exceeding 10% of the larger of (plan assets, pension obligation) get amortized back to P&L. This creates a lagged, smoothed earnings impact. IFRS eliminated the corridor in 2013 (IAS 19R) — all remeasurements stay permanently in OCI.

**Investment behavior effect:** Research shows that the elimination of the corridor method under IAS 19R led companies to shift pension assets from equities into bonds, reducing the mismatch risk that would create OCI volatility.

### Cash flow classification

IFRS allows interest paid, interest received, and dividends received to be classified as operating, investing, or financing — management's choice. US GAAP mandates interest paid as operating. An IFRS company can boost operating cash flow by classifying interest paid as financing. Always check the accounting policy note when comparing operating cash flow across jurisdictions.

---

## Recent and upcoming changes (2025-2027)

### Effective January 2025

- **IAS 21 amendments (Lack of Exchangeability):** New rules for currency translation when a currency cannot be freely exchanged. Relevant for companies with operations in Argentina, Venezuela, or other restricted-currency jurisdictions.

### Effective January 2026

- **IFRS 9/7 amendments (Classification and Measurement):** Narrow amendments to financial instrument classification. Includes new guidance on Power Purchase Agreements (PPAs) — relevant for energy companies and corporates with long-term renewable contracts.
- **Annual Improvements Volume 11:** Minor amendments to IFRS 1, IFRS 7, IFRS 9, IFRS 10, IAS 7.

### Effective January 2027

- **IFRS 18 (Presentation and Disclosure):** See dedicated section below.
- **IFRS 19 (Subsidiaries without Public Accountability):** Reduced disclosure for certain subsidiaries. Narrow impact.

### IASB projects expected 2026

| Project | Expected timing | Investor relevance |
|---------|----------------|-------------------|
| **Rate-regulated activities** | New standard Q2 2026 | Utility investors: regulatory assets/liabilities finally on balance sheet |
| **Financial Instruments with Characteristics of Equity (FICE)** | Finalized 2026 | Better disclosure on priority of claims — hybrids, prefs, contingent converts |
| **Provisions (targeted improvements)** | Redeliberation ongoing | Tighter definition of "present obligation" — fewer kitchen-sink provisions |
| **Hedge accounting PIR** | Begins Q1 2026 | Post-implementation review of IFRS 9 hedging requirements |
| **IAS 28 fair value option** | Exposure draft Feb 2026 | Scope of fair value option for associates/JVs |

---

## IFRS 18: Presentation and Disclosure in Financial Statements

Issued April 9, 2024. Effective **January 1, 2027** (retrospective — must restate 2026 comparatives). Replaces IAS 1. The biggest change to financial statement presentation in 20+ years.

**Motivation:** An [[IASB]] study found 60%+ of companies reported "operating profit" using at least nine different calculation methods — cross-company comparison was nearly impossible.

### New income statement structure

IFRS 18 mandates three activity categories plus two required subtotals:

| Category | Content | Examples |
|----------|---------|---------|
| **Operating** | Main business activities (residual) | Revenue, COGS, operating expenses |
| **Investing** | Largely independent investments | Interest income, rental income, associate profits |
| **Financing** | Capital structure transactions | Interest expense, dividends on redeemable shares |

**Two mandatory subtotals:**
1. **Operating profit/loss** — standardized definition for the first time
2. **Profit before financing and income taxes** — eliminates capital structure effects for peer comparison

**Financial institution exception:** Banks, insurers, and investment companies whose main business involves financing/investing must reclassify those items into **operating**. Bank interest income → operating (not investing), because lending is the core business.

### Management-defined performance measures (MPMs)

The most consequential change for investors. Any adjusted metric (adjusted EBITDA, adjusted EPS, etc.) used in **public communications** that meets the MPM definition must now be:

| Requirement | Detail |
|-------------|--------|
| Disclosed in audited financial statements | Single dedicated note |
| Labeled and described | What aspect of performance it represents |
| Reconciled to closest IFRS subtotal | Item-by-item |
| Tax effect shown | Per adjustment |
| Non-controlling interest effect shown | Per adjustment |
| **Audited** | Subject to ISA 200 |

**Before IFRS 18:** Non-[[GAAP]] metrics were optional, inconsistent, unaudited. **After:** Reconciliations are mandatory, audited, and standardized. "Creative" adjustments face audit scrutiny.

### Sector impact

| Impact level | Sectors | Why |
|-------------|---------|-----|
| **Very high** | Banks, insurers, asset managers | Operating/investing/financing boundaries fundamentally reclassified |
| **High** | Real estate, utilities | Complex operating/investing boundaries; heavy MPM users |
| **Moderate** | Industrials, diversified | Clear categories but many adjusted metrics to reconcile |
| **Lower** | Pure-play tech/software | Clean operating categories; still must disclose MPMs |

### Investor verdict

**Improves analysis long-term:**
- "Operating profit" gets a standard definition for the first time
- Adjusted metrics become audited and reconciled
- "Profit before financing and income taxes" enables clean peer comparison

**Transition noise (2026-2027):**
- Restated comparatives create one-time complexity
- Financial statement notes become denser (5-10 new MPM disclosures per company)
- No peer benchmarks until second year of adoption

### Key dates

| Date | Milestone |
|------|-----------|
| Apr 9, 2024 | IFRS 18 issued |
| Jan 1, 2026 | Systems must be live (restatement of comparatives begins) |
| Jan 1, 2027 | Mandatory effective date |
| 2027 reports | First public IFRS 18 financials + MPM disclosures |

Early adoption permitted but requires regional endorsement (EU expected before 2027; UK UKEB Q4 2025 earliest).

---

## Related

- [[Shell]] — IFRS consolidation risk re: [[Raizen]]
- [[Raizen]] — consolidation threshold blocking shareholder rescue
- [[Brazil corporate bond rout February 2026]] — event context
- [[Insurance]] — IFRS 17 impact on sector comparability
- [[Cross-currency basis]] — IFRS 9 hedge accounting for basis spreads
- [[Apollo]] — investment entity exception (fund consolidation)
- [[GAAP]] — US counterpart (FASB), GAAP vs non-GAAP context
- [[IASB]] — standard setter

---

*Created 2026-02-10. Expanded 2026-02-10.*
