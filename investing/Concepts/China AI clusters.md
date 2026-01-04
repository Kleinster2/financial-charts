#concept #china #ai #infrastructure

# China AI Clusters

Chinese hyperscalers building massive AI clusters using domestic and restricted-export chips. Compensating for per-chip disadvantage with scale.

---

## The configurations

| Company | Cluster | Scale | Chip | Performance |
|---------|---------|-------|------|-------------|
| **[[Huawei]]** | CloudMatrix 384 | 384 chips | Ascend 910C | 300 PFLOPS BF16 |
| **[[Huawei]]** | SuperPoD | 15,000+ chips | Ascend | Scaling |
| **[[Huawei]]** | Atlas 960 | 15,488 chips | Ascend | 2027 |
| **[[Baidu]]** | Kunlun cluster | 30,000 chips | Kunlun P800 | 345 TFLOPS/chip FP16 |
| **[[Alibaba]]** | Hanguang 800 | Deployed | Custom | Inference-focused |
| **[[Alibaba]]** | PPU cluster | Building | Custom training | 7nm, 2.5D chiplet |

---

## Huawei CloudMatrix / SuperPoD

See [[Huawei]] for full details.

| Spec | CloudMatrix 384 | NVIDIA GB200 NVL72 |
|------|-----------------|-------------------|
| Chips | 384 Ascend 910C | 72 Blackwell |
| Performance | 300 PFLOPS BF16 | ~180 PFLOPS |
| Power | 4.1x higher | Baseline |
| Power/FLOP | 2.5x worse | Baseline |

**Interconnect:** All-to-all optical, 5.5 Pbps internal bandwidth.

**Roadmap:**
- SuperPoD (2025): 15,000 chips
- Atlas 950 (2026): 8,000+ chips, 1 PFLOPS FP8, 128-144 GB memory
- Atlas 960 (2027): 15,488 chips, 2x performance of 950
- Ascend 970: Further out

---

## Baidu Kunlun P800 cluster

First Chinese company operating domestic AI accelerators at hyperscale for LLM training.

| Spec | Value |
|------|-------|
| Scale | 30,000 Kunlun P800 chips |
| Per-chip | 345 TFLOPS FP16 |
| Comparison | ~A100 / Ascend 910B level |
| Use case | Training "DeepSeek-like" models (100B+ params) |

**Models trained:**
- Qianfan-VL (3B, 8B, 70B parameters)
- Ernie improvements

See [[Kunlunxin]] for chip details.

---

## Alibaba configurations

**Hanguang 800 (inference):**
- Deployed since 2019
- E-commerce search and recommendation
- Inference-optimized

**PPU (training chip):**
- Revealed but not fully deployed
- Domestic 7nm process
- 2.5D chiplet packaging
- Will shift core AI training to domestic silicon

**Investment:** 380B yuan ($52B) over 3 years, AI-focused.

---

## Tencent approach

**Different strategy — no custom chips:**
- "Open compatibility, diverse computing power"
- Tencent Cloud adapts to mainstream domestic chips
- Works with Huawei Ascend, others
- $15B AI investment (2023-2026)

**Rationale:** Avoid chip development risk, leverage ecosystem.

---

## ByteDance approach

**Stockpile + adapt:**
- $14B NVIDIA H200 order (before restrictions)
- Rushed to stockpile ~1.3-1.6M H20 chips ($16B with Alibaba, Tencent)
- Experimenting with Huawei Ascend for training
- No custom chip program

See [[ByteDance]] for details.

---

## Chip comparison

| Chip | Company | Performance | Memory | vs NVIDIA |
|------|---------|-------------|--------|-----------|
| Ascend 910C | Huawei | ~80% H20 bandwidth | HBM2E | Closest domestic |
| Ascend 910B | Huawei | ~A100 level | HBM2E | 2/3 capacity, 40% bandwidth vs H20 |
| Kunlun P800 | Baidu | 345 TFLOPS FP16 | — | ~A100 level |
| Hanguang 800 | Alibaba | Inference-focused | — | Specialized |

**The gap:** Domestic chips use older HBM2E vs NVIDIA's HBM3. Memory bandwidth is the bottleneck.

---

## The HBM gap

China's AI clusters face a structural memory disadvantage that brute force can't fully solve.

### Why HBM3 matters

| Metric | HBM2E | HBM3 | HBM3E |
|--------|-------|------|-------|
| Bandwidth | 460 GB/s | 819 GB/s | 1.15 TB/s |
| Capacity/stack | 16 GB | 24 GB | 36 GB |
| Generations behind | Current China | NVIDIA H100 | NVIDIA H200/Blackwell |

**For inference:** Memory bandwidth determines tokens/second. HBM3E is 2.5x faster than HBM2E.

**For training:** Larger models need more memory. HBM3E offers 2x+ capacity per stack.

### Why China can't get HBM3

| Supplier | Status |
|----------|--------|
| [[SK Hynix]] | Won't supply China (US pressure, export controls) |
| [[Samsung]] | Won't supply China (same) |
| [[Micron]] | Won't supply China (US company) |
| Domestic (CXMT, etc.) | Years behind, no HBM production |

**The bottleneck:** HBM is an oligopoly. All three suppliers are aligned with US export policy. China has no domestic HBM source.

### How this limits brute force

| Strategy | Works for | Fails for |
|----------|-----------|-----------|
| More chips | Aggregate FLOPS | Memory-bound workloads |
| More power | Running more chips | Doesn't fix bandwidth |
| Better interconnect | Chip-to-chip | Chip-to-memory |

**The problem:** Inference is increasingly memory-bound (see [[Inference disaggregation]]). Decode phase needs memory bandwidth, not compute. More Ascend chips can't fix the HBM2E ceiling.

### Partial workarounds

| Approach | Benefit | Limit |
|----------|---------|-------|
| SRAM for decode | Faster than HBM | Tiny capacity, expensive |
| Model compression | Fits in less memory | Quality trade-off |
| Smaller models | Lower memory needs | Capability trade-off |
| Batch optimization | Better utilization | Latency penalty |

**Net effect:** China can match US on training FLOPS through scale, but inference quality/speed is structurally disadvantaged by HBM gap.

---

## Huawei Ascend roadmap

| Chip | Timeline | Performance | Memory |
|------|----------|-------------|--------|
| Ascend 910C | Shipping | Current best | HBM2E |
| Ascend 920 | Development | Target H100 | — |
| Ascend 950 | 2026 | 1 PFLOPS FP8 | 128-144 GB |
| Ascend 960 | 2027 | 2x 950 | — |
| Ascend 970 | Future | — | — |

---

## Total China AI investment

| Source | 2025 Investment |
|--------|-----------------|
| Government (Big Fund, etc.) | $56B |
| Internet companies | $24B |
| **Total** | ~$98B |

Major contributors: Alibaba, Tencent, ByteDance, Baidu, Huawei.

---

## The strategy

**Brute force compensation:**
1. More chips (scale > efficiency)
2. More power ([[China power advantage]])
3. Domestic interconnects (CloudMatrix, SuperPoD)
4. Stockpile restricted NVIDIA chips while available

**Trade-off:** Works for deployment and inference at scale. Less effective for frontier research where per-chip performance matters.

---

*Updated 2026-01-03*

---

## Related

- [[Huawei]] — CloudMatrix, SuperPoD, Ascend chips
- [[Kunlunxin]] — Baidu's chip spin-off
- [[Baidu]] — 30K Kunlun cluster
- [[Alibaba]] — Hanguang, PPU
- [[ByteDance]] — Stockpile strategy
- [[Tencent]] — Multi-vendor approach
- [[China power advantage]] — Enables brute force strategy
- [[Export controls]] — Why domestic chips matter
