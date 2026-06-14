---
aliases: [open source inference engines, inference engine commercialization, vLLM, SGLang, LMCache]
tags: [concept, ai, infrastructure, inference]
---

#concept #ai #infrastructure #inference

Open-source inference engines are the software layer that runs large language models efficiently in production — batching, KV-cache management, paged attention, scheduling. In 2025–26 the three leading projects each spun out a venture-backed company, creating a new cluster of inference-infrastructure startups. The engines trace mostly to academic labs (notably UC Berkeley's, under [[Databricks]]/Anyscale co-founder Ion Stoica), already process trillions of tokens a day for the largest AI companies, and are now commercialized by [[Inferact]] (vLLM), [[RadixArk]] (SGLang), and [[TensorMesh]] (LMCache). [[NVIDIA]]'s venture arm has backed most of them.

---

## Synthesis

This cluster is the supply side of the inference-cost collapse documented in [[Inference economics]], and it is the structural "below" pressure on both the foundation-model API business and the [[Agentic search infrastructure]] cohort. When an open-source engine serves an open-weight model ([[Open-weight models]], [[DeepSeek]]) at frontier-competitive performance for a fraction of the API price, any workflow or agent company can build on self-hosted open models instead of paying [[OpenAI]] or [[Anthropic]] API rates. That erodes lab pricing power from below at the same time the labs erode third-party tool layers from above — the two-sided squeeze on every thin layer in the agent stack.

The tell is that [[NVIDIA]] backs nearly all of them. NVentures is in [[RadixArk]] and [[TensorMesh]]; the engines integrate first-class with vLLM, TensorRT, and NVIDIA Dynamo. Nvidia does not need any single engine or company to win — it needs the inference-serving layer to standardize on software that runs best on its chips, whoever owns it. That is the [[CUDA moat]] extended up the stack from kernels into the serving layer. The companies themselves are infrastructure plays, not model labs: their edge is systems performance (throughput per GPU, latency, cache reuse), not weights — the "don't cosplay as a model company if you're a serving company" distinction.

---

## The engines and their commercial arms

| Engine | Origin | Commercial company | Funding | What it does |
|--------|--------|--------------------|---------|--------------|
| vLLM | UC Berkeley (Stoica lab) | [[Inferact]] | $150M seed / $800M ([[Andreessen Horowitz]] + [[Lightspeed Venture Partners]]) | PagedAttention; runs on 400,000+ GPUs worldwide |
| SGLang | UC Berkeley (Stoica lab) | [[RadixArk]] | $100M seed / $400M (Accel + [[NVIDIA]]) | RadixAttention; trillions of tokens/day for [[Google]], [[Microsoft]], xAI, [[NVIDIA]] |
| LMCache | UChicago / Berkeley / CMU | [[TensorMesh]] | $24.5M total (AMD Ventures, CoreWeave, NVentures) | KV-cache reuse; up to 10x latency/GPU-spend reduction |

---

## Why it matters

- Supply side of the inference price collapse — these engines are why self-hosted open-weight serving is cheap; see [[Inference economics]].
- The below-disintermediation vector — lets the [[Agentic search infrastructure]] cohort and any agent builder escape lab-API dependence by running open models, while also pressuring lab API margins.
- Nvidia's stack-up play — [[NVIDIA]] backing the serving layer is the [[CUDA moat]] moving from chips into software.
- Concentration of talent — vLLM and SGLang both incubated in one UC Berkeley lab (Ion Stoica), a Cambrian moment for inference systems comparable to the Databricks/Anyscale lineage.

All constituents are private; there is no public price series. (Market data not applicable.)

---

## Related

- [[Inference economics]] — the price collapse these engines drive
- [[Open source commoditization]] — the broader dynamic
- [[Open-weight models]] — the models these engines serve
- [[Fireworks AI]] — peer commercial inference-serving company
- [[Inferact]], [[RadixArk]], [[TensorMesh]] — the commercial arms
- [[NVIDIA]] — backs most of them; [[CUDA moat]] up the stack
- [[Agentic search infrastructure]] — the cohort this pressures from below
- [[DeepSeek]] — open-weight model whose cheap serving these engines enable

### Cross-vault
- [Technologies: Agentic Inference](obsidian://open?vault=technologies&file=Agentic%20Inference) — why agent inference is memory-bound and decode-heavy (the problem these engines optimize)
