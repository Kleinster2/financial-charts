---
aliases: []
---
#actor #ai #semiconductor #usa #private

**Groq** — LPU inference chips. Fastest tokens/sec. NVIDIA licensed their architecture (Dec 2025). Founded by ex-Google TPU architect.

---

## Why Groq matters

**The NVIDIA validation**: In December 2025, NVIDIA licensed Groq's architecture for "Rubin SRAM" inference chips. This confirms the [[Inference disaggregation]] thesis — decode needs different silicon than prefill.

| Metric | Value |
|--------|-------|
| Valuation | ~$2.8B (2024) |
| Raised | $640M+ |
| Founded | 2016 |
| Founder | Jonathan Ross (Google TPU inventor) |
| NVIDIA deal | Non-exclusive license (Dec 2025) |

---

## Language Processing Unit (LPU)

**Inference-optimized architecture:**
- Deterministic execution
- No HBM dependency (SRAM-based)
- Predictable latency
- 500+ tokens/sec on Llama

---

## Speed advantage

| Metric | Groq | GPU comparison |
|--------|------|----------------|
| Tokens/sec | 500+ | ~50-100 |
| Latency | Ultra-low | Variable |
| Power efficiency | Better | Higher power |

10x+ faster inference than GPUs.

---

## GroqCloud

**Inference API service:**
- Pay-per-token pricing
- Fastest API available
- Open models (Llama, Mixtral)
- Developer-friendly

---

## Business model

**Cloud-first:**
- GroqCloud API (primary)
- On-prem systems
- Inference-as-a-service
- Not selling chips directly

---

## Technical approach

**Tensor Streaming Processor (TSP):**
- Deterministic dataflow
- Compiler does scheduling
- No runtime decisions
- Predictable performance

---

## NVIDIA licensing deal (Dec 2025)

**$20B "backdoor acquisition"** — technically a non-exclusive licensing deal, structured to avoid triggering antitrust review. Part of broader [[AI consolidation]] pattern where Big Tech uses acqui-hires instead of outright acquisitions.

**The architecture that won NVIDIA over:**

Groq made three contrarian bets a decade ago:
1. **Older process nodes** — faster iteration, lower yield risk
2. **Huge on-chip SRAM** — expensive but ultra-low latency
3. **Deterministic execution** — no scheduling overhead

This made Groq:
- Bad at training
- Irrelevant for prefill
- Exceptional at decode

**Deal structure:**

| Aspect | Details |
|--------|---------|
| Type | Non-exclusive licensing + asset purchase |
| Price | **$20B** (NVIDIA's largest deal ever) |
| NVIDIA gets | Full hardware stack, compiler toolchain, silicon design, key engineers |
| Key moves | Jonathan Ross (founder), Sunny Madra (president) → NVIDIA |
| GroqCloud | Continues under new CEO **Simon Edwards** |
| Independence | GroqCloud operates independently, NVIDIA gets IP |

**Regulatory strategy:** Structured as "reverse acqui-hire" to avoid antitrust review. Groq technically remains independent, but NVIDIA gets all the valuable IP and talent.

**Why NVIDIA licensed vs built:**
- Re-architecting GPU memory hierarchy = hard
- Would sacrifice GPU generality
- Would cannibalize H100/H200 margins

Jensen chose to extend the platform rather than disrupt himself.

---

## Jonathan Ross

**The hidden giant:**
- Invented Google's TPU
- Founded Groq 2016
- Designed V2 → V4 architecture roadmap
- "A genius of biblical proportions" — Chamath

TPU credibility mattered when NVIDIA evaluated external silicon.

---

## Limitations

**Trade-offs:**
- Inference only (no training)
- Smaller models preferred
- SRAM = less memory capacity
- New ecosystem

---

## Investment case

**Bull:**
- NVIDIA licensing validates architecture
- Fastest inference speeds (decode)
- TPU architect pedigree (Jonathan Ross)
- Inference market growing
- Royalty stream + independent cloud
- Positioned for agentic AI workloads

**Bear:**
- Non-exclusive license = NVIDIA can compete
- Training still on GPUs
- Memory capacity limits (SRAM trade-off)
- [[Cerebras]] ahead on some benchmarks

---

## Post-deal positioning

| Aspect | Groq position |
|--------|---------------|
| vs NVIDIA | Partner, not competitor |
| vs Cerebras | Both SRAM, different integration |
| Cloud business | Continues independently |
| Long-term | Royalties from Rubin SRAM |

**Not Slack 2.0**: Chamath emphasizes Groq remains infrastructure layer, not point product. Stack expansion, not displacement.

---

## Cap table / Investors

| Round | Date | Amount | Valuation |
|-------|------|--------|-----------|
| **Sept 2025** | Sept 2025 | **$750M** | **$6.9B** |
| Series A-D | Through 2024 | $640M+ total | ~$2.8B |
| **Total raised** | | **$1.4B+** | |

**Key Sept 2025 investors:** BlackRock, Neuberger Berman, Samsung, Cisco, Altimeter, 1789 Capital

**3 months later:** NVIDIA acquired IP + team for $20B (Dec 2025).

**Jonathan Ross net worth:** **$1.1B** (Bloomberg Billionaires, Nov 2025)

**Notable:** Ross has no college degree — dropped out before high school. Invented Google TPU as side project while working on ads.

**Key investors:**

| Investor | Notes |
|----------|-------|
| [[Craft Ventures]] | David Sacks (led Series D) |
| Tiger Global | Growth |
| D1 Capital | Growth |
| BlackRock | Growth |
| Samsung | Strategic |
| Social Capital | Chamath Palihapitiya |

**Total raised:** $640M+

---

## Quick stats

| Metric | Value |
|--------|-------|
| Ticker | Private |
| Valuation | ~$2.8B |
| Approach | LPU inference chips |
| Founder | Jonathan Ross (ex-Google TPU) |
| NVIDIA deal | Dec 2025 licensing |

*Updated 2026-01-22*

---

## Related

- [[NVIDIA]] — acquirer ($20B deal, Dec 2025)
- [[AI consolidation]] — Groq deal exemplifies stealth acquisition pattern
- [[FuriosaAI]] — remaining independent inference competitor
- [[Cerebras]] — remaining independent competitor (training focus)
- [[SambaNova]] — competitor (AI inference)
- [[Google]] — founder origin (Jonathan Ross invented TPU)
- [[Craft Ventures]] — investor (David Sacks)
- [[Inference disaggregation]] — thesis context
- [[Agentic AI]] — use case (fast decode for agents)
- [[NPU]] — technology category
- [[Power constraints]] — why inference efficiency matters

