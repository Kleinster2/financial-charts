#concept #energy #utilities #infrastructure #primer

**Power grid primer** — foundational electrical engineering and market concepts for energy investing. Understanding the grid helps evaluate data center constraints, renewable integration, and utility economics.

> **Key insight:** Electricity cannot be stored economically at scale. Supply must match demand in real-time, every second. This constraint shapes everything about how power markets work.

---

## The fundamental constraint

```
Generation = Demand + Losses (at all times)
```

Imbalance → frequency deviation → equipment damage → blackout.

| Frequency | Status | Action |
|-----------|--------|--------|
| 60.00 Hz (US) | Normal | None |
| 59.95 Hz | Low | Increase generation |
| 59.90 Hz | Critical | Shed load (rolling blackouts) |
| 60.05 Hz | High | Reduce generation |

**Why this matters:** Unlike other commodities, electricity has no inventory buffer. The grid is a just-in-time system operating at continental scale.

---

## Grid structure

```
Generation → Transmission → Distribution → Consumption
  (plants)    (high voltage)  (local)       (homes, data centers)
```

### Generation

| Type | Characteristics | Role |
|------|-----------------|------|
| **Baseload** | Runs 24/7, low marginal cost | Nuclear, coal, hydro |
| **Intermediate** | Follows demand, flexible | [[Natural gas]] combined cycle |
| **Peaker** | Fast start, expensive | Gas turbines, batteries |
| **Variable** | Depends on weather | Solar, wind |

### Transmission

High-voltage lines (115kV - 765kV) moving bulk power long distances.

| Voltage | Use | Loss rate |
|---------|-----|-----------|
| 765kV | Long-distance bulk | ~1% per 100 mi |
| 345kV | Regional backbone | ~2% per 100 mi |
| 115-230kV | Sub-transmission | Higher |

**Transmission bottleneck:** Building new lines takes 7-10+ years (permitting, NIMBYism). This limits where data centers can locate.

### Distribution

Lower voltage (4kV - 35kV) delivering to end users. Local utility responsibility.

---

## AC vs DC

| Property | AC | DC |
|----------|-----|-----|
| Long-distance transmission | Higher losses | Lower losses |
| Voltage conversion | Easy (transformers) | Complex (converters) |
| Grid standard | Universal | Point-to-point |
| Use | Everything | Undersea cables, long hauls |

**HVDC (High Voltage DC):** Used for very long distances, undersea cables, connecting asynchronous grids. More efficient but expensive converters.

---

## US grid structure

Three separate grids (interconnections):

| Interconnection | Coverage | Capacity |
|-----------------|----------|----------|
| **Eastern** | East of Rockies | ~700 GW |
| **Western** | West of Rockies | ~250 GW |
| **ERCOT** | Most of Texas | ~90 GW |

Grids operate independently at 60 Hz. Limited DC ties between them.

**ERCOT isolation:** Texas deliberately isolated to avoid federal regulation. Backfired in 2021 freeze (no imports available).

---

## Regional operators (RTOs/ISOs)

| Operator | Region | Key markets |
|----------|--------|-------------|
| **[[PJM]]** | Mid-Atlantic, Midwest | Largest US market |
| **MISO** | Central US | Wind integration |
| **ERCOT** | Texas | Energy-only market |
| **CAISO** | California | Solar integration |
| **NYISO** | New York | Congested, high prices |
| **ISO-NE** | New England | Gas dependence |
| **SPP** | Plains | Wind surplus |

RTOs coordinate dispatch, run markets, ensure reliability.

---

## Capacity vs energy

| Concept | Unit | What it measures |
|---------|------|------------------|
| **Capacity** | MW or GW | Maximum instantaneous output |
| **Energy** | MWh or GWh | Output over time |
| **Capacity factor** | % | Actual output / theoretical max |

| Source | Typical capacity factor |
|--------|------------------------|
| Nuclear | 90%+ |
| Coal | 40-50% |
| Gas CC | 40-60% |
| Wind | 25-40% |
| Solar | 15-25% |

**Capacity factor explains why:** A 1 GW nuclear plant produces ~2x the energy of a 1 GW solar farm annually.

---

## Power markets

### Energy market

Buy/sell electricity in real-time or day-ahead.

| Market | Timing | Purpose |
|--------|--------|---------|
| Day-ahead | 24 hrs before | Schedule generation |
| Real-time | 5-15 min | Balance deviations |

**Merit order:** Generators dispatched lowest marginal cost first.

```
Dispatch order (typical):
1. Nuclear, wind, solar (near-zero marginal cost)
2. Coal
3. [[Natural gas]] combined cycle
4. [[Natural gas]] peakers
```

**Price setting:** Last unit dispatched sets price for all. If gas sets price, everyone gets gas price — even zero-marginal-cost solar.

### Capacity market

Pay generators to be available, not just for energy produced.

| Market | Has capacity market? |
|--------|---------------------|
| PJM | Yes |
| MISO | Yes |
| NYISO | Yes |
| ERCOT | **No** (energy-only) |
| CAISO | Limited |

**Why capacity markets exist:** Energy-only prices too low to support investment in reliable generation. Capacity payments ensure plants stay available.

**ERCOT experiment:** No capacity market → relies on scarcity pricing (prices spike to $9,000/MWh) to incentivize investment. Volatile.

---

## Data center load growth

Data centers are transforming grid planning:

| Metric | 2020 | 2030E |
|--------|------|-------|
| US data center load | ~20 GW | ~50-90 GW |
| Share of US demand | ~3% | ~7-12% |

**Challenges:**
- Load growth after decades of flat demand
- Concentrated in specific regions (Virginia, Texas, Arizona)
- Need reliable 24/7 power (can't use intermittent)
- Want low-carbon power (corporate commitments)

See [[Power constraints]], [[BYOP]], [[Hyperscaler capex]].

---

## Interconnection queue

New generation must connect to the grid. Queue backlogs are massive:

| RTO | Queue backlog | Avg wait time |
|-----|---------------|---------------|
| PJM | 250+ GW | 4-5 years |
| MISO | 170+ GW | 3-4 years |
| CAISO | 200+ GW | 4+ years |

**Why so slow:** Studies required, transmission upgrades needed, limited staff, speculative projects clog queue.

**[[BYOP]] (Bring Your Own Power):** Hyperscalers bypassing queue by co-locating with existing generation or building behind-the-meter.

---

## Renewable integration challenges

### Intermittency

Solar produces during day, wind is variable. Doesn't match demand curve.

**Duck curve:** California phenomenon — solar floods midday, then disappears at sunset when demand peaks. Requires fast ramping or storage.

### Grid stability

Traditional generators provide:
- **Inertia:** Spinning mass resists frequency changes
- **Reactive power:** Voltage support
- **Black start:** Restart grid after outage

Solar/wind provide none of these inherently. Requires grid-forming inverters or keeping some traditional plants online.

### Curtailment

Sometimes too much renewable generation → negative prices → curtail (waste) power. California curtails 5-10% of solar in spring.

---

## Storage technologies

| Technology | Duration | Use case | Cost |
|------------|----------|----------|------|
| Li-ion batteries | 2-4 hours | Peak shaving, frequency | $$$ |
| Pumped hydro | 8-12 hours | Bulk storage | $$ (if geography exists) |
| Compressed air | 4-12 hours | Bulk storage | $$ |
| Hydrogen | Days-weeks | Seasonal | $$$$ (nascent) |
| Flow batteries | 4-12 hours | Long duration | $$$ |

**4-hour problem:** Li-ion economic for ~4 hours. Longer duration needs other technologies. See [[Form Energy]] (iron-air).

---

## Utility business models

### Regulated utilities

| Characteristic | Detail |
|----------------|--------|
| Revenue | Rate base × allowed ROE |
| Risk | Low (guaranteed return) |
| Growth | Capex → grows rate base |
| Examples | Southern Company, [[Duke Energy]] |

**Rate base:** Value of assets on which utility earns return. More investment = more earnings.

### Independent power producers (IPPs)

| Characteristic | Detail |
|----------------|--------|
| Revenue | Sell energy + capacity to market |
| Risk | Higher (merchant exposure) |
| Growth | Build/acquire plants |
| Examples | [[Vistra]], [[Constellation Energy]], NRG |

### Renewables/YieldCos

| Characteristic | Detail |
|----------------|--------|
| Revenue | Long-term PPAs |
| Risk | Low (contracted) |
| Growth | Acquire projects |
| Examples | [[Clearway]], NextEra |

---

## Key metrics for investors

| Metric | Definition | Use |
|--------|------------|-----|
| **Rate base** | Regulated asset value | Utility earnings driver |
| **Heat rate** | BTU per kWh | Gas plant efficiency |
| **Spark spread** | Power price − gas cost | Gas plant margin |
| **Dark spread** | Power price − coal cost | Coal plant margin |
| **Capacity price** | $/MW-day | IPP revenue |
| **PPA price** | $/MWh contracted | Renewable value |

---

## Related

- [[Power constraints]] — data center bottleneck
- [[BYOP]] — bring your own power
- [[PJM]] — largest US grid operator
- [[Vistra]] — IPP, nuclear fleet
- [[Constellation Energy]] — nuclear leader
- [[Nuclear renaissance]] — clean baseload
- [[Hyperscaler capex]] — demand driver
- [[Form Energy]] — long-duration storage
- [[Battery chemistry primer]] — storage technology
