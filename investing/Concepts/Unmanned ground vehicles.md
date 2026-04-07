---
aliases: [UGV, UGVs, unmanned ground vehicle, ground robots, military robots, robotic combat vehicle]
tags: [concept, defense, robotics, technology]
---

# Unmanned ground vehicles

Military ground robots — reconnaissance, logistics, combat, EOD/bomb disposal. The least mature of the three unmanned domains (air, sea, ground), but Ukraine is forcing rapid adoption: 15,000 UGVs delivered to Ukrainian forces in 2025 (up from 2,000 in 2024), with 20,000+ planned for 2026.

---

## Synthesis

Ground autonomy lags aerial and maritime autonomy for a basic reason: terrain is harder than air or water. Off-road navigation, obstacle avoidance, and unpredictable surfaces demand more sophisticated AI than flying in open sky or cruising on open ocean. But Ukraine is collapsing the development timeline. The 3rd Assault Brigade now handles 80% of logistics operations with UGVs; in Pokrovsk and Myrnorad the figure is 90%. Ukrainian General Staff reports robotic platforms reduced personnel casualties by up to 30%. One UGV survives 7-8 trips before being destroyed — at $15,800-18,400 per unit, that's $2,000-2,300 per mission, roughly the cost of one quadcopter.

The US Army's Robotic Combat Vehicle (RCV) program was cancelled in May 2025 as part of SecDef Hegseth's budget reallocation, then restarted as UGCRV (Unmanned Ground Commercial Robotic Vehicle) with a $650K unit cost cap — a tacit admission that the original program was too expensive and too slow. Meanwhile, the real action is in autonomy software: [[Forterra]] ($238M Series C, >$1B valuation), [[Overland AI]] ($132M raised, 82nd Airborne deployment), and Scout AI ($15M seed) are building the AI stacks that convert existing military vehicles into autonomous platforms. The hardware is increasingly commodity; the software is the moat — the same pattern as [[Software-defined Defense]] in aerial systems.

Israel's Gaza operations (2024-2025) were characterized as the "first robotics war" — tens of thousands of autonomous systems deployed, including unmanned M113 APCs and D9 bulldozers. In December 2024, Ukraine's 13th KHARTIIA Brigade executed the first combined-arms robotic assault, coordinating unmanned surveillance drones, minelaying drones, and armed ground robots. The concept is no longer theoretical.

---

## Market size

| Source | 2025 | 2031-2035 | CAGR |
|--------|------|-----------|------|
| Mordor Intelligence | $1.96B | $3.08B (2031) | 7.8% |
| Precedence Research (all UGV) | $3.94B | $8.80B (2034) | 9.5% |
| Market Research Future | $3.19B | $12.14B (2035) | 14.3% |

Defense tech VC overall: $49.1B in 2025 (up from $27.2B in 2024, +41% in number of investing firms).

---

## Key US programs

### RCV (Robotic Combat Vehicle) — cancelled then restarted

| Phase | Status | Detail |
|-------|--------|--------|
| Phase I (2023-24) | Completed | Four contractors: McQ, [[Textron Systems]], [[General Dynamics]], [[Oshkosh Defense]]. ~$24.72M combined |
| Phase II | Won then cancelled | [[Textron Systems]] Ripsaw M3 selected (Mar 2025). Cancelled May 2025 (Hegseth budget realignment) |
| UGCRV (restart) | RFI issued | New, cheaper program. Requirements: >2,200 lbs payload, road + off-road, keep pace with dismounted soldiers. Unit cost cap: $650K |

Three planned variants (pre-cancellation): RCV-Light (up to 10 tons, rotorcraft-transportable), RCV-Medium, RCV-Heavy (direct fire support).

### S-MET (Small Multipurpose Equipment Transport)

- Increment I: [[General Dynamics]] MUTT selected (2020), squad logistics
- Increment II (2024-27): Two contracts, $22M total (Sep 2024) — American [[Rheinmetall]] Vehicles + [[Textron Systems]], and [[HDT Global]]. 8 prototypes each in 2025. Production contract for up to 2,195 systems planned late FY2027

### Other US programs

| Program | Lead | Detail |
|---------|------|--------|
| ISV Autonomy Kits | [[Overland AI]], [[Forterra]], Scout AI | $15.5M to three startups (Aug 2025). Autonomous driving kits for Infantry Squad Vehicle |
| ATV-S | Carnegie Robotics, [[Forterra]] | Autonomous HEMTT PLS2 trucks |
| NMESIS (Marines) | — | Unmanned anti-ship missile launcher. Fielding begins 2026 |
| ROGUE-Fires (Marines) | [[Forterra]] | Unmanned JLTV for autonomous missile launch, Pacific deployment |

---

## Key platforms

| Platform | Maker | Weight | Payload | Speed | Propulsion | Notes |
|----------|-------|--------|---------|-------|------------|-------|
| THeMIS | [[Milrem Robotics]] | 850 kg | 750-1,200 kg | 50 km/h | Hybrid diesel-electric | 19 nations, 8 NATO. 15 hrs diesel / 90 min silent electric |
| Ripsaw M3 | [[Textron Systems]] | 6,711 kg | 2,268 kg | 48 km/h | Hybrid-electric | Won RCV Phase II. Sweden first European buyer (Dec 2025) |
| Mission Master SP | [[Rheinmetall]] | — | Light | 40 km/h land, 6 km/h water | Electric | Amphibious. 13 provided to US Marines since 2023 |
| Mission Master CXT | [[Rheinmetall]] | — | 1,000 kg | — | Diesel-electric | 450 km range (50 km electric). Amphibious |
| Hunter WOLF | [[HDT Global]] | 1,100 kg | 450 kg | 32 km/h | Hybrid diesel-electric | 100 km range, 72 hrs endurance. UH-60 transportable |
| MUTT / MUTT XM | [[General Dynamics]] | — | — | — | — | Won S-MET I. XM: XM915 20mm gatling + Kongsberg RS6 (AUSA 2025) |
| TRX | [[General Dynamics]] | — | 1:1 payload-to-chassis | — | Hybrid-electric | RCV Phase I. TRX-SHORAD counter-UAS variant |
| ULTRA | [[Overland AI]] | — | — | — | — | Used by 82nd Airborne. Contested logistics, ISR, counter-UAS, breaching |
| HEEMAR | INKAS (Canada) | 285 kg | — | 16 km/h | Electric | Combat-proven in Ukraine: logistics, CASEVAC, kamikaze missions |

---

## Key companies

### Hardware

| Company | HQ | Focus | Status |
|---------|-----|-------|--------|
| [[Milrem Robotics]] | Estonia | THeMIS. 19 nations adopted | Majority owned by UAE's [[EDGE Group]]. ~296 employees |
| [[Textron Systems]] | US | Ripsaw M3 (RCV winner) | Public (parent [[Textron]], NYSE: TXT) |
| [[Rheinmetall]] | Germany | Mission Master family | Public (XETRA: RHM). Also S-MET II competitor |
| [[HDT Global]] | US | Hunter WOLF | Private. S-MET II competitor ($11.55M contract) |
| [[General Dynamics]] | US | MUTT, TRX | Public (NYSE: GD). S-MET I winner |
| [[Oshkosh Defense]] | US | TerraMax autonomy kit, FMAV | Public (parent [[Oshkosh]], NYSE: OSK). 1 operator supervises 5 vehicles |
| [[QinetiQ]] | UK | Titan (THeMIS-based), DragonFire laser | LSE: QQ. $415M R&D (2023). 160M GBP contract (May 2025) |
| Teledyne FLIR | US | PackBot 510/525 (EOD) | Public (parent [[Teledyne]], NYSE: TDY). 4,500+ units deployed |

### Autonomy software (the emerging moat)

| Company | Raised | Valuation | Key program | Notes |
|---------|--------|-----------|-------------|-------|
| [[Forterra]] | $238M Series C (Nov 2025) + more | >$1B | ROGUE-Fires, GEARS, autonomous breaching ($114M) | [[BAE Systems]] partnership for autonomous AMPV. Plans to double production to 1,000 systems |
| [[Overland AI]] | $132M+ ($32M Series A Jan 2025 + $100M in 2026) | — | ULTRA UGV with 82nd Airborne. DARPA RACER completed | Off-road autonomy. Led by [[8VC]], [[Point72 Ventures]] |
| Scout AI | $15M seed | — | Fury foundation model, NOMAD UGV | [[Align Ventures]], [[Booz Allen Ventures]]. Multiple DoD contracts |

---

## International programs

### Israel — "first robotics war"

[[Israel]]'s Gaza operations (2024-25) deployed tens of thousands of autonomous systems:
- Unmanned M113 APCs in Rafah campaign (May 2024)
- Unmanned D9 bulldozers for route-clearing, IED counter
- [[IAI]] Jaguar: semi-autonomous border patrol UGV (7.62mm MAG, 24/7 Gaza border)
- [[IAI]] Rex MK II: semi-autonomous offensive UGV (7.62mm)
- [[Elbit Systems]] M-RCV: automatic target recognition, launches UAVs via robotic arm
- Roboteam ROOK: multi-payload 6x6 (acquired by [[Ondas Holdings]], ONDS, Dec 2025)

### Europe

| Program | Country | Detail |
|---------|---------|--------|
| iMUGS follow-up | EU | 50M EUR under European Defence Fund |
| Project ATILLA | UK | Converting surplus Warrior IFVs into autonomous minefield breaching |
| Project THESEUS | UK | Autonomous last-mile resupply |
| AUROCHS | France | Heavy armed tactical robot (DIA flagged Jul 2025) |
| KUNA | Poland | National UGV program |
| France-Belgium compact UGV | France/Belgium | Renault + John Cockerill Defense. Unveiling Eurosatory 2026 |

### China

| Platform | Type | Notes |
|----------|------|-------|
| Norinco VU-T10 | Heavy UGV tank | Electric, 60 km/h. Trials ongoing |
| ZRY222 | Tracked fire support | ~1.2 tons, 4 guided rockets + 7.62mm. Tested 2025-2026 |
| Norinco 8x8 logistics mule | Supply transport | Forward position resupply |

[[China]] pursuing "complete chain of unmanned warfare equipment" under manned-unmanned teaming doctrine. China UGV market projected $321.5M by 2030.

### Russia

Limited success despite attempts:
- Uran-9: Poor Syria performance (2018) — 300-500m control range, frequent breakdowns
- Marker: Kornet ATGM + drone swarm capability. Serial production announced but no confirmed Ukraine deployment
- Impulse-KPTM: Mine-laying UGV (30 barrels, 120 mines)
- Focus shifted to expendable/simple platforms over sophisticated autonomy

---

## Ukraine lessons

| Metric | Value |
|--------|-------|
| UGVs delivered (2025) | 15,000 (up from 2,000 in 2024) |
| 2026 plan | 20,000+ |
| 3rd Assault Brigade logistics UGV share | 80% |
| Pokrovsk/Myrnorad logistics UGV share | 90% |
| Casualty reduction (General Staff est.) | Up to 30% |
| UGV survivability | 7-8 trips before hit |
| Unit cost | 600-700K UAH ($15,800-18,400) |
| Per-mission cost | $2,000-2,300 |
| Ukrainian manufacturers | 50+ companies, hundreds of variants |

First combined-arms robotic assault: December 2024, 13th KHARTIIA National Guard Brigade — coordinated unmanned surveillance drones, minelaying drones, and armed ground robots.

Key challenge: default analog comms vulnerable to Russian jamming. Digital control conversion underway.

---

## Autonomy levels

| Level | Description | Examples |
|-------|-------------|---------|
| Teleoperated | Human controls all movement | Most EOD robots, early combat UGVs |
| Semi-autonomous | Some independent operations, human guides | IAI Rex MK II, Jaguar |
| Supervisory control | Autonomous navigation, human oversight | THeMIS leader-follower, TerraMax (1 operator, 5 vehicles) |
| Fully autonomous | Independent perception + navigation | DARPA RACER target. [[Overland AI]], [[Forterra]], Scout AI working toward this |

---

## Related

- [[Drone warfare]] — aerial parallel (attritable mass, cost asymmetry)
- [[Drones]] — aerial unmanned sector
- [[Counter-UAS]] — ground-launched C-UAS variants
- [[Defense]] — sector
- [[Software-defined Defense]] — autonomy software as moat
- [[Robotics]] — broader sector
- [[Humanoid robotics]] — commercial parallel
- [[Ukraine war]] — primary proving ground
- [[Forterra]] — autonomy software leader (>$1B)
- [[Overland AI]] — off-road autonomy (82nd Airborne)
- [[Milrem Robotics]] — THeMIS, 19-nation adoption
- [[European defense spending]] — EU iMUGS funding
- [[Long defense AI]] — thesis overlap

---

*Created 2026-04-07*
