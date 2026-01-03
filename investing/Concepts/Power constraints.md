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

**Alternative providers filling the gap** (SemiAnalysis, Dec 2025):
- Bloom Energy — fuel cells
- Doosan Enerbility — turbines, nuclear
- Voltagrid — modular power

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

## Implications for semis

**Demand risk:**
- If power isn't available, hyperscalers can't deploy chips
- May slow AI chip demand even if supply constraints ease
- Could extend the "shortage" narrative longer (chips available, power not)

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

*Updated 2026-01-01*

## Related

- [[Nuclear power for AI]] — solution (baseload power)
- [[AI hyperscalers]] — demand driver (69GW needed)
- [[xAI]] — example (Colossus 2GW target)
- [[Constellation Energy]] — beneficiary (TMI restart)
- [[Vistra]] — beneficiary (Texas nuclear/gas)
- [[TVA]] — enabler (xAI power source)
- [[GE Vernova]] — supplier (turbines)
- [[Thermal limits]] — related constraint (cooling)
