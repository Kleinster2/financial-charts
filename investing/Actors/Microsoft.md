---
aliases: [MSFT]
---
#actor #hyperscaler #usa

**Microsoft (Azure)** — Tier 1 AI hyperscaler, OpenAI partner, largest enterprise cloud.

---

## Relevance to semis

Microsoft is the largest AI infrastructure spender. OpenAI partnership makes them critical demand driver for NVIDIA GPUs.

---

## Charts

![[msft-90d.png]]

![[msft-vs-qqq.png]]

![[msft-fundamentals.png]]

*Q2 2012 loss (-$492M, aQuantive writedown) excluded from chart.*

---

## Chip strategy

- Massive [[NVIDIA]] buyer (OpenAI infrastructure)
- **Maia**: Custom AI accelerator (announced 2023)
- **Cobalt**: ARM-based CPU
- Designed in-house, fabbed at [[TSMC]]

---

## OpenAI relationship

**Partnership restructured (Oct 2024):**
- Was: Exclusive cloud provider, deeply intertwined
- Now: Losing exclusivity early 2030s
- Microsoft building own AI capabilities separately

OpenAI's compute needs still flow through Microsoft Azure → NVIDIA → TSMC. But Microsoft is hedging.

---

## Azure model-agnostic strategy

Unlike Google (Gemini-focused), Azure positioned as neutral AI facilitator:

| Model | Provider | Available on Azure |
|-------|----------|-------------------|
| GPT-4 / ChatGPT | [[OpenAI]] | ✓ (primary) |
| Claude | [[Anthropic]] | ✓ |
| Grok | [[xAI]] | ✓ |
| Llama | [[Meta]] | ✓ |
| DeepSeek R1 | DeepSeek | ✓ |

**Result:** Azure grew 40% in fiscal Q1 2026 (ended Sep 30).

**Strategic logic:**
- Customers pick best model for use case
- Microsoft wins regardless of which model dominates
- Reduces OpenAI dependency risk
- Attracts customers wary of vendor lock-in

---

## AI leadership overhaul (Jan 2026)

Nadella in "founder mode" — weekly cross-team AI meetings, hands-on product focus.

**Key appointments:**
| Role | Person | Background |
|------|--------|------------|
| CoreAI (developer tools) | Jay Parikh | Ex-Meta engineering head (left 2021) |
| Microsoft AI (models) | Mustafa Suleyman | DeepMind co-founder |
| Corporate strategy | Kathleen Hogan | Ex-HR chief |
| AI economics advisor | Rolf Harms | Long-standing MS strategist |
| Office suite + LinkedIn | Ryan Roslansky | LinkedIn CEO |

**Suleyman's unit:** Independent budget, own pay scale to compete for AI talent. Internal jealousy noted.

**Succession signals:**
- 16 direct reports to Nadella
- Young talent elevated: Asha Sharma (37), Charles Lamanna (37) leading AI product categories
- Nadella is 58, same age Ballmer left — expected to stay several more years

---

## Competitive position (Jan 2026)

**AI coding tools market share (CB Insights):**
| Product | Share |
|---------|-------|
| GitHub Copilot | 24.9% |
| [[Anthropic]] Claude | 24% |
| Cursor | 24% |

Startups (Anthropic, Anysphere/Cursor, Replit) eating into Microsoft's coding tool share.

**Microsoft 365 Copilot:**
- 150M MAU
- Behind ChatGPT (800M) and Gemini (650M)
- Monetization challenge vs free competitors

**Startup engagement:**
- Meeting with Applied Compute (AI agents, ex-OpenAI founders)
- Meeting with Mercor (AI hiring platform)

---

## Fairwater AI campus design

**Specialized DC architecture (per SemiAnalysis satellite analysis):**

| Building Type | Stories | Power | Cooling | Purpose |
|---------------|---------|-------|---------|---------|
| **GPU Building** | 2 | 300MW | Liquid | Ultra-dense GPU clusters |
| **CPU/Storage Building** | 1 | 48MW | Air | Storage, control plane, RL environments |

**Design rationale:**
- GPUs must be physically close for **network coherence** — drives ultra-dense 2-story design
- CPU-based RL environments don't strictly need same availability zone
- Co-location improves developer productivity

**Implication:** Purpose-built AI DCs are fundamentally different from legacy facilities. Validates [[GPU deployment bottleneck]] — can't just retrofit existing DCs for Blackwell-class workloads.

See [[AI datacenter architecture]] for full design patterns.

---

## TCJA repatriation (2018)

Microsoft repatriated ~$130B under the [[Tax Cuts and Jobs Act]] one-time tax holiday. Deployed into buybacks and acquisitions (including LinkedIn, GitHub era).

---

## Short interest history (quarterly)

| Quarter | SI % float | Stock | Note |
|---------|------------|-------|------|
| **Q1 2026** | **0.65%** | ~$477 | Lowest of Mag 7 |
| Q4 2025 | 0.70% | $— | Fell from 52.5M to 48.5M shares |
| Q3 2025 | — | $— | |
| Q2 2025 | — | $— | |

See [[Short interest]] for interpretation framework.

---

## Quick stats

| Metric | Value |
|--------|-------|
| Ticker | MSFT (NASDAQ) |
| Market cap | ~$3.4T |
| Revenue (FY25) | ~$281B |
| Revenue (FY26E) | ~$327B |
| Revenue (FY27E) | ~$376B |
| AI capex | $50B+ annually |
| Primary chip | [[NVIDIA]] GPUs |
| Custom silicon | Maia (AI), Cobalt (CPU) |
| Foundry exposure | [[TSMC]] |
| Fairwater GPU building | 300MW, 2-story, liquid-cooled |
| Short interest | **0.65%** (Jan 2026) — lowest Mag 7 |

*Updated 2026-01-20*

![[msft-price-chart.png]]

![[msft-fundamentals.png]]

*Note: Net income gaps in 2015 and 2017 exclude one-time charges — Nokia write-down ($7.6B, Jul 2015) and [[Tax Cuts and Jobs Act]] transition tax ($6.3B, Dec 2017).*

---

## For theses

**[[Long TSMC]]**: All roads lead to TSMC
**[[AI hyperscalers]]**: Tier 1, possibly largest spender

---

## Related

- [[AI hyperscalers]] — Tier 1 spender
- [[NVIDIA]] — primary GPU supplier
- [[TSMC]] — foundry (Maia, Cobalt chips)
- [[OpenAI]] — exclusive partner (loosening)
- [[Anthropic]] — Claude on Azure
- [[Google]], [[Amazon]], [[Meta]] — hyperscaler peers
- [[Intel Foundry Services]] — Maia 2 potential foundry
- [[Constellation Energy]] — nuclear PPA for data centers
- [[Nuclear power for AI]] — energy strategy
- [[Quantum computing]] — bet (topological qubits, Majorana 1)
- [[AI datacenter architecture]] — Fairwater campus design
- [[GPU deployment bottleneck]] — Satya's "can't plug in" quote
- [[Tax Cuts and Jobs Act]] — ~$130B repatriation (2018)
