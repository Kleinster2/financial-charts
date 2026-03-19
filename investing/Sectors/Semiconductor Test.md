---
aliases: [Semi test, Chip testing, ATE sector, Semiconductor test ecosystem]
tags: [sector, semiconductors, ai, testing]
---

# Semiconductor Test

The semiconductor test ecosystem encompasses all equipment, consumables, and services required to verify chip functionality — from wafer-level probing through final system-level test. AI is driving a structural inflection: test cost as a percentage of total chip cost is rising from ~5% (traditional mobile/consumer SoCs) to **10-15%** for advanced AI packages, creating pricing power and volume leverage across the value chain.

## Why AI changes the economics

Two forces compound:

**1. Increased test intensity per device.** AI chips (GPUs, custom ASICs) have higher transistor counts, larger die areas, extreme performance/power constraints. More test vectors, longer burn-in, higher accuracy requirements. A single undetected defect in a multi-die module compromises the entire package — the cost of escape is orders of magnitude higher than consumer chips.

**2. More test steps from advanced packaging.** Chiplets, 2.5D integration ([[CoWoS]]), 3D stacked [[HBM]], complex interposers — each adds test insertions:
- **Known Good Die (KGD)** testing at wafer level before assembly (both logic and memory)
- **Wafer-level system integration** testing to catch early package failures
- **Mid-bond testing** in 3DIC flows
- **Post-package testing** for thermal, electrical, mechanical validation under final conditions

Probe cards are non-transferrable between chip designs — shorter [[NVIDIA]]/[[AMD]] product cycles and proliferating ASICs create a structural volume tailwind for consumable test hardware.

## Value chain

### Automated Test Equipment (ATE)

The core instruments that apply test patterns and measure chip responses.

| Company | Ticker | HQ | Notes |
|---------|--------|----|-------|
| **[[Advantest]]** | 6857.T | Japan | Better AI positioning (CoWoS exposure); dominant in HBM test |
| **[[Teradyne]]** | TER | US | Strong in logic; also robotics (Universal Robots) |
| **[[Chroma ATE]]** | 2360.TW | Taiwan | Power electronics, EV/battery testing |

All three ATE makers reported record or near-record results for FY2025/CY2025, with shares more than tripling over the past year (Mar 2026). [[Advantest]] expects +37% revenue and 2x+ net profit for FY ending Mar 2026. [[Teradyne]] posted strong revenue rebound and 26%-above-consensus Q1 2026 guidance. [[Chroma ATE]] posted record revenue and earnings for CY2025.

*Source: Nikkei Asia (Mar 19, 2026)*

### Wafer Probers

Precision machines that align wafers under probe cards for ATE contact. No longer commodity tools — now critical infrastructure for AI chip production.

| Company | Ticker | HQ | Notes |
|---------|--------|----|-------|
| **[[Accretech]]** (Tokyo Seimitsu) | 7729.T | Japan | Top-tier logic and memory probing |
| **[[Tokyo Electron]]** | 8035.T | Japan | Niche part of total business; better known for front-end fab tools |

AI drives: large-area reticles, high pin-count dies, multiple test passes (before and after partial assembly).

### Probe Cards

Consumable interface between prober and wafer. Each chip design requires a unique probe card (non-transferrable). Must accommodate higher pin counts, tighter pitches, thermal management for high-power AI parts.

| Company | Ticker | HQ | Key market |
|---------|--------|----|-----------|
| **[[Technoprobe]]** | TPRO.MI | Italy | AI/HPC logic die |
| **[[FormFactor]]** | FORM | US | Memory (SK Hynix supplier) |
| **[[MJC]]** | — | Japan | Memory (Samsung, [[Micron]] supplier) |

Structural tailwind: shorter product cycles from NVIDIA/AMD + proliferating ASIC entrants = more unique probe card designs per year.

### Test Sockets

Interface chip packages with testers. Growing specialization driven by thermal stress, insertion/removal cycles, high-frequency signal integrity.

| Company | Ticker | HQ | Notes |
|---------|--------|----|-------|
| **[[WinWay Technology]]** | 6190.TW | Taiwan | AI accelerator socket orders growing |
| **[[Enplas]]** | 6961.T | Japan | |
| **[[LEENO]]** | 058470.KQ | Korea | |
| **[[ISC Co]]** | 095340.KQ | Korea | |

### Test Handlers

Equipment that physically handles packages during final test. Thermal management is the key challenge — larger/hotter AI packages break legacy equipment.

| Company | Ticker | HQ | Notes |
|---------|--------|----|-------|
| **[[Cohu]]** | COHU | US | Eclipse platform for extreme thermal AI testing |

See [[Final test bottleneck]] for the thermal constraint thesis.

### Burn-in / Reliability Test

Stress testing under high temperature and voltage to catch early-life failures. Shifting from SiC/EV (which drove the previous surge) to AI/data center chips. Industry moving toward wafer-level burn-in (testing many dies in parallel before packaging).

| Company | Ticker | HQ | Notes |
|---------|--------|----|-------|
| **[[Aehr Test Systems]]** | AEHR | US | Wafer-level burn-in; pivoting from SiC to AI/DC |
| **[[Pentamaster]]** | 7160.KL | Malaysia | Burn-in and reliability systems |

### OSATs (Test-Focused)

Outsourced assembly and test providers offering integrated flows from wafer sort through system-level test.

| Company | Ticker | HQ | Notes |
|---------|--------|----|-------|
| **[[KYEC]]** | 2449.TW | Taiwan | **Monopoly on NVIDIA GB package testing** + Amazon ASIC exposure |
| **[[ASE]]** | ASX | Taiwan | #1 OSAT globally; expanding test-centric packaging |
| **[[Amkor]]** | AMKR | US | Integrated test + packaging services |

KYEC is the standout pure-play on AI test demand.

## Investment framework

Test is a "picks and shovels" play on AI silicon — foundry-agnostic, bottleneck-positioned, with rising cost share creating pricing power.

| Angle | Best positioned |
|-------|----------------|
| ATE (capex cycle) | Advantest > Teradyne (CoWoS edge) |
| Consumables (recurring) | Technoprobe, FormFactor (probe cards), WinWay (sockets) |
| Bottleneck pricing power | Cohu (thermal handler monopoly), KYEC (NVIDIA test monopoly) |
| Burn-in pivot | AEHR (SiC → AI/DC) |
| Diversified OSAT | ASE, Amkor |

See [[Long OSAT and test equipment]] for the active thesis.

## Related

- [[Final test bottleneck]] — thermal constraint thesis
- [[Long OSAT and test equipment]] — investment thesis
- [[Advanced packaging]] — upstream bottleneck driving test complexity
- [[CoWoS]] — TSMC's 2.5D packaging driving KGD test demand
- [[HBM]] — stacked memory requiring multi-step test
- [[Semiconductor primer]] — industry overview

## Sources

- Chips and Wafers: [Semiconductor Test: A Compelling Investment Theme](https://chipsandwafers.substack.com/p/semiconductor-test-a-compelling-investment) (March 2026)
