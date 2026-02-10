---
aliases: [memory interconnect chips, memory companion chips, DDR interface chips]
---
#concept #semiconductor #memory

Memory interface chips are the companion silicon required on every server DIMM module to mediate between the CPU's memory controller and the DRAM dies. They are not memory — they are the traffic cops that make memory work at speed.

---

## Why this matters

Every RDIMM, LRDIMM, and [[MRDIMM]] ships with mandatory interface chips specified by [[JEDEC]] standards. No module vendor can skip them. This creates a toll-booth business model: as long as servers use DIMMs, someone sells the companion chips.

The DDR5 generation is structurally better for interface chip vendors than DDR4:
- More chip types required per module (RCD + DB + SPD + TS + PMIC vs simpler DDR4 configs)
- Higher ASPs per chip (more complex silicon at faster speeds)
- New form factors ([[MRDIMM]], CUDIMM) add further chip count
- AI servers use 2-3x more DIMMs per node than traditional servers

---

## The chip stack

Each DDR5 server DIMM requires a combination of these companion chips:

| Chip | Full name | Function | Required on |
|------|-----------|----------|-------------|
| RCD | Registering Clock Driver | Command/address hub — routes CPU signals to DRAM ranks | Every RDIMM |
| DB | Data Buffer | Buffers data path between CPU and DRAM | LRDIMM only |
| CKD | Clock Driver | Distributes clock signal on clocked modules | CUDIMM, CSODIMM |
| MRCD | Multiplexed Rank RCD | High-speed command hub for multiplexed modules | [[MRDIMM]] only |
| MDB | Multiplexed Rank Data Buffer | Data buffering in 1+10 architecture (1 MRCD + 10 MDB) | [[MRDIMM]] only |
| SPD Hub | Serial Presence Detect | Stores module configuration data; sideband management | All DDR5 DIMMs |
| TS | Temperature Sensor | Thermal monitoring for throttling | All DDR5 DIMMs |
| PMIC | Power Management IC | On-module voltage regulation (new in DDR5) | All DDR5 DIMMs |

The DDR5 PMIC is a step change — DDR4 relied on motherboard voltage regulators, but DDR5 moved power management onto the module itself, adding a new chip to every DIMM.

---

## Content per server is expanding

| Module type | Interface chip count | Max speed | Use case |
|-------------|---------------------|-----------|----------|
| RDIMM (standard) | 1 RCD + SPD + TS + PMIC | 6,400 MT/s (DDR5-6400) | General-purpose servers |
| LRDIMM | 1 RCD + DBs + SPD + TS + PMIC | 6,400 MT/s | High-capacity servers |
| CUDIMM | 1 CKD + SPD + TS + PMIC | 6,400 MT/s | Client/workstation |
| [[MRDIMM]] | 1 MRCD + 10 MDB + SPD + TS + PMIC | 12,800 MT/s | AI/HPC (highest bandwidth) |

MRDIMM is the inflection — 11 high-value interface chips per module vs 1 RCD on standard RDIMM. [[Intel]] Granite Rapids (Xeon 6P) is the first platform to support MRDIMM.

---

## Market structure

Three companies dominate globally:

| Company | 2024 share | Differentiation |
|---------|-----------|-----------------|
| [[Montage]] | 36.8% | Volume leader, full DDR5 suite, only Chinese player, [[JEDEC]] board |
| [[Rambus]] | — | IP licensing moat (~41% of revenue from royalties), ~80% gross margin |
| [[Renesas]] (ex-[[IDT]]) | — | DDR4/DDR5 via 2019 IDT acquisition ($6.7B); small part of diversified business |

Top 3 hold ~48% of the global market. The remainder is fragmented across smaller players.

This is a standards-driven market — [[JEDEC]] defines the specifications, and all vendors implement to the same spec. Differentiation comes from:
- Generation leadership (first to market with each DDR5 speed grade)
- Yield and reliability at volume
- Breadth of portfolio (full suite vs single chip)
- Standards body influence (shaping the next spec)

---

## DDR generation transitions

Each DDR generation shift resets the competitive landscape temporarily:

| Transition | Timing | Effect on interface chips |
|------------|--------|--------------------------|
| DDR4 → DDR5 | 2022-2026 | Added PMIC, increased chip complexity, higher ASP |
| DDR5 → DDR6 | ~2028+ | R&D underway at [[Montage]]; spec not yet finalized by [[JEDEC]] |

During transitions, vendors with early silicon win design slots at [[Samsung]], [[SK Hynix]], and [[Micron]] that persist for the generation's life. Being late is costly.

---

## Relationship to HBM

[[HBM]] (High Bandwidth Memory) is a separate memory architecture — stacked DRAM dies connected via silicon interposer directly to GPU/accelerator packages. HBM does not use traditional interface chips (RCD, DB, etc.).

But HBM and DDR5 are complementary in AI servers: GPUs use HBM for high-bandwidth compute memory, while CPUs still need DDR5 DIMMs for system memory. More AI servers = more of both.

---

## Related

- [[Montage]] — #1 global market share (36.8%)
- [[Rambus]] — #2 competitor, IP licensing model
- [[Renesas]] — #3 competitor (IDT legacy)
- [[MRDIMM]] — highest interface chip content per module (1+10)
- [[JEDEC]] — standards body defining all interface chip specs
- [[Samsung]] — DRAM maker / module customer
- [[SK Hynix]] — DRAM maker / module customer
- [[Micron]] — DRAM maker / module customer
- [[Advanced packaging]] — related semiconductor concept
- [[AI datacenter architecture]] — demand driver
