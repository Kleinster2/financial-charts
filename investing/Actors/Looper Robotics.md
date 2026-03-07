---
aliases: [Looper, LooperRobotics]
---
#actor #china #robotics #ai #private

**Looper Robotics** — the Physical AI brand of [[DeepMirror]], a spatial intelligence company founded in 2019. Based in [[Hong Kong]]. Builds perception hardware and navigation software for robots — positioning as a Tier-1 supplier of robot perception infrastructure rather than building robots itself. Technical partner of [[Unitree]].

---

## Synopsis

Looper Robotics is [[DeepMirror]]'s go-to-market identity for the physical AI stack — cameras, SLAM software, and navigation libraries that turn commodity robot hardware into autonomous workers. The bet is that robot perception becomes a horizontal platform layer, analogous to how [[Qualcomm]] supplies smartphone brains without making phones. Their flagship Insight9 camera ($257 early adopter on Kickstarter) bundles a 188° triple-camera array, onboard VSLAM, and a 10 TOPS NPU into a ruggedized package rated for 24g vibration — specs that target industrial deployment, not hobbyists.

The company's competitive moat, if one emerges, lies in the full-stack integration: Insight9 hardware + TinyNav neural navigation (3,000 lines vs. 140,000+ in traditional SLAM stacks) + RoboSpatial 3D toolchain + OpenClaw task planning. Two robot products (NOMAD, RANGER) built on [[Unitree]] platforms with this stack pre-integrated are slated for mass production Q2 2026. The parent company [[DeepMirror]] has raised tens of millions in an A-round led by [[IDG Capital]] and the Shanghai AI Industry Equity Investment Fund, with co-investors including [[OPPO]], [[Eight Roads Ventures]], and [[Fosun RZ Capital]].

The risk is classic platform-layer risk: the robot OEMs (including [[Unitree]]) could vertically integrate their own perception stacks, and the Kickstarter launch strategy signals capital constraints. Whether "democratizing robot perception" becomes a real business or stays a pitch deck concept depends on whether the Insight9 earns design wins beyond the [[Unitree]] ecosystem.

---

## Quick stats

| Metric | Value |
|--------|-------|
| HQ | Wan Chai, [[Hong Kong]] |
| Parent | [[DeepMirror]] (DeepMirror Hong Kong Limited) |
| DeepMirror founded | 2019 |
| Co-founder & CEO | Harry Hu |
| Co-founder | [[Qifeng Chen]] (HKUST professor, Stanford PhD 2017) |
| Other co-founders | Zichao Qi, Jiabei Lei, Yizi Wu |
| DeepMirror R&D base | [[Guangzhou]], [[China]] |
| Status | Private |
| Funding (DeepMirror) | A-round: tens of millions of dollars |
| A-round leads | Shanghai AI Industry Equity Investment Fund, [[IDG Capital]] |
| A-round co-investors | 37Games, [[OPPO]], [[Eight Roads Ventures]], BV Capital, Shenzhen [[Xinwangda Electronic]], [[Fosun RZ Capital]] |
| Key partnership | [[Unitree]] (technical partner — integrated SLAM/perception) |

---

## Funding rounds (DeepMirror)

| Round | Date | Amount | Lead | Co-investors |
|-------|------|--------|------|-------------|
| Pre-A | ~2020 | Undisclosed | [[OPPO]], [[Eight Roads Ventures]] | BV Capital, [[Fosun RZ Capital]] |
| A | ~2022 | Tens of millions USD | Shanghai AI Industry Equity Investment Fund, [[IDG Capital]] | 37Games, [[OPPO]], [[Eight Roads Ventures]], BV Capital, Shenzhen [[Xinwangda Electronic]], [[Fosun RZ Capital]] |

*Looper Robotics is a brand/division of DeepMirror, not a separately funded entity. All funding flows through DeepMirror.*

### Cap table

No breakdown disclosed. Known investors: Shanghai AI Industry Equity Investment Fund, [[IDG Capital]], 37Games, [[OPPO]], [[Eight Roads Ventures]], BV Capital, [[Xinwangda Electronic]], [[Fosun RZ Capital]]. Founders (Harry Hu, [[Qifeng Chen]], Zichao Qi, Jiabei Lei, Yizi Wu) hold undisclosed stakes.

---

## Products

| Product | Type | Status | Details |
|---------|------|--------|---------|
| Insight9 | Spatial AI camera | Pre-launch (Kickstarter) | 188° FOV, onboard VSLAM, 10 TOPS NPU, 24g vibration, CNC aluminum, -20°C to 85°C |
| NOMAD | Robot (on [[Unitree]] platform) | Mass production Q2 2026 | Pre-integrated with full Looper perception/nav stack |
| RANGER | Robot (on [[Unitree]] platform) | Mass production Q2 2026 | Pre-integrated with full Looper perception/nav stack |
| TinyNav | Neural navigation library | Available | 3,000-line architecture vs. 140,000+ in traditional SLAM |
| RoboSpatial | 3D spatial toolchain | Available | Define POIs and task logic in real-world 3D views |

### Insight9 specs

- Vertical triple-camera array (ultra-wide 188° RGB, 157.2° high-dynamic)
- Octa-core ARM processor + 10 TOPS NPU for edge computing
- Built-in VSLAM (Visual Simultaneous Localization and Mapping)
- CNC-machined aluminum alloy, rated for 24g vibration (industry standard: 8g)
- Operating range: -20°C to 85°C
- Native ROS/ROS2 integration, built-in Linux OS
- Kickstarter early adopter price: $257

---

## OpenClaw integration (Mar 2026)

DeepMirror integrated the open-source [[OpenClaw]] framework into its Physical AI stack (announced 5 Mar 2026). The architecture: OpenClaw generates structured task plans from natural language → DeepMirror maps those into executable "skills" tied to perception and control → actions can be monitored, retried, or aborted. The company positions this as a "Physical Space Skills Hub" — a marketplace for reusable, versioned robotic skill modules deployable across platforms.

Target verticals: logistics (autonomous inventory audits), energy (first-response maintenance in hazardous facilities), public venues (airports, hospitals — service delivery + emergency response).

---

## Related

- [[Unitree]] — technical partner, robot platform provider
- [[DeepMirror]] — parent company (spatial intelligence, digital twins)
- [[Qifeng Chen]] — co-founder, HKUST faculty
- [[IDG Capital]] — A-round lead investor
- [[OPPO]] — investor, potential hardware channel
- [[Eight Roads Ventures]] — investor (Fidelity's VC arm)
