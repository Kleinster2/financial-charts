---
aliases: [CRWV]
---
#actor #neocloud #usa #ai

**CoreWeave** — GPU cloud provider. NVIDIA-backed. Poster child for AI infrastructure financing risk.

---

## Why CoreWeave matters

CoreWeave is the largest "neocloud" — GPU-focused cloud competing with hyperscalers:

| Metric | Value |
|--------|-------|
| Focus | GPU cloud for AI workloads |
| Revenue concentration | 65% from [[Microsoft]] |
| CDS spread | 773 bps (42% implied default probability) |
| Key backer | [[NVIDIA]] |
| IPO | March 2025 |
| 2026 revenue forecast | Lowered (Jan 2026) |

---

## Sector correlation

| Sector | Correlation | Fit |
|--------|-------------|-----|
| [[Crypto-to-AI]] (CORZ, HUT, IREN) | 0.38-0.53 | Secondary |
| [[DC REITs]] (EQIX, DLR) | 0.23-0.38 | Weak |

CRWV sits between sectors — more correlated with crypto-to-AI pivots (GPU hosting model) than traditional DC REITs (lease model). Not a clean fit for either, but leans toward Crypto-to-AI cluster.

---

## Revenue outlook (Jan 2026)

**Lowered forecast:**
- CoreWeave cut 2026 revenue projections
- Part of broader AI infrastructure financing concerns
- Stock pressure despite strong 2025 performance

---

## Business model

**What they do:**
- Rent NVIDIA GPUs to AI companies
- Compete with AWS/Azure/GCP on GPU availability
- Faster deployment than hyperscalers
- Focus on AI training/inference workloads

**Intrator's three pillars (Davos, Jan 2026):**
1. **Software layer** — parallelized computing solution, "years ahead of everybody"
2. **Physical infrastructure** — 42 data centers (own + colocation via Equinix, Switch, DigitalBridge)
3. **Capital structure** — "East Coast capital" (debt) for infrastructure, "West Coast capital" (equity) for software

**Key quote:** "Planetary scale computing buildout" — infrastructure at a scale "that defied the imagination."

**Customers:**
- Microsoft (65% of revenue)
- AI startups
- Enterprise AI teams
- Inference providers

---

## NVIDIA relationship

**"Symbiotic but not equal"** — Intrator's phrase (Davos, Jan 2026).

**NVIDIA is investor and supplier:**
- Strategic investment in CoreWeave
- Priority GPU allocation
- CoreWeave helps absorb GPU production
- First to deploy new architectures at scale: H100 → H200 → GB200 → Rubin

**Why CoreWeave gets chips first:**
- CoreWeave's software layer allows rapid deployment and troubleshooting at production scale
- NVIDIA develops in labs at sub-production scale, needs real-world testing
- CoreWeave acts as the bridge between NVIDIA labs and production deployment
- Jensen confirmed CoreWeave will be "among the first" with Rubin

**The demand orchestration allegation:**

CoreWeave is cited as example of NVIDIA controlling both supply AND demand:

> "When a quarter needs a little help, Jensen picks up the phone: 'Take the chips now — I'll assign you the clients later.'"

**Pattern (per Kakashiii analysis):**
- Recent deals ([[Scale AI]], [[IREN]], [[Nebius]], CoreWeave) share Microsoft ties
- NVIDIA facilitates relationships between neoclouds and customers
- Creates opacity: NVIDIA → CoreWeave → End customer
- Revenue quality question for both companies

**The question:** Is CoreWeave a real business or NVIDIA inventory management vehicle?

See [[Neocloud financing]] for broader pattern.

---

## Financing: "The Box" structure

**Intrator's innovation** — "East Coast capital" (debt) for infrastructure, "West Coast capital" (equity) for software.

**The Box SPV structure (Davos, Jan 2026):**

```
Microsoft/Meta contract → SPV ("The Box") → Waterfall payout
```

**What goes in the Box:**
- GPUs (collateral)
- Offtake contract (e.g., 5-year Microsoft deal)
- Data center contract
- Power purchase agreement

**Waterfall:**
1. Power costs
2. Data center costs
3. Principal + interest
4. **Then** CoreWeave gets paid

**Key insight:** CoreWeave doesn't touch revenue until all obligations paid. Debt amortizes within contract term.

**The "equity slug":**
- After 5-year contract: debt paid off, CoreWeave owns GPUs outright
- Intrator: "I want to own the equity slug... they have option value embedded in them"
- GPUs still useful after contract (contrary to depreciation critics)

**Not speculative:** GPUs are pre-sold to counterparties before purchase. Risk capital goes to "the long pole" — physical data centers.

**Debt load:**
- $7.5B+ debt financing (Blackstone, others)
- High leverage for growth-stage company
- GPUs as collateral

**IPO (March 2025):**
- Raised capital to fund GPU purchases
- Stock volatile post-IPO
- Market skeptical of unit economics

---

## The risk case

CoreWeave is cited in [[AI infrastructure financing risk]] as key vulnerability:

| Metric | Value | Concern |
|--------|-------|---------|
| CDS spread | 773 bps | 42% implied default probability |
| Revenue concentration | 65% Microsoft | Single customer dependency |
| Debt | $7.5B+ | High leverage |
| GPU depreciation | Faster than assumed | Asset value risk |

**If Microsoft pulls back:** CoreWeave faces existential risk.

---

## Bull case

- GPU shortage = pricing power
- Microsoft contract provides visibility
- NVIDIA backing = GPU access advantage
- AI demand is real and growing
- Hyperscalers can't meet all demand

---

## Bear case

- 65% Microsoft concentration is dangerous
- CDS spread implies near-junk credit
- GPU depreciation accelerating (Blackwell → Rubin)
- Competing with hyperscalers long-term is hard
- Could be NVIDIA inventory management vehicle

---

## Competitive position

| Competitor | Advantage |
|------------|-----------|
| AWS/Azure/GCP | Scale, balance sheet, ecosystem |
| Lambda Labs | Developer-friendly, simpler |
| Crusoe | Cheap power (stranded gas) |
| **CoreWeave** | GPU availability, speed |

CoreWeave wins on availability but loses on cost and scale long-term.

---

## Founders (Bloomberg Billionaires, Nov 2025)

| Name | Role | Net worth |
|------|------|-----------|
| Mike Intrator | CEO | **$5.0B** |
| Brian Venturo | CSO | **$3.2B** |
| Brannin McBee | CDO | **$2.2B** |
| Jack Cogen | Board (early investor) | **$1.8B** |

**Origin story:** Former Natsource commodities traders started crypto mining in 2017. Stored hardware in Venturo's grandfather's garage. Pivoted to AI after crypto struggled.

**Intrator's background:** Wall Street, commodities, structured finance. Not a technical founder — finance DNA enabled "The Box" SPV innovation. Understands project finance and asset-backed lending.

**Insider selling:** $1B+ sold since lockup expired Aug 2025.

---

## Quick stats

| Metric | Value |
|--------|-------|
| Ticker | CRWV |
| Founded | 2017 |
| IPO | March 2025 ($23B valuation) |
| Data centers | **42** (US, Canada, Western Europe, Nordics) |
| GPUs | 250,000+ |
| Stock since IPO | +90% |
| Key customer | [[Microsoft]] (65%) |
| Key backer | [[NVIDIA]] |
| CDS spread | 773 bps |

*Updated 2026-02-02*

---

## For theses

**[[AI infrastructure financing risk]]:** CoreWeave is the canary in the coal mine
**[[AI hyperscalers]]:** Neoclouds compete for same GPU demand

---

## Related

- [[NVIDIA]] — investor, supplier (strategic backer)
- [[Microsoft]] — major customer (65% of revenue)
- [[Core Scientific]] — partner ($3.5B hosting deal)
- [[Blue Owl]] — financing partner
- [[Blackstone]] — financing partner ($7.5B+ debt)
- [[Lambda Labs]] — competitor (GPU cloud)
- [[Crusoe Energy]] — competitor (GPU cloud)
- [[AI infrastructure financing risk]] — thesis context (canary in coal mine)
- [[AI infrastructure financing]] — thesis context
- [[AI hyperscalers]] — compete for GPU demand
- [[Neocloud financing]] — demand orchestration pattern
- [[GPU deployment bottleneck]] — shipped ≠ deployed
