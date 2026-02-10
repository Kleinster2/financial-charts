---
aliases: [Off-road AV, Off-highway autonomy, Autonomous construction]
---
#concept #robotics #ai #construction #defense

Off-road autonomy -- applying autonomous vehicle technology (perception, planning, control) to unstructured environments beyond paved roads: construction sites, mines, oilfields, forestry, and military terrain. The common thread is AV tech transfer from highway driving to environments without lane markings, traffic signals, or predictable surfaces.

---

## Why it matters

Most off-road autonomy companies use a retrofit approach -- adding sensors and compute to existing equipment rather than building new machines. This lowers the capital barrier and lets contractors upgrade fleets they already own.

Two primary demand drivers:

1. Labor shortage -- the construction industry alone needs ~349K new workers in 2026 (Associated Builders and Contractors). Autonomous equipment operates through shifts no human wants to fill.
2. Military force protection -- removing troops from harm's way during logistics, resupply, and route clearance. Force multiplication without additional headcount.

---

## Market sizing

| Metric | Value | Source |
|--------|-------|--------|
| Autonomous construction equipment market (2023) | $8.8B | Industry estimates |
| Growth rate | 7.5%+ annually | Industry estimates |
| Built environment tech funding (Q3 2025) | $4.4B | 66% YoY increase |
| US construction worker shortfall (2026) | ~349K | Associated Builders and Contractors |
| Cumulative infrastructure investment needed by 2040 | $106T | McKinsey |

---

## Approaches

| Approach | Description | Companies |
|----------|-------------|-----------|
| Full autonomy (retrofit) | Sensor/compute kits on existing equipment, no operator needed | [[Built Robotics]], [[SafeAI]], [[Bedrock Robotics]] |
| Human-alongside | Machine assists operator, adaptive control, ~30% productivity gains | [[Gravis Robotics]] |
| Supervised autonomy / teleop | Remote operators control machines from anywhere | [[Teleo]] |
| Military ground autonomy | Autonomous convoy, resupply, route clearance for defense | [[Forterra]], [[Overland AI]] |
| Dual-use (highway + off-road) | AV tech applied to both trucking and industrial environments | [[Kodiak AI]] |

---

## Key companies

| Company | Focus | Total raised | HQ |
|---------|-------|--------------|----|
| [[Bedrock Robotics]] | Construction retrofit, excavators/bulldozers | $350M+ | San Francisco |
| [[Built Robotics]] | Solar construction, excavator "exosystem" | $112M | San Francisco |
| [[Gravis Robotics]] | Human-alongside excavator retrofit | $23M | Zurich |
| [[SafeAI]] | Mining and construction retrofit | $64M+ | Santa Clara |
| [[Teleo]] | Teleoperation of heavy equipment | $28.35M | Palo Alto |
| [[Forterra]] | Military autonomous ground vehicles | $263M+ | Clarksburg, MD |
| [[Overland AI]] | Defense off-road autonomy | $100M | Seattle |
| [[Kodiak AI]] | Autonomous trucking + oilfield | Public (KDK) | — |

---

## Tech stack overlap with on-road AV

The perception-planning-control stack from highway AV transfers to off-road, but with key differences:

| Layer | On-road | Off-road |
|-------|---------|----------|
| Perception | Lane markings, traffic signs, vehicles | Terrain classification, obstacle detection in dust/mud |
| Planning | Route following, traffic rules | Dig plans, grade targets, terrain traversability |
| Control | Steering, acceleration | Hydraulic actuators, bucket/blade control |
| Environment | Structured, mapped | Unstructured, constantly changing |

[[Bedrock Robotics]] and [[Forterra]] both draw founding teams from [[Waymo]], illustrating the direct tech transfer pipeline.

---

## Related

Actors:
- [[Bedrock Robotics]] -- largest-funded construction autonomy startup ($350M+, $1.75B valuation)
- [[Built Robotics]] -- pioneer in autonomous excavation, shifted to solar
- [[Gravis Robotics]] -- ETH Zurich spinout, human-alongside approach
- [[SafeAI]] -- mining and construction, global offices
- [[Teleo]] -- supervised autonomy / teleoperation model
- [[Forterra]] -- defense ground autonomy, $1B+ valuation
- [[Overland AI]] -- defense off-road autonomy, DARPA RACER graduate
- [[Kodiak AI]] -- dual highway/oilfield autonomy, public via SPAC
- [[Waymo]] -- origin of much of the founding talent in this space

Concepts:
- [[Robotics]] -- broader sector
- [[Humanoid robotics inflection]] -- different form factor, same labor shortage driver

---

*Created 2026-02-10*
