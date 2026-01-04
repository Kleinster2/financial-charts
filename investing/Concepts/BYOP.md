---
aliases: [Bring Your Own Power, On-site power generation]
---
#concept #thesis #power #datacenter

**BYOP (Bring Your Own Power)** — Hyperscalers building their own power generation because the grid can't deliver fast enough.

---

## The thesis

Grid power availability is the binding constraint on AI infrastructure buildout. Hyperscalers are responding by generating their own power on-site rather than waiting for utilities.

**The problem:**
- 44GW gap between DC power needed and available grid capacity (Morgan Stanley)
- Utility interconnection takes 3-5+ years
- Grid left them on read

**The solution:**
- Build power generation alongside the datacenter
- Nuclear, gas turbines, or renewables
- "Behind the meter" = faster than grid connection

---

## BYOP deals

| Company | Project | Capacity | Strategy |
|---------|---------|----------|----------|
| [[OpenAI]] | UAE Stargate | 1GW | 4x Ansaldo Energia gas turbines |
| [[Meta]] | Socrates South | 200MW+ | Hybrid fleet (Solar/Siemens/CAT) |
| [[Microsoft]] | Constellation | 835MW | TMI nuclear restart |
| [[Amazon]] | Talen Energy | 960MW | Susquehanna nuclear co-location |
| [[Google]] | Kairos Power | 500MW | SMR development |
| [[Oracle]] | Nuclear DC | TBD | Nuclear permits (Larry Ellison) |
| [[xAI]] | Colossus | 2GW | Bitcoin miner partnerships |

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
| [[Solar Turbines]] Titan 250 IGT | 3 | 23 MW | 69 MW |
| [[Solar Turbines]] Titan 130 IGT | 9 | 16.5 MW | 148.5 MW |
| [[Siemens Energy]] SGT-400 IGT | 3 | 14.3 MW | 42.9 MW |
| Caterpillar 3520 fast-start | 15 | 3.1 MW | 46.5 MW |
| **Gross total** | | | **~307 MW** |

**N+1+1 design** = redundancy, operational capacity 200MW+

**Key insight:** 4 turbine types diversifies supplier risk. Fast-start engines (Caterpillar) for peaker role, IGTs for baseload.

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

*Updated 2026-01-04*

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
- [[Google]] — Kairos Power SMR
- [[xAI]] — Colossus (crypto miner power)
- [[Ansaldo Energia]] — gas turbine supplier
- [[Solar Turbines]] — gas turbine supplier
- [[GE Vernova]] — power equipment
- [[Siemens Energy]] — power equipment
- [[Constellation Energy]] — nuclear operator
- [[Vistra]] — Texas power
