---
aliases: [TurboQuant, PolarQuant, QJL, Quantized Johnson-Lindenstrauss]
tags: [product, ai, inference, compression, google]
---

# TurboQuant

[[Alphabet|Google]] Research's KV-cache compression algorithm suite, formally unveiled March 25, 2026. Reduces LLM memory usage by 6x and speeds attention computation by 8x — with zero accuracy loss and no retraining required. The market reaction was immediate: memory stocks ([[Micron]], [[SanDisk]], [[Seagate]]) sold off on fears of reduced AI memory demand, though [[Jevons' Paradox]] suggests the freed capacity may simply enable larger models and longer contexts rather than shrinking the total memory market.

---

## Quick stats

| Metric | Value |
|--------|-------|
| Developer | [[Alphabet|Google]] Research |
| Announced | March 25, 2026 |
| Target | KV (key-value) cache in LLM inference |
| Memory reduction | 6x (KV cache) |
| Speed improvement | 8x (attention logit computation on [[NVIDIA]] H100) |
| Minimum quantization | 3-bit (no retraining) |
| Accuracy loss | Zero (perfect recall on Needle-in-a-Haystack at 100K tokens) |
| Cost reduction estimate | 50%+ for enterprises (VentureBeat) |
| Availability | Open research framework, free including commercial use |
| Pre-print | arXiv:2504.19874 (Apr 2025), arXiv:2406.03482, arXiv:2502.02617 |
| Conferences | [[ICLR]] 2026 (Rio de Janeiro), AISTATS 2026 (Tangier) |

---

## How it works

TurboQuant is a two-stage compression system targeting the KV cache — the "digital cheat sheet" that stores past computation results so the model doesn't recompute them. As context windows expand (100K+ tokens), the KV cache becomes the dominant memory bottleneck, consuming GPU VRAM and throttling inference speed.

### Stage 1: PolarQuant

Traditional quantization encodes vectors in Cartesian coordinates (X, Y, Z). PolarQuant converts vectors to polar coordinates — reducing each to a radius (data strength) and direction angles (data meaning). After random rotation, angle distributions become highly predictable and concentrated, eliminating the need for expensive per-block normalization constants that typically add 1-2 bits of overhead and negate compression gains. Google's analogy: instead of "go 3 blocks East, 4 blocks North," the instruction becomes "go 5 blocks at 37 degrees."

### Stage 2: Quantized Johnson-Lindenstrauss (QJL)

PolarQuant leaves residual errors. QJL applies a 1-bit error correction layer, reducing each error vector to a sign bit (+1 or -1). This serves as a zero-bias estimator — when the model calculates attention scores (deciding which tokens in the prompt are most relevant), the compressed version remains statistically identical to the full-precision original.

The combination achieves what previous quantization methods couldn't: sub-4-bit compression without degraded outputs. Most 3-bit quantization systems suffer significant logic degradation; TurboQuant at 3-bit maintains perfect recall.

---

## Benchmarks

| Test | Model | Result |
|------|-------|--------|
| Needle-in-a-Haystack (100K tokens) | Llama-3.1-8B, Mistral-7B | Perfect recall — matches uncompressed |
| Semantic search recall | Multiple | Superior to RabbiQ, Product Quantization (PQ) |
| Attention logit speed (4-bit) | [[NVIDIA]] H100 | 8x vs 32-bit unquantized baseline |
| Community port (Qwen3.5-35B on MLX) | 8.5K-64K context | 100% exact match at all quantization levels; 2.5-bit ≈ 5x KV cache reduction |

---

## Market discovery timeline

| Date | Event | Market reaction |
|------|-------|----------------|
| Apr 2025 | Original PolarQuant pre-print on arXiv | No market reaction — academic paper |
| Jun 2024 | QJL pre-print published | None |
| Feb 2025 | PolarQuant extended paper | None |
| Mar 25, 2026 | Google Research formal blog post unveiling TurboQuant suite | [[Micron]] -3.9%, [[SanDisk]] -3.5%, [[Seagate]] down (exact TBD); Google Research tweet: 7.7M+ views in 24 hours |
| Mar 25-26 | Community ports to MLX (Apple Silicon) and llama.cpp within 24 hours | Accelerated fear of reduced memory demand |

The papers existed for nearly a year before Google chose to formally unveil them as a production-ready suite. The timing — at ICLR 2026 — was strategic, coinciding with the "Agentic AI" wave where massive context windows and searchable vector memory are critical infrastructure.

---

## Investment implications

The memory stock selloff reflects a binary reading: less memory needed per model → less demand for DRAM/NAND. But the more likely outcome follows [[Jevons' Paradox]]:

1. If inference costs drop 50%, usage scales — longer contexts, more concurrent users, cheaper agent orchestration
2. Freed VRAM enables running models that previously required multi-GPU setups on single GPUs — expanding the addressable market
3. Mobile/edge AI benefits most — smartphone NPUs can now run meaningfully larger models locally, which increases hardware upgrade cycles
4. The real losers aren't memory makers but cloud inference providers with pricing power built on scarcity (i.e., GPU compute costs as moat)

VentureBeat: TurboQuant provides "the essential plumbing for the burgeoning Agentic AI era: the need for massive, efficient, and searchable vectorized memory that can finally run on the hardware users already own."

The semantic search application is underappreciated — TurboQuant achieves superior recall vs existing methods with near-zero indexing time, making it ideal for real-time vector databases where data is constantly added.

---

## Related

- [[Alphabet]] — parent company
- [[Google]] — research division
- [[NVIDIA]] — H100 benchmark hardware; 8x speedup measured on H100
- [[Micron]] — memory stock impacted by selloff
- [[SanDisk]] — memory stock impacted by selloff
- [[Jevons' Paradox]] — efficiency gains historically increase total consumption
- [[Co-Packaged Optics]] — adjacent AI inference efficiency technology
- [[AI inference]] — the workload TurboQuant optimizes

---

*Sources: Google Research blog (Mar 25), Ars Technica (Mar 25), VentureBeat (Mar 25), TechCrunch (Mar 25), SiliconANGLE (Mar 25), arXiv:2504.19874, arXiv:2406.03482, arXiv:2502.02617, 247 Wall St (Mar 26), community benchmarks (@Prince_Canuma on X).*
