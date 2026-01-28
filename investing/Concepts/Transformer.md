---
aliases: [Transformer architecture, Attention mechanism, Self-attention]
---
#concept #ai #architecture

**Transformer** — The architecture behind all modern AI. Introduced in "Attention Is All You Need" ([[Google]], 2017). Foundation of GPT, BERT, Claude, Gemini, Llama — everything. **173,000+ citations** (top 10 most-cited papers of 21st century).

---

## Why Transformers matter

| Metric | Value |
|--------|-------|
| Paper | "Attention Is All You Need" (2017) |
| Citations | **173,000+** |
| Impact | Foundation of ALL modern LLMs |
| Key innovation | Self-attention mechanism |
| What it replaced | RNNs, LSTMs, CNNs for sequences |

**Every major AI model today is a Transformer:** [[ChatGPT]], [[Claude]], [[Gemini]], [[Llama]], [[Qwen]], [[DeepSeek]], etc.

---

## The paper

**"Attention Is All You Need"** — NeurIPS 2017

| Detail | Value |
|--------|-------|
| Published | June 12, 2017 |
| Institution | [[Google]] Brain / [[Google]] Research |
| Training time | 12 hours (base), 3.5 days (big) |
| Original task | Machine translation |
| BLEU score | 28.4 (English→German, SOTA) |

### Authors (equal contribution, randomized order)

| Name | Notable later role |
|------|-------------------|
| Ashish Vaswani | Essential AI (co-founder) |
| [[Noam Shazeer]] | [[Character.AI]] (co-founder) |
| Niki Parmar | Essential AI (co-founder) |
| Jakob Uszkoreit | Inceptive (co-founder) |
| Llion Jones | [[Sakana AI]] (co-founder) |
| [[Aidan Gomez]] | [[Cohere]] (co-founder) |
| Łukasz Kaiser | [[OpenAI]] |
| Illia Polosukhin | NEAR Protocol (co-founder) |

**8 authors → 6+ billion-dollar companies.** The paper's alumni network is extraordinary.

---

## Key innovation: Self-attention

**The problem with RNNs/LSTMs:** Process sequences one token at a time. Can't parallelize. Long-range dependencies are hard.

**Transformer solution:** Attention mechanism lets every token "see" every other token simultaneously.

| Approach | Sequence processing | Parallelization |
|----------|--------------------| ----------------|
| RNN/LSTM | Sequential (slow) | Poor |
| **Transformer** | All at once | **Excellent** |

**"Attention is all you need"** — No recurrence, no convolutions. Just attention.

---

## Architecture

```
Input → Embedding → [Encoder × 6] → [Decoder × 6] → Output
```

### Encoder (6 identical layers)
1. Multi-head self-attention
2. Feed-forward network
3. Residual connections + layer norm

### Decoder (6 identical layers)
1. Masked multi-head self-attention
2. Cross-attention (to encoder output)
3. Feed-forward network
4. Residual connections + layer norm

**Multi-head attention:** Multiple attention "heads" learn different relationships (8 heads in original).

---

## Why it worked

| Factor | Contribution |
|--------|--------------|
| **Parallelization** | GPUs can process all tokens simultaneously |
| **Long-range dependencies** | Any token can attend to any other |
| **Scalability** | More compute = better results (scaling laws) |
| **Simplicity** | Cleaner than RNN/LSTM architectures |

---

## What followed

| Year | Model | Innovation |
|------|-------|------------|
| 2017 | **Transformer** | Attention mechanism |
| 2018 | GPT-1 | Decoder-only, generative pretraining |
| 2018 | BERT | Encoder-only, bidirectional |
| 2019 | GPT-2 | Scale (1.5B params) |
| 2020 | GPT-3 | Scale (175B params), few-shot learning |
| 2022 | ChatGPT | RLHF, conversational |
| 2023+ | GPT-4, Claude, etc. | Multimodal, reasoning |

**Decoder-only** (GPT family): Generate text left-to-right
**Encoder-only** (BERT): Understand text bidirectionally
**Encoder-decoder** (T5, original): Translation, seq2seq

---

## Scaling laws

**Key discovery:** Transformer performance scales predictably with:
- Model size (parameters)
- Dataset size (tokens)
- Compute (FLOPs)

This enabled the "just make it bigger" strategy that produced GPT-3, GPT-4, etc.

---

## Limitations and successors

| Limitation | Attempted solutions |
|------------|---------------------|
| Quadratic attention cost | Sparse attention, linear attention |
| Context window limits | RoPE, ALiBi, ring attention |
| No world model | [[World Models]], embodied AI |
| Hallucinations | RLHF, constitutional AI |

**Post-Transformer architectures emerging:**
- State space models (Mamba)
- [[World Models]] (spatial intelligence)
- Mixture of Experts (efficiency)

---

## Investment implications

**Historical context** — not directly investable.

**Why it matters:**
- Explains why [[NVIDIA]] dominates (Transformers need parallel compute)
- Scaling laws drove the AI capex boom
- Foundation of every AI company's core technology

**Author alumni:**
- [[Character.AI]] (Shazeer) — $1B+ valuation
- [[Cohere]] (Gomez) — $5.5B valuation
- Essential AI (Vaswani, Parmar) — $800M+ valuation
- [[Sakana AI]] (Jones) — $200M+ valuation

---

## Quick stats

| Metric | Value |
|--------|-------|
| Paper | "Attention Is All You Need" |
| Year | 2017 |
| Citations | 173,000+ |
| Key innovation | Self-attention |
| Impact | Foundation of all modern LLMs |

*Created 2026-01-27*

---

## Related

- [[ImageNet]] — prior breakthrough (2012, data)
- [[AlexNet]] — prior breakthrough (2012, CNNs)
- [[ResNet]] — prior breakthrough (2015, depth)
- [[ChatGPT]] — Transformer application
- [[Claude]] — Transformer application
- [[NVIDIA]] — hardware beneficiary
- [[Scaling laws]] — key insight enabled by Transformers
