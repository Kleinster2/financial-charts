---
date: 2026-02-23
aliases: [distillation wars, AI distillation controversy, model distillation scandal]
tags: [event, ai, china, ip]
---

# AI distillation wars (2025-2026)

US frontier AI labs accused Chinese competitors — principally [[DeepSeek]], [[Moonshot AI]], and [[MiniMax]] — of systematically extracting capabilities from their models via [[model distillation]]. [[OpenAI]] went first (Feb 12, 2026), [[Anthropic]] followed with granular technical evidence (Feb 23). Both disclosures landed during the US debate over AI chip [[export controls]], framing a commercial dispute as a national security issue.

---

## Timeline

| Date | Event |
|------|-------|
| Jan 2025 | [[DeepSeek]] launches [[DeepSeek-R\|R1]], sparking [[DeepSeek day]] ($600B [[NVIDIA]] wipeout). Users note similarities to [[ChatGPT]] |
| Late 2025 | [[OpenAI]] internally detects accounts linked to [[DeepSeek]] employees circumventing access restrictions |
| Feb 12, 2026 | [[OpenAI]] publicly accuses [[DeepSeek]] of using obfuscated third-party routers to distill [[ChatGPT]] models |
| Feb 23, 2026 | [[Anthropic]] publishes detailed blog post accusing [[DeepSeek]], [[Moonshot AI]], [[MiniMax]] of "industrial-scale distillation attacks" on [[Claude]] |
| Feb 24, 2026 | Backlash — Elon Musk, media outlets highlight hypocrisy given labs' own training on scraped internet data |

---

## Anthropic's evidence (Feb 23, 2026)

The most detailed disclosure. [[Anthropic]] attributed each campaign "with high confidence" through IP address correlation, request metadata, infrastructure indicators, and corroboration from industry partners.

| Lab | Exchanges | Targets |
|-----|-----------|---------|
| [[DeepSeek]] | ~150,000 | Foundational logic, alignment, censorship-safe alternatives to policy-sensitive queries |
| [[Moonshot AI]] | ~3.4M | Agentic reasoning, tool use, coding, data analysis, computer vision |
| [[MiniMax]] | ~13M | Agentic coding, tool use, orchestration |
| Total | 16M+ | Via 24,000+ fraudulent accounts |

### Infrastructure

The labs used "hydra cluster" architectures — sprawling networks of fraudulent accounts distributing traffic across [[Anthropic]]'s API and third-party cloud platforms. A single proxy network managed 20,000+ accounts simultaneously, mixing distillation traffic with unrelated customer requests to evade detection.

When [[Anthropic]] launched a new [[Claude]] model, [[MiniMax]] redirected nearly half its traffic to siphon capabilities from the fresh release.

### Anthropic's response

Investing in behavioral fingerprinting, tightening verification on abused pathways, sharing indicators with other labs and cloud providers, building product/API/model-level countermeasures to make outputs less useful for illicit distillation.

---

## OpenAI's accusations (Feb 12, 2026)

Less granular than [[Anthropic]]'s disclosure. [[OpenAI]] observed "accounts associated with [[DeepSeek]] employees developing methods to circumvent [[OpenAI]]'s access restrictions and access models through obfuscated third-party routers."

[[OpenAI]]'s framing: "[[DeepSeek]]'s next model (whatever its form) should be understood in the context of its ongoing efforts to free-ride on the capabilities developed by [[OpenAI]] and other US frontier labs."

---

## The hypocrisy problem

The backlash was immediate and pointed:

- [[Anthropic]] settled for $1.5B over allegations of training [[Claude]] on pirated books from Library Genesis
- Every frontier lab trained on scraped internet data — books, articles, code, art — without compensating creators
- [[DeepSeek]] was a paying API customer. Distillation is arguably *more* defensible than scraping — at least they paid for the tokens
- Elon Musk led the charge on X; Futurism, Cybernews ran "hypocrisy" headlines
- One X user: "When you guys train your model by bombarding others for free of cost, it's fine. But if others are training by paying your model, it's illegal?"

The labs want one rule upstream (scraping is fair use) and another downstream (distillation is theft). The contradiction is structural, not incidental.

---

## Legal landscape

| Argument | Status |
|----------|--------|
| Copyright on AI outputs | Likely unprotectable — US Copyright Office says outputs without sufficient human input are not copyrightable |
| Terms of service violation | Valid contract claim, but near-unenforceable across US-China jurisdictions |
| Trade secret | Requires the secret to be secret — but these models are sold as API products |
| IP theft framing | Politically effective, legally weak |

See [[model distillation]] for the deeper IP analysis.

---

## Why the timing matters

Both disclosures landed during the US debate over tightening AI chip [[export controls]]. The argument being constructed for Washington:

1. Hardware controls are insufficient if Chinese labs can distill US models over the wire
2. API access itself may need restrictions — not just chips
3. Model weights should potentially be treated as controlled technology

This reframes a commercial dispute (TOS violation) as a national security issue (technology transfer to adversaries). The labs are building the case for a regulatory moat they cannot build technically.

---

## Investor narrative angle

If [[DeepSeek]] can replicate 80% of [[Claude]]'s capabilities by spending a few hundred thousand dollars on API calls instead of billions on training, that threatens the valuation thesis for every frontier lab. The "distillation is theft" framing reframes a competitive vulnerability as a law enforcement problem — easier to raise capital when the story is "we're being robbed by China" rather than "our moat is shallower than we told investors."

See [[model distillation]] for the moat implications.

---

## Analysis

The distillation complaints are a rearguard action. The real question isn't whether distillation is fair — it's whether frontier capability is a durable competitive advantage at all. If 16 million API calls can meaningfully close the gap with models that cost billions to train, then the value isn't in the weights. It's in distribution, ecosystem, enterprise relationships, and platform lock-in — exactly where [[OpenAI]] and [[Anthropic]] are sprinting right now.

The geopolitical framing is effective because it aligns commercial interest (protect our moat) with national interest (don't let China catch up). But the underlying economics are the same: distillation works because the knowledge in these models is extractable, and no TOS or export control can fully prevent that.

---

## Related

- [[Model distillation]] — concept (technique, IP landscape, moat implications)
- [[DeepSeek]] — primary accused across both disclosures
- [[Anthropic]] — published detailed evidence (Feb 23)
- [[OpenAI]] — first to accuse (Feb 12)
- [[Moonshot AI]] — 3.4M exchanges targeting agentic capabilities
- [[MiniMax]] — 13M exchanges, largest volume
- [[Export controls]] — political context (chip debate timing)
- [[DeepSeek day]] — origin (Jan 2025, R1 launch)
- [[AI Race]] — competitive dynamics
- [[Model lab economics]] — moat/valuation implications
- [[Open source commoditization]] — related pressure on frontier pricing

*Event date: February 23, 2026 (Anthropic disclosure)*
