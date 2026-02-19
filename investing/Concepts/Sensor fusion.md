---
aliases: [Sensor fusion, Multi-sensor fusion, Perception stack]
---
#concept #robotics #ai #autonomous

**Sensor fusion** — Combining data from multiple sensors (cameras, LiDAR, IMU, force sensors, encoders) into a unified understanding of the world. The hardware/algorithm layer that feeds [[State estimation]] and perception.

---

## Why it matters for investors

Sensor fusion decisions determine cost structure, capability ceiling, and competitive positioning. [[Tesla]]'s vision-only bet vs. [[Waymo]]'s multi-sensor approach is a $100B+ strategic divergence. In robotics, the same debate plays out: more sensors = more data but more cost and complexity.

---

## Sensor tradeoffs

| Sensor | Strengths | Weaknesses | Cost |
|--------|-----------|------------|------|
| Cameras (RGB) | Rich texture, color, cheap | No depth, lighting sensitive | $5–50 |
| Depth cameras (RGB-D) | 3D perception | Short range, sun interference | $50–500 |
| LiDAR | Precise 3D, works in dark | Expensive, no color | $500–10K+ |
| IMU | Orientation, acceleration | Drifts over time | $1–50 |
| Joint encoders | Exact joint positions | Only internal state | $10–100 |
| Force/torque sensors | Contact detection, grip force | Fragile, expensive | $100–2K |
| Tactile sensors | Surface texture, slip detection | Emerging, limited coverage | $50–500 |

---

## Fusion architectures

| Approach | Method | Used by |
|----------|--------|---------|
| Early fusion | Combine raw sensor data before processing | End-to-end neural nets |
| Late fusion | Process each sensor independently, merge decisions | Traditional ADAS |
| Kalman-based | Optimal statistical fusion of noisy measurements | [[Mobileye]], most robotics |
| Transformer-based | Attention across sensor modalities | [[Tesla]] FSD, BEVFormer |
| Vision-only | Cameras only, no LiDAR/radar | [[Tesla]] (controversial) |

---

## The vision-only debate

| Position | Argument | Champion |
|----------|----------|----------|
| Vision-only | Humans drive with eyes; cameras are cheap and scalable | [[Tesla]] |
| Multi-sensor | Redundancy saves lives; LiDAR provides ground truth depth | [[Waymo]], [[Mobileye]] |
| Pragmatic | Start multi-sensor, remove as AI improves | Most robotics companies |

For humanoid robots, the debate is less polarized — most use cameras + IMU + joint encoders + force sensors. The question is whether to add LiDAR/depth cameras for navigation and whether tactile sensors are worth the cost for manipulation.

---

## Cost architecture implications

Sensor choice directly impacts [[Unitree Cost Architecture]]-style analysis:

- [[Unitree]] G1: cameras + IMU + joint encoders → keeps BOM under $16K
- [[Boston Dynamics]] Atlas: LiDAR + depth + force/torque → premium price
- [[Waymo]] Gen 6: 42% fewer sensors → sub-$20K per Driver unit (cost curve bending)

Fewer sensors at equivalent capability = cost moat. But premature sensor removal = safety risk.

---

*Created 2026-02-19*

---

## Related

- [[State estimation]] — primary consumer of fused sensor data
- [[Embodied AI]] — parent framework
- [[Unitree Cost Architecture]] — sensor choice drives BOM
- [[Tesla]] — vision-only pioneer
- [[Waymo]] — multi-sensor approach
- [[Mobileye]] — EyeQ chip processes fused sensor data
- [[NVIDIA]] — sensor processing compute (Drive, Jetson)
- [[Autonomous vehicles]] — parallel domain
