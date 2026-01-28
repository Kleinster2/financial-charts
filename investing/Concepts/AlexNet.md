---
aliases: [Alex Krizhevsky, AlexNet 2012]
---
#concept #ai #architecture #history

**AlexNet** — The model that proved deep learning works. Won ImageNet 2012 by 10+ points. Trained on 2 GPUs in a bedroom. Triggered the modern AI revolution.

---

## Why AlexNet matters

| Metric | Value |
|--------|-------|
| Event | ILSVRC 2012 (ImageNet Challenge) |
| Error rate | **15.3%** (vs 26.2% second place) |
| Margin | **10.9 points** |
| Hardware | 2× NVIDIA GTX 580 |
| Training location | Krizhevsky's bedroom |
| Impact | Launched deep learning era |

**Before AlexNet:** AI winter, skepticism about neural networks.
**After AlexNet:** Google, Facebook, everyone pivots to deep learning.

---

## The team

| Person | Role | Later |
|--------|------|-------|
| **Alex Krizhevsky** | Lead author, architect | Google |
| **[[Ilya Sutskever]]** | Co-author | [[OpenAI]] co-founder/Chief Scientist |
| **[[Geoffrey Hinton]]** | Advisor | "Godfather of AI," Nobel Prize 2024 |

**University of Toronto** — Hinton's lab.

---

## Architecture innovations

| Innovation | Impact |
|------------|--------|
| **ReLU activation** | Faster training than sigmoid/tanh |
| **Dropout** | Regularization, reduced overfitting |
| **GPU training** | Parallelized convolutions |
| **Data augmentation** | More effective training data |
| **Local response normalization** | (Later superseded) |

### Network structure

```
Input (224×224×3)
→ Conv1 (96 filters) → ReLU → Pool → LRN
→ Conv2 (256 filters) → ReLU → Pool → LRN
→ Conv3 (384 filters) → ReLU
→ Conv4 (384 filters) → ReLU
→ Conv5 (256 filters) → ReLU → Pool
→ FC6 (4096) → Dropout → ReLU
→ FC7 (4096) → Dropout → ReLU
→ FC8 (1000 classes) → Softmax
```

**60 million parameters** — massive for 2012.

---

## The three elements

[[Fei-Fei Li]]: "Three fundamental elements of modern AI converged for the first time."

| Element | Contribution |
|---------|--------------|
| **[[ImageNet]]** | 1.2M labeled training images |
| **GPUs** | NVIDIA CUDA enabled parallel training |
| **Deep learning** | CNNs could finally be trained at scale |

---

## Why it was surprising

| Expectation | Reality |
|-------------|---------|
| "Neural nets don't scale" | AlexNet scaled |
| "Need hand-crafted features" | Learned features won |
| "Deep networks can't train" | GPUs + ReLU + dropout made it work |

**The AI community was shocked.** Traditional computer vision researchers had spent decades on hand-engineered features. A neural network trained end-to-end crushed them.

---

## Immediate aftermath

| Company | Response |
|---------|----------|
| **[[Google]]** | Acquired Hinton's DNNresearch (2013) |
| **Facebook** | Hired [[Yann LeCun]] to lead AI (2013) |
| **[[Baidu]]** | Hired [[Andrew Ng]] (2014) |
| **Everyone** | Pivoted to deep learning |

**NVIDIA stock:** Beginning of the AI-driven rise.

---

## Lineage

| Year | Model | vs AlexNet |
|------|-------|------------|
| 2012 | **AlexNet** | Baseline |
| 2013 | ZFNet | Refined AlexNet |
| 2014 | VGGNet | Deeper (19 layers) |
| 2014 | GoogLeNet | Inception modules |
| 2015 | [[ResNet]] | Skip connections (152 layers) |
| 2017 | [[Transformer]] | Attention replaces convolutions |

---

## Quick stats

| Metric | Value |
|--------|-------|
| Year | 2012 |
| Challenge | ImageNet ILSVRC |
| Error rate | 15.3% |
| Parameters | 60M |
| GPUs | 2× GTX 580 |
| Training time | ~6 days |

*Created 2026-01-27*

---

## Related

- [[ImageNet]] — dataset that enabled it
- [[Geoffrey Hinton]] — advisor ("Godfather of AI")
- [[Ilya Sutskever]] — co-author, [[OpenAI]] co-founder
- [[NVIDIA]] — GPUs enabled training
- [[ResNet]] — successor architecture
- [[Transformer]] — eventual successor paradigm
- [[Google]] — acquired Hinton's company
