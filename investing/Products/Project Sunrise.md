---
aliases: [Sunrise constellation]
---
#product #space #datacenter #constellation

**Project Sunrise** — [[Blue Origin]] orbital data center constellation. Filed with the FCC on March 19, 2026: up to 51,600 satellites in sun-synchronous orbits between 500 and 1,800 km altitude, with optical (laser) inter-satellite links sized for hyperscaler-grade transport. Complements Blue's earlier 5,408-satellite [[TeraWave]] constellation filing. The filing moves Blue from "vision" (Bezos's Oct 2025 "10-20 year" framing for orbital DCs) to "active program" within the platform war for orbital compute.

---

## Quick stats

| Metric | Value |
|---|---|
| Operator | [[Blue Origin]] (not [[Amazon]]) |
| FCC filing | March 19, 2026 |
| Satellite count | Up to 51,600 |
| Orbit | Sun-synchronous, 500-1,800 km altitude |
| Inter-satellite links | Optical (laser) |
| Orbital plane spacing | 5-10 km altitude separation |
| Satellites per plane | 300-1,000 |
| Complementary constellation | [[TeraWave]] (5,408 satellites, prior filing) |
| Deployment timeline | 2030s (per industry consensus) |

---

## Why Project Sunrise matters

The structural read: Blue is building this directly, *not* Amazon — meaning rockets and compute are vertically integrating inside Blue, mirroring [[SpaceX]]/[[Starlink]]/[[TERAFAB]]. Per [[Space Capital]] (Chad Anderson, Apr 26, 2026): "The architecture points toward a single institutional anchor customer — a hyperscaler or a government — that makes the whole system viable. That's the same playbook as [[Starshield]]."

Project Sunrise's scale (51,600 satellites + 5,408 TeraWave = ~57,000 total) is in the same league as SpaceX's 1M-satellite FCC filing (Jan 2026, with [[xAI]]) for orbital data center compute. The two filings together establish an orbital DC market structure with two integrated platforms (Blue + SpaceX) and supplier-tier hardware ([[NVIDIA]] [[Vera Rubin Space 1]], [[Google]] [[Project Suncatcher]]) — see [[Space data centers]] for the platform-war framing.

---

## Engineering profile

| Engineering challenge | Sunrise approach |
|---|---|
| Power | Sun-synchronous orbit (24/7 solar) |
| Cooling | TBD (radiator-based, see [[Space data centers]]) |
| Inter-satellite networking | Optical/laser mesh; "hyperscaler-grade transport" |
| Ground stations | Optical downlink to mesh-routed ground stations |
| Cosmic rays | TBD (radiation hardening trade-offs) |
| Repair logistics | Modular swap-out of failed satellites |

The optical inter-satellite link selection is consequential. [[SemiAnalysis]]'s critique of orbital DCs (see [[Space data centers]]) flagged Starlink's ~100 Gbps inter-satellite links as inadequate for AI-training-scale traffic versus InfiniBand's 3,200 Gbps per GPU. Whether Sunrise's optical mesh closes that gap at production cost is the open technical question.

---

## Filing context

| Element | Detail |
|---|---|
| Filer | Kuiper Systems LLC (Blue Origin operating entity) |
| Filed | March 19, 2026 |
| Stated purpose | "Provide in-space computing services" — orbital AI workload hosting |
| Constellation purpose | "Meet the growing computing requirements — and thus power demand — of artificial intelligence applications" |

The terminology "in-space computing services" is the regulatory framing for orbital data centers as a satellite-services market.

---

## Related

- [[Blue Origin]] — operator
- [[Jeff Bezos]] — founder/financier
- [[Space data centers]] — concept; orbital DC platform-war framing
- [[TeraWave]] — Blue Origin's earlier constellation filing
- [[Vera Rubin Space 1]] — [[NVIDIA]] orbital compute module (potential payload)
- [[Project Suncatcher]] — [[Google]] orbital DC initiative (parallel platform)
- [[SpaceX]] — competing platform (1M-satellite FCC filing, [[Terrafab]] AI satellite)
- [[Starshield]] — anchor-customer playbook reference
- [[Power constraints]] — terrestrial problem orbital DCs aim to solve

---

## Sources

- [Blue Origin joins the orbital data center race — SpaceNews](https://spacenews.com/blue-origin-joins-the-orbital-data-center-race/)
- [Blue Origin Plans 51,600-Satellite Computing Constellation — Aviation Week](https://aviationweek.com/space/satellites/blue-origin-plans-51600-satellite-computing-constellation)
- [Tom's Hardware coverage](https://www.tomshardware.com/networking/jeff-bezos-blue-origin-reveals-51-600-satellite-space-data-center-plans-project-sunrise-will-operate-in-sun-synchronous-orbits-between-500-1-800km-in-altitude)
- [Space Capital Space IQ Q1 2026](https://youtu.be/iGmr4g4Iot4) — platform-war framing

*Created 2026-04-27*
