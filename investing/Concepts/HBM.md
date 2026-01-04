---
aliases: [High Bandwidth Memory, HBM3, HBM3E, HBM4]
---
#concept #memory #ai

**HBM (High Bandwidth Memory)** — 3D-stacked DRAM enabling massive bandwidth for AI accelerators. The memory bottleneck solution for GPUs.

---

## Why it matters

AI training/inference is memory-bound:
- GPUs need to feed data faster than traditional DRAM allows
- HBM stacks DRAM dies vertically with through-silicon vias (TSVs)
- Enables 10x+ bandwidth vs standard DDR

---

## Generations

| Gen | Bandwidth | Capacity | Status |
|-----|-----------|----------|--------|
| HBM2e | ~460 GB/s | 16GB/stack | Legacy |
| HBM3 | ~820 GB/s | 24GB/stack | Current |
| HBM3E | ~1.15 TB/s | 36GB/stack | Ramping 2024-25 |
| HBM4 | ~1.5+ TB/s | 48GB+/stack | 2026+ |

---

## Supply chain

Only 3 suppliers:
- [[SK Hynix]] — Market leader, [[NVIDIA]]'s primary supplier
- [[Samsung]] — #2, catching up
- [[Micron]] — Distant #3, ramping HBM3E

---

## Key dynamics

- [[Memory shortage 2025-2026]] driven partly by HBM demand
- HBM is 5x+ ASP vs commodity DRAM — margin accretive
- Yield is challenging — vertical stacking compounds defect rates
- [[Advanced packaging]] required (CoWoS at [[TSMC]])

---

## Who benefits

- Memory makers: [[SK Hynix]], [[Samsung]], [[Micron]]
- [[TSMC]]: CoWoS packaging for HBM integration
- Equipment: [[ASE]], testers, advanced packaging tools
- End demand: [[NVIDIA]], [[AMD]], [[Broadcom]] custom silicon

---

## China HBM gap

China's AI clusters are stuck on HBM2E while NVIDIA uses HBM3E — a structural disadvantage.

> **Key insight:** HBM is the chokepoint that makes [[Export controls]] effective. GPUs can be designed domestically (Ascend, Kunlun). HBM cannot — the oligopoly (SK Hynix, Samsung, Micron) is aligned with US policy. No workaround exists.

### The gap

| Metric | HBM2E (China) | HBM3E (NVIDIA) | Gap |
|--------|---------------|----------------|-----|
| Bandwidth | 460 GB/s | 1.15 TB/s | 2.5x |
| Capacity/stack | 16 GB | 36 GB | 2.25x |
| Generation | 2022 | 2024 | 2 years |

### Why China can't close it

| Supplier | Status |
|----------|--------|
| [[SK Hynix]] | Won't supply (US pressure, export controls) |
| [[Samsung]] | Won't supply (aligned with US) |
| [[Micron]] | Won't supply (US company) |
| Domestic (CXMT) | Years behind, no HBM production |

**The bottleneck:** HBM is an oligopoly. All three suppliers aligned with US export policy. No domestic source.

### Why it matters for AI

| Workload | Bottleneck | HBM impact |
|----------|------------|------------|
| **Training** | Compute + memory | Partially offset by more chips |
| **Inference (prefill)** | Compute | Less affected |
| **Inference (decode)** | Memory bandwidth | Directly limited by HBM gap |

**The problem:** Decode phase (token generation) is memory-bound. See [[Inference disaggregation]]. More chips can't fix per-chip bandwidth limits.

### Strategic implications

- [[China AI clusters]] can match training FLOPS through brute force
- Inference speed/quality is structurally disadvantaged
- [[Export controls]] are effective because HBM is chokepoint
- No near-term workaround — domestic HBM is years away

---

*Updated 2026-01-03*

---

## Related

- [[SK Hynix]] — supplier (#1 HBM, won't supply China)
- [[Samsung]] — supplier (#2 HBM, aligned with US)
- [[Micron]] — supplier (#3 HBM, US company)
- [[Memory shortage 2025-2026]] — context (HBM demand causing shortage)
- [[Advanced packaging]] — requirement (CoWoS for integration)
- [[NVIDIA]] — customer (primary HBM buyer)
- [[China AI clusters]] — affected (stuck on HBM2E)
- [[Export controls]] — mechanism (HBM as chokepoint)
- [[Inference disaggregation]] — context (decode is memory-bound)
- [[Long memory]] — thesis (HBM oligopoly = pricing power)
