---
aliases: [electrolyzer, electrolyser, electrolysers, water electrolysis, electrolysis equipment]
tags: [concept, hydrogen, energy, industrial, decarbonization, clean_tech]
---

# Electrolyzers

Electrolyzers are industrial machines that use electricity to split water (H₂O) into hydrogen (H₂) and oxygen (O₂). They are the central piece of hardware in the [[Green hydrogen]] supply chain — if the electricity feeding them comes from renewables, the hydrogen produced carries near-zero carbon. Every strategic document on decarbonizing [[Steel|steel]], [[Ammonia|ammonia]], refining, long-haul shipping, and aviation runs through electrolyzer deployment at scale.

Electrolyzer manufacturing has become one of the cleanest test cases for the [[Second China shock]] thesis: Chinese alkaline systems sell at roughly a third of Western prices, Western incumbents are financially stressed, and the EU's flagship [[European Green Deal]] hydrogen subsidy is flowing disproportionately to projects specifying Chinese equipment.

---

## What they do — the basic science

Water electrolysis is one of the oldest industrial chemistries (commercial use since the 1920s). An electric current applied across two electrodes in water (with an ion-conducting medium between them) drives the reaction:

2 H₂O + electricity → 2 H₂ + O₂

The practical question is not whether it works but at what capex/opex, what efficiency (kWh of electricity per kg of H₂), what flexibility (can it ramp up and down with variable renewables), and what lifetime (years of operation before stack replacement).

Modern reference numbers:
- Electricity input: ~50-55 kWh per kg H₂ (theoretical minimum ~39.4 kWh/kg)
- Stack lifetime: 60,000-90,000 operating hours depending on technology
- Current density: varies by technology from ~0.4 A/cm² (alkaline) to 2+ A/cm² (advanced PEM)

---

## The four technology families

| Technology | Operating temp | Capex | Maturity | Strengths | Weaknesses |
|---|---|---|---|---|---|
| **Alkaline (AEL)** | 60-90°C | Lowest | Most mature (100+ years) | Cheap, long-lived, no precious metals | Slow ramp, lower current density, hot caustic KOH handling |
| **PEM** (proton exchange membrane) | 50-80°C | Mid-to-high | Mature commercial | Fast ramp, compact, responsive to renewable variability | Uses iridium/platinum, sensitive to water purity |
| **SOEC** (solid oxide electrolysis cell) | 700-850°C | Highest | Early commercial | Highest efficiency, can use industrial waste heat, enables co-electrolysis of CO₂ for synfuels | Immature, thermal cycling fatigue, expensive ceramics |
| **AEM** (anion exchange membrane) | 40-60°C | Emerging | Pre-commercial | Combines alkaline economics with PEM ramp behavior | Membrane durability still unproven |

Alkaline dominates deployed capacity today (~60-70% of installed base). PEM leads new-order volume in the West. SOEC is where [[Bloom Energy]], Topsoe, and Sunfire have placed differentiated bets. AEM is the dark-horse candidate several Chinese and European startups are pursuing.

---

## Why they matter for decarbonization

| End market | Role of H₂ | Electrolyzer demand implication |
|---|---|---|
| [[Steel|Steel]] | Replaces coking coal in direct-reduced iron (DRI) processes; [[Thyssenkrupp]], [[SSAB HYBRIT]], [[H2 Green Steel]] plants | Each Mt of green DRI needs ~50,000-80,000 tpa of H₂, meaning ~500 MW of electrolyzer capacity per plant |
| [[Ammonia]] / fertilizer | Replaces natural gas as H₂ feedstock in Haber-Bosch | Global ammonia production is ~230 Mt/year; full decarbonization requires ~500+ GW of electrolyzers |
| Oil refining | Replaces grey H₂ currently made via SMR (majority of industrial H₂ today) | Refinery demand for H₂ is ~50 Mt/year globally |
| Long-haul shipping | H₂-derived fuels (ammonia, methanol, liquid H₂) | Not direct H₂ use; same electrolyzer demand underneath |
| Aviation (e-SAF) | Green H₂ + captured CO₂ → synthetic aviation fuels | Very electrolyzer-intensive (low round-trip efficiency) |
| Grid storage | Long-duration via power→H₂→power | Economics still poor at 2026 prices |
| Heavy trucking | Fuel cells for long-haul where batteries fail | Hyundai, Daimler, Volvo hedging bets |

Cumulative electrolyzer capacity needed globally for 2050 net-zero scenarios ranges from 3,000 GW (IEA) to 5,500 GW (IRENA) — versus roughly 2 GW installed at end-2023. Whichever number is right, the buildout is enormous and the manufacturing capacity to support it does not yet exist in the West.

---

## The Second China shock pattern

### Chinese cost advantage

Chinese alkaline electrolyzers currently sell at roughly $300-500 per kW of installed capacity. Western equivalents sell at $1,000-1,500 per kW. The 60-70% price gap is driven by:

- **Scale**: Chinese firms operate GW-scale annual manufacturing capacity; most Western firms are still at tens to hundreds of MW per year
- **Vertical integration**: Longi Hydrogen was spun out of Longi Solar (the world's largest solar-panel maker), sharing supply-chain infrastructure for stamped metal, electrodes, gasketing
- **Industrial-policy subsidy**: provincial subsidies and state-firm procurement targets
- **Lower component costs**: Chinese steel, chemicals, and electronics sourced at domestic prices

No efficiency gain or process innovation at a Western manufacturer closes a 60-70% cost gap. The gap is structural.

### The EU Hydrogen Bank auction outcome

The EU Hydrogen Bank's first auction (Dec 2023, awarded Apr 2024) cleared at strike prices of €0.37-0.48/kg — well below what Western-equipment projects could bid. A significant majority of winning projects specified Chinese electrolyzer equipment, according to industry trade press. The second auction (Dec 2024) saw similar patterns. This is the hydrogen equivalent of Europe "inventing the solar market and surrendering it to China" ([[Adam Tooze]]'s framing in the 2025 LRB lecture).

### Western manufacturer stress

| Firm | 2026 state |
|---|---|
| [[Nel ASA]] ([[Norway]]) | Cut capacity, restructured multiple times, stock down 80%+ from 2021 peaks |
| [[ITM Power]] (UK) | Repeatedly restructured, new CEO, smaller ambition scope |
| [[Plug Power]] (US) | Persistent cash-burn, going-concern auditor flag in recent 10-K, depends on IRA 45V tax credit |
| [[Siemens Energy]] Silyzer | Embedded in larger grid-equipment business; survives on internal cross-subsidy |
| McPhy (France) | Restructured 2024; survives on scale-down |
| Cummins Accelera | Backed by Cummins balance sheet; lower exposure to standalone dependency |
| Bloom Energy (US SOEC) | Differentiated in high-temperature niche; avoids head-to-head with alkaline |
| Topsoe (Denmark SOEC) | Differentiated similarly |
| Sunfire (Germany SOEC + AEL) | Private, aggressive expansion, funded by IRA/EU subsidies |

### Chinese leaders

- Longi Hydrogen (subsidiary of Longi Solar) — largest global alkaline capacity
- Sungrow Hydrogen (solar-inverter parent)
- Peric (state-affiliated)
- 718 Institute (state research institute spinoff)
- CIMC-Cockerill Jingli JV
- Haoyuan Qingneng

Combined Chinese alkaline manufacturing capacity is estimated at 4-6 GW per year — larger than the rest of the world combined.

---

## The US alternative path

The [[Inflation Reduction Act]] Section 45V provides up to **$3/kg production tax credit** for clean hydrogen, tiered by carbon intensity. Treasury final rules (issued Jan 2025) specify domestic content and commissioning-date constraints that partially shield US equipment manufacturers from Chinese imports, though the rules are weaker than the [[IRA]] EV critical-mineral/battery-component thresholds.

The result is a bifurcated global market:
- **US domestic deployment**: partially protected by 45V rules + tariffs, though still small in aggregate capacity
- **EU deployment**: minimally protected, Chinese-equipment dominant
- **Chinese domestic deployment**: 100% domestic equipment by policy
- **Rest of world** ([[Middle East]], [[India]], [[Australia]], [[Chile]], [[Morocco]] — the big green-H₂ export ambitions): price-competitive tendering, China usually wins

This is structurally identical to the solar-panel bifurcation that emerged 2015-2020.

---

## The economic reality check

Despite the policy attention, green hydrogen deployment has underperformed announcements. Through 2025:

- Announced global project pipeline: ~1,500 GW by 2030
- Projects reaching Final Investment Decision (FID): ~8 GW (roughly 0.5% of announcements)
- Actually operating: ~2 GW

The electrolyzer business is therefore not yet in volume production mode at anything like the scale the 2050 scenarios require. Demand has been pulled forward by subsidy announcements but held back by offtake uncertainty, grid-connection delays, and the collapse in European gas prices after peak [[2022 European energy crisis|2022 crisis]] that reduced the economic urgency.

This makes the electrolyzer competition an interesting stress test: the industrial-policy battle is being fought over a market whose actual size is still 2-3 orders of magnitude below what the announcements imply. Winners of the current phase may or may not be the winners of the eventual real deployment phase.

---

## Investment implications

| Bull case | Bear case |
|---|---|
| Steel, ammonia, refining decarbonization cannot happen without electrolyzers; demand must eventually arrive | Demand keeps sliding right; green H₂ not cost-competitive without subsidy through at least 2030 |
| IRA and EU subsidies crystalize Western manufacturer competitive position | Chinese cost advantage is structural; subsidy cannot offset a 60-70% cost gap forever |
| SOEC technology (Bloom, Topsoe) may differentiate at high-temp industrial sites | SOEC capex still uneconomic outside niche applications |
| Electrolyzer makers that survive the shakeout will capture a massive long-cycle build | Shakeout may eliminate most current Western names before scale demand arrives |
| Integrated players (Longi, Siemens Energy) have balance-sheet staying power | Pure-play electrolyzer firms have demonstrable cash-burn problem |

---

## Related

### Concepts
- [[Green hydrogen]] — the commodity electrolyzers produce
- [[Hydrogen]] — the underlying molecule and industrial use cases
- [[Second China shock]] — the pattern of Chinese cost advantage and Western industrial stress
- [[European Green Deal]] — the policy framework that set the demand signal
- [[Inflation Reduction Act]] — Section 45V production tax credit architecture
- [[Ammonia]]
- [[Steel]]

### Actors — Western manufacturers
- [[Nel ASA]]
- [[ITM Power]]
- [[Plug Power]]
- [[Siemens Energy]]
- [[Bloom Energy]]
- [[Cummins]]

### Actors — Chinese manufacturers
- [[Longi Green Energy]] (parent of Longi Hydrogen)
- [[Sungrow]]

### Actors — End users / demand drivers
- [[Thyssenkrupp]]
- [[SSAB]]
- [[H2 Green Steel]]
- [[Fortescue]]
- [[Air Products]]

---

## Sources

- IEA, *Global Hydrogen Review 2024*
- IRENA, *World Energy Transitions Outlook 2023*
- European Hydrogen Bank, auction results Dec 2023 and Dec 2024
- BloombergNEF, *Hydrogen Economy Outlook* series
- US Treasury 45V final rules, January 2025
