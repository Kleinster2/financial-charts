#concept #risk #datacenter #power

Data centers consume more electricity than most countries. Only 16 nations (including US and China) use more power than the global DC fleet. The strain is global and accelerating.

---

## Bloomberg analysis (Jun 2024)

This June 2024 Bloomberg article provides important historical context — the grid strain was already critical **before** the Blackwell ramp.

---

## Scale of the problem

| Metric | Value |
|--------|-------|
| Global data centers (2024) | **>7,000** (up from 3,600 in 2015) |
| Current DC electricity consumption | **508 TWh/year** (> Italy, > Australia) |
| Projected 2034 consumption | **1,580 TWh** (= India) |
| DCs as % of global energy | <2% → **4%** by 2030 (Goldman Sachs) |
| Only 16 nations consume more than DCs | US, China, etc. |

---

## AI is the driver

**[[NextEra Energy]] CEO John Ketchum:** "It's AI" — energy needs for training and inference are "10 to 15 times the amount of electricity" of traditional computing.

| Chip | Power draw |
|------|------------|
| [[NVIDIA]] H100 | **700W** (8x a 60-inch TV) |
| [[NVIDIA]] B100 | **~1,400W** (nearly 2x H100) |

**Ian Buck (Nvidia head of accelerated computing):** "People like to fill their data centers" — efficiency gains won't reduce total demand.

---

## Renewable energy pressure

**Ireland case study:**
- DCs consumed **53%** of Ireland's renewable energy supply (2022)
- Heading to **1/3 of country's total energy** by 2026 (up from 18% in 2022)
- Wholesale power prices **1/3 higher** than rest of Europe
- Dublin moratorium on new DC connections until ~2028

---

## Grid connection backlogs

| Region | Wait time |
|--------|-----------|
| **West London** | Until 2030 |
| **Virginia (Dominion)** | 2-4 years |
| **Texas (ERCOT)** | 1-2 years |
| **Sweden (E.ON SE)** | Queuing for years |

**Bidding wars:** Tech companies competing for sites with ready access to power (NextEra).

---

## DC physical growth

| Metric | 2010 | 2024 |
|--------|------|------|
| Average DC size | ~80K sq ft | **412K sq ft** (**5x** increase) |
| Largest planned | — | **10M sq ft** (2x Mall of America) |

---

## Southeast Asia surge

| Country | DC capacity by 2026 |
|---------|---------------------|
| **Malaysia** | **2,855 MW** (10x increase, mostly Johor) |
| **Singapore** | Imposed moratorium (like Ireland) |
| **Region total** | **153 new DCs**, **5,419 MW** potential |

**Malaysia's problem:** Would exceed country's total renewable output — relies on coal/gas (Tenaga Nasional Berhad).

**"The next Virginia":** Rangu Salgame (Princeton Digital Group) sees Johor as "the next Virginia in the making." PDG went "from shovel to production in 12 months" — building 300 MW in Johor within 2 years.

---

## Utility strain evidence

**[[Dominion Energy]] (Data Center Alley):**
- Connected **94 DCs** consuming **~4 GW** (past 5 years)
- Now fielding requests for multi-GW campuses — 2-3 would match ALL facilities since 2019
- **18 load relief warnings** in spring 2022 alone
- Filed letter to regulators: "far outside of the normal, safe operating protocol"

**Goldman Sachs:** US utilities need **~$50 billion** in new power generation capacity for DCs.

---

## Water-power tradeoff quantified

Water-free cooling methods require **~5% more energy** on average ([[Microsoft]] estimate). Texas heat + water constraints pushing Microsoft and Google toward less efficient closed-loop systems.

---

## Microsoft GPU scaling

| System | Year | GPUs |
|--------|------|------|
| GPT-3 training | 2020 | 10,000 |
| Azure supercomputer | Nov 2023 | 14,400 H100s |
| Next generation | TBD | **30x more powerful** |

---

## Key insight

The problem is self-compounding. Texas offers faster grid connections (1-2 years vs 4+ elsewhere), so DCs concentrate there, but Texas faces water constraints pushing toward water-free cooling which uses **5% more energy**. Every constraint pushes DCs toward trade-offs that worsen other constraints.

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
- [[Microsoft]] — largest player in Texas by megawatt
- [[NVIDIA]] — H100/B100 power consumption
