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

## Related

- [[SK Hynix]] — supplier (#1 HBM)
- [[Samsung]] — supplier (#2 HBM)
- [[Micron]] — supplier (#3 HBM)
- [[Memory shortage 2025-2026]] — context (HBM demand causing shortage)
- [[Advanced packaging]] — requirement (CoWoS for integration)
- [[NVIDIA]] — customer (primary HBM buyer)
