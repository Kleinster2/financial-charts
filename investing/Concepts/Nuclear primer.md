#concept #nuclear #energy #science #primer

**Nuclear primer** — foundational physics, reactor technology, and fuel cycle concepts for energy investing. Understanding nuclear helps evaluate the renaissance thesis, SMR potential, and uranium supply dynamics.

> **Key insight:** Nuclear is the only proven source of carbon-free, 24/7 baseload power at scale. Its constraints are regulatory and economic, not technical. The technology works — the question is whether society will allow it.

---

## Nuclear fission basics

Heavy atoms (uranium, plutonium) split when hit by neutrons, releasing energy and more neutrons → chain reaction.

```
U-235 + neutron → fission products + 2-3 neutrons + ~200 MeV energy
                            ↓
                    Hit more U-235 atoms
                            ↓
                      Chain reaction
```

| Concept | Definition |
|---------|------------|
| **Fission** | Splitting heavy atoms |
| **Critical** | Self-sustaining chain reaction |
| **Subcritical** | Reaction dying out |
| **Supercritical** | Reaction accelerating |

**Control:** Reactor operates slightly supercritical to generate power. Control rods absorb neutrons to regulate.

---

## Energy density — why nuclear wins

| Fuel | Energy per kg |
|------|---------------|
| Uranium (fission) | **80,000,000 MJ** |
| Natural gas | 55 MJ |
| Coal | 24 MJ |
| Lithium battery | 0.5 MJ |

**Implication:** A single fuel pellet (size of fingertip) = energy of 17,000 cubic feet of natural gas or 1,780 lbs of coal.

**Land use:** Nuclear plant produces ~1 GW on ~1 square mile. Equivalent solar needs 75+ square miles.

---

## Uranium fuel

### Natural uranium

| Isotope | Abundance | Fissile? |
|---------|-----------|----------|
| U-238 | 99.3% | No (fertile) |
| U-235 | 0.7% | **Yes** |

Only U-235 sustains chain reaction. Natural uranium has too little.

### Enrichment

Increase U-235 concentration:

| Level | U-235 % | Use |
|-------|---------|-----|
| Natural | 0.7% | CANDU reactors |
| LEU (Low Enriched) | 3-5% | Most reactors |
| HALEU | 5-20% | Advanced reactors, SMRs |
| HEU (Weapons grade) | 90%+ | Weapons, naval |

**Enrichment methods:** Gaseous diffusion (old), gas centrifuge (standard), laser (emerging).

**HALEU bottleneck:** Advanced reactors need HALEU. Only Russia produced commercially until recently. US ramping domestic supply — see [[Centrus Energy]].

---

## Reactor generations

| Generation | Era | Examples |
|------------|-----|----------|
| Gen I | 1950s-60s | Shippingport, Magnox |
| Gen II | 1970s-90s | Most operating plants (PWR, BWR) |
| Gen III/III+ | 2000s+ | AP1000, EPR, APR1400 |
| Gen IV | Future | Molten salt, fast reactors |

---

## Reactor types (Gen II/III)

### PWR (Pressurized Water Reactor)

Most common globally (~70% of fleet).

```
Primary loop (radioactive):
  Reactor → Hot water (315°C, 155 bar) → Steam generator → back to reactor

Secondary loop (clean):
  Steam generator → Turbine → Condenser → back to steam generator
```

| Property | Value |
|----------|-------|
| Coolant | Light water |
| Moderator | Light water |
| Fuel | Enriched UO₂ (3-5%) |
| Pressure | ~155 bar |
| Examples | Westinghouse AP1000, Framatome EPR |

**Advantage:** Two loops separate radioactive water from turbine.

### BWR (Boiling Water Reactor)

~15% of global fleet.

```
Single loop:
  Reactor → Steam directly → Turbine → Condenser → back to reactor
```

| Property | Value |
|----------|-------|
| Coolant | Light water (boils) |
| Moderator | Light water |
| Fuel | Enriched UO₂ |
| Pressure | ~75 bar |
| Examples | GE-Hitachi BWRX-300 |

**Simpler** but turbine is mildly radioactive.

### CANDU (Pressurized Heavy Water)

Canadian design. Uses natural uranium + heavy water (D₂O).

| Property | Value |
|----------|-------|
| Coolant | Heavy water |
| Moderator | Heavy water |
| Fuel | **Natural uranium** (no enrichment) |
| Examples | Canadian fleet, India, China |

**Advantage:** No enrichment needed. Can refuel while operating.

---

## Small Modular Reactors (SMRs)

| Property | Traditional | SMR |
|----------|-------------|-----|
| Capacity | 1,000+ MW | <300 MW |
| Construction | On-site (10+ years) | Factory-built, modular |
| Capital cost | $10B+ | Lower (in theory) |
| Siting | Limited locations | More flexible |

### SMR designs

| Company | Design | Type | Status |
|---------|--------|------|--------|
| **NuScale** | VOYGR | Light water PWR | NRC approved, projects cancelled |
| **GE-Hitachi** | BWRX-300 | Boiling water | Under review |
| **[[TerraPower]]** | Natrium | Sodium-cooled fast | Kemmerer, WY demo |
| **X-energy** | Xe-100 | High-temp gas | Under development |
| **[[Oklo]]** | Aurora | Fast reactor | Under development |
| **Kairos** | KP-FHR | Molten salt-cooled | Under development |

**Reality check:** No SMR has achieved commercial operation in US yet. Cost savings unproven. NuScale's first project cancelled due to cost overruns.

---

## Advanced reactor concepts (Gen IV)

### Molten Salt Reactors

Fuel dissolved in liquid salt. Can't melt down (already liquid).

| Advantage | Challenge |
|-----------|-----------|
| Inherently safe | Corrosion |
| High temperature (efficiency) | New materials needed |
| Can burn waste | Unproven at scale |

### Fast Reactors

Use fast (unmoderated) neutrons. Can "breed" fuel and burn waste.

| Advantage | Challenge |
|-----------|-----------|
| Breeds more fuel than consumes | Sodium coolant (reactive) |
| Burns long-lived waste | Proliferation concerns |
| 100x fuel efficiency | Complex |

[[TerraPower]] Natrium is sodium-cooled fast reactor.

### High-Temperature Gas Reactors

Helium-cooled, graphite-moderated. Very high temperatures for industrial heat.

---

## Nuclear fuel cycle

```
Mining → Conversion → Enrichment → Fabrication → Reactor → Storage/Reprocessing
```

| Step | What happens | Key players |
|------|--------------|-------------|
| **Mining** | Extract uranium ore | Cameco, Kazatomprom, Uranium Energy |
| **Conversion** | UO₂ → UF₆ (gas for enrichment) | Cameco, Orano |
| **Enrichment** | Increase U-235 % | Urenco, Rosatom, Centrus |
| **Fabrication** | Make fuel assemblies | Westinghouse, Framatome |
| **Reactor** | Generate power | Utilities |
| **Storage** | Spent fuel pools, dry casks | On-site at plants |
| **Reprocessing** | Recover U, Pu (optional) | France (Orano), Russia |

### Open vs closed cycle

| Cycle | Description | Countries |
|-------|-------------|-----------|
| **Open** | Once-through, store waste | US, most countries |
| **Closed** | Reprocess, recycle fuel | France, Russia, Japan |

**US policy:** No reprocessing (proliferation concerns). Spent fuel stored on-site indefinitely.

---

## Uranium supply

| Source | 2024 share |
|--------|------------|
| Kazakhstan | ~45% |
| Canada | ~15% |
| Namibia | ~10% |
| Australia | ~8% |
| Uzbekistan | ~7% |
| Russia | ~5% |

**Russia dependence:** Russia enriches ~40% of global uranium. US utilities still buy Russian enrichment services. Sanctions creating supply concerns.

See [[Uranium]], [[Kazatomprom]], [[Cameco]].

---

## Economics

### Capital costs

| Plant type | Overnight cost ($/kW) |
|------------|----------------------|
| Nuclear (new build) | $6,000-12,000 |
| Gas combined cycle | $1,000-1,500 |
| Solar utility | $800-1,200 |
| Wind onshore | $1,200-1,700 |

**Nuclear's problem:** Massive upfront cost, long construction (10+ years), cost overruns common.

### Operating costs

| Plant type | Marginal cost ($/MWh) |
|------------|-----------------------|
| Nuclear | ~$25-30 |
| Gas CC | ~$30-50 (fuel dependent) |
| Solar/Wind | ~$0 |

**Nuclear's advantage:** Once built, very cheap to run. 60+ year life. No fuel price volatility.

### Levelized cost (LCOE)

| Source | LCOE ($/MWh) |
|--------|--------------|
| New nuclear | $130-200 |
| Existing nuclear | $30-40 |
| Gas CC | $45-75 |
| Solar + storage | $50-80 |

**Implication:** Extending existing plants is economic. Building new is expensive. This is why the [[Nuclear renaissance]] focuses on relicensing and restarts.

---

## Regulatory framework (US)

| Agency | Role |
|--------|------|
| **NRC** | Licenses reactors, safety oversight |
| **DOE** | R&D, loan guarantees, HALEU supply |
| **FERC** | Wholesale power markets |

**Licensing timeline:** 5-10 years for new designs. NRC approval ≠ construction permit ≠ operating license.

**Relicensing:** Original 40-year licenses. Most plants extended to 60 years. Some pursuing 80 years (SLR - Subsequent License Renewal).

---

## Safety

### Defense in depth

Multiple independent barriers:
1. Fuel pellet ceramic
2. Fuel rod cladding
3. Reactor vessel
4. Containment building

### Major accidents

| Accident | Year | Cause | Deaths |
|----------|------|-------|--------|
| Three Mile Island | 1979 | Operator error, partial meltdown | 0 |
| Chernobyl | 1986 | Design flaw + operator error | ~50 direct, disputed long-term |
| Fukushima | 2011 | Tsunami, backup power failure | 1 (radiation), ~2,000 (evacuation) |

**Perspective:** Coal kills ~800,000/year from air pollution. Nuclear's safety record is excellent per TWh generated.

---

## Nuclear renaissance drivers

| Driver | Detail |
|--------|--------|
| **AI/data center demand** | Need 24/7 clean power |
| **Decarbonization** | Only proven clean baseload |
| **Energy security** | Reduce gas dependence |
| **Bipartisan support** | Rare policy consensus |
| **Hyperscaler demand** | [[Meta]], [[Microsoft]], [[Amazon]] signing nuclear deals |

See [[Nuclear renaissance]], [[Power constraints]].

---

## Key metrics for investors

| Metric | Definition | Use |
|--------|------------|-----|
| **Capacity factor** | Actual output / max | Operational excellence |
| **Refueling outage** | Days offline for refueling | Efficiency |
| **Fleet size (GW)** | Total capacity | Scale |
| **PPA price** | Contracted $/MWh | Revenue visibility |
| **License life** | Years remaining | Asset duration |

---

## Related

- [[Nuclear renaissance]] — current investment theme
- [[Uranium]] — fuel commodity
- [[Constellation Energy]] — largest US nuclear fleet
- [[Vistra]] — nuclear fleet owner
- [[Cameco]] — uranium producer
- [[Centrus Energy]] — US enrichment
- [[TerraPower]] — advanced reactor developer
- [[Oklo]] — SMR developer
- [[NuScale]] — SMR (struggling)
- [[Power constraints]] — why nuclear matters for AI
- [[Power grid primer]] — grid context
