#concept #space #satellite #infrastructure #primer

**Satellite primer** — foundational orbital mechanics, satellite technology, and space economics concepts for space sector investing. Understanding satellites helps evaluate constellation economics, launch costs, and competitive dynamics.

> **Key insight:** Space is becoming infrastructure, not exploration. The economics changed when reusable rockets cut launch costs 90%. Now it's about deploying capital-efficient constellations at scale.

---

## Orbital mechanics basics

### Orbits by altitude

| Orbit | Altitude | Period | Latency | Use |
|-------|----------|--------|---------|-----|
| **LEO** | 200-2,000 km | 90-120 min | 20-40 ms | Broadband, imaging |
| **MEO** | 2,000-35,786 km | 2-12 hrs | 100-150 ms | Navigation (GPS) |
| **GEO** | 35,786 km | 24 hrs | 600+ ms | Broadcast, weather |
| **HEO** | Elliptical | Variable | Variable | Polar coverage |

### Why altitude matters

| Factor | LEO | GEO |
|--------|-----|-----|
| **Latency** | Low (good for internet) | High (bad for internet) |
| **Coverage per sat** | Small footprint | Large footprint |
| **Satellites needed** | Many (thousands) | Few (tens) |
| **Launch cost** | Lower per sat | Higher per sat |
| **Satellite life** | 5-7 years | 15+ years |
| **Atmospheric drag** | Yes (requires station-keeping) | No |

**LEO tradeoff:** Low latency requires massive constellations. Each satellite covers small area, moves fast (90-min orbit).

---

## Satellite types by function

### Communications

| Type | Orbit | Examples |
|------|-------|----------|
| Broadband internet | LEO | **Starlink**, OneWeb, Kuiper |
| Direct-to-cell | LEO | Starlink, AST SpaceMobile |
| Broadcast (TV) | GEO | DirecTV, Dish |
| Backhaul | GEO/MEO | SES, Intelsat |

### Earth observation

| Type | Resolution | Examples |
|------|------------|----------|
| Optical imaging | 30cm-10m | Planet, Maxar, BlackSky |
| SAR (radar) | 1-25m | Capella, ICEYE, Umbra |
| Hyperspectral | Variable | Pixxel |
| Weather | Variable | NOAA, EUMETSAT |

### Navigation

| System | Operator | Orbit |
|--------|----------|-------|
| **GPS** | US | MEO |
| **Galileo** | EU | MEO |
| **GLONASS** | Russia | MEO |
| **BeiDou** | China | MEO + GEO |

---

## Constellation economics

### LEO broadband model

```
Revenue = Subscribers × ARPU × 12

Costs:
- Satellite manufacturing
- Launch
- Ground infrastructure
- Operations
- Spectrum fees
```

### Starlink economics (estimated)

| Metric | Value |
|--------|-------|
| Satellites deployed | ~6,000+ |
| Manufacturing cost | ~$250K per sat |
| Launch cost (Falcon 9) | ~$15M for 60 sats |
| Per-sat launch cost | ~$250K |
| Total per sat | ~$500K |
| Subscribers | ~4M+ |
| ARPU | ~$100/month |
| Revenue run-rate | ~$5B+ |

**Unit economics improving:** SpaceX manufactures at scale, launches on own rockets, iterating fast.

### GEO economics

| Metric | Typical |
|--------|---------|
| Satellite cost | $200-500M |
| Launch cost | $100-200M |
| Lifespan | 15+ years |
| Annual depreciation | $20-40M |
| Revenue per transponder | $1-3M/year |

**GEO challenge:** High upfront cost, long payback, technology risk over 15-year life.

---

## Launch economics

### Cost per kg to orbit

| Era | Cost/kg to LEO |
|-----|----------------|
| Space Shuttle | ~$54,000 |
| Atlas V | ~$13,000 |
| Falcon 9 (expendable) | ~$2,700 |
| Falcon 9 (reusable) | ~$1,500 |
| Starship (target) | ~$100-200 |

**Reusability revolution:** SpaceX reuses Falcon 9 boosters 20+ times. Each reuse amortizes fixed cost.

### Launch providers

| Provider | Vehicle | Reusable | Cost/kg |
|----------|---------|----------|---------|
| **SpaceX** | Falcon 9, Starship | Yes | Lowest |
| **Rocket Lab** | Electron, Neutron | Partial | Medium (small sats) |
| **ULA** | Vulcan | Partial | Higher |
| **Arianespace** | Ariane 6 | No | Higher |
| **China** | Long March | Some | Medium |
| **Blue Origin** | New Glenn | Yes (planned) | TBD |

### Starship impact

| Capability | Falcon 9 | Starship |
|------------|----------|----------|
| Payload to LEO | 22 tons | 100-150 tons |
| Cost per launch | ~$70M | ~$10-20M (target) |
| Fairing size | 5.2m | 9m |
| Reusability | Booster only | Full (booster + ship) |

**If Starship works:** Launch costs drop another 10x. Changes economics of everything in space.

---

## Spectrum and regulatory

### Spectrum basics

Satellites communicate via radio frequencies. Spectrum is limited and regulated.

| Band | Frequency | Use |
|------|-----------|-----|
| **L-band** | 1-2 GHz | Mobile, navigation |
| **S-band** | 2-4 GHz | Weather, some mobile |
| **C-band** | 4-8 GHz | Traditional satcom |
| **Ku-band** | 12-18 GHz | Broadcast, broadband |
| **Ka-band** | 26-40 GHz | High-throughput broadband |
| **V-band** | 40-75 GHz | Future capacity |

### ITU coordination

International Telecommunication Union allocates orbital slots and spectrum.

- **Filing priority:** First to file, first served
- **Milestone requirements:** Must deploy within timeframe or lose rights
- **Interference coordination:** Must coordinate with neighbors

**Starlink advantage:** Filed early for massive spectrum allocation. Competitors struggle to match.

---

## Ground infrastructure

### Ground stations

| Component | Purpose |
|-----------|---------|
| **Gateways** | Connect constellation to internet backbone |
| **User terminals** | Customer equipment (dishes) |
| **TT&C** | Telemetry, tracking, command |

### Inter-satellite links (ISLs)

Laser links between satellites. Reduce ground station dependency.

| Benefit | Value |
|---------|-------|
| Lower latency | Light through space faster than fiber through ground |
| Coverage | Serve areas without ground stations (oceans, poles) |
| Resilience | Less ground infrastructure needed |

**Starlink ISLs:** Deploying laser links across constellation. Competitive advantage.

---

## Satellite manufacturing

### Traditional approach

| Characteristic | Value |
|----------------|-------|
| Build time | 2-3 years |
| Cost | $200M-500M (GEO comms) |
| Customization | High |
| Manufacturers | Airbus, Boeing, Lockheed, Northrop |

### New space approach

| Characteristic | Value |
|----------------|-------|
| Build time | Weeks-months |
| Cost | $250K-5M (LEO) |
| Standardization | High |
| Manufacturers | SpaceX (in-house), Planet, Spire |

**Vertical integration:** SpaceX builds satellites, launches them, operates them. Captures full stack economics.

---

## Key players

### Launch

| Company | Status |
|---------|--------|
| **[[SpaceX]]** | Dominant (~90% of commercial mass to orbit) |
| **[[Rocket Lab]]** | #2, growing with Neutron |
| **ULA** | Government-focused |
| **Blue Origin** | New Glenn in development |

### Broadband constellations

| Constellation | Operator | Satellites | Status |
|---------------|----------|------------|--------|
| **Starlink** | SpaceX | ~6,000+ deployed | Operating, profitable |
| **Kuiper** | Amazon | 3,236 planned | Launching 2025 |
| **OneWeb** | Eutelsat | ~600 | Operating |
| **Lightspeed** | Telesat | 298 planned | In development |

### Earth observation

| Company | Focus |
|---------|-------|
| **Planet** | Daily global imaging |
| **Maxar** | High-resolution imagery |
| **BlackSky** | Real-time intelligence |
| **Capella** | SAR (sees through clouds) |

---

## Business models

### Capacity-based (traditional)

Sell transponder capacity or bandwidth to customers. Wholesale model.

| Metric | Definition |
|--------|------------|
| Transponder | Unit of satellite capacity |
| Fill rate | % of capacity sold |
| ARPU | Revenue per transponder |

### Consumer broadband (Starlink)

Sell direct to consumers and businesses.

| Metric | Definition |
|--------|------------|
| Subscribers | Paying customers |
| ARPU | Monthly revenue per sub |
| Churn | Customer cancellation rate |
| CAC | Customer acquisition cost |

### Data-as-a-service (EO)

Sell imagery or analytics, not raw capacity.

| Model | Description |
|-------|-------------|
| Imagery subscription | Access to satellite images |
| Analytics | Derived insights (crop health, ship tracking) |
| Government contracts | Defense, intelligence |

---

## Key metrics for investors

| Metric | What it measures |
|--------|------------------|
| **Satellites deployed** | Constellation progress |
| **Subscribers** | Demand, market fit |
| **Launch cadence** | Deployment capability |
| **Cost per sat** | Manufacturing efficiency |
| **Backlog** | Future revenue visibility |
| **ARPU** | Pricing power |
| **Capacity utilization** | Asset efficiency |

---

## Risks

| Risk | Description |
|------|-------------|
| **Launch failure** | Can lose multiple satellites |
| **Technology obsolescence** | 15-year GEO sats vs fast LEO iteration |
| **Competition** | Starlink dominance |
| **Space debris** | Kessler syndrome risk |
| **Regulatory** | Spectrum, orbital slots |
| **Capital intensity** | Billions before breakeven |

---

## Related

- [[Space]] — sector overview
- [[SpaceX]] — launch and Starlink leader
- [[Rocket Lab]] — small launch pioneer
- [[Planet Labs]] — earth observation
- [[Amazon]] — Project Kuiper
- [[Defense]] — government customer
