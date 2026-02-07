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
parent_actor: "[[Google]]"
parent_concept: "[[AI accelerators]]"
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
| **TPU v5p** | 2023 | Performance flagship, 459 TFLOPS |
| TPU v6 (Trillium) | 2024 | 4.7x v5e performance |

---

## TPU v5 variants

| Variant | Focus | Use case |
|---------|-------|----------|
| **TPU v5p** | Performance | Large model training |
| **TPU v5e** | Efficiency | Inference, cost-sensitive training |

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

**Note:** TPU TFLOPS not directly comparable — different architecture optimized for different operations.

---

## Architecture

| Feature | Description |
|---------|-------------|
| MXU | Matrix Multiply Unit (systolic array) |
| VPU | Vector Processing Unit |
| SparseCore | Sparse tensor acceleration |
| ICI | Custom chip-to-chip interconnect |
| Pod architecture | Tightly coupled multi-chip systems |

**Systolic array:** TPUs use systolic arrays for matrix ops — different from GPU SIMT model. Highly efficient for specific workloads.

---

## Software stack

| Component | Status |
|-----------|--------|
| JAX | Primary framework (Google-developed) |
| TensorFlow | Native support |
| PyTorch | PyTorch/XLA (works but JAX preferred) |
| Hugging Face | Supported via Optimum-TPU |
| FLAX | JAX-based neural net library |

**JAX advantage:** Google's JAX framework designed for TPUs. Best performance on TPU requires JAX.

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

**Pricing (v5e):** ~$1.20/chip/hour on-demand, ~$0.80 spot.

---

## Competitive position

| vs | TPU advantage | TPU disadvantage |
|----|---------------|------------------|
| [[H100]] | Tight integration, pod scale | GCP-only, less flexible |
| [[MI300X]] | Software maturity | GCP-only |
| [[Gaudi]] | Scale, proven at Google | GCP-only |
| [[Trainium]] | More workload types | Trainium cheaper on AWS |

**Key limitation:** TPUs only available on Google Cloud. No on-premise, no other clouds.

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
