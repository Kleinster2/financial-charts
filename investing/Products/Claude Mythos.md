---
aliases: [Mythos, Capybara, Claude Capybara, Claude Mythos Preview]
tags: [product, ai]
parent_actor: "[[Anthropic]]"
---

# Claude Mythos

[[Anthropic]]'s next-generation [[Claude]] model, leaked on 2026-03-27 through a misconfigured content management system. Capybara is a new tier above [[Claude Opus|Opus]] — the first expansion of [[Anthropic]]'s three-tier naming hierarchy since [[Claude]] launched. [[Anthropic]] confirmed the model exists but has not announced a release date. Currently in testing with a limited group of early-access customers.

---

## Quick stats

| Metric | Value |
|--------|-------|
| Parent | [[Anthropic]] |
| Product family | [[Claude]] |
| Tier | Capybara (above Opus) |
| Codename | Mythos |
| Status | In testing with early-access customers (as of Mar 27 2026) |
| Leak date | 2026-03-27 |
| Leak vector | Misconfigured CMS — ~3,000 unpublished assets publicly searchable |
| Discovered by | Alexandre Pauwels (Cambridge), Roy Paz (LayerX Security) |

---

## Capabilities (from leaked materials)

[[Anthropic]] described the model internally as a "step change" in capability. Leaked benchmark data shows dramatic improvement over [[Claude Opus|Opus 4.6]] across three domains:

- Software coding
- Academic reasoning
- Cybersecurity (vulnerability discovery and exploitation)

An [[Anthropic]] spokesperson confirmed they are "developing a general purpose model with meaningful advances in reasoning, coding, and cybersecurity." No public benchmarks released.

---

## Cybersecurity implications

Leaked internal safety documents flagged that Mythos could significantly heighten cybersecurity risks by rapidly identifying and exploiting software vulnerabilities. The concern is acceleration of a cyber arms race — a model that finds vulnerabilities faster than defenders can patch them shifts the offense-defense balance. This extends the pattern established by [[Claude Code Security]] (Feb 2026), which found 500+ bugs undetected for decades.

## Controlled rollout and regulatory response (Apr 2026)

Rather than release Mythos broadly, [[Anthropic]] put the model behind [[Project Glasswing]], a controlled defensive-cyber program. Reuters reported on April 7 that launch partners included [[Amazon]], [[Microsoft]], [[Apple]], [[CrowdStrike]], [[Palo Alto Networks]], [[Google]], and [[NVIDIA]], with roughly 40 additional organizations responsible for critical software infrastructure also receiving access. Anthropic paired the rollout with up to $100M in usage credits and $4M in donations to open-source security groups.

The more important signal was who reacted. Reuters reported on April 9 that U.S. officials briefed major bank CEOs on Mythos' cyber-risk potential. Three days later, the [[Bank of England]], [[Financial Conduct Authority]], and the [[UK National Cyber Security Centre]] were reported to be coordinating on whether Mythos-class models could expose vulnerabilities in critical financial IT systems, with UK banks, insurers, and exchanges due to be briefed within a fortnight.

That is a different category of AI release. Mythos was not treated as a consumer launch or even a normal enterprise product cycle. It was treated as a controlled capability with potential financial-stability and operational-resilience implications.

---

## Model tier: Capybara

| Tier | Model class | Positioning |
|------|-------------|-------------|
| [[Claude Haiku|Haiku]] | Smallest | Fast, cheap, simple tasks |
| [[Claude Sonnet|Sonnet]] | Mid-range | Balanced performance/cost |
| [[Claude Opus|Opus]] | Largest (current) | Maximum capability |
| Capybara | Next-gen | Step change above Opus |

Whether Capybara becomes a permanent tier or is specific to the Mythos generation is unclear from the leaked materials.

---

## Market discovery timeline

| Date | Event | Market reaction |
|------|-------|-----------------|
| 2026-03-27 | CMS misconfiguration exposes ~3,000 unpublished assets including Mythos benchmarks and safety evaluations | Cybersecurity selloff: CRWD -7%, PANW -6%, ZS -4.5%, OKTA -3%, S -3%, FTNT -3% |
| 2026-03-27 | [[Anthropic]] spokesperson confirms model exists, describes "step change" in reasoning/coding/cybersecurity | — |
| TBD | Public release | — |

---

## Competitive context

Leaked the same week [[OpenAI]] teased [[OpenAI Spud|Spud]], its next model. Both frontier labs revealing next-gen models within days of each other heading into Q2 2026.

---

## Treasury endorsement (April 2026)

[[Scott Bessent]] cited Mythos as the exemplar of the US compounding lead in AI. Speaking at the WSJ CEO Council on April 14, 2026, he told [[Paul Gigot]]: "The Anthropic mythos model was a step function change." Used to argue that learning improvements compound logarithmically ("x to the 10th to x to the 12th") and are therefore difficult for [[China]] to close — a central justification for his claim that the US remains "3 to 6 months ahead" and is on track for 70-80% of global compute share. See [[US-China AI race#Bessent on the gap (April 14, 2026)]].

This is the first senior administration source to publicly endorse Mythos as the compounding-lead exemplar — notable given the parallel [[Project Glasswing]] controlled rollout treating Mythos as a cybersecurity-risk capability.

---

## Policy-debate role — Dwarkesh × Jensen (Apr 15, 2026)

Mythos became the central exhibit in Dwarkesh Patel's export-controls exchange with [[Jensen Huang]]. Dwarkesh framed Mythos as the decisive example of AI crossing into weapon-adjacent capability — found zero-day vulnerabilities in every major operating system and browser, including one in OpenBSD after 27 years of secure-by-design engineering, so consequential [[Anthropic]] is withholding public release until defenders patch. The Dwarkesh thesis: if [[China]] had enough [[NVIDIA]] compute to train and run millions of instances of a Mythos-class model, that materially raises cyber-offensive risk to the US.

Jensen's rebuttal directly defused the Mythos framing: "Mythos was trained on fairly mundane capacity and a fairly mundane amount of it." The threshold Dwarkesh treats as dangerous is, in Jensen's read, already available to China in abundance — 60% of mainstream chip manufacturing, 50% of the world's AI researchers, ghost data centers fully powered. Jensen rejected the enriched-uranium and "Boeing selling nukes" analogies as category errors: "comparing AI to anything you just mentioned is lunacy." Preventing [[DeepSeek]]-on-Huawei diffusion, in his framing, matters more than denying a single capability tier.

Mythos now carries dual policy-debate weight: [[Scott Bessent|Bessent]] uses it to justify the compounding-lead thesis (export controls buy time during a logarithmic gap); Dwarkesh uses it to justify containment; Jensen uses it to argue the containment thesis is incoherent because the training threshold is already crossed. The three readings cannot all be right — watch which one dominates the next cycle of chip-export policy.

See [[Export controls#Jensen Huang rebuttal (Dwarkesh, Apr 15, 2026)]] for the full Jensen argument and [[Jensen Huang]] for the speaker profile.

---

## Related

- [[Anthropic]] — parent company
- [[Project Glasswing]] — controlled early-access program for Mythos Preview
- [[Claude]] — product family
- [[Claude Opus]] — current top tier (Opus 4.6), which Mythos reportedly surpasses
- [[Claude Code Security]] — Anthropic's existing AI vulnerability scanner
- [[OpenAI Spud]] — OpenAI's competing next-gen model, teased the same week
- [[AI cybersecurity disruption basket]] — tracks vendor disruption from AI labs
- [[Cybersecurity]] — sector impact
- [[Scott Bessent]] — Treasury endorsement April 2026
- [[US-China AI race]] — Bessent uses Mythos to argue US 3-6 months ahead
- [[Jensen Huang]] — rebuts the Mythos-as-containment-justification framing (Apr 15, 2026)
- [[Export controls]] — policy debate where Mythos functions as central exhibit

### Cross-vault
- [Technologies: Claude Mythos](obsidian://open?vault=technologies&file=Claude%20Mythos) — technical architecture, model tier taxonomy, leak mechanics
