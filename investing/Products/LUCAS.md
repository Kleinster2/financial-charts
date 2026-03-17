---
aliases: [LUCAS drone, FLM-136, FLM-136 Block 1, Low-cost Uncrewed Combat Attack System, Flexible Loitering Munition 136]
tags: [product, drones, defense, loitering-munition, usa]
---

# LUCAS

**LUCAS** (Low-cost Uncrewed Combat Attack System) — a $35,000 one-way attack drone built by [[SpektreWorks]], reverse-engineered from [[Iran]]'s [[Shahed-136]]. First combat use February 28, 2026 during [[Operation Epic Fury]]. The weapon that proved the US could take the cheap-drone playbook validated in [[Ukraine war|Ukraine]] and deploy it at strategic scale in 18 months.

---

## Synopsis

LUCAS is the first long-range loitering munition the US has used in combat. At $35,000 per unit vs. $2.5M for a Tomahawk, it inverts the cost equation that has defined US precision strike since 1991. The design lineage runs through four countries: German Dornier DAR (1980s anti-radar drone) to Israeli [[IAI]] Harpy to Iranian [[Shahed-136]] to American LUCAS. [[SpektreWorks]] reverse-engineered a captured Shahed, cut the weight by 59% (81.5 kg vs 200 kg), added GPS-denied visual navigation, Starlink datalinks, and autonomous swarm coordination via the MUSIC mesh network — capabilities the Shahed lacks entirely. The result is lighter, smarter, and networked, but shorter-range and smaller-warhead than its Iranian parent.

The procurement story matters as much as the specs. Public unveiling to combat employment: 43 weeks. The vehicle was APFIT — a rapid acquisition authority that compressed the 5-10 year MDAP timeline into months. The government owns the design IP, structured for multi-vendor production at scale (the "Liberty Ship" model). Current production is [[SpektreWorks]] only, but the Drone Dominance Program targets 200,000+ drones by 2028 across up to 20 manufacturers. LUCAS is the first weapon fielded under this framework. Whether it's the Shahed killer or just the proof of concept depends on whether the Pentagon can actually execute mass production at the $35K price point.

---

## Specifications

| Spec | LUCAS (FLM-136 Block 1) | [[Shahed-136]] (comparator) |
|------|-------------------------|----------------------------|
| Length | 2.99 m (9.8 ft) | 3.5 m |
| Wingspan | 2.50 m (8.2 ft) | 2.5 m |
| Launch weight | 81.5 kg (180 lb) | ~200 kg |
| Payload | 18.1 kg (40 lb) | ~30-40 kg |
| Range | ~822 km (444 nm / 500 mi) | ~2,000-2,500 km |
| Endurance | 6 hours | ~3-4 hours |
| Cruise speed | 137 km/h (74 kt) | ~185 km/h |
| Dash speed | 194 km/h (105 kt) | — |
| Ceiling | 15,000 ft (4,500 m) | ~4,000 m |
| Engine | DA-215 (215cc, 2-cyl, Desert Aircraft) | Mado MD-550 (4-cyl, ~50 hp) |
| Guidance | GPS/INS + visual nav (GPS-denied) | GPS/INS only |
| Networking | MUSIC mesh, Starlink/Starshield BLOS | None |
| Swarm capable | Yes (hub-and-spoke architecture) | No |
| Unit cost | ~$35,000 | Est. $20,000-50,000 |
| Launch | Pneumatic catapult, RATO, truck-mounted, shipborne | Truck-mounted 5-unit rack |

LUCAS is 59% lighter but carries half the payload and has roughly one-third the range of the Shahed. The advantage is not raw performance — it's networking, autonomy, and the sensor suite.

---

## Warhead options

| Type | Application |
|------|-------------|
| High-explosive fragmentation | Soft targets (baseline config) |
| Thermobaric | Area effect |
| Fragmentation with zirconium incendiary liners | Combined blast/incendiary |
| Shaped charge | Armored vehicles, fortified positions |

Interchangeable nose sections: explosive warhead module OR EO/IR sensor module for ISR/BDA (battle damage assessment). The same airframe serves as both weapon and reconnaissance platform.

---

## Networking and autonomy

LUCAS integrates into the Multi-domain Unmanned Systems Communications (MUSIC) mesh network using a hub-and-spoke swarm architecture:

- Hub drones carry satellite comms (Viasat MUSIC and [[SpaceX]] Starlink/Starshield), gimballed camera, and beyond-line-of-sight datalinks
- Spoke drones use line-of-sight comms only — cheaper, lighter
- Swarm coordination via Noda orchestrator software (startup; declined to comment on operational role)
- Autonomous waypoint navigation with GPS-denied visual fallback
- Warfighters can control multiple LUCAS units from a single interface

This is the key differentiation from the [[Shahed-136]], which flies a pre-programmed GPS route with no ability to adapt, coordinate, or relay data.

---

## Development timeline

| Date | Milestone |
|------|-----------|
| 2015 | [[SpektreWorks]] founded in Phoenix, AZ |
| Pre-2025 | US captures [[Shahed-136]]; SpektreWorks reverse-engineers into FLM-136 target drone |
| Jun 6, 2025 | Executive Order 14307, "Unleashing American Drone Dominance" (Trump) |
| Jul 10, 2025 | [[Pete Hegseth]] "Drone Dominance" memo — reclassifies Group 1/2 UAS as consumable commodities |
| Jul 16, 2025 | LUCAS publicly debuted at Pentagon courtyard event with Hegseth |
| Jul ~24, 2025 | $30M APFIT contract awarded to [[SpektreWorks]] (Army Contracting Command) |
| 2025 | Testing at Yuma Proving Ground (Marine Corps-sponsored, inert payloads) |
| Dec 3, 2025 | CENTCOM announces Middle East deployment — Task Force Scorpion Strike (SOCCENT) |
| Dec 16, 2025 | First shipborne launch from USS Santa Barbara (LCS-32) in Persian Gulf (Task Force 59) |
| Jan 3, 2026 | OSINT-identified use in Operation Absolute Resolve (Venezuela) — not officially confirmed |
| Feb 28, 2026 | First officially confirmed combat use in [[Operation Epic Fury]] against [[Iran]] |
| Mar 5, 2026 | Admiral Brad Cooper calls LUCAS "indispensable"; SASC hearing on drone industrial base |

Public debut to combat: 43 weeks. Concept to deployment: ~18 months.

---

## Combat deployment

### Operation Epic Fury (Feb 28, 2026) — confirmed

Task Force Scorpion Strike (SOCCENT) launched ground-based LUCAS against:
- IRGC command and control facilities
- Iranian air defense assets
- Missile and drone launch sites
- Military airfields
- [[Shahed-136]] manufacturing sites

Part of a multi-domain attack (6,000+ total targets in Epic Fury). CENTCOM declined to disclose number of LUCAS fired, hit rate, or BDA. One official: "Don't think of it as a traditional squadron; it could be 100 or 2,000." CENTCOM has "countless" available for future surges.

Owen West (DIU director) testified to SASC (Mar 5): "Just a few days ago, America used one-way attack drones for the first time in combat in Iran, with Task Force Scorpion Strike firing the LUCAS drone, a reverse-engineered Shahed-136."

### Operation Absolute Resolve (Venezuela, Jan 3, 2026) — unconfirmed

OSINT researchers identified LUCAS-type drones via acoustic analysis of ground video from the Venezuela operation. Deployed alongside 150+ aircraft. Not officially confirmed by CENTCOM as LUCAS.

---

## Cost context

| Munition | Unit cost | LUCAS equivalents for same spend |
|----------|-----------|----------------------------------|
| LUCAS | $35,000 | 1 |
| JDAM | ~$80,000 | 2.3x |
| Hellfire | ~$150,000 | 4.3x |
| Tomahawk (Block V) | ~$2,500,000 | 71x |

At $35K/unit, $800M buys ~23,000 LUCAS rounds. For context, the US fired 168 Tomahawks in the first 100 hours of [[Operation Epic Fury]] (CSIS) — at $420M in Tomahawks alone. The same spend would buy 12,000 LUCAS.

---

## Procurement

| Field | Detail |
|-------|--------|
| Acquisition pathway | APFIT (Accelerate the Procurement and Fielding of Innovative Technologies) |
| Contract authority | Army Contracting Command |
| Initial contract | $30M to [[SpektreWorks]] |
| IP ownership | US government (not SpektreWorks) |
| Multi-vendor intent | Up to 20 simultaneous manufacturers |
| Program umbrella | Drone Dominance Program ($1.1B, 200,000+ drones by Jan 2028) |
| Program lead | Owen West (Senior Advisor for Drone Dominance / DIU director) |
| Key official | Col. Nicholas Law (Director of Experimentation, OSD R&E) |

---

## Design lineage

Dornier DAR (West Germany, 1980s anti-radar drone) --> [[IAI]] Harpy (Israel) --> [[Shahed-136]] / Shahed-131 (Iran) --> Geran-2 (Russian copy) --> FLM-136 / LUCAS (US reverse-engineered copy)

The delta-wing one-way attack drone concept traces to a 1980s West German design. LUCAS is the fourth-generation derivative.

---

## Variants (known/conceptual)

| Variant | Status | Description |
|---------|--------|-------------|
| LUCAS / FLM-136 Block 1 | Production | Baseline loitering munition (combat-deployed) |
| LUCAS ISR | Conceptual | Surveillance-oriented with enhanced recon sensors |
| LUCAS EW | Conceptual | Electronic warfare payload for radar/comms disruption |

---

## Related

- [[SpektreWorks]] — manufacturer (Phoenix, AZ)
- [[Shahed-136]] — design origin (Iranian, reverse-engineered)
- [[Operation Epic Fury]] — first confirmed combat use (Feb 28, 2026)
- [[Drones]] — sector overview
- [[Drone warfare]] — cost asymmetry thesis
- [[AeroVironment]] — Switchblade family (tactical competitor, different class)
- [[Anduril]] — ALTIUS-600M (loitering munition competitor)
- [[Kratos]] — attritable drone peer
- [[Pete Hegseth]] — Drone Dominance directive
- [[Iran]] — target of strikes; origin of reverse-engineered design
- [[Iran conflict defense repricing]] — munitions demand catalyst
- [[Defense]] — sector hub
