#concept #risk #datacenter #power

Beyond prices — data centers are distorting the power itself. Harmonic distortion from AI workloads is damaging home appliances and aging power equipment, potentially causing billions in damage.

---

## Bloomberg analysis (Dec 2024)

Bloomberg analyzed ~770,000 home sensors ([[Whisker Labs]] "Ting" devices) and found strong correlation between DC proximity and "bad harmonics" — wave pattern deviations that damage appliances.

---

## Key findings

| Metric | Value |
|--------|-------|
| [[Sensors]] within 50 miles of significant DC activity | **>75%** of highly-distorted readings |
| [[Sensors]] within 20 miles of DC activity | **>50%** of worst distortions |
| Americans in most-impacted areas | **3.7 million** |
| Industry threshold for damage | **8%** total harmonic distortion (THD) |
| Worst readings observed | **12.9%** THD |

---

## Distance correlation

| Power quality | Median distance from DCs |
|---------------|--------------------------|
| **Best harmonics** | 87+ miles |
| **Worst harmonics** | Within 20 miles |

---

## Geographic hotspots

| Location | Data |
|----------|------|
| **Loudoun County, VA** (Data Center Alley) | 4x national average for sensors exceeding 8% |
| **Prince William County, VA** | 78% of sensors exceeded limit in Oct; some at 12.9% |
| **Chicago area** | 9,300+ of 16,000 sensors had at least one 8%+ reading |
| **York County, VA** (control — 80+ mi from DCs) | Steady <3% THD |

---

## What bad harmonics do

- Force electronics to run hot
- Cause motors in refrigerators/ACs to rattle
- Lead to sparks and home fires (in severe cases)
- Reduce appliance lifespan
- **"Billions in damage"** to home appliances and aging power equipment

---

## The technical problem

**AI load is "sawtooth" not smooth:**
- Traditional DC loads were predictable
- AI training/inference creates volatile, fluctuating demand
- Aman Joshi ([[Bloom Energy]] CCO): "No grid is designed to be able to handle that kind of load fluctuation not only for one data center but for multiple data centers at the same time"

**Scale comparison:**
- A data center = **10,000x** the load of a single house
- DCs are "city-sized users" that pop up in 1-2 years
- Grid planning typically takes much longer

---

## Utility responses

| Utility | Response |
|---------|----------|
| **[[Dominion Energy]]** (Data Center Alley) | Disputes findings; building new transmission line into Loudoun County |
| **ComEd/[[Exelon]]** (Chicago) | Disputes Whisker Labs methodology |
| **Northern Virginia Electric Cooperative** | Dedicated substations to isolate DC from residential supply |

---

## Solutions

| Solution | Details |
|----------|---------|
| **Dedicated substations** | Isolate DCs from distribution circuits |
| **Filters and capacitors** | Can address harmonics around DCs |
| **New transmission lines** | Dominion building into Loudoun County |
| **Measurement** | NERC task force analysis on DC impacts (2025) |

---

## Expert warnings

| Source | Quote |
|--------|-------|
| **Bob Marshall** (CEO, Whisker Labs) | "Harmonics are a pretty good canary in the coal mine for early signs of stress and problems" |
| **Hasala Dharmawardena** (IEEE/NERC) | "The data center is a very large load. Take your house and increase that by 10,000. That is the difference." |
| **Carrie Bentley** (CEO, Gridwell Consulting) | "If you know it exists, it is easy to fix. So if this is a problem, it is a nice problem." |

---

## Whisker Labs data methodology

- ~770,000 sensors analyzed
- Feb-Oct 2024 readings
- Cross-referenced with DC Byte location data (~1,500 US DCs)
- 8% THD = IEEE threshold for damage

---

*Source: [Bloomberg - AI Power Needs Threaten Billions in Damages for US Households](https://www.bloomberg.com/graphics/2024-ai-power-home-appliances/) (Dec 27, 2024)*

*Created 2026-01-14*

---

## Related

- [[Power constraints]] — parent concept
- [[DC power prices]] — companion consumer impact (price increases)
- [[Global DC grid strain]] — global context
- [[Whisker Labs]] — data source (Ting sensors)
- [[Dominion Energy]] — utility serving Data Center Alley
- [[Exelon]] — ComEd parent, Chicago power quality disputes
- [[Bloom Energy]] — fuel cells, AI load volatility research
