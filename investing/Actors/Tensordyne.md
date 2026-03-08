---
aliases: [Recogni]
---
#actor #semiconductor #ai #inference #usa #private

**Tensordyne** — AI inference chip startup building dataflow architecture silicon. Formerly Recogni (rebranded ~Sep 2025). Claims 1/3 the capex per token and 1/8 the power per token vs [[Blackwell]]-generation [[NVIDIA]] racks.

---

## Synopsis

San Jose-based inference chip company that rebranded from Recogni in late 2025 to reflect a broader AI focus beyond its automotive origins. The core pitch: a dataflow architecture that scales to 144-chip domains (TP144 tensor parallelism), delivering 3M tokens/sec throughput per rack on Llama3.3-70B — at a fraction of the cost and power of [[NVIDIA]] equivalents. Raised $102M Series C in February 2024, co-led by [[Celesta Capital]] and GreatPoint Ventures. The bull case is the same as every [[NVIDIA]] alternative: hyperscalers and enterprises want inference cost reduction and supplier diversification. The bear case is also familiar: [[CUDA moat]], ecosystem lock-in, and the graveyard of chipmakers who claimed NVIDIA-beating benchmarks but couldn't ship at scale. Worth watching whether Tensordyne's numbers hold up in production deployments, not just benchmarks.

---

## Quick stats

| Metric | Value |
|--------|-------|
| Ticker | Private |
| HQ | San Jose, CA |
| Founded | — |
| Former name | Recogni (rebranded ~Sep 2025) |
| Founder/CPO | R.K. Anand (ex-Juniper Networks EVP) |
| Architecture | Dataflow |

---

## Leadership

| Role | Name | Background |
|------|------|------------|
| Founder/CPO | R.K. Anand | Ex-Juniper Networks EVP |

---

## Technology

Dataflow architecture — fundamentally different from von Neumann designs:

| Claim | Value | Comparison |
|-------|-------|------------|
| Throughput | 3M tokens/sec per rack | Llama3.3-70B |
| Capex per token | 1/3x | vs [[Blackwell]]-gen [[NVIDIA]] racks |
| Power per token | 1/8x | vs [[Blackwell]]-gen [[NVIDIA]] racks |
| Tensor parallelism | Up to TP144 | 144 chips per domain |

These are company claims — independent benchmarks pending.

---

## Cap table

| Round | Date | Amount | Lead investors |
|-------|------|--------|----------------|
| Series C | Feb 2024 | $102M | [[Celesta Capital]], GreatPoint Ventures |
| Earlier rounds | — | — | — |
| Total known | | $102M+ | |

Other investors: Mayfield, DNS Capital, BMW i Ventures, SW Mobility Fund, Pledge Ventures, Tasaru Mobility Investments (Saudi subsidiary)

---

## Related

- [[Celesta Capital]] — lead investor (Series C)
- [[NVIDIA]] — incumbent competitor
- [[SambaNova]] — peer (alternative AI chip, also Celesta portfolio)
- [[Cerebras]] — peer (alternative AI chip)
- [[Groq]] — peer (inference chip)
- [[CUDA moat]] — the ecosystem barrier facing all challengers
- [[Blackwell]] — NVIDIA generation being benchmarked against
