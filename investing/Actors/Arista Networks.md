---
aliases: [ANET, Arista]
---
#actor #networking #usa #public

**Arista Networks** (ANET) — Cloud networking company. Data center switches. AI cluster networking. 400G/800G leader. Founded 2004, HQ Santa Clara.

---

## Sector correlation

| Sector | ETF | Correlation |
|--------|-----|-------------|
| Technology | XLK | 0.68 |
| [[Semiconductors]] | SMH | 0.63 |
| Software | IGV | 0.56 |
| *S&P 500* | *SPY* | *0.59* |

ANET shows moderate Technology correlation (XLK r = 0.68).

---

## Why Arista matters

Critical AI infrastructure:

| Metric | Value |
|--------|-------|
| Ticker | ANET (NYSE) |
| Market cap | ~$120B |
| Revenue (FY2025) | $9.0B (+28.6% YoY) |
| Q4 2025 revenue | $2.49B (+28.9% YoY, +7.8% QoQ) |
| Q4 GAAP EPS | $0.75 (+21% YoY) |
| Q4 non-GAAP EPS | $0.82 (+24% YoY) |
| Q4 non-GAAP GM | 63.4% |
| Q4 operating margin | 47.5% |
| Q1 2026 guide | $2.6B |
| Focus | Data center switches, AI networking |

---

## AI networking opportunity

**GPU clusters need switches:**
- 10,000+ GPU clusters
- Ultra-low latency required
- High bandwidth (400G/800G)
- Arista dominates this

---

## Product portfolio

| Product | Use Case |
|---------|----------|
| EOS | Extensible Operating System — cloud-native, software-defined |
| 7800R3 | Spine switches |
| 7060X | Leaf switches |
| 7130 | Ultra-low latency |
| CloudVision | Network management |

---

## Customers

| Customer | Relationship |
|----------|--------------|
| Microsoft | Major customer |
| Meta | Major customer |
| Hyperscalers | Primary market |
| Enterprises | Growing segment |

Microsoft + Meta = significant revenue concentration.

---

## AI cluster architecture

**Spine-leaf topology:**
```
GPU Servers → Leaf Switches → Spine Switches
                    ↓
            All-to-all connectivity
```

Arista provides the switch fabric.

---

## Competitive landscape

| Competitor | Position |
|------------|----------|
| Cisco | Legacy, catching up |
| Juniper | HPE acquiring |
| NVIDIA (Mellanox) | InfiniBand competitor |
| Broadcom | Supplies merchant silicon |

---

## InfiniBand vs Ethernet

| Technology | Arista |
|------------|--------|
| Ethernet | Arista's domain |
| InfiniBand | NVIDIA's domain |
| AI clusters | Both used |
| Trend | Ethernet gaining share |

Arista benefits from Ethernet adoption in AI.

---

## Investment case

**Bull:**
- AI infrastructure buildout
- 400G/800G upgrade cycle
- Hyperscaler relationships
- Ethernet vs InfiniBand tailwind

**Bear:**
- Customer concentration (MSFT, META)
- NVIDIA InfiniBand competition
- High valuation
- Cisco fighting back

---

## Q4 2025 / FY2025 Earnings (Feb 12, 2026)

Blowout quarter — first time crossing $1B quarterly net income.

| Metric | Q4 2025 | Q4 2024 | YoY |
|--------|---------|---------|-----|
| Revenue | $2.49B | $1.93B | +28.9% |
| GAAP GM | 62.9% | 63.8% | -90bps |
| Non-GAAP GM | 63.4% | 64.2% | -80bps |
| GAAP net income | $955.8M | $801.0M | +19.3% |
| Non-GAAP net income | $1.047B | $849.6M | +23.2% |
| GAAP EPS | $0.75 | $0.62 | +21% |
| Non-GAAP EPS | $0.82 | $0.66 | +24% |

| Metric | FY2025 | FY2024 | YoY |
|--------|--------|--------|-----|
| Revenue | $9.006B | $7.003B | +28.6% |
| GAAP net income | $3.511B | $2.852B | +23.1% |
| GAAP EPS | $2.75 | $2.23 | +23.3% |
| Non-GAAP EPS | $2.98 | $2.32 | +28.4% |

**Key highlights:**
- 150 million cumulative ports shipped milestone
- Acquired **VeloCloud SD-WAN** portfolio from [[Broadcom]]
- Launched R4 series platforms for AI/data center networking
- Arista AVA: agentic AI for network operations
- ESUN (Ethernet for Scale-Up Networks) initiative with OCP
- Todd Nightingale appointed President
- **Q1 2026 guidance: $2.6B revenue** — implies continued ~25%+ growth

**Margin compression note:** Non-GAAP GM ticked down from 65.2% (Q3) to 63.4% (Q4) — likely mix shift toward higher-bandwidth AI networking equipment (400G/800G), which carries lower margins but higher ASPs.

---


![[anet-employees-chart.png]]
*Headcount: 5,115 (2025) — up 15.9% YoY*

## Quick stats

| Metric | Value |
|--------|-------|
| Ticker | ANET (NYSE) |
| Market cap | ~$120B |
| Revenue (FY2025) | $9.0B |
| Focus | Data center switches, AI networking |
| Key customers | [[Microsoft]], [[Meta]] |
| Q1 2026 guide | $2.6B |

*Updated 2026-03-20*

---

## Optical networking innovations

### XPO (eXtra-dense Pluggable Optics) - OFC 2026

Unveiled at OFC 2026 (March 13), [[Arista Networks]] launched XPO to counter [[Co-Packaged Optics]] density arguments:

**XPO specifications:**
- 12.8Tbps per module (8× current OSFP capacity)
- 64 lanes at 200Gbps per lane
- 204.8Tbps per rack unit (4× OSFP per RU)  
- Integrated liquid cooling cold plate (400W per module)
- 45 founding members in Multi-Source Agreement
- [[Microsoft]] backing provides hyperscaler credibility
- Volume production targeted 2027

**System impact:** In a 400MW data center with 128,000 GPUs, typical 1,400+ OSFP switch racks would drop by 75% with XPO density. This directly challenges the "pluggables have a density ceiling" narrative that CPO proponents use.

### LPO power efficiency - OFC 2025

Andy Bechtolsheim presented power comparison data at OFC 2025:
- At 1.6Tbps: DSP pluggable consumes 25W, CPO ~10W, LPO ~10W
- LPO matches CPO on power consumption while preserving pluggable serviceability
- LPO removes DSP from the pluggable module, shifts signal conditioning to switch chip
- Already deployed in [[NVIDIA]] Spectrum-X and [[Meta]] networks

---

## Related

- [[Microsoft]] — major customer
- [[Meta]] — major customer
- [[NVIDIA]] — competitor (InfiniBand) and adjacent (GPU clusters)
- [[Broadcom]] — supplier (merchant silicon)
- [[Cisco]] — competitor (legacy networking)
- [[HPE]] — competitor (via [[Juniper Networks]])
- [[Credo Technology Group]] — adjacent (cables in same clusters)
- [[AI hyperscalers]] — customer category
- [[Data Centers]] — customer vertical
- [[AI infrastructure]] — growth driver
- [[OFC 2026]] — XPO launch
- [[Ciena]] — competing CPO approach (Vesta)
- [[Co-Packaged Optics]] — XPO directly counters CPO density claims

