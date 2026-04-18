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

## Jensen CoreWeave defense (Dwarkesh, Apr 15, 2026)

[[Jensen Huang]] addressed the circular-financing critique head-on in the Dwarkesh interview, disclosing the specific numbers behind the NVIDIA-CoreWeave structure:

| Figure | Value |
|---|---|
| CoreWeave real EBITDA | ~$2B |
| NVIDIA backstop (cost of goods guarantee) | ~$6.3B |
| NVIDIA equity in CoreWeave | ~$2B |

Jensen's exact framing: "CoreWeave's EBITDA is $2B of real EBITDA. The cost of goods is $6.3B. We only guaranteed the difference. And we only have $2B of equity in them."

**What this resolves:** The frequently cited "NVIDIA backstops CoreWeave for $6.3B" figure is the full hardware cost of goods — not a loss guarantee. Jensen's claim: NVIDIA covers the *shortfall* between the guaranteed COGS and CoreWeave's contracted revenue, not the whole stack. Against $2B of standing EBITDA, the structure looks less like a Hollywood-style loss underwrite and more like an anchor-tenant arrangement.

**What it doesn't resolve:** The $6.3B COGS figure confirms the scale of NVIDIA's exposure. If CoreWeave's [[Microsoft]] concentration (65% of revenue) deteriorates — either from workload migration or contract renegotiation — the "real EBITDA" number that Jensen leaned on shrinks fast. The backstop logic depends on the standing EBITDA holding up.

**Framing for the circular-financing critique:** Consistent with Jensen's stated investment philosophy — *"as much as needed, as little as possible"* — NVIDIA's CoreWeave commitment is sized to unblock deployment, not to own the neocloud economics. See [[Jensen Huang]] for the broader pattern (OpenAI $30B, Anthropic $10B, photonics $4B).

*Source: Dwarkesh Patel podcast, "Will Nvidia's moat persist?" Apr 15, 2026.*

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

## $4B data center financing rejected (Feb 2026)

Lenders balked at financing a **$4B CoreWeave data center** (CNBC, Feb 21). [[Blue Owl]], a major AI infrastructure lender, was involved. The pullback signals tightening credit appetite for GPU-collateralized deals amid broader concerns about:
- CoreWeave's high existing leverage ($7.5B+ debt)
- GPU depreciation risk
- [[Blue Owl]]'s own OBDC II redemption crisis creating risk aversion

**Competitive impact:** Financing difficulty for GPU-based infrastructure positions [[Google]]'s [[TPU]] stack and custom silicon more favorably — Google self-finances, avoiding third-party credit risk.

---

## Perplexity partnership (Mar 4, 2026)

Stock +8% on the announcement, recovering from -25% the previous week.

Multi-year strategic partnership with [[Perplexity]] for AI inference workloads. CoreWeave will provide dedicated [[NVIDIA]] GB200 NVL72-powered clusters (see [[Blackwell]]), and [[Perplexity]] will power next-generation inference workloads for its Sonar and Search API ecosystem through CoreWeave infrastructure. In return, CoreWeave is deploying Perplexity Enterprise Max across its organization. Financial terms were not disclosed.

**Context:** Stock had fallen ~25% the prior week on wider-than-expected quarterly loss and cautious near-term guidance. The [[Perplexity]] deal provided a signal of demand diversification beyond [[Microsoft]] (65% of revenue) — a key bear thesis vulnerability.

| Detail | Value |
|--------|-------|
| Stock move | +8% (Mar 4) |
| Partner | [[Perplexity]] |
| Infrastructure | [[NVIDIA]] GB200 NVL72 clusters ([[Blackwell]]) |
| Workload | AI inference (Sonar, Search API) |
| Terms | Not disclosed |

Source: Reuters, Mar 4, 2026.

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

## Structural factors

- GPU supply environment: shortage conditions support pricing for capacity holders
- Customer concentration: ~65% of revenue from [[Microsoft]]
- Supplier relationship: [[NVIDIA]] backing and allocation access; equity stake context
- Credit market signal: CDS spread implies near-junk credit pricing
- Hardware cycle: accelerated GPU depreciation through Blackwell → Rubin transition
- Competitive structure: hyperscalers ([[AWS]], [[Azure]], [[GCP]]) operate GPU capacity at larger scale
- AI-compute demand growth tracked across hyperscaler and neocloud segments

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
- [[Perplexity]] — multi-year inference partnership (Mar 2026)
- [[GPU deployment bottleneck]] — shipped ≠ deployed
