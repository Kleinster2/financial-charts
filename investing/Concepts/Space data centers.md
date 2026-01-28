#concept #speculative #datacenter #space

**[[Space]] data centers** — Orbital computing infrastructure to bypass Earth's power/land constraints. Multiple billionaires pursuing. Economically unviable today but serious R&D underway.

---

## Why space?

| Constraint on Earth | [[Space]] solution |
|---------------------|----------------|
| **Power grid strain** | 24/7 solar (sun-synchronous orbit) |
| **Land scarcity** | Unlimited orbital real estate |
| **Permitting delays** | FAA + FCC bulk licenses (2 applications) |
| **Grid connection** | 7+ year waits in Northern Virginia | Self-powered |
| **NIMBY opposition** | No neighbors in orbit |

**Phil Metzger (UCF):**
> "If you can get a bulk launch license from the FAA and a bulk constellation license from the FCC, that's just two applications — then you can build thousands of data centers."

---

## Key players

| Player | Initiative | Scale | Timeline |
|--------|------------|-------|----------|
| **[[SpaceX]]** | Starship-launched network | **100GW** combined | 4-5 years (Musk) |
| **[[Blue Origin]]** | Bezos DC vision | — | 10-20 years (Bezos) |
| **Eric Schmidt** | Acquired [[Relativity Space]] | — | — |
| **[[Google]]** | Project Suncatcher | 2 prototype satellites | Early 2027 |
| **[[Starcloud]]** | [[NVIDIA]]-backed | **5GW** single DC | — |
| **[[Axiom Space]]** | ISS replacement + DC | — | — |
| **[[China]]** | AI supercomputer test | Proof of concept | Deployed |

**SpaceX advantage:** [[Starlink]] experience (9,300+ satellites), Starship development, vertical integration.

---

## Scale comparison

| Facility | Capacity | Size |
|----------|----------|------|
| [[OpenAI]] Stargate (Abilene) | 1.2 GW | 4M sq ft |
| [[Starcloud]] orbital DC | **5 GW** | **4km × 4km** solar panels |
| Musk's vision | **100 GW** | Satellite network |

[[Starcloud]]'s 5GW = 4x Stargate, requires solar panels 2.5 miles wide.

---

## Engineering challenges

### Solar panels

| Challenge | Detail |
|-----------|--------|
| Scale | 4km × 4km for 5GW |
| Launch | Won't fit on current rockets |
| Deployment | Must unfurl in orbit |
| Debris risk | Large surface = more collisions |
| Control | Difficult to maneuver |

### Cooling

**No air or water in space — only option is radiators:**

| Factor | Challenge |
|--------|-----------|
| Heat rejection | Via infrared radiation only |
| Earth blocking | Earth fills half the sky in LEO |
| Sun avoidance | Radiators must point away from both |
| Constant movement | Must reorient every 90 minutes |

**Jason Wright (Penn State):**
> "You have to cool upwards into space, because the Earth itself is warm. If you're in low-Earth orbit, Earth fills up half your sky."

### Cosmic rays

- High-energy particles damage electronics
- Requires radiation hardening
- Adds weight and cost
- Reduces chip performance

### Latency

| Orbit | Latency |
|-------|---------|
| Low Earth Orbit | ~20-40ms (similar to ground) |
| High orbit (likely for DCs) | **Up to 3 seconds** |

High orbits needed to avoid congestion but add significant delay.

### Repairs

- No technicians in space
- Modular design required
- Robotic satellite swaps for repairs
- Higher failure tolerance needed

---

## Launch economics

**Depends on [[SpaceX]] Starship:**

| Factor | Status |
|--------|--------|
| Full reusability | Not yet achieved |
| 2025 testing | Multiple unplanned explosions |
| Satellite deployment | Demonstrated |
| Orbital mission | Not yet completed |
| Cost target | $10/kg to orbit (vs $2,700 today) |

**Reality:** Starship is years from reliable, cheap operation. [[Space]] DCs depend on this breakthrough.

---

## Timeline estimates

| Source | Estimate | Context |
|--------|----------|---------|
| **[[Elon Musk]]** | 4-5 years | "If we can solve the other parts" |
| **[[Jeff Bezos]]** | 10-20 years | "I bet it's not more than 20 years" |
| **Consensus** | Unknown | "Remain in realm of science fiction far longer" |

**Phil Metzger:** "I don't think there's any new physics involved, but there's going to need to be a lot of technical maturity."

---

## Google Project Suncatcher

**Most concrete near-term initiative:**

| Detail | Value |
|--------|-------|
| Announced | November 2025 |
| Partner | Planet (satellite company) |
| Goal | Technology development for space AI computing |
| Timeline | 2 prototype satellites by early 2027 |

---

## SpaceX IPO connection

**$30B+ IPO (2026) partly to fund space DCs:**

| Factor | Detail |
|--------|--------|
| IPO size | $30B+ |
| Purpose | Starship development, space DCs |
| Advantage | [[Starlink]] experience (9,300+ satellites) |
| Strategy | Repurpose [[Starlink]] technology |

---

## Investment implications

**Today:** No direct investment — all private or speculative.

**Watch for:**
- SpaceX IPO (2026) — most direct exposure
- Relativity [[Space]] (Schmidt-backed)
- Axiom [[Space]]
- NVIDIA ([[Starcloud]] backer)
- Satellite component suppliers

**If viable:**
- Disrupts terrestrial DC buildout
- Changes [[Power constraints]] calculus
- New category of space infrastructure

**If not:**
- Ground-based constraints remain binding
- Nuclear/gas [[BYOP]] continues
- Geographic arbitrage (Middle East, Nordics)

---

## Related

- [[Power constraints]] — problem space DCs aim to solve
- [[SpaceX]] — leading player, Starship dependency
- [[Blue Origin]] — Bezos vision
- [[NVIDIA]] — [[Starcloud]] backer
- [[Google]] — Project Suncatcher
- [[AI hyperscalers]] — potential customers
- [[GPU deployment bottleneck]] — related constraint

*Created 2026-01-15*
