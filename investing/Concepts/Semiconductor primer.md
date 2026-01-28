#concept #semiconductors #science #primer

**Semiconductor primer** — foundational physics and manufacturing concepts for semiconductor investing. Understanding the technology helps evaluate node transitions, yield dynamics, and competitive moats.

> **Key insight:** Semiconductors are the most complex manufactured objects in human history. A modern chip has ~100 billion transistors built with atomic precision. This complexity creates massive barriers to entry and winner-take-most dynamics.

---

## What is a semiconductor?

Materials with electrical conductivity between conductors (copper) and insulators (glass). Silicon is the dominant semiconductor — abundant, stable, well-understood.

| Material | Conductivity | Use |
|----------|--------------|-----|
| Conductors | High | Wires |
| **Semiconductors** | Controllable | Chips |
| Insulators | None | Isolation |

**Why silicon wins:** Can be "doped" with impurities to precisely control conductivity. Forms stable oxide (SiO2) for insulation. Abundant (sand).

---

## Transistors — the building block

A transistor is an electrical switch. Apply voltage → current flows. Remove voltage → current stops.

```
        Gate
         |
    +---------+
    |         |
Source     Drain
    |         |
    +---------+
```

| State | Gate voltage | Current |
|-------|--------------|---------|
| Off | Low | Blocked |
| On | High | Flows |

**Digital logic:** Off = 0, On = 1. Combine billions of transistors → computation.

### Transistor evolution

| Generation | Structure | Era |
|------------|-----------|-----|
| Planar | Flat gate on top | Pre-2011 |
| **FinFET** | Fin wraps around gate (3 sides) | 2011-2024 |
| **GAA** | Gate surrounds channel (4 sides) | 2024+ |

**Why evolution matters:** Better gate control = less leakage = lower power = higher density.

[[TSMC]] introduced FinFET at 16nm. [[Samsung]] first to GAA at 3nm. TSMC GAA at 2nm (2025).

---

## Process nodes — what the numbers mean

"5nm" and "3nm" are **marketing names**, not physical measurements.

| Node name | Actual gate pitch | Transistor density |
|-----------|-------------------|-------------------|
| 7nm | ~54nm | ~100M/mm² |
| 5nm | ~48nm | ~170M/mm² |
| 3nm | ~45nm | ~290M/mm² |
| 2nm | ~42nm | ~400M/mm² (est.) |

**What matters:** Density (transistors per mm²), performance (speed), power efficiency.

**Naming chaos:** Intel "7" ≈ TSMC "5". Intel renamed to match marketing reality (Intel 7, Intel 4, Intel 3).

---

## Lithography — printing circuits

Lithography projects circuit patterns onto silicon using light.

| Generation | Light source | Wavelength | Minimum feature |
|------------|--------------|------------|-----------------|
| DUV (ArF) | Argon fluoride laser | 193nm | ~40nm |
| DUV immersion | ArF + water lens | 193nm | ~20nm |
| **EUV** | Tin plasma | 13.5nm | ~8nm |
| High-NA EUV | Larger optics | 13.5nm | ~4nm |

**EUV is the bottleneck:** Only [[ASML]] makes EUV machines. $200M+ each. [[TSMC]] has 100+, [[Intel]] and [[Samsung]] fewer.

### Multi-patterning

Before EUV, chipmakers used multiple DUV exposures to achieve finer features. Complex, expensive, yield-killing. EUV reduces masks from 4+ to 1.

---

## Manufacturing flow

Wafer → hundreds of chips → dicing → packaging

```
1. Wafer fab (front-end)
   - Deposition (add layers)
   - Lithography (pattern)
   - Etch (remove material)
   - Repeat 100+ times

2. Testing
   - Probe each die on wafer

3. Packaging (back-end)
   - Dice wafer into chips
   - Bond to substrate
   - Add connections
   - Encapsulate

4. Final test
```

**Cycle time:** 3-4 months from blank wafer to finished chip.

---

## Yield — the profit lever

**Yield** = % of functional chips per wafer.

| Yield | Impact |
|-------|--------|
| 90%+ | Mature node, high profit |
| 70-90% | Ramping, acceptable |
| <50% | Problem, losing money |

**Why yield matters:** A 300mm wafer costs ~$15,000-20,000 to process. Low yield = high cost per chip.

**Defect density:** Larger chips have lower yield (more area to have defects). This is why GPUs are harder than mobile chips.

See [[Yield as competitive moat]].

---

## Packaging — the new battleground

Traditional: One chip in one package.

Advanced packaging: Multiple chips ("chiplets") in one package, connected with high-bandwidth links.

| Technology | What it does | Leader |
|------------|--------------|--------|
| **CoWoS** | Chip-on-Wafer-on-Substrate, 2.5D | [[TSMC]] |
| **HBM** | High Bandwidth Memory stacking | [[SK Hynix]] |
| **Foveros** | 3D die stacking | [[Intel]] |
| **SoIC** | TSMC 3D integration | [[TSMC]] |

**Why packaging matters now:**
- Moore's Law slowing (harder to shrink)
- Chiplets enable mix-and-match (GPU + HBM + I/O)
- [[NVIDIA]] H100/H200 are packaging-limited, not lithography-limited

See [[Advanced packaging]].

---

## Memory types

| Type | Speed | Persistence | Use |
|------|-------|-------------|-----|
| **SRAM** | Fastest | Volatile | CPU cache |
| **DRAM** | Fast | Volatile | Main memory |
| **NAND** | Slow | Persistent | Storage (SSD) |
| **HBM** | Very fast | Volatile | AI accelerators |

**HBM (High Bandwidth Memory):** DRAM dies stacked vertically, connected with through-silicon vias (TSVs). Essential for AI chips.

See [[HBM]], [[Memory shortage 2025-2026]].

---

## Equipment — who makes the machines

| Equipment type | Leaders | Why it matters |
|----------------|---------|----------------|
| Lithography | [[ASML]] (monopoly) | Defines minimum feature size |
| Deposition | [[Applied Materials]], [[Lam Research]] | Adds material layers |
| Etch | [[Lam Research]], [[Tokyo Electron]] | Removes material |
| Inspection | [[KLA]] | Finds defects |
| Ion implant | Applied Materials | Doping |

**ASML monopoly:** Only company making EUV. 5-year lead. Export-controlled to [[China]].

See [[Semiconductor equipment]].

---

## Foundry model

**IDM (Integrated Device Manufacturer):** Designs and manufactures own chips.
- [[Intel]], [[Samsung]], [[Texas Instruments]]

**Fabless:** Designs chips, outsources manufacturing.
- [[NVIDIA]], [[AMD]], [[Qualcomm]], [[Apple]]

**Foundry:** Manufactures chips for others.
- [[TSMC]] (60% market share), [[Samsung]], [[GlobalFoundries]]

**Why foundry won:** $20B+ per fab. Few can afford it. Fabless companies access cutting-edge without capex.

See [[Foundry monopoly consolidation]].

---

## Node economics

| Node | Fab cost | Design cost | Who can afford |
|------|----------|-------------|----------------|
| 28nm | $3B | $50M | Many |
| 7nm | $10B | $300M | Few |
| 3nm | $20B+ | $500M+ | Hyperscalers, Apple |
| 2nm | $30B+ | $1B+ | Even fewer |

**Consolidation inevitable:** Only TSMC, Samsung, Intel attempting leading-edge. Everyone else stopped at 12nm+.

---

## Key metrics for investors

| Metric | Definition | Why it matters |
|--------|------------|----------------|
| **Wafer starts** | Wafers entering production | Demand indicator |
| **ASP** | Average selling price | Mix, pricing power |
| **Utilization** | Fab capacity used | Margin driver |
| **Capex intensity** | Capex / Revenue | Investment cycle |
| **Yield ramp** | Time to mature yield | New node profitability |

---

## [[China]] constraints

[[Export controls]] limit [[China]]'s semiconductor capability:

| Restricted | Impact |
|------------|--------|
| EUV machines | Cannot make <7nm |
| Advanced DUV | Limited multi-patterning |
| HBM | Memory bottleneck |
| US-designed EDA | Design tool constraints |

[[SMIC]] stuck at ~7nm with DUV multi-patterning. Far behind TSMC.

---

## Related

- [[Semiconductors]] — sector overview
- [[TSMC]] — foundry leader
- [[ASML]] — lithography monopoly
- [[NVIDIA]] — AI chip leader
- [[Foundry monopoly consolidation]] — why winner-take-most
- [[Yield as competitive moat]] — manufacturing advantage
- [[Advanced packaging]] — chiplets, CoWoS, HBM
- [[Export controls]] — [[China]] restrictions
- [[EUV]] — extreme ultraviolet lithography
- [[HBM]] — high bandwidth memory
