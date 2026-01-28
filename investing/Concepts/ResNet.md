---
aliases: [Residual Network, ResNet-50, ResNet-152, Skip connections]
---
#concept #ai #architecture

**ResNet** — Microsoft's 2015 architecture that solved the "vanishing gradient" problem. Skip connections enabled 152-layer networks. Won ImageNet 2015 with **3.6% error** (superhuman). Foundation for modern deep networks.

---

## Why ResNet matters

| Metric | Value |
|--------|-------|
| Paper | "Deep Residual Learning" (2015) |
| Authors | Kaiming He et al. (Microsoft Research) |
| Depth | Up to **152 layers** (8× deeper than VGG) |
| ImageNet error | **3.6%** (superhuman ~5%) |
| Key innovation | Skip connections |

**Before ResNet:** Deeper networks performed worse (degradation problem).
**After ResNet:** Depth became a feature, not a bug.

---

## The problem ResNet solved

**Degradation problem:** Adding more layers to a network should improve performance. But in practice:

| Depth | Expected | Actual (pre-ResNet) |
|-------|----------|---------------------|
| 20 layers | Good | Good |
| 56 layers | Better | **Worse** |

**Why?** Vanishing gradients — signals get weaker as they backpropagate through many layers. Deep networks couldn't learn.

---

## The solution: Skip connections

Instead of learning `H(x)`, learn the **residual** `F(x) = H(x) - x`.

```
Input (x) ─────────────────────┐
    │                          │
    ▼                          │
[Conv → BN → ReLU → Conv → BN] │
    │                          │
    ▼                          │
    + ◄────────────────────────┘  (skip connection)
    │
    ▼
   ReLU
    │
    ▼
Output = F(x) + x
```

**Why it works:**
- Gradients flow directly through skip connections
- Network can learn identity mappings easily
- Each block only needs to learn small refinements

---

## The team

| Person | Role | Later |
|--------|------|-------|
| **Kaiming He** | Lead author | Facebook AI (FAIR) |
| Xiangyu Zhang | Co-author | Megvii |
| Shaoqing Ren | Co-author | Faster R-CNN author |
| Jian Sun | Co-author | Megvii co-founder |

**Microsoft Research Asia** — Beijing lab.

---

## Architecture variants

| Model | Layers | Parameters | Top-5 error |
|-------|--------|------------|-------------|
| ResNet-18 | 18 | 11M | 10.9% |
| ResNet-34 | 34 | 21M | 7.8% |
| **ResNet-50** | 50 | 25M | **6.7%** |
| ResNet-101 | 101 | 44M | 6.4% |
| ResNet-152 | 152 | 60M | **6.2%** |

**ResNet-50** became the standard backbone for computer vision.

---

## Competition dominance (2015)

| Task | Result |
|------|--------|
| ImageNet classification | **1st place** (3.6% error) |
| ImageNet detection | **1st place** |
| ImageNet localization | **1st place** |
| COCO detection | **1st place** (28% improvement) |
| COCO segmentation | **1st place** |

**Swept everything.** Skip connections were the key.

---

## Impact on AI

| Before ResNet | After ResNet |
|---------------|--------------|
| ~20 layers practical | 100+ layers practical |
| Depth was limited | Depth became a scaling axis |
| Careful architecture needed | Skip connections = default |

**Influence on Transformers:** Residual connections are a core component of the [[Transformer]] architecture (2017).

---

## Lineage position

| Year | Architecture | Layers | Innovation |
|------|--------------|--------|------------|
| 2012 | [[AlexNet]] | 8 | Deep CNNs work |
| 2014 | VGGNet | 19 | Deeper, simpler |
| 2014 | GoogLeNet | 22 | Inception modules |
| **2015** | **ResNet** | **152** | **Skip connections** |
| 2017 | [[Transformer]] | N/A | Attention (uses residuals) |

---

## Quick stats

| Metric | Value |
|--------|-------|
| Year | 2015 |
| Institution | Microsoft Research |
| Key innovation | Skip connections |
| Max depth | 152 layers |
| ImageNet error | 3.6% |
| Standard variant | ResNet-50 |

*Created 2026-01-27*

---

## Related

- [[AlexNet]] — predecessor (2012)
- [[ImageNet]] — benchmark
- [[Transformer]] — uses residual connections
- [[Microsoft]] — origin (MSR Asia)
- [[Kaiming He]] — lead author
