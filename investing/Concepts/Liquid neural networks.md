---
aliases: [Liquid neural network, Liquid network, Liquid networks, LNN, Liquid time-constant network, Liquid time-constant networks, LTC, Closed-form continuous-time network, CfC]
---
#concept #ai #robotics

**Liquid neural networks** — continuous-time neural networks whose neuron time-constants adapt to the input even after training, so the network keeps changing its internal dynamics while it runs rather than freezing its weights at deployment. Developed at [[MIT]] CSAIL by [[Ramin Hasani]], Mathias Lechner, Alexander Amini, and [[Daniela Rus]], and inspired by the 302-neuron nervous system of the C. elegans roundworm.

---

## How they differ from standard networks

A conventional neural network fixes its weights once training ends. A liquid network instead models each neuron as a continuous-time differential equation whose time-constant — how fast the neuron reacts — depends on the incoming signal. The dynamics stay "liquid" at inference, which is what lets the network adapt to conditions it did not see in training. The original formulation is the liquid time-constant network (LTC, 2020-21); the later closed-form continuous-time variant (CfC, 2022) solves the dynamics analytically instead of calling a numerical ODE solver, removing most of the runtime cost.

## What the property buys

- Tiny networks: a 19-neuron liquid network has steered a car — orders of magnitude fewer units than a comparable deep net, at a fraction of the compute.
- Interpretability and robustness: the compact, causal attention can be inspected and degrades gracefully under distribution shift. In self-driving research the network keeps its attention on the road's middle distance and obstacles rather than fixating on roadside features, and holds up better through dawn and dusk transitions where conventional models drift (FT visual story, Nov 2024).
- Edge deployment: the small footprint suits onboard robot, vehicle, and device hardware where GPU clusters are not available — directly relevant to the [[Physical AI]] data-and-compute bottleneck.

## Commercialisation — Liquid AI

The approach was spun out of MIT into [[Liquid AI]] (2023; [[Ramin Hasani]] CEO). In December 2024 the company raised a $250M Series A led by [[AMD]], at roughly a $2.4bn valuation ([[Bloomberg]]). Its product line is the Liquid Foundation Models (LFMs, first released September 2024 in 1B, 3B, and 40B mixture-of-experts sizes) — general-purpose models built on the liquid architecture rather than the standard [[Transformer|transformer]], designed to run multimodally on phones, laptops, vehicles, and other edge devices.

## Why it matters

Liquid networks are an architectural counter-bet to the transformer-on-GPU paradigm that drives the [[AI capex arms race]]. The strategic tell is the lead investor: [[AMD]], a chip vendor, backing an architecture whose selling point is doing more with far less compute at the edge. If efficient non-transformer models scale, they pressure the compute-maximalist thesis and shift value toward edge silicon and on-device inference; if they do not, they stay a niche for power- and latency-constrained settings. Adoption against entrenched transformers is still early — reported 2025 revenue is small (~$13.2M, secondary estimate).

---

## Synthesis

Liquid networks are the contrarian architecture bet in AI: where the transformer thesis says scale up compute, the liquid thesis says shrink it — continuous-time dynamics that keep adapting at inference, few enough neurons to run on a phone or a robot's onboard chip. For robotics that attacks the [[Physical AI]] bottleneck directly, since GPU clusters are not available at the edge. The signal worth watching is who funds it: [[AMD]] leading [[Liquid AI]]'s round is a chipmaker hedging the possibility that the next efficient model does not need a datacentre full of GPUs. The bet is unproven against entrenched transformers — but if it lands, it reprices both the compute-maximalist [[AI capex arms race]] and the edge-silicon names.

*No chart available — this is a technology-architecture concept with no standalone tradeable instrument; the nearest public proxy is lead investor [[AMD]], whose note carries its own charts.*

---

## Related
- [[Physical AI]] — edge compute for onboard robot inference
- [[Daniela Rus]] — co-creator, MIT CSAIL director
- [[Liquid AI]] — MIT spinout commercialising the architecture
- [[AMD]] — lead investor (Dec 2024 Series A)
- [[MIT]] — origin (CSAIL)
- [[Embodied AI]] — physical-world AI context

*Created 2026-06-21 from a cold-research pass during the cross-vault scope decision on the FT "Are the robots finally coming?" ingestion. Sources: MIT News (2021); TechCrunch (Dec 2023); Bloomberg (Dec 2024); McKinsey (liquid foundation models); Liquid AI.*
