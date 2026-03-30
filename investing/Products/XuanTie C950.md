---
aliases: [C950, Xuantie C950]
tags:
  - product
  - semiconductor
  - cpu
  - risc-v
  - ai-infrastructure
  - china
---

The XuanTie C950 is [[Alibaba]]'s flagship [[RISC-V]] server CPU, announced March 24, 2026 at [[DAMO Academy]]'s RISC-V Ecosystem Conference in Shanghai. It is the first CPU to natively run trillion-parameter language models ([[Qwen|Qwen3]]-235B, [[DeepSeek]] V3-671B) on a RISC-V architecture. Fabricated at 5nm (reportedly by [[TSMC]]), it scores >70 on SPECint2006, a world record for RISC-V single-core performance and 3x its predecessor the C920. In SPECInt 2017 terms, Google researcher Laurie Kirk benchmarked it roughly on par with [[Apple]]'s M1 from 2020 — meaning it is years behind Western state-of-art, but it doesn't need to match them: it needs to run [[Alibaba]]'s own models on an architecture [[China]] controls end-to-end without US [[export controls]] exposure.

---

## Specifications

| Spec | Detail |
|------|--------|
| Architecture | 64-bit multi-core RISC-V, out-of-order superscalar |
| ISA profile | RVA23 (v23.1) compliant |
| Clock | 3.2 GHz |
| Decode | 8-instruction wide |
| Pipeline | 16-stage |
| Out-of-order window | >1,000 instructions |
| Cores per cluster | Up to 8 (via XL-300 interconnect) |
| Process node | 5nm (fab partner undisclosed; reportedly [[TSMC]]) |
| AI acceleration | XuanTie Tensor Processing Engine (TPE), 8 TOPS per TPE |
| Data types | FP16 down to INT4/FP8, plus MXFP8, MXFP4, RVFP4 |
| Vector engine | Co-designed Vector Acceleration Engine |
| Matrix engine | Co-designed Matrix Acceleration Engine (tensor ops for transformer inference) |
| L1 cache latency | 4-cycle load-to-use |
| L2 cache | Private per-core, large capacity |
| Memory modes | Multiple RISC-V virtual memory modes, two-stage address translation |

---

## Performance

| Benchmark | Score | Context |
|-----------|-------|---------|
| SPECint2006 (single-core) | >70 | World record for RISC-V |
| SPECInt 2017 | ~2.6 GHz equivalent | Roughly on par with [[Apple]] M1 (2020) per Google researcher |
| vs C920 predecessor | 3x overall, 4x memory bandwidth | |
| vs mainstream CPUs | >30% gain in cloud networking/storage tasks | [[Alibaba]] claim, specific to customized workloads |

Native support for [[Qwen|Qwen3]]-235B and [[DeepSeek]] V3-671B verified. The claim is that co-designed vector + matrix engines handle transformer inference without external accelerators.

---

## Competitive comparison

| Chip | Architecture | ISA | AI inference | Fab | Export-control exposure |
|------|-------------|-----|-------------|-----|----------------------|
| XuanTie C950 | RISC-V | Open, royalty-free | Native (TPE, 8 TOPS) | 5nm (reportedly [[TSMC]]) | None |
| [[Arm AGI CPU]] | Arm | Licensed, royalty | SVE2 (bfloat16, INT8) | [[TSMC]] 3nm | Subject to US controls |
| [[Intel]] Xeon | x86 | Proprietary | AMX extensions | Intel foundry | Subject to US controls |
| [[AMD]] EPYC | x86 | Proprietary | AVX-512 | [[TSMC]] | Subject to US controls |
| XuanTie C930 | RISC-V | Open | 8 TOPS matrix engine | 5nm | None |

The C950 is not competitive with Western server CPUs on raw performance — Kirk's analysis puts it at M1-era levels, roughly 4-5 years behind current Arm/x86 server chips. The strategic value is the architecture: [[RISC-V]] carries no licensing fees, no [[ARM Holdings|Arm]] royalties, and no US [[export controls]] on the instruction set itself.

---

## Strategic context

[[Alibaba]] CEO Yongming Wu (March 2026): the company's response to the gap with Western chips is "more profound co-design with Alibaba's cloud infrastructure and the [[Qwen]] model to provide improved cost effectiveness." This is vertical integration as moat — the chip doesn't need to win on SPECint, it needs to run Qwen inference cheaply on [[Alibaba]] Cloud.

[[Morningstar]] analyst Chelsey Tam: the chip's significance "lies primarily in improving supply chain resilience amid scarce computing power and lowering overall costs." She doesn't expect a major revenue impact since capacity constraints limit production scale.

The C950 sits within [[Alibaba]]'s three-pillar AI stack:

| Pillar | Component | Role |
|--------|-----------|------|
| Chips | [[Zhenwu 810E]] (GPU-class), XuanTie C950 (CPU), [[Hanguang 800]] (inference) | Compute |
| Cloud | [[Alibaba]] Cloud (#1 [[China]], ~35% share) | Distribution |
| Models | [[Qwen]] (open source, 1B+ downloads) | Intelligence |

---

## Also announced: XuanTie C925

Alongside the C950, [[DAMO Academy]] released the C925, an energy-efficient companion core:

| Metric | C925 vs C930 |
|--------|-------------|
| Energy efficiency | +11% |
| Chip area | -32% |
| Target | Edge computing, balanced performance |

The C925, C930, and C950 form the full flagship RISC-V CPU portfolio: edge (C925) to mid-range (C930) to high-end server (C950).

---

## Market discovery timeline

| Date | Event | Market reaction |
|------|-------|-----------------|
| 2023 | XuanTie C920 and C907 released, automotive and enterprise targets | Modest attention; RISC-V seen as IoT-tier |
| Mar 2025 | XuanTie C930 released — first server-grade RISC-V CPU, RVA23, 8 TOPS matrix engine | RISC-V gains credibility for data center use |
| Mar 2025 | [[China]] 8-agency nationwide RISC-V guidance issued | VeriSilicon +10% limit up; policy signal |
| Jan 30, 2026 | [[Zhenwu 810E]] AI accelerator launched (96GB HBM2e, comparable to [[NVIDIA]] H20) | Completes [[Alibaba]]'s custom silicon stack |
| Mar 24, 2026 | XuanTie C950 unveiled at RISC-V Ecosystem Conference, Shanghai. World record SPECint2006 for RISC-V. Native LLM inference. 5nm. | BABA -0.39% on the day; no material stock reaction — chip expected, performance gap with West acknowledged |

The lack of stock reaction mirrors the Arm AGI CPU pattern (March 24 for Arm too): the market knew [[Alibaba]] was building custom silicon. The C950 confirms capability but doesn't change revenue expectations. The real test is whether [[Alibaba]] Cloud can scale production and whether the vertical integration advantage (co-designed chip + model + cloud) translates into margin improvement.

---

## Related

### Parent
- [[Alibaba]] — parent company, T-Head semiconductor division
- [[DAMO Academy]] — R&D arm that developed the chip

### Architecture
- [[RISC-V]] — open-source ISA, no licensing or export control exposure
- [[Arm Holdings]] — licensed alternative (royalty-based)

### Competitors
- [[Arm AGI CPU]] — Arm's first production server silicon (3nm, 136-core, announced same day)
- [[Intel]] — x86 Xeon server CPUs
- [[AMD]] — x86 EPYC server CPUs

### Sibling products
- [[Zhenwu 810E]] — [[Alibaba]]'s AI accelerator (GPU-class, 96GB HBM2e)
- [[Hanguang 800]] — earlier AI inference chip

### Themes
- [[Export controls]] — strategic motivation for RISC-V investment
- [[US-China tech race]] — broader context
- [[Agentic AI]] — C950 positioned for AI agent inference workloads
- [[Qwen]] — primary model the C950 is co-designed to run

*Created 2026-03-30. Sources: CNBC (Mar 24), The Register (Mar 25), TrendForce (Mar 25), CNX Software (Mar 25), SCMP (Mar 24).*
