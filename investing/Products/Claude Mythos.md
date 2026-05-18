---
aliases: [Mythos, Capybara, Claude Capybara, Claude Mythos Preview]
tags: [product, ai]
parent_actor: "Anthropic"
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

### Bessent–Powell emergency Treasury meeting (April 10 2026)

The more important signal was who reacted, and at what level. On April 10 2026, US Treasury Secretary [[Scott Bessent]] and Federal Reserve Chair [[Jerome Powell]] convened an urgent meeting at the Treasury Department with major US bank CEOs to discuss the cyber-risk capabilities of Mythos. The bank CEOs were already in Washington for a Financial Services Forum board meeting, which is how the agenda was set up on short notice.

| Attendee | Bank |
|---|---|
| [[Brian Moynihan]] | [[Bank of America]] |
| [[Jane Fraser]] | [[Citigroup]] |
| [[David Solomon]] | [[Goldman Sachs]] |
| [[Ted Pick]] | [[Morgan Stanley]] |
| [[Charlie Scharf]] | [[Wells Fargo]] |
| (absent) | [[Jamie Dimon]] ([[JPMorgan Chase]]) — only major banking CEO unable to attend |

That a single AI model triggered a same-day convening of Treasury, the Fed, and the bulge-bracket CEO bench is the cleanest signal to date that frontier AI cyber capabilities have crossed into the financial-stability perimeter. The meeting is read in the vault alongside [[AI in financial services#Systemic risk vectors|systemic AI risks for financial services]] — Mythos is now the canonical case study for the cyber vector in that framework.

### UK parallel (April 12 2026)

Two days later, the [[Bank of England]], [[Financial Conduct Authority]], and the [[UK National Cyber Security Centre]] were reported to be coordinating on whether Mythos-class models could expose vulnerabilities in critical financial IT systems, with UK banks, insurers, and exchanges due to be briefed within a fortnight. See [[Financial Conduct Authority#Anthropic Mythos review (Apr 2026)]].

That is a different category of AI release. Mythos was not treated as a consumer launch or even a normal enterprise product cycle. It was treated as a controlled capability with potential financial-stability and operational-resilience implications.

*Sources: [CNBC: Powell, Bessent discussed Anthropic's Mythos AI cyber threat with major U.S. banks](https://www.cnbc.com/2026/04/10/powell-bessent-us-bank-ceos-anthropic-mythos-ai-cyber.html); [Bloomberg: Bessent, Powell Summon Bank CEOs to Urgent Meeting Over Anthropic's New AI Model](https://www.bloomberg.com/news/articles/2026-04-10/anthropic-model-scare-sparks-urgent-bessent-powell-warning-to-bank-ceos); [Fortune: Bessent and Powell convened Wall Street CEOs](https://fortune.com/2026/04/10/bessent-powell-anthropic-mythos-ai-model-cyber-risk/); [FT, Tett, May 8 2026](https://www.ft.com/content/c0aec3de-b553-4089-b5d3-074c5b83be57).*

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

## Capability tier and release color (Patel, Apr 23, 2026)

[[Dylan Patel]] on [[Invest Like the Best]] (Apr 23, 2026, recorded the day [[Claude Opus|Opus 4.7]] launched) added detail on Mythos's internal availability and capability framing that complements the public benchmarks-and-leak story:

- **Internal availability since Feb 2026.** [[Anthropic]] had Mythos working internally roughly two months before the late-March CMS-leak discovery. The selective-deployment program ([[Project Glasswing]]) — which Patel calls "earwig" / "glasswig" as a running joke — released the model only to [[Cybersecurity]] firms and ~40 critical-infrastructure organizations, deliberately delaying broad release on safety grounds
- **Capability tier: L4 → L6 software engineer in two months.** [[Anthropic]]'s 2024-2025 internal goal was "an L4 software engineer" by end of 2025; Patel's read is that [[Claude Opus|Opus 4.6]] (Feb 2026) hit L4 and Mythos reached L6 by February 2026 — a step Patel calls "potentially the biggest step up in model capabilities in 2 years." See [[Idea-execution inversion]] for the structural implication
- **Per-token cost 5-10x prior tier; lower per-task cost.** Patel: "Mythos is more expensive as a model but it spends a lot less tokens to do the thing and therefore it is actually cheaper in most tasks than [[Claude Opus|4.6 Opus]] because it's just way more efficient even though each individual token is smarter." The pricing is per the model card already published to selective customers
- **Public release deliberately weakened at cyber.** Per the model card disclosed to [[Project Glasswing]] participants, the broader public release (when it lands) will have measurably reduced cyber-offensive capability versus the version currently in defenders' hands. Patel: "they explicitly said in the model card hey we actually preferentially made it worse at cyber"
- **Begging-for-access anecdote.** Patel's framing of capacity scarcity at the frontier: "One of my funniest memories in the past month and a half is myself and [[Leopold Aschenbrenner|Leopold]] being on our knees in front of an Anthropic co-founder begging him for access to Mythos and then pretending it doesn't exist cuz we knew it existed." Color illustrates the gating dynamic that drives [[Inference economics#Permanent-underclass thesis (Patel, Apr 2026)|the permanent-underclass thesis]] — concentration of frontier-tier access among well-capitalized customers with [[Anthropic]] relationships

The April 23 framing sits alongside [[Scott Bessent|Bessent]]'s "step function change" Treasury endorsement and the [[Jensen Huang|Jensen]] / [[Dwarkesh Patel|Dwarkesh]] policy debate — three different uses of the same model: as compounding-lead exemplar (Bessent), as cyber-containment justification (Dwarkesh), as evidence that scaling laws still work and execution costs continue collapsing (Patel).

*Source: [[Dylan Patel]] on [[Invest Like the Best]] (Apr 23, 2026)*

---

## Policy-debate role — Dwarkesh × Jensen (Apr 15, 2026)

Mythos became the central exhibit in Dwarkesh Patel's export-controls exchange with [[Jensen Huang]]. Dwarkesh framed Mythos as the decisive example of AI crossing into weapon-adjacent capability — found zero-day vulnerabilities in every major operating system and browser, including one in OpenBSD after 27 years of secure-by-design engineering, so consequential [[Anthropic]] is withholding public release until defenders patch. The Dwarkesh thesis: if [[China]] had enough [[NVIDIA]] compute to train and run millions of instances of a Mythos-class model, that materially raises cyber-offensive risk to the US.

Jensen's rebuttal directly defused the Mythos framing: "Mythos was trained on fairly mundane capacity and a fairly mundane amount of it." The threshold Dwarkesh treats as dangerous is, in Jensen's read, already available to China in abundance — 60% of mainstream chip manufacturing, 50% of the world's AI researchers, ghost data centers fully powered. Jensen rejected the enriched-uranium and "Boeing selling nukes" analogies as category errors: "comparing AI to anything you just mentioned is lunacy." Preventing [[DeepSeek]]-on-Huawei diffusion, in his framing, matters more than denying a single capability tier.

Mythos now carries dual policy-debate weight: [[Scott Bessent|Bessent]] uses it to justify the compounding-lead thesis (export controls buy time during a logarithmic gap); Dwarkesh uses it to justify containment; Jensen uses it to argue the containment thesis is incoherent because the training threshold is already crossed. The three readings cannot all be right — watch which one dominates the next cycle of chip-export policy.

See [[Export controls#Jensen Huang rebuttal (Dwarkesh, Apr 15, 2026)]] for the full Jensen argument and [[Jensen Huang]] for the speaker profile.

---

## May 17, 2026 — bug-bounty submission flood (FT)

[[FT]] (Jamie John, May 17) names [[Claude Mythos]] as the named catalyst for the bug-bounty submission flood now overwhelming corporate vulnerability-disclosure programmes. Companies that pay hackers to find software flaws — [[HackerOne]] (Goldman Sachs / Google / US DoD clients), [[Bugcrowd]] (OpenAI / T-Mobile / Motorola clients), and smaller programmes like Curl and Nextcloud — are seeing submission volume rise sharply while legitimate-vulnerability discovery stays flat.

HackerOne CEO Kara Sprague specifically cited Mythos: the platform has "introduced new agentic validation capabilities" this year to "help organisations manage high volumes of findings, such as those generated by models like Mythos." HackerOne submissions +76% YoY March 2026; legitimate-vulnerability rate steady at 25% (so noise is what's growing, not signal). Bugcrowd reports more than quadrupled in three weeks in March. Curl suspended its paid bug bounty in January 2026; Nextcloud suspended in April 2026.

The market-structure implication: Mythos's deployment converted bug-bounty submission from a high-signal external-research channel into an adversarial filtering problem similar to what generative AI did to search-result spam. The platforms are adapting (AI agents to triage AI-submitted reports) but the unit economics of the external-research counterbalance to vendor security teams is now structurally changed. See [[AI cybersecurity disruption basket#May 17, 2026 — bug bounty disruption (FT)]] for the broader basket-thesis implication.

The vulnerability-discovery story has both a positive externality (more legitimate flaws caught faster by AI-using researchers) and a negative externality (most platforms have to suspend or rebuild to filter noise). The net market read on Anthropic's competitive position is still positive — Mythos is doing what it was designed to — but Anthropic now has a new stakeholder cohort (security-platform operators) whose adaptation costs are real.

*Source: [FT](https://www.ft.com/content/dbec4441-02dc-4053-8500-85677973d324), May 17, 2026.*

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
