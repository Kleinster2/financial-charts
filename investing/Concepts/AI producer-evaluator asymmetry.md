---
aliases: [AI input-cost collapse, AI signal-collapse pattern, AI producer-evaluator gap, adversarial filtering market structure]
tags: [concept, ai, market-structure, framework]
---

# AI producer-evaluator asymmetry

A structural framework for how generative AI breaks market designs that depend on the cost of producing input being comparable to the cost of evaluating it. When the producer-side cost collapses (AI generates submissions in seconds) but the evaluator-side cost doesn't (legitimate review still requires expert time), the signal-to-noise ratio of the market dilutes — and the market must either die, rebuild gatekeeping with AI on both sides, revert to closed channels, or add staking / credentialing to filter volume. Useful as a diagnostic across bug bounties, peer review, job applications, customer complaints, code review, creative submissions, and any other system that historically relied on input cost as an implicit filter.

---

## The asymmetry that breaks

Many economic systems work because of a roughly balanced cost structure between producers and evaluators:

| Side | Cost | Source |
|---|---|---|
| Producer | Time + expertise to generate a submission | Effort tax |
| Evaluator | Time + expertise to assess a submission | Attention tax |

The ratio was implicitly bounded by the producer side: you couldn't get flooded with more submissions than people were willing to put effort into producing. Bug bounties, academic peer review, journalism pitches, job applications, regulatory filings, complaint procedures, code review, and creative submissions all rest on this balance.

Generative AI collapses the producer side:

| Side | New cost | Implication |
|---|---|---|
| Producer | ≈ zero (prompt + seconds of compute) | Volume scales without effort cost |
| Evaluator | Unchanged (still requires expert time) | Volume scales faster than gatekeeping |

The new ratio is unbounded on the producer side. Submission volume can grow arbitrarily; legitimate-signal volume can't. Signal-to-noise dilutes.

---

## The diagnostic test — volume vs legitimate rate

The cleanest empirical marker that a market has crossed the asymmetry threshold is divergence between submission volume and legitimate-finding rate. Both should rise together if AI is genuinely augmenting producers (helping researchers find more real bugs, helping journalists pitch more real stories). Flat legitimate rate alongside rising volume is the slop-scaling pattern — pure denominator growth without numerator growth.

| Market | Year | Volume change | Legitimate rate | Verdict |
|---|---|---|---|---|
| [[HackerOne]] | YoY March 2026 | +76% | Steady at 25% | Slop-scaling confirmed |
| [[Bugcrowd]] | 3-week period March 2026 | Reports more than quadrupled | "Most proving to be false" | Slop-scaling confirmed |

This is the diagnostic worth tracking across other markets. If a system publishes both submission volume and acceptance rate, the *acceptance rate trajectory* is the binding signal — if it's flat or falling while volume rises, AI is the cause.

---

## Four sustainable equilibria

Once the asymmetry breaks, the market must converge on one of four responses. Each has a representative example from the 2025-26 bug-bounty episode:

### 1. Die / suspend

The market closes because the gatekeeping cost has become prohibitive relative to the signal value extracted. The open-access benefit is lost.

- Curl bug bounty (Daniel Stenberg): suspended paid programme January 2026 — "explosion in AI slop reports"
- Nextcloud: suspended programme April 2026 — "massive increase of low-quality reports"

### 2. Rebuild gate with AI on both sides

The market installs AI-powered triage so the evaluator side also scales. Builds a parallel infrastructure that wasn't needed before; ongoing costs scale with submission volume.

- [[HackerOne]]: "introduced new agentic validation capabilities" for high-volume findings
- [[Bugcrowd]]: AI agents for triage; positions human creativity as the irreplaceable layer

### 3. Revert to closed channels

The market exits open submission entirely and reverts to invitation-only / warm-introduction / personal-trust gates. Loses the original benefit of open access (catching the legitimate outsider with the unusual angle).

- VC pitch decks visibly moving back toward warm-intro-only at many firms
- Some academic journals closing public submission entirely
- Creative agencies closing inboxes to unsolicited material

### 4. Add staking / credentialing

The market requires submitters to bond something they value (verified identity, payment, reputational risk) before each submission. Filters AI-generated volume but also filters legitimate amateurs and unverified researchers.

- Bug-bounty platforms introducing "more stringent background checks"
- Payment-to-submit models (rare, but emerging)
- Bonded-submission models where the submitter loses the bond on rejected reports

Markets are typically cycling through some combination of all four simultaneously. Whichever combination ends up cost-effective at scale defines the new market structure.

---

## Cross-market manifestations

The pattern shows up wherever an existing system relied on input cost as the implicit filter. Different markets are at different stages of breaking:

| Market | Stage | Notes |
|---|---|---|
| Search / SEO content | Fully broken | Google response = AI on both sides (algorithmic + AI Overviews). Result: search-result quality contested. |
| Email | Repeatedly broken | Spam was the original break; AI-personalized phishing is the second wave. Both sides run AI. |
| Bug bounties | Visibly breaking 2026 | This concept's home case |
| Academic peer review | Breaking | AI-generated submissions flooding journals. Some banning AI-assisted; others requiring disclosure. |
| Job applications | Breaking | Producer-side AI cover letters meet evaluator-side ATS systems running AI rejection. |
| Customer service / regulatory complaints | Early stage | AI complaint generation hitting CFPB, FTC, ombudsmen. Stricter intake gates emerging. |
| VC pitch decks | Quietly broken | Partners reverting toward warm intros only; many firms no longer reading unsolicited decks. |
| Code review at large companies | Early stage | Agentic coding tools ([[Claude Code]], Devin) submitting PRs at machine rate; senior-engineer review time unchanged. |
| Trade-secret discovery (legal) | Emerging | AI document generation vs reviewer time. Production-volume disputes already in case law. |
| Creative submissions to publishers/agencies | Visibly breaking | Closed inboxes increasingly common. |

Each of these is the same structural problem; the visible-stage difference is just whether the gatekeeping side has installed AI triage yet.

---

## The Sora inversion — same pattern, different axis

[[Sora]]'s March 2026 discontinuation is the same producer-evaluator asymmetry rotated 90 degrees. Instead of AI breaking the producer side, the structural advantage is *which side already had data scale at the producer end*.

| Asymmetry axis | Bug bounty case | Video AI case |
|---|---|---|
| Producer-side scaling factor | AI generates submissions at zero marginal cost | Chinese short-video platforms ([[TikTok]] / [[Douyin]] / [[Kuaishou]]) own training data US can't replicate |
| Gatekeeping disadvantage | Evaluator can't scale to match producer | US labs have content-moderation / IP-respect constraints that Chinese labs don't |
| Visible outcome | Bug-bounty submission flood | OpenAI exits video; Chinese cohort leads |
| Vault note | [[AI cybersecurity disruption basket#May 17, 2026 — bug bounty disruption (FT)]] | [[AI Video Generation#May 17, 2026 — Chinese groups pull ahead of US rivals (FT)]] |

The deeper point: both stories are about systems where input was historically scarce or expensive (legitimate bug reports; quality video training data) and where AI / data advantages collapsed that scarcity *for one side only*. The market reorganizes around whoever benefits from the asymmetric collapse.

This is why "AI augments humans" claims need an asymmetric-adoption check. Adoption isn't uniform across producer and evaluator sides of a market; whichever side adopts faster captures the structural rents from the transition. Chinese labs adopted training-data abundance faster than US labs adopted content-moderation flexibility. Bug-bounty submitters adopted AI generation faster than platforms adopted AI triage. In both cases, the slow-side incumbents lose first.

---

## Implications for AI thesis

Three implications worth carrying forward when evaluating AI investments and exposures:

1. The [[AI cybersecurity disruption basket]] thesis broadens. Original framing: AI labs disrupt incumbent security vendors via product substitution. Add a second channel: the external-research market structure (bug bounties) that historically counter-balanced vendor security teams is also disrupted, weakening incumbent vendors' "we catch the things our own teams miss via the bounty pipeline" defense. Two channels of disruption strengthens the short thesis.
2. Every "AI augments humans" pitch needs an asymmetric-adoption stress test. If the augmentation flows to the producer side faster than the evaluator side, the market becomes more noisy, not more productive. The HackerOne data is the cleanest example: AI is augmenting both researchers (finding flaws faster) and adversarial submitters (generating slop) — net signal is flat while volume rises.
3. Markets that publish both submission volume and acceptance rate are leading indicators. When these diverge (acceptance rate flat or falling while volume rises), the asymmetry has crossed the threshold and one of the four equilibria is now playing out. Watch for divergence in: academic-journal submission/acceptance rates, regulatory-complaint intake/resolution rates, code-review PR volume/merge rates, customer-service ticket volume/first-contact-resolution rates.

---

## Related

- [[AI cybersecurity disruption basket]] — bug bounty as the home case; bidirectional cross-link to May 17 section
- [[AI Video Generation]] — the Sora-inversion case (geography-based asymmetry)
- [[Claude Mythos]] — named catalyst for the bug-bounty submission flood
- [[Claude Code]] — agentic coding tool generating PRs at machine rate; producer-side AI in the code-review asymmetry
- [[AI disintermediation]] — adjacent thesis on AI displacing intermediary professional services
- [[Inference economics]] — supply-side cost-structure context that makes producer-side AI deployment economic
- [[February 2026 AI Disruption Cascade]] — broader software-repricing event the basket sits inside

### Cross-vault

- [Technologies: Generative AI](obsidian://open?vault=technologies&file=Concepts%2FGenerative%20AI) — foundational technology stub candidate
- [Geopolitics: AI race](obsidian://open?vault=geopolitics&file=Concepts%2FAI%20race) — geographic-asymmetry framing for the Sora inversion

---

*Created 2026-05-18. First articulated in response to the FT May 17 AI bundle: [bug bounty AI slop](https://www.ft.com/content/dbec4441-02dc-4053-8500-85677973d324) + [Chinese video AI lead](https://www.ft.com/content/9804b1de-653b-40b2-bffb-17c76ebebe34). Concept extraction promoted from scattered context across [[AI cybersecurity disruption basket]] and [[AI Video Generation]] into a standalone structural framework that generalizes across markets.*
