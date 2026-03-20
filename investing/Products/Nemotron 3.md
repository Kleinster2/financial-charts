---
aliases: [Nemotron 3 Super, Nemotron 3 Ultra, Nemotron 3 Omni, Nemotron 3 VoiceChat, NeMo Tron 3]
tags: [product, ai, model, open-source]
---

#product #ai #model #opensource

Nemotron 3 — [[NVIDIA]]'s family of open-weight foundation models for agentic AI, announced at [[GTC 2026]] (March 17, 2026). The flagship product of NVIDIA's $26B open model investment and the [[Nemotron Coalition]].

## Synopsis

Nemotron 3 is NVIDIA's play to do for AI models what [[CUDA moat|CUDA]] did for GPU computing: give away the software layer to sell the silicon. The family spans four models — Super (agentic inference), Ultra (sovereign AI base model), Omni (multimodal), and VoiceChat (real-time conversation) — plus safety and retrieval models. Super shipped first and immediately topped benchmarks for open models in its class. Ultra, still forthcoming, is what [[Jensen Huang]] called "the best base model the world's ever created" — positioned as the foundation for any country or enterprise to fine-tune sovereign AI without dependence on [[OpenAI]], [[Anthropic]], or Chinese closed providers.

The strategic logic: NVIDIA is perhaps the only company that can afford to give away frontier models because it makes the money back on hardware. [[Meta]]'s [[Llama]] has a similar open strategy but no hardware revenue to subsidize it. The $26B five-year commitment to open models (confirmed by Wired, validated by NVIDIA) signals this isn't a side project — it's core strategy. The [[Nemotron Coalition]] of eight AI labs (including [[Mistral]], [[Perplexity]], [[Cursor]], and [[Mira Murati]]'s [[Thinking Machines Lab]]) ensures ecosystem gravity. Every company fine-tuning Nemotron models on NVIDIA's NeMo platform is more likely to run inference on NVIDIA GPUs.

---

## Nemotron 3 Super

| Metric | Value |
|--------|-------|
| Parameters | 120B total, 12B active |
| Architecture | Hybrid Mamba-Transformer MoE |
| Context window | 1M tokens |
| Precision | NVFP4 on [[Blackwell]] |
| License | Open weights, permissive |
| Status | Available now |

### Architecture innovations

- Hybrid MoE: Mamba layers for 4x memory/compute efficiency + Transformer layers for advanced reasoning
- Latent MoE: Activates 4 expert specialists for the cost of 1 by compressing tokens before they reach experts
- Multi-Token Prediction: Predicts multiple future words simultaneously → 3x faster inference
- NVFP4 on Blackwell: 4x faster than FP8 on [[Hopper]], no accuracy loss

### Benchmarks

| Benchmark | Score | Ranking |
|-----------|-------|---------|
| SWE-Bench Verified | 60.47% | Leading open models |
| PinchBench | 85.6% | Leading open models |
| RULER 1M (long context) | 91.75% | Leading open models |
| Artificial Analysis Intelligence Index | 36 | #1 efficiency + openness in class |
| DeepResearch Bench I | #1 | Powers NVIDIA AI-Q agent |
| DeepResearch Bench II | #1 | Powers NVIDIA AI-Q agent |

### Throughput

- 5x higher throughput vs previous Nemotron Super
- 2x higher accuracy vs previous Nemotron Super
- 2.2x throughput vs GPT-OSS-120B equivalent

### Adoption

AI-native companies: [[Perplexity]] (search + orchestration), [[CodeRabbit]], Factory, Greptile (code review agents), Edison Scientific, Lila Sciences (life sciences agents)

Enterprise platforms: [[Amdocs]], [[Palantir]], [[Cadence]], [[Dassault Systèmes]], [[Siemens]] — deploying for telecom, cybersecurity, semiconductor design, manufacturing

Cloud/inference providers: [[Google Cloud]] (Vertex AI), [[Oracle]] (OCI), [[AWS]] (Bedrock, coming soon), [[Microsoft]] Azure, [[CoreWeave]], Crusoe, [[Nebius]], [[Together AI]], [[Baseten]], [[Cloudflare]], DeepInfra, Fireworks AI, Lightning AI, Modal, FriendliAI

Hardware vendors: [[Dell]], [[HPE]] — optimized for on-premise deployment

---

## Nemotron 3 Ultra

| Metric | Value |
|--------|-------|
| Status | Coming soon (announced GTC 2026) |
| Purpose | Best-in-class open base model for fine-tuning |
| Target | Sovereign AI, enterprise customization |
| First co-development | With [[Mistral]] (Nemotron 4 development) |

Jensen's GTC quote: "Nemotron 3 Ultra is going to be the best base model the world's ever created. This allows us to help every country build their sovereign AI."

Positioned to let any country or enterprise fine-tune a frontier model for its specific domain, language, or regulatory context — without dependence on any single proprietary model provider. Paired with NVIDIA's release of 10T+ tokens of pre/post-training datasets, 15 training environments for RL, and evaluation recipes.

---

## Nemotron 3 Omni

Integrates audio, vision, and language understanding. Draws information from videos and documents with greater efficiency than comparable multimodal models.

---

## Nemotron 3 VoiceChat

Enables AI to listen and respond simultaneously during real-time conversations. Combines speech recognition, LLM processing, and text-to-speech.

---

## Additional models

- Safety models: Detect unsafe content in text and images
- Retrieval pipeline: Improve relevance and accuracy of model outputs (RAG)

---

## Training methodology

NVIDIA released the complete training methodology alongside Super:
- Data: 10T+ tokens of pre- and post-training datasets (published)
- RL environments: 15 training environments for reinforcement learning
- Evaluation recipes: Full eval recipes published
- Synthetic data: Trained on synthetic data generated using frontier reasoning models
- Platform: NVIDIA NeMo for fine-tuning and custom model building

This level of openness (weights + data + recipes) is unusual — most "open" models release weights only. Lowers the barrier to domain-specific customization significantly.

---

## Strategic context

### NVIDIA's $26B open model investment

NVIDIA committing $26B over 5 years to open models (Wired, confirmed by NVIDIA). The logic per [[Next Platform]]: "NVIDIA is perhaps the only company that can afford to give away its models because it can make its revenue stream back on AI systems. This may eventually be too costly for [[Meta]] to give it away as [[Google]], [[OpenAI]], and [[Anthropic]] most certainly do not."

### Open model families (nine domains)

| Family | Domain |
|--------|--------|
| Nemotron | Language, reasoning, agentic AI |
| Cosmos | Physical AI world generation |
| Alpamayo | Autonomous vehicles |
| Groot | Humanoid robotics |
| BioNeMo | Digital biology, molecular design |
| Earth2 | Weather/climate forecasting |
| Financial services | Domain-specific |
| Healthcare | Domain-specific |
| Telecommunications | Domain-specific |

Jensen at GTC: "We are now at the frontier of every single domain of AI models."

### The CUDA parallel

Same playbook: give away the software ecosystem, sell the silicon. CUDA libraries locked in a decade of AI training developers. Nemotron models aim to lock in the next decade of inference and fine-tuning workloads. Every organization using NeMo + Nemotron is more likely to buy NVIDIA GPUs for inference.

---

## Related

- [[NVIDIA]] — parent company
- [[Nemotron Coalition]] — eight-lab collaborative for open frontier models
- [[NemoClaw]] — enterprise agent platform built on [[OpenClaw]], uses Nemotron models
- [[CUDA moat]] — parallel strategy (give away software, sell silicon)
- [[Sovereign AI race]] — Nemotron Ultra positioned for sovereign fine-tuning
- [[GTC 2026]] — launch event
- [[Mistral]] — coalition partner, co-developing Nemotron 4
- [[Perplexity]] — coalition partner, early adopter
- [[Cursor]] — coalition partner
- [[Thinking Machines Lab]] — coalition partner ([[Mira Murati]])
- [[Jensen Huang]] — "best base model the world's ever created"
- [[Vera Rubin]] — hardware platform for Nemotron inference

### Sources
- [NVIDIA Blog: Nemotron 3 Super for Agentic AI](https://blogs.nvidia.com/blog/nemotron-3-super-agentic-ai/) (Mar 2026)
- [Tom's Hardware: Nemotron Coalition](https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidias-nemoclaw-coalition-brings-eight-ai-labs-together-to-build-open-frontier-models) (Mar 17, 2026)
- [Next Platform: The Open Agentic AI World According to Nvidia](https://www.nextplatform.com/code/2026/03/18/the-open-agentic-ai-world-according-to-nvidia/) (Mar 18, 2026)
- [Shashi.co: GTC 2026 Five Arguments](https://www.shashi.co/2026/03/gtc-2026-jensen-huangs-five-arguments.html) (Mar 2026)
