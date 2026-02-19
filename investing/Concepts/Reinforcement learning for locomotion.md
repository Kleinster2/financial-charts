---
aliases: [RL for locomotion, Legged locomotion RL, Locomotion learning]
---
#concept #robotics #ai #reinforcement-learning

**Reinforcement learning for locomotion** — Training legged robots to walk, run, climb, and recover from disturbances through trial-and-error in simulation, then deploying on real hardware. The specific RL approach that made modern quadrupeds and humanoids possible.

---

## Why it matters for investors

Before ~2019, legged robots walked using hand-crafted controllers that took years to develop and broke on unexpected terrain. RL changed this: train a policy in millions of simulated episodes, transfer to hardware, and the robot handles terrain it was never explicitly programmed for. This breakthrough enabled [[Unitree]]'s consumer-price quadrupeds and is now enabling humanoid locomotion.

---

## How it works

1. **Simulation:** Robot model in physics engine (MuJoCo, Isaac Sim)
2. **Reward design:** Define what "good walking" means (forward speed, energy efficiency, not falling)
3. **Training:** Policy network tries millions of random actions, reinforced when reward is high
4. **Domain randomization:** Vary friction, mass, slopes, disturbances so policy is robust
5. **[[Sim-to-real transfer]]:** Deploy trained policy on physical hardware
6. **Fine-tuning:** Optionally adapt with small amount of real-world data

---

## Key milestones

| Year | Milestone | Significance |
|------|-----------|-------------|
| 2019 | ANYmal learns to walk via RL (ETH Zurich) | First robust sim-to-real legged locomotion |
| 2020 | [[Unitree]] A1 with RL policies | Consumer quadruped with learned locomotion |
| 2022 | Agility Digit walks in warehouses | First commercial humanoid deployment |
| 2023 | [[Unitree]] H1 running at 3.3 m/s | RL-trained humanoid speed record |
| 2024 | [[Unitree]] G1 ships at $16K | Mass-market humanoid with RL locomotion |
| 2025 | [[Unitree]] G1 at -47°C, Spring Gala | RL policies handle extreme conditions |
| 2026 | Factory deployment, 4 m/s running | RL locomotion + manipulation combined |

---

## Reward engineering

The art of RL for locomotion is defining the right reward function:

| Reward term | What it encourages |
|-------------|-------------------|
| Forward velocity | Moving toward goal |
| Energy penalty | Efficient gaits (not flailing) |
| Smoothness | Natural-looking motion |
| Survival bonus | Not falling over |
| Foot clearance | Lifting feet (avoids shuffling) |
| Symmetry | Left-right gait balance |
| Contact timing | Proper foot-strike patterns |

Bad reward design → robot finds "degenerate" gaits (hopping, sliding, exploiting simulation bugs). Reward engineering is as much art as science.

---

## Why quadrupeds first

| Factor | Quadruped | Humanoid |
|--------|-----------|----------|
| DOF | 12-16 | 30-43+ |
| Stability | 4 contact points | 2 contact points |
| Fall recovery | Easier (lower center of gravity) | Much harder |
| Training time | Hours | Days-weeks |
| Hardware risk | Lower (lighter, shorter falls) | Higher |

This gradient explains [[Unitree Quadruped Bridge|Unitree's quadruped bridge strategy]]: master RL locomotion on quadrupeds (cheaper, safer, faster iteration), then transfer algorithms and intuitions to humanoids.

---

## Whole-body control frontier

The current frontier is combining RL locomotion with manipulation — a humanoid walking while carrying objects, opening doors, or assembling parts. This requires:

- Locomotion policy (legs)
- Manipulation policy (arms/hands)
- Coordination layer (don't fall while reaching)

[[UnifoLM]]-X1-0 factory deployment is an early attempt. The "walking while working" problem is the key unlock for humanoid commercial viability.

---

*Created 2026-02-19*

---

## Related

- [[Embodied AI]] — parent concept
- [[Sim-to-real transfer]] — how RL policies reach real hardware
- [[State estimation]] — required for policy to know robot state
- [[Motion planning]] — classical alternative / complement to RL
- [[Unitree Quadruped Bridge]] — quadruped-first RL strategy
- [[Unitree]] — volume leader in RL-trained legged robots
- [[UnifoLM]] — combines RL locomotion with VLA manipulation
- [[Boston Dynamics]] — historically hand-crafted, now adopting RL
- [[NVIDIA]] — Isaac Lab for RL training
