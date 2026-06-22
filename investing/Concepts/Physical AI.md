---
aliases: [Physical intelligence]
---
#concept #ai

**Physical AI** — AI systems that perceive, reason about, and act in the physical world: robots, autonomous vehicles, embodied agents. [[Jensen Huang]] gave the field its banner at Computex in June 2024 — "The next wave of AI is physical AI" — AI that understands the laws of physics and can work among us. Investable read-through sits in [[Robotics]], [[Space]], and the actor notes; this note carries the field's structure.

---

## The 2024 robot-learning inflection

After decades in which robots had to be programmed in code or trained slowly by trial and error — producing narrow abilities in controlled environments — AI-powered behaviour cloning produced a step change around 2023-24 (FT visual story, Nov 20 2024):

- The [[Toyota Research Institute]] teaches robot arms complex movements within hours instead of weeks, using diffusion-based learning from human demonstrations — see [[Diffusion models (robotics)]] for the mechanism.
- [[Stanford]] / [[Google|Google DeepMind]] teams trained policies on the most dexterous tasks they could devise; all succeeded ([[Chelsea Finn]]). Earlier iterations autonomously cooked shrimp, cleaned stains, and called a lift.
- [[Russ Tedrake]] (TRI/[[MIT]]) on the moment: "The floodgates have really opened" — tech giants jumping in, start-ups springing up.

The caveat that anchors expectations: Tesla's Optimus units serving drinks at a [[Tesla]] event were teleoperated by humans — demo polish still runs ahead of autonomy. Nick Hawes (Oxford) notes deep learning unlocked generalisation across inputs, but the general-purpose rollout "still is off there in the future."

## Training stack

The pipeline roboticists converged on builds physical capability on top of the language/vision stack:

1. Language data — the robot learns what instructions mean ("pick up the blue mug") from large text corpora, as LLMs do.
2. Vision-language data — labelled images and visual question-answering ground words to scenes, connecting instruction to environment.
3. Action data — behaviour cloning (human demonstrations) supplies the how-and-where of movement; diffusion turns demonstrations into generalisable trajectories.
4. Fine-tuning — new skills absent from training data are taught task by task.

This pre-training shortcut matters because it lets robots inherit world knowledge from existing text/image troves before any physical teaching begins. Packaged into a single network that maps images and instructions straight to actions, this stack is a [[VLA model]].

## Large behaviour models

The field's bet is foundation models for the physical world — large behaviour models trained on growing databases of recorded robot actions, intended to generalise to unpredictable commercial and domestic settings the way LLMs generalise across text.

- Binding constraint: action-data scarcity (the physical analogue of LLM text exhaustion). A communal effort to generate training data is under way.
- Cross-embodiment transfer: action data need not come from the same robot type or the exact target skill — robots can effectively teach robots that look nothing like them.
- Data flywheel: Tedrake argues hardware proliferation (factory automatons to Roomba vacuums) fills the gap — more deployed robots, more recorded actions.
- [[Toyota Research Institute]] and [[Boston Dynamics]] partnered (Oct 2024) on whole-body large behaviour models for humanoids (Atlas); [[Hyundai]] later added [[Google|Google DeepMind]] Gemini Robotics integration (Jan 2026).

## Frontier directions

[[Liquid neural networks]] ([[Daniela Rus]], [[MIT]] CSAIL): dynamic-connection networks that behave more like biological brains, need fewer neurons and less compute — attractive for onboard robot hardware. In self-driving research they handle dawn/dusk transitions better by focusing on the road's middle distance and obstacles rather than roadside features. Now commercialised by [[Liquid AI]] (MIT spinout; $250M Series A led by [[AMD]], ~$2.4bn, Dec 2024).

## Capital flows

More than $11bn of robotics and drone venture deals had been done by late October 2024 — surpassing 2023's $9.72bn full-year total, short of 2022's $13.23bn ([[PitchBook]], cited by FT). The funding quantum leap had not arrived as of late 2024; the excitement had.

---

## Quick stats

| Metric | Value |
|--------|-------|
| Category | AI / robotics concept |
| Banner framing | [[Jensen Huang]], Computex Jun 2024 ("the next wave of AI") |
| Core mechanism | Behaviour cloning + [[Diffusion models (robotics)]] |
| Key labs | [[Toyota Research Institute]], [[Google]] DeepMind, [[Stanford]], [[Boston Dynamics]], [[NVIDIA]] |
| 2024 robotics+drone VC | >$11bn YTD late-Oct 2024 ([[PitchBook]]) |

---

## Related

- [[Robotics]] — sector hub (market sizes, humanoid landscape)
- [[Diffusion models (robotics)]] — the action-generation breakthrough
- [[VLA model]] — vision-language-action architecture (the training stack packaged into one network)
- [[Liquid neural networks]] — efficient continuous-time networks ([[Daniela Rus]] / [[Liquid AI]])
- [[Toyota Research Institute]] — hours-not-weeks behaviour cloning, TRI-BD behaviour models
- [[Boston Dynamics]] — hardware embodiment (Atlas, Spot)
- [[Jensen Huang]] — Computex Jun 2024 framing
- [[NVIDIA]] — platform play (Cosmos physical-AI models, [[Groot]] humanoid models)
- [[Google]] — DeepMind robotics (Parada team, Gemini Robotics)
- [[Tesla]] — Optimus (teleoperation caveat, Nov 2024)
- [[Russ Tedrake]] / [[Chelsea Finn]] / [[Daniela Rus]] — researchers
- [[Space]] — space-sector physical-intelligence link

*Expanded 2026-06-10 from FT visual story "Are the robots finally coming?" (Nov 20, 2024) — backfill.*
