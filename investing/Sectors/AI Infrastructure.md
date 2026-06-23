---
aliases: [AI infra, AI compute, AI compute infrastructure, AI stack]
---
#sector #ai #infrastructure #tech

# AI [[Infrastructure]]

Stack index for the physical and cloud layer powering AI workloads. The analytical work lives in the layer-level children below; this note is the stack map plus parent-level synthesis (capex, demand, financing).

> [!info] Stack index, not a single tradeable cluster
> Internal correlation across the 22 mapped AI Infrastructure actors averages 0.27 over the trailing year — the stack diagram below is conceptually right but the price driver is not shared across compute, storage, data centers, power, and cooling. The analytical entry points are the children that trade as coherent clusters: [[AI Compute]] (0.58), [[AI Storage]], [[Data Centers]] (0.26 — itself broad), [[DC REITs]] (0.40), [[Memory]] (0.38), [[Connectivity]] (0.34). See [[2026-05-09-sector-internal-correlation-diagnostic]] for method and full table.

---

## Correlation structure

| Metric | Value | Interpretation |
|--------|-------|----------------|
| Avg correlation | 0.27 | Diluted — stack-level, not tradeable as one |
| Mapped actors | 22 | spans compute, storage, DC, power, cooling |
| Period | trailing ~252 sessions | |
| Method | pairwise log-return correlation | [[2026-05-09-sector-internal-correlation-diagnostic]] |

The parent is a stack-level taxonomy; tradeable clusters are the layer children. Read the matrix at the child level — see the layer table below.

---

## Stack as index

```
Applications ([[ChatGPT]], [[Copilot]], etc.)
        ↓
Cloud / Compute       → see [[AI Compute]] (chips), [[Data Centers]] (cloud + neoclouds)
        ↓
Chips                 → see [[AI Compute]] (training/inference accelerators), [[Memory]] / [[HBM]], [[Connectivity]] (networking silicon)
        ↓
Storage               → see [[AI Storage]], [[AI storage bottleneck]]
        ↓
Data Centers          → see [[Data Centers]], [[DC REITs]]
        ↓
Power                 → see [[Power constraints]], [[Nuclear power for AI]], [[Grid infrastructure super-cycle]], [[Global DC grid strain]]
        ↓
Cooling               → no dedicated hub yet; tracked via [[Vertiv]], [[Modine Manufacturing]], [[Schneider Electric]]
```

Each arrow is a layer that prices off a different driver. The parent hub (this note) is for cross-layer synthesis — capex aggregates, demand drivers, capacity-financing flows, and the stack-wide thesis. Member companies, layer-specific charts, and within-layer correlation diagnostics live in the children.

---

## Layers — analytical entry points

| Layer | Where it lives | Avg corr | Lens | Active thesis |
|-------|----------------|---------:|------|---------------|
| Compute (chips + foundry) | [[AI Compute]] | 0.58 | [[TSMC]] + its largest AI customers ([[NVIDIA]], [[AMD]]) priced as a cluster | [[Long NVIDIA]], [[Long TSMC]] |
| Memory ([[HBM]] + DRAM/NAND) | [[Memory]] / [[Korea Memory]] / [[US Memory]] | 0.38 / 0.53 / 0.70 | [[HBM]] cycle, packaging-bound supply | [[Long memory]] |
| Storage (training/inference fabric) | [[AI Storage]] | n/a | [[Pure Storage]], [[VAST Data]], Weka, NetApp — GPU-feed bottleneck | — |
| Networking (compute fabric) | [[Connectivity]] | 0.34 | [[Broadcom]], [[Marvell]], [[Cisco]], Arista — chip-side and switch-side | — |
| Cloud + neocloud | [[Data Centers]] (overview) / [[Crypto-to-AI]] (0.61, neocloud cluster) / [[DC REITs]] (0.40, colocation REITs) | varies | [[AWS]], Azure, GCP captive vs [[CoreWeave]] / [[Lambda Labs]] vs [[Equinix]] / [[Digital Realty]] | [[Long datacenter infrastructure]] |
| Power | [[Power constraints]], [[Nuclear power for AI]], [[Grid infrastructure super-cycle]], [[Global DC grid strain]] | n/a | [[Constellation Energy]], [[Vistra]], [[NextEra Energy]], [[Oklo]], [[NuScale]] | [[Long nuclear]] |
| Cooling / power equipment | no hub yet | n/a | [[Vertiv]], [[Modine Manufacturing]], [[Schneider Electric]], [[Eaton]] | — |
| Packaging (cross-layer chokepoint) | [[Advanced packaging]] concept; trades through [[AI Compute]] and [[Semiconductor Test]] | n/a | [[CoWoS]] capacity, [[TSMC]]-bound | [[Long OSAT and test equipment]] |

---

## Capex aggregate (parent-level synthesis)

Hyperscaler AI capex (2025 estimates):

| Company | AI capex | YoY |
|---------|----------|-----|
| [[Microsoft]] | ~$80B | +40% |
| [[Google]] | ~$50B | +30% |
| [[Amazon]] | ~$75B | +35% |
| [[Meta]] | ~$40B | +25% |

Total hyperscaler capex approaching $300B annually. [[Gartner]] (Jan 2026) puts total 2026 AI infrastructure spending above $1.3T once neoclouds, sovereigns, and enterprise are included — the gap between the hyperscaler total and the full number is captured in [[AI infrastructure financing]].

---

## Demand drivers

| Driver | Impact | Where it shows up |
|--------|--------|-------------------|
| LLM training | Massive GPU clusters | [[AI Compute]], [[Memory]] |
| Inference scaling | Growing faster than training | [[AI Compute]], [[AI Storage]], [[Connectivity]] |
| [[Agentic AI]] | Always-on compute | [[AI Compute]], [[Power constraints]] |
| Enterprise adoption | Broadening demand | [[Data Centers]], [[DC REITs]] |
| Sovereign AI | Government buildouts | [[Data Centers]], [[Nuclear power for AI]] |

---

## Bottlenecks (2025-2026)

| Bottleneck | Constraint | Where to track | Beneficiaries |
|------------|------------|----------------|---------------|
| GPU supply | NVIDIA capacity | [[AI Compute]] | [[NVIDIA]], [[TSMC]] |
| [[HBM]] | [[Memory]] shortage | [[Memory]] / [[Korea Memory]] | [[SK Hynix]], [[Samsung]] |
| [[CoWoS]] packaging | [[TSMC]] capacity | [[Advanced packaging]] | [[TSMC]], OSAT |
| Power | Grid constraints | [[Power constraints]] / [[Global DC grid strain]] | utilities, nuclear |
| Cooling | [[Thermal limits]] | no hub yet — [[Vertiv]], [[Modine Manufacturing]] | Vertiv, Modine |
| [[Real estate]] | Land/permits | [[DC REITs]] | data center [[REITs]] |
| Storage feed | GPU idle waiting on data | [[AI Storage]] / [[AI storage bottleneck]] | [[VAST Data]], [[Pure Storage]] |

See [[Power constraints]], [[Memory shortage 2025-2026]], [[Advanced packaging]], [[AI storage bottleneck]].

---

## Cross-layer thesis: capacity becomes a financing stack

[[Anthropic hyperscaler financing surge April 2026]] is the clearest current example of the AI infrastructure stack becoming a financing stack rather than a sequence of separable line items. [[Amazon]] committed $5B upfront and up to $20B future while [[Anthropic]] committed more than $100B over ten years to [[AWS]] technologies and up to 5 GW of capacity. [[Google]] committed $10B upfront and up to $30B future while [[Google Cloud]] reportedly provides 5 GW over five years, on top of the Apr 6 Google/[[Broadcom]] [[TPU]] expansion.

The May 6 [[Colossus]] 1 lease to [[Anthropic]] (≈0.3 GW deliverable now) folds the same logic into a [[Training-to-inference cluster rotation]]: a heterogeneous cluster that prices as inference capacity, not training capacity, becomes a financing instrument as well as compute. The sector read-through is that cloud, chips, data centers, and power are no longer separable — frontier labs need capital and capacity together, and hyperscalers will finance customers if it anchors demand for their custom silicon and data center buildout.

The trade for this hub is [[AI infrastructure financing]] — capital providers and the cross-layer flow itself, rather than any one layer.

---

## Investment theses anchored to this hub

| Thesis | Lives in | Notes |
|--------|----------|-------|
| [[Long NVIDIA]] | [[AI Compute]] | compute dominance |
| [[Long datacenter infrastructure]] | [[Data Centers]], [[DC REITs]] | picks & shovels |
| [[Long nuclear]] | [[Nuclear power for AI]] | power solution |
| [[Long memory]] | [[Memory]] | [[HBM]] demand |
| [[AI infrastructure financing]] | parent-level | capital providers / cross-layer flow |

---

## Risks

| Risk | Impact | Where to watch |
|------|--------|----------------|
| AI winter / demand slowdown | Overcapacity | [[Data Centers]], [[AI Compute]] |
| [[Power constraints]] | Buildout delays | [[Power constraints]], [[Global DC grid strain]] |
| Regulation | Compute restrictions | [[Export controls]] |
| Competition to [[NVIDIA]] | Margin compression | [[AI Compute]] |
| Hyperscaler insourcing | Chip vendor displacement | [[AI Compute]] ([[TPU]], [[Trainium]]) |

---

## Related

- [[Data Centers]] — data-center sector hub
- [[AI hyperscalers]] — demand
- [[Power constraints]] — bottleneck
- [[AI storage bottleneck]] — storage-specific constraint
- [[Project Stargate]] — $500B initiative
- [[CES 2026]] — product announcements
- [[Robotics]] — next AI infrastructure wave
- [[Anthropic hyperscaler financing surge April 2026]] — cross-layer financing case
- [[Training-to-inference cluster rotation]] — cluster-asset rotation framework
- [[Anthropic vs OpenAI compute race]] — capacity-procurement contest
- [[Situational Awareness LP]] — AI-infrastructure investor whose 13F separates bottleneck longs from crowded semiconductor-beta hedges

## Sources

- [[Gartner]] (Jan 2026) — total AI infrastructure spending forecast
- [[2026-05-09-sector-internal-correlation-diagnostic]] — children correlation table

*Restructured 2026-05-10 — promoted from layer-by-layer member-list to stack-level index. Members live in children.*
