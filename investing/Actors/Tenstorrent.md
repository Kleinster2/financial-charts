---
aliases: []
---
#actor #ai #semiconductor #usa #private

**Tenstorrent** — Jim Keller's AI chip company. [[RISC-V]] based. Open architecture bet.

---

## Why Tenstorrent matters

Led by legendary chip architect:

| Metric | Value |
|--------|-------|
| Valuation | ~$2.6B (2025) |
| Raised | $700M+ |
| Founded | 2016 |
| CEO | Jim Keller (2021-) |

---

## Jim Keller

**Legendary chip architect:**

| Company | Achievement |
|---------|-------------|
| AMD | K8, Zen architecture |
| [[Apple]] | A4/A5 chips |
| [[Tesla]] | FSD chip |
| [[Intel]] | Brief stint |
| Tenstorrent | CEO |

One of the greatest chip architects alive.

---

## [[RISC-V]] approach

**Open architecture bet:**
- [[RISC-V]] CPU cores
- Open-source ISA
- No ARM/x86 licensing
- Customizable

---

## Products

| Product | Type |
|---------|------|
| Wormhole | AI accelerator chip |
| Grayskull | Earlier generation |
| [[RISC-V]] cores | Licensable IP |
| Chiplets | Modular design |

---

## Business model

**Dual approach:**
1. AI accelerator chips/systems
2. [[RISC-V]] IP licensing

Both hardware and IP revenue.

---

## Open ecosystem

**Counter to NVIDIA lock-in:**
- Open-source software stack
- [[RISC-V]] (vs proprietary)
- Chiplet modularity
- Developer-friendly

---

## Cap table / Investors

| Round | Date | Amount | Valuation |
|-------|------|--------|-----------|
| Series A | 2019 | $25M | — |
| Series B | 2020 | $60M | — |
| Series C | 2023 | $100M | ~$1B |
| Series D | Jan 2025 | $693M | $2.6B |
| **Total** | | **$700M+** | |

**Key investors:**

| Investor | Notes |
|----------|-------|
| AFG Partners | Lead (Series D) |
| [[Hyundai]] Motor Group | Strategic (automotive AI) |
| [[Samsung]] | Strategic |
| LG | Strategic |
| Bezos Expeditions | [[Jeff Bezos]] |
| Eclipse Ventures | Early |
| Real Ventures | Canadian VC |

**Total raised:** $700M+

**Korean strategic angle:** [[Hyundai]], [[Samsung]], LG invested — automotive AI focus

---

## Investment case

**Bull:**
- Jim Keller credibility
- [[RISC-V]] open architecture
- Korean strategic backing
- Alternative to NVIDIA

**Bear:**
- CUDA ecosystem moat
- Late to market
- Unproven at scale
- Execution risk

---

## Quick stats

| Metric | Value |
|--------|-------|
| Ticker | Private |
| Valuation | ~$2.6B |
| CEO | Jim Keller |
| Approach | [[RISC-V]] AI chips |

*Updated 2026-01-01*

---

## San Francisco AI silicon event — pre-event lens (week of Apr 27, 2026)

Tenstorrent holds an AI silicon and customer-benchmark event in San Francisco the week of Apr 27, 2026 — flagged by [[Patrick Moorhead]] in his Apr 26 "Week Ahead in Tech" preview. This is the first formal proof-point delivery moment for the open-architecture / [[RISC-V]] alternative to [[NVIDIA]]. Moorhead frames three watch items: open-architecture momentum, [[RISC-V]] traction, and customer proof points against [[NVIDIA]] / [[AMD]]. The vault's [[AI capex arms race]] thesis treats the event as one of six testable items in Phase 3.

### Why benchmarks alone do not settle the question

[[NVIDIA]]'s moat is the [[CUDA]] developer stack, not chip specs. Specs-equivalent or specs-superior chips have lost on software stack maturity for a decade ([[Cerebras]], [[Groq]], [[SambaNova]]). The deployment bar is whether a frontier lab or hyperscaler can move a real workload onto Tenstorrent silicon without paying a developer-time tax that exceeds the hardware cost savings. The event needs to deliver named customers running real workloads, not just benchmark slides.

### What the event resolves

| Watch item | Why it matters | Tenstorrent state |
|---|---|---|
| Named customers running production workloads | The single most important disclosure. Specific labs / clouds named with deployment context, not vague "ecosystem partners." | Korean strategic ([[Hyundai]], [[Samsung]], LG) named via investment, not deployment |
| MLPerf-equivalent benchmarks vs H100 / MI300 | The chip-specs floor. Need to clear a published, third-party-verifiable benchmark to be credible. [[NVIDIA]]'s critique of [[Google]] [[TPU]] for not submitting MLPerf applies here too. | Wormhole specs disclosed; no MLPerf submission to date |
| Software stack updates (PyBuda, TT-Metalium) | The CUDA-equivalent. Maturity of the compiler, runtime, kernel library, and developer documentation determines whether real teams can port workloads. | Open-source stack; maturity vs CUDA TBD |
| Roadmap clarity post-Wormhole | Wormhole and Grayskull are out. Next-generation silicon timing and process node disclosure determines whether Tenstorrent stays on the roadmap or falls off. | Wormhole shipping; next-gen TBD |
| Korean strategic partner deployment traction | [[Hyundai]] / [[Samsung]] / LG invested for automotive AI. Any production-deployment disclosure (vs strategic-investment posture) is the read on whether the strategic capital converted to volume. | Strategic capital from 2023-2025 rounds; production status TBD |
| Foundry strategy disclosure | [[Samsung]] foundry partnership disclosed earlier; [[Intel]] foundry possibility floated. Whoever fabs Tenstorrent silicon is a read on the multi-year scaling capacity. | Currently mixed (Samsung confirmed); volumes TBD |
| Funding / valuation update | Last round Jan 2025 at $2.6B post-money. Any new round or valuation marker reframes the credibility of the alternative-architecture thesis. | $700M+ raised, $2.6B post-money |

### Structural read

The deployment bar is software-stack maturity, not chip specs. If Tenstorrent delivers named customers, MLPerf-equivalent third-party-verifiable benchmarks, AND a credible developer story, the open-architecture thesis broadens from a private-bet narrative to a market-testable hypothesis. If the event delivers strategic partnerships and benchmark slides without production customers, Tenstorrent stays in the same category as [[Cerebras]] / [[Groq]] / [[SambaNova]] — credible alternative architectures that have not yet broken the [[CUDA]] moat at scale.

This event is the first time the [[Jim Keller]] credibility narrative gets paired with externally verifiable customer adoption. The vault should track post-event whether the question shifts from "can Tenstorrent ship?" to "can Tenstorrent ship at scale?"

---

## Related

- [[NVIDIA]] — competitor (CUDA lock-in target)
- [[AMD]] — connection (Jim Keller origin)
- [[Cerebras]] — peer (alternative AI chip)
- [[Groq]] — peer (inference chip)
- [[SambaNova]] — peer (enterprise AI chip)

