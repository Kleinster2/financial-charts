---
aliases: [Counter-drone, Counter-UAS, C-UAS, CUAS, counter-sUAS, anti-drone]
tags: [concept, defense, drones, technology]
---

# Counter-UAS

Technologies and systems that detect, track, identify, and neutralize unauthorized or hostile unmanned aerial systems. The mirror image of [[Drone warfare]] — every drone capability creates counter-drone demand, and the cost asymmetry between cheap attack drones and expensive interceptors is the defining problem of modern air defense.

---

## Synthesis

The counter-UAS market is growing at ~25% CAGR because the drone threat is growing faster than defenses. A $500 FPV drone forced a US Navy destroyer to fire a $2.1M SM-2 missile in the Red Sea. [[Iran]]'s [[Shahed-136]] costs $20-35K; intercepting one costs $500K-$15M. The math doesn't work at scale — the US cannot shoot $4M PAC-3 missiles at $500 drones. Three solutions are converging: directed energy (near-zero marginal cost per shot), cyber takeover (non-kinetic, no collateral damage), and interceptor drones (cost-matched kinetic). The companies that solve the cost equation win the market. [[Rafael]]'s [[Iron Beam]] (~$2-3/shot) and [[Epirus]]'s Leonidas (defeats entire swarms simultaneously) represent the directed-energy frontier. Ukraine's STING drone (~$2,000/unit, 3,000+ Shahed kills) represents the kinetic low-cost frontier.

The US FY2026 budget requests $3.187B for Combating Uncrewed Systems (+$940M over FY2025). The FY2026 NDAA created JIATF-401, a new joint task force with procurement veto power over all C-sUAS purchases — centralizing a market that was previously fragmented across services.

---

## The cost asymmetry problem

| Threat | Cost | Interceptor | Cost | Ratio |
|--------|------|-------------|------|-------|
| FPV drone | ~$500 | SM-2 missile | $2.1M | 4,200:1 |
| [[Shahed-136]] | $20-35K | PAC-3 MSE | $4-12M | 115-600:1 |
| Commercial quadcopter | ~$1K | Coyote Block 2 | $100-200K | 100-200:1 |
| Drone swarm (50 units) | ~$25K | Traditional SHORAD salvo | $5-10M+ | 200-400:1 |

This is the fundamental market driver: conventional air defense economics invert when the threat costs less than the interceptor.

---

## Segments

### Detection

Radar held 56.1% of the detection market in 2024.

| Method | Strengths | Limitations |
|--------|-----------|-------------|
| RF analysis | Detects controller signals, locates operator | Fails on autonomous drones (no signal) |
| Radar | Long range, all-weather | Struggles with small, low-flying targets; clutter |
| Acoustic | Passive, hard to counter | Degrades in noisy environments, short range |
| Electro-optical / IR | Visual ID, classification | Limited by weather, lighting; labor-intensive |
| Multi-sensor fusion | Combines strengths of all above | Complexity, cost, integration challenge |

### Defeat / neutralization

| Method | How it works | Players | Cost per engagement |
|--------|-------------|---------|---------------------|
| RF jamming | Disrupts control/GPS link | [[L3Harris]] (CORVUS-RAVEN), [[Hensoldt]] (XPELLER) | Near-zero (electricity) |
| Cyber takeover | Protocol-level hijack, controlled landing | [[D-Fend Solutions]] (EnforceAir) | Near-zero |
| Directed energy — laser | Burns optics/structure | [[Rafael]] ([[Iron Beam]], 100kW), [[RTX]] (HELWS, 10-50kW) | ~$2-3/shot (Iron Beam) |
| Directed energy — HPM | Fries electronics, defeats swarms simultaneously | [[Epirus]] (Leonidas) | Near-zero per burst |
| Kinetic interceptor | Missile or projectile | [[RTX]] (Coyote, $100-200K), [[Anduril]] (Roadrunner, ~$500K reusable) | $100K-$500K |
| Interceptor drone | Drone-on-drone | Ukraine STING (~$2K), [[L3Harris]] (VAMPIRE) | $2-50K |

---

## Market size

| Source | 2025 | 2030/2035 | CAGR |
|--------|------|-----------|------|
| MarketsandMarkets | $6.64B | $20.31B (2030) | 25.1% |
| BIS Research | $4.93B | $36.42B (2035) | 22.1% |
| Precedence Research | — | $19.06B (2035) | — |
| Market.us | — | — | 27.9% |

AI-enhanced autonomous C-UAS subsegment: $600M (2025) to $2.7B (2030), ~35% CAGR.

US FY2026 C-UxS budget: $3.187B requested (+$940M over FY2025 enacted).

---

## Key players

### Detection specialists

| Company | Product | Status | Notes |
|---------|---------|--------|-------|
| [[Dedrone]] (now [[Axon]]) | DedroneBeyond sensor fusion | Acquired Oct 2024 (~$209M) | DHS-approved for anti-terrorism. 30+ countries, 190+ critical infrastructure sites, 30+ airports. Pre-acquisition: $27.3M revenue (2023), 696% 3-year growth |
| [[DroneShield]] | DroneOptID, RfPatrol, DroneGun, DroneCannon | ASX: DRO. A$3.58B market cap (Apr 2026) | FY2025: A$216.5M revenue (+277%), first full-year profit. A$2.09B pipeline (300+ deals) |
| [[D-Fend Solutions]] | EnforceAir (cyber takeover) | Private. $59M+ total funding | RF cyber-takeover — commandeers drone for safe landing. 60%+ YoY revenue growth. ~30 countries including Five Eyes, G7 |
| [[Hensoldt]] | XPELLER, SPEXER 2000 radar | Frankfurt-listed | Supplies radar to [[Rheinmetall]] Skyranger 30. "High three-digit million" framework. Jan 2026: TYTAN Technologies C-UAS partnership |

### Defeat / effector systems

| Company | Product | Status | Notes |
|---------|---------|--------|-------|
| [[Epirus]] | Leonidas HPM | Private. $1.4B valuation. ~$595M raised | Solid-state high-power microwave. Defeated 49-drone swarm in single burst (2025 demo). $43.55M Army IFPC-HPM Gen II contract (Jul 2025). 236 employees |
| [[RTX]] | Coyote Block 2/3NK, HELWS laser | NYSE: RTX | $5.04B Army contract (Sep 2025) for Coyote + KuRFS radars (through 2033). Coyote Block 3NK: non-kinetic swarm defeat |
| [[Rafael]] | [[Iron Beam]] (Or Eitan), Drone Dome | Israeli state-owned | Iron Beam: 100kW laser, ~$2-3/shot. Operational delivery Dec 30, 2025. First combat use Mar 2, 2026. Drone Dome: modular C-UAS (radar + jamming + laser) |
| [[L3Harris]] | VAMPIRE, CORVUS-RAVEN | NYSE: LHX | VAMPIRE: palletized ISR/rocket system, combat-proven since 2023. Black Wake (maritime), Bat (facilities), EW variants. High-volume production ramped Mar 2026 (Huntsville, AL) |
| [[Anduril]] | Lattice C2, Roadrunner interceptor | Private. ~$14B | $20B 10-year Army enterprise agreement (Mar 2026). First task order: $87M for Lattice as JIATF-401 counter-drone C2. Roadrunner: reusable VTOL interceptor, $250M/500 units (Oct 2024, ~$500K/unit) |

### Directed energy — the cost solution

| System | Type | Power | Cost/shot | Status |
|--------|------|-------|-----------|--------|
| [[Iron Beam]] ([[Rafael]]) | Laser | 100kW | ~$2-3 | Operational Dec 2025, first combat Mar 2, 2026 |
| Leonidas ([[Epirus]]) | HPM | Classified | Near-zero | Army IFPC-HPM Gen II. Defeats swarms simultaneously |
| HELWS ([[RTX]]) | Laser | 10-50kW | Near-zero | Multiple variants. UK palletized version in development |
| IFPC-HEL ([[Lockheed Martin]]) | Laser | 300kW (target) | Near-zero | Reduced to single prototype. Final lab testing |

---

## Key US programs

| Program | Authority | Role |
|---------|-----------|------|
| JIATF-401 | FY2026 NDAA (Dec 18, 2025) | Joint task force under Deputy SecDef. Procurement veto on all C-sUAS purchases. Commercial Solutions Opening launched Feb 2026 |
| JCO (predecessor) | Est. Feb 2020, Army G-3/5/7 | Counter-swarm demos (2025). Being absorbed into JIATF-401 |
| LIDS | Army primary C-UAS | FY2025 NDAA directed additional kinetic effector procurement |
| Replicator 2 | DIU + JCO | Low-collateral defeat options for joint force |
| SAFER SKIES Act | FY2026 NDAA | Gives state/local law enforcement C-UAS authority. $250M FEMA to 11 states for FIFA 2026 |

---

## Regulatory drivers

- FAA receives 100+ monthly reports of drones near airports
- Pending House bill would require FAA "Office of Counter-UAS Activities" with minimum performance requirements within 270 days
- DHS established new office to combat drone/counter-drone threats
- SAFER SKIES Act (Dec 2025): state/local law enforcement can detect, track, seize, disable, or destroy threatening drones over critical infrastructure, prisons, major events

---

## Related

- [[Drone warfare]] — the threat driving this market
- [[Drones]] — sector hub
- [[Dedrone]] — detection leader (now [[Axon]])
- [[Epirus]] — directed energy (Leonidas HPM)
- [[DroneShield]] — ASX-listed detection + defeat
- [[D-Fend Solutions]] — cyber takeover
- [[Iron Beam]] — [[Rafael]] 100kW laser, first operational DE C-UAS
- [[Anduril]] — Lattice C2 + Roadrunner interceptor
- [[RTX]] — Coyote + HELWS laser
- [[L3Harris]] — VAMPIRE family
- [[Hensoldt]] — XPELLER, radar
- [[Golden Dome]] — domestic air defense context
- [[Defense]] — sector
- [[Software-defined Defense]] — AI/autonomy overlap
- [[Long defense AI]] — thesis overlap

---

*Created 2026-04-07*
