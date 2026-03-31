---
aliases: [Iran chip energy risk, semiconductor energy vulnerability 2026, fab power crisis]
tags: [concept, semiconductors, energy, iran, ai, lng]
---

# Iran conflict semiconductor energy risk

How the [[2026 Iran conflict market impact|2026 Iran conflict]] energy shock threatens the global semiconductor supply chain — and by extension, the AI infrastructure buildout. Part of [[Iran conflict economic disruption]].

---

## The chain

```
Strait of Hormuz closed
    → Qatar LNG offline (force majeure, up to 5 years)
        → Asian LNG prices surge (JKM +90%, heading to $30-40/MMBtu)
            → South Korea & Taiwan signal coal dependence
                → Fabs face power instability risk
                    → Wafer losses, extended lead times
                        → Chip supply tightens
                            → AI capex cycle gets supply shock
```

Each link is now either confirmed or actively materializing as of March 22, 2026.

---

## Why South Korea and Taiwan matter

| Country | Share of global advanced chips | LNG dependence | Hormuz LNG as % of total gas |
|---------|-------------------------------|-----------------|------------------------------|
| **Taiwan** | ~65% (via [[TSMC]]) | ~50% of electricity from gas | **27%** |
| **South Korea** | ~20% (via [[Samsung Semiconductor]], [[SK Hynix]]) | ~25% of electricity from gas | 6% (but large absolute volumes) |

Combined: **~85% of the world's advanced semiconductor manufacturing** is concentrated in two countries acutely exposed to the LNG disruption.

Neither has meaningful domestic energy production. Taiwan has no oil, no gas, no coal to speak of. South Korea imports >95% of its energy.

---

## Fab power requirements

Semiconductor fabrication is among the most energy-intensive manufacturing on Earth:

| Metric | Value |
|--------|-------|
| TSMC total electricity consumption (2024) | ~23 TWh — more than some countries |
| Single advanced fab | Power consumption of a small city (~200-300 MW) |
| Power quality requirement | Uninterrupted, voltage-stable to extreme precision |
| Cost of a single unplanned outage | Destroys wafers in process — **$50-150M per event** depending on fab |
| Restart time after outage | **Days to weeks** (clean rooms must be re-qualified) |

Fabs cannot tolerate brownouts, rolling blackouts, or voltage fluctuations. A millisecond-scale power disruption can destroy an entire production lot. This is why semiconductor plants are typically first in line for power allocation — but that only works if total supply is adequate.

---

## Coal switching — necessary but insufficient

Both countries are reverting to coal to fill the LNG gap:

| Country | Action (as of March 22) | Limitation |
|---------|------------------------|------------|
| **South Korea** | Lifting coal power operating caps; scrambling to replace Qatari LNG | Coal plants at ~60% average utilization — headroom exists but limited |
| **Taiwan** | Preparing to rely more on coal; racing to secure June US LNG shipments | Coal share already declining under energy transition policy; reversed by necessity |

Coal can fill **base-load electricity** gaps. But coal ramp-up takes weeks, supply chains need to adjust, and the environmental/political cost is significant. More critically, coal-heavy grids are less stable — more voltage variation, more risk of localized outages.

---

## Demand destruction vs. rationing

The critical question: does the energy shock stay at the "expensive but available" stage, or cross into "rationing"?

| Stage | Impact on fabs | Status (March 22) |
|-------|---------------|-------------------|
| **Price surge** | Higher operating costs, margin compression | Current — electricity costs rising across Asia |
| **Voluntary conservation** | Government asks industry to reduce; fabs exempt | Emerging — SE Asia implementing WFH, 4-day weeks |
| **Mandatory rationing** | Rolling blackouts, allocation quotas | Not yet — but Taiwan has near-zero reserves margin in summer |
| **Force allocation** | Government prioritizes sectors; fabs protected but suppliers may not be | Hypothetical |

Taiwan's summer electricity demand regularly approaches system capacity even in normal years. Adding an LNG supply shock on top of seasonal peak demand creates the scenario where rationing moves from theoretical to operational.

Buffer status (as of Mar 22): Taiwan has secured over half its LNG needs for May, but keeps only ~11 days of LNG in reserve and depends on just-in-time deliveries for the rest. South Korean chipmakers reportedly have around six months of [[Helium supply crisis 2026|helium]] supplies — a more comfortable buffer, but helium is only one of several chemical inputs at risk (see below).

Even if fabs themselves are protected, their **supply chains** may not be — packaging, testing, substrate manufacturing, chemical suppliers, and water treatment facilities all need power too.

---

## Lead time and pricing implications

If fab output drops even 5-10%:

| Effect | Mechanism |
|--------|-----------|
| **Lead times extend** | Advanced node wafers already at 3-6 month lead times; disruption pushes to 6-9+ |
| **Pricing power increases** | [[TSMC]] and [[Samsung Semiconductor]] gain leverage to raise prices (TSMC already +10% for 2026) |
| **Allocation tightens** | Hyperscalers ([[Microsoft]], [[Amazon]], [[Google]], [[Meta]]) competing harder for limited wafer starts |
| **AI training hardware delayed** | [[NVIDIA]] Blackwell, [[AMD]] MI300 ramp depends on TSMC 3nm/5nm capacity |
| **Capex plans slip** | Data center buildout timelines extend — the 44GW [[Power constraints]] gap gets worse, not better |

---

## The strategic irony

The US went to war partly to project power and demonstrate advanced military capability — including AI-enabled targeting via [[Maven Smart System|Project Maven]], autonomous drones, and [[Precise Mass|precise mass]] doctrine. All of these systems depend on advanced semiconductors manufactured in the very countries whose energy supply the war is disrupting.

The drones that need chips → come from fabs that need power → that comes from LNG → that transits Hormuz → which is closed because of the war that uses the drones.

This is not a feedback loop that planners appear to have modeled. The Heritage Foundation's 2007 wargame (cited in [[Iran conflict economic disruption]]) focused on oil prices and SPR releases. Nobody modeled the LNG → semiconductor → military technology chain because in 2007, AI chips weren't a strategic input and Taiwan's LNG dependence wasn't at current levels.

---

## Beyond energy — chemical input vulnerabilities

The semiconductor supply chain's exposure to the Hormuz closure goes beyond LNG. Two additional chemical inputs transit the conflict zone:

### Sulphur

Roughly half of global seaborne sulphur transits the [[Strait of Hormuz]] (FT, Tej Parikh, Mar 22). Sulphur is used in chip cleaning and etching processes. Even before the war, sulphur was facing a supply squeeze from accelerating demand in the tech and electric vehicle industries — the [[Mosaic|Mosaic FY2025 results]] showed sulfur costs +80% YoY in their Phosphates segment. The war converts a gradual tightening into an acute shortage.

### Bromine

The [[Dead Sea]] is the world's largest source of bromine, a chemical used to score (lithographic patterning) on silicon wafers. [[South Korea]] imports virtually all of its bromine supply from [[Israel]] — specifically from [[ICL Group]], the world's #1 bromine producer. While Israel is not party to the Hormuz closure, it is a combatant in the Iran conflict. Bromine supply chains face both direct conflict risk (attacks on Israeli facilities) and indirect risk (shipping disruption, insurance withdrawal on Israel-origin cargo).

### Wafer transport bottleneck

The freight division of [[Cathay Pacific|Cathay Pacific Airways]] handles approximately 30% of global wafer transport — a concentration that mirrors the chip production concentration in East Asia. [[Cathay Pacific]]'s regional hub in [[Dubai]] has limited access due to the conflict, creating a logistics bottleneck even for wafers that have been successfully fabricated. Chip deliveries are already facing delays from air and shipping transportation bottlenecks across the region.

*Source: FT, Tej Parikh, March 22 2026*

---

## Investment read-through

| Position | Rationale |
|----------|-----------|
| **Long TSMC/Samsung** (pricing power) | Supply constraint = higher ASPs; both have announced price increases |
| **Long NVIDIA** (scarcity premium) | If wafer supply tightens, GPU allocation becomes even more valuable |
| **Short AI infrastructure timeline** | The 69GW buildout ([[Power constraints]]) gets harder if the chips arrive slower |
| **Long US onshoring** | Every disruption strengthens the case for [[TSMC Arizona expansion]], Samsung Taylor TX, Intel Ohio |
| **Watch memory** | [[SK Hynix]] HBM production in South Korea — HBM is the bottleneck chip for AI training |

## The mid-April cliff — Papic timeline

[[Marko Papic]], chief strategist at [[BCA Research]], who predicted a US attack on Iran as a tail risk for 2026 in January (FT Free Lunch newsletter, Jan 11), frames a hard deadline:

*"There is no way for the US to replace the oil and natural gas out of the strait on any timeline that avoids a global recession. In my estimation, the US, Israel and Iran have about until mid-April to conclude hostilities and begin returning shipping through Hormuz, or else the world will see its first post-Covid-19 break in supply chains."*

This aligns with [[Amrita Sen]]'s [[Energy Aspects]] reopening estimate (end of April at earliest) and Phil Kornbluth's helium restart timeline (4-5 weeks to resume production + 2-3 months to restore supply chain — see [[Helium supply crisis 2026]]). The convergence of multiple independent expert timelines on an April/May inflection point adds credibility to the framing.

Gulf sovereign wealth funds may also redirect planned AI investments to local security needs — reducing the data center buildout pipeline in the region even after hostilities end.

*Source: FT, Tej Parikh, March 22 2026*

---

## Related

- [[Iran conflict economic disruption]] — parent hub
- [[LNG]] — the transmission mechanism (Qatar offline, Hormuz closed)
- [[Natural gas]] — Waha disconnect, TTF surge
- [[TSMC]] — largest advanced foundry, Taiwan-based
- [[Samsung Semiconductor]] — second-largest, South Korea-based
- [[SK Hynix]] — HBM memory leader, South Korea
- [[Power constraints]] — AI data center power gap (44GW shortfall)
- [[AI Infrastructure]] — the demand side
- [[Semiconductors]] — sector hub
- [[Precise Mass]] — military tech that depends on these chips
- [[Iran conflict defense repricing]] — defense spending that requires chip supply
- [[TSMC Arizona expansion]] — onshoring response
- [[ICL Group]] — Dead Sea bromine supplier; South Korea's primary source for lithographic patterning chemical
- [[Cathay Pacific]] — handles ~30% of global wafer transport; Dubai hub access limited
- [[BCA Research]] — Papic mid-April deadline for supply chain break
- [[Helium supply crisis 2026]] — helium is only one of several chemical inputs disrupted (also sulphur, bromine)

---

*Created 2026-03-22*
