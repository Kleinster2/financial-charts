#concept #moat #tsmc #manufacturing

**Advanced packaging** (2.5D, 3D, CoWoS) is how multiple chips are integrated into a single package. It's become a critical bottleneck for AI semiconductors.

---

## Why it matters

Modern AI accelerators aren't single chips — they're **systems** combining:
- GPU/CPU dies (logic)
- HBM (memory)
- Interposers (connection layer)

You can have the best GPU and the best HBM, but without packaging to integrate them, you have nothing shippable.

---

## Key technologies

| Technology | What it does |
|------------|--------------|
| **CoWoS** | TSMC's 2.5D packaging — silicon interposer connects GPU + HBM |
| **2.5D** | Chips sit side-by-side on interposer |
| **3D** | Chips stacked vertically |
| **HBM integration** | Memory stacks bonded to logic |

---

## Competitive landscape

| Player | Technology | Position |
|--------|------------|----------|
| [[TSMC]] | CoWoS | **Monopoly** on AI accelerators (NVIDIA, AMD) — capacity tight |
| [[SK Hynix]] | 2.5D | Indiana line 2028, turn-key HBM + packaging |
| [[Intel]] | EMIB, Foveros | Emerging CoWoS alternative for tier-2, US-based |
| [[Samsung]] | Various | Has packaging but trails on integration |
| [[ASE]]/Amkor/SPIL | OSAT | Could take overflow if Intel misses window |

---

## TSMC's packaging moat

Beyond foundry, TSMC locks in customers through CoWoS:
- NVIDIA's AI GPUs require CoWoS
- Capacity constrained — another allocation bottleneck
- Adds to [[Customer lock-in via co-design]]

---

## CoWoS allocation crisis (Jan 2026)

**NVIDIA has locked up >50% of TSMC's CoWoS capacity through 2027.**

| Customer | Impact |
|----------|--------|
| [[NVIDIA]] | >50% of CoWoS secured |
| [[Google]] | TPU production cut 4M → 3M units for 2026 |
| [[AMD]] | Exploring Samsung alternatives |
| [[Amazon]] | Capacity-constrained on custom chips |

**The math:** If NVIDIA has half, everyone else fights over the remainder. Google couldn't get enough CoWoS for planned TPU production — forced to cut 25%.

**This is why alternatives matter:** Intel EMIB, Samsung packaging, SK Hynix Indiana are now strategic, not just backup options.

---

## SK Hynix challenge (Dec 2025)

SK Hynix planning first 2.5D mass production line in West Lafayette, Indiana (2028):
- Currently depends on TSMC for packaging
- Turn-key model: HBM + packaging together
- Could disrupt TSMC's packaging monopoly
- "Korea's two semiconductor giants are basically trolling Taiwan" — Samsung on foundry, SK Hynix on packaging

---

## Intel EMIB as alternative (Jan 2026 update)

CoWoS capacity so tight that tier-2 chip makers exploring [[Intel]]'s EMIB:

**Who's looking:**
- Marvell, [[MediaTek]] actively trying EMIB
- Apple, Qualcomm adding "EMIB familiarity" to job posts
- Non-Intel customers already confirmed
- **[[Google]]** exploring Intel EMIB for TPU v9 (2027)
- **[[Broadcom]]** has placed orders

**EMIB advantages:**
- More affordable than CoWoS
- Good thermal performance
- Mature technology with solid track record
- US-based (TSMC back-end ships to Taiwan)

**Intel capacity expansion (New Mexico):**

| Capability | Expansion |
|------------|-----------|
| EMIB | +30% capacity |
| Foveros 3D | +150% capacity |

**New business model:** TSMC front-end wafer fab + Intel back-end packaging. Not impossible — integrating the two takes effort but works for lower-spec products.

**Window may be temporary:** If Intel fails to seize this opportunity, traditional OSATs ([[ASE]], Amkor, SPIL) take the overflow.

**Intel's angle:** If front-end foundry can't win customers, start with back-end packaging as beachhead into AI supply chain.

---

## Samsung turnkey bundle (Jan 2026)

**[[Samsung]]'s differentiation: TSMC doesn't make memory.**

Samsung offering integrated solution to hyperscalers:

| Component | Samsung offering |
|-----------|------------------|
| Foundry | SF2 (2nm) process |
| Advanced packaging | CoWoS alternative |
| Memory | HBM from Samsung |
| Integration | Single vendor, Texas facilities |

**Why "turnkey" matters:** Customers can get foundry + packaging + HBM from one vendor. TSMC requires separate memory sourcing (SK Hynix, Samsung, Micron) and coordination.

**Target customers:** [[Google]], [[AMD]], [[Amazon]] — all exploring Samsung as TSMC overflow.

**The trade-off:** Samsung yields still behind TSMC (~55-60% vs ~65%), but one-stop shopping has value when capacity is scarce.

---

## Implications

- Packaging is a **separate moat** from foundry
- AI chip supply chain has multiple bottlenecks: foundry AND packaging
- SK Hynix U.S. packaging could benefit from [[CHIPS Act]] and [[N-2 rule]] constraints on TSMC

---

*Updated 2026-01-04*

---

## Related

- [[TSMC]] — leader (CoWoS monopoly for AI accelerators)
- [[NVIDIA]] — capacity hog (>50% CoWoS locked through 2027)
- [[Google]] — constrained (TPU cut 4M→3M)
- [[SK Hynix]] — challenger (Indiana 2.5D line 2028)
- [[Intel]] — alternative (EMIB +30%, Foveros +150% expansion)
- [[Samsung]] — turnkey (foundry + packaging + HBM bundle)
- [[ASE]] — overflow (if Intel misses window)
- [[Customer lock-in via co-design]] — mechanism (CoWoS adds switching costs)
- [[CHIPS Act]] — enabler (US packaging investment)
- [[N-2 rule]] — context (constraints on TSMC packaging)
- [[Supply chain bottlenecks]] — context (packaging as constraint layer)
