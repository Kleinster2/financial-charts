---
aliases: [High Bandwidth Memory, HBM3, HBM3E, HBM4]
---
#concept #memory #ai

HBM (High Bandwidth [[Memory]]) — 3D-stacked DRAM enabling massive bandwidth for AI accelerators. The [[Memory|memory]] bottleneck solution for GPUs.

Chart data not applicable for HBM itself; tradeable market exposure lives in [[Korea Memory]] and [[US Memory]].

---

## Synthesis

HBM is the premium bottleneck inside the memory cycle. It converts generic DRAM scarcity into AI-infrastructure pricing power because accelerator customers need bandwidth, validated stacks, and guaranteed supply more than cheap commodity bits. That concentrates the cleanest exposure in [[Korea Memory]], where [[SK Hynix]] and [[Samsung]] control the supply curve, while [[Micron]] gives [[US Memory]] a smaller but still relevant HBM channel.

The strategic read-through is that HBM makes [[Export controls]] more effective and the memory shortage more durable. [[China]] can build domestic AI accelerators, and [[ChangXin Memory]] has a real domestic HBM roadmap, but the public evidence still stops before the investable breakpoint: named customer qualification, proven stack yield, and qualified HBM3E/HBM4 volume. For positioning, HBM is the bridge between the [[Memory shortage 2025-2026]] supercycle, Korea's macro upgrade, and the separation of Korea memory from US semi beta.

---

## Why it matters

AI training/inference is memory-bound. See [[GPU memory scaling]] for the structural trend driving HBM demand.

- GPUs need to feed data faster than traditional DRAM allows
- HBM stacks DRAM dies vertically with through-silicon vias (TSVs)
- Enables 10x+ bandwidth vs standard DDR

---

## Generations

| Gen | Bandwidth | Capacity | Status |
|-----|-----------|----------|--------|
| HBM2e | ~460 GB/s | 16GB/stack | Legacy |
| HBM3 | ~820 GB/s | 24GB/stack | Current |
| HBM3E | ~1.15 TB/s | 36GB/stack | Ramping 2024-25 |
| HBM4 | ~1.5+ TB/s | 48GB+/stack | Launches Feb 2026 |

---

## 2026 market forecast

| Source | 2026 HBM market | YoY growth |
|--------|-----------------|------------|
| [[Bank of America]] | $54.6B | +58% |
| [[Goldman Sachs]] | HBM for ASIC-based AI chips | +82% demand |

[[Memory]] price outlook: +40% through Q2 2026 ([[Counterpoint Research]]).

Drivers:
- AI accelerator ramp (NVIDIA [[Blackwell]], AMD MI400)
- Custom ASIC proliferation ([[Google]] [[TPU]], [[Amazon]] [[Trainium]])
- HBM4 launch (SK Hynix, Feb 2026)

---

## HBM4 launch (Jan 2026)

SK Hynix 16-layer HBM4 launching February 2026:

| Metric | Detail |
|--------|--------|
| Launch | February 2026 |
| Layers | 16 (vs 12 for HBM3E) |
| Bandwidth | ~1.5+ TB/s |
| First customer | NVIDIA ([[Rubin]] architecture) |
| Supply status | Fully sold out — entire 2026 supply contracted |

[[CES 2026]] showcase: SK Hynix demonstrated 16-layer HBM4 alongside SOCAMM2 and LPDDR6.

Production hub: Yongin cluster (Korea) expected to become world's largest HBM production hub by 2027.

### HBM4 pricing (Feb 2026)

| Supplier | HBM4 unit price | Margin |
|----------|----------------|--------|
| [[Samsung]] | ~$700 (+30% vs HBM3E) | 50-60% operating margin |
| [[SK Hynix]] | Mid-$500s (set Aug 2025) | May raise to match Samsung |

Samsung has started mass production and shipped commercial HBM4 products. The 30% generation-on-generation price increase confirms pricing power in a tight market. [[Bloomberg Intelligence]]: if Samsung wins more [[NVIDIA]] HBM volume, the ASP gap between Samsung and SK Hynix narrows in 2026.

*Source: [[Bloomberg]] / Chosun Ilbo, Feb 27 2026*

---

## Supply chain

Only 3 suppliers:
- [[SK Hynix]] — Market leader, [[NVIDIA]]'s primary supplier
- [[Samsung]] — \#2, catching up
- [[Micron]] — Distant \#3, ramping HBM3E

---

## Key dynamics

- [[Memory shortage 2025-2026]] driven partly by HBM demand
- HBM is 5x+ ASP vs commodity DRAM — margin accretive
- Yield is challenging — vertical stacking compounds defect rates
- [[Advanced packaging]] required ([[CoWoS]] at [[TSMC]])
- Macro pass-through is now visible in Korea: the [[Bank of Korea]]'s May 2026 outlook attributed +0.7 percentage points of 2026 GDP growth to stronger semiconductor and IT exports, more than offsetting the [[2026 Iran conflict market impact|Iran-war]] energy drag.
- Incumbent pricing power is now contracted as well as cyclical: [[Micron]] reported FY3Q26 gross margin of 84.6%, guided FY4Q26 near 86%, and described multi-year strategic customer agreements with take-or-pay volume commitments.

### Korea macro bridge (May 2026)

The HBM cycle is now a central-bank input, not just a chip-industry theme. The [[Bank of Korea]] raised its 2026 [[South Korea]] growth forecast to 2.6% from 2.0% on May 28, 2026, with stronger semiconductor and IT exports adding 0.7 percentage points to GDP. The same bridge put the Middle East war drag at -0.4 percentage points, which means AI-memory demand is large enough to offset a national energy-import shock in the official forecast.

The investment implication is that [[HBM]] scarcity has two channels: direct supplier pricing power for [[SK Hynix]] and [[Samsung]], and a country-level growth/wealth channel through [[Kospi]], exports, and BoK policy. That is why Korea can look like both an oil-importer casualty in FX and a winner in equities at the same time.

*Sources: [[Financial Times|FT]], "AI boom outweighs [[Iran]] war pain, Korean central bank chief says," May 28 2026: https://www.ft.com/content/2d1c6dbb-aef5-4f08-bc5a-20c0aa3c1149; Bank of Korea, "Economic Outlook (May 2026)": https://www.bok.or.kr/eng/bbs/E0000634/view.do?depth=400423&menuNo=400423&nttId=10098207&programType=newsDataEng&relate=Y.*

---

## Who benefits

- [[Memory]] makers: [[SK Hynix]], [[Samsung]], [[Micron]]
- [[TSMC]]: [[CoWoS]] packaging for HBM integration
- Equipment: [[ASE]], testers, advanced packaging tools
- End demand: [[NVIDIA]], [[AMD]], [[Broadcom]] custom silicon

---

## [[China]] HBM gap

[[China]]'s HBM problem is no longer "no domestic activity." It is "no public proof of qualified domestic volume." The demand pull is real: [[Huawei]], [[Cambricon]], [[Biren Tech]], [[ByteDance]], [[Baidu]], [[Alibaba]], and [[DeepSeek]] all sit inside a domestic accelerator ecosystem that needs HBM-class bandwidth. [[ChangXin Memory]] has enough reported HBM activity to matter for the watchlist. But as of June 28, 2026, public evidence still does not show a named customer qualification, qualified HBM3E/HBM4 shipment, or global pricing impact from Chinese HBM supply.

> Key insight: the export-control chokepoint has shifted from "China has no workaround" to "China has a roadmap but not validated volume." That still preserves incumbent pricing power until [[Huawei]]-, [[Cambricon]]-, or [[Biren Tech]]-class accelerators publicly qualify domestic HBM.

### What [[China]] has vs lacks

| Layer | Public evidence | Missing proof |
|---|---|---|
| Domestic DRAM base | [[ChangXin Memory]] lists DDR5, LPDDR5/5X, DDR4, and LPDDR4X products | Cost/yield parity with [[Samsung]], [[SK Hynix]], and [[Micron]] |
| HBM product | HBM2 production claims and HBM3 sample/testing reports exist | Public HBM SKU, yield, volume shipment, or customer acceptance |
| [[Packaging]] and test | Reported domestic stacking / [[Advanced packaging]] work and Shanghai back-end plans | Qualified TSV, known-good-die, stack-test, and final-test flow at volume |
| Customers | Domestic AI chips create HBM-class demand; [[Huawei]] has discussed in-house HBM branding | Named [[ChangXin Memory]] HBM qualification at [[Huawei]], [[Cambricon]], [[Biren Tech]], or hyperscale buyers |
| Market impact | [[SemiAnalysis]] via Barron's flagged possible CXMT HBM wafer allocation in 2027-2028 | Evidence Chinese HBM is lowering global HBM prices today |

### The bandwidth gap

The useful comparison is illustrative rather than absolute: if China relies on HBM2E/HBM3-class domestic supply while [[NVIDIA]] platforms move through HBM3E and HBM4, the per-stack gap remains large.

| Metric | HBM2E-class supply | HBM3E / HBM4 leader supply | Difference |
|---|---:|---:|---:|
| Bandwidth | ~460 GB/s | ~1.15 TB/s to 1.5+ TB/s | 2.5x-3.3x |
| Capacity/stack | ~16 GB | ~36 GB to 48GB+ | 2.25x-3x |
| Commercial status | reported / legacy / domestic-roadmap | qualified incumbent supply | qualification, not physics alone |

### Why it is hard

HBM is not just a DRAM wafer problem. It is a stack-yield and customer-qualification problem. The hard parts compound:

- front-end DRAM yield and die size
- TSV formation and thinning
- known-good-die screening before stacking
- stack assembly and thermal reliability
- advanced package integration with accelerators and substrates
- final qualification by the accelerator customer

That is why HBM2 claims or HBM3 samples do not automatically become global supply relief. A domestic stack can be strategically material to [[China semiconductor strategy]] before it becomes an investable threat to incumbent HBM margins.

### Why it matters for AI

| Workload | Bottleneck | HBM impact |
|----------|------------|------------|
| Training | Compute + memory | Partially offset by more chips |
| Inference (prefill) | Compute | Less affected |
| Inference (decode) | [[Memory]] bandwidth | Directly limited by HBM gap |

The problem: Decode phase (token generation) is memory-bound. See [[Inference disaggregation]]. More chips can't fix per-chip bandwidth limits.

### Strategic implications

- [[China AI clusters]] can match training FLOPS through brute force
- Inference speed/quality is structurally disadvantaged
- [[Export controls]] remain effective because qualified HBM is the chokepoint
- Domestic HBM is a medium-term watch item, not a 2026 price breaker
- The signal that changes the read is named HBM3/HBM3E qualification by [[Huawei]], [[Cambricon]], or [[Biren Tech]]

### What to watch

| Watch item | Why it matters |
|---|---|
| Named HBM3/HBM3E customer qualification | Moves China from roadmap to validated AI-infrastructure supply |
| HBM wafer allocation in 2027-2028 | Tests whether reported capacity forecasts become real output |
| Shanghai back-end packaging ramp | Shows whether domestic stacking/test constraints are easing |
| [[Huawei]] in-house HBM supplier disclosure | Distinguishes true domestic supply from branding / module-level integration |
| Incumbent strategic customer agreements | Confirms whether [[Micron]], [[Samsung]], and [[SK Hynix]] retain pricing floors despite China capacity |

---

*Updated 2026-06-28 (China HBM reality check)*

---

## Sources

- CXMT official product page, checked June 28 2026: https://www.cxmt.com/en/product.html
- [[Reuters]], "Chinese firms make headway producing high-bandwidth memory for AI chipsets," May 2024: https://www.reuters.com/technology/chinese-firms-make-headway-producing-high-bandwidth-memory-ai-chipsets-2024-05-15/
- [[Financial Times]], 2025 reporting on CXMT HBM3 sample testing and equipment/material constraints: https://www.ft.com/content/64caeab8-a326-4626-98fb-e1bf665827d3; https://www.ft.com/content/f3ee292b-ba56-4e9f-944a-da26d5706583
- Barron's / [[SemiAnalysis]], Jun 25 2026, CXMT disruption concerns and possible HBM wafer allocation: https://www.barrons.com/livecoverage/stock-market-news-today-062526/card/concerns-about-china-s-cxmt-disrupting-memory-supply-likely-overplayed-pi57kJKTvjOjuaSC69yu
- [[Micron]] FY3Q26 results and prepared remarks, Jun 24 2026: https://investors.micron.com/news-releases/news-release-details/micron-technology-inc-reports-record-results-third-quarter
- [[Samsung]] Q1 2026 earnings presentation: https://images.samsung.com/is/content/samsung/assets/global/ir/docs/2026_1Q_conference_eng.pdf
- [[SK Hynix]] HBM4 development / mass-production readiness, Sep 12 2025: https://news.skhynix.com/sk-hynix-completes-worlds-first-hbm4-development-and-readies-mass-production/

---

## Related

- [[Memory]] — parent industry hub; HBM is the premium product layer
- [[GPU memory scaling]] — the structural trend driving HBM demand
- [[Korea Memory]] — Korean HBM-leadership micro-cluster
- [[SK Hynix]] — supplier (#1 HBM, won't supply [[China]])
- [[Samsung]] — supplier (#2 HBM, aligned with US)
- [[Micron]] — supplier (#3 HBM, US company)
- [[Memory shortage 2025-2026]] — context (HBM demand causing shortage)
- [[Advanced packaging]] — requirement ([[CoWoS]] for integration)
- [[ChangXin Memory]] — domestic Chinese DRAM and HBM roadmap actor
- [[YMTC]] — reported domestic HBM packaging / stacking collaborator
- [[Huawei]] — strategic target customer for domestic HBM
- [[Cambricon]] — domestic accelerator demand pull
- [[Biren Tech]] — domestic accelerator demand pull
- [[Ascend]] — Huawei accelerator family constrained by memory bandwidth
- [[NVIDIA]] — customer (primary HBM buyer)
- [[China AI clusters]] — affected by HBM qualification gap
- [[Export controls]] — mechanism (HBM as chokepoint)
- [[Inference disaggregation]] — context (decode is memory-bound)
- [[Long memory]] — thesis (HBM oligopoly = pricing power)
