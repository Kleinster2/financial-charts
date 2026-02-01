#concept #semiconductors #memory #ai

**GPU memory scaling** — Each AI GPU generation requires exponentially more memory capacity and bandwidth. This structural trend drives demand for [[HBM]] and benefits memory makers ([[SK Hynix]], [[Samsung]], [[Micron]]).

---

## The trend

![[gpu-memory-scaling.png]]
*V100 (32GB) → A100 (80GB) → H100 (80GB) → H200 (141GB) → B200 (192GB) → Rubin (288GB est.)*

| GPU | Year | Memory | Bandwidth | vs V100 |
|-----|------|--------|-----------|---------|
| V100 | 2017 | 32 GB | 900 GB/s | 1x |
| A100 | 2020 | 80 GB | 2 TB/s | 2.5x / 2.2x |
| H100 | 2022 | 80 GB | 3.35 TB/s | 2.5x / 3.7x |
| H200 | 2024 | 141 GB | 4.8 TB/s | 4.4x / 5.3x |
| B200 | 2025 | 192 GB | 8 TB/s | **6x / 8.9x** |

**8 years: 6x memory capacity, 9x bandwidth.**

This isn't slowing down. Rubin (2026-27) will require HBM4 with even higher capacity per stack.

---

## Why it's happening

| Driver | Detail |
|--------|--------|
| **Model size** | GPT-4 ~1.8T params vs GPT-3 175B (10x in 3 years) |
| **Context windows** | 4K → 128K → 1M+ tokens |
| **Batch sizes** | Larger batches = more memory for activations |
| **Inference KV cache** | Long contexts require massive KV cache storage |
| **Multi-modal** | Images, video, audio = more data per forward pass |

**The math:** A 1T parameter model in FP16 needs ~2TB just to store weights. Add activations, gradients, optimizer states — memory requirements explode.

---

## Why it matters for investors

### Memory is no longer cyclical

Traditional view: Memory is commoditized, cyclical, boom-bust.

New reality: AI GPUs create **structural demand growth** that overrides the cycle.

| Old cycle driver | New driver |
|------------------|------------|
| PC/smartphone refresh | AI training clusters (hyperscaler capex) |
| Price-sensitive consumers | Performance-sensitive enterprises |
| Commodity DDR4/DDR5 | Premium HBM (5x+ ASP) |

**The insight from the [[SK Hynix]] chart:** They lost $9B in 2023 (memory downturn), made $20B+ in 2025 (HBM boom). Same company, same fabs — but GPU memory scaling changed the game.

### Who benefits

| Beneficiary | Why |
|-------------|-----|
| [[SK Hynix]] | #1 HBM supplier, NVIDIA's primary partner |
| [[Samsung]] | #2 HBM, catching up |
| [[Micron]] | #3 HBM, ramping |
| [[TSMC]] | CoWoS packaging for HBM integration |
| [[Hanmi Semiconductor]] | HBM bonding equipment |

### Who's squeezed

| Loser | Why |
|-------|-----|
| [[China]] AI | Can't access advanced HBM (export controls) |
| Budget AI deployments | Memory cost dominates TCO |
| Commodity DRAM | Capex diverted to HBM |

---

## The numbers

**HBM content per GPU:**

| GPU | HBM stacks | GB per stack | Total |
|-----|------------|--------------|-------|
| H100 | 6 | ~16 GB | 80 GB |
| H200 | 6 | ~24 GB | 141 GB |
| B200 | 8 | 24 GB | 192 GB |
| Rubin (est.) | 8 | 36+ GB | 288+ GB |

Each generation needs more stacks AND more capacity per stack.

**Dollar content per GPU:**

HBM is ~5x ASP vs commodity DRAM. A B200 with 192GB HBM3e has **$2,000-3,000+ of memory content** — a significant portion of the GPU BOM.

---

## Investment implication

The [[Long memory]] thesis is built on this trend:

> "Memory looks cyclical until you realize every NVIDIA GPU generation doubles HBM content. It's not a cycle — it's a secular growth driver wearing cyclical clothes."

The 2023 memory downturn was real. The 2025-26 HBM boom is structural. GPU memory scaling is why.

---

## Related

- [[HBM]] — the product enabling this scaling
- [[Memory shortage 2025-2026]] — current manifestation
- [[SK Hynix]] — primary beneficiary
- [[Samsung]] — #2 HBM supplier
- [[Micron]] — #3 HBM supplier
- [[NVIDIA]] — demand driver
- [[Long memory]] — investment thesis
- [[Advanced packaging]] — required for HBM integration

---

*Sources: [BentoML](https://www.bentoml.com/blog/nvidia-data-center-gpus-explained-a100-h200-b200-and-beyond), [Exxact](https://www.exxactcorp.com/blog/hpc/comparing-nvidia-tensor-core-gpus), [BIZON](https://bizon-tech.com/blog/nvidia-b200-b100-h200-h100-a100-comparison)*

*Created 2026-01-31*
