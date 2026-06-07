---
aliases: [Semis, Chips, Semiconductor industry, Semiconductor sector]
---
#sector #semiconductors #tech

# Semiconductors

Industry [[index]] for the semiconductor value chain. The analytical work lives in the children below; this note is the navigation layer plus parent-level industry context.

> [!info] Industry [[index]], not a single tradeable cluster
> Internal correlation across the 23 mapped Semiconductors actors averages 0.31 over the trailing year — too diluted to read as one signal because design, memory, equipment, materials, and analog have structurally different price drivers. The analytical entry points are the children below, all of which screen tighter than the parent: [[AI Compute]] (0.58), [[US Memory]] (0.70), [[Korea Memory]] (0.35), [[Memory]] (0.38), [[Semiconductor Materials]] (0.65), [[Semiconductor Test]] (0.46), [[WFE]] (0.83), [[Sensors]] (0.50), [[Connectivity]] (0.34), [[Korea AI chips]] (0.30). See the May 9 sector-internal-correlation diagnostic report for method and full table.

---

![[semiconductors-chart.png]]
*[[SOXX]] and [[SMH]] normalized from Jan. 2026 show the parent semiconductor proxy tape. This chart is a headline-market proxy, not proof that the full [[Semiconductors]] parent is one tradeable cluster.*

## Correlation structure

| Metric | Value | Interpretation |
|--------|-------|----------------|
| Avg correlation | 0.31 | Diluted — taxonomic, not tradeable |
| Mapped actors | 23 | |
| Period | trailing ~252 sessions | |
| Method | pairwise log-return correlation | May 9 sector-internal-correlation diagnostic report |

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
| [[Sensors]] | 0.50 | [[Image sensors]], MEMS, automotive/industrial sensing | child | — |
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
| Post-node scaling / system optimization | [[Tau Scaling Law]], [[Advanced packaging]], [[NVIDIA alternatives]] |

### Apr 24 2026: CPU-led record rally

[[Reuters]]' Apr 24 chip-rally piece marked a useful shift in sector leadership. The Philadelphia Semiconductor Index closed +4.3% at a record high after [[Intel]]'s Q1/Q2 results turned AI inference CPU demand into a market-wide readthrough. Verified Apr 24 closes: [[Intel]] +23.6%, [[AMD]] +13.9%, [[Arm Holdings]] +14.8%, [[NVIDIA]] +4.3%, [[Texas Instruments]] -1.8% after its prior-day +19.4% Q1 earnings move, and [[SMH]] +5.1%.

The sector implication is that the AI cycle is no longer priced as a single [[NVIDIA]] GPU trade. [[LSEG]] consensus cited by Reuters had semiconductor sub-industry Q1 earnings growth at 109.2%, versus 48.2% for the broader [[S&P 500]] information-technology sector. The Philadelphia chip [[index]] traded around 26.6x forward earnings versus about 20.7x for the [[S&P 500]]. Those multiples are now being justified by the idea that inference and [[Agentic AI]] workloads pull demand into CPUs, analog/power, memory, and manufacturing capacity, not just accelerators.

### Apr 24 2026: [[China]] domestic AI-stack validation

The same day, [[DeepSeek]] V4 Preview showed the other side of the cycle: not just more demand for US chips, but substitution pressure inside [[China]]. [[CNN]] reported that [[Huawei]] supports V4 with Supernode technology combining large [[Ascend]] 950 clusters, and [[Counterpoint Research|Counterpoint]]'s Wei Sun said V4 runs on domestic chips from Huawei and [[Cambricon Technologies]] rather than NVIDIA hardware.

For semiconductors, the signal is that export controls are creating a protected domestic accelerator market. Huawei and [[Cambricon]] do not need to beat [[Blackwell]] chip-for-chip if Chinese model developers optimize around their clusters and Chinese customers accept slightly lower frontier performance in exchange for sovereignty, cost, and availability. This is the semiconductor expression of [[China AI Plus]].

### May 25 2026: Huawei post-node scaling claim

[[Huawei]]'s [[Tau Scaling Law]] / [[LogicFolding]] announcement adds a design-framework layer to the China semiconductor story. Huawei says the approach can raise performance and transistor density by reducing signal-propagation time across devices, circuits, chips, and systems; Reuters framed the claim around a 2031 target for 14 angstrom / 1.4nm-equivalent density, while noting no independent performance data was supplied.

Sector read-through: the China gap is shifting from "can [[SMIC]] reach the next node?" to "how much of the node gap can a vertically integrated system designer offset?" That pulls [[Advanced packaging]], interconnect, EDA, thermals, and cluster networking into the same competitive question as lithography. The first observable test is fall 2026 [[Kirin]] chips using LogicFolding; the larger investment test is whether the same ideas improve [[Ascend]] AI clusters.

### May 8 2026 rally ([[Apple]]-Intel deal extension)

The semiconductor cohort rallied as a basket on May 8 after [[Wall Street Journal]] broke the [[Apple-Intel chip-making agreement May 2026|Apple-Intel preliminary chip-making agreement]]. The basket-level move makes May 8 the second large semis rally session in two weeks (after the Apr 24 CPU-led record) and reinforces the cycle thesis that AI demand is no longer a single-stock ([[NVIDIA]]) trade. Verified May 8 vault-actor closes:

| Ticker | Actor | Move | Sigma | Why |
|--------|-------|------|-------|-----|
| MU | [[Micron]] | +15.5% | +3.3σ | Best week since 2008; AI memory cycle + [[Apple]]-Intel adjacent |
| INTC | [[Intel]] | +14.0% | +2.4σ | Direct [[Apple]] deal beneficiary; second 14% session in a week |
| [[AMD]] | [[AMD]] | +11.4% | +2.3σ | Follow-on dual-source candidate at Intel |
| DELL | [[Dell]] | +13.1% | +2.5σ | PC-side beneficiary — implies more US-made PCs |
| QCOM | [[Qualcomm]] | +8.2% | +2.2σ | Adjacent dual-source candidate |
| KLAC | [[KLA]] | +6.0% | +1.8σ | WFE participates on broader US fab capex implications |
| AMAT | [[Applied Materials]] | +6.0% | +1.6σ | Same |
| MRVL | [[Marvell]] | +6.3% | +1.0σ | Connectivity cluster participation |

Cross-name reads:
- AAPL itself only moved +2.0% — the market read the deal as [[Apple]] optionality, not a TSMC repudiation. The [[Long TSMC]] thesis is intact but capped.
- [[TSMC]] (TSM) showed only a modest move because the AI capacity constraint already prices most of the lost-anchor risk into the foundry leader.
- The [[Short TSMC long Korea]] thesis weakens at the margin — [[Samsung]] was the natural dual-source for fabless customers nervous about TSMC; Intel takes that title with [[Apple]]'s qualification. See [[Foundry Wars]] and [[Apple-Intel chip-making agreement May 2026]].

Year-to-date context: [[Reuters]] cites [[PHLX Semiconductor]] Index up over 65% YTD through May 8 2026. The [[Jonathan Krinsky]] commentary referenced on [[CNBC]] May 8 warned of a 25-30% correction risk for the SOX, characterizing the magnitude of markup as resembling 1999. Krinsky is the cleanest published bear voice on the cycle multiple right now; the implied risk is that any AI-capex-cycle deceleration (Q3 reporting season is the likely test) compresses the SOX faster than the equity-market beta would suggest.

Same-session structural reads:
- The [[Apple]]-Intel deal is supply-side US industrial-policy completion: [[CHIPS Act]] subsidies + Aug 2025 ~10% government Intel stake (supply-side) + May 8 [[Donald Trump|Trump]]-[[Tim Cook]] White House advocacy (demand-side) = coordinated industrial-policy framework closer to Korea/Taiwan/Japan than to US pre-2025 policy.
- The two-anchor Intel demand portfolio now stands: [[TERAFAB]] (Apr 7, [[Tesla]]/SpaceX/[[xAI]] cluster) + [[Apple]] (May 8). Two structurally different demand pillars hedge each other if 18A HVM stumbles.

*Sources: [CNBC — Wall Street AI chip love moves from NVIDIA to Intel, AMD, Micron](https://www.cnbc.com/2026/05/08/wall-street-ai-chip-love-moves-from-nvidia-to-intel-amd-and-micron.html); [[Apple-Intel chip-making agreement May 2026]]; local `quick_movers.py` May 8 screen.*

### May 20-21 2026: supply-limited framing hardens

Reuters' May 20 interview with [[ASML]] CEO Christophe Fouquet and the May 21 FT interview with [[James Anderson]] / [[Morgan Samet]] point at the same sector structure from opposite sides. Fouquet describes a supply-limited market driven by AI, satellites, and robotics, with bottlenecks likely to recur across the chain as the market scales. Anderson and Samet describe the demand-side consequence: platform buyers must keep spending, while the bottleneck suppliers have the cleaner pricing-power position.

That strengthens the parent-sector read that semiconductors should be mapped through children, not as one broad "chips" factor. The supplier scarcity lives most clearly in [[AI Compute]], [[WFE]], [[Memory]], and [[AI capex chain basket]]. The buyer-side pressure lives in [[AI hyperscalers]], [[AI infrastructure financing]], and [[AI capex arms race]].

[[TERAFAB]] is the stress test. Reuters reported on May 6 that [[SpaceX]] proposed a $55B initial [[Texas]] semiconductor facility, with total investment potentially rising to $119B if later phases are completed. If the project stays aspirational, it still functions as evidence that large AI buyers want to escape supplier dependence. If it becomes real, it pulls more demand into the same equipment bottlenecks that benefit [[ASML]], [[Applied Materials]], [[KLA Corporation]], and [[Lam Research]].

*Sources: [Reuters via Investing.com — ASML CEO sees tight supply](https://www.investing.com/news/stock-market-news/exclusiveasml-ceo-sees-tight-supply-in-booming-chip-market-as-ai-demand-soars-4701446), May 20 2026; [Financial Times — Big Tech software era is over, says top investor James Anderson](https://www.ft.com/content/9d2bd5b3-80c6-49b9-a04b-edc4162c9320), May 21 2026; [Reuters via Investing.com — SpaceX files plan for $55 billion Terafab chip facility in [[Texas]]](https://www.investing.com/news/economy-news/spacex-plans-55-billion-chip-plant-in-texas-4662329), May 6 2026.*

### May 28 2026: best year since 1999, rally broadens past a lagging Nvidia

The FT marked the [[PHLX Semiconductor]] [[index]] up roughly 75% year-to-date — its best start to a year since the 1999 dotcom peak — and up more than $5tn in market value over the prior two months, about 1.5x the entire FTSE 100. The vault's tradeable proxy confirms the magnitude: [[SOXX]] closed +79.9% YTD at the May 27 2026 session (the close before the article), with [[Lam Research]] +72.5% and [[KLA]] +53.8% YTD.

The defining feature of the 2026 leg is that [[NVIDIA]] is the laggard, not the leader. Verified YTD moves through the May 27 close (vault `prices_long`):

| Ticker | Actor | YTD 2026 | Driver per FT |
|--------|-------|---------:|---------------|
| INTC | [[Intel]] | +209.2% | CPU-demand outlook; shares above their dotcom-era all-time high; US 10% stake plus [[NVIDIA]] / [[SoftBank]] investments |
| MU | [[Micron]] | +194.5% | Memory supercycle; crossed $1tn market value this week |
| ARM | [[Arm Holdings]] | +163.8% | Strategic pivot to selling its own chips; forecasts a fivefold revenue rise over five years |
| [[AMD]] | [[AMD]] | +121.7% | Chip-supply deals with [[Meta]] and [[OpenAI]] |
| NVDA | [[NVIDIA]] | +12.6% | Still the largest public company (~$5.1tn cap), but its competitors massively outpaced it this year |

Nvidia's relative lag while Intel, AMD, and Arm multiplied is the cleanest market expression yet of the broadening already logged in the Apr 24 and May 8 sections: the AI cycle is no longer priced as a single GPU trade. The FT attributes the diversification partly to anticipation that the AI infrastructure market is shifting toward CPUs alongside GPUs — the same systems-scarcity refinement tracked in [[AI capex arms race]].

The memory leg hardened: [[Micron]] and [[SK Hynix]] crossed $1tn in market value on successive days, joining the trillion-dollar club; [[UBS]] said Micron could more than double over the next 12 months even after an ~860% gain in the prior year (vault confirms MU +864.8% over the trailing year through May 27). See [[Memory shortage 2025-2026]] and [[US Memory]] / [[Korea Memory]].

Demand sits against the hyperscaler-capex backdrop the vault already sizes: [[Meta]], [[Alphabet]], [[Amazon]], and [[Microsoft]] have earmarked about $725bn for AI data centres and equipment in 2026 (see [[AI capex arms race]] refinement VI). [[Bank of America]] reiterated high conviction in continued AI infrastructure strength, citing under-appreciated sovereign, enterprise, and industrial demand.

The supercycle-versus-bubble question is now explicit at the top of the market, and the May 28 piece adds three attributed voices to the running debate. [[Jamie Dimon]] told a conference there was "a lot of exuberance," likening the mood to the run-ups before the 1972, 1986, 2000, and 2007 downturns and saying that did not give him comfort. Charles Lemonides of ValueWorks read the same tape constructively, calling hyperscaler demand "locked and loaded" with the chip and memory groups minting money. Nelson Yu of AllianceBernstein held both: real demand creation is underway, but he warned that — as with any commodity — rising prices eventually beget demand destruction, and that Big Tech's spending plans would likely be scaled back in a recession. This extends the caution [[Jonathan Krinsky]] voiced on May 8 (25-30% SOX correction risk, the markup "resembling 1999").

*Source: [Financial Times — Chip stocks race towards biggest gains since dotcom era on AI demand](https://www.ft.com/content/48cdf575-5509-4b50-a54d-1b767e41be47) (George Steer & Michael Acton, May 28 2026); price moves verified against vault `prices_long` at the May 27 2026 close, one session before the article.*

### Jun 5 2026: rate shock reverses the SOX markup

The Jun. 5 [[Nasdaq semiconductor selloff June 2026]] is the downside test of the May 28 melt-up. A stronger-than-expected payrolls report pushed the 2-year Treasury yield to 4.17% per FT and fully priced a December Fed hike, turning the AI chip trade into a duration selloff. Local closes confirm the scale: [[SOXX]] -10.44%, [[SMH]] -9.22%, [[QQQ]] -4.80%, and [[SPY]] -2.58%. FT reported the [[PHLX Semiconductor]] Index down 10.3%, its worst day since March 2020.

The cross-section was memory/AI-compute heavy rather than a single-stock shock: [[Micron]] -13.25%, [[Arm Holdings]] -12.84%, [[Intel]] -11.28%, [[Western Digital]] -11.06%, and [[AMD]] -10.86%, while [[NVIDIA]] fell a smaller -6.20%. Against QQQ beta, SOXX's shortfall was about -1.17 percentage points before intercept and roughly -1.0x residual sigma with intercept, so the clean read is high-beta tech/rates shock first, semiconductor-specific derating second.

This does not break the supply-scarcity thesis by itself. It proves the sector's valuation is now tied to the same capital-markets window as [[AI infrastructure financing]], [[Hyperscaler capex]], and the [[SpaceX IPO 2026]] absorption test.

*Sources: [FT](https://www.ft.com/content/2929bbd3-1f71-4424-a577-f016c3c65603), Jun. 5 2026; local `prices_long` closes through Jun. 5 2026.*

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
- [[Tau Scaling Law]] — Huawei's post-node scaling framework
- [[LogicFolding]] — architecture scheduled for fall 2026 Kirin and later Ascend

### Cross-vault
- [Technologies: Semiconductors](obsidian://open?vault=technologies&file=Semiconductors) — fabrication processes, transistor physics, node scaling
- [Geopolitics: Semiconductors](obsidian://open?vault=geopolitics&file=Concepts%2FSemiconductors) — chip statecraft, [[Export controls]], industrial policy

## Sources

- [[Gartner]], Jan 2026 — industry size figures
- [[Reuters]] / [[LSEG]] consensus, Apr 24 2026 — Q1 earnings growth and forward-multiple comparison
- [[Reuters]] / [[Financial Times]], May 2026 — supply-limited and platform-vs-supplier framing
- May 9 sector-internal-correlation diagnostic report — children correlation table

*Restructured 2026-05-10 — promoted from member-list to index hub. Members live in children.*
