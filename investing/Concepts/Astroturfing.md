---
aliases: [astroturf, fake grassroots, coordinated inauthentic behavior, CIB]
tags: [concept, marketing, social-media, regulation]
---
#concept #marketing #socialmedia #regulation

**Astroturfing** — Coordinated activity disguised as organic, grassroots support. The term predates the internet (US senator Lloyd Bentsen used it in 1985 to describe industry mail campaigns staged to look like constituent letters), but its operating surface has migrated almost entirely onto social platforms. The current AI-era variant is the practice of running large numbers of [[Synthetic creators|synthetic personas]] — accounts that look like ordinary users but are operated centrally — to promote a product, narrative, or political position.

## Synthesis

Astroturfing matters more in 2026 than it did in 2016 because the unit cost of a plausible fake account collapsed. The pre-AI version of the practice had hard ceilings: human-staffed content farms, crude bot networks easily detected at the network or behavioral layer, and limited content-generation capacity. The post-2024 version replaces all three layers with cheap substitutes — generative models for content, [[Phone farm|phone farms]] of real devices for behavior and network identity, and orchestration platforms like [[Doublespeed]] for control. The result is that an operation that previously needed dozens of human contractors can now run on a few hundred rented smartphones and one engineer. The detection side is iterating, but the cost asymmetry is the structural fact: defenders pay for compute and headcount; attackers pay for hardware that depreciates on a phone-replacement cycle.

---

## Why it gets its own concept note

Three things make astroturfing a distinct concept rather than a sub-case of fraud:

1. Legality is jurisdiction-specific and surface-specific. Paid promotion without disclosure violates [[FTC]] endorsement guidelines in the US; violates platform TOS on [[TikTok]], [[Meta]], X, and [[Reddit]]; and may or may not be a criminal matter depending on what is being promoted and where.
2. The supply curve has changed. Pre-2022, astroturfing required either large outsourced human teams (Russian Internet Research Agency, Filipino content farms) or crude bot networks easily detected by platforms. After 2024, generative content plus device-level evasion ([[Phone farm|phone farms]]) drops the cost of plausible astroturfing by an order of magnitude.
3. Detection is now an arms race rather than a one-time problem. Platforms and astroturfing vendors iterate against each other in roughly real time.

---

## Modern operating models

| Model | Example | Cost structure |
|-------|---------|----------------|
| State-sponsored influence ops | Russian IRA, Chinese Spamouflage, Iranian networks | Fully internalized; not priced |
| Commercial astroturfing-as-a-service | [[Doublespeed]], various less-public competitors | $1,500–$7,500/month per client |
| Brand "seeding" agencies | Many; often blur line between paid promotion and creator outreach | Project-based |
| Political consultancies running synthetic ops | Documented but mostly off-the-record | Project-based |

The commercial layer is the one that matters for this vault, because it has price points, named investors, and named clients (when breached).

---

## Detection and enforcement

Three pressure points exist on the detection side:

1. Platform-level: account-graph clustering, device fingerprinting, behavioral analysis. [[TikTok]], [[Meta]], and [[Reddit]] all run dedicated integrity teams; X (formerly Twitter) does as well, with significantly reduced staffing post-2022. Effectiveness varies; large coordinated networks regularly survive for months.
2. Regulatory-level: the [[FTC]] Endorsement Guides require disclosure of paid promotion regardless of whether the promoter is human or AI. The October 2025 [[Doublespeed]] breach produced a publicly enumerated list of undisclosed paid AI promoters — the cleanest possible enforcement target the FTC has had in this category.
3. Press-level: outlets including [[404 Media]] specialize in exposing the operating details of astroturfing networks. Press exposure is often what triggers platform action and regulatory attention.

---

## Why it matters in this vault

- Demand signal for [[Synthetic creators]]. As long as astroturfing clears as a marketing spend, the supply will exist.
- Platform integrity tax on [[TikTok]], [[Meta]], X, [[Reddit]]. Detection costs are real and ultimately fall on advertiser ROI.
- Regulatory and reputational tail risk for [[a16z]] and similar venture investors funding the commercial layer.
- Antecedent for thinking about state-actor influence operations; many of the same techniques scale across commercial and political use.

---

## Related

- [[Doublespeed]] — current poster-child commercial astroturfing vendor
- [[Synthetic creators]] — the persona layer
- [[Phone farm]] — the hardware layer
- [[Agentic AI]] — the autonomy layer
- [[FTC]] — primary US regulator
- [[404 Media]] — primary press source
- [[TikTok]] — primary current target platform
- [[Meta]] — frequent target across products
- X (formerly Twitter) — frequent target
- [[Reddit]] — has been explicit that platforms like Doublespeed violate TOS

---

*Created 2026-04-27. Stub.*
