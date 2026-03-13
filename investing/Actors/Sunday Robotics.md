---
tags: [actor, robotics, ai, private, usa]
aliases: [Sunday, Sunday Inc, Memo]
---

**Sunday Robotics** — Mountain View startup building Memo, an autonomous wheeled household robot trained via patented data-capture gloves. Hit unicorn status ($1.15B) with $165M Series B led by [[Coatue]] (Mar 2026).

---

## Synopsis

Sunday Robotics is the most aggressively funded bet on household robotics since [[Figure AI]] raised for industrial humanoids. Founded in 2023 by two Stanford PhD dropouts — CEO Tony Zhao (creator of the ALOHA imitation-learning system) and CTO Cheng Chi (inventor of Diffusion Policy) — the company emerged from stealth in Nov 2025 with $35M from [[Benchmark]] and Conviction, then closed a $165M Series B at $1.15B valuation 4 months later (Mar 12, 2026), led by [[Coatue]] with [[Bain Capital]] Ventures, [[Fidelity]] Management & Research, [[Tiger Global]], and Xtal Ventures.

The core insight is the data flywheel, not the robot. Sunday's patented Skill Capture Glove (~$200 per unit vs. ~$20,000 for a conventional teleoperation rig) lets non-engineers record household routines in real homes. 2,000+ gloves deployed across 500+ homes have generated ~10M real-world episodes as of the stealth launch, scaling to tens of millions by Mar 2026 with a 5x target by year-end. The foundation model (ACT-1) trains on this human-motion data without needing robot-generated data at all — a fundamentally different approach from [[1X Technologies]]' teleoperation model or [[Tesla Optimus]]' simulation-first path.

The product (Memo) is a wheeled, dual-gripper robot — not bipedal, not five-fingered. That's a deliberate scope cut: wheels mean no stair-climbing but far simpler balance and locomotion, custom grippers mean millimeter precision with fewer failure modes. Current build cost is ~$20,000/unit (hand-built); target retail is under $10,000 at scale. First 50 units ship free to "Founding Family Beta" households late 2026, consumer launch targeted for Thanksgiving 2026. The risk is that the home environment is the hardest deployment context in robotics — every kitchen is different — and no company has cracked it at consumer price points. Jibo, Anki, and Mayfield Robotics all died trying.

---

## Quick stats

| Field | Value |
|---|---|
| Full name | Sunday Inc. (d/b/a Sunday Robotics) |
| Founded | 2023 |
| HQ | Mountain View, CA |
| CEO | Tony Zhao |
| CTO | Cheng Chi |
| Headcount | ~70+ (Mar 2026), up from 25 at stealth launch |
| Product | Memo (autonomous household robot) |
| Total raised | $200M |
| Valuation | $1.15B post-money (Series B, Mar 2026) |
| Website | sunday.ai |

---

## Funding rounds

| Round | Date | Amount | Valuation | Lead | Other investors |
|---|---|---|---|---|---|
| Seed | ~Early 2023 | Undisclosed | Undisclosed | Undisclosed | — |
| Series A | Nov 2025 | $35M | Undisclosed | [[Benchmark]], Conviction | — |
| Series B | Mar 12, 2026 | $165M | $1.15B post | [[Coatue]] | [[Bain Capital]] Ventures, [[Fidelity]] Management & Research, [[Tiger Global]], [[Benchmark]] (existing), Conviction (existing), Xtal Ventures |

Round was oversubscribed. Thomas Laffont ([[Coatue]]) joined the board.

---

## Product: Memo

| Spec | Detail |
|---|---|
| Height | 1.7m (5'7") |
| Weight | 170 lbs |
| Runtime | 4 hours |
| Locomotion | Wheeled base (cannot climb stairs) |
| Manipulation | Custom dual-gripper, millimeter-level precision |
| Exterior | Soft-touch cladding (rigid + elastic polymers) |
| Speed | 50% of human walking pace |
| Design | White limbs, cartoonish face, plastic "ballcap" |

Demonstrated capabilities: 33-step table-to-dishwasher cycle, loading dishwashers, folding laundry, making espresso, handling delicate items (wine glasses, baby plates).

Design philosophy: Wheels over legs, grippers over hands. Fewer degrees of freedom = fewer failure modes. The tradeoff is stair-climbing and dexterity for fine manipulation — Sunday bets that 80%+ of household tasks don't need either.

---

## Technology

### Skill Capture Glove (patented)
- ~$200 per unit (vs. ~$20,000 for conventional teleoperation rigs)
- Records human movement and force data during natural household routines
- 2,000+ gloves deployed to "Memory Developers" across 500+ homes
- No robot needed for data collection — humans just do chores while wearing gloves
- This is the moat: it turns every home into a training data source

### Data scale
- ~10M real-world household episodes at stealth launch (Nov 2025)
- Tens of millions by Mar 2026
- Plan to 5x in-the-wild data collection by end of 2026

### Foundation model: ACT-1
- Trained on "zero robot data" — maps human dexterity via "Skill Transform" software
- Based on Stanford research: ALOHA (imitation learning), ACT (Action Chunking with Transformers), Diffusion Policy, UMI (Universal Manipulation Interface)
- Full-stack: hardware, manufacturing, and software all in-house

---

## People

### Tony Zhao — Co-founder & CEO
- B.S. EECS, UC Berkeley (2021) — worked with Sergey Levine and Dan Klein
- Stanford CS PhD (advised by Chelsea Finn) — dropped out 2024
- Stanford Robotics Fellowship 2022-23
- Previously [[Google DeepMind]] and [[Tesla]] Autopilot
- Created ALOHA (open-source low-cost bimanual manipulation)
- Co-authored ACT (Action Chunking with Transformers), Mobile ALOHA, ALOHA 2

### Cheng Chi — Co-founder & CTO
- B.S. CS, University of Michigan
- PhD CS, Columbia University (advised by Shuran Song; transferred to Stanford)
- Previously at Nuro (autonomous vehicles — localization/mapping)
- Invented Diffusion Policy (RSS 2023)
- Co-invented UMI (Universal Manipulation Interface) — Best Systems Paper Finalist, RSS 2024
- Two Best Paper Awards, two Best Systems Paper Finalist honors
- Architects data collection infrastructure and ML pipelines

Team includes alumni from Stanford, [[Tesla]], [[Google DeepMind]], [[Waymo]], [[Meta]], [[OpenAI]], [[Apple]], [[Neuralink]].

---

## Competitive landscape

| Company | Form factor | Approach | Home price target | Key backer |
|---|---|---|---|---|
| Sunday (Memo) | Wheeled, dual-gripper | Glove data capture → imitation learning | <$10,000 | [[Coatue]], [[Benchmark]] |
| [[1X Technologies]] (NEO) | Bipedal humanoid (66 lbs) | Teleoperation training, "Redwood AI" model | ~$20,000 pre-order | [[OpenAI]] Startup Fund |
| [[Figure AI]] | Bipedal humanoid | Industrial-first, general purpose | N/A (industrial) | [[Microsoft]], [[OpenAI]] ($675M) |
| [[Tesla Optimus]] | Bipedal humanoid | Simulation + factory deployment first | TBD | [[Tesla]] internal |

Sunday's bet: you don't need legs or five fingers for household chores, and real-world data from gloves beats simulation and teleoperation. The others are building general-purpose humanoids; Sunday is building a purpose-built appliance.

---

## Timeline

- 2023 — Founded. Operated in stealth with seed funding.
- Nov 19, 2025 — Beta applications open.
- Nov 20, 2025 — Emerges from stealth with $35M (Series A) from [[Benchmark]] and Conviction. 25 employees. 1,000-person waitlist. 10,000+ job applications in 3 months.
- Mar 12, 2026 — $165M Series B at $1.15B, led by [[Coatue]]. Team at 70+.
- Late 2026 (target) — "Founding Family Beta": 50 individually numbered units shipped free to selected households.
- Thanksgiving 2026 (target) — Consumer launch.

---

## Risks

- Home environment is the graveyard of consumer robotics. Jibo ($73M raised, shut down), [[Anki]] ($200M raised, shut down), Mayfield Robotics ([[Bosch]]-backed, shut down). Unstructured environments with infinite variation have defeated every prior attempt at consumer price points.
- Wheeled platform limits use cases. No stairs, limited terrain. If 20%+ of household tasks require stair access, the value proposition shrinks.
- $20,000 → <$10,000 cost reduction is not guaranteed. 50%+ manufacturing cost reduction requires scale that assumes strong demand — circular logic.
- Data moat assumes glove fidelity translates. Human hand motion captured via gloves must translate to a non-anthropomorphic dual-gripper. The "Skill Transform" step is the least publicly documented piece of the stack.
- Consumer hardware margins are brutal. Even at $10,000 retail, margins are thin if the robot needs ongoing software updates, support, and part replacement.

---

## Core thesis

Sunday's bet is that the data problem — not the hardware problem — is what's held household robotics back. If the Skill Capture Glove creates a genuine data flywheel (cheap collection → better model → more capable robot → more users → more data), then the wheeled form factor and sub-$10K price point could crack the market that humanoid makers are overbuilding for. The $1.15B valuation prices in execution on the Thanksgiving 2026 launch. Miss that, and the narrative shifts fast.

---

## Related

- [[1X Technologies]] — bipedal humanoid competitor, [[OpenAI]]-backed
- [[Figure AI]] — humanoid competitor, industrial-first
- [[Tesla Optimus]] — humanoid competitor, simulation-first
- [[Coatue]] — Series B lead, Thomas Laffont on board
- [[Benchmark]] — Series A investor
- [[Tiger Global]] — Series B participant
- [[Bain Capital]] — Series B participant (Bain Capital Ventures)
- [[Fidelity]] — Series B participant
