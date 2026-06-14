---
aliases: [Inferact AI, vLLM]
tags: [actor, ai, infrastructure, inference, private, usa]
---

#actor #ai #infrastructure #inference #private #usa

One-line read: **Inferact** is the vLLM team's commercial company — the maintainers of the most widely deployed open-source inference engine (running on 400,000+ GPUs) turning it into a managed "universal inference layer" — and the highest-valued ($800M) of the Berkeley/Ion-Stoica inference-engine spinouts; the bet is that owning the dominant open-source engine converts into the commercial default, with the risk being whether an open-source-first company can monetize without alienating the community that made vLLM ubiquitous.

---

Inferact is the company built by the core maintainers of vLLM, the leading open-source LLM inference engine (known for its PagedAttention memory technique and continuous batching), which runs on over 400,000 GPUs worldwide. Founded in November 2025 and emerging from the UC Berkeley lineage around Ion Stoica, it raised a $150M seed at an $800M valuation in January 2026 co-led by [[Andreessen Horowitz]] and [[Lightspeed Venture Partners]] — the highest valuation in the [[Open-source inference engines]] cluster, ahead of sibling [[RadixArk]] (SGLang, $400M). Its plan is a next-generation commercial inference engine — a "universal inference layer" of serverless vLLM plus observability, troubleshooting, and disaster recovery — while continuing to fund the open-source project rather than competing with it.

---

## Quick stats

| Metric | Value |
|--------|-------|
| Ticker | Private |
| Founded | November 2025 |
| HQ | San Francisco / UC Berkeley orbit |
| Founders | Simon Mo (CEO), Woosuk Kwon, Kaichao You, Roger Wang |
| Category | Open-source inference engine (vLLM) — commercial arm |
| Latest valuation | $800M (seed, Jan 2026) |
| Scale | vLLM on 400,000+ GPUs worldwide |

---

## Leadership

- Simon Mo — co-founder and CEO; UC Berkeley PhD student and a founding maintainer of vLLM.
- Woosuk Kwon — co-founder; original creator of vLLM / PagedAttention.
- Kaichao You — co-founder; vLLM maintainer (Tsinghua).
- Roger Wang — co-founder; vLLM maintainer.

---

## Funding history

| Round | Date | Amount | Valuation | Lead / investors |
|-------|------|--------|-----------|------------------|
| Seed | Jan 2026 | $150M | $800M | [[Andreessen Horowitz]] + [[Lightspeed Venture Partners]] (co-lead); [[Sequoia Capital]], Altimeter Capital, Redpoint Ventures, ZhenFund |

---

## How Inferact works

vLLM is the open-source engine underneath — its PagedAttention treats the KV cache like paged virtual memory, raising GPU utilization and throughput, and continuous batching keeps the accelerator fed. Inferact's commercial layer wraps that engine as a managed, serverless product: a "universal inference layer" adding observability, troubleshooting, and disaster recovery, expected to run on Kubernetes, so an enterprise gets vLLM performance without operating the stack. The stated posture is collaboration over competition — Inferact funds the open-source project with dedicated financial and developer resources, betting that stewardship of the de facto standard engine is the durable commercial moat.

---

## Competitive landscape

| Front | Players | Dynamic |
|-------|---------|---------|
| Open-source engine spinouts | [[RadixArk]] (SGLang), [[TensorMesh]] (LMCache) | Direct peers from the same Berkeley/Stoica lineage; Inferact is the highest-valued |
| Managed inference clouds | [[Fireworks AI]], Together AI, Baseten | Commercial serving competitors that also build on or alongside open engines |
| Foundation-model first-party serving | [[OpenAI]], [[Anthropic]], [[Google]] | The labs serve their own models; Inferact's pitch is neutral, open-weight serving |

---

## What to watch

- Open-source/commercial tension — whether monetizing a managed layer alienates the vLLM contributor community that drives adoption.
- Valuation gap vs [[RadixArk]] — Inferact $800M vs RadixArk $400M on similar theses; whether the premium for vLLM's larger install base holds.
- Foundation-model encroachment — labs improving first-party serving compress the neutral-layer opportunity.
- Revenue model — serverless vLLM pricing vs self-hosting-for-free; the conversion rate from OSS users to paying customers.

---

## Related

- [[Open-source inference engines]] — the cluster (vLLM's commercial arm)
- [[RadixArk]] — sibling spinout (SGLang); same UC Berkeley / Ion Stoica lineage
- [[TensorMesh]] — peer (LMCache KV-caching)
- [[Fireworks AI]] — managed-inference competitor
- [[Andreessen Horowitz]], [[Lightspeed Venture Partners]], [[Sequoia Capital]] — investors
- [[Inference economics]] — the cost dynamics it drives
- [[NVIDIA]] — its engine runs on (and is optimized for) Nvidia GPUs

### Cross-vault
- [Technologies: Agentic Inference](obsidian://open?vault=technologies&file=Agentic%20Inference) — why agent inference is memory-bound and decode-heavy (the problem vLLM optimizes)

*Created 2026-06-13 (expanded from stub). Private company — figures from funding announcements; revenue undisclosed.*
