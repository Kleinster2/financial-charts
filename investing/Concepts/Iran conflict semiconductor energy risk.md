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

## Investment read-through

| Position | Rationale |
|----------|-----------|
| **Long TSMC/Samsung** (pricing power) | Supply constraint = higher ASPs; both have announced price increases |
| **Long NVIDIA** (scarcity premium) | If wafer supply tightens, GPU allocation becomes even more valuable |
| **Short AI infrastructure timeline** | The 69GW buildout ([[Power constraints]]) gets harder if the chips arrive slower |
| **Long US onshoring** | Every disruption strengthens the case for [[TSMC Arizona expansion]], Samsung Taylor TX, Intel Ohio |
| **Watch memory** | [[SK Hynix]] HBM production in South Korea — HBM is the bottleneck chip for AI training |

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

---

*Created 2026-03-22*
