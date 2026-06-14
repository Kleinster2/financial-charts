---
aliases: [Tensormesh, LMCache]
tags: [actor, ai, infrastructure, inference, private, usa]
---

#actor #ai #infrastructure #inference #private #usa

TensorMesh is the company behind LMCache, the leading open-source KV-caching project (8,000+ GitHub stars; integrates with vLLM, SGLang, TensorRT, and NVIDIA Dynamo). Its platform, Tensormesh Inference, stores and reuses computed KV-cache results to eliminate redundant computation, claiming up to 10x reductions in latency and GPU spend, and bills cached input tokens at zero cost. Led by Junchen Jiang (University of Chicago faculty, LMCache co-creator), it sits in the [[Open-source inference engines]] cluster as the cache-acceleration specialist.

---

## Quick stats

| Metric | Value |
|--------|-------|
| Ticker | Private |
| Founders | Junchen Jiang (UChicago) + LMCache team (UChicago / Berkeley / CMU) |
| Category | Inference cost optimization (KV caching) — LMCache commercial arm |
| Total raised | $24.5M |
| Claim | Up to 10x latency / GPU-spend reduction; zero-cost cached input tokens |

---

## Funding history

| Round | Date | Amount | Valuation | Lead / investors |
|-------|------|--------|-----------|------------------|
| Seed (incl. extension) | May 2026 | $20M (round); $24.5M total | — | AMD Ventures, CoreWeave, NVentures ([[NVIDIA]]), Valley Capital Partners, Laude Ventures |

---

## Related

- [[Open-source inference engines]] — the cluster (LMCache commercial arm)
- [[RadixArk]] (SGLang), [[Inferact]] (vLLM) — peers; LMCache integrates with both
- [[NVIDIA]] — investor (NVentures); LMCache integrates with NVIDIA Dynamo
- [[Inference economics]] — KV-cache reuse is a core cost lever

*Stub created 2026-06-13 — expand with LMCache adoption and pricing-model detail.*
