---
aliases: [Bring Your Own Power, BYOG, Bring Your Own Generation, On-site power generation]
---
#concept #thesis #power #datacenter

**BYOP (Bring Your Own Power)** — Hyperscalers building their own power generation because the grid can't deliver fast enough.

---

## The thesis

Grid power availability is the binding constraint on AI infrastructure buildout. Hyperscalers are responding by generating their own power on-site rather than waiting for utilities.

**The problem:**
- 44GW gap between DC power needed and available grid capacity ([[Morgan Stanley]])
- Utility interconnection takes 3-5+ years
- Grid left them on read

**The solution:**
- Build power generation alongside the datacenter
- Nuclear, gas turbines, or renewables
- "Behind the meter" = faster than grid connection

---

## BYOG: Policy formalization (Jan 2026)

**PJM's "Bring Your Own Generation" proposal formalizes BYOP as policy:**

| Mechanism | Effect |
|-----------|--------|
| **Expedited interconnection** | Fast-track for new capacity that offsets large loads |
| **Curtailment** | New large loads without matching generation subject to curtailment |
| **Capacity auction reform** | June deadline to study long-duration alternatives |

**Why this matters:**
- Regulators now *requiring* BYOP, not just permitting it
- Era of hyperscalers grabbing existing capacity at premium prices is ending
- [[Vistra]], [[Constellation Energy]], [[Talen Energy]] shares fell sharply (Jan 17) on this news
- Meta's Vistra deal (2.6 GW, mostly existing capacity) was poorly timed

**Political context:**
- White House and state governors issued emergency directive
- $15B in 15-year supply contracts to encourage new plants
- [[Consumer]] anger over rising power bills driving action

**Winner:** [[Natural gas]] and grid batteries — can be built fast to satisfy BYOG requirements.

---

## BYOP deals

| Company | Project | Capacity | Strategy |
|---------|---------|----------|----------|
| [[OpenAI]] | UAE Stargate | 1GW | 4x Ansaldo Energia gas turbines |
| [[Meta]] | Socrates South | 200MW+ | Hybrid fleet (Solar/[[Siemens]]/CAT) |
| [[Meta]] | Vistra deal | 2.6GW | 20-yr PPA, 3 nuclear plants (OH/PA) — mostly existing |
| [[Microsoft]] | Constellation | 835MW | TMI nuclear restart |
| [[Amazon]] | Talen Energy | 960MW | [[Susquehanna]] nuclear co-location |
| [[Google]] | [[Kairos Power]] | 500MW | SMR development |
| [[Oracle]] | Nuclear DC | TBD | Nuclear permits ([[Larry Ellison]]) |
| [[xAI]] | Colossus | 2GW | Bitcoin miner partnerships |
| [[Meta]] / [[EdgeConneX]] | Project Walleye (Ohio) | TBD | Island mode -- on-site gas microgrid, first combined DC + power financing ($3B) |

---

## Case study: OpenAI UAE Stargate (Jan 2026)

**Single-vendor approach:**

| Metric | Value |
|--------|-------|
| Turbine | [[Ansaldo Energia]] AE94.3 |
| Quantity | 4 units |
| Gross capacity | 1.3GW |
| Derated capacity | **1GW** (desert heat -23%) |
| Phase 1 | 200MW by YE2026 |
| Status | "Going well" |

**Key insight:** On-site gas turbines = faster than waiting for grid or nuclear. UAE site progressing faster than Texas Abilene.

---

## Case study: Meta Socrates South (Jan 2026)

**Hybrid fleet approach:**

| Equipment | Units | MW each | Total |
|-----------|-------|---------|-------|
| [[Solar Turbines]] [[Titan]] 250 IGT | 3 | 23 MW | 69 MW |
| [[Solar Turbines]] [[Titan]] 130 IGT | 9 | 16.5 MW | 148.5 MW |
| [[Siemens Energy]] SGT-400 IGT | 3 | 14.3 MW | 42.9 MW |
| [[Caterpillar]] 3520 fast-start | 15 | 3.1 MW | 46.5 MW |
| **Gross total** | | | **~307 MW** |

**N+1+1 design** = redundancy, operational capacity 200MW+

**Key insight:** 4 turbine types diversifies supplier risk. Fast-start engines ([[Caterpillar]]) for peaker role, IGTs for baseload.

---

## Single-vendor vs hybrid fleet

| Approach | Example | Pros | Cons |
|----------|---------|------|------|
| **Single-vendor** | OpenAI (Ansaldo) | Simplicity, scale pricing | Supply chain concentration |
| **Hybrid fleet** | Meta (4 vendors) | Diversification, resilience | More complexity |

Both valid strategies — depends on risk tolerance and scale.

---

## Nuclear vs gas for BYOP

| Power source | Timeline | Pros | Cons |
|--------------|----------|------|------|
| **Gas turbines** | 1-2 years | Fast deploy, proven | Carbon emissions, fuel cost |
| **Nuclear (existing)** | 2-3 years | Baseload, carbon-free | Regulatory, limited sites |
| **Nuclear (SMR)** | 5-10 years | Scalable, carbon-free | Unproven at scale |

**Current trend:** Gas turbines for speed, nuclear for long-term.

---

## Alternative power providers

**Filling the BYOP gap (SemiAnalysis):**

| Company | Technology |
|---------|------------|
| [[Ansaldo Energia]] | Gas turbines (Italian) |
| [[Solar Turbines]] (CAT) | Mid-size gas turbines |
| [[GE Vernova]] | Full portfolio |
| [[Siemens Energy]] | Gas + wind |
| Bloom Energy | Fuel cells |
| Doosan Enerbility | Turbines, nuclear |
| Voltagrid | Modular power |

---

## Ratepayer Protection Pledge (Mar 4, 2026)

**Trump formalized BYOP as federal policy** via the [[Ratepayer Protection Pledge]]. Seven hyperscalers ([[Google]], [[Meta]], [[Microsoft]], [[OpenAI]], [[Amazon]], [[Oracle]], [[xAI]]) signed five commitments: pay for all AI power generation, cover grid upgrades, negotiate separate utility rates (paying even for unused capacity), invest in local workforce, and provide backup power to grids.

**Key capacity commitments from the signing:**

| Company | Commitment |
|---------|-----------|
| [[Google]] | 7,800 MW new energy contracted in Texas; acquiring [[Intersect Power]] |
| [[xAI]] | 1.2 GW per data center (and every future DC); orbital data centers in development |
| [[Meta]] | $650M Louisiana ratepayer savings over 15 years |

**Permitting acceleration:** [[Lee Zeldin]] (EPA) issuing permits in 2-3 weeks vs 20+ years historically. Trump claims the idea took 6 months to convince companies ("they thought I was kidding").

**Structural critique:** Paying for generation doesn't build it faster. Natural gas plants still take years regardless of permit speed. The political cover for communities (no rate increases guaranteed by CEO signatures) may be more immediately impactful than the power commitments themselves.

---

## Overbuilding risk (Mar 2026)

David Crane (CEO, [[Generate Capital]], $8B AUM, former under-secretary for infrastructure under Biden, former CEO of [[NRG Energy]]) warned that on-site power plants for data centers risk being overbuilt (FT, Mar 31 2026).

Crane (Mar 31): *"As much as the data centre people tell you their demand for electricity is infinite, it feels to me like there will be a time when they'll be overbuilt. They're going to have spare electrons."*

*"Someone's got to pay for the infrastructure that's put in place and then not being used . . . you need to have take-or-pay contracts, so if they suddenly don't need the power, it's on the back of the data centre company, not the power company."*

Three drivers of potential overcapacity:
- On-site plants must be oversized for reliability (N+1 redundancy). Once the data center gets grid connection, the excess generation has no buyer
- AI chips getting more efficient could reduce per-rack power draw
- Quantum computing breakthroughs could reduce compute power requirements

Ben Hertz-Shargel (global head of grid edge, [[Wood Mackenzie]], Mar 31): *"The AI ship has sailed, but the energy cost of serving it is very much in question."*

Crane's counterpoint: overbuilding could be an "opportunity" if planned for — underused plants could be integrated back into the grid to boost supply for regular customers and bring down prices.

Demand backdrop: [[BloombergNEF]] estimates US data center power demand surges from 34.7 GW (2024) to 106 GW by 2035. Utility capex plans up 19% for 2026-2030 (Wolfe Research). [[NextEra Energy]] alone planning 15 GW of new plants for data centers over next 9 years.

*Source: FT, Martha Muir (New York), Mar 31 2026*

---

## Investment implications

**Power suppliers win:**
- Gas turbine makers ([[GE Vernova]], [[Siemens Energy]])
- Nuclear operators ([[Constellation Energy]], [[Vistra]])
- Equipment providers ([[Bloom Energy]])

**Hyperscalers bear risk:**
- Massive upfront capex for power
- Operating expense (fuel, maintenance)
- Regulatory exposure

**Semi implications:**
- GPUs can ship before power is ready
- Creates [[GPU deployment bottleneck]]
- Revenue quality questions for [[NVIDIA]]

---

## Quick stats

| Metric | Value |
|--------|-------|
| Grid gap | 44GW (US 2025-28) |
| OpenAI UAE | 1GW (gas) |
| Meta Socrates | 200MW+ (hybrid) |
| Microsoft TMI | 835MW (nuclear) |
| Amazon Talen | 960MW (nuclear) |

*Updated 2026-04-04*

---

## Related

- [[Power constraints]] — broader thesis (44GW gap)
- [[Nuclear power for AI]] — nuclear BYOP strategy
- [[AI datacenter architecture]] — design patterns
- [[GPU deployment bottleneck]] — consequence (shipped ≠ deployed)
- [[OpenAI]] — UAE Stargate (1GW)
- [[Meta]] — Socrates South (200MW+)
- [[Microsoft]] — Constellation TMI restart
- [[Amazon]] — Talen nuclear co-location
- [[Google]] — [[Kairos Power]] SMR
- [[xAI]] — Colossus (crypto miner power)
- [[Ansaldo Energia]] — gas turbine supplier
- [[Solar Turbines]] — gas turbine supplier
- [[GE Vernova]] — power equipment
- [[Siemens Energy]] — power equipment
- [[Constellation Energy]] — nuclear operator
- [[Vistra]] — Texas power
- [[Generate Capital]] — David Crane overbuilding warning (Mar 2026)
- [[EdgeConneX]] — Project Walleye operator ([[EQT]], first combined DC + power financing)
- [[DC power prices]] — ratepayer impact of DC demand
- [[Global DC grid strain]] — grid queue crisis driving BYOP adoption (UK: 125 GW queue, 8-10 yr waits)
- [[Ratepayer Protection Pledge]] — Trump's take-or-pay formalization
