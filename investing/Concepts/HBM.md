---
aliases: [High Bandwidth Memory, HBM3, HBM3E, HBM4]
---
#concept #memory #ai

HBM (High Bandwidth [[Memory]]) — 3D-stacked DRAM enabling massive bandwidth for AI accelerators. The [[Memory|memory]] bottleneck solution for GPUs.

Chart data not applicable for HBM itself; tradeable market exposure lives in [[Korea Memory]] and [[US Memory]].

---

## Synthesis

HBM is the premium bottleneck inside the memory cycle. It converts generic DRAM scarcity into AI-infrastructure pricing power because accelerator customers need bandwidth, validated stacks, and guaranteed supply more than cheap commodity bits. That concentrates the cleanest exposure in [[Korea Memory]], where [[SK Hynix]] and [[Samsung]] control the supply curve, while [[Micron]] gives [[US Memory]] a smaller but still relevant HBM channel.

The strategic read-through is that HBM makes [[Export controls]] more effective and the memory shortage more durable. [[China]] can build domestic AI accelerators, but without HBM3E/HBM4 access it remains structurally bandwidth-constrained, especially in decode-heavy inference. For positioning, HBM is the bridge between the [[Memory shortage 2025-2026]] supercycle, Korea's macro upgrade, and the separation of Korea memory from US semi beta.

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

[[China]]'s AI clusters are stuck on HBM2E while NVIDIA uses HBM3E — a structural disadvantage.

> Key insight: HBM is the chokepoint that makes [[Export controls]] effective. GPUs can be designed domestically ([[Ascend]], Kunlun). HBM cannot — the oligopoly (SK Hynix, Samsung, Micron) is aligned with US policy. No workaround exists.

### The gap

| Metric | HBM2E ([[China]]) | HBM3E (NVIDIA) | [[Gap]] |
|--------|---------------|----------------|-----|
| Bandwidth | 460 GB/s | 1.15 TB/s | 2.5x |
| Capacity/stack | 16 GB | 36 GB | 2.25x |
| Generation | 2022 | 2024 | 2 years |

### Why [[China]] can't close it

| Supplier | Status |
|----------|--------|
| [[SK Hynix]] | Won't supply (US pressure, export controls) |
| [[Samsung]] | Won't supply (aligned with US) |
| [[Micron]] | Won't supply (US company) |
| Domestic ([[ChangXin Memory]]) | Years behind, no HBM production |

The bottleneck: HBM is an oligopoly. All three suppliers aligned with US export policy. No domestic source.

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
- [[Export controls]] are effective because HBM is chokepoint
- No near-term workaround — domestic HBM is years away

---

*Updated 2026-02-03 (market forecast)*

---

## Related

- [[Memory]] — parent industry hub; HBM is the premium product layer
- [[GPU memory scaling]] — the structural trend driving HBM demand
- [[Korea Memory]] — Korean HBM-leadership micro-cluster
- [[SK Hynix]] — supplier (\#1 HBM, won't supply [[China]])
- [[Samsung]] — supplier (\#2 HBM, aligned with US)
- [[Micron]] — supplier (\#3 HBM, US company)
- [[Memory shortage 2025-2026]] — context (HBM demand causing shortage)
- [[Advanced packaging]] — requirement ([[CoWoS]] for integration)
- [[NVIDIA]] — customer (primary HBM buyer)
- [[China AI clusters]] — affected (stuck on HBM2E)
- [[Export controls]] — mechanism (HBM as chokepoint)
- [[Inference disaggregation]] — context (decode is memory-bound)
- [[Long memory]] — thesis (HBM oligopoly = pricing power)
