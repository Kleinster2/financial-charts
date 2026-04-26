---
aliases:
  - TPU
  - Tensor Processing Unit
  - Google TPU
  - TPU v5
  - TPU v5p
  - TPU v5e
tags:
  - product-family
  - semiconductor
  - ai-accelerator
parent_actor: "Google"
parent_concept: "AI accelerators"
---

# TPU

[[Google]]'s custom AI accelerator. Tensor Processing Unit. Powers [[Gemini]], Google Search, YouTube recommendations. Available via [[Google]] Cloud. Not sold as standalone hardware.

## Quick stats (TPU v5p)

| Metric | Value |
|--------|-------|
| Architecture | TPU v5p |
| HBM memory | 95GB per chip |
| Interconnect | ICI (Inter-Chip Interconnect) |
| BF16 performance | 459 TFLOPS per chip |
| Int8 performance | 918 TOPS per chip |
| Pod size | Up to 8,960 chips |
| Announced | December 2023 (Cloud Next) |
| Availability | Google Cloud only |

---

## Version history

| Version | Release | Key changes |
|---------|---------|-------------|
| TPU v1 | 2016 | Inference only, 8-bit integers |
| TPU v2 | 2017 | Training + inference, HBM, 180 TFLOPS |
| TPU v3 | 2018 | Liquid cooling, 420 TFLOPS |
| **TPU v4** | 2021 | 4,096-chip pods, 275 TFLOPS BF16 |
| TPU v5e | 2023 | Cost-optimized, inference focus |
| TPU v5p | 2023 | Performance flagship, 459 TFLOPS |
| TPU v6 (Trillium) | 2024 | 4.7x v5e performance |
| TPU v7 | Late 2025 | Reached ~94% of [[NVIDIA]] GB200 BF16 TFLOPS (first TPU at NVIDIA parity) |
| **TPU 8t** (8th gen, training) | Unveiled Apr 22, 2026 (Cloud Next 2026, Las Vegas) | Specialised for training AI models |
| **TPU 8i** (8th gen, inference) | Unveiled Apr 22, 2026 (Cloud Next 2026, Las Vegas) | More memory to run AI systems faster — designed for inference at scale, the agentic-era split |

---

## TPU v5 variants

| Variant | Focus | Use case |
|---------|-------|----------|
| TPU v5p | Performance | Large model training |
| TPU v5e | Efficiency | Inference, cost-sensitive training |

v5p for frontier model training, v5e for deployment at scale.

---

## TPU v5p vs competitors

| Spec | TPU v5p | H100 | MI300X |
|------|---------|------|--------|
| HBM | 95GB | 80GB | 192GB |
| BF16 | 459 TFLOPS | 1,979 TFLOPS | 1,307 TFLOPS |
| Availability | GCP only | Universal | Growing |
| Interconnect | ICI | NVLink | Infinity Fabric |
| Software | JAX/TensorFlow | CUDA | ROCm |

Note: TPU TFLOPS not directly comparable — different architecture optimized for different operations.

---

## Architecture

| Feature | Description |
|---------|-------------|
| MXU | Matrix Multiply Unit (systolic array) |
| VPU | Vector Processing Unit |
| SparseCore | Sparse tensor acceleration |
| ICI | Custom chip-to-chip interconnect |
| Pod architecture | Tightly coupled multi-chip systems |

Systolic array: TPUs use systolic arrays for matrix ops — different from GPU SIMT model. Highly efficient for specific workloads.

---

## Software stack

| Component | Status |
|-----------|--------|
| JAX | Primary framework (Google-developed) |
| TensorFlow | Native support |
| PyTorch | PyTorch/XLA (works but JAX preferred) |
| Hugging Face | Supported via Optimum-TPU |
| FLAX | JAX-based neural net library |

JAX advantage: Google's JAX framework designed for TPUs. Best performance on TPU requires JAX.

---

## What TPUs power

| Product | TPU usage |
|---------|-----------|
| [[Gemini]] | Training and inference |
| Google Search | Ranking, AI Overviews |
| YouTube | Recommendations |
| Google Translate | Neural MT |
| Gmail | Smart Compose, spam |
| Google Photos | Search, memories |

Nearly all Google AI runs on TPUs internally.

---

## Cloud availability

| Offering | Description |
|----------|-------------|
| Cloud TPU | On-demand TPU VMs |
| TPU Pods | Multi-chip configurations |
| Vertex AI | Managed ML with TPU backend |
| GKE | Kubernetes with TPU nodes |

Pricing (v5e): ~$1.20/chip/hour on-demand, ~$0.80 spot.

---

## Competitive position

| vs | TPU advantage | TPU disadvantage |
|----|---------------|------------------|
| [[H100]] | Tight integration, pod scale | GCP-only, less flexible |
| [[MI300X]] | Software maturity | GCP-only |
| [[Gaudi]] | Scale, proven at Google | GCP-only |
| [[Trainium]] | More workload types | Trainium cheaper on AWS |

Key limitation: TPUs only available on Google Cloud. No on-premise, no other clouds.

---

## Apr 22, 2026: 8th-gen unveiling at Cloud Next 2026, Las Vegas

At Google Cloud Next 2026 in Las Vegas (Apr 22 2026), [[Google Cloud]] unveiled the 8th generation of the TPU line as two distinct chips:

- **TPU 8t** — training-optimised, the successor to TPU v7 ("Ironwood") at the frontier-training tier.
- **TPU 8i** — inference-optimised with more memory, designed for the agentic-era inference workload.

The split-purpose design tracks the broader industry move from a single all-purpose chip toward dedicated training-vs-inference silicon (see [[Training-inference convergence]]).

### Customer roster as named at Cloud Next 2026

[[Google Cloud]] CEO [[Thomas Kurian]] said nine of the top ten AI labs use TPUs. The publicly named or publicly disclosed customer set as of Apr 2026:

| Customer | Status |
|---|---|
| [[Anthropic]] | Largest external TPU customer; Apr 2026 deal expanded to "up to one million TPUs" plus 5 GW Google Cloud capacity over 5 years |
| [[Apple]] | Apple Intelligence training partly on TPU (publicly disclosed) |
| [[Meta]] | Multibillion-dollar multiyear deal signed Feb 2026 |
| [[OpenAI]] | Now taking TPU capacity in 2026 (despite [[Microsoft]] cloud relationship) |
| [[Safe Superintelligence]] | Named at Cloud Next 2026 |
| [[Thinking Machines Lab]] | Named by Kurian in [[FT]] interview |
| [[Midjourney]] | Named at Cloud Next 2026 |
| [[Salesforce]] | Named at Cloud Next 2026 |
| [[Figma]] | Named at Cloud Next 2026 |
| [[Palo Alto Networks]] | Named at Cloud Next 2026 |
| [[Cursor]] | Named at Cloud Next 2026 |
| [[Citadel Securities]] | Quant research workflows on TPU |
| All 17 [[US]] DoE national labs | AI co-scientist software on TPU |

Kurian said only [[NVIDIA]] currently rivals Google's combination of integrated AI hardware and software at frontier scale.

### Huang counter and the data fight

[[NVIDIA]] CEO [[Jensen Huang]] criticised Google for not submitting TPUs to independent benchmark tests, and claimed "100 per cent" of TPU demand comes from [[Anthropic]]. The Cloud Next 2026 customer roster directly contradicts the "100% Anthropic" framing — [[Apple]], [[Meta]], [[OpenAI]], [[Safe Superintelligence]], [[Thinking Machines Lab]], [[Midjourney]], [[Salesforce]], [[Figma]], [[Palo Alto Networks]], and [[Cursor]] are all separately disclosed.

Huang's narrower point on independent benchmarking remains live: TPU 8t / 8i have not yet been submitted to MLPerf. The chip-spec dispute is real even when the customer-share dispute is resolved.

According to an [[Epoch AI]] estimate cited by [[FT]] (Apr 2026), Google now controls roughly 25% of global AI computing power — about 3.8M TPUs and about 1.3M GPUs — versus [[Microsoft]]'s ~3.2M [[NVIDIA]] GPUs.

*Sources: FT, Apr 26 2026; Google Cloud Next 2026 keynote, Apr 22 2026; CNBC, TechCrunch, Digitimes (Apr 22-23 2026); SemiAnalysis on TPUv7→8 lineage.*

---

## Anthropic as external anchor tenant (2026)

[[Anthropic]] is the cleanest external validation of [[Google]]'s TPU strategy. The Apr 6 2026 Google + [[Broadcom]] agreement gave Anthropic multiple gigawatts of next-generation TPU capacity starting in 2027, later reported at about 3.5 GW. The Apr 24 2026 financing package added a reported 5 GW Google Cloud capacity layer over five years, alongside Google's $10B upfront / up to $40B total equity commitment to Anthropic.

The read-through is two-sided. TPUs are now credible enough for a non-Google frontier lab to run material workloads at multi-GW scale. But capacity sold to Anthropic is also capacity not available to [[Gemini]], exposing the internal tension between Google Cloud's platform business and Google DeepMind's model competition.

See [[Anthropic hyperscaler financing surge April 2026]] and [[Anthropic vs OpenAI compute race]].

---

## Strategic significance

| Aspect | Implication |
|--------|-------------|
| Vertical integration | Google controls full stack |
| NVIDIA independence | Reduces reliance on external supply |
| Cloud differentiation | Unique GCP capability |
| Cost structure | Lower marginal cost than buying GPUs |

Google is least dependent on NVIDIA among hyperscalers due to TPU investment.

---

## Related

- [[Google]] — parent actor
- [[AI accelerators]] — parent concept
- [[Gemini]] — powered by TPU
- [[H100]] — competitor (NVIDIA)
- [[MI300X]] — competitor (AMD)
- [[Trainium]] — AWS equivalent
- [[Gaudi]] — Intel competitor
- [[Vertex]] — Google Cloud ML platform
