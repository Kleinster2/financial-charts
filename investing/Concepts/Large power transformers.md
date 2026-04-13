---
aliases: [Power transformers, Electrical transformers, Large power transformer, LPT]
---
#concept #energy #grid #electrical #datacenter

**Large power transformers** — The voltage-conversion hardware that lets bulk power become usable power. In the AI data center buildout, they have become a schedule-setting bottleneck: campuses can be financed and permitted faster than transformers can be delivered.

---

## Synthesis

The AI buildout is not failing for lack of ambition. It is colliding with a piece of grid hardware whose manufacturing and installation timeline is longer than the planning cycle of many campuses. That shifts the real constraint from compute budgets to energization, and turns transformer yards, substations, and adjacent electrical gear into first-order investment bottlenecks.

---

## Why they matter

Data centers do not take power straight from a transmission line and start training models. They need voltage stepped down, routed through substations, and conditioned before it reaches switchgear, [[UPS]] systems, and racks. That makes transformers non-optional at every large campus.

| Stage | Role |
|-------|------|
| Transmission / substation | Step voltage between grid layers |
| Facility intake | Deliver usable power to the campus |
| Generator interconnection | Tie on-site power into the electrical yard |

---

## The bottleneck

| Metric | Value | Source |
|--------|-------|--------|
| Pre-2020 lead time | 24-30 months | [[Bloomberg]] / Sightline, Apr 2026 reporting |
| Current lead time | Up to 5 years | [[Bloomberg]] / Sightline, Apr 2026 reporting |
| 2026 large DC / AI-factory pipeline | ~16 GW across ~140 projects | Sightline Climate, Feb 24 2026 |
| Already under construction | ~5 GW | Sightline Climate, Feb 24 2026 |
| 2025 delayed share | 26% of 110 projects | Latitude [[Media]] / Sightline, Feb 27 2026 |

The important shift is that the constraint is no longer abstract. "Power shortage" resolves into specific boxes and yards: transformers, switchgear, breakers, batteries, substation work, and the labor to install them. If a transformer has a five-year lead time, the campus schedule is fiction no matter what the capex deck says.

---

## Public-market expressions

| Expression | Why it matters |
|-----------|----------------|
| [[Hubbell]] | Substation and connector hardware around transformer yards |
| [[Quanta Services]] | Builds substations, feeder lines, and interconnection work |
| [[Eaton]] | MV/LV distribution, [[UPS]], and facility power chain |
| [[ABB]] | Medium-voltage gear and building automation around the powered shell |
| [[Schneider Electric]] | Power distribution and cooling layers after energization |
| [[GE Vernova]] | When grid equipment stalls, developers lean harder on on-site generation |
| [[Siemens Energy]] | Same [[BYOP]] workaround logic through turbines plus grid tech |
| [[Bloom Energy]] | Fast-deploy on-site power when utility timelines do not clear |

---

## Why investors care

- Existing powered sites gain option value.
- Grid-equipment lead times create pricing power for incumbents and favored suppliers.
- The bottleneck shifts value from who wants to build to who can actually energize.
- On-site generation becomes a workaround, not a side story.

---

## Disambiguation

Not to be confused with [[Transformer]], the AI architecture note.

---

## Related

- [[Power constraints]]
- [[Power infrastructure bottleneck]]
- [[Grid infrastructure super-cycle]]
- [[Data center physical layer]]
- [[Shadow grids]]
- [[Data Centers]]
