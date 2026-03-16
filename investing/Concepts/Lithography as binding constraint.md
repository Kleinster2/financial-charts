#concept #semiconductors #bottleneck #lithography #asml

Lithography as binding constraint — [[ASML]]'s EUV tool production is THE bottleneck for scaling AI compute through 2030. Not power, not data centers, not packaging — the semiconductor supply chain itself.

---

## Synthesis

The bottleneck has rotated. 2023: [[CoWoS]] packaging. 2024-2025: power and data centers. 2026+: the chips themselves, and specifically the machines that make them. [[Dylan Patel]] ([[SemiAnalysis]], Mar 2026) frames this simply: 3.5 EUV tools = 1 GW of AI compute. [[ASML]] makes ~70 tools/year, growing to ~100 by 2030. Cumulative installed base reaches ~700 by decade end. Even if 100% were allocated to AI (they won't be), that's ~200 GW — less than what [[Sam Altman]] (52 GW/year), [[Elon Musk]] (100 GW/year), and [[Anthropic]]+[[Google]]+[[Meta]] collectively want.

Power and data centers were shorter lead-time bottlenecks. CoWoS is simpler packaging. Fabs take 2-3 years to build (vs <1 year for data centers). The tools inside those fabs have even longer supply chains — [[Carl Zeiss SMT|Zeiss]] lenses, Cymer sources, reticle stages moving at 9 Gs — each artisanal, each with thousands of sub-suppliers. [[ASML]] has said its supply chain includes 10,000+ companies.

The semiconductor supply chain is "not AGI-pilled." Everyone in it thinks they're expanding fast by going from 60 to 100 tools/year. The AI labs think they need capacity for 200+ GW/year. This gap is the central tension in AI scaling through the end of the decade.

---

## The math: EUV tools → gigawatts

For 1 GW of [[NVIDIA]] [[Rubin]] data center capacity:

| Component | Wafers needed | EUV passes/wafer | Total EUV passes |
|-----------|--------------|-----------------|-----------------|
| 3nm logic | ~55,000 | ~20 | ~1.1M |
| 5nm components | ~6,000 | fewer | — |
| DRAM memory | ~170,000 | varies | — |
| Total | — | — | ~2M EUV passes |

An EUV tool does ~75 wafers/hour at ~90% uptime.

Result: ~3.5 EUV tools per gigawatt.

| Metric | Value |
|--------|-------|
| EUV tool price | $300-400M |
| GW data center CapEx | ~$50B |
| EUV cost per GW | ~$1.2B |
| Ratio | EUV tools are 2.4% of total GW cost |

The cheapest component in the stack is the hardest to scale.

---

## ASML production trajectory

| Year | EUV tools/year | Cumulative installed base |
|------|---------------|--------------------------|
| 2024 | ~60 | ~250-300 |
| 2025 | ~70 | ~320-370 |
| 2026 | ~70-80 | ~400-450 |
| 2027 | ~80 | ~480-530 |
| 2028 | ~90 | ~570-620 |
| 2029 | ~95 | ~665-715 |
| 2030 | ~100 | ~700 |

At 3.5 tools/GW, ~700 EUV tools = ~200 GW theoretical max (if 100% allocated to AI).

Reality: mobile, PC, automotive, and other chips also need EUV. AI's share is large and growing but not 100%. Sam Altman's 52 GW/year target (~25% of total fabbed capacity) is "very reasonable" — he's at roughly 25% of [[Blackwell]] deployment this year already.

---

## Why ASML can't just scale faster

### The four major EUV tool components

| Component | Maker | Constraint |
|-----------|-------|-----------|
| EUV source | Cymer (San Diego, ASML-owned) | Tin droplet laser system — hits droplet 3x in sequence |
| Reticle stage | Wilmington, CT | Moves at 9 Gs, sub-nanometer accuracy |
| Wafer stage | Europe | Complementary to reticle, opposite direction |
| Optics/lenses | [[Carl Zeiss SMT]] (Europe) | 18 multilayer mirrors per tool, artisanal production |

Each mirror: perfect layers of molybdenum and ruthenium, stacked, any defect ruins it. Total production: ~1,000/year for ~60 tools. [[Carl Zeiss SMT|Zeiss]] employs <1,000 people on this work. You can't just hire and train replacements — these are "super, super specialized" engineers.

The full tool is so large it's assembled in Eindhoven, deconstructed, shipped on multiple planes, and reassembled at the customer site. That process alone takes months.

### ASML's conservative culture

ASML has lived through semiconductor boom-bust cycles. They view going from 60 to 100 tools/year as aggressive growth. They have not tried to "YOLO expand" capacity. [[Leopold Aschenbrenner]] jokes he's the only [[SemiAnalysis]] client who says their numbers are too low — "everyone else tells me our numbers are too high."

### ASML's pricing generosity

Despite having an absolute monopoly, ASML has "never raised the price more than they've increased the capability of the tool." Tool prices went from $150M to $400M, but capabilities more than doubled (throughput, overlay accuracy). [[NVIDIA]] takes the margin. Memory makers take margin. [[TSMC]] takes some. ASML leaves money on the table — a cultural choice, not an economic one.

---

## Bottleneck rotation timeline

| Period | Primary bottleneck | Lead time | Resolution |
|--------|-------------------|-----------|------------|
| 2023 | [[CoWoS]] packaging | Months | Simpler process, scaled quickly |
| 2024-2025 | Power + data centers | 6-18 months | Behind-the-meter gas, multiple solutions |
| 2026+ | Semiconductor manufacturing | 2-3 years (fabs) + tool supply | No quick fix |

Why prior bottlenecks resolved faster:
- CoWoS is simpler packaging technology
- Power generation has 16+ vendor types (combined-cycle, aeroderivatives, reciprocating engines, fuel cells, solar+battery)
- Data centers can be built in 8 months ([[Amazon]] record)
- None of these require the most complicated machines humans make at volume

---

## The ASML arbitrage opportunity

Patel raised an unexploited trade: someone could put down $1B in deposits for 10 EUV tools, wait for the market to realize there aren't enough, and sell the option at a premium. Same playbook as energy turbine deposits in 2023-2024 (buy [[GE Vernova]] / [[Siemens]] / [[Mitsubishi]] capacity, sell forward).

Problem: ASML probably wouldn't agree. They're too conservative and relationship-driven to let a speculator sit in their allocation queue. But the demand signal from such an attempt could push them to expand faster.

---

## What could break the constraint

| Potential disruptor | Probability | Timeline |
|--------------------|------------|----------|
| ASML scales to 150+/year | Low-medium | 2030+ |
| 3D DRAM reduces EUV passes per bit | Medium | Late 2020s |
| 1000W source (+50% throughput) | High | ~2030 |
| Going back to 7nm DUV for some AI chips | Low | Stopgap only |
| Synchrotron/particle accelerator lithography | Very low | 2030s+ |
| [[Elon Musk]] TeraFab on Samsung process | Medium | 2028+ |

The 1000W source is the most likely near-term relief — [[ASML]] demonstrated it in Feb 2026. At 330 WPH (up from 220), each tool produces 50% more wafers. Effectively turns 700 tools into ~1,050 tool-equivalents.

Going back to 7nm (what [[Huawei]] does with DUV multi-patterning) doesn't work well because:
- Inference performance gap is ~20x between Hopper and [[Blackwell]] on modern workloads (not 2-3x as FLOPS suggest)
- On-chip bandwidth vs inter-chip bandwidth gap widens with smaller nodes
- You can replicate some architectural improvements on old nodes, but not networking or memory bandwidth advances

---

## Related

- [[ASML]] — the monopoly supplier
- [[EUV lithography]] — the technology
- [[Carl Zeiss SMT]] — critical optics supplier
- [[TSMC]] — largest consumer of EUV tools
- [[GPU depreciation cycle]] — why chip supply constraint sustains GPU value
- [[AI compute demand curve]] — demand side of this bottleneck
- [[Supply chain bottlenecks]] — broader supply chain view
- [[Power constraints]] — prior bottleneck (now solvable)
- [[GPU deployment bottleneck]] — downstream effect
- [[SemiAnalysis]] — primary data source for tool tracking
- [[Rubin]] — next-gen chip requiring 3nm EUV capacity
- [[Anthropic vs OpenAI compute race]] — how labs navigate the constraint

*Source: [[Dylan Patel]] ([[SemiAnalysis]]) on Dwarkesh Patel podcast, Mar 13, 2026*

*Created 2026-03-16*
