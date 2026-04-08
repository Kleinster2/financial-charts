#concept #datacenter #infrastructure #ai

**Data center infrastructure** — The physical supply chain enabling AI buildout: power distribution, cooling, racks, security, building automation. Critical bottleneck as hyperscaler capex explodes.

---

## Supply chain map

![[dc-supplier-map-quartr.png]]
*Source: Quartr Pro. Note: "very fragmented space and this list is not to be relied upon as exhaustive."*

---

## Subsystems and key players

### Power distribution

| Subsystem | Function | Key players |
|-----------|----------|-------------|
| **MV distribution** | Medium voltage switchgear, transformers | [[ABB]], [[Schneider Electric]], [[Eaton]], [[Siemens]], [[Vertiv]], [[Delta Electronics]] |
| **LV distribution** | Low voltage to racks | [[Eaton]], [[Vertiv]], [[Schneider Electric]], [[Legrand]], [[ABB]] |
| **UPS** | Uninterruptible power | [[Eaton]], [[Vertiv]], [[Schneider Electric]], [[ABB]], [[Delta Electronics]] |
| **Backup power** | Generators | [[Caterpillar]], [[Generac]], Kohler, Rolls-Royce |

### Thermal management

| Subsystem | Function | Key players |
|-----------|----------|-------------|
| **HVAC/Cooling** | Air and liquid cooling | [[Vertiv]], [[Schneider Electric]], [[Trane Technologies]], [[Carrier Global]], [[Daikin]], [[Munters]], Stulz, Asetek |
| **Liquid cooling** | Direct-to-chip, immersion | [[Vertiv]], [[Trane Technologies]], [[nVent Electric]], Asetek, [[Modine Manufacturing]] |

### Physical infrastructure

| Subsystem | Function | Key players |
|-----------|----------|-------------|
| **Server cabinets** | Racks, enclosures | [[Vertiv]], [[Eaton]], [[Legrand]], [[nVent Electric]], Rittal, [[Dell]] |
| **Building automation** | BMS, DCIM | [[Siemens]], [[Johnson Controls]], [[Honeywell]], [[Schneider Electric]], [[Cisco]] |
| **Security systems** | Physical + cyber | [[Palo Alto Networks]], [[Fortinet]], [[Honeywell]], Bosch, Assa Abloy |

---

## Diversified vs pure-play

**Multi-segment leaders** (appear in 4+ categories):
- [[Eaton]] — power distribution, UPS, racks
- [[Vertiv]] — cooling, UPS, racks, monitoring
- [[Schneider Electric]] — power, cooling, racks, software
- [[ABB]] — power distribution, automation
- [[Delta Electronics]] — power supplies, UPS, fans

**Pure-plays by segment:**

| Segment | Pure-play |
|---------|-----------|
| Cooling | [[Vertiv]], [[Trane Technologies]], [[Munters]], Asetek |
| Backup power | [[Generac]], [[Caterpillar]] |
| Enclosures | [[nVent Electric]], Rittal |
| HVAC | [[Daikin]], [[Carrier Global]], [[Trane Technologies]] |

---

## Performance comparison

![[dc-infrastructure-comparison.png]]
*[[Vertiv]] (+3100%) dominates as DC pure-play. [[nVent Electric|NVT]] (+600%) also outperforms diversified peers [[Eaton|ETN]], [[Trane Technologies|TT]], [[Carrier Global|CARR]] (+400%). Since Jan 2020.*

---

## Investment implications

**Thesis:** AI buildout requires massive physical infrastructure. Hyperscaler capex → infrastructure suppliers.

**Bottlenecks favor suppliers:**
- Power equipment: 18-24 month lead times
- Custom cooling: limited capacity
- High-power racks: specialized manufacturing

**Bull case:**
- [[Hyperscaler capex]] at record levels
- AI DC density increasing (100+ kW/rack)
- Liquid cooling transition just starting
- Grid modernization parallel tailwind

**Bear case:**
- Cyclical capex risk
- Competition intensifying
- Customer concentration (hyperscalers)
- Valuation stretched after 2023-2025 rally

---

## Quick stats

| Metric | Value |
|--------|-------|
| Global DC market | ~$350B (2025) |
| AI DC CAGR | 28% (2025-2034) |
| Power equipment | 18-24 mo lead times |
| Liquid cooling TAM | $4.2B → $13.2B by 2029 |

---

## Recent events

### $14B+ debt issuance pipeline (Apr 2026)

[[Rick Rieder]] ([[BlackRock]], Apr 7 Bloomberg): ~$14B in data center/AI infrastructure debt issuance expected over the next couple of weeks. Rieder expects the market to absorb it without difficulty — hyperscalers are "in great shape from a leverage point of view" and some names will be new issuers entering the bond market for the first time. Credit markets have massive cash reserves ($7.8T in [[Money market funds|money market funds]]) and real institutional buyers (insurance companies, pension funds) stepping in as yields back up.

Rieder's caveat: some of the biggest-name issuance is pricing at very tight spread levels — "from a return perspective, not that interesting." He prefers equity, convertibles, or loans-with-warrants for technology exposure, where upside potential is materially greater than the carry pickup on tight IG debt. Earlier-stage issuers pricing wider are more appealing.

This pipeline connects to the [[AI infrastructure financing risk]] question: whether the pace of capital-intensive buildout can be sustained if geopolitical uncertainty ([[2026 Strait of Hormuz crisis|Iran crisis]]) persists and borrowing costs remain elevated.

- [[2026 HVAC antitrust lawsuit]] — March 26 selloff: CARR -4.0σ, TT -3.0σ, NVT -2.6σ (basket, not named), JCI -2.5σ. Triple headwind: Rubin chiller-free + antitrust + [[Watsco]] demand softness.

---

## Related

- [[AI datacenter architecture]] — design requirements
- [[Power constraints]] — enabling bottleneck
- [[Hyperscaler capex]] — demand driver
- [[GPU deployment bottleneck]] — infrastructure as constraint
- [[Thermal limits]] — cooling requirements
- [[BYOP]] — on-site power generation
- [[Long datacenter infrastructure]] — thesis

### Power & electrical
- [[Eaton]] — power distribution, UPS
- [[Vertiv]] — cooling, power (pure-play)
- [[Schneider Electric]] — power, cooling, software
- [[ABB]] — power distribution, automation
- [[Delta Electronics]] — power supplies, UPS (Taiwan)
- [[Generac]] — backup generators
- [[Caterpillar]] — large generators
- [[Siemens Energy]] — gas turbines

### Events
- [[2026 HVAC antitrust lawsuit]] — HVAC cartel class-action, March 2026

### Cooling & HVAC
- [[Trane Technologies]] — HVAC, liquid cooling
- [[Carrier Global]] — HVAC, QuantumLeap
- [[Daikin]] — world's largest HVAC
- [[Munters]] — humidity, precision cooling
- [[Modine Manufacturing]] — liquid cooling
- [[nVent Electric]] — enclosures, liquid cooling

### Racks & enclosures
- [[Legrand]] — PDUs, cable management
- [[nVent Electric]] — enclosures

### Automation & security
- [[Johnson Controls]] — building automation
- [[Honeywell]] — automation, security
- [[Palo Alto Networks]] — cybersecurity
- [[Fortinet]] — cybersecurity

### Cross-vault
- [Technologies: Data Center Infrastructure](obsidian://open?vault=technologies&file=Data%20Center%20Infrastructure) — power delivery, cooling architectures, networking topology

