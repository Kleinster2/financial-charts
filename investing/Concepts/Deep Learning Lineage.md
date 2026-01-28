---
aliases: [AI architecture history, Deep learning history, Neural network evolution]
---
#concept #ai #history

**Deep Learning Lineage** — The architectural evolution from [[AlexNet]] (2012) to modern LLMs. Each breakthrough solved a specific problem and enabled the next.

---

## The timeline

| Year | Architecture | Key innovation | Impact |
|------|--------------|----------------|--------|
| 2012 | [[AlexNet]] | Deep CNNs + GPUs | Proved deep learning works |
| 2014 | VGGNet | Deeper, simpler (19 layers) | Standardized design |
| 2014 | GoogLeNet | Inception modules | Efficient depth |
| 2015 | [[ResNet]] | Skip connections (152 layers) | Solved vanishing gradients |
| 2017 | [[Transformer]] | Self-attention | Parallelization, scaling |
| 2018 | BERT | Bidirectional pretraining | Language understanding |
| 2018 | GPT | Generative pretraining | Text generation |
| 2020 | GPT-3 | Scale (175B params) | Few-shot learning |
| 2022 | [[ChatGPT]] | RLHF | Conversational AI |
| 2023+ | GPT-4, [[Claude]], etc. | Multimodal, reasoning | Current frontier |

---

## Three eras

### Era 1: Vision (2012-2016)
**Problem:** Can neural networks recognize images?

| Architecture | Layers | ImageNet error |
|--------------|--------|----------------|
| [[AlexNet]] | 8 | 15.3% |
| VGGNet | 19 | 7.3% |
| GoogLeNet | 22 | 6.7% |
| [[ResNet]] | 152 | **3.6%** (superhuman) |

**Ended when:** AI exceeded human performance on ImageNet (2015).

### Era 2: Language (2017-2022)
**Problem:** Can neural networks understand and generate language?

| Model | Type | Innovation |
|-------|------|------------|
| [[Transformer]] | Architecture | Attention mechanism |
| BERT | Encoder | Bidirectional understanding |
| GPT-2 | Decoder | Scale (1.5B) |
| GPT-3 | Decoder | Scale (175B), few-shot |
| [[ChatGPT]] | Application | RLHF, conversation |

**Ended when:** ChatGPT proved consumer AI viable (Nov 2022).

### Era 3: General AI (2023+)
**Problem:** Can AI reason, see, act?

| Capability | Models |
|------------|--------|
| Multimodal | GPT-4V, [[Gemini]], [[Claude]] |
| Reasoning | o1, [[DeepSeek]] R1, [[Qwen]] |
| Agents | Claude Code, Devin, Manus |
| [[World Models]] | [[World Labs]], Genie |

**Current frontier:** Spatial intelligence, embodied AI, AGI.

---

## The key breakthroughs

### 1. Data ([[ImageNet]], 2009)
**Insight:** AI needs massive labeled datasets, not just better algorithms.
**Who:** [[Fei-Fei Li]]
**Impact:** Enabled training deep networks

### 2. Depth ([[AlexNet]], 2012)
**Insight:** Deep networks + GPUs can solve vision.
**Who:** Krizhevsky, [[Ilya Sutskever]], [[Geoffrey Hinton]]
**Impact:** Proved deep learning works

### 3. Very Deep Networks ([[ResNet]], 2015)
**Insight:** Skip connections solve vanishing gradients.
**Who:** Kaiming He ([[Microsoft]])
**Impact:** Enabled 100+ layer networks

### 4. Attention ([[Transformer]], 2017)
**Insight:** Attention mechanism enables parallelization and scaling.
**Who:** Vaswani et al. ([[Google]])
**Impact:** Foundation of all modern LLMs

### 5. Scale (GPT-3, 2020)
**Insight:** Bigger models + more data = emergent capabilities.
**Who:** [[OpenAI]]
**Impact:** Scaling laws, few-shot learning

### 6. Alignment ([[ChatGPT]], 2022)
**Insight:** RLHF makes models useful and safe.
**Who:** [[OpenAI]]
**Impact:** [[Consumer AI]] products

---

## Hardware co-evolution

| Year | AI milestone | Hardware |
|------|--------------|----------|
| 2012 | [[AlexNet]] | 2× GTX 580 (bedroom) |
| 2017 | [[Transformer]] | TPU pods |
| 2020 | GPT-3 | Thousands of V100s |
| 2023 | GPT-4 | ~25,000 A100s |
| 2024 | Frontier models | H100 clusters |
| 2025+ | Next generation | Blackwell, custom ASICs |

**[[NVIDIA]]'s rise tracks this lineage exactly.**

---

## Key figures

| Person | Contribution | Affiliation |
|--------|--------------|-------------|
| [[Fei-Fei Li]] | [[ImageNet]] | [[Stanford]], [[World Labs]] |
| [[Geoffrey Hinton]] | [[AlexNet]] advisor, backprop | Toronto, [[Google]] |
| [[Ilya Sutskever]] | [[AlexNet]], GPT | Toronto, [[OpenAI]], [[SSI]] |
| [[Yann LeCun]] | CNNs, early deep learning | NYU, [[Meta]] |
| Kaiming He | [[ResNet]] | [[Microsoft]], Meta |
| Ashish Vaswani | [[Transformer]] | [[Google]], Essential AI |
| [[Yang Zhilin]] | Transformer-XL | CMU, [[Moonshot AI]] |

---

## Investment implications

**The pattern:** Each breakthrough created massive value:
- [[AlexNet]] → [[Google]] acquires DNNresearch
- [[Transformer]] → 6+ unicorns from 8 authors
- GPT-3/ChatGPT → [[OpenAI]] $300B valuation

**Current bets on next breakthrough:**
- [[World Models]] (spatial intelligence)
- Efficient architectures (Mamba, [[DeepSeek]])
- [[Agentic AI]] (tool use, coding)

---

## Quick stats

| Era | Years | Key architecture |
|-----|-------|------------------|
| Vision | 2012-2016 | CNNs ([[AlexNet]] → [[ResNet]]) |
| Language | 2017-2022 | [[Transformer]] → [[ChatGPT]] |
| General AI | 2023+ | Multimodal, reasoning, agents |

*Created 2026-01-27*

---

## Related

- [[ImageNet]] — data breakthrough
- [[AlexNet]] — first deep learning success
- [[ResNet]] — depth breakthrough
- [[Transformer]] — attention breakthrough
- [[ChatGPT]] — consumer AI breakthrough
- [[NVIDIA]] — hardware beneficiary
- [[Scaling laws]] — key insight
- [[World Models]] — next paradigm?
