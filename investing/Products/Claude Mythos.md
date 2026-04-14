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

## Related

- [[Anthropic]] — parent company
- [[Project Glasswing]] — controlled early-access program for Mythos Preview
- [[Claude]] — product family
- [[Claude Opus]] — current top tier (Opus 4.6), which Mythos reportedly surpasses
- [[Claude Code Security]] — Anthropic's existing AI vulnerability scanner
- [[OpenAI Spud]] — OpenAI's competing next-gen model, teased the same week
- [[AI cybersecurity disruption basket]] — tracks vendor disruption from AI labs
- [[Cybersecurity]] — sector impact

### Cross-vault
- [Technologies: Claude Mythos](obsidian://open?vault=technologies&file=Claude%20Mythos) — technical architecture, model tier taxonomy, leak mechanics
