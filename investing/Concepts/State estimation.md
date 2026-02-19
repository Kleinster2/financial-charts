---
aliases: [State estimation, Localization, Robot proprioception]
---
#concept #robotics #ai #engineering

**State estimation** — How a robot determines where it is, how it's moving, and what's happening around it using noisy, incomplete sensor data. The foundational layer beneath all [[Embodied AI]] — if state estimation is wrong, nothing above it works.

---

## Why it matters for investors

State estimation is the unglamorous bottleneck separating controlled demos from real-world deployment. Factory floors (flat, predictable) are largely solved. Unstructured environments (homes, construction sites, outdoors) remain frontier problems. This gap maps directly to [[Wang Xingxing]]'s [[Embodied AI|80/80 benchmark]] — and determines which robotics companies can expand beyond controlled settings.

---

## What the robot needs to know

| State | Question | Sensors |
|-------|----------|---------|
| Pose | Where am I in the world? | IMU, cameras, LiDAR, GPS |
| Velocity | How fast am I moving/rotating? | IMU, encoders, optical flow |
| Joint configuration | Where are my limbs? | Joint encoders, torque sensors |
| Contact forces | What am I touching? How hard? | Force/torque sensors, current sensing |
| Object state | Where are the things I'm manipulating? | Cameras, depth sensors, tactile |
| Terrain | Is the ground flat? Slippery? Soft? | Force feedback, IMU, vision |

Humans fuse proprioception + vision + vestibular input unconsciously. Robots must compute it explicitly, in real-time, from imperfect data.

---

## Core techniques

| Method | Function | Use case |
|--------|----------|----------|
| Kalman filter (EKF/UKF) | Fuse noisy sensor readings into optimal estimate | IMU + encoders → pose estimation |
| SLAM | Simultaneous localization and mapping | Navigation in unknown spaces |
| Visual-inertial odometry (VIO) | Camera + IMU fusion for positioning | Drones, mobile robots |
| Contact estimation | Infer ground/object forces from joint torques | Legged locomotion, manipulation |
| Particle filters | Probabilistic tracking of multiple hypotheses | Object pose under occlusion |
| Factor graphs | Graph-based optimization over sensor history | High-accuracy offline/online SLAM |

---

## Why quadrupeds are a training ground

Legged robots are state estimation on hard mode — the robot must estimate contact timing, ground reaction forces, body orientation, and foot placement simultaneously while in dynamic motion. This is why [[Unitree]]'s [[Unitree Quadruped Bridge|quadruped bridge]] matters: 7 years of quadruped locomotion (2016–2023) = 7 years of refining state estimation on real hardware before building humanoids.

Wheeled robots (warehouses, delivery) have easier state estimation — continuous ground contact, simpler dynamics. Humanoids in unstructured environments have the hardest version of the problem.

---

## Solved vs. frontier

| Environment | State estimation difficulty | Status |
|-------------|---------------------------|--------|
| Factory floor (flat, mapped) | Low | Largely solved |
| Warehouse (structured, dynamic) | Medium | Commercially viable |
| Construction site | High | Active research |
| Outdoor terrain (mud, snow, slopes) | High | [[Unitree]] G1 demo at -47°C |
| Home (clutter, children, pets) | Very high | Years away |

The investment implication: companies claiming general-purpose humanoid deployment should be evaluated against this difficulty gradient. Most current demos operate at the "factory floor" level.

---

## Connection to embodied AI stack

State estimation sits at the bottom of the [[Embodied AI]] stack:

1. **State estimation** — where am I, what's around me
2. **World models** ([[UnifoLM]]-WMA) — predict what happens next
3. **Planning/policy** ([[UnifoLM]]-VLA) — decide what to do
4. **Control** — execute motor commands

Errors compound upward. A 2cm position error in state estimation becomes a failed grasp at the action layer. This is why sensor fusion quality and calibration matter more than model size for physical AI.

---

*Created 2026-02-19*

---

## Related

- [[Embodied AI]] — parent concept
- [[UnifoLM]] — Unitree's model stack (depends on state estimation)
- [[Unitree Quadruped Bridge]] — 7 years of state estimation refinement
- [[Unitree]] — volume leader in legged robots
- [[Humanoid robotics]] — hardest state estimation challenge
- [[Autonomous vehicles]] — parallel domain (SLAM, VIO, sensor fusion)
- [[Mobileye]] — ADAS state estimation → robotics via [[Mentee Robotics]]
