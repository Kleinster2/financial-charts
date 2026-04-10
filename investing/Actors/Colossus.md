---
aliases: [Colossus 1, Colossus Memphis, MACROHARDRR, Colossus 2]
tags: [actor, datacenter, ai-infrastructure, xai, memphis]
---
#actor #datacenter #ai-infrastructure #xai

**Colossus** — [[xAI]]'s flagship AI training data center in Memphis, Tennessee. Built 0 → 100K [[NVIDIA]] H100 GPUs in 122 days. One of the highest single-site AI compute capacities in the United States. Powered primarily by ~35 on-site gas turbines installed under permitting workarounds — later forced to adapt after the EPA closed the non-road engine loophole in January 2026. Expansion underway into Colossus 2 (branded "MACROHARDRR") in Tennessee plus a third building in Mississippi, targeting 2 GW combined capacity. Seen by [[Deepwater Asset Management]] as the clearest proof that [[SpaceX]]'s sovereign AI stack has a credible energy-execution track record.

---

## Quick stats

| Detail | Value |
|--------|-------|
| Operator | [[xAI]] (now [[SpaceX]] subsidiary post Feb 2026 merger) |
| Location | Memphis, TN + Tennessee + Mississippi (expansion) |
| Initial buildout | 100,000 [[NVIDIA]] H100 GPUs |
| Build time | 122 days (0 → 100K) |
| Current GPU base | H100 + [[Blackwell]] (scaling) |
| Target capacity | 2 GW (combined Memphis + MACROHARDRR + MS) |
| Power source | ~35 on-site gas turbines + [[TVA]] grid + [[Megapack]] battery banks |
| Key commit | 1.2 GW primary power per data center ([[Ratepayer Protection Pledge]], Mar 4 2026) |
| Branding | "Macrohard" painted on roof |
| Construction lead | [[Igor Babuschkin]] (departed Aug 2025) |

---

## Build-speed playbook

Colossus became a case study in how fast a frontier-model data center can actually be stood up when regulatory and engineering constraints are pushed to the edge:

- Land lease structured as "temporary" to bypass standard data-center permitting timelines (similar to carnival/event permits).
- 35 gas turbines installed without permits — classified as "non-road engines" under a loophole later closed by the EPA in January 2026.
- 80+ mobile generators for power balancing, with Tesla [[Megapack]] battery banks for load switching (generators too slow to react to millisecond-scale GPU demand shifts).
- Seamless failover to generators when municipal load on TVA is high — without interrupting active training runs.
- Same-day training runs on newly installed GPU racks, versus weeks at other hyperscalers.
- "The Cybertruck bet": engineer Tyler bet Elon he could get a training run up on fresh GPUs within 24 hours of delivery. He did. He got the Cybertruck.

The [[NAACP]] and environmental groups appealed the turbine installations. The EPA closed the non-road engine loophole in Jan 2026, meaning new data centers cannot replicate this approach. Daily fines up to $10,000 per violation apply under the new permit regime. Colossus is the last xAI facility that was stood up this way.

---

## Expansion

### Colossus 2 / MACROHARDRR (Tennessee)
A third building was purchased and branded "MACROHARDRR." Targeting contribution toward the 2 GW total. Located for direct [[TVA]] power access, part of xAI's BYOP (bring your own power) strategy. See [[Power constraints]].

### Mississippi expansion
Third building across the state line from Memphis, $20B+ investment per Gov. Tate Reeves. Brings combined capacity to ~2 GW.

Musk's framing (2025): "More AI compute than everyone else combined within five years" — with Colossus cluster as the anchor of that claim.

---

## Ratepayer Protection Pledge commitments (Mar 4, 2026)

[[Gwynne Shotwell]] (SpaceX) represented xAI at the White House [[Ratepayer Protection Pledge]] signing and committed to:

- 1.2 GW as primary power source per data center (applies to Colossus and every additional xAI facility).
- Expansion of the existing Megapack installation — already the largest global Megapack deployment.
- Grid backup sufficient for the city of Memphis plus the town of South Haven, MS.
- New substations and electrical infrastructure being built.
- ~4.7 billion gallons per year of water recycling, protecting the Memphis aquifer.
- Thousands of workers from Memphis area (TN + MS).
- Orbital data center design as a long-term pressure release valve — space compute would free terrestrial plants back to community use.

Shotwell: "I've been in the space industry for nearly 40 years... I have never seen things move more quickly than under your administration."

---

## Role in the sovereign AI stack

[[Deepwater Asset Management]] ([[Gene Munster]] + [[Doug Clinton]]) cited Colossus specifically as the evidence that SpaceX's sovereign AI stack has the energy-execution track record to be taken seriously. Their read: the Colossus gas-turbine improvisation, combined with Tesla's broader energy business, means the combined Musk ecosystem understands energy delivery for AI better than any other hyperscaler. Energy is the first bottleneck on new data centers (3+ year wait for turbines via conventional channels), and Colossus is the proof of concept that the sovereign AI stack can fast-track around it when it has to. See [[Sovereign AI stack]] for the broader framework.

The counterpoint: the build-speed playbook relied on permitting workarounds that are now closed. Colossus 2 and the Mississippi expansion will need to be built under standard rules, which removes the biggest differentiator on the energy layer. Whether the execution-speed advantage survives the regulatory tightening is the open question.

---

## Related

- [[xAI]] — operator
- [[SpaceX]] — parent (post Feb 2026 merger)
- [[NVIDIA]] — GPU supplier (H100, Blackwell)
- [[TVA]] — grid power source
- [[Megapack]] — battery banks for load balancing
- [[Power constraints]] — context (2GW target, BYOP strategy)
- [[Grok]] — product trained on Colossus
- [[Igor Babuschkin]] — built Colossus, led Grok dev (departed Aug 2025)
- [[Elon Musk]] — controller
- [[Sovereign AI stack]] — Deepwater framework citing Colossus as energy-execution proof
- [[Ratepayer Protection Pledge]] — Mar 4 2026 White House commitments
- [[Gwynne Shotwell]] — SpaceX rep at pledge signing
- [[Memphis]] — host city
- [[Tesla Energy]] — sibling energy business (Megapack supply chain)

*Created 2026-04-09 as hub note for a facility previously referenced only inside xAI.md. No new claims — consolidation of existing vault content plus Deepwater framing.*
