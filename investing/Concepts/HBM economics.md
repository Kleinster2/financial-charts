---
aliases: [HBM wafer economics, HBM capacity]
---
#concept #memory #semiconductors

**HBM economics** — High Bandwidth Memory consumes ~4x wafer capacity per GB compared to standard DRAM, creating a structural cost shift as AI accelerators consume global wafer capacity.

---

## The math

| Memory type | Wafer capacity per GB | Relative cost |
|-------------|----------------------|---------------|
| Standard DRAM | 1x (baseline) | Lower |
| [[HBM]] | ~4x | Much higher |

HBM stacks multiple DRAM dies vertically with through-silicon vias (TSVs). Each layer needs its own wafer area, plus the base logic die, plus advanced packaging (CoWoS, etc.).

Result: Same GB of HBM consumes dramatically more fab capacity than standard DRAM.

---

## Supply squeeze dynamics

AI accelerators ([[NVIDIA]] GPUs, Google TPUs, custom ASICs) require massive HBM. As AI demand explodes:

1. **HBM consumes wafer starts** — Samsung, [[SK Hynix]], [[Micron]] shift capacity to HBM
2. **Standard DRAM gets squeezed** — same fabs, competing allocation
3. **Consumer memory starves** — DDR5 for PCs, phones deprioritized
4. **Prices spike** — DRAM prices up **172%** since early 2025

---

## Current market (Jan 2026)

| Metric | Value | Source |
|--------|-------|--------|
| DRAM price increase | **+172%** since early 2025 | Industry data |
| Server memory pricing | Expected to **double** by late 2026 | [[Bank of America]] |
| HBM TAM | $35B (2025) → $100B (2028) | [[Micron]] |
| Consumer DRAM supply | Severely constrained | Multiple OEMs |

---

## Who wins

| Player | Position |
|--------|----------|
| [[SK Hynix]] | **#1 HBM** — 50%+ share, pricing power |
| [[Samsung]] | **#2 HBM** — catching up, multi-year hyperscaler deals |
| [[Micron]] | **#3 HBM** — ramping, exited consumer (Crucial) |

All three have locked multi-year HBM supply deals with AI hyperscalers ([[NVIDIA]], Google, [[Microsoft]], etc.), guaranteeing volume at favorable pricing.

---

## Who loses

| Loser | Impact |
|-------|--------|
| **PC OEMs** | [[Dell]], [[HP Inc.]], [[Lenovo]] facing cost spikes |
| **Smartphone makers** | [[Xiaomi]] +25% DRAM cost per phone |
| **Consumer upgraders** | DIY PC builders priced out |
| **Local AI builders** | Mac Mini, workstation RAM costs rising |

The [[Memory squeeze thesis]] argues consumer-grade hardware window may be closing.

---

## Structural vs cyclical

This is **structural**, not just a cycle:

| Factor | Implication |
|--------|-------------|
| AI training demand | Only increasing |
| AI inference scaling | Emerging new demand |
| HBM generations | HBM4 even more capacity-intensive |
| Fab investment lag | New capacity takes 2-3 years |

The memory industry has never seen demand this concentrated in high-capacity products. Traditional boom/bust cycles may not apply.

---

## For theses

- [[Memory squeeze thesis]] — consumer hardware getting priced out
- [[Long memory]] — structural shortage thesis

---

## Related

### Concepts
- [[Local-first AI]] — needs local memory, affected by squeeze
- [[Agentic AI]] — drives hardware demand
- [[Advanced packaging]] — HBM packaging bottleneck

### Actors
- [[SK Hynix]] — #1 HBM, 50%+ share
- [[Samsung]] — #2 HBM, multi-year supply deals
- [[Micron]] — #3 HBM, exited consumer

### Sectors
- [[Memory]] — parent sector

*Created 2026-01-28*
