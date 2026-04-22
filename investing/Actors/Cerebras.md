---
aliases: []
---
#actor #ai #semiconductor #usa #private

**Cerebras** — Wafer-scale AI chips. Entire wafer = one chip. Training + inference. Last independent SRAM player after NVIDIA-Groq deal.

---

## Why Cerebras matters

Post-NVIDIA-Groq positioning (per Gavin Baker):

> "Cerebras is now in a very interesting and highly strategic position as the last independent SRAM player that was ahead of Groq on all public benchmarks."

| Metric | Value |
|--------|-------|
| Valuation | ~$22B (Jan 2026 talks) |
| Previous valuation | $8.1B (Sep 2025) |
| Total raised | $2B+ |
| Founded | 2016 |
| Approach | Wafer-scale integration |
| Strategic position | Last independent SRAM player |

---

## Wafer-scale engine (WSE)

One wafer = one chip:

| Spec | WSE-3 |
|------|-------|
| Transistors | 4 trillion |
| Cores | 900,000 |
| Size | 46,225 mm² |
| vs GPU | 56x larger than [[H100]] |

Biggest chip ever made.

---

## Why wafer-scale?

Eliminates interconnect bottleneck:
- No chip-to-chip communication
- Massive on-chip memory bandwidth
- Designed for large AI models
- Single chip = simpler programming

---

## CS-3 system

Complete AI system:
- WSE-3 chip
- 44GB on-chip SRAM
- 125 petaflops FP16
- Inference + training

---

## Business model

Systems + cloud:
- Sell complete systems ($2-[[3M]]+)
- Cerebras Cloud inference
- Condor Galaxy supercomputer (with [[G42]])
- Enterprise + sovereign AI

---

## Customers

| Customer | Use Case |
|----------|----------|
| [[G42]] ([[UAE]]) | Condor Galaxy cluster |
| [[GSK]] | Drug discovery |
| [[AstraZeneca]] | Pharma AI |
| National labs | Research |

---

## January 2026 developments

### $1B raise at $22B valuation

| Metric | Value |
|--------|-------|
| Round size | ~$1B (in talks) |
| Pre-money valuation | $22B |
| Previous (Sep 2025) | $8.1B |
| Increase | 2.7x in 4 months |
| IPO target | Q2 2026 |

Significance: Among largest private AI hardware raises ever. Validates "last independent SRAM player" thesis.

### OpenAI $10B+ compute deal (Jan 14, 2026)

| Detail | Value |
|--------|-------|
| Deal value | $10B+ |
| Compute | 750 MW |
| Duration | 2026-2028 (multi-year) |
| Customer | [[OpenAI]] |

Game-changer: OpenAI diversifying beyond NVIDIA. Cerebras now has two mega-customers (OpenAI + [[G42]]).

Why OpenAI chose Cerebras:
- Inference cost advantage (SRAM)
- Reduce NVIDIA dependency
- Capacity availability
- [[Sam Altman]] was early Cerebras investor
- 15x faster responses than GPU-based systems

---

## [[GPT]]-5.3-[[Codex]]-Spark: first non-NVIDIA [[GPT]] model (Feb 2026)

The OpenAI deal's first concrete output — and a landmark for the inference market:

| Detail | Value |
|--------|-------|
| Model | [[GPT]]-5.3-[[Codex]]-Spark |
| Hardware | Cerebras Wafer Scale Engine 3 |
| Speed | 1,000+ tokens/sec |
| Benchmark | 77.3% on [[Terminal-Bench]] 2.0 (vs 64% for [[GPT]]-5.2-[[Codex]]) |
| Context | 128K, text-only |
| Availability | [[ChatGPT]] Pro, [[Codex]] app/CLI/VS Code |
| Significance | OpenAI's first [[GPT]] model that does not run on [[NVIDIA]] |

The model is optimized for real-time code editing — developers get immediate feedback on targeted edits to code, logic, or interfaces. Complements long-running frontier models (which work autonomously for hours/days) with a latency-first tier for interactive work.

[[Infrastructure]] integration: Cerebras's low-latency path was integrated into OpenAI's production serving stack alongside GPU infrastructure. OpenAI's framing: GPUs remain fundamental for training and broad inference; Cerebras excels where extremely low latency matters. Not a replacement — a dedicated tier.

Latency improvements shipped alongside [[Codex]]-Spark:
- WebSocket connection reduced per-roundtrip overhead by 80%
- Per-token overhead down 30%
- Time-to-first-token cut in half
- WebSocket path default for [[Codex]]-Spark, rolling out to all models

*Source: [Techzine](https://www.techzine.eu/news/analytics/138754/openai-swaps-nvidia-for-cerebras-with-gpt-5-3-codex-spark/) (Feb 2026), [Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/openai-lauches-gpt-53-codes-spark-on-cerebras-chips) (Feb 2026)*

---

## Andrew Feldman vs NVIDIA (Mar 2026)

Cerebras CEO has been publicly attacking [[NVIDIA]]'s inference position on [[LinkedIn]] for months:

Core argument: [[CUDA moat|CUDA]] is only needed for training, not inference. As the industry shifts to inference-dominant workloads, NVIDIA's software lock-in dissolves. The mental moat that kept enterprises on GPUs doesn't apply when the workload is fundamentally different.

This is aggressive positioning ahead of GTC, where NVIDIA plans to unveil its [[Groq]]-based inference platform — a direct competitive response to Cerebras's OpenAI wins.

---

## Apr 17, 2026 — OpenAI commitment expands, IPO revived

The renewed US IPO filing and the same-day reporting on the enlarged [[OpenAI]] relationship turned Cerebras from an architecture story into a public-markets underwriting question. The core issue is no longer whether the product is differentiated. It is whether investors are willing to fund a business whose forward demand looks enormous while the disclosed 2025 base was still concentrated in Abu Dhabi-linked customers and GAAP profitability depended on non-operating income.

See [[Cerebras IPO revival April 2026]] for the full event note, including the customer-concentration math, the operating-loss to net-income bridge, and the split between realized 2025 economics and the forward OpenAI story.

---

## IPO filing

Filed September 2024:
- First major AI chip IPO attempt
- Revealed $136M revenue (2023)
- Heavy losses
- [[G42]] concentration risk flagged
- IPO now targeting Q2 2026

---

## Post-NVIDIA-Groq landscape

After NVIDIA licensed [[Groq]]'s architecture (Dec 2025):

| Player | Status |
|--------|--------|
| [[Groq]] | NVIDIA partner, continues cloud |
| [[SambaNova]] | [[Acquired]] by [[Intel]] |
| Cerebras | Last independent SRAM player |

Why Cerebras wasn't acquired:

| Factor | Groq | Cerebras |
|--------|------|----------|
| Integration | Many-chip rack, fits [[NVLink]] | WSE = independent rack |
| Architecture | Easier to integrate | Harder to merge |
| Benchmarks | Strong | Ahead of Groq (public) |

Cerebras's wafer-scale approach makes integration harder — but may preserve independence.

---

## Strategic options

1. Stay independent — IPO, compete with [[Rubin]] SRAM
2. Hyperscaler acquisition — [[Google]], [[Amazon]], [[Microsoft]]
3. NVIDIA deal — Similar to Groq (licensing)
4. Sovereign AI focus — [[G42]] relationship, geopolitics

The bull case: Being last independent SRAM player = strategic scarcity value.

---

## Investment case

Bull:
- Last independent SRAM player — strategic scarcity
- Ahead of Groq on public benchmarks
- Differentiated architecture (wafer-scale)
- Large model specialist
- IPO = liquidity event
- Potential acquisition target

Bear:
- NVIDIA [[Rubin]] SRAM competes directly
- Customer concentration ([[G42]])
- High system costs
- Integration difficulty limits partnerships
- Unproven at scale

---

## Cap table / Investors

| Round | Amount | Valuation |
|-------|--------|-----------|
| Series A | $25M | — |
| Series B | $60M | — |
| Series C | $112M | — |
| Series D | $250M | — |
| Series E | $250M | ~$4B |
| Sep 2025 | — | $8.1B |
| Jan 2026 (talks) | ~$1B | $22B |
| Total | $2B+ | |

Key investors:

| Investor | Notes |
|----------|-------|
| [[Benchmark]] | Early (Series A) |
| [[Eclipse Ventures]] | Early |
| Alpha Wave Global | Growth (Series F) |
| [[Altimeter Capital]] | Growth |
| [[Coatue]] | Growth |
| [[UAE G42]] | Strategic (Condor Galaxy) |

[[G42]] relationship: Strategic partner and customer — built Condor Galaxy supercomputer together.

---

## Quick stats

| Metric | Value |
|--------|-------|
| Ticker | Private (IPO Q2 2026) |
| Valuation | ~$23.1B last private mark; IPO fundraising reportedly targets ~$35B |
| Total raised | $2B+ |
| Approach | Wafer-scale chips |
| Product | WSE-3, CS-3 |
| Position | Last independent SRAM player |
| Key customers | OpenAI ($20B+ potential), [[G42]] |

*Updated 2026-04-17*

---

## Related

### Customers
- [[OpenAI]] — $20B+ potential multi-year compute commitment (Apr 2026 update)
- [[UAE G42]] — Condor Galaxy, strategic partner

### Competitors
- [[NVIDIA]] — competitor, potential acquirer
- [[Groq]] — former competitor (now NVIDIA partner)
- [[SambaNova]] — former competitor ([[Intel]]-acquired)
- [[Tenstorrent]] — AI chip peer

### Concepts
- [[Inference disaggregation]] — market context (SRAM for decode)
- [[Long Cerebras]] — thesis (last independent SRAM player)

### Sources
- [Bloomberg: Cerebras $22B Valuation](https://www.bloomberg.com/news/articles/2026-01-13/cerebras-in-discussions-to-raise-funds-at-22-billion-valuation)
- [TechCrunch: OpenAI Cerebras Deal](https://techcrunch.com/2026/01/14/openai-signs-deal-reportedly-worth-10-billion-for-compute-from-cerebras/)
- [Reuters: Cerebras discloses US IPO filing](https://www.reuters.com/technology/nvidia-rival-cerebras-reveals-us-ipo-filing-ai-boom-drives-listings-2026-04-17/)
- [Reuters: OpenAI to spend more than $20 billion on Cerebras chips](https://www.reuters.com/technology/openai-spend-more-than-20-billion-cerebras-chips-receive-equity-stake-2026-04-17/)

