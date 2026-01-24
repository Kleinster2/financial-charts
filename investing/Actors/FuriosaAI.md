---
aliases: [Furiosa, Furiosa AI]
---
#actor #ai #chips #korea #private

**FuriosaAI** — South Korean NPU startup building inference-optimized chips. RNGD delivers 2-3x better perf/watt vs NVIDIA GPUs. Mass production began January 2026. Rejected Meta's $800M acquisition offer.

---

## Why FuriosaAI matters

| Metric | Value |
|--------|-------|
| Valuation | **$735M** (Jul 2025) |
| Total raised | **$246M** |
| Founded | 2017 |
| Employees | ~200 |
| HQ | Seoul (Gangnam) |
| Status | Private (IPO prep) |

**The pitch:** Inference-optimized [[NPU]] chips that match NVIDIA GPU performance at 2-3x better power efficiency — critical as [[Power constraints]] become binding.

**The validation:** Meta tried to acquire for $800M (Mar 2025). FuriosaAI declined, citing disagreements over post-acquisition strategy. Three months later, signed LG AI Research as major customer.

---

## Key product: RNGD

| Spec | Detail |
|------|--------|
| Name | RNGD ("Renegade") |
| Type | [[NPU]] (Neural Processing Unit) |
| Process | **TSMC 5nm** |
| Memory | **48GB HBM3** (12-layer, CoWoS-S) |
| On-chip SRAM | **256MB** |
| Bandwidth | **1.5 TB/s** |
| Power | **150W** (vs H100 350W) |
| Clock | 1.0 GHz |

**Performance:**

| Precision | TOPS/TFLOPS |
|-----------|-------------|
| BF16 | 256 TFLOPS |
| FP8 | 512 TFLOPS |
| INT8 | 512 TOPS |
| INT4 | 1024 TOPS |

**Throughput:** 2,000-3,000 tokens/sec on 10B parameter models (varies by context length).

---

## Technical architecture

**Tensor Contraction Processor (TCP):**

RNGD uses tensor contraction as primary operation rather than matrix multiplication — claims >99% of FLOPS in BERT-class workloads map to this primitive.

| Component | Details |
|-----------|---------|
| Processing Elements | 8 PEs per chip |
| Slices per PE | 64 (each with compute pipeline + SRAM) |
| Fusion | PEs can fuse (up to 4) for larger workloads |
| Data flow | Systolic array — data flows through compute, minimal memory traffic |

**Why this matters for power:**
- Traditional chips (Von Neumann): fetch → compute → store → repeat
- RNGD: data flows through compute units, gets reused at each stage
- Moving data costs more energy than computation — minimizing movement = efficiency

**Hot Chips 2024:** Presented RNGD running Meta's Llama with 3x better performance per watt vs NVIDIA H100.

---

## Founder: June Paik

| Background | Detail |
|------------|--------|
| Education | Seoul National → UC Berkeley → Georgia Tech |
| [[Samsung]] | Memory chip engineer, led new product team |
| [[AMD]] | GPU design experience |
| Origin story | Soccer injury → months in bed → studied AI end-to-end → realized power would be the ceiling |

**Co-founder:** Hanjoon Kim (CTO) — also ex-Samsung.

**Philosophy:** "Blitzscaling" approach — fast decisions, risk-taking, long-term mission over short-term security.

**Hot Chips 2024 keynote:** Paik debuted RNGD as solution for "sustainable AI computing" — framing inference efficiency as existential for AI scaling.

---

## Customers and partnerships

| Customer/Partner | Status | Details |
|------------------|--------|---------|
| **[[LG]] AI Research** | **Design win** (Jul 2025) | 7-month evaluation → commercial deal. Running EXAONE foundation models. 2.25x better perf/watt vs GPUs. |
| [[OpenAI]] | Demo partner (Sep 2025) | "Sustainable enterprise AI" demo in Seoul |
| ByteBridge | Partnership (Oct 2025) | AI infrastructure transformation in Asia-Pacific |
| CMC Korea | Partnership (Aug 2025) | AI solutions development in Vietnam |
| Kakao | Early customer | First-gen NPU for computer vision |
| Meta | Acquisition rejected | $800M offer (Mar 2025), declined |

**LG deal significance:** "One of the first major on-premises enterprise adoptions of inference hardware from a semiconductor startup." Targets electronics, finance, telecom, biotech.

---

## Investment angle

**Inference vs training:**

| Market | Dominant player | Furiosa position |
|--------|-----------------|------------------|
| Training | [[NVIDIA]] (GPUs) | Not competing |
| Inference | NVIDIA + others | Target market |

**Why inference matters:** Training happens once. Inference (using models) happens billions of times. Power efficiency = cost savings at scale.

---

## Competitive landscape

| Company | Type | Status (Jan 2026) |
|---------|------|--------|
| [[NVIDIA]] | GPU incumbent | Dominant — acquired [[Groq]] assets (Dec 2025) |
| [[Groq]] | LPU (inference) | **Acquired by NVIDIA** ($20B, Dec 2025) |
| [[Cerebras]] | Wafer-scale | Training focus, shipping |
| [[Tenstorrent]] | RISC-V AI | Early, Jim Keller credibility |
| **FuriosaAI** | **NPU (inference)** | **Mass production started Jan 2026** |
| [[Ascend]] (Huawei) | China domestic | Sanctioned, [[SMIC]] fab limits |

**Post-Groq landscape:** With NVIDIA absorbing Groq's IP and key engineers (including founder Jonathan Ross), FuriosaAI becomes one of few remaining independent inference chip startups at scale. [[Cerebras]] focuses more on training; [[Tenstorrent]] is earlier stage.

---

## South Korea AI ecosystem

**Government push:**

- AI as national priority
- [[OpenAI]] opened Seoul office
- [[NVIDIA]] signed government GPU deal
- Talent pool from [[Samsung]], [[SK Hynix]]

**Furiosa advantage:** Korean semi expertise + startup agility.

---

## Bull case

- **2-3x power efficiency** = real cost savings at scale
- **[[Groq]] absorbed by NVIDIA** = one less independent competitor
- **LG commercial deal** validates technology in production
- Inference market growing faster than training (training once, inference billions of times)
- [[Power constraints]] make efficiency existential, not just nice-to-have
- South Korea talent pool ([[Samsung]], [[SK Hynix]]) + government support
- IPO path clear (targeting 2026-2027)

## Bear case

- NVIDIA's CUDA ecosystem moat still intact
- Scale risk — mass production just starting
- Customer adoption — enterprises slow to switch from NVIDIA
- Funding needs — competing vs NVIDIA requires deep pockets
- [[NVIDIA]] now has Groq's inference IP — will integrate into Rubin
- Single major customer ([[LG]]) — concentration risk

---

## Funding history

| Round | Date | Amount | Valuation |
|-------|------|--------|-----------|
| Seed | 2017 | <$1M | — |
| Series A | 2019 | $25M | — |
| Series B | 2021 | $80M | — |
| Series C | 2024 | — | ~$700M |
| **Series C Bridge** | **Jul 2025** | **$125M** | **$735M** |
| **Total** | | **$246M** | |

**Series D (targeting Jan 2026):**
- Seeking **$300-500M**
- Advisers: Morgan Stanley, Mirae Asset Securities
- Purpose: RNGD mass production, global expansion, 3rd-gen chip R&D
- IPO preparation underway

**Key investors:**

| Investor | Notes |
|----------|-------|
| Korea Development Bank | Government, Series C Bridge lead |
| Industrial Bank of Korea | Government |
| Keistone Partners | Series C Bridge |
| Kakao Investment | Strategic |
| SoftBank Ventures | Korean venture arm |
| [[SK Hynix]] | Strategic |
| IMM Investment | Korean VC |

**Meta acquisition attempt (Mar 2025):** Meta offered $800M. FuriosaAI declined — disagreements over post-acquisition business strategy and organizational structure, not price. Three months later signed LG as major customer, validating independence strategy.

*Updated 2026-01-22*

---

## Related

- [[NPU]] — technology category
- [[NVIDIA alternatives]] — competitive landscape
- [[NVIDIA]] — dominant competitor
- [[Groq]] — former peer (acquired by NVIDIA Dec 2025)
- [[Cerebras]], [[Tenstorrent]] — remaining independent peers
- [[Samsung]] — founder origin, Korean ecosystem
- [[SK Hynix]] — Korean ecosystem, strategic investor
- [[OpenAI]] — demo partner
- [[LG]] — major customer (EXAONE models)
- [[Power constraints]] — why efficiency matters
- [[Inference disaggregation]] — structural trend favoring specialized chips

