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
4. **Prices spike** — significant DRAM price increases through 2025-2026

---

## Current market (Feb 2026)

| Metric | Value | Source |
|--------|-------|--------|
| DDR4 8G spot price | ~$30.76-30.90 | TrendForce Feb 2026 |
| DRAM spot market | "Weak demand, suppliers lowering quotes" | TrendForce |
| [[Micron]] Q1 FY26 revenue | **$13.64B** | YCharts |
| [[Micron]] gross margin | **56.00%** | YCharts |
| [[Micron]] profit margin | **38.41%** | YCharts |
| [[Micron]] 1-year return | **+351.74%** | Yahoo Finance |
| [[Micron]] market cap | **$461.7B** | Yahoo Finance |

**Micron's dominance:** Investing $24B in new Singapore manufacturing facility for memory chips, driven by AI demand. Stock up from $61.54 to $410+ in one year. Gross margin of 56% reflects HBM pricing power.

---

## Who wins

| Player | Position | Market cap |
|--------|----------|------------|
| [[SK Hynix]] | **\#1 HBM** — 50%+ share, pricing power | ~$100B+ |
| [[Samsung]] | **\#2 HBM** — catching up, multi-year hyperscaler deals | ~$300B |
| [[Micron]] | **\#3 HBM** — ramping, exited consumer | **$461.7B** |

All three have locked multi-year HBM supply deals with AI hyperscalers ([[NVIDIA]], Google, [[Microsoft]], etc.), guaranteeing volume at favorable pricing.

---

## Who loses

| Loser | Impact |
|-------|--------|
| **PC OEMs** | [[Dell]], [[HP Inc.]], [[Lenovo]] facing cost spikes |
| **Smartphone makers** | Higher DRAM cost per phone |
| **Consumer upgraders** | DIY PC builders face higher costs |
| **Local AI builders** | Mac Mini, workstation RAM costs rising |

The [[Memory squeeze thesis]] argues consumer-grade hardware window may be closing.

---

## Structural vs cyclical

This appears **structural**, not just a cycle:

| Factor | Implication |
|--------|-------------|
| AI training demand | Only increasing |
| AI inference scaling | Emerging new demand |
| HBM generations | HBM4 even more capacity-intensive |
| Fab investment lag | New capacity takes 2-3 years |

The memory industry has never seen demand this concentrated in high-capacity products.

**Caveat:** TrendForce Feb 2026 notes "weak" spot market demand with suppliers lowering quotes — monitor for cyclical vs structural dynamics.

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
- [[SK Hynix]] — \#1 HBM, 50%+ share
- [[Samsung]] — \#2 HBM, multi-year supply deals
- [[Micron]] — \#3 HBM, exited consumer

### Sectors
- [[Memory]] — parent sector

### Sources
- [TrendForce DRAMeXchange](http://www.dramexchange.com/)
- [Yahoo Finance - MU](https://finance.yahoo.com/quote/MU/)

*Created 2026-01-28 | Updated with Feb 2026 spot prices*
