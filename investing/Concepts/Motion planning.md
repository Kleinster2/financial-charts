---
aliases: [Motion planning, Trajectory optimization, Path planning]
---
#concept #robotics #ai #control

**Motion planning** — How a robot decides what movements to make to achieve a goal while avoiding obstacles and respecting physical constraints. The bridge between knowing where you are ([[State estimation]]) and executing actions.

---

## Why it matters for investors

Motion planning determines whether a robot can work in cluttered, dynamic environments or only in cleared factory floors. It's the capability that separates a $16K [[Unitree]] G1 doing scripted assembly from a general-purpose household robot. Solving motion planning in unstructured environments is a prerequisite for the mass-market humanoid opportunity.

---

## Classical vs. learned approaches

| Approach | How it works | Strengths | Weaknesses |
|----------|-------------|-----------|------------|
| RRT/PRM | Random sampling of configuration space | Completeness guarantees | Slow for high-DOF robots |
| Trajectory optimization | Optimize smooth path subject to constraints | Elegant, efficient | Needs good initialization |
| Model predictive control (MPC) | Re-plan continuously over short horizon | Reactive, handles dynamics | Compute-intensive |
| Learned policies (RL) | Neural net maps state → action directly | Fast inference, adapts | No safety guarantees |
| Hybrid | Classical planning + learned refinement | Best of both | Complex to engineer |

The industry is moving toward hybrid: classical planners for safety-critical constraints + learned policies for dexterity and adaptation.

---

## The degrees-of-freedom challenge

| Robot | DOF | Planning difficulty |
|-------|-----|-------------------|
| Robot arm (industrial) | 6 | Solved (decades of work) |
| Mobile base + arm | 9-10 | Commercially viable |
| Quadruped | 12-16 | Solved via RL |
| Humanoid ([[Unitree]] G1) | 43 | Active frontier |
| Humanoid + manipulation | 50+ | Research stage |

More DOF = exponentially harder planning. A 43-DOF humanoid carrying an object while walking on uneven terrain is orders of magnitude harder than a 6-DOF factory arm.

---

## Real-time requirements

| Task | Planning budget | Approach |
|------|----------------|----------|
| Factory pick-and-place | 100ms+ | Classical optimization |
| Walking on flat ground | 10-50ms | MPC + RL |
| Catching a thrown object | <10ms | Pure RL (reflexive) |
| Full-body manipulation while walking | 5-20ms | Hybrid, emerging |

Humanoids doing useful work need to plan whole-body motion (legs + arms + torso) in milliseconds. This is why on-robot compute matters — cloud latency kills real-time planning.

---

## Investment implications

- **Compute on the edge:** Motion planning can't wait for cloud roundtrips → drives demand for [[NVIDIA]] Jetson/Thor and on-robot processors
- **Simulation dependency:** Motion planning algorithms are tested in sim first → [[Sim-to-real transfer]] matters
- **DOF as moat:** Companies with experience planning for high-DOF systems ([[Unitree]], [[Boston Dynamics]]) have accumulated know-how that's hard to replicate

---

*Created 2026-02-19*

---

## Related

- [[State estimation]] — prerequisite (must know where you are to plan)
- [[Embodied AI]] — parent framework
- [[Reinforcement learning for locomotion]] — learned locomotion policies
- [[Sim-to-real transfer]] — planning policies trained in simulation
- [[Unitree]] — 43-DOF G1 humanoid
- [[Boston Dynamics]] — state-of-the-art dynamic motion planning
- [[NVIDIA]] — on-robot compute for real-time planning
