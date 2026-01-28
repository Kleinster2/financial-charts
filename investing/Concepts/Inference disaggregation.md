#concept #ai #semiconductor #architecture

**Inference disaggregation** — LLM inference splits into two fundamentally different compute problems: prefill (parallel, compute-bound) and decode (sequential, memory-bound). Optimizing for both requires different silicon.

> **The core idea**: No single chip is optimal for both problems — so NVIDIA is choosing to combine architectures instead of forcing one chip to do everything.

> **The takeaway**: The bottleneck moved, and the winning platform moved with it.

---

## The key insight

LLM inference is not one problem — it's two:

| Phase | What it does | Bottleneck | Optimal silicon |
|-------|--------------|------------|-----------------|
| **Prefill** | Reads entire prompt at once | Compute (FLOPs) | GPU ([[NVIDIA]]) |
| **Decode** | Generates tokens one at a time | Memory bandwidth | SRAM ([[Groq]], [[Cerebras]]) |

**Why this matters**: NVIDIA GPUs dominate prefill but are inefficient at decode. Decode is becoming the dominant cost as context windows grow.

---

## Prefill (reading)

The model ingests the prompt:

| Property | Characteristic |
|----------|----------------|
| Parallelism | Massive — all tokens processed together |
| Math | Heavy matrix multiplication |
| Bottleneck | Compute-bound |
| Memory access | Predictable, batched |
| GPU fit | Excellent — what GPUs were designed for |

**NVIDIA dominates this phase.**

---

## Decode (writing)

The model generates output tokens:

| Property | Characteristic |
|----------|----------------|
| Parallelism | Minimal — one token at a time |
| Math | Relatively light |
| Bottleneck | Memory bandwidth |
| Memory access | Random, latency-sensitive |
| GPU fit | Poor — like "taking elevators to walk across a hallway" |

The bottleneck is moving data, not computing.

---

## Why GPUs are inefficient at decode

GPUs were designed for:
- Massive parallelism
- External memory access ([[HBM]])
- Flexibility across workloads

Decode is the opposite:
- Sequential
- Latency-sensitive
- Bandwidth-dominated
- Deterministic

**On-chip vs off-chip**: GPUs access external [[HBM]]. Decode-optimized chips use on-chip SRAM — orders of magnitude faster for the access patterns decode requires.

---

## SRAM architectures

[[Groq]] and [[Cerebras]] made the same bet:

| Decision | [[Trade]]-off | Decode benefit |
|----------|-----------|----------------|
| Large on-chip SRAM | Expensive in die area | Ultra-low latency |
| Deterministic execution | Less flexibility | No scheduling overhead |
| Older process nodes | Lower transistor density | Faster iteration, lower cost |

**The result**: 10x+ faster tokens/sec than GPUs at decode.

---

## The enabler: NVLink opening

**The hinge the whole deal swings on.**

Historically, NVIDIA's rule was:
- NVIDIA GPUs talk to other NVIDIA GPUs (NVLink, NVSwitch)
- Everyone else uses PCIe (much slower, higher latency)

**What changed (Blackwell/Rubin generation):**

| Before | After |
|--------|-------|
| Closed interconnect | NVLink-C2C for external chips |
| External = PCIe only | External = first-class NVLink |
| GPU-to-GPU only | GPU-to-accelerator cooperation |

This allows:
- Groq SRAM chip handles decode
- NVIDIA GPU handles prefill
- Data moves fast enough that the split actually works

**Without this, disaggregation collapses.** The latency of PCIe would kill the benefit of SRAM decode.

**Why NVIDIA did this now:**
- Position of strength move
- "You open the ecosystem after you've become unavoidable"
- Signals: "We are the platform, we will absorb specialists rather than crush them"
- NVIDIA doesn't have to be best at everything — just control the hub

---

## NVIDIA-Groq deal (Dec 2025)

NVIDIA licensed Groq's architecture rather than acquiring:

| Aspect | Details |
|--------|---------|
| Deal type | Non-exclusive licensing |
| NVIDIA gets | Groq engineers + IP for "Rubin SRAM" variant |
| Groq gets | NVIDIA validation + royalties |
| Groq independence | Continues operating GroqCloud |

**Jensen's logic**: Replicating Groq would require:
- Re-architecting memory hierarchy
- Sacrificing GPU generality
- Cannibalizing H100/H200 margins

Easier to license and integrate.

---

## NVIDIA's 3 Rubin variants

Gavin Baker's framework:

| Variant | Memory | Optimized for |
|---------|--------|---------------|
| **Rubin CPX** | GDDR (high capacity, lower bandwidth) | Massive context prefill |
| **Rubin** | [[HBM]] (balanced) | Training + batched inference |
| **Rubin SRAM** | SRAM (Groq-derived) | Low-latency agentic decode |

**Mix and match**: Optimal performance/cost for each workload.

---

## Strategic implications

### For NVIDIA
- Preserves GPU margins for training + prefill
- Adds decode capability without cannibalization
- Extends platform dominance to full inference stack

### For Groq
- Validation from industry leader
- Royalty stream
- Continues independent cloud business
- Competes with NVIDIA customers

### For Cerebras
- "Last independent SRAM player" (per Gavin Baker)
- Strategic acquisition target
- Wafer-scale harder to integrate than Groq's rack architecture
- Ahead of Groq on public benchmarks

---

## Economic implications

If decode costs fall materially:

| Effect | Beneficiary |
|--------|-------------|
| $/token drops | All AI users |
| Always-on agents viable | [[Agentic AI]] |
| Latency-sensitive apps explode | Voice, robotics, real-time |
| More inference demand | Full stack (training + inference) |

**Chamath's framing**: "Much cheaper → much more valuable → more developer pull."

---

## SRAM economics: latency premium, not replacement

**Critical nuance**: SRAM wins on latency, not cost efficiency.

| Metric | GPU ([[HBM]]) | SRAM (Groq/Cerebras) |
|--------|-----------|----------------------|
| Throughput/$ | Better | Worse |
| Latency/user | Worse | Much better |
| Batch efficiency | High | Low |
| Use case | Bulk inference | Real-time, agentic |

**SRAM is a premium feature**, not a GPU replacement. Users pay more for:
- Instant responses
- Voice interaction
- Multi-step reasoning loops
- Real-time copilots

This is why NVIDIA complements rather than replaces — different economic profiles for different workloads.

---

## SRAM limitations

SRAM-based decode is not universal:

| Works well | Doesn't help |
|------------|--------------|
| Short-to-medium context | Very long-context generation |
| Single-user latency | High-throughput batching |
| Agentic reasoning | Training |
| Real-time voice | Memory-heavy tasks |

Still relies on other chips for prefill and memory-intensive workloads.

---

## ASIC consolidation thesis

Gavin Baker's prediction:

> "All ASICs except TPU, AI5 and Trainium will eventually be canceled."

**Survivors:**

| Player | Why survives |
|--------|--------------|
| NVIDIA | 3 Rubin variants + ecosystem |
| [[Google]] TPU | Vertical integration |
| [[Amazon]] Trainium | Vertical integration |
| [[Cerebras]] | Unique niche (wafer-scale) |

**At risk:**

| Player | Problem |
|--------|---------|
| [[Meta]] ASIC | "Surprisingly weak" |
| [[Microsoft]] ASIC | Can't compete with Rubin |
| Most startups | Ecosystem gravity |
| [[Intel]]/[[SambaNova]] | Late, weaker |

**The dynamic**: "Consolidation by ecosystem gravity, not brute force."

The 3 Rubin variants + networking chips make standalone competition nearly impossible. Only vertically integrated hyperscalers or extreme niche players survive.

---

## What to watch

- [ ] Groq GroqCloud growth post-NVIDIA deal
- [ ] Cerebras strategic positioning (acquisition target?)
- [ ] Rubin SRAM variant timeline
- [ ] Decode-heavy workload pricing (agentic, voice)
- [ ] Prefill/decode cost ratio changes

---

## Related

- [[Groq]] — Decode-optimized, NVIDIA licensed
- [[Cerebras]] — Last independent SRAM player
- [[NVIDIA]] — Platform consolidator
- [[Agentic AI]] — Decode-heavy use case
- [[SambaNova]] — Acquired by [[Intel]]
