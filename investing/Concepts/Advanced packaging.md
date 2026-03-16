#concept #moat #tsmc #manufacturing

**Advanced packaging** (2.5D, 3D, CoWoS) is how multiple chips are integrated into a single package. It's become a critical bottleneck for AI semiconductors.

---

## Why it matters

Modern AI accelerators aren't single chips — they're **systems** combining:
- GPU/CPU dies (logic)
- [[HBM]] (memory)
- Interposers (connection layer)

You can have the best GPU and the best [[HBM]], but without packaging to integrate them, you have nothing shippable.

---

## Packaging fundamentals

A bare die from the fab is worse than useless — it will get contaminated, damaged, and can't connect to anything. Packaging serves three purposes: **protection** (physical/chemical), **connection** (to the PCB), and **translation** (from microscopic die signals to macroscopic board signals).

The north star: **maximize interconnect density** — how many connections per mm² from chip to outside world. Equivalently, minimize **pitch** (spacing between interconnects). Denser interconnects = faster data movement between chips = better GPU performance.

## Technology evolution

### Wirebonding (1960s-1990s)
Tiny gold wires connect chip to package like miniature suspension bridges. Simple and cheap, but wires create electrical bottlenecks and only use the edges of the chip — limited surface area for connections. Still used today for low-performance chips.

### Flip-chip (1990s-2010s)
The transformative insight: "Why only use the edges? That's not much surface area." Flip the chip face-down and connect through tiny solder bumps across the entire face. More connections, shorter paths, better performance. Still the workhorse for most processors. Key challenge: CTE (Coefficient of Thermal Expansion) mismatch — different materials expand differently under heat. Solved with underfill mold between chip and substrate. This is the basis of [[SK Hynix]]'s MR-MUF [[HBM]] packaging.

### Wafer-level packaging / 2.5D interposers (2010s-present)
The insight: "Why build a separate box when you can build packaging directly on the wafer using the same lithography tools?" This led to **[[CoWoS]]** — place multiple chips side-by-side on a silicon interposer (a passive routing layer, not a chip itself) that connects them with incredibly dense wiring. This is how [[NVIDIA]] connects GPU die to [[HBM]] stacks in every AI accelerator.

**[[Intel]] EMIB alternative:** CoWoS wastes silicon — the interposer covers the entire area but silicon is only needed where data actually travels. EMIB uses silicon "bridges" only at the chip-to-chip connections, with cheaper organic substrate everywhere else.

### 3D stacking (now)
Bunk beds for chips. Stack dies vertically, connected by Through-Silicon Vias (TSVs) — vertical pillars punched through the silicon. [[HBM]] already works this way: 8-16 DRAM dies stacked with thousands of TSVs creating a massive memory bandwidth highway. [[AMD]]'s 3D V-Cache extends this to logic. The transformative step: logic-on-logic stacking.

### Hybrid bonding (future)
The most transformative packaging technology since flip-chip. Eliminates solder bumps entirely — directly fuses copper pads between chips. Process: polish copper pads and dielectric surfaces to sub-nanometer (atomically smooth) flatness, press together, and copper atoms diffuse across the interface via Van der Waals forces to form a single metallic bond.

Why it matters:
- **Density:** Sub-10μm pitch → 10,000+ interconnects/mm² (solder balls are spheres that bulge, capping density)
- **Power:** Shorter connections = less energy wasted pushing electrons through bumps
- **Thermals:** No solder bumps = better heat transfer between layers

Critical math: interconnect density scales with the **square** of pitch reduction (2D grid). Halve the pitch → 4x the density. This is why hybrid bonding is essential for packaging scaling to keep up with transistor shrinks.

Challenge: surface prep is insanely demanding. Sub-nanometer flatness across an entire wafer. One particle and the bond fails. [[BESI]] is the leading equipment supplier.

## Key technologies (summary)

| Technology | What it does |
|------------|--------------|
| **CoWoS** | TSMC's 2.5D packaging — silicon interposer connects GPU + [[HBM]] |
| **EMIB** | Intel's alternative — silicon bridges only where needed, organic substrate elsewhere |
| **2.5D** | Chips sit side-by-side on interposer |
| **3D / TSV** | Chips stacked vertically, connected by through-silicon vias |
| **[[HBM]] integration** | Memory stacks bonded to logic |
| **ABF substrate** | [[Ajinomoto]] Build-up Film — critical substrate material (~90% share) |
| **Hybrid bonding** | Direct Cu-Cu bonding for high-density interconnects — [[BESI]] equipment |

---

## Competitive landscape

| Player | Technology | Position |
|--------|------------|----------|
| [[TSMC]] | CoWoS | **Monopoly** on AI accelerators (NVIDIA, AMD) — capacity tight |
| [[SK Hynix]] | 2.5D | Indiana line 2028, turn-key [[HBM]] + packaging |
| [[Intel]] | EMIB, Foveros | Emerging CoWoS alternative for tier-2, US-based |
| [[Samsung]] | Various | Has packaging but trails on integration |
| [[ASE]]/[[Amkor]]/SPIL | OSAT | Could take overflow if Intel misses window |

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
| [[Google]] | TPU production cut 4M → [[3M]] units for 2026 |
| [[AMD]] | Exploring Samsung alternatives |
| [[Amazon]] | Capacity-constrained on custom chips |

**The math:** If NVIDIA has half, everyone else fights over the remainder. Google couldn't get enough CoWoS for planned TPU production — forced to cut 25%.

**This is why alternatives matter:** Intel EMIB, Samsung packaging, SK Hynix Indiana are now strategic, not just backup options.

---

## SK Hynix challenge (Dec 2025)

SK Hynix planning first 2.5D mass production line in West Lafayette, Indiana (2028):
- Currently depends on TSMC for packaging
- Turn-key model: [[HBM]] + packaging together
- Could disrupt TSMC's packaging monopoly
- "Korea's two semiconductor giants are basically trolling [[Taiwan]]" — Samsung on foundry, SK Hynix on packaging

---

## Intel EMIB as alternative (Jan 2026 update)

CoWoS capacity so tight that tier-2 chip makers exploring [[Intel]]'s EMIB:

**Who's looking:**
- [[Marvell]], [[MediaTek]] actively trying EMIB
- [[Apple]], [[Qualcomm]] adding "EMIB familiarity" to job posts
- Non-Intel customers already confirmed
- **[[Google]]** exploring Intel EMIB for TPU v9 (2027)
- **[[Broadcom]]** has placed orders

**EMIB advantages:**
- More affordable than CoWoS
- Good thermal performance
- Mature technology with solid track record
- US-based (TSMC back-end ships to [[Taiwan]])

**Intel capacity expansion (New [[Mexico]]):**

| Capability | Expansion |
|------------|-----------|
| EMIB | +30% capacity |
| Foveros 3D | +150% capacity |

**New business model:** TSMC front-end wafer fab + Intel back-end packaging. Not impossible — integrating the two takes effort but works for lower-spec products.

**Window may be temporary:** If Intel fails to seize this opportunity, traditional OSATs ([[ASE]], [[Amkor]], SPIL) take the overflow.

**Intel's angle:** If front-end foundry can't win customers, start with back-end packaging as beachhead into AI supply chain.

---

## Samsung turnkey bundle (Jan 2026)

**[[Samsung]]'s differentiation: TSMC doesn't make memory.**

Samsung offering integrated solution to hyperscalers:

| Component | Samsung offering |
|-----------|------------------|
| Foundry | SF2 (2nm) process |
| Advanced packaging | CoWoS alternative |
| Memory | [[HBM]] from Samsung |
| Integration | Single vendor, Texas facilities |

**Why "turnkey" matters:** Customers can get foundry + packaging + [[HBM]] from one vendor. TSMC requires separate memory sourcing (SK Hynix, Samsung, [[Micron]]) and coordination.

**[[Target]] customers:** [[Google]], [[AMD]], [[Amazon]] — all exploring Samsung as TSMC overflow.

**The trade-off:** Samsung yields still behind TSMC (~55-60% vs ~65%), but one-stop shopping has value when capacity is scarce.

---

## Taiwan panel-to-packaging conversion (2025-2026)

Taiwan's dying LCD panel industry is being cannibalized for cleanroom capacity. [[Innolux]] and [[AUO]] are selling old panel fabs to semiconductor packagers ([[TSMC]], [[ASE]], ChipMOS, Powertech) who need instant capacity for AI chips. Building greenfield packaging plants takes 3-5 years; buying a panel fab with existing cleanrooms, power, and water treatment = months.

Key deals: Innolux Fab 4 → TSMC ($538M, for CoWoS), Innolux Fab 2 → ChipMOS ($28M), AUO L3C → Powertech ($217M), Innolux Fab 5 → ASE (rumored).

**TSMC buying panel fabs for CoWoS is the clearest signal of how severe the packaging capacity crunch is.**

See [[Taiwan panel-to-packaging conversion]] for full details.

---

## Implications

- Packaging is a **separate moat** from foundry
- AI chip supply chain has multiple bottlenecks: foundry AND packaging
- SK Hynix U.S. packaging could benefit from [[CHIPS Act]] and [[N-2 rule]] constraints on TSMC
- Panel fab conversions are accelerating capacity additions but still won't close the 15-20% supply-demand gap near-term

---

*Updated 2026-03-10*

---

## Related

- [[TSMC]] — leader (CoWoS monopoly for AI accelerators)
- [[NVIDIA]] — capacity hog (>50% CoWoS locked through 2027)
- [[Google]] — constrained (TPU cut 4M→[[3M]])
- [[SK Hynix]] — challenger (Indiana 2.5D line 2028)
- [[Intel]] — alternative (EMIB +30%, Foveros +150% expansion)
- [[Samsung]] — turnkey (foundry + packaging + [[HBM]] bundle)
- [[ASE]] — overflow (if Intel misses window)
- [[Ajinomoto]] — supplier (ABF substrate monopoly ~90%)
- [[BESI]] — equipment (hybrid bonding leader)
- [[Disco]] — equipment (wafer dicing ~80% share)
- [[Customer lock-in via co-design]] — mechanism (CoWoS adds switching costs)
- [[CHIPS Act]] — enabler (US packaging investment)
- [[N-2 rule]] — context (constraints on TSMC packaging)
- [[Supply chain bottlenecks]] — context (packaging as constraint layer)
- [[Semiconductor Test]] — downstream (packaging complexity drives test steps)
- [[Semiconductor bonding equipment]] — equipment for hybrid bonding
- [[Taiwan panel-to-packaging conversion]] — panel fabs being bought for packaging capacity
- [[Innolux]] — panel fab seller (TSMC, ChipMOS, ASE)
- [[AUO]] — panel fab seller (Powertech)


### Cross-vault
- [Technologies: Advanced Packaging](obsidian://open?vault=technologies&file=Advanced%20Packaging) — full technical breakdown: CoWoS generations, interposer stitching, hybrid bonding, TSV mechanics

## Sources

- Jason's Chips: [Short n Casual Intro to Packaging](https://jasonschips.substack.com/p/short-n-casual-advanced-packaging) — technical evolution primer (March 2026)
