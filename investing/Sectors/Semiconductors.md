---
aliases: [Semis, Chips, Semiconductor industry, Semiconductor sector]
---
#sector #semiconductors #tech

# Semiconductors

Industry index for the semiconductor value chain. The analytical work lives in the children below; this note is the navigation layer plus parent-level industry context.

> [!info] Industry index, not a single tradeable cluster
> Internal correlation across the 23 mapped Semiconductors actors averages 0.31 over the trailing year — too diluted to read as one signal because design, memory, equipment, materials, and analog have structurally different price drivers. The analytical entry points are the children below, all of which screen tighter than the parent: [[AI Compute]] (0.58), [[US Memory]] (0.70), [[Korea Memory]] (0.35), [[Memory]] (0.38), [[Semiconductor Materials]] (0.65), [[Semiconductor Test]] (0.46), [[WFE]] (0.83), [[Sensors]] (0.50), [[Connectivity]] (0.34), [[Korea AI chips]] (0.30). See [[2026-05-09-sector-internal-correlation-diagnostic]] for method and full table.

---

## Correlation structure

| Metric | Value | Interpretation |
|--------|-------|----------------|
| Avg correlation | 0.31 | Diluted — taxonomic, not tradeable |
| Mapped actors | 23 | |
| Period | trailing ~252 sessions | |
| Method | pairwise log-return correlation | [[2026-05-09-sector-internal-correlation-diagnostic]] |

The parent is taxonomic; tradeable clusters are the children. Read the matrix at the child level — see the table immediately below.

---

## Children — analytical entry points

Each child is the place where members, correlation diagnostics, charts, and thesis live. The parent is for industry-level context only.

| Child | Avg corr | What it tracks | Members live in | Active thesis |
|-------|---------:|----------------|-----------------|---------------|
| [[WFE]] | 0.83 | The four equipment oligopolists ([[ASML]], [[Applied Materials]], [[Lam Research]], [[KLA]]) trading off the same wafer-fab capex cycle | child | [[Long WFE]] |
| [[US Memory]] | 0.70 | [[Micron]], [[SanDisk]], [[Western Digital]] — USD-listed memory exposure | child | [[Long memory]] |
| [[AI Compute]] | 0.58 | [[TSMC]] + its largest AI customers ([[NVIDIA]], [[AMD]]) trading as a foundry-customer cluster | child | [[Long NVIDIA]], [[Long TSMC]] |
| [[Korea Memory]] | 0.53 | [[SK Hynix]], [[Samsung]] — KRW-listed memory, [[HBM]]-dominant | shared with [[Memory]] | [[Long memory]], [[Short TSMC long Korea]] |
| [[Sensors]] | 0.50 | Image sensors, MEMS, automotive/industrial sensing | child | — |
| [[Semiconductor Test]] | 0.46 | Test equipment ([[Teradyne]], [[Advantest]]) — narrower than WFE, AI/memory-leveraged | child | [[Long OSAT and test equipment]] |
| [[Memory]] | 0.38 | DRAM + NAND industry overview; splits into [[US Memory]] and [[Korea Memory]] for tradeable signal | [[Memory]] | [[Long memory]] |
| [[Connectivity]] | 0.34 | [[Broadcom]], [[Qualcomm]], [[Marvell]] — networking + RF cluster | child | — |
| [[Korea AI chips]] | 0.30 | Korean AI accelerator names; broader than [[Korea Memory]] | child | — |
| [[Semiconductor Materials]] | 0.65 (concept) | [[JSR Corporation]], [[Shin-Etsu]] and other Japan/Korea materials chokepoints | child | [[Long Japan photoresists]], [[Long Japan wafers]] |

Hubs that exist as taxonomy but don't trade as a cluster:
- "Foundry" — no peer set; [[TSMC]] dominates and trades with its customers ([[AI Compute]] is the right entry point).
- EDA — duopoly ([[Synopsys]], [[Cadence]]); 0.75 internal but only two names; functions as a paired trade rather than a hub.
- OSAT — [[ASE]], [[Amkor]]; tracked under the [[Advanced packaging]] concept and via [[Long OSAT and test equipment]].

Special cases:
- [[Intel]] — uncorrelated with the sector (0.28-0.34). IDM turnaround story; tracked as an actor, not as a sector member.

---

## Industry size ([[Gartner]], Jan 2026)

| Metric | 2025 | YoY |
|--------|------|-----|
| Total semiconductor revenue | $793B | +21% |
| AI semiconductors (processors, [[HBM]], networking) | ~$264B | — |
| AI share of total | ~1/3 | — |

Key milestones:
- [[NVIDIA]] first company to cross $100B in semiconductor revenue
- NVIDIA extended lead over [[Samsung]] by $53B in 2025

### AI infrastructure spending

| Metric | 2026 forecast |
|--------|---------------|
| AI infrastructure spending | >$1.3 trillion |

Capex flowing to [[AI hyperscalers]], neoclouds, and enterprises for AI compute, networking, and data centers. Source: [[Gartner]] (Jan 12, 2026).

---

## Value-chain map

```
Design → Foundry → Packaging → Test → System integration
   ↑         ↑          ↑         ↑
  EDA     Equipment    OSAT     Equipment
```

| [[Segment]] | Where the trade lives | Industry margin band |
|-------------|-----------------------|----------------------|
| Design (fabless) | [[AI Compute]], [[Connectivity]] | 60-75% gross |
| Foundry | [[AI Compute]] (via [[TSMC]]); [[Intel]] standalone | 50-55% (TSMC) |
| [[Memory]] | [[Memory]] / [[US Memory]] / [[Korea Memory]] | 30-65% (cyclical) |
| Equipment | [[WFE]] | 45-55% |
| EDA | not hubbed; paired ([[Synopsys]], [[Cadence]]) | 80-90% |
| OSAT | [[Advanced packaging]] concept | 15-25% |
| Materials | [[Semiconductor Materials]] | varies |

---

## Industry KPIs

Cross-cutting metrics. Sub-sector charts and time series live in the children.

| Metric | Definition | Read | Why it matters |
|--------|------------|------|----------------|
| Gross margin | (Rev - COGS) / Rev | >60% (fabless) | Pricing power & IP value |
| Inventory days | Days to sell inventory | <80-100 | Cyclical glut/shortage tell |
| R&D intensity | R&D / Revenue | >15-20% | Sustaining innovation lead |
| Capex intensity | Capex / Revenue | >30% (foundry/memory) | Capacity scale (barrier to entry) |
| Book-to-bill | Orders / Shipments | >1.1x | Forward demand ([[WFE]]) |
| Yield | Functional die / Wafer | >90% (mature) | Manufacturing efficiency (foundry) |

---

## Cross-cutting themes (2025-2026)

Each theme is anchored in a child or concept where the live data lives.

| Theme | Where to read it |
|-------|------------------|
| [[AI hyperscalers]] demand | [[AI Compute]], [[Memory]], [[HBM]] |
| [[Memory shortage 2025-2026]] | [[Korea Memory]], [[US Memory]] |
| [[Advanced packaging]] / [[CoWoS]] bottleneck | [[Advanced packaging]] concept |
| [[Export controls]] / [[China]] bifurcation | [[Korea AI chips]], [[Semiconductor Materials]] |
| [[Power constraints]] for fabs | [[Power constraints]] concept |
| [[Leading edge race]] — 2nm competition | [[AI Compute]] ([[TSMC]] vs [[Samsung]] vs [[Intel]]) |

### Apr 24 2026: CPU-led record rally

[[Reuters]]' Apr 24 chip-rally piece marked a useful shift in sector leadership. The Philadelphia Semiconductor Index closed +4.3% at a record high after [[Intel]]'s Q1/Q2 results turned AI inference CPU demand into a market-wide readthrough. Verified Apr 24 closes: [[Intel]] +23.6%, [[AMD]] +13.9%, [[Arm Holdings]] +14.8%, [[NVIDIA]] +4.3%, [[Texas Instruments]] -1.8% after its prior-day +19.4% Q1 earnings move, and [[SMH]] +5.1%.

The sector implication is that the AI cycle is no longer priced as a single [[NVIDIA]] GPU trade. [[LSEG]] consensus cited by Reuters had semiconductor sub-industry Q1 earnings growth at 109.2%, versus 48.2% for the broader [[S&P 500]] information-technology sector. The Philadelphia chip index traded around 26.6x forward earnings versus about 20.7x for the [[S&P 500]]. Those multiples are now being justified by the idea that inference and [[Agentic AI]] workloads pull demand into CPUs, analog/power, memory, and manufacturing capacity, not just accelerators.

### Apr 24 2026: [[China]] domestic AI-stack validation

The same day, [[DeepSeek]] V4 Preview showed the other side of the cycle: not just more demand for US chips, but substitution pressure inside [[China]]. [[CNN]] reported that [[Huawei]] supports V4 with Supernode technology combining large [[Ascend]] 950 clusters, and [[Counterpoint Research|Counterpoint]]'s Wei Sun said V4 runs on domestic chips from Huawei and [[Cambricon Technologies]] rather than NVIDIA hardware.

For semiconductors, the signal is that export controls are creating a protected domestic accelerator market. Huawei and [[Cambricon]] do not need to beat [[Blackwell]] chip-for-chip if Chinese model developers optimize around their clusters and Chinese customers accept slightly lower frontier performance in exchange for sovereignty, cost, and availability. This is the semiconductor expression of [[China AI Plus]].

### May 8 2026 rally (Apple-Intel deal extension)

The semiconductor cohort rallied as a basket on May 8 after [[Wall Street Journal]] broke the [[Apple-Intel chip-making agreement May 2026|Apple-Intel preliminary chip-making agreement]]. The basket-level move makes May 8 the second large semis rally session in two weeks (after the Apr 24 CPU-led record) and reinforces the cycle thesis that AI demand is no longer a single-stock ([[NVIDIA]]) trade. Verified May 8 vault-actor closes:

| Ticker | Actor | Move | Sigma | Why |
|--------|-------|------|-------|-----|
| MU | [[Micron]] | +15.5% | +3.3σ | Best week since 2008; AI memory cycle + Apple-Intel adjacent |
| INTC | [[Intel]] | +14.0% | +2.4σ | Direct Apple deal beneficiary; second 14% session in a week |
| AMD | [[AMD]] | +11.4% | +2.3σ | Follow-on dual-source candidate at Intel |
| DELL | [[Dell]] | +13.1% | +2.5σ | PC-side beneficiary — implies more US-made PCs |
| QCOM | [[Qualcomm]] | +8.2% | +2.2σ | Adjacent dual-source candidate |
| KLAC | [[KLA]] | +6.0% | +1.8σ | WFE participates on broader US fab capex implications |
| AMAT | [[Applied Materials]] | +6.0% | +1.6σ | Same |
| MRVL | [[Marvell]] | +6.3% | +1.0σ | Connectivity cluster participation |

Cross-name reads:
- AAPL itself only moved +2.0% — the market read the deal as Apple optionality, not a TSMC repudiation. The [[Long TSMC]] thesis is intact but capped.
- [[TSMC]] (TSM) showed only a modest move because the AI capacity constraint already prices most of the lost-anchor risk into the foundry leader.
- The [[Short TSMC long Korea]] thesis weakens at the margin — [[Samsung]] was the natural dual-source for fabless customers nervous about TSMC; Intel takes that title with Apple's qualification. See [[Foundry Wars#Apple-Intel reshuffle May 2026]].

Year-to-date context: [[Reuters]] cites [[PHLX Semiconductor]] Index up over 65% YTD through May 8 2026. The [[Jonathan Krinsky]] commentary referenced on CNBC May 8 warned of a 25-30% correction risk for the SOX, characterizing the magnitude of markup as resembling 1999. Krinsky is the cleanest published bear voice on the cycle multiple right now; the implied risk is that any AI-capex-cycle deceleration (Q3 reporting season is the likely test) compresses the SOX faster than the equity-market beta would suggest.

Same-session structural reads:
- The Apple-Intel deal is supply-side US industrial-policy completion: [[CHIPS Act]] subsidies + Aug 2025 ~10% government Intel stake (supply-side) + May 8 [[Donald Trump|Trump]]-[[Tim Cook]] White House advocacy (demand-side) = coordinated industrial-policy framework closer to Korea/Taiwan/Japan than to US pre-2025 policy.
- The two-anchor Intel demand portfolio now stands: [[TERAFAB]] (Apr 7, Tesla/SpaceX/xAI cluster) + Apple (May 8). Two structurally different demand pillars hedge each other if 18A HVM stumbles.

*Sources: [CNBC — Wall Street AI chip love moves from NVIDIA to Intel, AMD, Micron](https://www.cnbc.com/2026/05/08/wall-street-ai-chip-love-moves-from-nvidia-to-intel-amd-and-micron.html); [Apple-Intel chip-making agreement May 2026]; local `quick_movers.py` May 8 screen.*

---

## Theses anchored to this hub

| Thesis | Lives in | Notes |
|--------|----------|-------|
| [[Long NVIDIA]] | [[AI Compute]] | AI platform dominance |
| [[Long TSMC]] | [[AI Compute]] | foundry moat |
| [[Long memory]] | [[Memory]] / [[Korea Memory]] / [[US Memory]] | [[HBM]] cycle |
| [[Long WFE]] | [[WFE]] | equipment leverage |
| [[Long Japan photoresists]] | [[Semiconductor Materials]] | materials chokepoint |
| [[Long Japan wafers]] | [[Semiconductor Materials]] | upstream duopoly |
| [[Long OSAT and test equipment]] | [[Semiconductor Test]] / [[Advanced packaging]] | packaging bottleneck |
| [[Short standalone ASICs]] | parent-level | consolidation around NVIDIA |
| [[Short TSMC long Korea]] | [[Korea Memory]] vs [[AI Compute]] | relative value |

---

## Cyclicality

| [[Segment]] | Cycle exposure | Where to track |
|-------------|----------------|----------------|
| [[Memory]] | High (but [[HBM]] buffered) | [[Korea Memory]], [[US Memory]] |
| Equipment | Medium (backlog visibility) | [[WFE]] |
| Foundry | Low (long-term contracts) | [[AI Compute]] |
| Fabless AI | Low (structural demand) | [[AI Compute]] |

Traditional cycle: 3-4 years, inventory-driven. AI capex is decoupling the leading edge from the historical PC/mobile cycle.

---

## Geographic concentration

| Activity | Location | Risk |
|----------|----------|------|
| Leading-edge foundry | Taiwan (90%+) | [[Taiwan concentration risk]] |
| [[HBM]] | Korea (95%+) | Moderate |
| Equipment | US, [[Netherlands]], [[Japan]] | Low |
| Assembly/test | [[Asia]] ([[China]], [[Malaysia]], [[Vietnam]]) | Medium |

---

## Related

- [[AI hyperscalers]] — demand driver
- [[Export controls]] — geopolitical constraint
- [[Advanced packaging]] — key bottleneck (→ OSAT)
- [[Memory shortage 2025-2026]] — near-term theme (→ [[Memory]])
- [[Taiwan]] — geographic risk (→ [[AI Compute]])

### Cross-vault
- [Technologies: Semiconductors](obsidian://open?vault=technologies&file=Semiconductors) — fabrication processes, transistor physics, node scaling
- [Geopolitics: Semiconductors](obsidian://open?vault=geopolitics&file=Concepts%2FSemiconductors) — chip statecraft, [[Export controls]], industrial policy

## Sources

- [[Gartner]], Jan 2026 — industry size figures
- [[Reuters]] / [[LSEG]] consensus, Apr 24 2026 — Q1 earnings growth and forward-multiple comparison
- [[2026-05-09-sector-internal-correlation-diagnostic]] — children correlation table

*Restructured 2026-05-10 — promoted from member-list to index hub. Members live in children.*
