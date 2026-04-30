---
aliases: [Overview, Overview Energy Inc]
tags: [actor, energy, space, datacenter, private]
---

#actor #energy #space #datacenter #private

**Overview Energy** — Space solar power startup developing a constellation of geosynchronous satellites that collect continuous sunlight in orbit and beam it back to existing terrestrial solar facilities as low-intensity near-infrared light, extending the hours those facilities can generate power. On Apr 27, 2026, [[Meta]] announced a "first-of-its-kind" agreement giving [[Meta]] early access to up to 1 GW of capacity from Overview's space solar system, with initial orbital demonstration in 2028 and commercial power delivery targeted for 2030. The deal positions Overview as the first credibly funded commercial space-based solar power offtake in the AI data center supply pipeline.

---

## Quick stats

| Field | Value |
|---|---|
| Sector | Space-based solar power |
| Status | Private |
| First major customer | [[Meta]] (up to 1 GW early access) |
| Orbital demonstration target | 2028 |
| Commercial power delivery target | 2030 |
| Technology | Geosynchronous satellites; near-infrared beam to existing solar farms |

---

## Founding

Founded in 2022; HQ Washington, DC.

| Item | Detail |
|---|---|
| Founded | 2022 |
| HQ | Washington, DC |
| Stealth exit | Dec 10, 2025 (first airborne power-beaming demonstration) |

---

## Funding rounds

| Date | Round | Amount | Investors |
|---|---|---|---|
| 2022-2025 | Pre-seed / Seed (combined disclosure) | ~$20M total | [[Engine Ventures]], [[Lowercarbon Capital]], [[Prime Movers Lab]], [[EQT Foundation]], [[Earthrise Ventures]], [[Aurelia Institute]] |

Total raised to date: ~$20M (per TechCrunch, pv magazine USA, Dec 2025). Specific round structure (Seed / Series A breakdown) and per-investor allocation not publicly disclosed; the figure is the cumulative reported total at stealth exit Dec 10, 2025.

The Apr 27, 2026 [[Meta]] agreement is an offtake for up to 1 GW, not an equity investment. Cap table to be updated when subsequent funding rounds are disclosed.

---

## Cap table (Apr 2026)

Per-investor ownership splits not publicly disclosed. Six named investors (Engine Ventures, Lowercarbon Capital, Prime Movers Lab, EQT Foundation, Earthrise Ventures, Aurelia Institute) plus undisclosed others. Update pending public filings or subsequent funding round.

---

## Stealth exit and demonstration record

Overview emerged from stealth on Dec 10, 2025 by demonstrating the world's first airborne power-beaming for space solar energy: power was transmitted from a moving aircraft to a ground receiver 5 kilometers (~3 miles) below. The demonstration validated the wireless-power transmission core of the system in motion, which is a closer analog to satellite-to-ground beaming than static lab demos.

| Milestone | Date | Detail |
|---|---|---|
| Founded | 2022 | Washington DC |
| Stealth exit | Dec 10, 2025 | First airborne moving-platform power-beam demo (5km, plane to ground) |
| [[Meta]] forward offtake | Apr 27, 2026 | Up to 1 GW |
| LEO orbital demonstration | Target 2028 | Megawatt-class transmission |
| Commercial power delivery | Target 2030 | At-scale GEO constellation

---

## Why this matters

The structural problem in the AI data center buildout is around-the-clock power. Solar and wind are intermittent. Nuclear (SMRs, the [[Cameco]]/[[NuScale]]/[[Oklo]] thesis) takes a decade. Gas turbines work but face procurement bottlenecks ([[GE Vernova]] order book). Grid interconnects take 4-7 years. Hyperscaler power procurement has been the binding constraint since 2024.

Overview's pitch is methodologically novel: don't build new ground capacity, *extend the duty cycle of existing capacity* by beaming additional sunlight to operating solar farms. That sidesteps the two binding constraints — land and grid interconnect — by routing through facilities already connected to the grid. The output is incremental MWh on existing assets, not new sited generation. If it works, it converts existing solar PPAs into 24/7 baseload-equivalent power.

The technology has a long history of academic and government interest (NASA, JAXA, Caltech's SSPP demonstrator, China's Bishan project) but has never reached commercial scale because the economics required either ground-to-orbit cost reduction or a willing high-margin customer. [[Meta]]'s 1 GW commitment is the first AI-era hyperscaler willingness to underwrite the second path.

---

## How it works (Apr 27 disclosure)

| Component | Detail |
|---|---|
| Collection | Geosynchronous orbit satellites collect sunlight 24/7 |
| Transmission | Beamed as low-intensity near-infrared light |
| Reception | Existing terrestrial solar PV facilities |
| Conversion | Standard PV cells convert the beam to electricity |
| Safety claims | Beam invisible, less intense than sunlight, "passively safe" for humans, animals, aircraft |
| Land/grid impact | None — uses existing facilities |

The receiver-side advantage is that [[Meta]] (and any future customer) does not need to permit and build new ground generation. The constraint moves to the upstream: launch costs, satellite manufacturing, and the orbital aperture economics.

---

## Strategic positioning

| vs traditional power source | Overview claim |
|---|---|
| New utility-scale solar | No new land, no new interconnect |
| Nuclear / SMRs | Faster commercialization (target 2030 vs SMR 2032+) |
| Battery storage | No degradation cycle; no lithium supply dependence |
| Gas peakers | Zero-carbon |
| Existing solar PPAs | Increases asset capacity factor without owner capex |

The competitive vulnerability is execution risk. Space-based solar has been "five years away" for forty years. The 2028 orbital demonstration is the first proof point; commercial delivery is 2030. [[Meta]]'s commitment is a forward offtake, not deployed power.

---

## Read-throughs

For [[Meta]]: the deal is the most aggressive AI-era hyperscaler power experiment to date — even more so than [[Microsoft]]'s [[Three Mile Island]] reactor restart with [[Constellation Energy]] or [[Amazon]]'s [[Talen Energy]] nuclear PPA. [[Meta]] is signaling it will pay forward-cost premia for any path to durable around-the-clock data center power.

For the broader AI capex thesis: Overview validates that *novel* power sources are now part of the hyperscaler procurement budget, not just incremental scaling of existing forms. Combined with [[Project Stargate]]'s gas-turbine procurement, [[Anthropic]]'s [[Microsoft]]-backed nuclear strategy, and [[xAI]]'s [[Memphis]] grid-edge work, this is the proliferation of unconventional power being absorbed into AI infrastructure.

---

## Open questions

- Funding history — Overview's prior round structure, total raise, lead investors not yet public
- Satellite manufacturing path — internal or contracted; payload mass and beam aperture economics
- Launch partner — [[SpaceX]], [[Blue Origin]], or sovereign launchers; cost per GEO satellite is the binding economic factor
- Receiver-side design — which solar facilities specifically, and the offtake economics for the host facility
- The 2028 demo — single satellite or constellation; demonstration scale (kW vs MW class)

---

## Related

### Actors
- [[Meta]] — first major customer (up to 1 GW early access, Apr 27 2026)

### Concepts
- [[AI capex arms race]] — power procurement is the binding constraint
- [[Power constraints]] — hyperscaler-specific shortage thesis
- [[BYOP]] — bring-your-own-power data center model

### Adjacent
- [[Constellation Energy]] — [[Microsoft]] / [[Three Mile Island]] nuclear restart
- [[Talen Energy]] — [[Amazon]] / [[Susquehanna]] nuclear PPA
- [[GE Vernova]] — gas turbine bottleneck
- [[Cameco]], [[NuScale]], [[Oklo]] — SMR thesis
- [[SpaceX]], [[Blue Origin]] — likely launch partners

---

## Sources

- [PR Newswire — Overview Energy and Meta Announce First-of-Its-Kind Agreement to Bring Space Solar Energy to Data Centers](https://www.prnewswire.com/news-releases/overview-energy-and-meta-announce-first-of-its-kind-agreement-to-bring-space-solar-energy-to-data-centers-302753490.html) — Apr 27, 2026
- [pv magazine USA — Meta signs with Overview Energy to power AI datacenters with space-based solar](https://pv-magazine-usa.com/2026/04/27/meta-signs-with-overview-energy-power-ai-datacenters-with-space-based-solar/) — Apr 27, 2026
- [The Next Web — Meta signs a deal to beam solar energy from space to its AI data centres](https://thenextweb.com/news/meta-overview-energy-space-solar) — Apr 27, 2026

*Created 2026-04-27*
