#concept #defense #cloud #procurement

**Joint Warfighting Cloud Capability (JWCC)** — the Pentagon's $9B multi-vendor cloud contract, awarded December 2022 to [[Amazon|AWS]], [[Microsoft]], [[Google]], and [[Oracle]]. Replaced the failed single-vendor JEDI contract. Provides enterprise cloud across all classification levels (unclassified through top-secret) and all domains (strategic to tactical edge). Managed by [[DISA]]. Successor contract "JWCC Next" expected to solicit in early 2026 with awards by early 2027.

---

## Quick stats

| Detail | Value |
|--------|-------|
| Contract ceiling | $9B |
| Awarded | December 7, 2022 |
| Vendors | [[Amazon\|AWS]], [[Microsoft]], [[Google]], [[Oracle]] |
| Structure | Multiple-award IDIQ; vendors compete for task orders |
| Task orders awarded | ~$2.7B through early 2025 |
| Classification split | ~50% unclassified, ~30% classified, ~10% top-secret |
| Task orders issued | 65+ |
| Managing agency | [[DISA]] (Defense Information Systems Agency) |
| Successor | JWCC Next — solicitation Q1 CY2026, award early FY2027 |

---

## JEDI → JWCC

The Joint Enterprise Defense Infrastructure (JEDI) was a $10B single-vendor cloud contract. Awarded to [[Microsoft]] in October 2019 over [[Amazon|AWS]]. Amazon challenged the award in the Court of Federal Claims, arguing Trump exerted "improper pressure" due to his animosity toward [[Jeff Bezos]] and the Washington Post. A federal judge halted Microsoft's work in February 2020. After 20 months of litigation and no progress, the Pentagon canceled JEDI in July 2021 and announced a multi-vendor replacement.

The lesson: single-vendor lock-in was politically and legally untenable. JWCC split the work across four hyperscalers competing for task orders — cheaper, more resilient, and harder to challenge.

---

## Task order dynamics

Vendor-by-vendor breakdowns are not publicly released (competitive sensitivity + OPSEC). Known specifics:

- [[Oracle]] — secured the largest single award: US Army's PeopleSoft migration to Oracle Government Cloud (legacy advantage + [[Accenture]] Federal Services integration)
- [[Amazon|AWS]] — early sole-source wins for joint intelligence community edge cloud pilot and public key infrastructure initiative
- [[Microsoft]] — sole-source task orders for enterprise messaging and email security gateway pilot
- [[Google]] — Navy task orders alongside [[Oracle]]

The ramp has been gradual: $600M by May 2024, ~$1B by August 2024, ~$2.7B by early 2025 — well below the $9B ceiling with the contract still in early innings.

---

## JWCC Next

DISA is preparing a successor contract ("JWCC Next") to replace and extend JWCC. Key changes:

- Broader provider pool — opens to smaller, non-traditional cloud providers offering AI tools, satellite relays, and rugged edge services. Large hyperscalers hold main cloud regions; smaller firms compete for mission-specific tasks (maritime sensor data, airborne fusion)
- Third-party marketplace access — [[DISA]] discovered mid-contract that customers needed access to third-party vendor tools, not just the four primes
- Longer contract term — aiming to avoid the 5-year transition cycle
- AI integration — reflects Pentagon's shift toward AI-native cloud infrastructure

Timeline: solicitation expected Q1 CY2026 (Q2 FY2026), awards early FY2027. Some overlap planned with existing JWCC for smooth transition.

---

## Relationship to Pentagon AI contracts

JWCC and the ~$200M AI lab contracts ([[Pentagon AI access dispute 2026]]) are separate procurement vehicles serving different purposes:

| | JWCC | AI lab contracts |
|--|------|-----------------|
| Purpose | Enterprise cloud infrastructure | Frontier AI model access on classified networks |
| Vendors | [[Amazon\|AWS]], [[Microsoft]], [[Google]], [[Oracle]] | [[Anthropic]], [[OpenAI]], [[Google]], [[xAI]] |
| Value | $9B ceiling | ~$200M each |
| Structure | IDIQ with task orders | Direct contracts |
| Classification | All levels | Classified focus |

The AI lab contracts deploy frontier models *on top of* cloud infrastructure that JWCC provides. [[Palantir]]'s Maven Smart Systems, which uses [[Claude]] code, runs on this classified cloud layer. The [[Pentagon AI access dispute 2026|Anthropic supply-chain risk designation]] creates tension: JWCC vendors ([[Amazon]], [[Google]], [[Microsoft]]) are also major Anthropic investors/compute providers, but must comply with the ban in their government work.

JWCC Next's expansion to "nontraditional vendors" including AI companies could blur this boundary — AI labs might compete directly for JWCC Next task orders rather than through separate contracts.

---

## Related

- [[Pentagon AI access dispute 2026]] — separate AI model contracts, but runs on JWCC infrastructure
- [[Amazon]] — JWCC vendor + Anthropic's $8B lead investor; navigating dual role
- [[Microsoft]] — JWCC vendor, won original JEDI; Azure hosts OpenAI models
- [[Google]] — JWCC vendor + Anthropic investor; DeepMind quietly working with Pentagon
- [[Oracle]] — JWCC vendor; largest single task order (Army PeopleSoft)
- [[Palantir]] — Maven Smart Systems runs on classified cloud, uses Claude
- [[Scale AI]] — Donovan platform deployed on SIPRNet/JWICS
- [[Defense IT Services]] — subsector context
