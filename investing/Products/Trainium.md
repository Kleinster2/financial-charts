---
aliases:
  - Trainium
  - Trainium2
  - AWS Trainium
  - Trn1
  - Trn2
tags:
  - product-family
  - semiconductor
  - ai-accelerator
parent_actor: "[[Amazon]]"
parent_concept: "[[AI accelerators]]"
---

# Trainium

[[Amazon]] AWS's custom AI training chip. Developed by Annapurna Labs (acquired 2015). Positioned as cost-effective NVIDIA alternative. Trainium2 launched 2024.

## Quick stats (Trainium2)

| Metric | Value |
|--------|-------|
| Architecture | Trainium2 |
| Process | Undisclosed (likely TSMC 3/5nm) |
| HBM memory | 96GB per chip |
| Memory bandwidth | 2.8 TB/s |
| Interconnect | NeuronLink (custom) |
| Performance | 4x Trainium1 |
| Announced | November 2023 (re:Invent) |
| Instances | Trn2 (EC2) |

---

## Version history

| Model | Release | Key specs |
|-------|---------|-----------|
| Inferentia | 2019 | Inference-only chip |
| **Trainium** | 2022 | First training chip, 32GB HBM |
| Inferentia2 | 2023 | 2nd-gen inference |
| **Trainium2** | 2024 | 4x performance, 96GB HBM |
| Trainium3 | 2025+ | Announced, details TBD |

---

## Trainium2 vs competitors

| Spec | Trainium2 | H100 | TPU v5p |
|------|-----------|------|---------|
| HBM | 96GB | 80GB | 95GB |
| Bandwidth | 2.8 TB/s | 3.35 TB/s | — |
| Availability | AWS only | Universal | GCP only |
| Interconnect | NeuronLink | NVLink | ICI |
| Software | Neuron SDK | CUDA | JAX |

---

## EC2 instances

| Instance | Chip | Use case |
|----------|------|----------|
| Trn1 | Trainium | Training |
| Trn1n | Trainium (network optimized) | Distributed training |
| Trn2 | Trainium2 | Large-scale training |
| Inf1 | Inferentia | Inference |
| Inf2 | Inferentia2 | Inference |

**Trn1.32xlarge:** 16 Trainium chips, 512GB memory, $21.50/hour on-demand.

---

## UltraClusters

| Cluster | Scale | Customer |
|---------|-------|----------|
| UltraCluster | 100,000+ Trainium2 chips | [[Anthropic]] |
| Project Rainier | Largest Trainium2 deployment | [[Anthropic]] |

[[Anthropic]] is anchor customer — committed to massive Trainium2 deployment for future Claude models.

---

## Software stack (Neuron SDK)

| Component | Status |
|-----------|--------|
| PyTorch | Supported (torch-neuronx) |
| TensorFlow | Supported |
| JAX | Supported |
| Hugging Face | Optimum-Neuron integration |
| Megatron-LM | Supported |
| vLLM | Supported |

**Neuron Compiler:** Ahead-of-time compilation for Trainium. Requires model conversion but enables optimization.

---

## Anthropic partnership

| Aspect | Details |
|--------|---------|
| Announced | November 2023 |
| Investment | Part of Amazon's $4B in Anthropic |
| Commitment | Anthropic primary cloud partner |
| Deployment | Project Rainier UltraCluster |
| Models | Future Claude training on Trainium |

Amazon's largest AI chip customer commitment. Validates Trainium for frontier model training.

---

## Cost advantage

| Comparison | Trainium vs NVIDIA |
|------------|-------------------|
| Price/performance | Up to 50% better (AWS claims) |
| Trn1 vs P4d (A100) | ~30-50% lower cost |
| Trn2 vs P5 (H100) | TBD |

AWS prices Trainium aggressively to drive adoption.

---

## Challenges

| Issue | Impact |
|-------|--------|
| Software maturity | Neuron SDK less mature than CUDA |
| Model support | Not all architectures optimized |
| AWS-only | No on-premise, no other clouds |
| Ecosystem | Smaller developer community |
| Porting effort | Models need Neuron compilation |

Similar challenges to TPU — proprietary, cloud-locked, software friction.

---

## Annapurna Labs

| Metric | Value |
|--------|-------|
| Acquired | 2015 |
| Price | $350M |
| HQ | Israel |
| Founder | Avigdor Willenz (also Habana/Gaudi) |
| Products | Graviton, Trainium, Inferentia, Nitro |

Same founder as Habana Labs (Intel Gaudi). Annapurna powers all AWS custom silicon.

---

## Strategic significance

| Aspect | Implication |
|--------|-------------|
| NVIDIA hedge | Reduces AWS dependence on external supply |
| Cost structure | Lower marginal cost than reselling GPUs |
| Differentiation | Unique AWS capability |
| Anthropic lock-in | Key AI partner on AWS silicon |

AWS following Google's TPU playbook — vertical integration for AI.

---

## Related

- [[Amazon]] — parent actor
- [[AI accelerators]] — parent concept
- [[Anthropic]] — anchor customer (Project Rainier)
- [[H100]] — competitor (NVIDIA)
- [[TPU]] — Google equivalent
- [[Gaudi]] — Intel competitor (same founder heritage)
- [[MI300X]] — AMD competitor
