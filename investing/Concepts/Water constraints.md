#concept #risk #datacenter #water

Data center water consumption is emerging as a hard constraint on AI infrastructure buildout, alongside [[Power constraints]].

---

## The scale (Bloomberg/IEA, May 2025)

| Metric | Value |
|--------|-------|
| DCs in high/extremely high water stress areas | **58%** of all global DCs |
| New DCs since 2022 in high water stress areas | **2/3** (two-thirds) |
| New AI DCs in water-scarce areas (past 3 years) | **160+** (70% increase vs prior 3 years) |
| Global DC water consumption (current) | **560 billion liters/year** |
| Global DC water consumption (2030 projection) | **1,200 billion liters/year** (2x+) |

---

## Water usage per facility

| Metric | Value |
|--------|-------|
| 100 MW data center water use | **2 million liters/day** |
| Equivalent household consumption | **6,500 households** |
| DC evaporation rate | **~80%** of water drawn |
| Residential evaporation rate | ~10% (rest discharged) |
| Indirect water (power plants) | **60%** of total DC water consumption |

**The 60% indirect figure is key:** DCs powered by water-hungry power plants in water-stressed regions have double the water footprint.

---

## US geographic concentration

**5 states account for 72% of new DCs in high water-stress areas:**

| State | Situation |
|-------|-----------|
| **California** | 1,260 MW in water-stressed areas |
| **Arizona** | 500 MW+ in water-stressed areas |
| **Texas** | 1,200 MW + 255 MW sites; "hottest summers on record" |
| **Illinois** | Part of 72% concentration |
| **Virginia** | Part of 72% concentration (Data Center Alley) |

**59 additional facilities planned in US dry regions by 2028** (DC Byte).

---

## Global data centers in water-stressed areas (1997-2025)

![[global-dc-water-stress.png]]

| Country | DCs in high/extremely high stress |
|---------|-----------------------------------|
| **China** | 262 |
| **Germany** | 166 |
| **UK** | 153 |
| **Australia** | 140 |
| **India** | 135 |
| **Spain** | 117 |
| **Canada** | 95 |
| **Russia** | 92 |
| **Indonesia** | 87 |
| **Saudi Arabia** | 81 |
| **Thailand** | 73 |
| **France** | 67 |
| **UAE** | 60 |
| **Italy** | 55 |
| **Chile** | 52 |
| **Mexico** | 52 |

**Key insight:** China and India have **even greater proportion** of DCs in drier areas compared to US — reflects both growing DC footprint and heightened water scarcity from climate change.

---

## The water-power tradeoff

Data centers face a fundamental constraint trade-off:

| Cooling method | Water use | Power use |
|----------------|-----------|-----------|
| **Evaporative (swamp cooling)** | High (~80% evaporated) | Lower |
| **Closed-loop (no evaporation)** | Minimal | Higher |
| **Air conditioning** | None | Highest |

**The tension:**
- Regions with most renewable energy (especially solar) often have least water
- DCs using less water in hotter regions require more power
- Closed-loop systems are "more power-hungry than evaporative methods"

---

## Hyperscaler water commitments

| Company | Commitment | Reality |
|---------|------------|---------|
| **Amazon** | Water positive by 2030 | Relies widely on evaporative cooling |
| **Microsoft** | Water positive by 2030 | Developing closed-loop systems for 2026 |
| **Google** | Water positive by 2030 | Providing more granular annual reporting |

**AWS specifics:**
- Cools **24 data centers using treated sewage**
- Hoping to dramatically expand recycled water use
- Uses different cooling methods based on time of year/weather

**Microsoft specifics:**
- Developed closed-loop DC design (water circulates without evaporation)
- First deployment: **Wisconsin and Arizona, 2026**

---

## Political and community backlash

**Water-related protests against data centers:**

| Location | Outcome |
|----------|---------|
| **Chile** | Temporarily revoked Google's authorization for $200M facility |
| **Netherlands** | Protests against DC water use |
| **Uruguay** | Water-related protests |
| **The Dalles, Oregon** | City sued to prevent release of Google's water records (13-month legal battle) |

**Texas concerns:**
- Jennifer Walker (National Wildlife Federation): "I'm concerned about any super water-intensive industry that is going to come into our state"
- Texas Water Development Board sent water use survey to DCs — received "lackluster response"

---

## Lack of transparency

- Almost no information about DC water usage on individual system level is publicly available
- Water usage often treated as trade secret
- Google beginning to provide more granular detail in annual reports
- State officials lack data needed for water planning

---

## Expert warnings

| Source | Quote |
|--------|-------|
| **Newsha Ajami** (Lawrence Berkeley / Stanford) | "It is very much a growing issue — and it is spreading everywhere" |
| **Sharlene Leurig** (Fluid Advisors) | "Water has traditionally been far less consequential for industrial users than energy costs and availability" |
| **Amy Bush** (RMBJ Geo, Abilene) | "Every part of the state is facing this water-energy nexus crisis" |

---

## Solutions under development

| Solution | Details |
|----------|---------|
| **Cold plate cooling** | Hot chips directly on cold plates using water |
| **Immersion cooling** | Submerging chips/servers in liquid |
| **Synthetic coolants** | Some being phased out (PFAS/"forever chemicals") |
| **Closed-loop systems** | Microsoft (2026), Crusoe Energy (Stargate) |
| **Recycled water** | AWS using treated sewage at 24 DCs |
| **Watershed restoration** | Cloud firms working with local nonprofits |

---

## Implications

**For hyperscalers:**
- Water positive commitments increasingly difficult as AI demand grows
- Location decisions constrained by both power AND water availability
- May need to accept higher power costs for lower water use

**For geographic winners:**
- Water-rich regions gain advantage (Great Lakes, Pacific Northwest)
- Middle East buildout (Saudi, UAE) requires desalination or closed-loop

**For investors:**
- Water infrastructure companies may benefit
- Cooling technology companies (immersion cooling) gaining relevance
- ESG risk for hyperscalers in water-stressed regions

---

*Source: [Bloomberg - How AI Demand Is Draining Local Water Supplies](https://www.bloomberg.com/graphics/2025-ai-impacts-data-centers-water-data/) (May 8, 2025)*

*Created 2026-01-14*

---

## Related

- [[Power constraints]] — companion constraint (power-water tradeoff)
- [[Thermal limits]] — cooling is the connection between power and water
- [[AI hyperscalers]] — demand driver
- [[Amazon]] — 24 DCs using treated sewage
- [[Microsoft]] — closed-loop DC design (2026)
- [[Google]] — The Dalles water controversy
- [[OpenAI]] — Stargate Abilene in water-stressed Texas
- [[Crusoe Energy]] — closed-loop cooling for Stargate
- [[AI datacenter architecture]] — cooling system design
