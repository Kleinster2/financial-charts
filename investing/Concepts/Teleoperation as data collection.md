---
aliases: [Teleoperation data collection, Human-in-the-loop robotics, Learning from demonstration]
---
#concept #robotics #ai #data

**Teleoperation as data collection** — Using human operators to remote-control robots, generating kinematically correct training data for [[Embodied AI]] models. The bootstrap method before full autonomy — humans teach robots by doing.

---

## Why it matters for investors

The biggest bottleneck in embodied AI isn't algorithms — it's data. Unlike language (internet-scale text) or vision (billions of images), there is no internet-scale dataset of robot manipulation. Teleoperation is the primary method for creating one. Companies with efficient data collection pipelines iterate faster.

---

## How it works

1. Human operator wears VR headset / haptic gloves / exoskeleton
2. Operator controls robot remotely, performing tasks (grasping, assembly, cleaning)
3. Robot records: joint positions, forces, camera feeds, actions taken
4. Data is curated and used to train VLA models (vision-language-action)
5. Trained model replaces human operator for that task

The human provides the intelligence; the robot provides the embodied data in its own kinematic frame.

---

## Key platforms

| Company | System | Method |
|---------|--------|--------|
| [[Unitree]] | Embodied Avatar | VR teleoperation of G1 → feeds [[UnifoLM]] training |
| [[Figure AI]] | Teleop rigs | Human demonstrations → policy learning |
| [[Tesla]] | Optimus data collection | Employees wearing motion-capture suits |
| Toyota Research | Diffusion Policy | Bimanual teleoperation demos |
| UC Berkeley | ALOHA / Mobile ALOHA | Low-cost bimanual teleop ($20K rigs) |

---

## Data quality hierarchy

| Source | Quality | Scale | Cost |
|--------|---------|-------|------|
| Expert teleoperation | Highest | Low | Expensive |
| Crowd-sourced teleop | Medium | Medium | Moderate |
| Simulation | Variable | Unlimited | Cheap |
| Autonomous trial-and-error (RL) | Low initially | High | Compute cost |
| Internet video | Low (no action labels) | Massive | Free |

Expert teleoperation produces the best data but doesn't scale. The industry is converging on **teleop to bootstrap → autonomous deployment to scale** — exactly [[Unitree]]'s data engine strategy.

---

## The data flywheel transition

```
Phase 1: Humans teleoperate → collect demonstrations
Phase 2: Train model on demonstrations → robot attempts autonomously  
Phase 3: Human corrects failures → more data
Phase 4: Robot mostly autonomous → human supervises edge cases
Phase 5: Full autonomy (the 80/80 target)
```

Most companies are in Phase 2-3. [[Unitree]]'s factory deployment (G1 assembling robots) is early Phase 4 for narrow tasks.

---

## Open-source movement

Low-cost teleoperation rigs are democratizing data collection:

- **ALOHA** (Stanford/Google): ~$20K bimanual teleop, open-source
- **Unitree** open-sourced G1 task datasets on [[HuggingFace]] (wipe table, prepare fruit, pack objects — 100K+ downloads)
- **Open X-Embodiment**: Google-led consortium pooling robot data across institutions

This mirrors the open-source LLM movement — shared data accelerates everyone, but companies with proprietary deployment data maintain an edge.

---

*Created 2026-02-19*

---

## Related

- [[Embodied AI]] — parent concept
- [[UnifoLM]] — trained on teleoperation data from Embodied Avatar
- [[Unitree]] — Embodied Avatar platform, open-source datasets
- [[Figure AI]] — teleoperation-based training
- [[Tesla]] — motion capture for Optimus training
- [[Sim-to-real transfer]] — complementary data source (sim vs. teleop)
- [[State estimation]] — required for accurate teleoperation recording
