#concept #semiconductor #manufacturing #equipment

# EUV lithography

Extreme ultraviolet lithography — 13.5nm wavelength light used to pattern sub-7nm chips. [[ASML]] has 100% monopoly. Required for all leading-edge logic and advanced memory.

---

## Quick stats

| Metric | Value |
|--------|-------|
| Wavelength | 13.5nm |
| vs DUV | 14x shorter (193nm) |
| Resolution | ~13nm (Low-NA) |
| ASML market share | **100%** |
| System cost | $150-220M |
| First HVM | October 2019 ([[TSMC]] N7+) |

---

## How it works

**Laser-produced plasma (LPP):**
1. [[TRUMPF]] 30kW CO2 laser fires at tin droplets 50,000 times/second
2. Tin plasma emits 13.5nm photons
3. Light collected by multilayer mirrors ([[Carl Zeiss SMT]])
4. Entire system operates in vacuum (EUV absorbed by air)

Each machine: 100,000 parts, 40 freight containers + 3 cargo planes + 20 trucks to ship.

---

## Why ASML has a monopoly

| Component | Supplier | Status |
|-----------|----------|--------|
| System integration | [[ASML]] | Sole integrator |
| Mirrors | [[Carl Zeiss SMT]] | Exclusive (ASML owns 24.9%) |
| Laser | [[TRUMPF]] | Sole supplier of 30kW CO2 |
| Light source | Cymer (ASML subsidiary) | Acquired 2013 |

**30+ years of joint development, $9B+ R&D.** Supply chain is single-sourced for critical components — impossible to replicate quickly.

---

## Current systems

| System | Throughput | Overlay | Price | Status |
|--------|------------|---------|-------|--------|
| **NXE:3400C** | 170 wph | 1.4nm | ~$170M | First HVM-oriented (2019) |
| **NXE:3600D** | 160 wph | 1.1nm | ~$200M | Current workhorse |
| **NXE:3800E** | 195-220 wph | <1.1nm | ~$180M | Latest, supports 2nm |
| **NXE:4000F** | >220 wph | <0.8nm | TBD | Expected 2026 |

---

## Customer adoption

| Customer | First EUV HVM | Current nodes |
|----------|---------------|---------------|
| [[TSMC]] | Oct 2019 (N7+) | 7nm, 5nm, 3nm, 2nm |
| [[Samsung]] | 2020 | 5nm, 3nm, 2nm |
| [[Intel]] | 2024 (Intel 4) | Intel 4, Intel 3, 18A |
| [[SK Hynix]] | 2021 (10nm DRAM) | Advanced DRAM, HBM |

TSMC bought 18 of 30 units shipped in 2019.

---

## What it enabled

| Node | Year | EUV layers |
|------|------|------------|
| 7nm (N7+) | 2019 | First commercial |
| 5nm | 2020 | 10+ layers |
| 3nm | 2022 | 20+ layers |
| 2nm | 2025 | Extensive |

**Without EUV:** Would require 4-5x DUV exposures per layer (multi-patterning), destroying economics.

---

## Limitations

| Challenge | Detail |
|-----------|--------|
| Cost | $150-220M per system |
| Complexity | Vacuum operation, tin contamination |
| Throughput | Lower than DUV (~200 vs 300 wph) |
| Resolution limit | ~13nm at NA 0.33 |

For finer features (sub-8nm), need [[High-NA EUV]].

---

## China situation

**EUV completely banned** under US/Dutch export controls. China cannot:
- Buy EUV systems
- Get parts or service for any EUV
- Access the technology

Domestic alternative (SMEE) attempting EUV via laser-driven plasma, but years behind.

---

## Related

**Technology:**
- [[DUV lithography]] — predecessor, still 80% of volume
- [[High-NA EUV]] — next generation (0.55 NA)
- [[Multi-patterning]] — DUV workaround

**Companies:**
- [[ASML]] — sole EUV supplier
- [[Carl Zeiss SMT]] — mirror supplier
- [[TRUMPF]] — laser supplier
- [[TSMC]] — largest EUV customer
- [[Samsung]] — \#2 customer
- [[Intel]] — aggressive adopter

**Context:**
- [[Export controls]] — blocks China access
- [[Semiconductor manufacturing]] — where EUV fits

*Created 2026-01-28*
