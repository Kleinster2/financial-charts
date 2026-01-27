#actor #ai #modellab

**Anthropic** — AI lab, maker of Claude. More capital-efficient than [[OpenAI]].

---

## Financial position (Jan 2026)

| Metric | Value |
|--------|-------|
| Revenue | **$7-9B** annualized (was $87M early 2024) |
| Revenue mix | 80% enterprise, 20% consumer |
| Business customers | **300,000+** |
| Large accounts ($100K+ ARR) | **7x growth** in past year |
| 2025 loss | **$5.6B** (confirmed Jan 2026) |
| Burn rate | Dropping to **9% of revenue by 2027** |
| Break-even target | **2028** |
| Valuation | **$300-350B** (post Microsoft $5B + NVIDIA $10B) |

Burning **14x less cash** than OpenAI before profitability.

---

## Cap table

### Key investors

| Investor | Amount | Notes |
|----------|--------|-------|
| **[[Google]]** | $2B+ | Cloud partner, multiple rounds |
| **[[Amazon]]** | $4B | AWS partnership, Bedrock distribution |
| **[[Microsoft]]** | $5B | Late 2025, despite OpenAI relationship |
| **[[NVIDIA]]** | $10B | Late 2025 |
| **Salesforce** | $750M | 2023 |
| **Spark Capital** | — | Early investor, led Series A/B |
| **Menlo Ventures** | — | Early investor |
| **Sound Ventures** | — | Ashton Kutcher's fund |
| **Jaan Tallinn** | — | Skype co-founder, safety-focused |
| **Eric Yuan** | — | Zoom founder |

**Total raised:** $15B+

**Notable:** Both Google AND Amazon invested (rare). Microsoft invested despite OpenAI partnership (hedging).

---

## Recent developments

### Harness crackdown (Jan 2026)

**Jan 9**: Blocked third-party tools (OpenCode, etc.) from spoofing Claude Code headers to access Max subscription benefits.

**What happened:**
- Claude Code enforces token limits client-side: 5-hour rolling windows (~220K tokens for Max20) + weekly token caps
- "Hours" in Anthropic marketing (e.g., "24-40 hrs Opus/week") are estimated usage time, not separate limits — all token-based
- Third-party tools spoofed Claude Code headers to get Max authentication but bypassed rate limiting logic
- Result: overnight autonomous loops consuming weeks of token allocation in hours

**Fallout:**
- 147+ GitHub reactions, 245 HN points
- DHH called it "very customer hostile"
- Many Max subscribers canceled
- **xAI employees cut off** from Claude via Cursor — Tony Wu: "rly pushes us to develop our own coding product"
- OpenAI employees already blocked Aug 2025

**Official rationale** (Shihipar): Technical instability — unauthorized harnesses introduce bugs Anthropic can't diagnose.

**Response:** OpenCode launched "OpenCode Black" ($200/mo) via enterprise gateways.

**Thesis implication:** Not harness moat defense — compute arbitrage enforcement. Third-party harnesses still work via enterprise pricing (OpenCode Black). Anthropic protecting margin on Max subscription, not blocking competition.

---

### Trump AI Czar endorsement at Davos (Jan 23, 2026)

**[[David Sacks]]** (White House AI/Crypto Czar) highlighted Claude Code at Davos as the product "everyone's going crazy over":
- Called it "powered by Anthropic's Opus 4.5" — "a real breakthrough in coding"
- Described it as beginning of personal digital assistants — not just code, but all knowledge worker output
- Mentioned "co-work" tab: non-coders can create spreadsheets, PowerPoints, websites
- Can point at user's file drive and email — emulates style and format of existing work
- "Just need one more layer of abstraction on top of a tool like that and you'll have your own personal digital assistant"
- Predicted this could happen in 2026: coding assistants → personal digital assistants
- Referenced movie "Her" (Joaquin Phoenix, voice interface)

**Significance:** First time a sitting White House official has publicly endorsed a specific AI product by name at a major international forum. Reinforces Anthropic's positioning as the leading coding/agent AI company.

*Source: Davos panel (Sacks, Kratsios, Bartiromo), Jan 23 2026*

---

### IPO prep (Dec 2025)
- Engaged Wilson Sonsini (law firm)
- Valuation $300-350B post latest investments

**Product milestones:**
- **Claude Code hit $1B milestone**
- **Bun acquisition** — JavaScript runtime, infrastructure play
- **Agent Skills** open standard launched (Dec 18) — integrations with Notion, Canva, Figma, Atlassian

**Partnerships:**
- **DOE Genesis Mission** — Multi-year partnership across 17 national labs
- **Accenture** — 30,000 professionals to be trained, enterprise deployment focus

**Citi ASIC projections:**
- $0 (F25) → **$20.9B (F26E)** → $4.4B (F27E) via [[Broadcom]]

---

## Why more efficient than OpenAI

**Cumulative losses to profitability:**

| Company | Cumulative burn | Break-even | Source |
|---------|----------------|------------|--------|
| Anthropic | ~$12-15B | 2028 | WSJ, The Information |
| OpenAI | $115-143B | 2029-2030 | The Information, Deutsche Bank |

Anthropic needs **~8-10x less capital** than OpenAI to reach profitability.

OpenAI also faces a **$207B funding shortfall** through 2030 (HSBC).

**Daniela Amodei (CNBC, Jan 2026):**
> "Anthropic has always had a fraction of what our competitors have had in terms of compute and capital, and yet, pretty consistently, we've had the most powerful, most performant models."

> "We are just much more efficient at how we use those resources."

Dario's investor pitch: build cutting-edge models at **1/10th the cost**.

**Why:**
- Enterprise-focused (higher margins, stickier)
- Avoiding costly image/video generation
- Algorithmic efficiency over brute-force scale
- Less consumer acquisition cost

**OpenAI's commitments for comparison:**
- Stargate US: $500B over 4 years (SoftBank, Oracle, MGX)
- Stargate Norway: 100,000 GPUs by end 2026
- Total compute commitments by 2033: $1.4T (HSBC/Deutsche Bank)

---

## Compute strategy

**Multi-cloud approach** — AWS Trainium + Google TPUs + NVIDIA GPUs. Diversified to avoid single-vendor lock-in.

### Google Cloud deal (Oct 2025)

| Metric | Value |
|--------|-------|
| TPU commitment | Up to **1M TPUs** |
| Deal value | "Tens of billions of dollars" |
| Capacity | **1GW+** online in 2026 |
| Chip cost estimate | ~$35B of ~$50B total DC cost |

Largest expansion of Anthropic's TPU usage to date. Separate from Broadcom direct purchases.

### AWS partnership (Project Rainier)

| Metric | Value |
|--------|-------|
| Chips | Hundreds of thousands of Trainium |
| Facilities | Multiple US data centers |
| Relationship | "Primary training partner and cloud provider" |
| AWS revenue impact | 1-2 pp in late 2024, **5+ pp expected H2 2025** (Rothschild) |

### Broadcom direct TPUs (~1M TPUv7)

| Component | Source | Notes |
|-----------|--------|-------|
| TPUv7 chips | [[Broadcom]] direct | Anthropic-owned, not through Google |
| DC infrastructure | TeraWulf, Hut 8, Cipher Mining | Crypto miners pivoting |
| Operations | [[FluidStack]] | Cabling, burn-in, testing |

**Why direct purchase matters:**
- Independence from Google Cloud pricing
- Own infrastructure = lower long-term cost
- Validates [[Crypto-to-AI pivot]] thesis

### Summary: Three compute paths

| Path | Chips | Ownership | Use case |
|------|-------|-----------|----------|
| Google Cloud | TPUs | Rented | Flexible capacity |
| AWS | Trainium | Rented | Training, inference |
| Broadcom direct | TPUv7 | Owned | Core training clusters |

All roads lead to [[TSMC]] — TPUs and Trainium fabbed there.

---

## Strategic dependencies

- **[[Google]]** — Cloud partner, investor
- **[[Amazon]]** — Investor, AWS partnership
- **[[Broadcom]]** — TPU supplier

Less dependent on single partner than OpenAI-Microsoft.

---

## Agentic code moat

Anthropic is capturing the "agentic code orchestrator" niche:

- **Claude Code** — production agent, not autocomplete
- **Agent SDK** — platform for building agents
- **Trust layer** — enterprise won't let unreliable agents touch code
- **55% of enterprise AI spend** is coding — largest category

See [[Long Anthropic]] for full thesis.

---

## For theses

**[[Long Anthropic]]**: Agentic code orchestrator moat, enterprise trust
**[[Long TSMC]]**: Locking TSMC capacity via TPUs
**[[AI hyperscalers]]**: Validates AI capex
**[[Model lab economics]]**: Best-positioned lab for profitability

---

*Updated 2026-01-26*

## Related

- [[Claude]] — flagship AI product
- [[Dario Amodei]] — CEO and co-founder
- [[OpenAI]] — competitor, origin (founders left OpenAI)
- [[Google]] — $2B+ investor, cloud partner
- [[Amazon]] — $8B investor, primary cloud partner
- [[Microsoft]] — $5B investor (hedging OpenAI)
- [[NVIDIA]] — $10B investor
- [[Broadcom]] — TPU supplier (~1M TPUv7 direct)
- [[TSMC]] — foundry for TPUs
- [[TeraWulf]] — DC infrastructure partner
- [[Hut 8]] — DC infrastructure partner
- [[Cipher Mining]] — DC infrastructure partner
- [[FluidStack]] — deployment/operations partner
- [[Crypto-to-AI pivot]] — validates thesis (miners hosting AI)
- [[Long Anthropic]] — thesis
- [[Agentic AI]] — core capability (Claude Code)
- [[Model lab economics]] — profitability context
