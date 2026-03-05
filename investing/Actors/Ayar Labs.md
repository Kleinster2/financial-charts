---
aliases: [Ayar]
---
#actor #ai-infrastructure #optics #private

**Ayar Labs** — optical I/O chiplet company replacing copper interconnects with light-based data transmission in AI data centers. [[NVIDIA]]- and [[AMD]]-backed. Raised $500M Series E at $3.75B valuation (Mar 3, 2026).

Ayar Labs is solving the next physical bottleneck in AI infrastructure: the copper wires between chips inside data centers. As AI clusters scale to tens of thousands of GPUs, electrical interconnects become the constraint — consuming too much power, limiting bandwidth, and adding latency. Ayar's answer is TeraPHY, the world's first UCIe optical interconnect chiplet: 8 Tbps bidirectional, 10 nanosecond latency, 1/4 to 1/8 the power consumption of copper. It's a drop-in chiplet — no ASIC co-design required — carrying CXL, [[NVLink]], UALink, and Ethernet via UCIe streaming raw mode. The light source is SuperNova, a proprietary 16-wavelength laser. Fabrication runs on [[GlobalFoundries]] 45nm silicon photonics, with migration path to [[TSMC]] nodes.

The $500M Series E at $3.75B (3.75x step-up from $1B+ Series D), led by [[Neuberger Berman]], brought total funding to ~$870M. The strategic investor roster is the real signal: [[NVIDIA]], [[AMD]], [[Alchip Technologies]], and [[MediaTek]] all invested — four companies that collectively design or package most of the world's AI accelerators. Commercialization target is mid-2026, with funds earmarked for production scale-up, a Hsinchu [[Taiwan]] office, and ecosystem partnerships. Revenue is estimated at ~$91.6M for 2025, making this an early-revenue company rather than a pre-revenue bet. The risk is execution: can they mass-produce photonic chiplets at the yield and volume required before competitors — [[Lightmatter]] at $4.4B, [[Marvell]] (which acquired Celestial AI for ~$3.25B), and incumbents like [[Coherent]] — close the gap?

---

## Quick stats

| Metric | Value |
|--------|-------|
| Founded | 2015 |
| HQ | Santa Clara, CA |
| Employees | ~209 |
| CEO | Mark Wade (co-founder) |
| CTO | Vladimir Stojanovic (co-founder, UC Berkeley professor) |
| Total raised | ~$870M |
| Latest round | Series E, $500M (Mar 3, 2026) |
| Valuation | $3.75B (post-money) |
| Revenue | ~$91.6M (2025 estimate) |
| Commercialization | Mid-2026 target |
| Origin | DARPA POEM project (MIT, UC Berkeley, CU Boulder) |

---

## Technology

Core problem: Copper electrical interconnects are the bottleneck in AI data centers — too much power, limited bandwidth, too much latency as clusters scale.

Solution: Silicon photonic chiplets that transmit data using light instead of electricity.

| Product | Function | Specs |
|---------|----------|-------|
| TeraPHY | Optical I/O chiplet | 8 Tbps bidirectional (4 Tbps per direction), 10 ns latency, UCIe-compatible |
| SuperNova | Multi-wavelength light source | Proprietary 16-wavelength DFB laser array, powers TeraPHY optical ports |

TeraPHY technical details:
- 8x 1 Tbps optical ports, 16 wavelengths per fiber at 32 Gbps per wavelength
- 1/4 to 1/8 power consumption of electrical interconnects
- Manufactured on [[GlobalFoundries]] 45nm silicon photonics platform; can migrate to [[TSMC]] nodes
- Integrates electrical and photonic circuits on a single die
- Protocol support: CXL, [[NVLink]], UALink, Ethernet — all carried via UCIe streaming raw mode
- UCIe (Universal Chiplet Interconnect Express) compatible — drop-in, no ASIC co-design required

Competitive advantage over peers: TeraPHY is a drop-in UCIe chiplet. Unlike [[Lightmatter]] and Celestial AI (now [[Marvell]]), Ayar does not require customers to co-design their ASICs around a proprietary photonic platform. This avoids vendor lock-in and makes adoption easier.

---

## Funding history

| Round | Date | Amount | Lead | Key Investors |
|-------|------|--------|------|---------------|
| Seed | 2016 | ~$275K | MIT competition (OptiBits) | Academic origin |
| Series A | ~2017-2018 | Undisclosed | [[Playground Global]] | — |
| Series B | Nov 2020 | $35M | Downing Ventures, BlueSky Capital | [[Intel]] Capital, [[GlobalFoundries]], [[Lockheed Martin]] Ventures |
| Series C | Apr 2022 | $130M | Boardman Bay Capital | [[HPE]], [[NVIDIA]] entered |
| Series C1 | May 2023 | $25M (extension) | — | — |
| Series D | Dec 2024 | $155M | [[Advent International]], Light Street Capital | [[AMD]], [[Intel]] Capital, [[NVIDIA]] |
| Series E | Mar 2026 | $500M | [[Neuberger Berman]] (Gabe Cahill takes board observer seat) | [[ARK Invest]], [[Insight Partners]], [[QIA]], [[Sequoia]] Global Equities, [[1789 Capital]], [[AMD]], [[NVIDIA]], [[Alchip Technologies]], [[MediaTek]] |

Total raised: ~$870M

Series E valuation: $3.75B — a 3.75x step-up from the $1B+ Series D.

Use of funds: scale production, open Hsinchu Taiwan office, ecosystem partnerships, mid-2026 commercialization push.

---

## Leadership

| Role | Name | Background |
|------|------|------------|
| CEO (co-founder) | Mark Wade | Became CEO Dec 2023. Previously President, Chief Scientist, CTO. Led team that designed optics in world's first processor to communicate using light. |
| CTO (co-founder) | Vladimir Stojanovic | UC Berkeley professor |
| Co-founders | Chen Sun, Alex Wright-Gladstein, Milos Popovic, Rajeev Ram | Popovic at CU Boulder; Ram at MIT |

Academic origin: Core technology invented at MIT and UC Berkeley (2010-2015) under the DARPA POEM project.

---

## Key partnerships

| Partner | Relationship |
|---------|-------------|
| [[NVIDIA]] | Multi-round strategic investor (Series C/D/E), developing optical I/O for NVLink interconnects |
| [[AMD]] | Strategic investor (Series D/E) |
| [[GlobalFoundries]] | Fabrication partner (45nm silicon photonics) |
| [[Alchip Technologies]] | Integration partnership (Sep 2025) for AI accelerator integration; Series E investor |
| Global Unichip Corp (GUC) | [[TSMC]] majority-owned ASIC design integration |
| [[MediaTek]] | New Series E strategic investor |
| Quantifi Photonics | SuperNova-powered Laser 1300 Series |

---

## Competitive landscape

| Company | Valuation | Approach | Status |
|---------|-----------|----------|--------|
| Ayar Labs | $3.75B | Drop-in UCIe chiplets (no co-design) | Series E, ~$91.6M revenue (2025 est.), mid-2026 commercialization |
| [[Lightmatter]] | $4.4B | 3D photonic interconnects, Passage platform | Requires ASIC co-design, vendor lock-in risk |
| Celestial AI | Acquired by [[Marvell]] ~$3.25B | Photonic Fabric platform | Acquired Feb 2026 ($1B cash + shares, up to $5.5B with earnouts) |
| Ranovus | — | Odin single-chip optical engine | Earlier stage |
| Xscape Photonics | — | Optical interconnects | $57M raised |
| [[Coherent]] | Public | Co-packaged optics | Incumbent moving into CPO |
| Avicena | — | Micro-LED based optical interconnects | Earlier stage |
| [[Astera Labs]] | Public (ALAB) | Connectivity/fabric for AI infrastructure | Adjacent market |

---

## Investment case

Bull:
- Both [[NVIDIA]] and [[AMD]] as strategic investors — hedging both sides of the GPU war
- UCIe drop-in approach avoids vendor lock-in, lowers adoption barrier vs. [[Lightmatter]]
- Four chip companies investing simultaneously ([[NVIDIA]], [[AMD]], [[Alchip Technologies]], [[MediaTek]]) validates the technology
- ~$91.6M revenue already — not a pure pre-revenue bet at this point
- [[Alchip Technologies]] partnership connects to [[TSMC]] packaging ecosystem via GUC
- Mid-2026 commercialization timeline puts them ahead of most optical interconnect peers

Bear:
- $3.75B valuation on ~$91.6M revenue — 41x revenue multiple demands rapid scaling
- [[GlobalFoundries]] 45nm is not leading edge — yield and scale questions at high volume
- [[Marvell]] acquired Celestial AI for ~$3.25B — deep-pocketed competitor with distribution
- [[Lightmatter]] at $4.4B with $850M raised — well-funded rival
- [[Coherent]] and other incumbents moving into CPO could squeeze the standalone chiplet approach
- Optical interconnect adoption timeline may slip if AI cluster growth slows

---

## Related

- [[NVIDIA]] — multi-round strategic investor, potential NVLink optical integration
- [[AMD]] — strategic investor (Series D/E)
- [[GlobalFoundries]] — fabrication partner (45nm silicon photonics)
- [[TSMC]] — migration path for TeraPHY; connected via GUC and [[Alchip Technologies]]
- [[Alchip Technologies]] — integration partnership (Sep 2025), Series E investor
- [[MediaTek]] — Series E strategic investor
- [[Neuberger Berman]] — Series E lead
- [[ARK Invest]] — Series E investor
- [[QIA]] — Series E investor
- [[1789 Capital]] — Series E investor
- [[Sequoia]] — Series E investor (Global Equities)
- [[Insight Partners]] — Series E investor
- [[Advent International]] — Series D co-lead
- [[Lightmatter]] — competitor (3D photonic interconnects, Passage)
- [[Marvell]] — competitor (acquired Celestial AI)
- [[Coherent]] — competitor (incumbent CPO)
- [[Astera Labs]] — adjacent (connectivity/fabric)
- [[AI capex arms race]] — demand driver
- [[Memory shortage 2025-2026]] — parallel bottleneck theme

*Updated 2026-03-04*
