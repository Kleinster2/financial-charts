---
aliases: [AI chip alternatives, GPU alternatives, NVIDIA competitors]
---
#concept #ai #chips #competition

**NVIDIA alternatives** — Companies building AI chips to compete with NVIDIA's GPU dominance. Most target inference (where CUDA moat is weaker) rather than training.

---

## Why alternatives matter

| Factor | Description |
|--------|-------------|
| NVIDIA dominance | ~90% AI chip market share |
| CUDA lock-in | Software ecosystem moat |
| Supply constraints | GPU shortages, allocation |
| Cost | H100s expensive ($25-40K) |
| Power | GPUs power-hungry |
| Concentration risk | Customers want optionality |

**Thesis:** No market stays 90% concentrated forever. Alternatives will capture share, especially in inference.

---

## Training vs Inference

| Market | NVIDIA position | Alternative opportunity |
|--------|-----------------|------------------------|
| **Training** | Dominant (CUDA essential) | Harder to displace |
| **Inference** | Strong but contestable | Power efficiency matters more |

**Key insight:** Training happens once. Inference happens billions of times. Power/cost efficiency wins in inference.

---

## The alternatives landscape

### US/Western startups

| Company | Approach | Stage | Valuation |
|---------|----------|-------|-----------|
| [[Groq]] | LPU, inference speed | Shipping | ~$2.8B |
| [[Cerebras]] | Wafer-scale chips | Shipping | ~$4B |
| [[Tenstorrent]] | RISC-V, open architecture | Shipping | ~$2.6B |
| [[SambaNova]] | Dataflow architecture | Shipping | ~$5B |
| [[Graphcore]] | IPU | Struggling | — |
| [[FuriosaAI]] | NPU, inference | Mass prod 2026 | ~$700M |

### Hyperscaler custom silicon

| Company | Chip | Use |
|---------|------|-----|
| [[Google]] | TPU | Training + inference |
| [[Amazon]] | Trainium, Inferentia | AWS customers |
| [[Microsoft]] | Maia | Azure (coming) |
| [[Meta]] | MTIA | Internal |

### China domestic (sanctioned)

| Company | Chip | Constraint |
|---------|------|------------|
| [[Huawei]] / [[Ascend]] | Ascend 910 | [[SMIC]] fab limits |
| [[Biren Tech]] | BR100 | Entity List |
| [[Enflame]] | CloudBlazer | Entity List |
| [[Kunlunxin]] | Kunlun | Baidu spinout |

### Incumbents

| Company | Approach | Status |
|---------|----------|--------|
| [[AMD]] | MI300X GPU | #2, gaining share |
| [[Intel]] | Gaudi | Struggling |
| [[Broadcom]] | Custom ASICs | Google TPU partner |

---

## Competitive approaches

| Approach | Companies | Advantage | Risk |
|----------|-----------|-----------|------|
| Wafer-scale | Cerebras | Massive parallelism | Yield, cost |
| Inference-optimized | Groq, FuriosaAI | Speed, power | Training can't do |
| Open architecture | Tenstorrent | No lock-in | Ecosystem |
| Custom silicon | Google, Amazon | Optimized for workload | R&D cost |
| RISC-V | Tenstorrent | Open ISA | Early |

---

## The CUDA moat

**Why NVIDIA is hard to displace:**

| Factor | Description |
|--------|-------------|
| Software ecosystem | CUDA, cuDNN, TensorRT |
| Developer familiarity | Millions trained on CUDA |
| Framework integration | PyTorch, TensorFlow optimized |
| Libraries | 15+ years of optimization |
| Network effects | More developers → more libraries → more developers |

**How alternatives compete:**
- Target inference (less CUDA-dependent)
- Offer massive cost/power savings
- Open-source software stacks
- Focus on specific workloads

---

## Investment thesis

**Bull case for alternatives:**
- Inference market growing faster than training
- Hyperscalers want supplier diversity
- Power efficiency increasingly critical
- NVIDIA can't supply everyone
- Some workloads don't need CUDA

**Bear case:**
- CUDA moat is real
- NVIDIA keeps innovating
- Switching costs high
- Most alternatives unprofitable
- Hyperscaler silicon stays internal

---

## Who's winning (2026)

| Company | Status |
|---------|--------|
| [[AMD]] | Gaining share, MI300 competitive |
| [[Groq]] | Inference speed leader, shipping |
| [[Cerebras]] | Training niche, big customers |
| Google TPU | Internal success |
| Amazon Inferentia | Growing AWS adoption |
| [[Tenstorrent]] | Early, Jim Keller credibility |
| [[FuriosaAI]] | Just entering mass production |
| Graphcore | Struggling |
| Intel Gaudi | Struggling |

---

## How to play it

**Direct (private):**
- Groq, Cerebras, Tenstorrent — need private access or IPO

**Public alternatives:**
- [[AMD]] — #2 GPU, MI300X competitive
- [[Broadcom]] — custom ASIC for Google

**Indirect:**
- Bet on customers diversifying (hyperscalers)
- Short NVIDIA concentration (risky)

---

## Related

- [[NVIDIA]] — dominant incumbent
- [[Groq]], [[Cerebras]], [[Tenstorrent]], [[SambaNova]] — US alternatives
- [[FuriosaAI]] — Korean alternative
- [[Ascend]] — China alternative
- [[AMD]] — #2 GPU
- [[CUDA moat]] — why NVIDIA is hard to displace
- [[Inference disaggregation]] — structural trend
- [[Long inference stack]] — thesis

