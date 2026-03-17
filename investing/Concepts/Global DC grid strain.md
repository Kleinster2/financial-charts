---
aliases:
  - DC grid strain
  - data center power crisis
  - DC power crunch
tags:
  - concept
  - risk
  - datacenter
  - power
---

**Global DC grid strain** — data centers consume more electricity than most countries. Only 16 nations (including the US and [[China]]) use more power than the global DC fleet. The strain is global and accelerating.

---

## Synthesis

The DC power constraint is the single hardest bottleneck in the AI buildout — harder than chips, harder than talent. Every geography that becomes a DC hub eventually hits a grid wall: [[Ireland]] (moratorium 2021, conditional reopening Dec 2025), [[Amsterdam]] (moratorium 2019), [[Singapore]] (moratorium), [[Frankfurt]] (new regulations 2022), and parts of [[Virginia]] and [[Texas]] where queue times stretch years. [[McKinsey]] estimates up to a third of global DC demand is unmet.

The emerging response is bifurcating. Regulators are conditioning new approvals on additionality — Ireland's [[CRU]] now requires 80% of DC power from new Irish renewables within six years. Operators are responding with off-grid microgrids (biomethane/HVO) and collocated renewables + DC sites. But the economics don't yet close cleanly: biomethane costs more than natural gas, and operators still want grid connections for demand spikes. The off-grid model solves the regulatory problem but not the cost problem. Whether these workarounds can scale to the ~5.8GW Ireland alone needs — let alone global demand — remains the open question. The constraint is self-compounding: DCs flee to faster-permitting geographies ([[Texas]]), which then hit their own limits (water, grid).

---

## [[Bloomberg]] analysis (Jun 2024)

This June 2024 [[Bloomberg]] article provides important historical context — the grid strain was already critical before the [[Blackwell]] ramp.

---

## Scale of the problem

| Metric | Value |
|--------|-------|
| Global data centers (2024) | >7,000 (up from 3,600 in 2015) |
| Current DC electricity consumption | 508 TWh/year (> [[Italy]], > [[Australia]]) |
| Projected 2034 consumption | 1,580 TWh (= [[India]]) |
| DCs as % of global energy | <2% → 4% by 2030 ([[Goldman Sachs]]) |
| Only 16 nations consume more than DCs | US, [[China]], etc. |

---

## AI is the driver

[[NextEra Energy]] CEO John Ketchum: "It's AI" — energy needs for training and inference are "10 to 15 times the amount of electricity" of traditional computing.

| Chip | Power draw |
|------|------------|
| [[NVIDIA]] [[H100]] | 700W (8x a 60-inch TV) |
| [[NVIDIA]] B100 | ~1,400W (nearly 2x [[H100]]) |

Ian Buck ([[NVIDIA]] head of accelerated computing): "People like to fill their data centers" — efficiency gains won't reduce total demand.

---

## Renewable energy pressure

[[Ireland]] case study:
- DCs consumed 53% of Ireland's renewable energy supply (2022)
- More than 1/5 of country's electricity consumed by DCs; rising to ~1/3 by 2034
- Wholesale power prices 1/3 higher than rest of [[Europe]]
- Tech = 13% of GDP, major corporation tax revenue source — economic incentive to keep DC investment flowing
- 42% of power still from natural gas (2024); Ireland's target is 80% renewables by 2030

CRU moratorium and reversal (2021–2025):
- 2021: [[CRU]] (Commission for Regulation of Utilities) imposed effective moratorium on new DC projects
- Dec 2025: CRU lifted moratorium — new DCs can proceed, but must have 80% of annual power from additional renewable generation in Ireland within 6 years of startup
- CRU highlighted ~5.8GW additional demand capacity needed for the DC sector medium-term
- [[EirGrid]] (grid operator) and [[ESB]] (network operator) expected to detail implementation rules by end of March 2026
- Maurice Mortell (Digital Infrastructure Ireland chair): Ireland is "the canary in the coal mine" for the global DC power crunch

Dublin microgrid wave (Mar 2026):
- [[Pure Data Centres]] ([[UK]], backed by [[Oaktree Capital]]) launched Europe's first off-grid DC microgrid in Dublin — 110MW capacity, enough for 110,000 homes
- Power partner: AVK-SEG. Runs on biomethane with hydrogenated vegetable oil (HVO) as backup
- Gary Wojtaszek (Pure exec chair): "Europe has been energy constrained for a long time. I see this as something that's really going to explode everywhere"
- Five other microgrids being built in Dublin; AVK-SEG working on three. Ben Pritchard (AVK-SEG CEO): "Data won't wait"
- Cost reality: biomethane more expensive than natural gas — DCs still want grid connections for gas at scale, especially for demand swings. Local generation requirements make Dublin metro projects "trickier than people might like to admit" (senior DC executive)

Green energy park model:
- [[Schroders]] Greencoat Renewables invested in first combined renewables + DC site (Drogheda, County Louth, north of Dublin)
- Paul O'Donnell (Schroders Greencoat): even scaling back to 2-3GW of new DCs "is the big economic investment Ireland is going to unlock"

*Source: FT, Jude Webber, Mar 17 2026*

---

## Grid connection backlogs

| Region | Wait time |
|--------|-----------|
| West London | Until 2030 |
| [[Virginia]] ([[Dominion Energy|Dominion]]) | 2-4 years |
| [[Texas]] (ERCOT) | 1-2 years |
| [[Sweden]] ([[E.ON]] SE) | Queuing for years |

Bidding wars: tech companies competing for sites with ready access to power ([[NextEra Energy|NextEra]]).

---

## DC physical growth

| Metric | 2010 | 2024 |
|--------|------|------|
| Average DC size | ~80K sq ft | 412K sq ft (5x increase) |
| Largest planned | — | 10M sq ft (2x Mall of America) |

---

## [[Southeast Asia]] surge

| Country | DC capacity by 2026 |
|---------|---------------------|
| [[Malaysia]] | 2,855 MW (10x increase, mostly Johor) |
| [[Singapore]] | Imposed moratorium (like [[Ireland]]) |
| Region total | 153 new DCs, 5,419 MW potential |

[[Malaysia]]'s problem: would exceed country's total renewable output — relies on coal/gas (Tenaga Nasional Berhad).

"The next Virginia": Rangu Salgame (Princeton Digital Group) sees Johor as "the next Virginia in the making." PDG went "from shovel to production in 12 months" — building 300 MW in Johor within 2 years.

---

## Utility strain evidence

[[Dominion Energy]] (Data Center Alley):
- Connected 94 DCs consuming ~4 GW (past 5 years)
- Now fielding requests for multi-GW campuses — 2-3 would match ALL facilities since 2019
- 18 load relief warnings in spring 2022 alone
- Filed letter to regulators: "far outside of the normal, safe operating protocol"

[[Goldman Sachs]]: US utilities need ~$50 billion in new power generation capacity for DCs.

---

## Water-power tradeoff quantified

Water-free cooling methods require ~5% more energy on average ([[Microsoft]] estimate). [[Texas]] heat + water constraints pushing [[Microsoft]] and [[Google]] toward less efficient closed-loop systems.

---

## [[Microsoft]] GPU scaling

| System | Year | GPUs |
|--------|------|------|
| GPT-3 training | 2020 | 10,000 |
| Azure supercomputer | Nov 2023 | 14,400 [[H100]]s |
| Next generation | TBD | 30x more powerful |

---

## Key insight

The problem is self-compounding. [[Texas]] offers faster grid connections (1-2 years vs 4+ elsewhere), so DCs concentrate there, but [[Texas]] faces water constraints pushing toward water-free cooling which uses 5% more energy. Every constraint pushes DCs toward trade-offs that worsen other constraints.

---

*Source: [Bloomberg - AI Is Already Wreaking Havoc on Global Power Systems](https://www.bloomberg.com/graphics/2024-ai-data-centers-power-grids/) (Jun 21, 2024)*

*Created 2026-01-14*

---

## Related

- [[Power constraints]] — parent concept
- [[DC power prices]] — consumer impact (price increases)
- [[DC power quality]] — consumer impact (harmonics damage)
- [[Water constraints]] — companion constraint
- [[NextEra Energy]] — world's largest wind/solar builder
- [[Dominion Energy]] — utility serving Data Center Alley
- [[Microsoft]] — largest player in [[Texas]] by megawatt
- [[NVIDIA]] — [[H100]]/B100 power consumption
- [[Ireland]] — moratorium reversed Dec 2025, microgrid wave
- [[Oaktree Capital]] — backing [[Pure Data Centres]] microgrids
- [[Schroders]] — Greencoat Renewables investing in DC-adjacent green energy parks
- [[Singapore]] — DC moratorium, [[Southeast Asia]] hub
- [[Malaysia]] — Johor DC buildout, 2,855 MW by 2026
