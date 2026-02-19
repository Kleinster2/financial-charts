---
aliases: [Physical AI, Embodied intelligence, Embodied foundation models]
---
#concept #ai #robotics

**Embodied AI** — AI systems that perceive, reason about, and act in the physical world through robotic bodies. The bridge between large language/vision models and real-world manipulation, locomotion, and navigation.

---

## Why it matters for investors

The AI investment cycle so far has been digital: data centers, cloud, software. Embodied AI extends AI into the physical economy — manufacturing, logistics, healthcare, agriculture, construction. This is the next capex cycle after hyperscaler infrastructure.

[[Jensen Huang]] (NVIDIA GTC 2025): "The next wave of AI is physical AI." [[Elon Musk]]: "Optimus will be worth more than everything else Tesla does combined."

---

## Core technical stack

| Layer | Function | Examples |
|-------|----------|---------|
| World models | Predict physical dynamics | [[UnifoLM]]-WMA, Google RT-2 |
| Vision-Language-Action (VLA) | Map perception + language → actions | [[UnifoLM]]-VLA, RT-X, Octo |
| Reinforcement learning | Learn locomotion/manipulation via trial | [[Unitree]] quadruped RL, [[Figure AI]] |
| Simulation | Generate synthetic training data | NVIDIA Isaac, MuJoCo |
| Hardware | Actuators, sensors, compute | Custom actuators, [[NVIDIA]] Jetson/Thor |

The key insight: unlike chatbots, embodied AI requires closing the **perception-action loop** in real time, with safety-critical consequences.

---

## Data engine paradigm

The winning strategy emerging across leaders:

1. Deploy robots in real environments
2. Robots generate task execution data
3. Data trains better models
4. Better models → more capable robots → more data

This mirrors [[Tesla]]'s FSD fleet data flywheel but for manipulation. [[Unitree]]'s factory deployment (G1 building robots via [[UnifoLM|UnifoLM-X1-0]]) is the clearest example. More robots deployed = faster model improvement = wider moat.

**Implication:** Companies with volume shipments ([[Unitree]]: 20K target 2026) compound faster than lab-only players.

---

## The 80/80 benchmark

[[Wang Xingxing]] ([[Unitree]] CEO) proposed robotics' "ChatGPT moment" threshold: a robot must complete **80% of tasks in 80% of unfamiliar environments**. No one is there yet. Current state:
- Controlled factory environments: partially demonstrated
- Customer factories: not yet
- General household: years away

---

## Key players

| Company | Approach | Volume | Status |
|---------|----------|--------|--------|
| [[Unitree]] | Cost-disruption + open-source models | 20K target (2026) | IPO mid-2026 |
| [[Tesla]] Optimus | Vertical integration, FSD transfer | Internal deployment | Production TBD |
| [[Figure AI]] | Humanoid-first, BMW partnership | Pilot | Private ($2.6B raised) |
| [[Boston Dynamics]] | Research-grade, [[Hyundai]] backing | Low volume | Subsidiary |
| [[AGIBOT]] | Chinese humanoid portfolio | Scaling | HK IPO rumored |
| [[Mobileye]] / [[Mentee Robotics]] | ADAS perception → humanoid | Pre-production | $900M acquisition |
| NVIDIA | Platform (Isaac Sim, Thor chips) | Picks & shovels | Public |

---

## Investment frameworks

**Picks and shovels:** [[NVIDIA]] (simulation + compute), [[Teradyne]] (test equipment for robot components), [[Trimble]] (construction environments)

**Volume leaders:** [[Unitree]] (highest humanoid shipments globally), [[Tesla]] (if Optimus scales)

**Data moat:** Companies with closed-loop data engines compound faster. Open-source ([[Unitree]]) vs. closed ([[Tesla]]) is an unresolved strategic debate.

**The "assembly trap":** Skeptics warn that cherry-picked factory demos at 2x speed don't prove commercial viability. The gap between "robot assembles parts in controlled setting" and "robot works 8-hour shift in unknown factory" remains vast.

---

## Timeline

| Year | Milestone |
|------|-----------|
| 2022 | Tesla Optimus prototype, Unitree H1 |
| 2023 | Figure 01 demo, RT-2 (Google) |
| 2024 | Unitree G1 ships at $16K, Figure BMW deal |
| 2025 | Unitree 5,500 humanoids shipped, UnifoLM open-sourced |
| 2026 | Unitree 20K target, factory self-deployment, IPO. Mobileye acquires Mentee ($900M) |
| 2028+ | Warehouse-scale deployment (if 80/80 achieved) |

---

*Created 2026-02-19*

---

## Related

- [[UnifoLM]] — Unitree's embodied AI model family
- [[Unitree]] — volume leader
- [[Humanoid robotics]] — form factor
- [[Robotics]] — sector
- [[Unitree Cost Architecture]] — hardware cost moat
- [[Unitree Quadruped Bridge]] — locomotion transfer advantage
- [[Tesla]] — Optimus competitor
- [[Figure AI]] — US humanoid startup
- [[Boston Dynamics]] — research-grade incumbent
- [[Mobileye]] — ADAS-to-robotics via [[Mentee Robotics]]
- [[NVIDIA]] — simulation + compute platform (Isaac, Thor)
- [[Teradyne]] — test equipment for robotic components
