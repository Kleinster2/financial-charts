#concept #risk #datacenter #power

Data center power availability is emerging as a hard constraint on AI infrastructure buildout.

---

## The gap (Morgan Stanley, Dec 2025)

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

**No line of sight** to solving it in US/Europe:
- Too slow to build
- Too much red tape
- Growing gap to demand

---

## BYOP (Bring Your Own Power)

The new paradigm — hyperscalers securing their own power:

| Company | Strategy |
|---------|----------|
| [[xAI]] | Bitcoin miner partnerships (TeraWulf, Cipher Mining) |
| [[Microsoft]] | [[Constellation Energy]] nuclear restart |
| [[Amazon]] | Talen Energy nuclear co-location |
| [[Google]] | Kairos Power SMR development |
| [[Oracle]] | Nuclear DC permits (Larry Ellison) |
| [[OpenAI]] | On-site gas turbines (UAE Stargate) |
| **[[Meta]]** | Hybrid turbine fleet (Socrates South, 200MW+) |

**OpenAI UAE Stargate example (Jan 2026):**
- 4x [[Ansaldo Energia]] AE94.3 gas turbines
- 1.3GW gross → 1GW derated (desert heat penalty -23%)
- Phase 1: 200MW by YE2026
- "Going well" vs Texas Abilene "not going BRRR"

**Meta Socrates South example (Jan 2026):**
- Hybrid fleet: [[Solar Turbines]], [[Siemens Energy]], Caterpillar
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

## Nuclear renaissance

See [[Nuclear power for AI]] for details.

**Why nuclear:**
- Baseload 24/7 (AI training runs continuously)
- Density (1GW on small footprint)
- Carbon-free (ESG commitments)
- Long-term PPAs match DC investment

**Key deals:**
| Deal | Capacity |
|------|----------|
| Microsoft + Constellation (TMI restart) | 835 MW |
| Amazon + Talen (Susquehanna) | 960 MW |
| Google + Kairos Power (SMR) | 500 MW |

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

Efficiency gains provide more compute per MW:

| Technology | Efficiency gain |
|------------|-----------------|
| Photonic interconnects | 2-4x |
| Specialist inference HW ([[Groq]]) | 2-4x |
| More efficient cooling | 0.3-0.4x power draw |
| Advanced nodes ([[TSMC]]) | Better perf/watt |

**But not nearly enough to close the demand gap.**

---

## Geographic winners

Power availability will drive DC location decisions:

| Region | Advantage |
|--------|-----------|
| **Tennessee/TVA** | xAI Colossus (TVA power) |
| **Texas (ERCOT)** | [[Vistra]] nuclear + gas |
| **Pennsylvania** | TMI restart, Susquehanna |
| **Middle East** | Cheap gas, sovereign wealth |
| **Nordics** | Hydro, cheap power |

---

## China's power advantage

**The asymmetry:**

| Constraint | US | China |
|------------|-----|-------|
| **GPU access** | Abundant (Blackwell) | Constrained (H200 only) |
| **Power access** | Constrained (44 GW gap) | Abundant |
| **Permitting** | Years of red tape | State-directed, fast |
| **Buildout pace** | Slow | 212 GW solar added in 2024 alone |

**China's edge:**
- 212 GW solar installed in one year (vs US ~30 GW)
- 253 GW planned for desert regions
- State-directed = no permitting delays
- Grid expansion keeps pace with demand

**Implication:** Chinese AI labs ([[ByteDance]], [[Baidu]], [[Alibaba]], [[Tencent]]) face GPU constraints but not power constraints. They can build massive clusters of older-gen chips without hitting power walls.

**The trade-off:**
- US: Best chips, can't power them
- China: Abundant power, can't get best chips

Power is buildable. Cutting-edge GPUs are blockaded. This may partially offset China's semiconductor disadvantage over time.

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
- HBM vs GDDR (HBM more efficient) = [[Long memory]]

---

## For theses

This is a **demand-side risk** for all AI chip theses:
- [[Long TSMC]] — may slow demand, but efficiency favors advanced nodes
- [[Long memory]] — HBM efficiency advantage, but overall demand at risk
- [[Long WFE]] — if DC buildout slows, fab buildout may follow
- [[AI hyperscalers]] — capex may shift to power infrastructure vs chips

**New angle:** Nuclear as enabling layer for AI infrastructure

---

## IEA World Energy Outlook 2025

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
| US + China + Europe | **82%** | **85%+** |
| US data center share of demand growth | — | **~50%** through 2030 |

**US energy mix for data centers (2024):**

| Source | Share |
|--------|-------|
| Natural gas | **40%+** |
| Renewables | ~25% |
| Nuclear | ~20% |
| Coal | ~15% |

**2035 projection:** Natural gas supplies >50% of US data center electricity. Gas is the bridge fuel for AI.

**Grid connection delays (IEA data):**

| Region | Wait time |
|--------|-----------|
| US typical | 1-3 years |
| Northern Virginia | **7 years** |
| UK / EU | **7-10 years** |
| Dublin | **Closed until 2028** |

**Grid investment lag:**
- Electricity generation investment: +70% since 2015
- Grid investment: lagging dramatically
- Result: can't connect new demand to new supply

**Supply chain concentrations:**

| Material | China share |
|----------|-------------|
| High-purity silicon | **95%** |
| Refined gallium | **99%** |
| Refined copper | **44%** |

Taiwan dominates advanced node manufacturing. Europe has near-monopoly on EUV lithography. No country controls all pieces — everyone is vulnerable.

**IEA framing:** "Age of Electricity" — nearly half the global economy will depend on electricity as primary energy input by 2035.

*Source: IEA World Energy Outlook 2025, November 2025*

---

## Political backlash (Jan 2026)

**Senate investigation** into DC power costs:

| Detail | Value |
|--------|-------|
| Senators | Warren, Van Hollen, Blumenthal (D) |
| Targets | Google, Microsoft, Amazon, Meta, CoreWeave, Digital Realty, Equinix |
| Deadline | Jan 12, 2026 |
| Demand | DCs pay more upfront for grid infrastructure |

**Bloomberg investigation finding:** Electricity costs up to **267% higher** in areas near significant DC activity (vs 5 years ago).

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

*Updated 2026-01-05*

## Related

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
- [[BYOP]] — dedicated concept note
