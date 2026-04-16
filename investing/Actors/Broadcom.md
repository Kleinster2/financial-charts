---
aliases: [AVGO]
---
#actor #fabless #enabler #interconnect

# Broadcom (AVGO)

Fabless chip designer that enables hyperscaler custom AI silicon. Also major networking and optical player.

---

## Sector correlation

| Sector | ETF | Correlation |
|--------|-----|-------------|
| Technology | XLK | 0.82 |
| [[Semiconductors]] | SMH | 0.81 |
| Software | IGV | 0.66 |
| *S&P 500* | *SPY* | *0.74* |

AVGO trades as a core Technology name (XLK r = 0.82).

---

## Role in AI supply chain

Broadcom sits between hyperscalers and foundries:

```
Hyperscaler (spec) → Broadcom (design) → TSMC (fab) → Hyperscaler (consume)
```

They're not a hyperscaler — they're an enabler that provides:
- Custom AI chip design (ASICs)
- Networking silicon for AI clusters
- Switching and routing chips

---

## Key customers

| Customer | Product | Scale |
|----------|---------|-------|
| Google | TPU design | Massive (internal + cloud) |
| Anthropic | TPUv7 | ~1M units direct |
| Meta | Custom AI silicon | Large |
| OpenAI | [[Titan]] chips | $10B deal |
| Others | Various ASICs | Varies |

Anthropic deal (Jan 2026, per [[SemiAnalysis]]):
- ~1,000,000 TPUv7 units purchased directly from Broadcom
- Deployed in Anthropic-controlled facilities (not Google Cloud)
- DC infrastructure from [[TeraWulf]], [[Hut 8]], [[Cipher Mining]]
- [[FluidStack]] handles deployment operations
- Largest single TPU deployment ever

---

## Key risk: [[Hyperscaler disintermediation]]

See [[Hyperscaler chip roadmap]] for full details.

MediaTek appearing in designs:
- Google TPUv7e, TPUv8e
- [[Microsoft]] Maia 400
- Bytedance APU

This isn't just Google — it's spreading.

---

## Google disintermediation (original risk)

Google TPUv8 has two paths:
- Sunfish (TPUv8ax): Broadcom turnkey — full bundle, higher ASP
- Zebrafish (TPUv8x): Google sources wafers/memory directly, MediaTek for supporting chips

The economics:
- Broadcom charges ~55% margins on TPUs
- This costs Google ~$15B/year — a "tax"
- [[NVIDIA]] Blackwell in 2026 will restore GPU cost leadership
- Google must cut ASIC costs to compete with Blackwell unit economics
- Zebrafish isn't just diversification — it's survival

If volume shifts to Zebrafish, Broadcom loses ASP and margin. This is existential pressure, not just negotiation tactics.

---

## Optical/Interconnect business

**[[Co-Packaged Optics]] leadership:** Bailly CPO switch represents the industry's first volume production CPO switching platform — integrating 8 optical engines with Tomahawk 5 silicon for 51.2Tbps aggregate bandwidth. This positions [[Broadcom]] ahead of competitors in the CPO transition while maintaining dominance in traditional switching silicon.

**Power efficiency claims:** At 800Gbps ports, [[Broadcom]] data shows pluggable transceivers consuming 15W versus CPO at 5.5W — roughly 3× power reduction. However, CEO Hock Tan cautioned on March 2026 earnings: "We're not quite there yet" regarding CPO readiness for mass deployment.

**Silicon photonics platform:**
- Alternative to traditional optical (InP)
- Data center interconnect integration
- Competing with [[Coherent]], [[Lumentum]]

**Networking silicon dominance:**
- Tomahawk switch chips (Ethernet) — powers [[Arista Networks]] switches
- Jericho routing chips
- High-speed SerDes development
- 224G SerDes current generation, 448G+ facing physics challenges

**AI cluster connectivity:**
- Ethernet fabric silicon
- Competing with InfiniBand ([[NVIDIA]])
- NVLink alternatives for scale-out
- Scale-out networking leadership

[[Broadcom]] uniquely combines ASIC design capability with networking and optical integration — enabling both custom AI chips and the interconnects that connect them.

---

## Why it matters for this vault

- Every custom AI chip they design goes to [[TSMC]]
- Alternative to [[NVIDIA]] GPU path for hyperscalers
- Custom silicon trend = more foundry demand
- But doesn't change TSMC concentration — Broadcom is fabless and uses TSMC

---

## Chip sourcing

- Foundry: [[TSMC]] (95% of external wafers)
- [[Samsung]] exposure: Low — not exploring alternatives
- F26 purchase commitments: Only $106M — unusual flexibility while others fight for capacity

---

## Revenue mix shift

| Period | Non-AI % of semi | Non-AI revenue |
|--------|------------------|----------------|
| 1QFY22 | ~90% | ~$5.5B |
| Peak (1QFY23) | ~85% | ~$6.3B |
| 4QFY25 | ~40% | ~$4.6B |
| 1QFY26E | ~35% | ~$4.1B |

- Non-AI down 30% from peak, first y/y growth in 9 quarters
- Wireless = lowest margin in non-AI
- Rest of non-AI (networking, storage) = higher margin than XPU
- No sharp recovery expected in F26
- Implication: AI dependency deepening, legacy business structurally smaller

---

## Customer concentration (FY25)

| Metric | Value |
|--------|-------|
| Top 5 customers | 40% of revenue |
| Largest distributor | 32% of revenue |
| [[Apple]] | $7B+ |
| [[China]] | 17% ($7.6B) |
| Distributor channel | 48% of revenue |

High concentration = risk if Google (Zebrafish) or [[Apple]] reduce orders.

---

## For theses

- [[Long Broadcom]] — ASIC explosion thesis, $14.5B → $100B F27E
- [[Long TSMC]] — Broadcom's custom chips all go to TSMC, reinforces moat
- [[Short TSMC long Korea]] — neutral to bearish Korea; more TSMC demand, not [[Samsung]]

---

## Recent developments (Dec 2025)

OpenAI deal (Oct 2025):
- $10B commitment, 10GW capacity
- Custom [[Titan]] chips, H2 2026 production
- Stock +9% on announcement

Citi projections:
- F25: $14.5B ASIC revenue
- F26E: $50.5B (+248%)
- F27E: $100B (+98%)

Stock: +50% YTD, market cap $1.5T+

---

## Q1 FY2026 earnings (Mar 4, 2026)

Revenue $19.31B (+29% YoY), beat $19.18B estimate. Adj EPS $2.05 vs $2.03 estimate. AI revenue $8.4B (+106% YoY) — driven by custom AI accelerators and networking chips.

| Metric | Q1 actual | Estimate |
|--------|-----------|----------|
| Revenue | $19.31B (+29% YoY) | $19.18B |
| Adj EPS | $2.05 | $2.03 |
| AI revenue | $8.4B (+106% YoY) | — |
| Infra software | $6.80B (~+1% YoY) | $6.88B (miss) |

Q2 guidance well above Street: ~$22.0B vs $20.56B estimate. Q2 AI semiconductor revenue expected $10.7B. CEO Hock Tan: "Our AI revenue growth is accelerating." Expects to sell at least 1M chips by 2027 based on stacked design tech.

Infrastructure software segment grew only ~1% to $6.80B, missing the $6.88B estimate — the [[VMware]] integration not yet delivering revenue growth.

Announced new $10B share buyback program through end of year.

Key customers driving AI: [[Google]] (TPU design), [[OpenAI]] (custom processors). Big Tech expected to spend $630B+ on AI infrastructure this year.

Andrew Rocco ([[Zacks]]): "regardless of which software companies win the AI race, they are all investing in Broadcom's networking chips and custom accelerators."

Stock +3.8% after-hours (Mar 4), closed +4.8% on Mar 5.

### TPU revenue locked through 2031 (Apr 2026)

[[Anthropic]]'s expanded [[Google]] [[TPU]] deal (~3.5 GW starting 2027, confirmed by Anthropic and Google Cloud press releases Apr 6) includes a Broadcom supply assurance agreement through 2031. [[Mizuho]] estimates $80B+ cumulative revenue for Broadcom from this commitment — the longest confirmed ASIC design lock-in. AVGO +6% on announcement. [[MediaTek]]'s competing TPU design work faces delays: [[TSMC]] CoWoS packaging bottleneck plus Google engineering changes pushed tape-out to mid-2026, volume production unlikely before 2027 (Digitimes, SemiWiki). [[OpenAI]] is also working with Broadcom on custom chips, extending the customer base beyond Google/Anthropic.

*Sources: Anthropic press release (Apr 6), Google Cloud press release (Apr 6), Bloomberg (Apr 6), Mizuho (Apr 7), Digitimes (Apr 7)*

Earnings call customer detail (6 XPU customers confirmed):

| Customer | Status | 2027 outlook |
|----------|--------|--------------|
| [[Google]] | Shipping (TPU) | Continued ramp |
| [[Meta]] | Shipping (MTIA) | Alive and shipping |
| [[OpenAI]] | Development ([[Titan]]) | First-gen XPU in volume, >1GW |
| [[Anthropic]] | Ramping (TPUv7) | Demand >3GW |
| Customer 5 | Undisclosed | Shipments >2x in 2027 |
| Customer 6 | New (undisclosed) | — |

CEO Hock Tan: line of sight to installed capacity approaching 10GW by 2027 and AI chip revenue exceeding $100B in 2027. Broadcom argues hyperscalers cannot replicate its custom silicon design capability — "they need us."

*Sources: Reuters Mar 4, CNBC, Sherwood News, TrendForce Mar 5 2026*

---

![[avgo-employees-chart.png]]
*Headcount: 33,000 (2025) — down 10.8% YoY*

## ASIC margin math — Jensen's rebuttal (Dwarkesh, Apr 15, 2026)

[[Jensen Huang]] addressed the "ASICs win on cost" thesis head-on: [[Broadcom]]'s ASIC business runs ~65% gross margin vs [[NVIDIA]]'s ~70%. The headline margin spread is 5 points — the entire advantage ASIC buyers capture on the bill-of-materials side.

**Why Jensen argues this is small.** Against the full stack [[NVIDIA]] delivers ([[CUDA moat|CUDA]], networking via [[Mellanox]], packaging via [[TSMC]] [[CoWoS]], system-level optimization, deployment tooling), the 5-point spread is a rounding error. Customers who choose ASICs save marginally on silicon cost but absorb cost at every other layer — integration, tooling, ecosystem gaps, deployment latency.

**Framing implication for Broadcom:** The Broadcom thesis that custom silicon captures economics from NVIDIA at the frontier is reframed as a shift at the margin, not at the structural level. Broadcom's ASIC business grows alongside NVIDIA, not at its expense, in Jensen's read. [[Google]] runs [[TPU]] and buys NVIDIA GPUs simultaneously; [[Meta]] runs [[MTIA]] and buys Blackwell; [[OpenAI]] runs [[Titan]] and takes $30B from NVIDIA.

**Counterpoint the vault tracks:** the bull case for Broadcom has always been that custom silicon captures *incremental* AI spend — not that it displaces existing NVIDIA installed base. Jensen's 65% vs 70% framing is consistent with that read, not a refutation of it. See [[Hyperscaler disintermediation]] for the unresolved debate.

---

## Quick stats

| Metric | Value |
|--------|-------|
| Ticker | AVGO (NASDAQ) |
| Market cap | ~$1.1T |
| Revenue (FY25) | ~$64B |
| Revenue (FY26E) | ~$97B |
| Revenue (FY27E) | ~$133B |
| AI revenue (FY25) | ~$14.5B |
| AI revenue (F27E) | $100B (Citi) |
| Gross margin | ~65% |
| Dividend yield | ~1.1% |

*Updated 2026-04-16 — Jensen ASIC margin rebuttal*

![[avgo-price-chart.png]]

![[avgo-fundamentals.png]]

*Note: The 2017/2018 profit spike reflects one-time tax benefits from the [[Tax Cuts and Jobs Act]] (Dec 2017), not operating performance.*

---

## Related

- [[Google]] — major customer (TPU design), disintermediating
- [[Anthropic]] — customer (~1M TPUv7 direct purchase)
- [[Meta]] — customer (custom ASICs)
- [[OpenAI]] — customer ($10B [[Titan]] chip deal)
- [[TSMC]] — foundry (95% of wafers)
- [[NVIDIA]] — competitor (GPU vs ASIC)
- [[MediaTek]] — competitor (Zebrafish threat)
- [[Coherent]] — competitor (optical)
- [[Lumentum]] — competitor (optical)
- [[Co-Packaged Optics]] — Bailly CPO switch, first volume production platform
- [[Arista Networks]] — customer (networking silicon)
- [[TeraWulf]], [[Hut 8]], [[Cipher Mining]] — DC partners for Anthropic TPUs
- [[FluidStack]] — deployment partner for Anthropic
- [[Long Broadcom]] — thesis
- [[Hyperscaler chip roadmap]] — disintermediation risk context
