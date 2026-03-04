---
aliases: [Ayar]
---
#actor #opticalinterconnects #ai-infrastructure #private #usa

**Ayar Labs** — optical interconnect startup replacing copper with light inside AI data centers. [[NVIDIA]]- and [[AMD]]-backed. Just raised $500M Series E at $3.75B (Mar 3, 2026).

Ayar Labs is solving the next bottleneck in AI infrastructure: the copper wires inside data centers. As AI clusters scale to tens of thousands of GPUs, the electrical interconnects between chips become the constraint — consuming too much power and limiting bandwidth. Ayar replaces those copper links with silicon photonics: optical I/O chiplets that transmit data using light at 8 Tbps per chiplet. The $500M Series E at $3.75B valuation, led by Neuberger Berman with [[NVIDIA]] and [[AMD]] returning as strategic investors, funds the transition from R&D to high-volume manufacturing of co-packaged optics (CPO). The company is pre-revenue but positioned at the intersection of every major AI infrastructure buildout. The risk is execution — can they mass-produce photonic chiplets on [[GlobalFoundries]]' 45nm platform at the scale and yield required?

---

## Quick stats

| Metric | Value |
|--------|-------|
| Founded | 2015 |
| HQ | Santa Clara, CA |
| CEO | Mark Wade (co-founder, ex-DARPA) |
| Total raised | ~$870M |
| Latest round | Series E, $500M (Mar 3, 2026) |
| Valuation | $3.75B (post-money) |
| Revenue | Pre-revenue / early revenue |
| Commercialization | Mid-2026 target |
| TAM estimate | $38B+ by late 2020s (CEO estimate) |

---

## Technology

Core problem: Copper electrical interconnects are the bottleneck in AI data centers — too much power, limited bandwidth as clusters scale.

Solution: Silicon photonic chiplets that transmit data using light instead of electricity.

| Product | Function | Specs |
|---------|----------|-------|
| TeraPHY | Optical I/O chiplet | 8 Tbps bandwidth, UCIe-compatible, drop-in chiplet |
| SuperNova | Multi-wavelength light source | DFB laser array, up to 16 wavelengths, powers up to 16 TeraPHY ports |

Key technical details:
- Manufactured on [[GlobalFoundries]] 45nm silicon photonics platform
- Integrates electrical and photonic circuits on a single die
- Protocol support: PCIe 5.0, CXL 2.0, potentially [[NVIDIA]] NVLink
- UCIe (Universal Chiplet Interconnect Express) compatible — drop-in, no ASIC co-design required

Competitive advantage over peers: TeraPHY is a drop-in UCIe chiplet. Unlike [[Lightmatter]] and Celestial AI (now [[Marvell]]), Ayar does not require customers to co-design their ASICs around a proprietary photonic platform. This avoids vendor lock-in and makes adoption easier.

---

## Funding history

| Round | Date | Amount | Lead | Key Investors |
|-------|------|--------|------|---------------|
| Seed | 2016 | ~$275K | MIT competition (OptiBits) | Academic origin |
| Series A | ~2017-2018 | Undisclosed | [[Playground Global]] | — |
| Series B | Nov 2020 | $35M | Downing Ventures, BlueSky Capital | [[Intel]] Capital, [[GlobalFoundries]], [[Lockheed Martin]] Ventures |
| Series C | Apr 2022 | $130-155M | Boardman Bay Capital | HPE, [[NVIDIA]] entered |
| Series D | Dec 2024 | $155M | [[Advent International]], Light Street Capital | [[AMD]], [[Intel]] Capital, [[NVIDIA]] |
| Series E | Mar 2026 | $500M | Neuberger Berman | ARK Invest, QIA, 1789 Capital, [[Insight Partners]], Sequoia Global Equities, [[Alchip Technologies]], [[MediaTek]], [[NVIDIA]], [[AMD]] |

Total raised: ~$870M

---

## Key partnerships

| Partner | Relationship |
|---------|-------------|
| [[NVIDIA]] | Strategic investor (Series C/D/E), TeraPHY potentially NVLink-compatible |
| [[AMD]] | Strategic investor (Series D/E) |
| [[GlobalFoundries]] | Manufacturing partner (45nm silicon photonics) |
| [[Alchip Technologies]] | Integration partnership (Sep 2025) — co-packaged optics into compute/switch packages, TSMC 2.5D/3D packaging |
| Quantifi Photonics | SuperNova-powered Laser 1300 Series |

---

## Leadership

| Role | Name | Background |
|------|------|------------|
| CEO (co-founder) | Mark Wade | Became CEO Dec 2023. Previously President, Chief Scientist, CTO. Led team that designed optics in world's first processor to communicate using light. Ex-DARPA program manager. |
| Co-founders | Alex Wright-Gladstein, Vladimir Stojanovic, Chen Sun | — |
| Academic advisors | Rajeev Ram (MIT), Milos Popovic (CU Boulder) | Core technology invented at MIT and UC Berkeley (2010-2015) |

---

## Competitive landscape

| Company | Valuation | Approach | Status |
|---------|-----------|----------|--------|
| Ayar Labs | $3.75B | Drop-in UCIe chiplets (no co-design) | Series E, pre-revenue, closest to HVM |
| [[Lightmatter]] | $4.4B | Photonic interposer (Passage M1000) | Requires ASIC co-design, vendor lock-in |
| Celestial AI | Acquired by [[Marvell]] ~$3.25B | Photonic Fabric platform | Acquired Feb 2026 ($1B cash + shares, up to $5.5B with earnouts) |
| Avicena | — | Micro-LED based optical interconnects | Earlier stage |
| [[Astera Labs]] | Public (ALAB) | Connectivity/fabric for AI infrastructure | Adjacent market |

---

## Investment case

Bull:
- Both [[NVIDIA]] and [[AMD]] as strategic investors — hedging both sides of the GPU war
- UCIe drop-in approach avoids vendor lock-in, lowers adoption barrier
- $38B+ TAM by late 2020s (CEO estimate) as every AI cluster needs optical I/O
- Closest to high-volume manufacturing among optical interconnect startups
- [[Alchip Technologies]] partnership connects to [[TSMC]] packaging ecosystem

Bear:
- Pre-revenue at $3.75B valuation — steep execution risk
- [[GlobalFoundries]] 45nm is not leading edge — yield and scale questions
- [[Marvell]] acquired Celestial AI for $3.25B — deep-pocketed competitor entering
- [[Lightmatter]] at $4.4B with similar positioning
- Optical interconnect adoption timeline may slip if AI cluster growth slows

---

## Related

- [[NVIDIA]] — strategic investor, potential NVLink integration
- [[AMD]] — strategic investor
- [[GlobalFoundries]] — manufacturing partner (45nm silicon photonics)
- [[Alchip Technologies]] — integration partnership, [[TSMC]] packaging
- [[Lightmatter]] — competitor (photonic interposer)
- [[Marvell]] — competitor (acquired Celestial AI)
- [[Astera Labs]] — adjacent (connectivity/fabric)
- [[AI capex arms race]] — demand driver
- [[Memory shortage 2025-2026]] — parallel bottleneck theme

*Created 2026-03-04*
