---
aliases: [Ascend, HiSilicon]
---
#actor #china #fabless

# Huawei

Chinese tech conglomerate and primary target of US export controls. Developing indigenous chips (Kirin, [[Ascend]]) despite restrictions. Proof case for [[China]]'s ability to work around sanctions.

---

## Why it matters

Huawei is the test case for export control effectiveness:
- **Kirin 9000S**: 7nm chip in Mate 60 Pro despite US sanctions
- [[Ascend]] AI chips: Competing with NVIDIA A100 in [[China]]
- HiSilicon: Fabless design arm, once top-10 globally

If Huawei succeeds, it validates [[China]]'s indigenous chip strategy. If it stagnates, it proves restrictions work.

---

## Chip portfolio

### Mobile (Kirin)
| Chip | Node | Foundry | Status |
|------|------|---------|--------|
| Kirin 9000S | 7nm | SMIC | [[Shipping]] (Mate 60 Pro) |
| Kirin 9100 | 5nm? | SMIC | Rumored 2025-26 |

How they did it: SMIC multi-patterning on DUV (no EUV). Lower yields, higher cost, but functional.

### AI/Data center ([[Ascend]])
| Chip | Comparison | Status |
|------|------------|--------|
| [[Ascend]] 910B | ~A100 performance | [[Shipping]] |
| [[Ascend]] 910C | Improved 910B | [[Shipping]] |
| [[Ascend]] 920 | [[Target]] H100 | Development |

Adoption: Alibaba, [[Baidu]], [[Tencent]] using for domestic AI training. Not export-competitive but sufficient for [[China]] market.

### [[AI Infrastructure]] (CloudMatrix / SuperPoD)

Huawei's answer to NVIDIA NVLink — proprietary interconnect for massive [[Ascend]] clusters:

CloudMatrix 384 vs GB200 NVL72:

| Spec | CloudMatrix 384 | NVIDIA GB200 NVL72 |
|------|-----------------|-------------------|
| Chips | 384 [[Ascend]] 910C | 72 Blackwell |
| Performance | 300 petaFLOPS BF16 | ~180 petaFLOPS |
| Memory | 3x more aggregate | Baseline |
| Power | 4.1x higher | Baseline |
| Power/FLOP | 2.5x worse | Baseline |

The trade-off: 5x more Ascends offsets each chip being 1/3 the performance. Brute force wins on raw FLOPS.

Interconnect technology:

| Feature | Details |
|---------|---------|
| Topology | All-to-all optical |
| Transceivers | 6,912 LPO (800 Gbps each) |
| Internal bandwidth | 5.5 Pbps (687.5 TB/s) |
| Claimed vs NVLink | 62x faster than NVLink144 |

Huawei's edge: [[Telecom]] DNA — decades of carrier-grade networking experience.

SuperPoD roadmap:

| System | Timeline | Scale |
|--------|----------|-------|
| SuperPoD | 2025 | 15,000 chips |
| Atlas 950 | Late 2026 | 8,000+ chips |
| Atlas 960 | 2027 | ~15,500 chips |

Why it matters: Combined with [[China power advantage]], Huawei can deploy massive clusters that match NVIDIA on aggregate compute despite per-chip disadvantage.

### Apr 2026: DeepSeek V4 validates the Supernode stack

[[CNN]] reported on Apr. 24, 2026 that [[DeepSeek]]'s V4 Preview is supported by Huawei Supernode technology combining large [[Ascend]] 950 clusters. [[Counterpoint Research|Counterpoint]]'s Wei Sun described V4 as running on domestic chips from Huawei and [[Cambricon Technologies]], in contrast to [[DeepSeek-R|R1]]'s NVIDIA-trained lineage.

This is the cleanest public validation of Huawei's AI-infrastructure strategy so far. Huawei does not need each chip to match [[NVIDIA]] on a per-accelerator basis if it can bind enough domestic chips together with its telecom-grade interconnect and make the system usable for a frontier-adjacent open model. The strategic win is ecosystem capture: Chinese developers optimize for Ascend/CANN because the model they want to use is already there.

For export controls, this is the scenario [[Jensen Huang]] warned about: if US hardware exits China, Chinese labs train and deploy on Huawei instead. The risk for the US stack is not that Huawei immediately beats Blackwell; it is that Huawei becomes good enough, scaled enough, and sovereign enough to become the default for [[China AI Plus]] deployment.

#### Apr 27 2026 — white paper + state-media framing closes the loop

DeepSeek's V4 technical white paper, surfaced in commentary on Bloomberg "The China Show" Apr 27, describes V4 as trained "almost exclusively" on Huawei [[Ascend]] hardware. A social-media account affiliated with Chinese state media on the same day framed the launch timing as evidence of "deeper integration with the Chinese chip ecosystem" — turning what could have been an engineering footnote into the official narrative anchor of the release. [[Bloomberg Intelligence]]'s [[Robert Lee]]: with V4 running near-frontier (~10% gap to leading [[Anthropic]] models per Lifebench) on cheap domestic compute, the practical chance of Chinese hyperscalers issuing wholesale [[Nvidia]] orders for V4-class workloads is "probably pretty limited." That moves Huawei from "domestic alternative" to default Chinese training-stack provider for the sovereign-deployment use case. See [[DeepSeek-V]] Apr 27 entry for the broader frontier-gap and pricing discussion.

### Networking
- Still major [[5G]] equipment provider (outside US/allies)
- Banned from US, [[UK]], [[Australia]], others

---

## Supply chain

| Component | Source | Constraint |
|-----------|--------|------------|
| Foundry | SMIC | Stuck at 7nm, N5 very limited |
| Memory | Domestic + stockpiles | [[HBM]] shortage |
| EDA tools | Domestic alternatives | Years behind [[Synopsys]]/[[Cadence]] |
| Equipment | Stockpiled + domestic | [[ASML]] EUV banned |

Key constraint: Cannot access leading-edge nodes. SMIC 7nm is 4-5 years behind TSMC N3.

---

## Apr 2026: smart-driving compute becomes an auto-AI wedge

At the Apr 2026 Beijing Auto Show, [[Reuters]] reported that Huawei plans to invest more than $10B over five years to boost computing power for smart driving. Automotive sales remain a relatively small part of Huawei's portfolio, but Reuters noted it is the company's fastest-growing segment.

This extends Huawei's national-champion role from telecom and AI chips into [[Automotive AI]]. The company can supply smart-driving systems, domestic compute, operating-system integration, and chip know-how to automakers that want to reduce dependence on [[NVIDIA]], [[Qualcomm]], and foreign software stacks. [[Dongfeng Motor]] is one example of a state-owned automaker working with Huawei on smart-driving systems.

---

## Strategic positioning

### Strengths
- Massive domestic market (1.4B people)
- Government backing (Big Fund, policy support)
- Proven workaround capability (Kirin 9000S)
- Vertical integration (HiSilicon design + Huawei systems)

### Weaknesses
- Cut off from TSMC, [[Samsung]] foundry
- EDA tools lagging
- [[HBM]] supply limited
- Export markets shrinking

---

## Export control history

| Date | Action |
|------|--------|
| May 2019 | Added to Entity List |
| Aug 2020 | FDPR extended — cut off from TSMC |
| Dec 2020 | SMIC added to Entity List |
| Sep 2023 | Mate 60 Pro launch — proved workaround |
| 2024-25 | Continued restrictions, [[Ascend]] adoption grows |
| Jun 2025 | [[Taiwan]] blacklisted Huawei + [[SMIC]] (unprecedented) |
| Sep 2025 | 3-year chip roadmap unveiled |
| Dec 2025 | NVIDIA H200 approved for [[China]] (25% surcharge) |

---

## 3-year chip roadmap (Sep 2025)

Huawei unveiled aggressive semiconductor development plan:

| Timeframe | [[Target]] |
|-----------|--------|
| 2025-26 | Scale [[Ascend]] 910C production (millions of units) |
| 2026-27 | [[Ascend]] 920 targeting H100 performance |
| 2027-28 | Next-gen architecture |

Scale ambitions: US intelligence estimates Huawei can produce millions of [[Ascend]] 910C units in 2026 (vs ~200K in 2025).

---

## Shadow manufacturing network

Huawei has built extensive workaround infrastructure:

| Component | Approach |
|-----------|----------|
| Foundry | SMIC multi-patterning on DUV (no EUV) |
| Equipment | Stockpiled + domestic alternatives |
| Supply chains | Multiple intermediary networks |
| Procurement | [[Shell]] companies, third-party buyers |

Reality: Despite export controls, Huawei continues advancing through combination of stockpiles, domestic alternatives, and supply chain workarounds.

---

## Thesis implications

| Thesis | Impact |
|--------|--------|
| [[Long TSMC]] | Huawei was major customer, now lost |
| [[Long WFE]] | [[China]] equipment demand partly driven by Huawei alternatives |
| [[Export controls]] | Huawei success = controls failing; struggle = controls working |

---

## National champion strategy (Jan 2026)

[[David Sacks]] (Davos, Jan 23): [[China]] is actively blocking NVIDIA chip imports to create a protected market for Huawei. This is the telecom playbook applied to AI chips.

| Phase | Strategy |
|-------|----------|
| Phase 1 | [[Block]] foreign competition (NVIDIA H200 imports blocked by customs) |
| Phase 2 | Huawei dominates domestic [[China]] market at scale |
| Phase 3 | Use domestic scale to compete globally |

The telecom parallel ([[Michael Kratsios]], Davos):
- In Trump I era, Huawei wasn't the best telecom technology — "certainly subpar compared to Ericsson and [[Nokia]]"
- But was "good enough" and "subsidized enough" to become default telecom for much of the world
- [[China]] now applying same playbook: AI chips don't need to be best, just good enough + subsidized + scaled

Why scale matters: Chip production is a scale-up business. Domestic market dominance gives Huawei:
- Volume to drive down per-unit costs
- Revenue to fund R&D (compare to SMIC advancing despite controls)
- Installed base for software ecosystem development
- Platform to proliferate globally (especially global south)

Sacks's test: "If in 5 years we look around the world and it's Huawei chips and DeepSeek models, then we lost."

US counter: American AI Export Program — turnkey AI packages (inference chips + models) for developing countries. See [[Export controls]].

*Source: Davos panel (Sacks, Kratsios, Bartiromo), Jan 23 2026*

---

## Jensen Huang citation (Dwarkesh, Apr 15, 2026)

[[NVIDIA]] CEO [[Jensen Huang]] used Huawei extensively as the rebuttal anchor to the "export controls are working" thesis:

- "Huawei is having its largest revenue year in history" — cited to contradict the premise that entity-listing slowed Huawei's AI chip business
- Roughly 50% of the world's AI researchers live in [[China]]; [[China]] builds 60% of mainstream chips
- "There's plenty of [[HBM2]]" — pushes back on the narrative that [[HBM]] supply is the binding constraint
- "Gang chips" — multiple lower-bandwidth memory dies ganged together to substitute for HBM3/HBM4
- Silicon photonics is being used to route around advanced packaging limits
- "7nm is enough" — [[SMIC]]-class nodes are sufficient for competitive training systems at cost penalty
- Worst case for the US: "[[DeepSeek]] running on Huawei is a horrible outcome for America" — if US AI stacks exit China, Chinese-origin open-weight models on Ascend become the global default

Jensen's framing: the point is not that Huawei has matched [[NVIDIA]], but that it has enough supply, enough talent, and enough ecosystem to become the default if US platforms retreat. See [[Export controls]] for the policy debate and [[Jensen Huang]] for his full rebuttal.

---

## What to watch

- [ ] Kirin next-gen node (5nm on SMIC?)
- [ ] [[Ascend]] 920 vs H100 benchmarks
- [ ] Huawei cloud AI adoption in [[China]]
- [ ] SMIC yield improvements
- [ ] Potential export control tightening
- [ ] Global AI chip proliferation — Huawei [[Ascend]] exports to global south
- [ ] Automotive AI compute — >$10B five-year smart-driving compute investment, domestic alternative to foreign auto-AI stacks
- [ ] American AI Export Program — US counter to Huawei global push

---

## Financials

| Metric | Value |
|--------|-------|
| Status | Private (employee-owned) |
| Revenue (2024) | ~$100B |
| R&D spend | ~$25B/year |
| Employees | ~200,000 |
| Smartphone share | Recovering in [[China]] |
| Listed | No (private) |

Ownership: Employee stock ownership plan. Not investable directly.

---

*Updated 2026-04-24*

---

## Related

- [[NVIDIA]] — competitor (CloudMatrix vs NVLink)
- [[SMIC]] — foundry partner (7nm Kirin, [[Ascend]])
- [[Export controls]] — constraint (Entity List since 2019)
- [[Taiwan tech protectionism]] — [[Taiwan]] blacklisted Huawei (Jun 2025)
- [[China power advantage]] — enabler (powers brute force strategy)
- [[Kunlunxin]] — domestic competitor ([[Baidu]]'s AI chips)
- [[David Sacks]] — articulated national champion threat (Davos Jan 2026)
- [[Michael Kratsios]] — telecom parallel from Trump I
- [[DeepSeek]] — model layer of [[China]] AI export strategy
- [[Ericsson]] — historical telecom competitor (outcompeted by subsidized Huawei)
- [[ByteDance]] — customer ([[Ascend]] adoption)
- [[Alibaba]] — customer ([[Ascend]] for cloud)
- [[TSMC]] — former foundry (cut off 2020)
- [[US-China tech race]] — global semiconductor investment context
- [[Automotive AI]] — smart-driving compute and vehicle OS context
- [[Dongfeng Motor]] — state-owned smart-driving partner context
- [[China AI Plus]] — policy umbrella for embedding AI in hardware
