---
aliases:
  - Ascend
  - Huawei Ascend
  - Ascend 910
  - Ascend 910B
  - Ascend 910C
  - Atlas
tags:
  - product
  - semiconductor
  - ai-accelerator
  - china
parent_actor: "[[Huawei]]"
parent_concept: "[[AI accelerators]]"
---

# Ascend

[[Huawei]]'s AI accelerator family. [[China]]'s primary domestic alternative to [[NVIDIA]]. Critical for Chinese AI labs facing [[Export controls]]. Ascend 910B/910C current generation.

## Quick stats (Ascend 910B)

| Metric | Value |
|--------|-------|
| Architecture | Da Vinci |
| Process | SMIC 7nm |
| HBM2e memory | 64GB |
| Memory bandwidth | 1.8 TB/s |
| FP16 performance | 320 TFLOPS |
| BF16 performance | 320 TFLOPS |
| TDP | 400W |
| Status | Volume production |

---

## Version history

| Model | Release | Key specs |
|-------|---------|-----------|
| Ascend 310 | 2018 | Inference chip, 8 TOPS INT8 |
| **Ascend 910** | 2019 | Training chip, 256 TFLOPS FP16 |
| Ascend 910A | 2021 | Incremental improvement |
| **Ascend 910B** | 2023 | SMIC 7nm, post-sanctions redesign |
| **Ascend 910C** | 2024 | Latest generation |
| Ascend 920 | 2025 | Next-gen (announced) |

---

## Ascend 910B vs competitors

| Spec | Ascend 910B | H100 | A100 |
|------|-------------|------|------|
| HBM | 64GB | 80GB | 80GB |
| Bandwidth | 1.8 TB/s | 3.35 TB/s | 2 TB/s |
| FP16 | 320 TFLOPS | 1,979 TFLOPS | 312 TFLOPS |
| Process | SMIC 7nm | TSMC 4nm | TSMC 7nm |
| Availability | China only | Restricted | Restricted |

**Reality check:** Ascend trails NVIDIA on specs but it's *available* in China. Availability beats performance when you can't buy the alternative.

---

## Strategic significance

| Factor | Implication |
|--------|-------------|
| [[Export controls]] | Only domestic option for Chinese AI labs |
| SMIC fabrication | Entirely domestic supply chain |
| National priority | Government-backed adoption |
| Huawei ecosystem | Cloud, servers, software stack |

Ascend is China's AI chip independence — imperfect but sovereign.

---

## Atlas product line

| Product | Configuration |
|---------|---------------|
| Atlas 800 | Training server (8x Ascend 910) |
| Atlas 800T A2 | Inference server |
| Atlas 900 | Training cluster (thousands of chips) |
| Atlas 300 | Inference card (PCIe) |

**Atlas 800T A2:** Used by [[Zhipu]] to train [[GLM]]-Image entirely on Huawei hardware.

---

## Software stack (CANN)

| Component | Status |
|-----------|--------|
| MindSpore | Huawei's ML framework |
| PyTorch | Supported via Ascend plugin |
| TensorFlow | Supported |
| CANN | Compute Architecture for Neural Networks |
| ModelArts | Huawei Cloud ML platform |

**MindSpore:** Huawei's open-source alternative to TensorFlow/PyTorch. Growing adoption in China.

---

## Major deployments

| Customer | Usage |
|----------|-------|
| [[Baidu]] | [[Ernie]] training |
| [[Alibaba]] | [[Qwen]] training |
| [[ByteDance]] | [[Doubao]] training |
| [[Zhipu]] | [[GLM]]-Image (Huawei-only) |
| [[iFlytek]] | Speech AI |
| Chinese government | Various agencies |

All major Chinese AI labs use Ascend alongside NVIDIA (where available).

---

## Manufacturing

| Aspect | Details |
|--------|---------|
| Foundry | [[SMIC]] |
| Process | 7nm (N+2) |
| Challenge | No EUV lithography |
| Yield | Lower than TSMC |
| Capacity | Constrained |

SMIC's 7nm uses multi-patterning DUV — works but less efficient than EUV. Huawei pays premium for domestic fabrication.

---

## Competitive position in China

| vs | Ascend advantage | Ascend disadvantage |
|----|------------------|---------------------|
| H100/H200 | Available, no restrictions | Performance gap |
| H20 (China) | More capable | H20 still NVIDIA |
| [[Cambricon]] | Scale, ecosystem | Cambricon growing |
| [[Biren]] | Production volume | Biren catching up |

Ascend leads Chinese domestic chips but faces growing local competition.

---

## Export control impact

| Timeline | Event |
|----------|-------|
| Oct 2022 | US bans advanced chip exports to China |
| 2023 | Huawei accelerates Ascend development |
| 2023 | Ascend 910B launches on SMIC 7nm |
| 2024 | Major Chinese labs adopt Ascend at scale |
| 2024 | [[Zhipu]] proves Huawei-only training viable |

Export controls accelerated Ascend adoption and development.

---

## Challenges

| Issue | Impact |
|-------|--------|
| Performance gap | 3-5x behind NVIDIA on raw specs |
| Software maturity | CANN/MindSpore less mature than CUDA |
| Yield/cost | SMIC 7nm more expensive |
| HBM supply | Relies on Samsung/SK Hynix |
| Interconnect | Trails NVLink in bandwidth |

Huawei closing gap but still behind NVIDIA's current generation.

---

## Related

- [[Huawei]] — parent actor
- [[AI accelerators]] — parent concept
- [[Export controls]] — why Ascend matters
- [[SMIC]] — foundry partner
- [[H100]] — restricted competitor
- [[Cambricon]] — Chinese competitor
- [[Biren]] — Chinese competitor
- [[GLM]] — trained on Ascend-only
- [[China]] — market context
