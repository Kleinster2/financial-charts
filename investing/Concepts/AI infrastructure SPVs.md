#concept #finance #datacenter #ai

Off-balance-sheet SPVs for AI data center financing. Template set by [[Meta]]-[[Blue Owl]] Hyperion deal (Oct 2025).

For SPV fundamentals, see [[SPV financing]]. Off-balance-sheet SPVs aren't new — used for decades in real estate, airlines, shipping, project finance. This note covers the AI infrastructure application.

---

## SPV model taxonomy

| Model | Collateral | Borrower | Credit | Term | Example |
|-------|------------|----------|--------|------|---------|
| **Hyperscaler SPV** | Real estate + equipment | Meta, Google | IG (A+) | 20-40yr | Meta-Blue Owl |
| **GPU-as-collateral ("Box")** | GPUs + offtake contracts | CoreWeave | High yield | 5yr | CoreWeave-Blackstone |
| **Hybrid SPV** | GPUs, NVIDIA co-invests | xAI | High yield | 5yr | xAI Colossus (Valor) |
| **Construction JV** | Project assets | Developer | Varies | 15yr+ | Crusoe-OpenAI (JPMorgan) |
| **Chip vendor financing** | Supply agreements | Labs | N/A | Per-GW | OpenAI-NVIDIA/AMD |

**Key distinctions:**
- **Hyperscaler SPV**: Real estate financing with IG credit — lowest risk, lowest rates
- **CoreWeave Box**: GPU depreciation risk but offtake de-risks; "equity slug" upside
- **xAI Hybrid**: NVIDIA takes equity in SPV itself — chip vendor becomes financier
- **Construction JV**: Traditional project finance with long-term lease anchor
- **Chip vendor**: Not debt — equity/warrants tied to deployment milestones

See [[AI infrastructure deals]] for detailed capital stacks on each.

---

## Why hyperscalers use SPVs

| Motivation | Benefit |
|------------|---------|
| Preserve debt capacity | Keep powder dry for M&A |
| Maintain credit ratings | Avoid downgrades from capex debt |
| Avoid earnings volatility | Construction costs don't hit P&L |
| Share risk | PE takes construction/demand risk |
| Focus on operations | Not real estate management |

---

## The Meta-Blue Owl template

**"Beignet Investor LLC"** — the deal that set the standard (Oct 2025).

### Structure

```
                    ┌─────────────────┐
                    │   Debt Investors│
                    │  Pimco ($18B)   │
                    │  BlackRock, etc │
                    └────────┬────────┘
                             │ $27.3B senior secured
                             ▼
         ┌───────────────────────────────────┐
         │         Beignet Investor LLC      │
         │              (SPV)                │
         │   Blue Owl 80% / Meta 20%         │
         └────────┬──────────────────────────┘
                  │ Long-term lease
                  ▼
         ┌─────────────────┐
         │      Meta       │
         │  (operates DC)  │
         └─────────────────┘
```

### Capital stack

| Component | Amount | Details |
|-----------|--------|---------|
| SPV debt | $27.3B | Senior secured, amortizing through 2049 |
| SPV equity | $2.5B | Blue Owl contribution |
| Meta distribution | $3B | One-time payment from JV |
| **SPV total** | **~$30B** | Off Meta's balance sheet |

### Key terms

- **Ownership**: Blue Owl 80% / Meta 20%
- **Security**: 144A-for-life senior secured, first-lien on all assets
- **Rating**: S&P A+
- **Amortization**: Mandatory sinking fund through 2049
- **Meta guarantee**: Residual value guarantee at lease end

### Why it works

1. **Meta** gets data center capacity without balance sheet debt
2. **Blue Owl** gets stable, long-term infrastructure returns
3. **Pimco/BlackRock** get A+-rated senior secured debt
4. **Everyone** benefits from hyperscaler credit quality

---

## How it differs from GPU-as-collateral ("The Box")

[[CoreWeave]] calls their GPU-collateral SPV structure "The Box" (see [[GPU-as-collateral]] for mechanics).

| Aspect | Meta-Blue Owl SPV | CoreWeave "Box" |
|--------|-------------------|-----------------|
| Collateral | Real estate + equipment | GPUs only |
| Typical borrower | Hyperscalers (Meta, [[Google]]) | Neoclouds ([[CoreWeave]], [[xAI]]) |
| Credit quality | Investment grade | High yield |
| Rates | 4-6% (IG) | 11-14% |
| Term | 20-40 years | 3-5 years |
| Risk profile | Real estate-like | Technology obsolescence |
| Residual value | Building ownership | "Equity slug" (GPUs with option value) |
| Capital source | "East Coast capital" (institutional) | "East Coast capital" (debt) + "West Coast capital" (equity) |

**Key distinction:** Meta-Blue Owl is essentially real estate financing with hyperscaler credit. CoreWeave's Box is asset-backed lending with GPU depreciation risk, but Intrator argues the "equity slug" (owning GPUs after contract term) has embedded option value.

---

## Key deals using SPV structure

| Deal | SPV Size | Ownership | Debt Investors |
|------|----------|-----------|----------------|
| [[Meta]]-Blue Owl | $30B | 80/20 | Pimco, BlackRock, Apollo |
| [[xAI]] Colossus | $20B | Valor-managed | Apollo, Diameter |

See [[AI infrastructure deals]] for full details.

---

## Historical context (why this matters)

**Off-balance-sheet financing has a checkered history:**

| Era | What happened |
|-----|---------------|
| **2001 Enron** | SPVs hid liabilities, enabled fraud |
| **2008 GFC** | [[Banks]] moved mortgages off-balance-sheet before crisis |
| **2025 AI** | Tech companies using SPVs for infrastructure |

**[[UBS]] warning (Oct 2025):** "During the dot-com era, most of the growth was financed with equity not debt. So when it burst, the impact in the economy was manageable. Now, there's a rapid growth of capex in AI firms driven by debt and it's starting to be kept off balance sheet."

**Key difference today**: Hyperscaler credit quality is strong. Meta/[[Google]] aren't Enron. But concentration risk exists — few borrowers, massive exposure.

---

## Risks

### For tech companies

- **Residual value guarantee**: If asset values fall, tech company on hook
- **Lease obligations**: Long-term commitments even if demand drops
- **Hidden leverage**: Analysts may miss off-balance-sheet exposure

### For financiers

- **Technology obsolescence**: Data centers could become stranded assets
- **Demand cycle**: AI buildout could overshoot
- **Concentration**: Few hyperscalers = concentrated exposure

### For the system

- **Opacity**: Hard to track total AI infrastructure debt
- **Correlation**: If AI demand drops, all deals stressed simultaneously
- **Bank exposure**: See [[Significant risk transfer]] — banks trying to lay off risk

---

## Who finances SPVs

### Equity (80% ownership typically)

| Firm | AUM | Notable |
|------|-----|---------|
| [[Blue Owl]] | $273B | Meta $27B, Crusoe |
| [[Blackstone]] | $1T+ | [[QTS]], [[CoreWeave]] |
| [[Brookfield]] | $900B+ | Infrastructure focus |
| [[KKR]] | $550B+ | Data centers |

### Debt investors

| Firm | Role | Example |
|------|------|---------|
| [[Pimco]] | Anchor | $18B in Meta SPV |
| [[BlackRock]] | Participant | $3B+ in Meta SPV |
| [[Apollo]] | Participant | Meta, xAI |

---

## Investment implications

**Direct plays:**
- [[Blue Owl]] (OWL) — largest AI infra SPV equity provider
- Blackstone (BX) — major player
- [[Private credit]] funds with IG AI exposure

**Indirect beneficiaries:**
- Hyperscalers preserving balance sheet flexibility
- [[Banks]] earning structuring fees ([[Morgan Stanley]])

---

## For theses

- [[AI infrastructure financing]] — broader context
- [[AI infrastructure financing risk]] — counterpoint (cascade risk)

---

*Updated 2026-02-02*

## Related

- [[AI infrastructure financing]] — broader context
- [[AI infrastructure deals]] — detailed case studies
- [[GPU-as-collateral]] — alternative structure
- [[Meta]] — template deal (Blue Owl Hyperion)
- [[Blue Owl]] — key SPV equity provider
- [[Pimco]] — key debt investor ($18B Meta anchor)
- [[Significant risk transfer]] — banks offloading exposure
- [[AI infrastructure financing risk]] — systemic concerns
- [[SPV financing]] — generic SPV fundamentals
