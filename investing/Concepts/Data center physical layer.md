---
aliases: [DC physical plant, Data center operations, Data center construction]
---
#concept #datacenter #infrastructure #ai #bottleneck

**Data center physical layer** — The concrete, steel, power, and cooling systems that constitute the actual "cloud." Industrial real estate with a severe physics problem: $600-650B in 2026 hyperscaler capex chasing equipment with 2-4 year lead times, cooling systems being redesigned in real time, and a grid built for a world that no longer exists.

Source: [TSCS "The Datacenter Bible"](https://tscsw.substack.com/p/the-datacenter-bible-from-layman) (Dec 2025, updated Feb 2026)

---

## Core thesis

There is no cloud. There is only a concrete building connected to a power grid, cooled by systems being redesigned in real time, and supplied by an equipment industry that cannot build fast enough. This is not a technology sector — it is industrial real estate with a thermodynamics problem.

---

## 2026 capex explosion

| Hyperscaler | 2025 actual | 2026 guided | vs Street consensus |
|-------------|-------------|-------------|---------------------|
| [[Alphabet]] / Google | $91.4B | $175-185B | +51% above Street |
| [[Amazon]] | $131.8B | ~$200B | Street est $146.6B |
| [[Meta Platforms]] | $72.2B | $115-135B | ~2x 2025 |
| [[Microsoft]] | — | $116-145B (est) | Varies by analyst |
| **Big Five total** | — | **$600-650B** | 36-62% above 2025 |

[[Goldman Sachs]] cumulative 2025-2027 capex projection: ~$1.4T (revised up from $1.15T). More than double the $477B spent 2022-2024. Capital intensity reaches 45-57% of revenue for some hyperscalers.

---

## Construction economics

### Material intensity
- Single hyperscale AI DC: up to **20,000 tons of steel** (~two Eiffel Towers)
- US cement demand for AI DCs by 2028: **1 million metric tons** (American Cement Association)
- Cement production = ~8% of global CO₂ emissions

### Land
- US weighted average: $244K/acre (Oct 2024, Cushman & Wakefield)
- [[Northern Virginia]] (Loudoun County): **$2-4M+/acre**
- Prince William County: ~$1M/acre
- Phoenix: $200-500K/acre
- Average parcel size: **224 acres** (144% increase since 2022) — hyperscalers buying entire zip codes

### The unit of measurement
The fundamental unit is the **megawatt (MW)**, not square footage. "I'm building a 100MW campus" is the standard. If you talk about square footage, you're revealing yourself as an amateur.

---

## Equipment lead times (the binding constraint)

Every project timeline in 2026 is dictated by transformer and generator procurement, full stop.

| Equipment | Lead time | Source |
|-----------|-----------|--------|
| Diesel generator (2MW) | 72-104 weeks | Stream Data Centers |
| Power transformer | 128 weeks | WoodMac Q2 2025 |
| Generator step-up transformer | 144 weeks (~3 years) | WoodMac |
| Large power transformer | up to 210 weeks | — |
| Switchgear | 44-48 weeks | WoodMac / Cushman & Wakefield |
| HV circuit breaker | 150+ weeks | — |
| Grid connection (primary markets) | **4-7+ years** | — |

WoodMac models a **30% shortfall** for power transformers across the US fleet. More than half of the nation's ~40M distribution transformers already beyond expected service life.

57% of DC projects faced delays of 3+ months in 2025 (JLL). Developers preordering critical equipment 24 months before breaking ground.

**Implication:** If you didn't order your switchgear two years ago, you aren't building a data center today. Massive barrier to entry favoring incumbents.

---

## Vacancy and pricing

| Metric | Value | Source |
|--------|-------|--------|
| Primary market vacancy | 1.6% (H1 2025) | CBRE |
| Northern Virginia colocation vacancy | **0.72%** | CBRE H1 2025 |
| Global occupancy | 97% | JLL |
| Under construction preleased | 74.3% | — |
| Colocation pricing | >$200/kW/month | JLL |
| Projected vacancy through 2027 | <5%, ~2% | JLL |

---

## Power redundancy architecture

### N-rating system

| Rating | Design | Use case | Cost |
|--------|--------|----------|------|
| **N** | Bare minimum capacity | Crypto miners, amateurs | Cheapest |
| **N+1** | One spare unit per system | Industry standard, most cloud | Moderate |
| **2N** | Two completely independent power paths | Banks, HFT, military | ~2x hardware |

The cloud has actually **lowered** the average physical tier. [[AWS]] builds cheap N+1 "availability zones" and relies on software redundancy. Works great until a software bug takes down us-east-1.

### Uptime Institute tiers

| Tier | Redundancy | Availability | Example |
|------|-----------|--------------|---------|
| I | N | 99.671% | Server closet |
| III | N+1 | 99.982% | Standard colocation |
| IV | 2N+1 | 99.995% | Banks, military |

Downtime cost for a large org: **$9,000/minute** ($540K/hour). For HFT firms, a minute of downtime is an extinction event.

---

## Thermodynamics

### The air cooling wall

Computers are heaters that do a little math on the side. Nearly all electricity input converts to heat.

| Era | Rack density | Cooling method |
|-----|-------------|----------------|
| Legacy | 5-10 kW | Air (cold aisle/hot aisle) |
| Pre-AI | 15-20 kW | Air (stressed) |
| AI training | 40-120 kW | **Liquid required** |

**[[Thermal limits]]:** Air's specific heat capacity is garbage compared to water. You cannot cool a 100kW rack with air — you'd need hurricane-force wind, with fans consuming 20% of power.

At legacy 15 kW densities, thermal runaway (72°F → 90°F+) begins in **75 seconds** if cooling fails. At 120kW [[Blackwell]] densities, the window is far shorter.

### Liquid cooling transition

Water conducts heat **23.5x better** than air. **3,500x** the heat-carrying capacity by volume.

Two approaches:
- **Direct-to-chip (DTC):** Liquid piped directly to the processor
- **Immersion cooling:** Server submerged in dielectric fluid

Liquid cooling market doubled to **$3B** in 2025. [[Goldman Sachs]] forecasts 76% of AI servers liquid-cooled by end of 2026.

**Retrofit nightmare:** You can't shove a liquid-cooled rack into an old air-cooled DC. Need plumbing, Coolant Distribution Units (CDUs), leak protection. Water and electricity famously don't mix.

**Stranded assets:** Portfolios of 10-year-old DCs designed for 5kW racks = Blockbuster in the Netflix era.

### PUE (Power Usage Effectiveness)

PUE = Total facility power / IT equipment power. Industry average ~1.58, best-in-class <1.2.

**The scam:** PUE doesn't measure water. Evaporative cooling gets great PUE while draining millions of gallons from local aquifers. Arbitraging the electric grid against the water table. Look "green" on energy (low PUE) while drying the river (high WUE).

---

## Power availability crisis

Global DC electricity demand projected to **double to ~945 TWh by 2030** (IEA Feb 2025). [[Goldman Sachs]] forecasts 175% growth by 2030.

### Virginia regulatory shift (Feb 2026 update)
- New GS-5 rate class (Jan 1, 2027): customers >25MW must sign **14-year contracts** with minimum demand charges regardless of usage
- [[Dominion Energy]] authorized rate increases: $775.6M across 2026-2027
- HB155: SCC review required before grid connection for high-power facilities
- 230+ organizations calling for a **national moratorium** on DC construction

### PJM capacity crisis
- 2026/2027 auction cleared at FERC cap of **$329.17/MW-day**
- Data centers driving **40% of capacity costs**
- NRDC estimates PJM consumers could pay **$163B extra** through 2033
- Long-term growth forecast: 3.6% annually (up from 3.1%), projecting 222 GW by 2036

Geography is now dictated by electrons, not fiber. Developers moving to tertiary markets (Columbus, Hillsboro, Iowa cornfields) — wherever utilities will sell 500MW.

---

## Facility design

### Raised floor vs slab-on-grade

| Factor | Raised floor | Slab-on-grade |
|--------|-------------|---------------|
| Cooling | Underfloor plenum | Overhead ducts / in-row |
| Flexibility | High (lift tiles, reconfigure) | Lower |
| Seismic risk | High (inverted pendulum) | Low (anchored to slab) |
| Load capacity | Limited | Superior |
| Cleaning | Hidden plenum accumulates debris | Simpler |
| Favored by | Colocation (tenant flexibility) | Hyperscalers (fixed deployments) |

**Venturi effect risk:** In raised-floor plenums, high air velocity near CRAC units creates low-pressure zones that *suck warm air down* into the cold supply — starving servers of cooling despite CRAC units at full power.

### Structural loading
- Standard cabinet: ~3,000 lbs on 8.8 sq ft = **340 PSF** point load
- Office building rating: 50-100 PSF (woefully insufficient)
- [[Digital Realty]] portfolio average: 178 PSF
- High-density facility (NJR3 Clifton): **400 PSF**

---

## Nuclear for data centers

Big tech nuclear commitments now exceed **10 GW**, but the [[HALEU]] fuel supply stands at ~1 metric ton produced via enrichment against a need for **40 tons** by end of decade. DOE planning to supplement through HEU downblending from defense stockpiles.

---

## UPS architecture (double conversion)

The industry gold standard for critical loads: Online Double-Conversion UPS.

1. **Rectifier** (AC→DC): converts raw grid power, performs power factor correction
2. **Battery bank:** charges from DC bus, provides instant bridge during failure
3. **Inverter** (DC→AC): regenerates clean sine-wave power, isolated from grid noise
4. **Static bypass:** failsafe path if UPS itself fails

The IT load never touches raw utility power — complete electrical isolation.

---

## Latency and speed of light

Fiber optic refractive index: ~1.47 → light travels **31% slower** in glass vs vacuum.
Air refractive index: ~1.0003 → microwaves travel at **99%** of *c*.

**HFT implication:** Chicago (CME) to New York (NYSE) — microwave beats fiber. The physics arbitrage that built the microwave tower industry between the two cities.

---

## Quick stats

| Metric | Value |
|--------|-------|
| 2026 Big Five capex | $600-650B |
| GS cumulative 2025-2027 | ~$1.4T |
| Power transformer lead time | 128-210 weeks |
| Primary market vacancy | 1.6% |
| Thermal runaway (15kW rack) | 75 seconds |
| Blackwell rack power | 120 kW |
| Water vs air heat capacity | 3,500x by volume |
| DC electricity demand 2030 | ~945 TWh (2x current) |
| PJM capacity auction | $329/MW-day (at cap) |
| Nuclear DC commitments | >10 GW |

---

## Related

- [[Data center infrastructure]] — supplier map and key players
- [[Thermal limits]] — liquid cooling necessity thesis
- [[AI datacenter architecture]] — design requirements
- [[Power constraints]] — grid bottleneck
- [[Hyperscaler capex]] — demand driver
- [[Long datacenter infrastructure]] — investment thesis
- [[Power infrastructure bottleneck]] — transformer/grid thesis
- [[Grid infrastructure super-cycle]] — broader grid investment
- [[Aeroderivative turbines for data centers]] — behind-the-meter power
- [[Data center land competition]] — real estate dynamics
- [[Space data centers]] — latency and cooling alternatives
- [[Dominion Energy]] — Virginia grid operator
- [[Digital Realty]] — DC REIT
- [[Equinix]] — colocation leader
- [[Vertiv]] — cooling/power pure-play
- [[Eaton]] — power distribution
