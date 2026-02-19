---
aliases: [firm capacity, firm energy, baseload power, dispatchable power, 24/7 power]
---
#concept #power #datacenter #energy

**Firm power** — Electricity generation that is available on demand with low risk of outage, regardless of weather, time of day, or season. The opposite of intermittent power (wind, solar). Data centers require firm power because they run 24/7/365 with zero tolerance for downtime.

---

## Why firm power matters

Data centers are not normal electricity consumers. A 100 MW hyperscale facility needs 100 MW *every second of every day*. Intermittent sources (solar, wind) can't guarantee this alone — they need firming through storage, backup generation, or grid balancing.

The AI buildout has elevated firm power from an engineering detail to an **investment-grade constraint**. DOE explicitly identifies firm power as a requirement for data center siting.

| Characteristic | Firm power | Intermittent power |
|---------------|-----------|-------------------|
| Availability | 24/7, on-demand | Weather/time-dependent |
| Capacity factor | 85-95% | 20-35% (solar/wind) |
| Examples | Nuclear, geothermal, natural gas, hydro (reservoir) | Solar, wind, run-of-river hydro |
| Data center suitability | Direct match | Requires firming (storage/backup) |
| Carbon profile | Varies (zero for nuclear/geothermal, high for gas) | Zero (but needs firm backup) |

---

## Firm power sources ranked for data centers

### Tier 1 — Zero-carbon firm (ideal)

| Source | Capacity factor | Scalability | Timeline | Key players |
|--------|----------------|-------------|----------|-------------|
| [[Nuclear power for AI\|Nuclear]] (existing fleet) | ~93% | Limited (plant restarts) | 1-3 years | [[Constellation Energy]], [[Talen Energy]] |
| [[Nuclear power for AI\|Nuclear]] (SMR) | ~93% (projected) | High (modular) | 2028-2032 | [[TerraPower]], [[Kairos Power]], NuScale, [[Oklo]] |
| Geothermal | ~90% | Geography-limited | 2-5 years | Fervo Energy, Sage Geosystems |
| Large hydro (reservoir) | ~40-60% | Geography-limited | Existing only | Regional utilities |

**Nuclear is the consensus winner** — highest capacity factor, zero-carbon, scalable (eventually). Every major hyperscaler has signed nuclear deals. See [[Nuclear power for AI]].

**Geothermal is the sleeper** — 24/7 firm availability like nuclear, but faster to deploy and no waste/proliferation concerns. Fervo Energy's enhanced geothermal (EGS) uses fracking techniques to unlock sites beyond traditional volcanic areas. [[Google]] signed a 115 MW Fervo PPA (2026 delivery).

### Tier 2 — Low-carbon firm (bridge)

| Source | Capacity factor | Carbon | Use case |
|--------|----------------|--------|----------|
| Natural gas combined cycle | ~55-85% | ~400g CO₂/kWh | Bridge fuel, [[BYOP]] on-site |
| Natural gas + CCS | ~55-85% | ~40g CO₂/kWh | If CCS works at scale |
| [[Aeroderivative turbines for data centers\|Aeroderivative turbines]] | ~55-85% | ~400g CO₂/kWh | Fast deployment, retired jet engines |

Natural gas is the **de facto firm power source today** — fast to deploy, proven, available. But conflicts with corporate clean energy commitments. CCS could resolve this but remains unproven at scale.

### Tier 3 — Intermittent + firming (aspiration)

| Combination | Effective capacity factor | Cost | Status |
|-------------|--------------------------|------|--------|
| Solar + 4-hour battery | ~40-50% effective | Moderate | Common but insufficient for 24/7 |
| Solar + wind + long-duration storage | ~70-85% effective | Expensive | Emerging (iron-air, compressed air) |
| Wind PPA + grid balancing | Varies | Grid-dependent | [[Equinix Brasil]] model (Auren wind PPA) |

**The gap:** No combination of intermittent + storage currently matches nuclear/geothermal for true 24/7 firm power at data center scale. Long-duration storage (100+ hours) could change this — see [[Grid storage]].

---

## The firmness spectrum

Not all "firm" power is equally firm. A useful framework:

| Level | Description | Example |
|-------|-------------|---------|
| **Baseload firm** | Always on, 85%+ capacity factor | Nuclear, geothermal |
| **Dispatchable firm** | Available on demand, ramp up/down | Natural gas, hydro with reservoir |
| **Contracted firm** | PPA guarantees delivery, grid handles intermittency | Corporate wind/solar PPAs |
| **Certified firm** | Renewable energy credits match consumption (annual) | Most corporate "100% renewable" claims |

**The dirty secret:** Most tech companies claiming "100% renewable" operate at the **certified** level — they buy RECs to match annual consumption, but the actual electrons powering their servers at 2 AM come from natural gas or nuclear. True 24/7 carbon-free energy (CFE) matching — hour-by-hour — is the new frontier.

**[[Google]] 24/7 CFE initiative:** Committed to matching electricity consumption with carbon-free sources on an **hourly basis** by 2030, not just annually. This requires firm clean power, not just wind/solar PPAs.

---

## Hyperscaler firm power strategies

| Company | Strategy | Key deals |
|---------|----------|-----------|
| [[Microsoft]] | Nuclear restart + SMRs | Three Mile Island restart ([[Constellation Energy]]), SMR development |
| [[Google]] | Geothermal + nuclear + 24/7 CFE | Fervo Energy 115 MW, [[Kairos Power]] SMR, [[Intersect Power]] acquisition |
| [[Amazon]] | Nuclear + gas bridge | [[Talen Energy]] Susquehanna nuclear PPA, Cumulus Data |
| [[Meta]] | Massive nuclear portfolio | 6.6 GW by 2035 — [[Constellation Energy]], Vistra, [[TerraPower]], Oklo |
| [[Oracle]] | Gas turbines + future nuclear | On-site gas generation for current buildout |

---

## Brazil's firm power position

[[Brazil]]'s electricity grid is **88% renewable** (mostly large hydro) — but hydro firmness depends on rainfall. Drought years (2021 crisis) exposed the grid's vulnerability. The [[Equinix Brasil]] model (Auren wind PPA + grid balancing) provides contracted firmness but not physical firmness.

**Brazil's firm power mix:**
- Large hydro (reservoir): ~65% of generation — firm when water levels are adequate
- Wind + solar: growing rapidly — intermittent
- Natural gas/biomass: backup — dispatchable firm
- Nuclear: Angra 1 & 2 (~2 GW) — baseload firm but tiny share

**The [[REDATA]] question:** Even with GPU import tax relief, companies won't train proprietary AI models in Brazil unless the power is demonstrably firm. Hydro variability is the silent risk.

---

## Investment implications

**Firm power = pricing power.** Assets that can deliver guaranteed 24/7 clean electricity to data centers command premium PPAs.

| Thesis | Expression | Risk |
|--------|-----------|------|
| Long nuclear utilities | [[Constellation Energy]], [[Vistra]] | Regulatory/restart delays |
| Long geothermal | Fervo Energy (private), Ormat Technologies | Technology/scale risk |
| Long gas bridge | [[GE Vernova]], [[Siemens Energy]] | Carbon commitments conflict |
| Long storage | [[Tesla]] Megapack, Form Energy (iron-air) | Duration/cost not yet proven |
| Short intermittent-only claims | Companies with only wind/solar PPAs | Market may not penalize yet |

**Key insight from DOE:** Firm power is the binding constraint on data center siting — more than land, water, or fiber connectivity. Regions with firm power surplus attract DC investment; regions without it lose.

---

## Quick stats

| Metric | Value |
|--------|-------|
| US DC power demand (2028 est.) | 69 GW |
| US firm power gap | 44 GW ([[Power constraints]]) |
| Nuclear capacity factor | ~93% |
| Solar capacity factor | ~20-25% |
| Wind capacity factor | ~30-35% |
| Geothermal capacity factor | ~90% |
| Hours in a year | 8,760 |

*Created 2026-02-19*

---

## Related

- [[Power constraints]] — parent concept (44GW US shortfall)
- [[Nuclear power for AI]] — primary firm power solution
- [[BYOP]] — hyperscalers building their own firm power
- [[Shadow grids]] — parallel firm power infrastructure
- [[Clean energy for AI]] — intersection of clean + firm
- [[Grid storage]] — firming intermittent sources
- [[Aeroderivative turbines for data centers]] — gas bridge to firm clean power
- [[Power grid primer]] — foundational grid concepts
- [[Equinix Brasil]] — Brazil firm power case study (hydro + wind PPA)
- [[Constellation Energy]] — largest US nuclear fleet (firm power leader)
- [[Google]] — 24/7 CFE hourly matching pioneer
- [[Geothermal]] — zero-carbon firm power (Fervo Energy)
- [[Latin America AI competitiveness]] — regional firm power dynamics
