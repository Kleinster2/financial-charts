---
aliases: [Neural Processing Unit, NPUs, inference chip, inference chips, inference accelerator]
---
#concept #ai #chips #hardware

**NPU (Neural Processing Unit)** — Purpose-built chips optimized for AI inference. [[Trade]] generality for efficiency: 2-4x better performance per watt than GPUs by minimizing data movement.

---

## Why NPUs matter

**The power constraint:** [[Power constraints]] are becoming binding. Training happens once; inference runs forever. At data center scale, inference power efficiency = operating cost.

| Chip type | Designed for | AI trade-off |
|-----------|--------------|--------------|
| **CPU** | Complex sequential logic | Terrible at parallel math |
| **GPU** | Massive parallel math (graphics) | General but power-hungry |
| **NPU** | Inference workloads specifically | Efficient but inflexible |

**The math:** Moving data costs more energy than computation. Modern AI workloads are memory-bound, not compute-bound. NPUs minimize data movement.

---

## How NPUs differ from GPUs

**Traditional architecture (Von Neumann):**
```
fetch data → compute → store result → repeat
```

This constant memory traffic dominates power consumption.

**NPU architecture (data flow):**
```
data flows through compute units → gets reused at each stage → minimal memory traffic
```

### Key techniques

| Technique | How it helps |
|-----------|--------------|
| **Systolic arrays** | Data pulses through compute units, reused at each step |
| **Large on-chip SRAM** | Keep weights/activations local, avoid [[HBM]] trips |
| **Tensor reorganization** | Hardware adapts to data patterns, not vice versa |
| **Lower clock speeds** | Power scales with frequency — trade speed for efficiency |
| **Specialized datapaths** | Fixed-function units for multiply-accumulate (MAC) |

### Systolic arrays explained

Named after the heart's systolic rhythm. Data flows through a grid of processing elements:
1. Input enters from edges
2. Each PE does multiply-accumulate (MAC) operation
3. Results flow to neighbors
4. Data gets reused multiple times before leaving chip

**Result:** Same computation, fraction of the memory accesses.

---

## Inference vs training

| Aspect | Training | Inference |
|--------|----------|-----------|
| Frequency | Once per model | Billions of times |
| Precision needed | High (FP32, BF16) | Lower (INT8, INT4 often fine) |
| Batch size | Large (maximize throughput) | Often small (latency matters) |
| Memory bandwidth | Critical (gradients, optimizer states) | Less critical |
| CUDA dependency | Essential (ecosystem) | Weaker (less framework-dependent) |
| Power sensitivity | Lower (one-time cost) | High (ongoing cost) |

**Implication:** [[CUDA moat]] is strongest in training. Inference is contestable — efficiency wins.

---

## NPU landscape (Jan 2026)

### Purpose-built inference chips

| Company | Chip | Approach | Status |
|---------|------|----------|--------|
| [[FuriosaAI]] | RNGD | Tensor contraction processor, 150W | Mass production Jan 2026 |
| [[Groq]] | LPU | SRAM-based, deterministic | **Acquired by [[NVIDIA]]** (Dec 2025) |
| Amazon | Inferentia 2 | AWS internal + cloud | Production |
| Google | TPU | Training + inference | Production (internal) |

### [[Consumer]] NPUs

| Company | Implementation | Use cases |
|---------|----------------|-----------|
| [[Apple]] | Neural Engine (in SoC) | Face ID, photos, Siri |
| [[Qualcomm]] | Hexagon NPU | On-device AI, always-on |
| [[Intel]] | NPU (in Core Ultra) | Windows AI features |
| [[AMD]] | XDNA (Ryzen AI) | Laptop AI acceleration |

**[[Consumer]] vs datacenter:** [[Consumer]] NPUs are small, low-power, integrated into SoC. Datacenter NPUs are standalone accelerators competing with GPUs.

### Hyperscaler custom silicon

| Company | Chip | Notes |
|---------|------|-------|
| [[Google]] | TPU v5e | Inference-optimized variant |
| [[Amazon]] | Inferentia 2 | 2x Inf1 throughput, 40% lower cost |
| [[Microsoft]] | Maia 100 | Azure, first in-house AI chip |
| [[Meta]] | MTIA | Internal inference |

---

## Power efficiency comparison

| Chip | TDP | Relative efficiency |
|------|-----|---------------------|
| [[NVIDIA]] H100 | 350W | Baseline |
| [[NVIDIA]] H100 PCIe | 350W | Baseline |
| FuriosaAI RNGD | **150W** | ~2-3x better perf/watt |
| Groq LPU | ~200W | ~2x better perf/watt |
| Amazon Inferentia 2 | ~175W | ~2x better perf/watt |

**At scale:** A 10MW data center with 2x better perf/watt effectively has 20MW of compute. Or same compute at half the power bill.

---

## The software challenge

**Why [[NVIDIA]] wins despite efficiency disadvantage:**

| Factor | [[NVIDIA]] advantage |
|--------|------------------|
| CUDA | 15+ years of libraries, optimization |
| Frameworks | PyTorch, TensorFlow deeply integrated |
| Developer familiarity | Millions trained on CUDA |
| Tooling | TensorRT, Triton, profilers |
| Ecosystem | Everything "just works" |

**How NPUs compete:**
- [[Target]] inference only (less CUDA-dependent)
- Offer massive cost savings (CFO > CTO)
- Open-source software stacks
- Focus on specific workloads (LLMs, vision)
- Work with cloud providers (abstraction layer)

---

## Investment implications

**Bull case for NPUs:**
- [[Power constraints]] make efficiency existential
- Inference market growing faster than training
- [[NVIDIA]] can't supply everyone
- Hyperscalers want supplier diversity
- Edge AI needs efficiency

**Bear case:**
- CUDA ecosystem moat is real
- [[NVIDIA]] keeps improving efficiency (Blackwell, Rubin)
- Most NPU startups unprofitable
- [[Groq]] absorbed by [[NVIDIA]] — consolidation pattern
- Switching costs remain high

**The [[Groq]] lesson:** [[NVIDIA]]'s $20B acquisition (Dec 2025) shows they take inference competition seriously. They'd rather absorb threats than compete.

---

## Key terms

| Term | Definition |
|------|------------|
| **MAC** | Multiply-accumulate: y = a*b + c. Core AI operation. |
| **Systolic array** | Compute grid where data flows rhythmically through PEs |
| **SRAM** | Fast on-chip memory (expensive, limited capacity) |
| **[[HBM]]** | High-bandwidth memory (slower than SRAM, more capacity) |
| **Tensor** | Multi-dimensional array — fundamental AI data structure |
| **Quantization** | Reducing precision (FP32 → INT8) to save compute/memory |
| **TDP** | Thermal design power — chip's power consumption target |

---

*Created 2026-01-22*

---

## Related

- [[FuriosaAI]] — Korean NPU startup (RNGD chip)
- [[Groq]] — LPU approach (acquired by [[NVIDIA]])
- [[NVIDIA alternatives]] — broader competitive landscape
- [[Power constraints]] — why efficiency matters
- [[Inference disaggregation]] — structural trend (prefill vs decode)
- [[AI ML primer]] — training vs inference fundamentals
- [[Semiconductor primer]] — chip manufacturing context
- [[Google]] — TPU pioneer
- [[Amazon]] — Inferentia, Trainium
