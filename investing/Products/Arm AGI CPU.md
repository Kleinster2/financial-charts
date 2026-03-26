---
aliases: [AGI CPU, Arm AGI]
tags:
  - product
  - semiconductor
  - cpu
  - ai-infrastructure
  - datacenter
---

The Arm AGI CPU is [[Arm Holdings]]' first production silicon in 35 years — a 136-core data center CPU built on [[TSMC]] 3nm, designed for [[Agentic AI]] inference workloads, co-developed with [[Meta]]. Announced March 24, 2026. Volume production H2 2026. Management projects $15B in annual revenue from this product line by 2031 — nearly 4x Arm's entire current revenue. The chip targets companies that can't afford to build custom Arm-based silicon, positioning it as the "off-the-shelf Arm server CPU" for the non-hyperscaler market.

---

## Market discovery timeline

The AGI CPU was telegraphed for months. The 16% stock move on March 25 wasn't the chip — it was the revenue ambition.

| Date | Event | Market reaction |
|------|-------|-----------------|
| 2023 | Development begins internally at Arm | Not disclosed at time |
| Jul 30, 2025 | Arm tells investors it's investing in chip-making (Q1 FY2026 earnings) | ARM drops ~20% over subsequent months — margin dilution fear |
| Jul 31, 2025 | TrendForce: "Arm Reportedly Weighs Chiplet and Solution Development, Raising Customer Tensions" | Industry press picks up customer conflict angle |
| Aug 18, 2025 | Arm hires [[Amazon]] AI exec to lead chip effort | Signal confirmed |
| Mar 20, 2025 | [[SoftBank]] acquires [[Ampere Computing]] for $6.5B | Ecosystem play becomes visible — SoftBank building full-stack Arm server portfolio |
| Feb 4, 2026 | Q3 FY2026 earnings: Haas hints at March 24 event, "details pending" | Anticipation builds |
| Mar 24, 2026 | AGI CPU announced at "Arm Everywhere" event, San Francisco. Chip specs, Meta partnership, customer list revealed | ARM closes down 1.5% — chip expected, specs land flat |
| Mar 25, 2026 | Revenue projections detailed: $15B AGI CPU / $25B total / $9 EPS by 2031. CFO guides 50% gross margin | ARM jumps 16% — scale was the surprise |

The gap between March 24 (down 1.5%) and March 25 (up 16%) tells the story: the market had priced in "Arm is making a chip." It had not priced in "Arm thinks this chip will generate 4x their current total revenue." Citi: revenue forecasts "well above even the highest of speculated estimates."

---

## Specifications

| Spec | Detail |
|------|--------|
| Cores | Up to 136 Neoverse V3 |
| ISA | Armv9.2 |
| Vector units | Dual 128-bit SVE2 per core (bfloat16, INT8 MMLA) |
| Process | [[TSMC]] 3nm N3P |
| Packaging | Two-die chiplet (single logical chip) |
| Clock | 3.2 GHz all-core, 3.7 GHz boost |
| TDP | 300W (air-cooled envelope) |
| Memory | 12x DDR5 channels, up to 8800 MT/s |
| Memory bandwidth | 800+ GB/s total, 6 GB/s per core |
| Memory latency | Sub-100ns |
| I/O | 96 PCIe Gen6 lanes |
| CXL | Native CXL 3.0 (memory expansion/pooling) |
| Chiplet interconnect | AMBA CHI Extension Links |
| Threading | Dedicated core per program thread (no SMT) — deterministic performance |
| Compliance | OCP DC-MHS, Arm SystemReady |

### Reference server design

1U dual-node chassis (OCP DC-MHS compliant, 21" ORv3 rack):

| Metric | Value |
|--------|-------|
| Nodes per 1U | 2 (independent compute nodes) |
| CPUs per node | 1 Arm AGI CPU |
| Memory per node | 12 DDR5 DIMM slots |
| Storage per node | E1.S boot + data drives (PCIe Gen5 SSDs) |
| Networking per node | 1x OCP NIC 3.0 |
| BMC | ASPEED AST2600 (DC-SCM 2.1) |
| Chassis power | 1,100W nominal (dual-node) |
| Power delivery | 48V bus bar (OCP ORv3) |
| Cooling | Dual rotor fans, 19+1 redundant |

### Rack-level density

| Configuration | Cores per rack |
|---------------|---------------|
| Air-cooled (standard 36kW rack) | 8,160 |
| Liquid-cooled | 45,000+ |

Arm claims 2x performance per rack versus comparable x86 deployments (which require 500W TDP and 2U chassis). This translates to up to $10B in CAPEX savings per GW of AI data center capacity.

---

## Competitive comparison

| CPU | Maker | Architecture | Cores | Neoverse gen | Process | TDP | Status |
|-----|-------|-------------|-------|-------------|---------|-----|--------|
| AGI CPU | [[Arm Holdings]] | Arm (first-party) | 136 | V3 | [[TSMC]] 3nm | 300W | H2 2026 production |
| Graviton4 | [[Amazon]] | Arm (custom) | 96 | V2 | — | — | Shipping (AWS M8) |
| Axion (gen 1) | [[Google]] | Arm (custom) | 72 | V2 | — | — | Shipping (GCP C4A) |
| Axion (gen 2) | [[Google]] | Arm (custom) | — | N3 | — | — | Announced |
| Cobalt 200 | [[Microsoft]] | Arm (Neoverse CSS) | 132 | V3 | [[TSMC]] 3nm | — | Shipping (Azure) |
| Grace | [[NVIDIA]] | Arm (custom) | 72 | V2 | — | — | Shipping |
| Vera CPU | [[NVIDIA]] | Arm (custom) | 88 | — | — | — | Announced |
| AmpereOne Aurora | [[Ampere Computing]] | Arm (Neoverse-based) | 512 | — | — | — | Announced |
| EPYC Turin (9005) | [[AMD]] | x86 (Zen 5) | 192 | N/A | [[TSMC]] 3/4nm | 500W | Shipping |
| Xeon 6 Granite Rapids | [[Intel]] | x86 | 128 | N/A | Intel 3 | 500W | Shipping |

The AGI CPU's 136 Neoverse V3 cores at 300W match [[Microsoft]]'s Cobalt 200 (132 V3 cores) most closely — both use the same Neoverse generation and [[TSMC]] 3nm. The difference: Cobalt is Azure-exclusive; AGI CPU is available to anyone. [[Ampere Computing]]'s Aurora promises 512 cores but on an older architecture.

Against x86: the AGI CPU runs at 300W vs 500W for top-end EPYC/Xeon, fitting two nodes in 1U vs one node in 2U — the 2x rack density claim follows from this physics.

---

## Economics

| Metric | Value |
|--------|-------|
| Gross margin | ~50% (per CFO Jason Child) |
| Revenue target (AGI CPU alone) | $15B/yr by 2031 |
| Revenue target (total Arm) | $25B/yr by 2031 |
| EPS target | $9 by 2031 |
| Current total revenue (FY2025) | $4.01B |
| Implied IP business growth | Doubles to ~$10B by 2031 |
| Pricing positioning | "Competitively priced" vs custom silicon programs (Mohamed Awad) |

Citi analysis: "$15B in revenue would drive $7.5B/$5B in incremental gross/operating profit — such a significant increase versus prior expectations that the market should not worry about the change in margin structure. It is the incremental profit and cash flow that is the driver of shareholder value."

The 50% gross margin was high enough to kill the margin compression bear thesis. The IP business runs at ~95% gross margins, but $15B at 50% generates more absolute gross profit ($7.5B) than the entire IP business does today.

---

## Customers and ecosystem

### Chip customers (confirmed)

| Customer | Use case |
|----------|----------|
| [[Meta]] | Lead partner / co-developer. Orchestrating alongside MTIA (Meta Training and Inference Accelerator). Multi-generation roadmap commitment |
| [[OpenAI]] | Inference infrastructure for ChatGPT and API |
| [[Cerebras]] | Accelerator management / control plane |
| [[Cloudflare]] | Edge cloud, API hosting, agentic workloads |
| F5 | Application delivery, networking |
| Positron | AI inference |
| Rebellions | Korean AI chip company |
| SAP | Enterprise applications |
| SK Telecom | Telco AI infrastructure |

### OEMs / ODMs (server manufacturers)

| Partner | Status |
|---------|--------|
| Lenovo | Early systems available |
| Supermicro | Early systems available |
| ASRock Rack | Early systems available |
| Quanta Computer | Early systems available |

### Ecosystem supporters (50+)

Advantest, Altera, AMI, [[Amazon|AWS]], Amkor, Arista, ASE Holdings, [[Broadcom]], Bristol Centre for Supercomputing, Cadence, Canonical, Cisco, Databricks, Furiosa, GitHub, [[Google|Google Cloud]], Hugging Face, [[Intel]] Foundry, [[Marvell]], MediaTek, [[Micron]], [[Microsoft|Microsoft Azure]], MongoDB, Nutanix, [[NVIDIA]], NXP, [[OpenAI]], Open Compute Project, Oracle Cloud, Red Hat, Redis, [[Samsung]], Siemens, SK hynix, Snowflake, Socionext, ST Micro, StatsChipPac, SUSE, Supermicro, [[Synopsys]], [[TSMC]], VMware.

### Notable ecosystem quotes

[[NVIDIA]] CEO Jensen Huang: "Our partnership began nearly two decades ago... Together we're creating one seamless platform, from cloud to edge to AI factories."

[[Amazon|AWS]] SVP James Hamilton: "The majority of compute capacity AWS added to our fleet in 2025 was powered by Graviton. This collaboration has been great for both companies."

[[TSMC]] SVP Kevin Zhang: "As the Arm AGI CPU manufacturer, we are excited to support this breakthrough platform. By leveraging our advanced 3nm process technology, the new Arm AGI CPU delivers significant performance and energy efficiency."

---

## The agentic AI thesis

The AGI CPU is purpose-built around a specific claim: agentic AI workloads are CPU-bound, not GPU-bound.

Traditional AI (chatbot query → model inference → response) is GPU-heavy. Agentic AI (persistent agents that reason, plan, coordinate, and act autonomously) requires sustained CPU compute for:

- Task scheduling and orchestration
- Memory management across long-running sessions
- Data movement between accelerators
- Networking and storage I/O
- Security enforcement
- Control plane processing

Arm claims data centers will need 4x current CPU capacity per GW as agent-driven applications scale. The AGI CPU's design reflects this: dedicated core per thread (no SMT, no throttling under sustained load), massive memory bandwidth (6 GB/s per core), and extensive I/O (96 PCIe Gen6 lanes) for accelerator connectivity.

[[NVIDIA]]'s own framing supports the thesis: the company recently told CNBC that CPUs are "becoming the bottleneck" as agentic AI reshapes compute requirements.

---

## Roadmap

| Milestone | Timeline |
|-----------|----------|
| Development started | 2023 |
| Test chips received, functional | Early 2026 |
| Early systems shipping to partners | March 2026 |
| Volume production | H2 2026 |
| Next-generation design | 12-18 months post-launch |

Led by Mohamed Awad, SVP Cloud AI. Arm has confirmed additional designs in the pipeline at 12-18 month cadence — implying gen 2 by late 2027/early 2028.

---

## Related

- [[Arm Holdings]] — parent company, first in-house chip in 35 years
- [[Meta]] — lead partner and co-developer, multi-generation commitment
- [[TSMC]] — fabrication on 3nm N3P
- [[OpenAI]] — customer
- [[Cerebras]] — customer
- [[Cloudflare]] — customer
- [[Agentic AI]] — target workload, CPU-bound thesis
- [[Ampere Computing]] — [[SoftBank]]-owned Arm server chip competitor/complement
- [[RISC-V]] — open-source ISA alternative
- [[Semiconductors]] — sector
- [[Intel]] — x86 competitor (Xeon)
- [[AMD]] — x86 competitor (EPYC)
- [[Amazon]] — Graviton competitor/Arm IP customer
- [[Google]] — Axion competitor/Arm IP customer
- [[Microsoft]] — Cobalt competitor/Arm IP customer (closest spec match: 132 V3 cores)
- [[NVIDIA]] — Grace/Vera competitor/Arm IP customer
