#concept #ai #ml #science #primer

**AI ML primer** — foundational machine learning and neural network concepts for AI investing. Understanding the technology helps evaluate compute requirements, scaling dynamics, and competitive moats.

> **Key insight:** Modern AI is fundamentally about scale. More data, more compute, more parameters → better performance. This "scaling law" drives the entire AI infrastructure buildout and explains why hyperscalers are spending $200B+ annually on capex.

---

## Machine learning basics

Traditional programming: Human writes rules → Computer follows rules

Machine learning: Human provides examples → Computer learns rules

```
Traditional: if (email contains "viagra") → spam
ML: Show millions of spam/not-spam → model learns patterns
```

| Type | What it does | Examples |
|------|--------------|----------|
| **Supervised** | Learn from labeled data | Image classification, spam detection |
| **Unsupervised** | Find patterns in unlabeled data | Clustering, anomaly detection |
| **Reinforcement** | Learn from rewards/penalties | Game playing, robotics |
| **Self-supervised** | Create labels from data itself | **LLMs (predict next word)** |

---

## Neural networks

Loosely inspired by brain neurons. Layers of connected nodes that transform inputs to outputs.

```
Input → [Hidden layers] → Output
  ↓         ↓                ↓
Image    Processing      "Cat" or "Dog"
```

| Component | Function |
|-----------|----------|
| **Neuron** | Weighted sum + activation function |
| **Layer** | Group of neurons |
| **Weights** | Parameters learned during training |
| **Activation** | Non-linearity (ReLU, softmax) |

**Deep learning:** Neural networks with many layers. "Deep" = many hidden layers.

---

## Key architectures

### CNNs (Convolutional Neural Networks)

Specialized for images. Detect patterns regardless of position.

| Use | Examples |
|-----|----------|
| Image classification | Is this a cat? |
| Object detection | Where are the cars? |
| Image generation | Early diffusion models |

**Key insight:** Convolutions share weights → fewer parameters → works on images.

### RNNs/LSTMs (Recurrent Neural Networks)

Process sequences. Have "memory" of previous inputs.

| Use | Examples |
|-----|----------|
| Time series | Stock prediction |
| Text (old approach) | Machine translation |
| Speech | Voice recognition |

**Problem:** Struggle with long sequences. Can't parallelize well.

### Transformers — the breakthrough

Introduced in "Attention Is All You Need" (2017). Replaced RNNs for language.

| Property | RNN | [[Transformer]] |
|----------|-----|-------------|
| Sequence handling | Sequential | **Parallel** |
| Long-range dependencies | Poor | **Excellent** |
| Training speed | Slow | **Fast (parallelizable)** |
| Scale | Limited | **Scales massively** |

**Why transformers won:** Parallelization enables massive scale. Scale enables emergent capabilities.

---

## Attention mechanism

The core innovation of transformers. Lets model focus on relevant parts of input.

```
"The cat sat on the mat because it was tired"
                                    ↓
                        "it" attends to "cat" (not "mat")
```

### Self-attention

Every token looks at every other token. Computes relevance scores.

```
Query (Q): What am I looking for?
Key (K): What do I contain?
Value (V): What information do I provide?

Attention = softmax(Q × K^T / √d) × V
```

**Computational cost:** O(n²) where n = sequence length. This is why context windows are expensive.

### Multi-head attention

Run multiple attention operations in parallel. Each "head" can focus on different relationships (syntax, semantics, etc.).

---

## [[Transformer]] architecture

```
Input tokens
     ↓
[Embedding] — Convert tokens to vectors
     ↓
[Positional encoding] — Add position information
     ↓
[[[Transformer]] blocks] × N
  ├── Multi-head self-attention
  ├── Add & normalize
  ├── Feed-forward network
  └── Add & normalize
     ↓
Output
```

| Variant | Use | Examples |
|---------|-----|----------|
| **Encoder-only** | Understanding | BERT |
| **Decoder-only** | Generation | **GPT, [[Claude]], [[Llama]]** |
| **Encoder-decoder** | Seq-to-seq | T5, original transformer |

**Modern LLMs are decoder-only:** Predict next token, autoregressively.

---

## Large Language Models (LLMs)

[[Transformer]] models trained on massive text to predict next token.

```
Training objective:
"The quick brown ___" → maximize P(fox)
```

| Model | Parameters | Developer |
|-------|------------|-----------|
| GPT-4 | ~1.8T (rumored) | [[OpenAI]] |
| [[Claude]] 3 | Undisclosed | [[Anthropic]] |
| [[Gemini]] Ultra | Undisclosed | [[Google]] |
| [[Llama]] 3 405B | 405B | [[Meta]] |
| [[Grok]] | Undisclosed | [[xAI]] |

### Emergent capabilities

Abilities that appear at scale but weren't explicitly trained:
- Chain-of-thought reasoning
- In-context learning
- Code generation
- Multilingual transfer

**Why this matters:** Nobody fully understands why scaling works. But it does.

---

## Scaling laws

Performance improves predictably with scale. Discovered by OpenAI (Kaplan et al., 2020).

```
Loss ∝ 1/N^α × 1/D^β × 1/C^γ

N = Parameters
D = Dataset size
C = Compute (FLOPs)
```

| To halve loss | Requires |
|---------------|----------|
| More parameters | ~10x |
| More data | ~10x |
| More compute | ~10x |

**Chinchilla scaling (DeepMind):** Optimal ratio is ~20 tokens per parameter. Many early models were over-parameterized, under-trained.

### Compute requirements

| Model size | Training compute (FLOPs) |
|------------|-------------------------|
| GPT-3 (175B) | ~3.6 × 10²³ |
| GPT-4 (est.) | ~2 × 10²⁵ |
| [[Llama]] 3 405B | ~4 × 10²⁵ |

**Doubling every 6-12 months.** This drives GPU demand.

---

## Training vs inference

| Property | Training | Inference |
|----------|----------|-----------|
| What | Learning weights | Using learned weights |
| Compute | Massive (once) | Smaller (per query) |
| Hardware | GPU clusters | GPUs, CPUs, custom |
| Batch size | Large | Small (often 1) |
| Latency | Irrelevant | Critical |
| Memory | Huge (optimizer states) | Model weights only |

### Training compute

```
FLOPs ≈ 6 × N × D

N = parameters
D = training tokens
```

GPT-4 training: ~$100M in compute (estimated).

### Inference compute

```
FLOPs per token ≈ 2 × N

N = parameters
```

Each token generated requires a full forward pass.

**KV cache:** Store computed attention keys/values to avoid recomputation. Trades memory for speed.

---

## Hardware landscape

### Training

| Hardware | Use | Leader |
|----------|-----|--------|
| **GPUs** | Dominant for training | [[NVIDIA]] H100/H200/B200 |
| **TPUs** | Google internal | [[Google]] |
| **Custom ASICs** | Hyperscaler internal | [[Amazon]] Trainium, [[Microsoft]] Maia |

**Why NVIDIA dominates:** CUDA ecosystem, 15+ years of ML optimization, network effects.

### Inference

| Hardware | Strength | Weakness |
|----------|----------|----------|
| GPUs | Flexible, fast | Expensive, power-hungry |
| Custom ASICs | Efficient | Inflexible |
| CPUs | Cheap, available | Slow |

**Inference ASICs:** [[Groq]], [[Cerebras]], [[SambaNova]], AWS Inferentia — optimized for specific workloads.

See [[NVIDIA]], [[AI Infrastructure]], [[Semiconductor primer]].

---

## Memory bandwidth bottleneck

LLM inference is **memory-bound**, not compute-bound.

```
Each token: Load all weights from memory → compute → next token
```

| Metric | H100 | Ideal |
|--------|------|-------|
| Memory | 80GB HBM3 | More |
| Bandwidth | 3.35 TB/s | Higher |
| Compute | 1979 TFLOPS | Underutilized |

**Arithmetic intensity:** LLM inference has low arithmetic intensity (few FLOPs per byte loaded). GPU compute is underutilized.

**Solutions:** Larger batch sizes, model parallelism, speculative decoding, quantization.

See [[HBM]], [[Memory shortage 2025-2026]].

---

## Model parallelism

Large models don't fit on one GPU. Split across many.

| Type | How it splits | Use |
|------|---------------|-----|
| **Data parallel** | Same model, different data | Training batches |
| **Tensor parallel** | Split layers across GPUs | Within-node |
| **Pipeline parallel** | Different layers on different GPUs | Across nodes |
| **Expert parallel** | Different experts on different GPUs | MoE models |

**Communication overhead:** GPUs must exchange activations/gradients. Requires fast interconnects (NVLink, InfiniBand).

See [[Optical networking primer]].

---

## Mixture of Experts (MoE)

Not all parameters active for every token. Route to specialized "experts."

```
Input → Router → Expert 1, 2, or 3 → Output
                 (only one active)
```

| Property | Dense | MoE |
|----------|-------|-----|
| Active parameters | All | Subset (~25%) |
| Total parameters | N | 4-8x N |
| Inference cost | Higher | **Lower** |
| Training cost | Lower | Higher |
| Memory | Lower | **Higher** (all experts loaded) |

**GPT-4 is MoE:** Rumored 8 experts × ~220B each = 1.8T total, but only ~220B active per token.

---

## Quantization

Reduce precision of weights to save memory and compute.

| Precision | Bits | Memory | Quality |
|-----------|------|--------|---------|
| FP32 | 32 | Baseline | Best |
| FP16 | 16 | 2x savings | Slightly worse |
| BF16 | 16 | 2x savings | Good for training |
| INT8 | 8 | 4x savings | Good |
| INT4 | 4 | 8x savings | Degraded |

**Post-training quantization (PTQ):** Quantize after training. Easy but quality loss.

**Quantization-aware training (QAT):** Train with quantization. Better quality, more effort.

---

## Context windows

How much text the model can "see" at once.

| Model | Context window |
|-------|----------------|
| GPT-3 | 4K tokens |
| GPT-4 | 8K-128K tokens |
| [[Claude]] 3 | 200K tokens |
| [[Gemini]] 1.5 | 1M+ tokens |

**Cost:** Attention is O(n²). Doubling context = 4x attention compute.

**Solutions:**
- Sparse attention (not all tokens attend to all)
- Sliding window attention
- Memory/retrieval augmentation (RAG)

---

## Fine-tuning and RLHF

### Pre-training

Train on massive unlabeled text. Learn language patterns.

Cost: $10M-$100M+

### Supervised fine-tuning (SFT)

Train on curated examples of desired behavior.

Cost: $100K-$1M

### RLHF (Reinforcement Learning from Human Feedback)

1. Humans rank model outputs
2. Train reward model on rankings
3. Optimize policy against reward model

**Why RLHF matters:** Aligns model behavior with human preferences. Makes models helpful, harmless, honest.

### DPO (Direct Preference Optimization)

Simpler alternative to RLHF. Skip reward model, optimize directly on preferences.

---

## Inference optimization techniques

| Technique | What it does |
|-----------|--------------|
| **KV caching** | Avoid recomputing attention for past tokens |
| **Continuous batching** | Add new requests to running batch |
| **Speculative decoding** | Draft with small model, verify with large |
| **Quantization** | Lower precision weights |
| **Distillation** | Train small model to mimic large |
| **Pruning** | Remove unnecessary weights |

---

## Multimodal models

Process multiple input types (text, image, audio, video).

| Model | Modalities |
|-------|------------|
| GPT-4V | Text, image |
| [[Gemini]] | Text, image, audio, video |
| [[Claude]] 3 | Text, image |

**Architecture:** Encode each modality → project to shared space → transformer processes jointly.

---

## Diffusion models

Dominant approach for image/video generation.

```
Training: Image → Add noise gradually → Learn to reverse
Inference: Start with noise → Denoise step by step → Image
```

| Model | Developer | Use |
|-------|-----------|-----|
| DALL-E 3 | OpenAI | Image generation |
| Midjourney | Midjourney | Image generation |
| Stable Diffusion | [[Stability AI]] | Open source images |
| Sora | OpenAI | Video generation |

---

## Key metrics for investors

| Metric | Definition | Why it matters |
|--------|------------|----------------|
| **Parameters** | Model size | Capability proxy |
| **Training FLOPs** | Compute used | Investment required |
| **Tokens/second** | Inference throughput | User experience, cost |
| **$/1M tokens** | API pricing | Unit economics |
| **Context window** | Input capacity | Use case enablement |

---

## [[Competitive moats]]

| Moat | Who has it |
|------|------------|
| **Compute scale** | Hyperscalers (Google, [[Microsoft]], [[Amazon]]) |
| **Data** | Google (search), Meta (social), OpenAI (usage) |
| **Talent** | OpenAI, Anthropic, DeepMind |
| **Distribution** | [[Microsoft]] (Office), Google (Search) |
| **CUDA ecosystem** | [[NVIDIA]] |

---

## Related

- [[AI Infrastructure]] — hardware buildout
- [[NVIDIA]] — GPU leader
- [[OpenAI]] — GPT developer
- [[Anthropic]] — [[Claude]] developer
- [[Google]] — [[Gemini]], TPUs
- [[Meta]] — [[Llama]], open source
- [[xAI]] — [[Grok]]
- [[Hyperscaler capex]] — demand driver
- [[HBM]] — memory bandwidth
- [[Semiconductor primer]] — chip fundamentals
- [[Optical networking primer]] — interconnects
- [[Scaling laws]] — why bigger is better
