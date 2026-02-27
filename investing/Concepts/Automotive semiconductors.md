#concept #demand #automotive #sic

[[Semiconductors]] for automotive applications — EVs, ADAS, infotainment. Different dynamics than AI/datacenter. [[EV transition]] drives SiC adoption; ADAS drives compute complexity.

> **Key insight:** Auto semis are NOT in competition with AI for leading-edge capacity. Different fabs, different bottlenecks, different cycle.

---

## Market overview

| Metric | Value |
|--------|-------|
| Market size (2024) | ~$55B |
| Wafer share | 17% of total semis |
| Growth 2025e | +7% |
| Status | Post-boom settling |
| Key driver | EV penetration rate |

[[Automotive]] was hot during EV hype (2021-2023), now normalizing as EV growth slowed.

---

## [[Market structure]]

**Who leads automotive semiconductors:**

| Rank | Company | 2024 Rev | Key products |
|------|---------|----------|--------------|
| \#1 | [[Infineon]] | ~$7B | Power, MCUs |
| \#2 | [[NXP]] | ~$6B | Radar, MCUs |
| \#3 | [[Renesas]] | ~$5B | MCUs (\#1 globally) |
| \#4 | [[STMicro]] | ~$4B | SiC, power |
| \#5 | [[Texas Instruments]] | ~$3B | Analog |
| \#6 | [[Analog Devices]] | ~$2.5B | Analog, BMS |
| \#7 | [[onsemi]] | ~$2B | SiC, image sensors |

**Note:** These are automotive-specific revenues; total company revenues are larger.

---

## Key segments

### Silicon Carbide (SiC)

Power semiconductors for EV inverters, chargers. Higher efficiency than silicon.

**Key players:**
- [[STMicro]] — $1.1B SiC revenue (2024), Tesla supplier
- Wolfspeed — Pure-play SiC, capacity buildout
- [[Infineon]] — European leader, vertically integrated
- [[onsemi]] — Growing share, El Segundo facility

**SiC supply chain:**

| Layer | Players |
|-------|---------|
| Substrates | Wolfspeed, [[Coherent]], SK Siltron |
| Epitaxy | In-house or Wolfspeed |
| Device makers | Infineon, STMicro, onsemi, Rohm |

**Current state (Dec 2025):**
- STMicro: 2025 "transition year" (decline), 2026 growth but below 2024, 2027 back to 2024 levels
- Main customer (Tesla?) inventory correction
- EV penetration slower than expected 2 years ago

**Why SiC matters for EVs:**
- 15-20% efficiency gain over silicon IGBTs
- Smaller, lighter inverter systems
- Longer range for same battery
- Higher temperature operation

### Power semiconductors (Silicon)

IGBTs, MOSFETs for motor control, power management.

**Key players:**
- Infineon
- onsemi
- STMicro
- Texas Instruments

### ADAS / Autonomous

[[Sensors]], compute for driver assistance.

**Key players:**
- [[Mobileye]] ([[Intel]]) — EyeQ chips, \#1 in L2 ADAS
- [[NVIDIA]] — Drive platform, high-end compute
- [[Qualcomm]] — Snapdragon Ride, infotainment crossover

**ADAS chip complexity:**

| Level | Compute needs | Key players |
|-------|---------------|-------------|
| L2 (hands-on) | Low-medium | Mobileye, NXP |
| L2+ (supervised) | Medium | Mobileye, NVIDIA |
| L3 (eyes-off) | High | NVIDIA, Qualcomm |
| L4 (driverless) | Very high | NVIDIA, custom ([[Waymo]], Tesla) |

### MCUs (Microcontrollers)

The "nervous system" of the car — body control, safety, powertrain.

**Key players:**
- [[Renesas]] — \#1 globally in auto MCUs
- [[NXP]] — \#2, strong in [[Europe]]
- [[Infineon]] — \#3, power + MCU
- [[STMicro]] — Growing share

**Content per vehicle:**
- ICE vehicle: 15-30 MCUs
- EV: 30-50+ MCUs (more electronics)
- Autonomous: 100+ (sensors, compute)

---

## Why it's different from AI/datacenter

| Factor | AI/Datacenter | [[Automotive]] |
|--------|---------------|------------|
| Growth | Accelerating | Settling |
| Demand driver | [[Hyperscaler capex]] | [[Consumer]] EV adoption |
| Node | Leading edge (2nm, 3nm) | Mature + specialty (SiC) |
| Cycle | Structural | Cyclical + secular |

Auto doesn't compete for leading edge capacity — different fabs, different bottlenecks.

---

## EV vs ICE chip content

**Semiconductor content per vehicle:**

| Vehicle type | Chip content | Key difference |
|--------------|--------------|----------------|
| ICE | **~$750** | Engine control, basic electronics |
| Hybrid | ~$700-900 | + motor control, BMS |
| BEV | **~$1,300** | SiC inverter, BMS, no ICE (~1.7× ICE) |
| BEV + L3 ADAS | ~$1,500+ | + ADAS compute |
| BEV (2030 est.) | **~$2,000** | +53% growth from 2024 |

**~70% of the ICE→BEV increase** comes from power semiconductors (mainly inverter). Remaining 30% from MCUs and sensors for infotainment, body & comfort. Power semi content alone is **~5× higher** in a BEV vs ICE.

**What EVs add:**
- SiC/IGBT power semiconductors (inverter)
- Battery Management System (BMS) chips
- Onboard charger ICs
- Thermal management ICs

**What EVs remove:**
- Engine control MCUs
- Transmission control
- Emissions sensors

**Net:** EVs have 50-100% more chip content than equivalent ICE.

---

## EV adoption vs expectations

- 2021-2022: Hype peak, chip shortage, massive auto semi investment
- 2023-2024: EV growth slowed, inventory correction
- 2025-2027: Normalization, slower penetration than expected

STMicro SiC revenue trajectory tells the story:
- 2024: $1.1B (peak)
- 2025: Decline (transition)
- 2026: Growth but below 2024
- 2027: Back to 2024 levels

---

## Relationship to foundry wars

**Minimal overlap with AI/foundry themes:**
- Auto uses mature nodes (28nm+) — not leading edge
- SiC is specialty fab (not TSMC/[[Samsung]])
- Different supply chain (Infineon, STMicro have own fabs)

**Some overlap:**
- NVIDIA Drive for autonomous
- Qualcomm auto chips (TSMC)
- Advanced ADAS compute moving to smaller nodes

---

## What to watch

- [ ] EV adoption rates ([[China]], [[Europe]], US)
- [ ] Tesla production / inventory
- [ ] SiC pricing and capacity
- [ ] ADAS compute complexity increasing
- [ ] Legacy auto chip supply/demand

---

## Key players to potentially track

| Company | Focus | Notes |
|---------|-------|-------|
| STMicroelectronics | SiC, MCUs | European, Tesla supplier |
| Infineon | Power, auto MCUs | European leader |
| onsemi | SiC, power | US-based |
| NXP | Auto MCUs, radar | Dutch |
| Renesas | Auto MCUs | Japanese |

---

## [[China]] angle

**Chinese auto semi players:**

| Company | Focus | Status |
|---------|-------|--------|
| [[BYD]] Semiconductor | Power, MCUs | Vertically integrated |
| [[CATL]] | BMS chips | Exploring |
| StarPower | IGBTs | Growing share |
| Horizon [[Robotics]] | ADAS compute | Backed by VW |

**Dynamics:**
- Chinese OEMs prefer domestic suppliers (geopolitics)
- [[BYD]] most vertically integrated
- Quality gap closing but still exists
- [[Export controls]] less relevant (mature nodes)

---

## Foundry relationships

**Where auto chips are made:**

| Node | Foundry | Products |
|------|---------|----------|
| 28nm+ | [[GlobalFoundries]], [[UMC]], [[TSMC]] | MCUs, power management |
| SiC | Wolfspeed, STMicro, Infineon | Power semiconductors |
| 16nm-7nm | [[TSMC]], [[Samsung]] | ADAS compute |
| 5nm-3nm | [[TSMC]] | High-end ADAS (NVIDIA, Qualcomm) |

**Key point:** Most auto chips don't need leading edge — specialty processes matter more.

---

## Investment implications

**Bull case for auto semis:**
- EV penetration is secular (slower than hyped, but real)
- Content per vehicle increasing
- ADAS complexity driving compute demand
- European players have strong moats

**Bear case:**
- EV adoption slowdown (especially US)
- SiC overcapacity risk
- [[China]] competition (BYD Semiconductor)
- Cyclical exposure to auto production

**How to play it:**

| Strategy | Names |
|----------|-------|
| Power/SiC | [[Infineon]], [[STMicro]], [[onsemi]] |
| MCUs | [[Renesas]], [[NXP]] |
| ADAS compute | [[NVIDIA]], [[Qualcomm]], [[Mobileye]] |
| [[China]] exposure | [[BYD]], domestic plays |
| Foundry angle | [[GlobalFoundries]] (specialty) |

*Updated 2026-01-04*

---

## Related

- [[Infineon]] — \#1 auto semis (power, MCUs)
- [[NXP]] — \#2 auto semis (radar, MCUs)
- [[Renesas]] — \#1 auto MCUs globally
- [[STMicro]] — SiC leader, Tesla supplier
- [[Analog Devices]] — \#2 analog, BMS chips
- [[onsemi]] — SiC, image sensors
- [[NVIDIA]] — ADAS compute (Drive platform)
- [[Qualcomm]] — ADAS, infotainment
- [[Mobileye]] — L2 ADAS leader ([[Intel]])
- [[Tesla]] — SiC demand driver
- [[BYD]] — vertically integrated (BYD Semiconductor)
- [[GM]] — legacy OEM transition
- [[Toyota]] — hybrid leader, EV late
- [[GlobalFoundries]] — specialty foundry for auto
- [[End market demand]] — context (17% of wafer share)
