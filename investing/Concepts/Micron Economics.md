---
aliases: [MU Economics, Micron Business Economics]
tags: [concept, memory, semiconductors, economics]
---
#concept #memory #semiconductors #economics

# Micron Economics

**Micron Economics** — the business economics of a memory company whose margin structure went from negative 9% gross margin (FY2023) to 81% (Q2 FY2026) in three years, driven by a structural shift from commodity DRAM to co-designed HBM with 18-42 month qualification lock-ins. The question is whether this represents a permanent regime change in memory economics or the most spectacular peak-margin signal in the industry's history.

---

## The story

Memory has always been a commodity business. For forty years the pattern held: prices spike, everyone builds fabs, eighteen months later there's oversupply and another crash. [[Micron]] lived this cycle more violently than most — it reported negative gross margins as recently as FY2023, when trailing twelve-month GM hit -9.1% and the company lost $5.8B on $15.5B revenue. All three survivors ([[Samsung]], [[SK Hynix]], Micron) came within quarters of financial crisis.

The economics were brutal because memory was fungible. A DDR4 DIMM from Samsung worked identically to one from Micron. JEDEC standards ensured the same pinouts, the same performance. Switching suppliers took days. Every price spike triggered the same response: customers switched to whoever was cheapest, manufacturers raced to add capacity, and margins collapsed.

The gross margin history tells the whole story of this cyclicality:

| Period | TTM Gross Margin | What happened |
|--------|-----------------|---------------|
| Q4 2018 | 59.6% | Peak of 2017-2018 DRAM supercycle — smartphone + server demand |
| Q2 2020 | 29.0% | Trough — oversupply after 2018 expansion, COVID uncertainty |
| Q1 2022 | 45.8% | WFH-driven demand + data center buildout |
| Q4 2023 | -14.5% | Worst in history — post-COVID demand cliff, inventory glut |
| Q2 2025 | 34.7% | Recovery starting — AI demand emerging |
| Q4 2025 | 45.3% | HBM revenue inflecting, DRAM pricing power returning |
| Q1 2026 | 58.4% | Approaching 2018 peak — but composition completely different |
| Q2 FY2026 | ~81% | Reported quarter — unprecedented for memory |

What changed is not the level of demand but its character. AI inference is memory-bound, not compute-bound. A million concurrent users on a 128K-token context window require 40TB of working memory just for conversation history. Video generation consumes 25x more memory than equivalent image models. The workload shifted from "memory needs to be big enough and fast enough" to "memory is the binding constraint."

[[HBM]] made the shift structural. Unlike commodity DRAM, HBM is a 3D stack of DRAM chips bonded directly to the GPU using through-silicon vias on a silicon interposer. Qualification takes 6-9 months minimum, sometimes 18-42 months for custom configurations. [[NVIDIA]]'s Blackwell GPU uses HBM qualified in 2023; the Vera Rubin platform uses HBM being qualified now. Revenue that shows up in 2027 is being locked in during 2025's qualification cycles.

The economics of this lock-in are transformative. HBM production consumes roughly 3 wafers of capacity for every 1 wafer of output (tighter tolerances, more testing, complex stacking). Every HBM wafer for an AI GPU is a wafer denied to commodity DDR5. As HBM production doubles (40%+ CAGR), standard DRAM supply tightens even as total wafer capacity grows. More production creates a worse shortage.

The margin math:

| Metric | Commodity DRAM era | HBM era (current) |
|--------|--------------------|--------------------|
| Gross margin range | -9% to 47% | 57% to 81% |
| Pricing mechanism | Spot/contract, quarterly reset | Multi-year LTAs, locked volumes |
| Customer switching cost | Days to weeks | 18-42 months (requalification) |
| Supply response time | 12-18 months | 3-5 years (new fabs) + 18-24 months (CoWoS packaging) |
| Revenue visibility | 1 quarter | 2-3 years |

Micron's HBM gross margins are accretive to both company and DRAM gross margins. HBM4 commands a ~50% price premium over HBM3E. The 2026 HBM supply is fully contracted — both price and volume locked. DDR5 is being bundled with HBM in some long-term agreements, pulling commodity DRAM pricing up with it.

The segment profitability tells you where the leverage is. In Q1 FY2026, gross margin fall-through (incremental gross profit per incremental dollar of revenue) hit +64.5% in mobile, +63.2% in automotive, and +44.1% in cloud. The mobile segment's strength is counterintuitive — it reflects the supply crunch from HBM cannibalization of consumer DRAM, not AI demand directly. Micron exited its Crucial consumer brand in February 2026, freeing capacity for higher-margin enterprise. When a supplier voluntarily exits consumer, the shortage is severe.

The capex trajectory reinforces the margin story. FY2024-2027 marks the first four consecutive years of capex growth in 25+ years. But capital intensity is dropping below 30% (vs 35% through-cycle guidance) because revenue is growing faster than capex. Idaho Fab 1 comes online mid-2027; Idaho Fab 2 starts construction 2026, operational end of 2028; New York fab targets 2030+. The supply response is measured in years, not quarters.

The bear case is the one that has worked for forty years: every memory cycle peaks, and this one will too. 81% gross margin is where the old pattern says to sell. If AI capex disappoints — [[OpenAI]] has suggested cutting planned infrastructure spend from $1.4T to ~$600B through 2030 — the demand side unwinds. When supply catches up (2028-2029 as new fabs come online), pricing reverts, and the margin structure compresses toward the historical 30-40% band. The market has always been right about peak margins in memory. Until it isn't.

The bull case is that AI broke the cycle. Memory is no longer fungible — co-designed HBM with custom features means "it is no longer possible to easily replace a rival's memory product" (SK Hynix, August 2025). The demand is elastic to price declines (cheaper inference → more inference consumption, unlike gadget cycles where lower DRAM prices don't cause people to buy a second phone). And the geopolitical fragmentation ([[China Micron ban June 2023]], CHIPS Act, export controls) has structurally split the global market, reducing effective supply in each region.

The answer probably lies between: not a permanent 80% GM business, but not a reversion to -9% either. The floor has moved up because the product has changed. The question is where the new floor settles.

---

## Reference

### Financials (fiscal year ends August)

| FY | Revenue | Gross Margin | Net Income | EPS | FCF |
|----|---------|-------------|------------|-----|-----|
| 2019 | $23.4B | 45.7% | $6.3B | $5.51 | — |
| 2020 | $21.4B | 30.6% | $2.7B | $2.42 | — |
| 2021 | $27.7B | 37.6% | $5.9B | $5.14 | $2.4B |
| 2022 | $30.8B | 45.2% | $8.7B | $7.75 | $3.1B |
| 2023 | $15.5B | -9.1% | -$5.8B | -$5.34 | -$6.1B |
| 2024 | $25.1B | 22.4% | $0.8B | $0.70 | $0.1B |
| 2025 | $37.4B | 39.8% | $8.5B | $7.59 | $1.7B |
| TTM Feb 2026 | $58.1B | 58.4% | $24.1B | $21.53 | $10.3B |

*Q2 FY2026 actual: $23.86B revenue, ~81% GM, $12.20 EPS. Q3 FY2026 guide: $33.5B.*

### HBM economics

| Metric | Value |
|--------|-------|
| HBM share of DRAM bits (2023) | ~1.5% |
| HBM share of DRAM bits (2025) | ~6% |
| HBM TAM (2025) | $35B |
| HBM TAM (2028E) | $100B |
| HBM CAGR | ~40% |
| HBM4 price premium over HBM3E | ~50% |
| DRAM wafer cannibalization ratio | ~3:1 (HBM vs standard) |
| Qualification timeline | 6-42 months |
| 2026 HBM supply | Fully contracted (price and volume) |

### DRAM pricing (2025-2026)

| Period | Contract DRAM price change |
|--------|---------------------------|
| Q4 2025 | +45-50% QoQ |
| Q1 2026E | +55-60% QoQ |
| LPDDR4X/5X Q1 2026 | +90% QoQ |
| NAND Q1 2026 | +33-38% QoQ |

### Capex and capacity

| Facility | Status | Timeline |
|----------|--------|----------|
| Idaho Fab 1 | Under construction | Mid-2027 first wafer |
| Idaho Fab 2 | Construction starting 2026 | End of 2028 |
| New York (Clay) | Groundbreaking Jan 2026 | 2030+ |
| Taiwan (Tongluo) | Acquired from [[Powerchip Semiconductor]] ($1.8B) | End FY2026 construction start |
| Singapore HBM packaging | On track | CY2027 |
| India back-end | Ramping | 2026 |

Total US investment commitment: $200B ($150B manufacturing + $50B R&D). CHIPS Act: $6.165B in grants + 25% investment tax credit.

---

## Related

- [[Micron]] — the company
- [[Micron Prices]] — absolute and relative price dynamics
- [[Memory shortage 2025-2026]] — the supply-demand context
- [[HBM economics]] — structural shift to HBM
- [[HBM]] — the product
- [[Memory squeeze thesis]] — investment thesis
- [[Long memory]] — thesis

*Created 2026-03-26*
