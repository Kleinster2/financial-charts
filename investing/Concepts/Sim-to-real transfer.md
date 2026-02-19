---
aliases: [Sim-to-real, Sim2real, Domain transfer, Reality gap]
---
#concept #robotics #ai #simulation

**Sim-to-real transfer** — Training robots in simulated environments, then deploying learned behaviors on physical hardware. The "reality gap" between simulation physics and the real world is a core bottleneck in [[Embodied AI]].

---

## Why it matters for investors

Simulation is cheap and parallelizable — you can run millions of training episodes overnight. Real-world training is slow, expensive, and breaks hardware. Every robotics company needs a sim-to-real strategy. The quality of that transfer determines how fast they can iterate.

This is why [[NVIDIA]]'s Isaac platform is a picks-and-shovels play on the entire robotics industry.

---

## The reality gap

| Simulated | Real world |
|-----------|-----------|
| Perfect physics | Friction varies, surfaces deform |
| Exact joint positions | Backlash, wear, calibration drift |
| Clean sensor data | Noise, occlusion, lighting changes |
| Instant reset after failure | Hardware breaks, costs money |
| Deterministic | Stochastic |

Policies trained purely in simulation often fail catastrophically on real hardware. The gap must be bridged.

---

## Bridging strategies

| Strategy | How it works | Who uses it |
|----------|-------------|-------------|
| Domain randomization | Randomize physics params in sim (friction, mass, delays) so policy learns robustness | [[Unitree]], OpenAI (Dactyl) |
| System identification | Measure real-world physics, calibrate sim to match | [[Boston Dynamics]], academia |
| Fine-tuning on real data | Pre-train in sim, adapt with small real-world dataset | [[Figure AI]], most startups |
| Digital twins | High-fidelity replica of specific real environment | [[NVIDIA]] Isaac, factory automation |
| Residual RL | Learn a correction layer on top of sim-trained policy using real data | Emerging approach |

Domain randomization is the dominant approach — make simulation deliberately noisy and varied so the policy becomes robust to real-world messiness.

---

## NVIDIA's platform play

[[NVIDIA]] Isaac ecosystem:

| Component | Function |
|-----------|----------|
| Isaac Sim | Physics simulation for robot training |
| Isaac Lab | RL training framework |
| Isaac ROS | Perception + nav for real deployment |
| Omniverse | Digital twin infrastructure |
| Thor (Jetson) | On-robot compute |

NVIDIA doesn't build robots — they sell the simulation and compute stack to everyone who does. Classic picks-and-shovels.

---

## Why real-world data wins long-term

Simulation can bootstrap, but [[Unitree]]'s data engine thesis argues real-world data ultimately wins:

- Sim captures ~90% of physics — the last 10% (surface texture, cable flex, thermal expansion) requires real contact
- Real-world data captures failure modes simulation can't predict
- Companies with volume deployments ([[Unitree]]: 20K target) generate data that sim-only players cannot

The winning formula is likely **sim for bootstrap + real-world for refinement** — not one or the other.

---

## Connection to stack

Sim-to-real sits between training infrastructure and deployment:

Training in sim → **Sim-to-real transfer** → [[State estimation]] → [[Embodied AI|World models]] → Action

Poor transfer = policy that worked in sim fails on hardware. Good transfer = months of development time saved.

---

*Created 2026-02-19*

---

## Related

- [[Embodied AI]] — parent concept
- [[State estimation]] — must work in real world, not just sim
- [[UnifoLM]] — trained with real-world data (Embodied Avatar)
- [[NVIDIA]] — Isaac simulation platform
- [[Unitree]] — real-world data engine approach
- [[Tesla]] — FSD sim + fleet data parallel
- [[Reinforcement learning for locomotion]] — primary consumer of sim-to-real
