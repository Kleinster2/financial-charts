---
aliases: [knowledge distillation, distillation, model distillation attacks, distillation attacks]
tags: [concept, ai, ip]
---

# Model distillation

Training a smaller "student" model on the outputs of a larger "teacher" model to replicate its capabilities at lower cost. A standard ML technique used internally by every frontier lab — and the center of a growing IP and geopolitical conflict when used across organizational boundaries.

---

## How it works

1. Query the teacher model (via API or direct access) with large volumes of prompts
2. Collect input-output pairs as training data
3. Train the student model to reproduce the teacher's responses
4. The student learns the teacher's reasoning patterns without the original training data or compute investment

Cost asymmetry: training a frontier model costs hundreds of millions to billions. Distilling from one costs orders of magnitude less — API fees plus student training compute.

---

## Legitimate vs illicit

| Use case | Example | Status |
|----------|---------|--------|
| Internal distillation | [[OpenAI]] GPT-4o-mini from GPT-4o | Standard practice, uncontroversial |
| Self-distillation | Lab distills its own models for cheaper tiers | Universal — every lab does this |
| Cross-lab distillation (with permission) | Licensed training partnerships | Legal, rare |
| Cross-lab distillation (without permission) | [[DeepSeek]] querying [[Claude]] via fake accounts | TOS violation, legally gray, politically explosive |

The technique itself is neutral. The controversy is about who distills whom, and whether they had permission.

---

## The IP problem

### Copyright

Most courts and the US Copyright Office have indicated that AI outputs lacking sufficient human-generated expressive input are generally not copyrightable. If the outputs aren't copyrightable, then collecting and training on them likely doesn't constitute copyright infringement. This undercuts the primary IP claim frontier labs could make.

### Terms of service

[[Anthropic]], [[OpenAI]], and other labs prohibit using outputs to train competing models in their TOS. This is a valid contract claim — but:
- Enforceable only within the jurisdiction where the contract was formed
- Near-meaningless against Chinese entities operating through proxy networks
- A contract claim, not an IP claim — weaker remedies, harder to enforce

### Trade secret

Requires the information to be secret and that reasonable steps were taken to protect it. But these models are sold as commercial API products — the whole business model is giving people access to the outputs. The "secret" is the weights, not the outputs.

### Net assessment

No existing IP framework cleanly covers cross-lab distillation. The legal argument is tissue-thin. The political argument (national security, technology transfer) is where the labs are placing their bets.

---

## The hypocrisy loop

The structural contradiction at the center of the distillation debate:

1. Frontier labs trained on scraped internet data — books, articles, code, art, forum posts — without compensating creators
2. When creators objected, labs argued fair use, transformative output, progress of science
3. Now competitors distill lab outputs, and labs cry theft
4. The distillers were paying customers — arguably a more defensible position than scraping

[[Anthropic]] settled for $1.5B over training on pirated Library Genesis books. The same labs that treat upstream creators' work as fair game want downstream use of their outputs to be prohibited. The principle they need — "you can't train on someone else's outputs without permission" — is exactly what artists, writers, and publishers have been arguing against the labs themselves.

---

## Moat implications

If distillation works — and the evidence from [[MiniMax]]'s M2.5 benchmarks suggests it does — then frontier model capability alone is not a durable moat.

| What's defensible | What's not |
|-------------------|------------|
| Distribution (ChatGPT's 900M WAU) | Raw model quality (distillable) |
| Enterprise relationships and trust | Benchmark scores |
| Platform ecosystem (MCP, Skills, agents) | Training investment (extractable) |
| Regulatory moats (export controls, compliance) | Algorithmic secrets (reverse-engineerable) |

This is why both [[OpenAI]] and [[Anthropic]] are racing toward platform lock-in — enterprise contracts, developer ecosystems, agent infrastructure. The models themselves are becoming commoditized faster than expected, and distillation accelerates that.

---

## Detection and countermeasures

[[Anthropic]]'s Feb 2026 blog post outlined their approach:

| Countermeasure | Description |
|----------------|-------------|
| Behavioral fingerprinting | Detecting query patterns distinct from normal usage |
| Rate limiting | Throttling suspicious high-volume access |
| Verification tightening | Stricter identity checks on pathways frequently abused |
| Output watermarking | Embedding detectable signals in model outputs |
| Cross-lab information sharing | Sharing indicators with other labs and cloud providers |
| Model-level countermeasures | Making outputs less useful for training (e.g., adding noise, limiting structured reasoning in responses) |

Technical arms race: countermeasures are cat-and-mouse. Determined actors with sufficient resources can always find new attack vectors — especially when the "attack" is just querying a commercial API at scale.

---

## Related

- [[AI distillation wars (2025-2026)]] — event (OpenAI + Anthropic accusations)
- [[DeepSeek]] — primary accused
- [[MiniMax]] — largest volume distiller (13M exchanges)
- [[Moonshot AI]] — agentic capability targeting
- [[Anthropic]] — detailed technical disclosure
- [[OpenAI]] — first public accusation
- [[Export controls]] — political context
- [[Open source commoditization]] — related pricing pressure
- [[Model lab economics]] — valuation implications if moat is weaker than assumed
- [[AI Race]] — competitive dynamics
