#concept #networking #infrastructure #science #primer

**Optical networking primer** — foundational physics and technology concepts for networking and AI infrastructure investing. Understanding optics helps evaluate transceiver demand, data center interconnects, and bandwidth bottlenecks.

> **Key insight:** Light moves data faster and more efficiently than electrons. As AI drives exponential bandwidth growth, optical networking becomes the critical path. Every AI training cluster is an optics story.

---

## Why optics?

| Property | [[Copper]] | Fiber |
|----------|--------|-------|
| Bandwidth | Limited | Nearly unlimited |
| Distance | ~100m (high speed) | 100+ km |
| Latency | Higher | **Speed of light** |
| Power | Higher | Lower per bit |
| EMI susceptibility | Yes | **No** |
| Cost (short) | Lower | Higher |
| Cost (long) | Higher | **Lower** |

**Crossover:** Beyond ~100m, fiber wins on everything. Inside racks, copper still dominates for cost.

---

## How fiber optics works

Light travels through glass fiber via total internal reflection.

```
Transmitter (laser) → Fiber (glass) → Receiver (photodetector)
         ↓                  ↓                    ↓
    Converts            Carries              Converts
   electrical          light                light back
    to light          signal               to electrical
```

| Component | Function |
|-----------|----------|
| **Laser/LED** | Converts electrical → optical |
| **Fiber** | Glass waveguide (carries light) |
| **Photodetector** | Converts optical → electrical |
| **Transceiver** | Contains both laser + detector |

---

## Fiber types

### Single-mode fiber (SMF)

| Property | Value |
|----------|-------|
| Core diameter | 9 µm |
| Light path | Single ray |
| Distance | Up to 100+ km |
| Use | Long-haul, metro, data center interconnect |

**Advantage:** No modal dispersion → high bandwidth over distance.

### Multi-mode fiber (MMF)

| Property | Value |
|----------|-------|
| Core diameter | 50 or 62.5 µm |
| Light path | Multiple rays |
| Distance | <500m |
| Use | Short-reach, within data centers |

**Advantage:** Cheaper components (VCSELs vs edge-emitting lasers). Easier alignment.

---

## Wavelength Division Multiplexing (WDM)

Send multiple signals on different wavelengths (colors) through one fiber.

```
λ1 (1530nm) ──┐
λ2 (1531nm) ──┼──→ [Multiplexer] ──→ Single Fiber ──→ [Demux] ──→ λ1, λ2, λ3...
λ3 (1532nm) ──┘
```

| Type | Channel spacing | Channels | Use |
|------|-----------------|----------|-----|
| CWDM (Coarse) | 20nm | 8-16 | Metro, enterprise |
| DWDM (Dense) | 0.8nm or less | 40-160+ | Long-haul, hyperscale |

**DWDM enables:** 400+ channels × 400Gbps each = 160+ Tbps per fiber pair.

---

## [[Coherent]] optics

Advanced modulation using phase and amplitude of light.

| Property | Direct detect | [[Coherent]] |
|----------|---------------|----------|
| Modulation | On/off | Phase + amplitude |
| Bits per symbol | 1 | 4-6+ (QAM) |
| Distance | Shorter | Longer |
| Cost | Lower | Higher |
| Speeds | Up to 100G | 400G-1.6T |

**How coherent works:**
- Encodes data in phase + amplitude (like radio QAM)
- Local oscillator laser at receiver
- Digital signal processing (DSP) corrects impairments

**Why coherent matters:** Enables 400G/800G/1.6T speeds over long distances. Essential for AI backbone networks.

---

## Transceiver form factors

| Form factor | Size | Power | Speed | Use |
|-------------|------|-------|-------|-----|
| SFP | Small | <1W | 1-25G | Enterprise |
| SFP-DD | 2x SFP | <4W | 100G | Data center |
| QSFP | Quad SFP | <5W | 40-100G | Common DC |
| QSFP-DD | Dual density | <15W | 400G | High bandwidth |
| QSFP-DD800 | Enhanced | <20W | 800G | AI clusters |
| OSFP | Larger | <25W | 400G-800G | High power |

**Trend:** Higher speeds require more power → thermal challenges → new form factors.

---

## Data center interconnect tiers

| Tier | Distance | Technology |
|------|----------|------------|
| **Intra-rack** | <3m | [[Copper]] DAC, AOC |
| **Intra-DC** | 100m-2km | MMF, SMF |
| **Campus/DCI** | 2-80km | SMF, coherent |
| **Metro** | 80-300km | DWDM coherent |
| **Long-haul** | 300+ km | DWDM coherent + amplifiers |
| **Subsea** | Trans-ocean | DWDM, repeatered |

---

## AI cluster networking

AI training requires massive bandwidth between GPUs/TPUs.

### Scale-up (within server/rack)

| Technology | Bandwidth | Distance |
|------------|-----------|----------|
| NVLink | 900 GB/s (H100) | Within node |
| NVSwitch | 3.6 TB/s switching | Within rack |
| [[Copper]] DAC | 400G per lane | <3m |

### Scale-out (between racks)

| Technology | Bandwidth | Distance |
|------------|-----------|----------|
| InfiniBand | 400G-800G | DC-wide |
| Ethernet (RoCE) | 400G-800G | DC-wide |
| Optical | Required beyond ~3m | — |

**NVIDIA's network:** Spectrum-X (Ethernet), InfiniBand (legacy). Both need optical transceivers for inter-rack.

---

## Key components and suppliers

### Transceivers

| Company | Strength |
|---------|----------|
| **[[Coherent Corp]]** | [[Coherent]] DSP, 800G/1.6T |
| **[[Lumentum]]** | Lasers, coherent |
| **II-VI** (now [[Coherent]]) | Vertically integrated |
| **[[Cisco]]** | Enterprise, some DC |
| **[[Intel]]** (Silicon Photonics) | Integration play |

### Optical components

| Component | Leaders |
|-----------|---------|
| Lasers (DFB, EML) | Lumentum, II-VI/[[Coherent]] |
| VCSELs | Lumentum, II-VI |
| Modulators | [[Coherent]] |
| Photodetectors | Multiple |
| DSP chips | Marvell, Broadcom, [[Coherent]] |

### Fiber

| Company | Position |
|---------|----------|
| **Corning** | Dominant in fiber |
| **Prysmian** | Cables |
| **OFS (Furukawa)** | Specialty fiber |

---

## Silicon photonics

Integrate optical components on silicon chips (like semiconductors).

| Advantage | Challenge |
|-----------|-----------|
| Lower cost at scale | Laser still external (III-V) |
| Integration with electronics | Coupling efficiency |
| Smaller form factor | Thermal management |

**Players:** [[Intel]] (Altera), [[Cisco]], Marvell, [[Broadcom]].

**Trend:** Co-packaged optics — transceivers integrated into switch ASICs. Reduces power, latency.

---

## Co-packaged optics (CPO)

Traditional: [[Switch]] ASIC → electrical traces → pluggable transceiver → fiber

CPO: [[Switch]] ASIC + optics on same package → fiber

| Property | Pluggable | CPO |
|----------|-----------|-----|
| Power | Higher | **30-50% lower** |
| Latency | Higher | Lower |
| Serviceability | Easy swap | Harder |
| Flexibility | High | Lower |

**Status:** Early deployment. [[Broadcom]] Tomahawk 5 supports CPO. Hyperscalers testing.

---

## Linear-drive optics (LPO)

Remove DSP retiming from transceiver. Let host handle it.

| Property | Traditional | LPO |
|----------|-------------|-----|
| DSP in transceiver | Yes | **No** |
| Power | Higher | **30% lower** |
| Latency | Higher | Lower |
| Cost | Higher | Lower |
| Distance | Longer | Shorter |

**Use case:** Within data center (<500m) where link conditions are controlled.

---

## AI infrastructure demand drivers

| Driver | Impact on optics |
|--------|------------------|
| GPU cluster scale | More transceivers per cluster |
| Training bandwidth | 400G → 800G → 1.6T |
| Inference at edge | More distributed connections |
| Hyperscaler capex | Direct transceiver orders |

**Numbers:** A 10,000 GPU cluster needs ~25,000+ optical transceivers. Hyperscalers deploying 100,000+ GPU clusters.

---

## Speed roadmap

| Year | Data center standard | Long-haul |
|------|---------------------|-----------|
| 2020 | 100G | 400G |
| 2023 | 400G | 800G |
| 2025 | 800G | 1.2T |
| 2027E | 1.6T | 1.6T+ |

**Doubling every 2-3 years.** Each generation = new transceivers, new DSPs, component upgrades.

---

## Key metrics for investors

| Metric | Definition | Why it matters |
|--------|------------|----------------|
| **Port shipments** | Transceivers sold | Volume, market share |
| **ASP** | Average selling price | Mix, pricing power |
| **Speed mix** | % of 400G/800G+ | Technology position |
| **Gross margin** | Profitability | Scale, competition |
| **Design wins** | Hyperscaler adoption | Future revenue |

---

## Investment considerations

**Bulls say:**
- AI driving exponential bandwidth growth
- Speed transitions create upgrade cycles
- Hyperscaler capex = direct demand
- High barriers (coherent DSP, lasers)

**Bears say:**
- Commoditization at lower speeds
- [[China]] competition in components
- CPO may disrupt pluggables
- Customer concentration (hyperscalers)

---

## Related

- [[AI Infrastructure]] — demand context
- [[Data Centers]] — physical layer
- [[Coherent Corp]] — optical leader
- [[Lumentum]] — laser company
- [[Broadcom]] — networking ASICs + DSP
- [[Marvell]] — DSP, custom silicon
- [[NVIDIA]] — networking (Spectrum-X)
- [[Corning]] — fiber manufacturer
- [[Hyperscaler capex]] — demand driver
- [[Semiconductor primer]] — chip context
