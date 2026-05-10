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

## Architectural divergence: Colossus 1 vs Colossus 2 (May 2026)

The May 2026 [[Anthropic]] lease made explicit a split that had been growing throughout the buildout: Colossus 1 (Memphis, original buildout) and Colossus 2 (MACROHARDRR, Tennessee + Mississippi expansion) are now operationally distinct facilities with different hardware profiles and different commercial purposes.

| Dimension | Colossus 1 (Memphis) | Colossus 2 (MACROHARDRR) |
|---|---|---|
| Hardware profile | Heterogeneous: ~150K H100, ~50K H200, ~20K GB200 (Mirae estimates) | Homogeneous: 100% [[Blackwell]] (GB200/GB300 generation) |
| Total GPUs | 220,000+ | Expanding; targeting balance of 2 GW combined goal |
| Power | ~300 MW | ~1.2 GW per facility per [[Ratepayer Protection Pledge]] |
| Operational use | Inference (leased to [[Anthropic]] May 2026) | Training (retained for xAI internal use) |
| Suitability | High — heterogeneous mix is fine for inference (no synchronous collective requirement) | Optimized — homogeneous Blackwell for synchronous training without straggler penalty |
| Counterparty | Single-tenant lease (Anthropic) | xAI internal |
| Revenue model | ~$5-6B/yr at ~$2.60/GPU-hr blended (Mirae); New Street Research lower estimate $3-4B | n/a |

The reframing matters because the original [[xAI]] thesis treated Colossus as one expanding training cluster. The actual operational split — heterogeneous half to inference rental, homogeneous half retained for training — is a sharper read of how the capacity is actually being used as of May 2026.

---

## The MFU problem on Colossus 1

[[The Information]] reported xAI's Model FLOPs Utilization (MFU) on the full Colossus fleet sits around 11% during training — far below [[Meta]] (~43%) and [[Google]] (~46%), which sit in the 35-45% industry-norm band. The disclosure puts a number on what observers had been inferring from xAI's slower model-cadence relative to its raw GPU count.

Two technical drivers cited by Zeeshan Patel (former xAI multimodal pre-training lead) and corroborated by ML-systems literature:

1. Straggler effect on heterogeneous hardware. In synchronous distributed training, every step gates on the slowest GPU finishing its forward/backward pass. Mixing H100 / H200 / GB200 in one fabric means the GB200s sit idle waiting on Hopper. Even one node with a stack-related stall freezes the entire cluster step. (See [[Distributed training scaling bottlenecks]] / [[Inference economics#Heterogeneous cluster asymmetry|Inference economics — heterogeneous cluster asymmetry]].)
2. NCCL ring topology latency at >100K GPU scale. [[NVIDIA]]'s Collective Communications Library (NCCL) was optimized for ring topologies that work well at 1K-10K GPUs. Past 100K, ring traversal latency dominates — GPUs idle waiting for data to traverse the network fabric. [[Google]] sidestepped this with custom topology (OCS / Apollo / Palomar). xAI has not yet built equivalent topology infrastructure.
3. Blackwell power smoothing. [[NVIDIA]] documents power smoothing as a hardware feature on GB200/GB300 specifically because Blackwell draws power so aggressively that uneven workloads can damage chips at the silicon level. Software stacks optimized for Hopper do not understand the new power profile, and Patel reports observed cases of GB200s being physically destroyed by xAI's Hopper-era stack imposing irregular loads.

[[Lambda Labs]] flagged a useful distinction in the public discussion: *fleet utilization* (how many GPUs are running at all) and *MFU* (how much theoretical compute each running GPU is actually capturing) are different metrics. The 11% figure refers to MFU, not fleet utilization — it does not mean 89% of Colossus GPUs are off, it means each running GPU is realizing only 11% of its theoretical FLOPs.

The strategic consequence Mirae Asset draws: xAI judged Colossus 1 was not efficient enough for frontier training and moved its own workloads to Colossus 2. Colossus 1 was then leased in its entirety to [[Anthropic]], whose inference workloads neutralize the heterogeneous-cluster penalty. See [[Training-to-inference cluster rotation]] for the full framework.

---

## Anthropic single-tenant lease (May 6, 2026)

On May 6, 2026, [[Anthropic]] signed a single-tenant lease for the entirety of Colossus 1 — all 220,000+ GPUs and 300 MW. The asset comes online inside May 2026, making it Anthropic's first major *deliverable* compute add of 2026 (vs the larger AWS / Google Cloud / Google-Broadcom commitments that come online over 2026-2027).

| Term | Value |
|---|---|
| Counterparty | [[Anthropic]] (single-tenant) |
| Lessor | xAI / SpaceX (via [[SpaceX xAI merger|consolidated SpaceXAI subsidiary]]) |
| Capacity | 220,000+ GPUs, ~300 MW |
| Use case | [[Claude]] inference (training is on retained Colossus 2 capacity) |
| Revenue (Mirae estimate) | $5-6B annual at ~$2.60/GPU-hr weighted blended rate |
| Revenue (New Street Research per Fortune) | $3-4B annual |
| Anthropic conversion target | ~$5B inference spend → ~$15B ARR via Claude inference |
| Orbital optionality | [[Anthropic]] also expressed interest in partnering on orbital data center capacity (Tom's Hardware report) |

The lease economics work asymmetrically for both sides. For xAI, the $5-6B revenue (if Mirae's number is right) almost exactly offsets the company's Q1 2026 annualized net loss of ~$6B — pulling combined economics close to break-even and reframing the SpaceXAI IPO narrative from "AGI cash incinerator" to "infrastructure tollgate." See [[SpaceX IPO 2026#Synthesis]] for IPO-defense implications. The $2.60/GPU-hr blended rate looks rich vs published [[CoreWeave]] / [[Lambda Labs]] H100 comps (~$1.80-$2.20/hr) — the premium is partly the single-tenant + immediate-availability + Blackwell-share factor and partly the bargaining position of an Anthropic that has hard-deliverable capacity scarcity.

For Anthropic, the lease addresses the binding constraint identified in [[Anthropic vs OpenAI compute race]] — the gap between *committed* capacity ([[AWS]] 5GW, [[Google Cloud]] 5GW, both multi-year build) and *deliverable* capacity (essentially zero before May 2026). 0.3 GW online this month is a small fraction of the multi-gigawatt commitments but is the only piece live before 2027. The Claude product had already shown reliability strain in [[Anthropic hyperscaler financing surge April 2026|April 2026]] disclosures; Mirae's framing is that this is the inflection where reliability stops being a constraint on Anthropic's revenue conversion.

The post-lease product changes — Claude Code 5-hour rate limits doubled across paid tiers, peak-hours limit reduction removed for Pro/Max, API rate limits raised "considerably" for Opus models — are the visible product-side evidence the capacity is real and being switched on. See [[Claude Code]] and [[Claude]].

The irony angle is unavoidable but is in the public record. [[Elon Musk]] is the plaintiff in *Musk v. OpenAI* (trial Apr 2026) and a public critic of [[Anthropic]] ("evil"); [[Dario Amodei]] founded Anthropic specifically to counterweight what he saw as misaligned incentives at the labs Musk was funding. The lease arrangement makes Anthropic the largest single customer of Musk's compute infrastructure within weeks of the trial. Musk's public framing: *"No one set off my evil detector"* (per Tom's Hardware reporting). See [[SpaceX xAI merger]] and [[Musk vs Altman lawsuit]] for the longer arc.

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
- [[Anthropic]] — Colossus 1 single-tenant lessee (May 6, 2026)
- [[NVIDIA]] — GPU supplier (H100, H200, GB200/Blackwell)
- [[Blackwell]] — GB200 architecture (Colossus 2 base, partial Colossus 1)
- [[H100]] — Hopper-generation GPUs (majority of Colossus 1 mix)
- [[TVA]] — grid power source
- [[Megapack]] — battery banks for load balancing
- [[Power constraints]] — context (2GW target, BYOP strategy)
- [[Grok]] — product trained on Colossus 2
- [[Claude]] — product served via Colossus 1 inference (post May 2026 lease)
- [[Igor Babuschkin]] — built Colossus, led Grok dev (departed Aug 2025)
- [[Elon Musk]] — controller
- [[Sovereign AI stack]] — Deepwater framework citing Colossus as energy-execution proof
- [[Ratepayer Protection Pledge]] — Mar 4 2026 White House commitments
- [[Gwynne Shotwell]] — SpaceX rep at pledge signing
- [[Memphis]] — host city
- [[Tesla Energy]] — sibling energy business (Megapack supply chain)
- [[Training-to-inference cluster rotation]] — concept framing for Colossus 1 lease
- [[Inference economics]] — heterogeneous-cluster asymmetry context
- [[Anthropic vs OpenAI compute race]] — May 2026 lease as deliverable-capacity datapoint
- [[Anthropic hyperscaler financing surge April 2026]] — May 6 lease as capstone of April surge
- [[SpaceX IPO 2026]] — lease as IPO-defense ("incinerator → tollgate" reframing)
- [[CoreWeave]] — neocloud rate comparable for the $2.60/GPU-hr lease pricing
- [[Lambda Labs]] — fleet utilization vs MFU distinction on the 11% xAI figure
- [[Space data centers]] — orbital optionality embedded in the Anthropic lease

*Created 2026-04-09 as hub note for a facility previously referenced only inside xAI.md. Expanded 2026-05-10 with Colossus 1 / Colossus 2 architectural split, MFU disclosure context, and May 6 Anthropic lease.*
