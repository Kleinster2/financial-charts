---
aliases: [Montage Technology, 澜起科技, 688008, 6809]
---
#actor #memory #china #semiconductor

**Montage Technology** (688008.SS / 6809.HK) — Chinese fabless memory interface chip designer. #1 globally with 36.8% market share (2024, Frost & Sullivan). Dual-listed on Shanghai STAR Market and [[HKEX]] (Feb 2026 debut). Founded 2004 in Shanghai. ~718 employees.

---

## Why Montage matters

Every server RDIMM and LRDIMM requires [[Memory interface chips|memory interface chips]] — RCDs, data buffers, clock drivers — to mediate between CPU and DRAM. Montage dominates this niche globally, selling into all three major DRAM makers: [[Samsung]], [[SK Hynix]], and [[Micron]]. The DDR5 transition increases chip count and ASP per module, and AI servers require far more DIMMs per node than traditional servers.

| Metric | Value |
|--------|-------|
| Tickers | 688008.SS (STAR), 6809.HK |
| Market cap | ~RMB 135B / ~$18.5B (A-share) |
| 2024 revenue | RMB 3.64B (~$500M) |
| 9M 2025 revenue | RMB 4.06B (+57.8% YoY) |
| Global market share | 36.8% (memory interconnect, 2024) |
| Customers | [[Samsung]], [[SK Hynix]], [[Micron]] |
| Gross margin | ~60% (interconnect: 64.8%) |
| Employees | ~718 |

---

## Price history

![[688008.SS-price-chart.png]]

*IPO on STAR Market at ~¥65 (Jul 2019), peaked ~¥130 in 2020 tech rally, ground through a brutal downcycle to ~¥42 by early 2023, then V-shaped recovery on DDR5 ramp and AI demand — now at all-time highs (~¥173) ahead of HK dual listing.*

---

## Financials

### Annual (RMB)

| Metric | FY2022 | FY2023 | FY2024 | YoY |
|--------|--------|--------|--------|-----|
| Revenue | 3.67B | 2.29B | 3.64B | +59.2% |
| Gross margin | 46.4% | 58.9% | 58.1% | -0.8pp |
| Net income | 1.30B | 451M | 1.41B | +213% |
| Net margin | ~35% | ~20% | ~38.8% | +19pp |

FY2023 was an industry-wide inventory destocking downcycle — revenue fell 39.5%. Gross margin paradoxically improved 12.5pp as the DDR5 mix (higher ASP, higher margin) increased while lower-margin DDR4 volumes dropped. FY2024 was a V-shaped recovery.

### Quarterly 2025 (RMB)

| Metric | Q1 | Q2 | Q3 | 9M 2025 |
|--------|----|----|----|----|
| Revenue | 1.22B | 1.41B | 1.42B | 4.06B |
| Rev YoY | +65.8% | +52.1% | +57.2% | +57.8% |
| Net income | 525M | 634M | 473M | 1.63B |
| NI YoY | +135% | +71.4% | +22.9% | +66.9% |
| Net margin | ~43% | ~45% | ~33% | ~40% |

TTM revenue (through Q3 2025): RMB 5.13B (+54% YoY). Analyst consensus: FY2025 ~RMB 5.6B. Q4 results expected ~March 2026.

### Segment breakdown (9M 2025)

| Segment | Revenue | YoY | Gross margin |
|---------|---------|-----|------|
| Interconnect chips (core) | RMB 3.83B | +61.2% | 64.8% |
| Jintide server platform | RMB 218M | +17.9% | lower |

---

## Product portfolio

### DDR5 memory interface chips (core)

Full companion chip suite for every DDR5 server DIMM:

| Chip | Function | Status |
|------|----------|--------|
| RCD (Registering Clock Driver) | Command/address hub on RDIMM | Gen4 (RCD04) mass production Oct 2025; 7200 MT/s |
| DB (Data Buffer) | Data path on LRDIMM | Shipping across DDR5 gens |
| CKD (Clock Driver) | Clock distribution for CUDIMM/CSODIMM | First to market; began revenue contribution 2024 |
| MRCD (Multiplexed Rank RCD) | Core controller for [[MRDIMM]] | Gen2 samples Jan 2025; 12,800 MT/s |
| MDB (Multiplexed Rank Data Buffer) | Data buffer for [[MRDIMM]] (1 MRCD + 10 MDB per module) | Gen2 samples Jan 2025 |
| SPD Hub | Serial presence detect | Shipping |
| TS (Temperature Sensor) | Thermal monitoring | Shipping |
| PMIC | Module power delivery | In portfolio |

New product revenue (PCIe Retimer + MRCD/MDB + CKD): RMB 422M in FY2024 (8x YoY). Q1 2025 alone: RMB 135M (+155% YoY).

### PCIe Retimers

| Product | Speed | Status |
|---------|-------|--------|
| PCIe 5.0 / CXL 2.0 | 32 GT/s, <5ns latency | Mass production since Jan 2023 |
| PCIe 6.x / CXL 3.x (M88RT61632) | 64 GT/s, PAM4, 43dB link budget | Customer sampling Jan 2025 |
| PCIe 7.0 | — | Engineering R&D |

One of only two major global suppliers of PCIe Retimer chips (per Frost & Sullivan). Critical for signal integrity in AI server rack-scale interconnects.

### CXL Memory Expansion Controller (MXC)

Targeting CXL-based memory pooling/disaggregation for AI workloads. Early stage.

### Jintide server platform

[[Intel]] Xeon CPUs repackaged with Montage's proprietary security features (PrC/DSC) for Chinese government, healthcare, and finance. Latest: Jintide C6P based on [[Intel]] Granite Rapids (Xeon 6P), up to 86 P-cores, DDR5-8000 MRDIMM support. Smaller revenue contributor (RMB 218M in 9M 2025).

---

## Competitive landscape

| Company | Share | Focus | Differentiation |
|---------|-------|-------|-----------------|
| Montage | 36.8% | Full DDR5 suite + PCIe Retimers + CXL | Volume leader; JEDEC board member; only Chinese player |
| [[Rambus]] | — | DDR5/MRDIMM chipsets + IP licensing | 41% of revenue from royalties; ~80% gross margin; IP moat |
| [[Renesas]] (ex-IDT) | — | DDR4/DDR5 RCDs, data buffers | Memory interface is small part of diversified $14B business |

Top 3 hold ~48% of global market. Montage leads on volume; [[Rambus]] on margins and IP. [[Renesas]] less focused. Montage sits on the [[JEDEC]] board and has led DDR5 RCD, MDB, and CKD standards development.

---

## AI / data center thesis

DDR5 content per server is structurally rising:
- AI training/inference servers use 8-24 DDR5 DIMMs per node (vs 4-8 in traditional servers)
- Each RDIMM requires 1 RCD; LRDIMMs need RCD + data buffers
- MRDIMMs need 1 MRCD + 10 MDB — dramatically higher chip count per module
- DDR5 penetration in servers accelerating from ~35% of DRAM shipments in 2024

HBM relationship is complementary, not competitive — AI servers with HBM-equipped GPUs ([[NVIDIA]], [[AMD]]) still need DDR5 DIMMs for CPU-attached memory. More AI servers = more DDR5 DIMMs = more Montage chips.

PCIe Retimers required for signal integrity across longer traces and active electrical cables in rack-scale AI clusters. CXL memory expansion is an emerging opportunity for memory-hungry AI workloads.

---

## Hong Kong dual listing

| Metric | Value |
|--------|-------|
| Exchange | [[HKEX]] (6809.HK) |
| IPO price | HK$106.89/share (top of range) |
| Raised | HK$7.04B (~$902M); HK$8.1B with overallotment |
| Debut | Feb 9, 2026 — surged ~57-64% on day one |
| Public tranche | 707x oversubscribed |
| Cornerstone investors | 17 (~$450M): UBS AM, Yunfeng Capital, JPMorgan AM |
| Sponsors | [[CICC]], [[Morgan Stanley]], [[UBS]] |
| Use of proceeds | R&D, capacity, brand, potential M&A |

A-H discount: HK offering priced ~50% below A-share, though gap narrowed on debut. Part of a wave of Chinese chip firms listing in HK alongside [[GigaDevice]].

---

## Intel relationship (declining)

[[Intel]] Capital was an early investor (2006, 2008; $175M for 10% in 2018). Systematically exiting:
- End 2023: 5.8% stake
- June 2024: Below 5% (no longer major shareholder)
- March 2025: No longer a related party
- Procurement declining: RMB 940M (2022) → 110M (2023) → 214M (2024)

---

## Valuation

| Metric | Value |
|--------|-------|
| Trailing P/E (A-share) | ~65x |
| vs STAR board avg | 51x (premium) |
| vs [[Rambus]] | ~45x (premium) |
| vs [[SMIC]] | 126x (discount) |

Significant growth priced in at current levels. The HK listing provides a second valuation anchor.

---

## Investment case

**Bull:**
- #1 global share in structural growth niche (DDR5 interface)
- AI servers multiply content per node — TAM expanding
- MRDIMM (1+10 chip architecture) is a step-function ASP increase
- 65% gross margin on interconnect chips, improving
- New products (CKD, MRCD/MDB, PCIe Retimer) scaling 8x YoY
- Dual listing = capital flexibility, international investor access
- JEDEC board seat = standards influence

**Bear:**
- ~65x trailing P/E prices in perfection
- [[Export controls]] — US restrictions could target foundry access or DRAM maker relationships
- Customer concentration: [[Samsung]], [[SK Hynix]], [[Micron]] are essentially the only buyers
- DDR generation transitions create periodic disruption
- Jintide depends on [[Intel]] cooperation, which regulators could restrict
- [[Rambus]] IP licensing moat provides margin resilience Montage lacks

---

## Key developments

- **Feb 2026:** HK listing debut (6809.HK), surged 57-64% day one
- **Oct 2025:** Gen4 DDR5 RCD (RCD04) mass production — 7200 MT/s
- **Jan 2025:** PCIe 6.x/CXL 3.x Retimer sampling; Gen2 MRCD/MDB samples
- **2025:** Jintide C6P launch (Granite Rapids-based); DDR6 and CXL 3.0 R&D underway

---

*Created 2026-01-05 · Updated 2026-02-09*

---

## Related

- [[GigaDevice]] — peer (HK secondary listing wave, Chinese memory)
- [[YMTC]] — peer ([[China]] memory ecosystem)
- [[SK Hynix]] — customer and competitor (memory interface)
- [[Samsung]] — customer (DRAM maker)
- [[Micron]] — customer (DRAM maker)
- [[Rambus]] — competitor (memory interface chips + IP licensing)
- [[Renesas]] — competitor (memory interface via IDT acquisition)
- [[Intel]] — declining investor, Jintide platform partner
- [[JEDEC]] — standards body (Montage board member)
- [[Export controls]] — key risk
- [[HKEX]] — dual listing venue
- [[SMIC]] — Chinese semiconductor peer (valuation comp)
