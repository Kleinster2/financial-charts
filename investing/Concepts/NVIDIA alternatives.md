---
aliases: [AI chip alternatives, GPU alternatives, NVIDIA competitors]
---
#concept #ai #chips #competition

NVIDIA alternatives — Companies building AI chips to compete with the dominant GPU stack. Most target inference where the [[CUDA moat]] is weaker rather than training.

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

Thesis: No market stays 90% concentrated forever. Alternatives will capture share, especially in inference.

---

## Training vs Inference

| Market | NVIDIA position | Alternative opportunity |
|--------|-----------------|------------------------|
| Training | Dominant (CUDA essential) | Harder to displace |
| Inference | Strong but contestable | Power efficiency matters more |

Key insight: Training happens once. Inference happens billions of times. Power/cost efficiency wins in inference.

---

## The alternatives landscape

### US/Western startups

| Company | Approach | Stage | Valuation |
|---------|----------|-------|-----------|
| [[Groq]] | LPU, inference speed | Acquired by NVIDIA (Dec 2025) | $20B deal |
| [[Cerebras]] | Wafer-scale chips | [[Shipping]] | ~$4B |
| [[Tenstorrent]] | [[RISC-V]], open architecture | [[Shipping]] | ~$2.6B |
| [[SambaNova]] | Dataflow architecture | [[Shipping]] | ~$5B |
| [[Graphcore]] | IPU | Struggling | — |
| [[FuriosaAI]] | [[NPU]], inference | Mass prod Jan 2026 | $735M |

### Hyperscaler custom silicon

| Company | Chip | Use |
|---------|------|-----|
| [[Google]] | TPU | Training + inference |
| [[Amazon]] | Trainium, Inferentia | AWS customers |
| [[Microsoft]] | Maia | Azure (coming) |
| [[Meta]] | MTIA | Internal |

### [[China]] domestic (sanctioned)

| Company | Chip | Constraint |
|---------|------|------------|
| [[Huawei]] / [[Ascend]] | Ascend 910 | [[SMIC]] fab limits |
| [[Biren Tech]] | BR100 | Entity List |
| [[Enflame]] | CloudBlazer | Entity List |
| [[Kunlunxin]] | Kunlun | [[Baidu]] spinout |

#### May 2026: Huawei's post-node path

Huawei's [[Tau Scaling Law]] / [[LogicFolding]] announcement makes the China alternatives story less purely about duplicating NVIDIA's chip spec sheet. The company is trying to substitute at the architecture and system layer: shorten interconnect, reduce latency, co-optimize software/silicon, and bind many domestic chips into usable clusters. Fall 2026 [[Kirin]] chips are the first commercial test; [[Ascend]] and large AI clusters are the later strategic target.

This reinforces the core alternatives thesis in China: a sovereign chip does not need to beat [[NVIDIA]] globally if export controls, procurement pressure, and domestic model deployment make it the default local target. The bear case remains power, heat, tooling, and system integration.

### Incumbents

| Company | Approach | Status |
|---------|----------|--------|
| [[AMD]] | MI300X GPU | \#2, gaining share |
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
| [[RISC-V]] | Tenstorrent | Open ISA | Early |

---

## The CUDA moat

Why NVIDIA is hard to displace:

| Factor | Description |
|--------|-------------|
| Software ecosystem | CUDA, cuDNN, TensorRT |
| Developer familiarity | Millions trained on CUDA |
| Framework integration | PyTorch, TensorFlow optimized |
| Libraries | 15+ years of optimization |
| [[Network effects]] | More developers → more libraries → more developers |

How alternatives compete:
- [[Target]] inference (less CUDA-dependent)
- Offer massive cost/power savings
- Open-source software stacks
- Focus on specific workloads

---

## Investment thesis

Bull case for alternatives:
- Inference market growing faster than training
- Hyperscalers want supplier diversity
- Power efficiency increasingly critical
- NVIDIA can't supply everyone
- Some workloads don't need CUDA

Bear case:
- CUDA moat is real
- NVIDIA keeps innovating
- Switching costs high
- Most alternatives unprofitable
- Hyperscaler silicon stays internal

---

## Who's winning (Jan 2026)

| Company | Status |
|---------|--------|
| [[AMD]] | Gaining share, MI300 competitive |
| [[Groq]] | Acquired by NVIDIA ($20B, Dec 2025) |
| [[Cerebras]] | Training niche, big customers |
| Google TPU | Internal success |
| Amazon Inferentia | Growing AWS adoption |
| [[Tenstorrent]] | Early, Jim Keller credibility |
| [[FuriosaAI]] | Mass production started, LG design win |
| Graphcore | Struggling |
| Intel Gaudi | Struggling |

Post-Groq landscape: NVIDIA absorbed its most visible inference competitor. [[FuriosaAI]] and [[Cerebras]] are now the leading independent AI chip startups.

---

## How to play it

Direct private exposure:
- Groq, Cerebras, Tenstorrent — need private access or IPO

Public alternatives:
- [[AMD]] — \#2 GPU, MI300X competitive
- [[Broadcom]] — custom ASIC for Google

Indirect exposure:
- Bet on customers diversifying (hyperscalers)
- Short NVIDIA concentration (risky)

## China hyperscaler custom silicon (May 2026)

ByteDance's reported training ASIC and ReRAM inference-chip work with [[InnoStar Semiconductor]] adds a third China path beyond buying [[Huawei]] Ascend or rationed [[NVIDIA]] H200s: hyperscalers with enough token volume can internalize the chip road map. This does not create an immediate NVIDIA substitute, but it means export controls push large Chinese AI platforms toward sovereign, workload-specific silicon.

*Source: [The Information, May 29 2026](https://www.theinformation.com/articles/chinas-bytedance-developing-new-ai-chips-like-nvidia-partner-groq).*

---

## Related

- [[NVIDIA]] — dominant incumbent
- [[NPU]] — technology category for inference chips
- [[Groq]] — acquired by NVIDIA (Dec 2025)
- [[Cerebras]], [[Tenstorrent]], [[SambaNova]] — US alternatives
- [[FuriosaAI]] — Korean alternative (leading independent)
- [[Ascend]] — [[China]] alternative
- [[Huawei]] — China alternative integrating chips, clusters, and software
- [[Tau Scaling Law]] — Huawei post-node design framework
- [[LogicFolding]] — Huawei architecture tied to Kirin and later Ascend
- [[AMD]] — \#2 GPU
- [[CUDA moat]] — why NVIDIA is hard to displace
- [[Inference disaggregation]] — structural trend
- [[Power constraints]] — why efficiency matters
- [[Long inference stack]] — thesis

