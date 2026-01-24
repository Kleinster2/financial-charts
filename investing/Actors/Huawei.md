---
aliases: [Ascend, HiSilicon]
---
#actor #china #fabless

# Huawei

Chinese tech conglomerate and primary target of US export controls. Developing indigenous chips (Kirin, Ascend) despite restrictions. Proof case for China's ability to work around sanctions.

---

## Why it matters

Huawei is the test case for export control effectiveness:
- **Kirin 9000S**: 7nm chip in Mate 60 Pro despite US sanctions
- **Ascend AI chips**: Competing with NVIDIA A100 in China
- **HiSilicon**: Fabless design arm, once top-10 globally

If Huawei succeeds, it validates China's indigenous chip strategy. If it stagnates, it proves restrictions work.

---

## Chip portfolio

### Mobile (Kirin)
| Chip | Node | Foundry | Status |
|------|------|---------|--------|
| Kirin 9000S | 7nm | SMIC | Shipping (Mate 60 Pro) |
| Kirin 9100 | 5nm? | SMIC | Rumored 2025-26 |

**How they did it**: SMIC multi-patterning on DUV (no EUV). Lower yields, higher cost, but functional.

### AI/Data center (Ascend)
| Chip | Comparison | Status |
|------|------------|--------|
| Ascend 910B | ~A100 performance | Shipping |
| Ascend 910C | Improved 910B | Shipping |
| Ascend 920 | Target H100 | Development |

**Adoption**: Alibaba, Baidu, Tencent using for domestic AI training. Not export-competitive but sufficient for China market.

### AI Infrastructure (CloudMatrix / SuperPoD)

Huawei's answer to NVIDIA NVLink — proprietary interconnect for massive Ascend clusters:

**CloudMatrix 384 vs GB200 NVL72:**

| Spec | CloudMatrix 384 | NVIDIA GB200 NVL72 |
|------|-----------------|-------------------|
| Chips | 384 Ascend 910C | 72 Blackwell |
| Performance | 300 petaFLOPS BF16 | ~180 petaFLOPS |
| Memory | 3x more aggregate | Baseline |
| Power | 4.1x higher | Baseline |
| Power/FLOP | 2.5x worse | Baseline |

**The trade-off:** 5x more Ascends offsets each chip being 1/3 the performance. Brute force wins on raw FLOPS.

**Interconnect technology:**

| Feature | Details |
|---------|---------|
| Topology | All-to-all optical |
| Transceivers | 6,912 LPO (800 Gbps each) |
| Internal bandwidth | 5.5 Pbps (687.5 TB/s) |
| Claimed vs NVLink | 62x faster than NVLink144 |

**Huawei's edge:** Telecom DNA — decades of carrier-grade networking experience.

**SuperPoD roadmap:**

| System | Timeline | Scale |
|--------|----------|-------|
| SuperPoD | 2025 | 15,000 chips |
| Atlas 950 | Late 2026 | 8,000+ chips |
| Atlas 960 | 2027 | ~15,500 chips |

**Why it matters:** Combined with [[China power advantage]], Huawei can deploy massive clusters that match NVIDIA on aggregate compute despite per-chip disadvantage.

### Networking
- Still major 5G equipment provider (outside US/allies)
- Banned from US, UK, Australia, others

---

## Supply chain

| Component | Source | Constraint |
|-----------|--------|------------|
| Foundry | SMIC | Stuck at 7nm, N5 very limited |
| Memory | Domestic + stockpiles | HBM shortage |
| EDA tools | Domestic alternatives | Years behind Synopsys/Cadence |
| Equipment | Stockpiled + domestic | ASML EUV banned |

**Key constraint**: Cannot access leading-edge nodes. SMIC 7nm is 4-5 years behind TSMC N3.

---

## Strategic positioning

### Strengths
- Massive domestic market (1.4B people)
- Government backing (Big Fund, policy support)
- Proven workaround capability (Kirin 9000S)
- Vertical integration (HiSilicon design + Huawei systems)

### Weaknesses
- Cut off from TSMC, Samsung foundry
- EDA tools lagging
- HBM supply limited
- Export markets shrinking

---

## Export control history

| Date | Action |
|------|--------|
| May 2019 | Added to Entity List |
| Aug 2020 | FDPR extended — cut off from TSMC |
| Dec 2020 | SMIC added to Entity List |
| Sep 2023 | Mate 60 Pro launch — proved workaround |
| 2024-25 | Continued restrictions, Ascend adoption grows |
| **Jun 2025** | **Taiwan blacklisted Huawei + [[SMIC]]** (unprecedented) |
| **Sep 2025** | **3-year chip roadmap unveiled** |
| Dec 2025 | NVIDIA H200 approved for China (25% surcharge) |

---

## 3-year chip roadmap (Sep 2025)

Huawei unveiled aggressive semiconductor development plan:

| Timeframe | Target |
|-----------|--------|
| 2025-26 | Scale Ascend 910C production (millions of units) |
| 2026-27 | Ascend 920 targeting H100 performance |
| 2027-28 | Next-gen architecture |

**Scale ambitions:** US intelligence estimates Huawei can produce millions of Ascend 910C units in 2026 (vs ~200K in 2025).

---

## Shadow manufacturing network

Huawei has built extensive workaround infrastructure:

| Component | Approach |
|-----------|----------|
| **Foundry** | SMIC multi-patterning on DUV (no EUV) |
| **Equipment** | Stockpiled + domestic alternatives |
| **Supply chains** | Multiple intermediary networks |
| **Procurement** | Shell companies, third-party buyers |

**Reality:** Despite export controls, Huawei continues advancing through combination of stockpiles, domestic alternatives, and supply chain workarounds.

---

## Thesis implications

| Thesis | Impact |
|--------|--------|
| [[Long TSMC]] | Huawei was major customer, now lost |
| [[Long WFE]] | China equipment demand partly driven by Huawei alternatives |
| [[Export controls]] | Huawei success = controls failing; struggle = controls working |

---

## National champion strategy (Jan 2026)

**[[David Sacks]] (Davos, Jan 23):** China is actively blocking NVIDIA chip imports to create a protected market for Huawei. This is the telecom playbook applied to AI chips.

| Phase | Strategy |
|-------|----------|
| **Phase 1** | Block foreign competition (NVIDIA H200 imports blocked by customs) |
| **Phase 2** | Huawei dominates domestic China market at scale |
| **Phase 3** | Use domestic scale to compete globally |

**The telecom parallel ([[Michael Kratsios]], Davos):**
- In Trump I era, Huawei wasn't the best telecom technology — "certainly subpar compared to Ericsson and Nokia"
- But was "good enough" and "subsidized enough" to become default telecom for much of the world
- China now applying same playbook: AI chips don't need to be best, just good enough + subsidized + scaled

**Why scale matters:** Chip production is a scale-up business. Domestic market dominance gives Huawei:
- Volume to drive down per-unit costs
- Revenue to fund R&D (compare to SMIC advancing despite controls)
- Installed base for software ecosystem development
- Platform to proliferate globally (especially global south)

**Sacks's test:** "If in 5 years we look around the world and it's Huawei chips and DeepSeek models, then we lost."

**US counter:** American AI Export Program — turnkey AI packages (inference chips + models) for developing countries. See [[Export controls]].

*Source: Davos panel (Sacks, Kratsios, Bartiromo), Jan 23 2026*

---

## What to watch

- [ ] Kirin next-gen node (5nm on SMIC?)
- [ ] Ascend 920 vs H100 benchmarks
- [ ] Huawei cloud AI adoption in China
- [ ] SMIC yield improvements
- [ ] Potential export control tightening
- [ ] **Global AI chip proliferation** — Huawei Ascend exports to global south
- [ ] **American AI Export Program** — US counter to Huawei global push

---

## Financials

| Metric | Value |
|--------|-------|
| Status | Private (employee-owned) |
| Revenue (2024) | ~$100B |
| R&D spend | ~$25B/year |
| Employees | ~200,000 |
| Smartphone share | Recovering in China |
| Listed | No (private) |

**Ownership:** Employee stock ownership plan. Not investable directly.

---

*Updated 2026-01-23*

---

## Related

- [[NVIDIA]] — competitor (CloudMatrix vs NVLink)
- [[SMIC]] — foundry partner (7nm Kirin, Ascend)
- [[Export controls]] — constraint (Entity List since 2019)
- [[Taiwan tech protectionism]] — Taiwan blacklisted Huawei (Jun 2025)
- [[China power advantage]] — enabler (powers brute force strategy)
- [[Kunlunxin]] — domestic competitor (Baidu's AI chips)
- [[David Sacks]] — articulated national champion threat (Davos Jan 2026)
- [[Michael Kratsios]] — telecom parallel from Trump I
- [[DeepSeek]] — model layer of China AI export strategy
- [[Ericsson]] — historical telecom competitor (outcompeted by subsidized Huawei)
- [[ByteDance]] — customer (Ascend adoption)
- [[Alibaba]] — customer (Ascend for cloud)
- [[TSMC]] — former foundry (cut off 2020)
- [[US-China tech race]] — global semiconductor investment context
