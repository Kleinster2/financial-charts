#concept #chips #architecture

# Training-inference convergence

The distinction between AI training and inference hardware is blurring. Workloads that were once separate now share similar compute requirements.

---

## What's happening

Historically:
- **Training**: Massive parallel compute, high memory bandwidth, batch processing
- **Inference**: Lower compute, latency-sensitive, cost-optimized

Now converging because:
- **Larger models**: Inference on 400B+ parameter models needs training-class hardware
- **Chain-of-thought**: Models "think" longer, more compute per query
- **Agentic workflows**: Multi-step reasoning, tool use, iteration
- **Real-time generation**: Video, audio, multimodal — inference becomes compute-heavy

---

## Evidence

| Company | Action | Date |
|---------|--------|------|
| [[Amazon]] | Discontinued Inferentia, Trainium handles both | Dec 2024 |
| [[NVIDIA]] | H100/H200/B200 used for training and inference | 2023-25 |
| [[Google]] | TPU v7 Ironwood marketed for inference at training scale | Nov 2025 |

---

## Implications

**For chip design:**
- Fewer specialized ASICs needed
- Unified architectures win (NVIDIA's advantage)
- Memory bandwidth matters for both workloads

**For [[Long Broadcom]]:**
- ASIC customers may consolidate chip designs
- Fewer SKUs but larger volumes per design

**For [[Inference economics]]:**
- Cost models based on "cheap inference" may be wrong
- Inference costs stay higher than expected

**For NVIDIA moat:**
- Unified CUDA ecosystem more valuable
- Harder for inference-only startups ([[Groq]]) to compete on total cost

---

## Counter-argument

Some workloads remain distinct:
- Edge inference (mobile, IoT) still needs efficiency-optimized chips
- Batch inference at scale may still favor specialized hardware
- Enterprise inference buyers prioritize cost/latency, not training capability

The convergence is strongest at the frontier model scale.

---

## The NVIDIA-Groq tension

[[NVIDIA]] acquired [[Groq]] for $20B (Dec 2025) — an inference-specialist. If convergence is real, why pay $20B for inference-only architecture?

Possible explanations:
1. **Competitive elimination**: Remove threat before it scales (Groq claimed 10x faster, 1/10th energy)
2. **Hedging**: Convergence may not be complete — edge/cost-sensitive inference stays distinct
3. **Technology acquisition**: Groq's deterministic LPU architecture is novel, may integrate into NVIDIA silicon
4. **Market segmentation**: Training companies see convergence, but inference *buyers* still want specialized cheap/fast inference

**Implication**: The convergence thesis may be overstated, or applies only to chip *designers* (Amazon), not chip *buyers* (enterprises). NVIDIA betting both ways.

---

*Updated 2025-12-30*

Related: [[Hyperscaler chip roadmap]], [[Amazon]], [[NVIDIA]], [[Google]], [[Groq]], [[Inference economics]], [[Long Broadcom]]
