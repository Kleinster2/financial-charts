#concept #bottleneck #supplychain

AI chip supply chain has multiple bottlenecks beyond just foundry capacity.

---

## The stack of constraints

| Layer | Bottleneck | Status |
|-------|------------|--------|
| **Power** | 44GW US shortfall | Hard constraint, no solution in sight |
| **Materials** | InP substrates for optical | Shortage widening through 2026+ |
| **Foundry** | TSMC sub-3nm capacity | Tight, annual price hikes |
| **Packaging** | CoWoS | Tight, alternatives emerging ([[Intel]] EMIB, [[SK Hynix]]) |
| **Memory** | [[HBM]] | Shortage through CY26, fully contracted |
| **Test** | Final test for large packages | Hidden bottleneck, equipment lag |

---

## Key insight

Even if one layer loosens, others constrain. "Solving" fab capacity doesn't help if:
- Power isn't available
- Packaging is full
- [[HBM]] is allocated
- Materials are short

**Bottlenecks cascade and shift** — watch for which one becomes binding.

---

## Constraint flow thesis

[[Sriram Viswanathan]] ([[Celesta Capital]], ex-[[Intel Capital]]) articulated a sequential constraint migration model in March 2026: as each layer of AI infrastructure saturates, the bottleneck migrates downstream.

**The flow: GPU → Memory → Networking → Power management → Energy**

| Phase | Constraint | Investment window |
|-------|-----------|-------------------|
| **1. GPU** | Core compute | 2020–2024 (mostly played out at venture level) |
| **2. Memory** | [[HBM]], DRAM | Current — [[Micron]], SK Hynix supply-constrained |
| **3. Networking** | Interconnect, coherency | Emerging — [[Upscale AI]], [[Astera Labs]], [[Broadcom]] |
| **4. Power management** | In-rack power delivery | Next — data center power architecture |
| **5. Energy** | Raw generation, grid | Structural — [[Power constraints]], nuclear, BYOG |

Sriram's framing: "Where is the constraint moving? From GPU to memory to networking to power management to energy — that sort of flow is likely to occur." Each transition creates a venture window before incumbents consolidate — and Celesta has portfolio companies positioned at each layer.

**Watch signal:** [[Broadcom]] earnings language on networking supply constraints as indicator of Phase 3 intensifying.

---

## Materials layer (emerging)

InP (Indium Phosphide) substrates for optical interconnects:
- Supply: Sumitomo ([[Japan]]), AXT (US but [[China]] manufacturing)
- Demand: AI data center optical interconnects
- [[Gap]] widening, 20-30% capacity increases not enough
- [[China]] export controls on gallium/germanium/InP materials
- Workarounds: recycled wafers, customer-supplied substrates

---

## Related

- [[Power constraints]] — layer (44GW US shortfall, hardest)
- [[Advanced packaging]] — layer (CoWoS tight)
- [[Memory shortage 2025-2026]] — layer ([[HBM]] fully contracted)
- [[Final test bottleneck]] — layer (hidden constraint)
- [[TSMC]] — layer (sub-3nm capacity tight)
- [[Gallium]] — material ([[China]] export controls)
- [[Germanium]] — material ([[China]] export controls)
- [[Celesta Capital]] — constraint flow thesis source ([[Sriram Viswanathan]])
- [[Upscale AI]] — networking layer challenger
- [[NVLink]] — networking layer incumbent
