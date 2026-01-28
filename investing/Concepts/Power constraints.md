#concept #risk #datacenter #power

Data center power availability is emerging as a hard constraint on AI infrastructure buildout.

---

## PJM BYOG proposal (Jan 2026)

**PJM releases "Bring Your Own Generation" proposal:**

| Element | Details |
|---------|---------|
| **Expedited interconnection** | Fast-track for new capacity that offsets large loads |
| **Curtailment** | New large loads without matching generation subject to curtailment |
| **Capacity auction reform** | June deadline to study long-duration alternatives |
| **Emergency auction** | White House/governors directive for 15-year hyperscaler contracts |

**Trigger:** Week of whiplash — PJM first cut demand forecasts, then released BYOG proposals after political pressure from Trump and state governors.

**PJM forecast changes (Jan 2026):**
- Near-term (through 2032): slightly lower
- Long-term: raised significantly
- Cut (~4.5 GW) still less than capacity auction shortfall (~6.5 GW)

**White House response:**
- Emergency auction for $15B in 15-year supply contracts
- Only ~6-7 GW new capacity vs ~40 GW needed by early 2030s
- More political signal than solution

**CreditSights warning:** US grid-connection requests >2x consensus datacenter demand forecast — bubble forming?

**Implications:**
- Era of hyperscalers grabbing existing capacity at premium prices may be ending
- [[Vistra]], [[Constellation Energy]], [[Talen Energy]] shares fell sharply (Jan 17)
- Big Tech must bring new generation, not commandeer existing grid
- Grid batteries should benefit alongside natural gas

*Source: Bloomberg Opinion (Liam Denning), Jan 19 2026*

---

## The gap ([[Morgan Stanley]], Dec 2025)

| Metric | Value |
|--------|-------|
| US DC power needed 2025-28 | 69GW |
| Self-generated (DCs under construction) | 10GW |
| Available grid capacity | 15GW |
| **Shortfall** | **44GW** |

44GW = output of ~44 nuclear power plants.

---

## Cost to close

| Component | Cost |
|-----------|------|
| Power generation ($60B/GW × 44) | $2.6T |
| Data center buildout | ~$2T |
| **Total** | **~$4.6T** |

---

## Timeline and response

This isn't new — hyperscalers and neoclouds were already reducing expansion plans 18-24 months ago.

**No line of sight** to solving it in US/[[Europe]]:
- Too slow to build
- Too much red tape
- Growing gap to demand

---

## BYOP (Bring Your Own Power)

The new paradigm — hyperscalers securing their own power:

| Company | Strategy |
|---------|----------|
| [[xAI]] | Bitcoin miner partnerships ([[TeraWulf]], [[Cipher Mining]]) |
| [[Microsoft]] | [[Constellation Energy]] nuclear restart |
| [[Amazon]] | Talen Energy nuclear co-location |
| [[Google]] | [[Kairos Power]] SMR development |
| [[Oracle]] | Nuclear DC permits ([[Larry Ellison]]) |
| [[Talen Energy]] | Amazon [[Susquehanna]] co-location |
| [[OpenAI]] | On-site gas turbines (UAE Stargate) |
| **[[Meta]]** | Hybrid turbine fleet (Socrates South, 200MW+) |

**OpenAI UAE Stargate example (Jan 2026):**
- 4x [[Ansaldo Energia]] AE94.3 gas turbines
- 1.3GW gross → 1GW derated (desert heat penalty -23%)
- Phase 1: 200MW by YE2026
- "Going well" vs Texas Abilene "not going BRRR"

**Meta Socrates South example (Jan 2026):**
- Hybrid fleet: [[Solar Turbines]], [[Siemens Energy]], [[Caterpillar]]
- ~307MW gross → 200MW+ operational (N+1+1 redundancy)
- 4 different turbine/engine types — diversified supplier approach
- See [[Meta]] for full breakdown

**Alternative providers filling the gap** (SemiAnalysis, Dec 2025):
- Bloom Energy — fuel cells
- Doosan Enerbility — turbines, nuclear
- Voltagrid — modular power
- **Ansaldo Energia** — gas turbines (Italian)

> "The grid left them on read" — hyperscalers turning to alternatives because utilities can't deliver.

---

## [[Nuclear renaissance]]

See [[Nuclear power for AI]] for details.

**Why nuclear:**
- Baseload 24/7 (AI training runs continuously)
- Density (1GW on small footprint)
- Carbon-free ([[ESG]] commitments)
- Long-term PPAs match DC investment

**Key deals:**
| Deal | Capacity |
|------|----------|
| Microsoft + Constellation (TMI restart) | 835 MW |
| Amazon + Talen ([[Susquehanna]]) | 960 MW |
| Google + [[Kairos Power]] (SMR) | 500 MW |

**Players:** [[Constellation Energy]], [[Vistra]], [[Oklo]], [[Cameco]], [[Centrus Energy]]

---

## Hyperscaler commitments (Dec 2025)

| Company | New capacity | Investment |
|---------|--------------|------------|
| [[Amazon]] | 3.7 GW | $65B+ (Indiana expansion + govt) |
| [[xAI]] | ~2 GW | Colossus 1-3 (Memphis) |

These represent partial offsets to the 44GW gap, but most capacity won't come online until 2026-2028.

---

## Mitigating factors

### Efficiency technologies

| Technology | Efficiency gain |
|------------|-----------------|
| **[[NPU]] inference chips** | **2-4x** perf/watt |
| Photonic interconnects | 2-4x |
| More efficient cooling | 0.3-0.4x power draw |
| Advanced nodes ([[TSMC]]) | Better perf/watt |
| Quantization (INT8, INT4) | 2-4x memory/compute savings |

**But not nearly enough to close the 44GW demand gap.**

### Inference efficiency: The rising solution

**The thesis:** Training happens once. Inference runs forever. Power efficiency for inference = ongoing cost savings.

**NPU pioneers:**

| Company | Chip | Perf/watt vs GPU | Status (Jan 2026) |
|---------|------|------------------|-------------------|
| [[FuriosaAI]] | RNGD | **2-3x better** | Mass production Jan 2026 |
| [[Groq]] | LPU | ~2x better | Acquired by [[NVIDIA]] (Dec 2025) |
| Amazon | Inferentia 2 | ~2x better | Production |
| Google | TPU v5e | Inference variant | Production |

**FuriosaAI example (Jan 2026):**
- RNGD: TSMC 5nm, 48GB HBM3, **150W TDP** (vs H100 350W)
- Hot Chips 2024: 3x better perf/watt vs H100 on [[Llama]]
- LG AI Research: commercial deployment for EXAONE models
- Meta tried to acquire for $800M — declined

**Why this matters for power constraints:**
- 10MW datacenter with 2x efficient chips = effective 20MW compute
- Or: same compute at half the power/cooling cost
- Location flexibility (can build where power is tighter)

**The Groq lesson:** NVIDIA's $20B acquisition (Dec 2025) shows they take inference efficiency seriously enough to absorb competitors rather than compete.

See [[NPU]] for technical details on how inference chips achieve efficiency.

---

## Geographic winners

Power availability will drive DC location decisions:

| Region | Advantage |
|--------|-----------|
| **Tennessee/TVA** | xAI Colossus (TVA power) |
| **Texas (ERCOT)** | [[Vistra]] nuclear + gas |
| **Pennsylvania** | TMI restart, [[Susquehanna]] |
| **Middle East** | Cheap gas, sovereign wealth |
| **Nordics** | Hydro, cheap power |

---

## [[China]]'s power advantage

**The asymmetry:**

| Constraint | US | [[China]] |
|------------|-----|-------|
| **GPU access** | Abundant (Blackwell) | Constrained (H200 only) |
| **Power access** | Constrained (44 GW gap) | Abundant |
| **Permitting** | Years of red tape | State-directed, fast |
| **Buildout pace** | Slow | 212 GW solar added in 2024 alone |

**[[China]]'s edge:**
- 212 GW solar installed in one year (vs US ~30 GW)
- 253 GW planned for desert regions
- State-directed = no permitting delays
- Grid expansion keeps pace with demand

**Implication:** Chinese AI labs ([[ByteDance]], [[Baidu]], [[Alibaba]], [[Tencent]]) face GPU constraints but not power constraints. They can build massive clusters of older-gen chips without hitting power walls.

**The trade-off:**
- US: Best chips, can't power them
- [[China]]: Abundant power, can't get best chips

Power is buildable. Cutting-edge GPUs are blockaded. This may partially offset [[China]]'s semiconductor disadvantage over time.

See [[China power advantage]] for full details on solar buildout, desert strategy, agrivoltaics, and offshore solar.

---

## GPU deployment bottleneck

Power constraints create a gap between GPU "shipment" and actual deployment:

**Evidence (Jan 2026):**
- **Satya (Nov 2025):** Microsoft has "chips sitting in inventory that I can't plug in"
- **Gavin Baker:** Blackwell deployment only started in last 3-4 months
- **Jensen:** Building major AI DC takes ~3 years

**The math doesn't work:**
- [[NVIDIA]]: 10M+ Blackwell/Rubin chips by end 2026
- Power required: 17-23GW
- Available: Far less (see 44GW gap above)
- Result: GPUs ship to storage, not data centers

**"Buy Now, Deploy Later" pattern:**
- Customers FOMO order GPUs before DCs ready
- GPUs sit in CIP (Construction in Progress) accounting
- Bill-and-hold arrangements possible
- Depreciation deferred until deployment

**Case study — [[Meta]]:**
- ~400K Blackwell GPUs purchased
- Prometheus DC (1GW, Ohio) not online until 2026
- $44B in CIP (Q3 2025), ~$30B of that is uninstalled compute
- 2023 disclosure: "servers stored by our suppliers"

See [[GPU deployment bottleneck]] for full analysis.

---

## Implications for semis

**Demand risk:**
- If power isn't available, hyperscalers can't deploy chips
- May slow AI chip demand even if supply constraints ease
- Could extend the "shortage" narrative longer (chips available, power not)
- **Revenue quality question:** NVIDIA "shipments" may be sitting in warehouses

**Geographic shift:**
- Data centers may move to power-rich locations
- Explains [[xAI]] Colossus 2 in Tennessee (TVA power)
- International locations with better power may benefit

**Efficiency premium:**
- More demand for power-efficient chips
- Favors advanced nodes (better perf/watt) = [[TSMC]]
- [[HBM]] vs GDDR ([[HBM]] more efficient) = [[Long memory]]

---

## For theses

This is a **demand-side risk** for all AI chip theses:
- [[Long TSMC]] — may slow demand, but efficiency favors advanced nodes
- [[Long memory]] — [[HBM]] efficiency advantage, but overall demand at risk
- [[Long WFE]] — if DC buildout slows, fab buildout may follow
- [[AI hyperscalers]] — capex may shift to power infrastructure vs chips

**New angle:** Nuclear as enabling layer for AI infrastructure

---

## [[IEA]] World Energy Outlook 2025

**"The Age of Electricity" — data centers now outspend oil:**

| Metric | Value |
|--------|-------|
| Data center spending 2025 | **$580B** |
| New oil supply spending 2025 | $540B |
| Difference | Data centers +$40B over oil |

This is the first time data center investment exceeds oil exploration/production. A "telling marker of the changing nature of modern, highly digitalised economies."

**Global demand projections:**

| Metric | Current | 2030 | 2035 |
|--------|---------|------|------|
| AI server electricity | 1x | **5x** | — |
| Total DC electricity | 1x | **2x** | **3x** |
| US DC electricity | ~200 TWh | — | **640 TWh** |

**Geographic concentration:**

| Region | Current DC capacity | New capacity share |
|--------|--------------------|--------------------|
| US + [[China]] + [[Europe]] | **82%** | **85%+** |
| US data center share of demand growth | — | **~50%** through 2030 |

**US energy mix for data centers (2024):**

| Source | Share |
|--------|-------|
| [[Natural gas]] | **40%+** |
| Renewables | ~25% |
| Nuclear | ~20% |
| Coal | ~15% |

**2035 projection:** [[Natural gas]] supplies >50% of US data center electricity. Gas is the bridge fuel for AI.

**Grid connection delays ([[IEA]] data):**

| Region | Wait time |
|--------|-----------|
| US typical | 1-3 years |
| Northern Virginia | **7 years** |
| [[UK]] / [[EU]] | **7-10 years** |
| Dublin | **Closed until 2028** |

**Grid investment lag:**
- Electricity generation investment: +70% since 2015
- Grid investment: lagging dramatically
- Result: can't connect new demand to new supply

**Supply chain concentrations:**

| Material | [[China]] share |
|----------|-------------|
| High-purity silicon | **95%** |
| Refined gallium | **99%** |
| Refined copper | **44%** |

[[Taiwan]] dominates advanced node manufacturing. [[Europe]] has near-monopoly on EUV lithography. No country controls all pieces — everyone is vulnerable.

**[[IEA]] framing:** "Age of Electricity" — nearly half the global economy will depend on electricity as primary energy input by 2035.

*Source: [[IEA]] World Energy Outlook 2025, November 2025*

---

## Trump administration position (Davos, Jan 23 2026)

**Sacks and Kratsios at Davos** — most detailed public articulation of administration's power/DC policy:

### Behind-the-meter policy reversal

| Era | Policy |
|-----|--------|
| Biden | DCs could NOT do behind-the-meter generation — had to be part of larger grid |
| Trump/Wright/FERC | Reversed — DCs can stand up their own power generation |

**Sacks:** "It was never [hyperscalers'] plan to draw off the grid. They all saw standing up their own power generation as part of their buildout."

**The argument that DCs lower rates (Sacks):**
1. DCs can sell excess power back to the grid
2. Fixed costs of power generation amortized over greater supply → lower meter rate for everybody
3. "The more scale you get in electricity, like most other things, the price comes down"

### Political dynamics

| Actor | Position |
|-------|----------|
| **Trump** | "Consumers should NOT pay higher rates because of data centers" |
| **Microsoft** | Pledged (week of Jan 20) DCs won't cause residential rate increases |
| **Bernie Sanders** | Letter saying stop all data center development |
| **Sacks response** | "If we do that we will lose the AI race" |

**Sacks on [[China]] power:** [[China]] spinning up new nuclear/coal plant every single week — much of it to power data centers. Stopping US DC buildout would be unilateral disarmament.

**Kratsios:** "If you're in a small community and someone shows up to build a data center, you have to make clear this is going to actually lower your rates long term."

**Microsoft pledge context:** Sacks expects other tech companies to make similar commitments. Trump truth post (Monday before panel): "if you're going to build a data center you have to pay your own way."

*Source: Davos panel (Sacks, Kratsios, Bartiromo), Jan 23 2026*

---

## Political backlash (Jan 2026)

**Senate investigation** into DC power costs:

| Detail | Value |
|--------|-------|
| Senators | Warren, Van Hollen, Blumenthal (D) |
| Targets | Google, Microsoft, Amazon, Meta, [[CoreWeave]], [[Digital Realty]], [[Equinix]] |
| Deadline | Jan 12, 2026 |
| Demand | DCs pay more upfront for grid infrastructure |

**Bloomberg investigation finding:** Electricity costs up to **267% higher** in areas near significant DC activity (vs 5 years ago). See detailed analysis below.

**Senator criticism:**
> "Tech companies regularly hide as much information as possible from the communities in which their data centers will be built... failing to pay their fair share of their electricity rates."

**Political context:** Power affordability became major issue in 2025 elections. Democrats won key races on pocketbook messaging.

**Risk:** Regulatory pushback could slow DC buildout, increase costs, or force location shifts.

---

## Blackout risk (NERC, Jan 2026)

**Winter assessment warning:**

| Metric | Value |
|--------|-------|
| Load growth vs prior winter | **+20GW** (= 20 nuclear plants) |
| Cause | Data centers "main contributor" |
| Risk areas | Northwest, Texas, Carolinas, Southeast, WA, OR |

**NERC:** "Data centers are a main contributor to load growth in those areas where demand has risen substantially since last winter."

**Vulnerable regions:**
- **Texas** — still fragile after Feb 2021 failures (200+ deaths)
- **New England** — gas pipeline constraints
- **Southeast** — newly elevated risk

**Winter factors:**
- Solar generation reduced (fewer daylight hours)
- Battery operations affected by cold
- Gas supply risk from freeze-offs, pipeline constraints

**Context:** US grid already stressed by aging infrastructure, severe storms, wildfires. DC boom adding to strain after two decades of flat demand.

---

## [[Consumer]] impact

Power constraints affect consumers through **price increases** and **power quality degradation**. See dedicated notes for full analysis:

### Price increases

**Key finding:** 70%+ of grid nodes with price increases are within 50 miles of significant DC activity.

| Impact | Value |
|--------|-------|
| Buffalo wholesale price change (2020-2025) | **+197%** |
| Baltimore wholesale price change | **+125%** |
| Americans affected by power quality issues | **3.7 million** |

See [[DC power prices]] for full Bloomberg analysis (Sep 2025).

### Power quality degradation

**Key finding:** AI "sawtooth" loads cause harmonic distortion that damages appliances. DCs are 10,000x the load of a single house.

| Impact | Value |
|--------|-------|
| [[Sensors]] within 50 miles of DCs with distortion | **>75%** |
| Industry damage threshold | **8% THD** |
| Worst readings observed | **12.9% THD** |

See [[DC power quality]] for full Bloomberg analysis (Dec 2024).

---

## Global grid strain

DCs consume more electricity than most countries — only 16 nations use more. See [[Global DC grid strain]] for full Bloomberg analysis (Jun 2024).

**Key stats:**
- **7,000+ global DCs** (up from 3,600 in 2015)
- **508 TWh/year** current consumption (> Italy)
- **1,580 TWh** projected by 2034 (= [[India]])
- AI = **10-15x** the electricity of traditional computing
- H100 = 700W, B100 = ~1,400W (2x)

---

## [[Space]] data centers (speculative)

**Billionaires exploring orbital data centers:**

| Player | Initiative | Timeline |
|--------|------------|----------|
| **[[SpaceX]]** | 100GW satellite network | 4-5 years (Musk) |
| **[[Blue Origin]]** | Bezos promoting concept | 10-20 years (Bezos) |
| **Eric Schmidt** | Acquired [[Relativity Space]] | — |
| **[[Google]]** | Project Suncatcher | 2 satellites by early 2027 |
| **[[Starcloud]]** | [[NVIDIA]]-backed, 5GW DC | — |

**Advantages:**
- 24/7 solar power (sun-synchronous orbit)
- No land constraints
- Simpler permitting (FAA + FCC bulk licenses vs years of ground permits)

**Challenges:**
- Massive solar panels ([[Starcloud]]: 4km × 4km for 5GW)
- Cooling via radiators (no air/water in vacuum)
- Cosmic ray damage to electronics
- Latency (3+ seconds in high orbit)
- [[Space]] debris risk
- Repair impossible without robotics
- Depends on [[SpaceX]] Starship full reusability

**Phil Metzger (UCF):** "If you can get a bulk launch license from the FAA and a bulk constellation license from the FCC, that's just two applications — then you can build thousands of data centers."

**Reality check:** "No new physics, but lots of technical maturity needed." Economically unviable today.

See [[Space data centers]] for full analysis.

---

## Water-power tradeoff

Power and water constraints are linked — see [[Water constraints]] for full analysis.

**The tension:**
- Evaporative cooling uses more water but less power
- Closed-loop cooling uses less water but more power
- Regions with most renewable energy (solar) often have least water

**Key stat:** 60% of DC water consumption is *indirect* — from power plants in water-stressed regions. Power constraints drive location decisions that exacerbate water constraints.

---

*Updated 2026-01-22*

---

## Related

- [[DC power prices]] — consumer impact (Bloomberg Sep 2025)
- [[DC power quality]] — consumer impact (Bloomberg Dec 2024)
- [[Global DC grid strain]] — global context (Bloomberg Jun 2024)
- [[Water constraints]] — companion constraint (water-power tradeoff)
- [[Nuclear power for AI]] — solution (baseload power)
- [[AI hyperscalers]] — demand driver (69GW needed)
- [[xAI]] — example (Colossus 2GW target)
- [[Constellation Energy]] — beneficiary (TMI restart)
- [[Vistra]] — beneficiary (Texas nuclear/gas)
- [[TVA]] — enabler (xAI power source)
- [[GE Vernova]] — supplier (turbines)
- [[Thermal limits]] — related constraint (cooling)
- [[GPU deployment bottleneck]] — consequence (shipped ≠ deployed)
- [[NVIDIA]] — affected (revenue quality risk)
- [[Ansaldo Energia]] — gas turbine supplier (OpenAI UAE)
- [[Solar Turbines]] — turbine supplier (Meta Socrates South)
- [[Siemens Energy]] — turbine supplier (Meta Socrates South)
- [[Meta]] — BYOP example (Socrates South 200MW+)
- [[AI datacenter architecture]] — design patterns
- [[Power-constrained geography]] — consequence ([[Ashburn]] overflow, hub migration)
- [[BYOP]] — dedicated concept note
- [[Dominion Energy]] — utility serving Data Center Alley (power quality issues)
- [[Exelon]] — ComEd parent, Chicago power quality disputes
- [[Bloom Energy]] — fuel cells, AI load volatility research
- [[Whisker Labs]] — power quality monitoring (Ting sensors)
- [[NextEra Energy]] — world's largest wind/solar builder, quoted on AI power demand
- [[SpaceX]] — space data center ambitions ($30B IPO)
- [[Blue Origin]] — Bezos space DC vision
- [[NPU]] — inference efficiency (mitigating factor)
- [[FuriosaAI]] — NPU example (2-3x perf/watt)
- [[Groq]] — inference efficiency (acquired by NVIDIA Dec 2025)
