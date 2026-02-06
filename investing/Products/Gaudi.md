---
aliases:
  - Gaudi
  - Gaudi 2
  - Gaudi 3
  - Intel Gaudi
  - Habana Gaudi
tags:
  - product
  - semiconductor
  - ai-accelerator
parent_actor: "[[Intel]]"
parent_concept: "[[AI accelerators]]"
---

# Gaudi

[[Intel]]'s AI accelerator family. Acquired via Habana Labs (2019, $2B). Positioned as cost-effective alternative to [[NVIDIA]]. Gaudi 3 launched 2024.

## Quick stats (Gaudi 3)

| Metric | Value |
|--------|-------|
| Architecture | Gaudi 3 |
| Process | TSMC 5nm |
| HBM2e memory | 128GB |
| Memory bandwidth | 3.7 TB/s |
| TDP | 600W |
| BF16 performance | 1,835 TFLOPS |
| FP8 performance | 3,670 TFLOPS |
| Announced | April 2024 (Intel Vision) |
| Volume | H2 2024 |

---

## Version history

| Model | Release | Key specs |
|-------|---------|-----------|
| **Gaudi** | 2019 | First-gen, Habana design |
| **Gaudi 2** | 2022 | 96GB HBM2e, 2.45 TB/s |
| **Gaudi 3** | 2024 | 128GB HBM2e, 3.7 TB/s, 5nm |
| Falcon Shores | 2025 | Next-gen (x86 + accelerator fusion) |

---

## Gaudi 3 vs competitors

| Spec | Gaudi 3 | H100 | MI300X |
|------|---------|------|--------|
| HBM | 128GB | 80GB | 192GB |
| Bandwidth | 3.7 TB/s | 3.35 TB/s | 5.3 TB/s |
| FP8 | 3,670 TFLOPS | 3,958 TFLOPS | 2,614 TFLOPS |
| TDP | 600W | 700W | 750W |
| Process | 5nm | 4nm | 5nm |

**Intel's pitch:** Competitive FP8, lower power, open software stack.

---

## Gaudi 2 specs

| Metric | Value |
|--------|-------|
| Process | TSMC 7nm |
| HBM2e memory | 96GB |
| Memory bandwidth | 2.45 TB/s |
| TDP | 600W |
| BF16 performance | 865 TFLOPS |

Gaudi 2 found adoption at AWS (EC2 DL1 instances) before Gaudi 3 launch.

---

## Architecture

| Feature | Description |
|---------|-------------|
| Matrix engines | Dedicated tensor compute units |
| GEMM engines | High-throughput matrix multiply |
| TPC cores | Programmable tensor processor cores |
| RoCE networking | RDMA over Converged Ethernet |
| Scale-out | Native multi-chip networking |

**Different approach:** Gaudi uses Ethernet-based scale-out (RoCE) vs NVIDIA's proprietary NVLink. More standard, potentially lower cost.

---

## Software stack

| Component | Status |
|-----------|--------|
| PyTorch | Supported (Intel fork) |
| Hugging Face | Optimum-Habana integration |
| DeepSpeed | Supported |
| vLLM | Supported |
| LangChain | Supported |

**Habana SynapseAI:** Intel's SDK for Gaudi. More open than CUDA but smaller ecosystem.

---

## Customer deployments

| Customer | Deployment |
|----------|------------|
| [[Amazon]] AWS | EC2 DL1 (Gaudi), DL2 (Gaudi 2) |
| [[IBM]] | Cloud instances |
| [[Dell]] | PowerEdge servers |
| [[HPE]] | ProLiant servers |
| [[Supermicro]] | Server integration |

AWS was early Gaudi adopter — notable given Amazon's own Trainium chips.

---

## Challenges

| Issue | Impact |
|-------|--------|
| Market share | <5% of AI accelerator market |
| Software ecosystem | Smaller than CUDA, ROCm |
| Intel execution | Delayed roadmaps, restructuring |
| Competition | NVIDIA dominant, AMD growing |
| Falcon Shores delay | Originally 2024, pushed to 2025 |

Intel has struggled to gain traction despite competitive specs.

---

## Habana Labs acquisition

| Metric | Value |
|--------|-------|
| Acquired | December 2019 |
| Price | $2B |
| HQ | Israel |
| Founder | Avigdor Willenz (also Galileo, Marvell Semiconductor) |
| Rationale | AI accelerator capability |

Intel's AI accelerator strategy built on Habana acquisition.

---

## Related

- [[Intel]] — parent actor
- [[AI accelerators]] — parent concept
- [[H100]] — primary competitor
- [[MI300X]] — AMD competitor
- [[Trainium]] — AWS custom silicon
- [[TPU]] — Google custom silicon
- [[HBM]] — memory technology
