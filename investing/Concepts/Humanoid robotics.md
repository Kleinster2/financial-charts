#concept #robotics #ai #automation

**Humanoid robotics** — Bipedal robots with human-like form factor. Transitioning from research to commercial deployment (2025-2027).

---

## Cost curve

| Year | Price range | Notes |
|------|-------------|-------|
| 2023 | $50K-$250K | Research prototypes |
| 2024 | $30K-$150K | 40% cost drop (Goldman) |
| 2025 | ~$35K avg | First commercial deployments |
| 2026 | $20K-$50K | Scale production begins |
| 2030 | ~$17K | 51% reduction from 2025 (BoA) |

Cost declining faster than expected — 40% drop 2023→2024 vs. projected 15-20% annual.

---

## Key players

| Company | Model | Price | Status |
|---------|-------|-------|--------|
| [[Tesla]] | Optimus | $25-30K target | Factory deployment, 5-10K units 2025 |
| [[Boston Dynamics]] | Atlas | <$320K | [[Hyundai]] ownership brings auto supply chain |
| [[Figure AI]] | Figure 02 | $30-50K est | $39B valuation (Sep 2025) |
| Unitree | G1 | $13,500 | Cheapest full-featured |
| 1X | NEO | $20K / $499/mo | Deliveries 2026 |

---

## Cost breakdown

| Component | Share | Notes |
|-----------|-------|-------|
| Actuators & motors | 40-50% | Largest cost driver |
| Sensors & vision | 15-20% | LiDAR, depth cameras |
| Compute | 10-15% | On-board AI |
| Frame & structure | 10-15% | |

**Hyundai advantage:** Parts costing $1,000 in robotics cost $100 in automotive due to volume. Atlas benefits from auto supply chain.

---

## Production targets

| Company | 2025 | 2026 | Long-term |
|---------|------|------|-----------|
| [[Tesla]] | 5-10K | 50K | 1M/year by 2027 |

---

## China factor

China robotics financing: 610 deals, 50B yuan ($7B) in first 9 months of 2025 — **250% YoY increase**.

Chinese manufacturers ([[Unitree]], [[UBTech]]) pushing aggressive pricing.

### China vs US: the scorecard (March 2026)

**Chinese companies now capture >90% of global humanoid robot sales** with thousands of units shipped in 2025. [[Unitree]] and [[Zhiyuan Robot]] among [[China]]'s 247 unicorns (Tracxn, Mar 2026).

Per Lian Jye Su (Omdia, chief analyst), three forces driving China's lead:

1. **Manufacturing base** — decades of industrial policy (Made in China 2025, 14th FYP) built high-end engineering capacity that carries into robotics from EVs, solar, aviation
2. **AI + chip capability** — from foundation models to domestically manufactured AI chipsets, full-stack now possible in China
3. **SOE demand** — state-owned enterprises provide guaranteed early adoption that doesn't exist elsewhere. Acts as a deployment catalyst

US companies are "very strong on the technical side" (hardware + software) but lag on production scale. [[Tesla]] Optimus "very probable" for 2027 availability, but the scale question tilts Chinese — manufacturing bases are in Asia.

### Data moat thesis

Deploying at scale creates a data collection flywheel: physical AI lacks public training datasets (no equivalent of Wikipedia/Reddit for real-world robot interaction). The companies shipping thousands of units are collecting proprietary training data for complex physical scenes. Early deployment losses may be the cost of building an irreplicable data moat — same pattern as early AI labs burning capital pre-ChatGPT.

*Source: [Rest of World / Omdia (Feb 25, 2026)](https://restofworld.org/2026/china-tesla-robot-race/)*

---

## China's state-funded robot training farms (Mar 2026)

Dozens of state-funded "robot training farms" have emerged across [[China]] to build large-scale robot-specific training data. The push addresses the key bottleneck: physical AI lacks public training datasets (no equivalent of Wikipedia/Reddit for robot interaction).

**Hubei Humanoid Robot Innovation Center (Wuhan):**

| Metric | Value |
|--------|-------|
| Facility | 12,000 sqm |
| Cost | Rmb200M ($29M) |
| Instructors | 70 (young graduates, 8-hour shifts) |
| Robots | 46 (purchased from [[AGIBOT]] at Rmb350,000 each) |
| Daily data output | ~100 hours of usable data |
| Method | Remote controls + sensor-equipped handheld devices; video labeled with annotations ("pivot left", "extending arm") |
| Data target | "Vision language action" (VLA) models |

**Policy escalation:**
- "Embodied intelligence" identified as **one of six future industries** in [[China]]'s **2026-30 five-year plan** (announced Mar 2026)
- [[MIIT]] strategy document for humanoid robotics to end of 2027: large-scale training databases and multimodal data "central to building the brain" of humanoid robots
- Hubei province: **Rmb10B** state fund for humanoids
- Local governments from Hangzhou to Mianyang pouring money into training farms

**Data collection as demand driver:** [[Bernstein]] estimates data collection sales made up **~20%** of [[China]]'s >20,000 humanoid robot shipments in 2025. Training centers are sustaining manufacturers while real-world demand is still emerging.

**[[China]] 2025 humanoid shipments by end market** (>20,000 units total, [[Bernstein]]):

| End market | Share |
|-----------|-------|
| Education and R&D | 42% |
| Data collection | 19% |
| Human-robot interaction services | 19% |
| Entertainment | 16% |
| Industrial and logistics | 4% |

[[Bernstein]] analyst Jay Huang (head of Asia industrial technologies): "China is becoming smarter in how it supports emerging industries facing bottlenecks." Government-funded data is shared, benefiting all participants.

**Simulation approach:** [[Motphys]] (Wuhan startup, co-founder Zhao Xiang) uses VR headsets for more efficient data collection. Zhao: "An intelligence breakthrough may require hundreds of millions or even billions of hours of data."

**Key challenge — data transferability:** Data collected from one robot cannot easily power another with different hardware. Hardware evolves so fast that today's data may not work for next year's model. [[Google DeepMind]]'s robotics AI models show early promise in cross-platform transfer but it remains an active research area.

**Potemkin risk:** At one training center the FT visited, a dozen humanlike robots hung motionless in a lobby — staff explained they were "the ones that perform when officials come to visit," not used for actual data collection.

*Source: FT (Ryan McMorrow in Wuhan), Mar 11, 2026*

---

## Adoption timeline

| Phase | Timeframe |
|-------|-----------|
| Industrial deployment | 2026-2028 |
| Widespread industrial | 2030s |
| Consumer adoption | 2040s |

---

## Investment implications

- **Near-term winners:** Actuator/motor suppliers, vision systems, compute
- **Watch:** Cost curve vs. labor arbitrage in different markets
- **Risk:** China price competition, labor union resistance

---

## Related

**Companies:**
- [[Tesla]] — Optimus
- [[Boston Dynamics]] — Atlas
- [[Figure AI]] — Figure 02
- [[Hyundai]] — Boston Dynamics owner

**Concepts:**
- [[Motphys]] — Wuhan simulation startup (VR-based data collection)
- [[AGIBOT]] — sold robots to training centers (Rmb350K each)
- [[Embodied AI]] — AI in physical robots
- [[Automation]] — Broader category
- [[Manufacturing automation]] — Key use case

---

*Created 2026-02-02*
