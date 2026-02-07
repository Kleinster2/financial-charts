---
aliases:
  - MLU
  - MLU370
  - MLU590
  - Siyuan
  - Machine Learning Unit
tags:
  - product
  - semiconductor
  - ai-accelerator
  - china
parent_actor: "[[Cambricon Technologies]]"
parent_concept: "[[AI accelerators]]"
---

# MLU

[[Cambricon Technologies]]' AI accelerator family. Machine Learning Unit. Second-largest domestic AI chip in [[China]] after [[Ascend]].

## Quick stats (MLU590)

| Metric | Value |
|--------|-------|
| Architecture | MLUarch03 |
| Process | TSMC 7nm |
| HBM2e memory | 96GB |
| Memory bandwidth | 2.0 TB/s |
| FP16 performance | 256 TFLOPS |
| INT8 performance | 1,024 TOPS |
| TDP | 450W |
| Launch | 2023 |

---

## Version history

| Model | Release | Key specs |
|-------|---------|-----------|
| MLU100 | 2018 | First chip, 128 TOPS INT8 |
| MLU270 | 2019 | 2nd-gen, 256 TOPS INT8 |
| **MLU370** | 2021 | Training capable, 48GB HBM2e |
| **MLU590** | 2023 | Flagship, 96GB HBM2e |
| Siyuan 370 | 2023 | Training accelerator card |
| Siyuan 590 | 2024 | Next-gen card |

---

## MLU590 vs competitors

| Spec | MLU590 | Ascend 910B | A100 |
|------|--------|-------------|------|
| HBM | 96GB | 64GB | 80GB |
| Bandwidth | 2.0 TB/s | 1.8 TB/s | 2.0 TB/s |
| FP16 | 256 TFLOPS | 320 TFLOPS | 312 TFLOPS |
| Process | TSMC 7nm | SMIC 7nm | TSMC 7nm |
| TDP | 450W | 400W | 400W |

Competitive with Ascend on specs. Key advantage: TSMC access (for now).

---

## Software stack (Neuware)

| Component | Status |
|-----------|--------|
| BANG C | Cambricon's programming language |
| Neuware SDK | Development toolkit |
| PyTorch | Supported via Catch |
| TensorFlow | Supported |
| MagicMind | Inference optimization |

**Smaller ecosystem:** Less mature than CUDA, CANN, or ROCm. Developer adoption is key challenge.

---

## Product line

| Product | Target |
|---------|--------|
| Siyuan cards | Data center accelerator cards |
| Edge AI chips | Edge inference |
| IP licensing | SoC integration |

Started with IP licensing (Huawei) before pivoting to standalone chips.

---

## Major deployments

| Customer | Usage |
|----------|-------|
| [[Baidu]] | Cloud AI instances |
| [[Alibaba]] | Cloud deployment |
| Lenovo | Server integration |
| Inspur | Server integration |
| Government | Smart city, surveillance |

Cambricon has presence in Chinese cloud providers alongside Ascend.

---

## Competitive position

| vs | Cambricon advantage | Cambricon disadvantage |
|----|---------------------|------------------------|
| [[Ascend]] | TSMC access, pure AI focus | Smaller scale, less integration |
| [[Biren]] | More mature | Biren claims better specs |
| NVIDIA | Available domestically | Performance, ecosystem |
| [[Zhipu]] | Hardware not software | Zhipu uses Cambricon chips |

Second player in Chinese AI chips — benefits from domestic preference but trails Huawei's scale.

---

## Risks

| Risk | Details |
|------|---------|
| [[TSMC]] access | Could lose foundry under tighter [[Export controls]] |
| Software ecosystem | Neuware less mature than CUDA, CANN |
| [[Ascend]] competition | Huawei scaling aggressively |

TSMC dependency is key vulnerability.

---

## Related

- [[Cambricon Technologies]] — parent actor
- [[AI accelerators]] — parent concept
- [[Ascend]] — primary domestic competitor
- [[Biren]] — domestic competitor
- [[Export controls]] — risk factor
- [[TSMC]] — current foundry (risk)
- [[SMIC]] — potential fallback foundry
- [[China]] — market context
