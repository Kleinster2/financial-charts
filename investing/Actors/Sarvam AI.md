---
aliases: [Sarvam]
tags:
  - actor
  - ai
  - india
  - startup
---

#actor #ai #india #startup

**Sarvam AI** — Indian AI startup building sovereign large language models for [[India]]. Developing multilingual models optimized for Indian languages.

---

## Quick stats

| Metric | Value |
|--------|-------|
| Founded | August 2023 |
| HQ | Bengaluru, Karnataka |
| Founders | Vivek Raghavan, Pratyush Kumar (ex-AI4Bharat, [[IIT Madras]]) |
| Funding | ~$41M (Seed + Series A, Dec 2023) |
| Investors | [[Lightspeed Venture Partners]], [[Khosla Ventures]], Peak XV Partners |
| Focus | Sovereign LLMs, Indian languages (10+) |
| Status | Private |

---

## February 2026 model launch

Announced at the [[India AI Impact Summit 2026]] (Feb 18, 2026). Six models released — the largest Indian-origin AI model family to date.

### Foundational LLMs

| Model | Parameters | Active params/token | Context window | Training data | Positioning |
|-------|-----------|---------------------|----------------|---------------|-------------|
| **Sarvam-30B** | 30B | ~1B (MoE) | 32,000 tokens | ~16T tokens | Real-time conversational; vs Google Gemma 27B, OpenAI GPT-OSS-20B |
| **Sarvam-105B** | 105B | ~9B (MoE) | 128,000 tokens | Trillions of tokens (multilingual) | Complex reasoning, enterprise; vs OpenAI GPT-OSS-120B, Alibaba Qwen-3-Next-80B |

Both models trained from scratch (not fine-tuned from existing open-source systems). Use mixture-of-experts architecture — only a fraction of parameters active per token, reducing compute costs. Trained using IndiaAI Mission compute (government-backed GPUs), infrastructure from Yotta (Indian data center operator), technical support from [[NVIDIA]].

Sarvam plans to open-source both models (training data/code availability TBD).

**Beta app:** Sarvam-105B released as "Indus" on Feb 20 — available on iOS, Android, and web.

### Multimodal models

| Product | Details |
|---------|---------|
| **Sarvam Vision** | 3B parameter vision-language/OCR model for Indian documents. 22 languages + English. 84.3% on olmOCR-Bench — outperforms [[Google]] Gemini 3 Pro, [[OpenAI]] ChatGPT, DeepSeek OCR v2 on multi-script documents. 93.28% on OmniDocBench |
| **Saaras V3** | Speech-to-text model, multiple Indian languages |
| **Bulbul V3** | TTS system, 11 Indian languages + Indian-accented English. 30+ speaker voices, control over pace/tone/expressivity. 8-48 kHz output |

### Hardware

| Product | Details |
|---------|---------|
| **Sarvam Kaze** | AI-powered wearable glasses — listens, understands, captures what users see in real time. 10+ Indian languages, voice-based interaction, real-time translation. Launch planned May 2026. First Made-in-India AI wearable |

### Enterprise products

- **Sarvam for Work** — coding-focused models and enterprise tools
- **Samvaad** — conversational AI agent platform
- Document intelligence APIs — production-ready, free for experimentation (Feb 2026)

---

## Overview

Sarvam AI positions itself as a full-stack AI platform making "AI that gets India." Founded by Vivek Raghavan and Pratyush Kumar, previously at AI4Bharat ([[IIT Madras]]). One of 12 teams shortlisted by the IndiaAI Mission (Apr 2025) for indigenous foundation model development, receiving government-backed compute resources. At the [[India AI Impact Summit 2026]] (Feb 2026), emerged as the most visible private player in India's sovereign AI push. Google CEO [[Sundar Pichai]] publicly expressed being "quite impressed" with Sarvam's models.

Co-founder Pratyush Kumar on scaling philosophy: "We don't want to do the scaling mindlessly. We want to understand the tasks which really matter at scale and go and build for them."

---

## Related

- [[India]] — home market
- [[India AI]] — national AI program
- [[India AI Impact Summit 2026]] — Feb 2026 model launch, Sarvam Kaze reveal
- [[IIT Madras]] — founders' academic origin (AI4Bharat)
- [[IIT Bombay]] — BharatGen sovereign LLM collaboration
- [[NVIDIA]] — technical support for model training
- [[Lightspeed Venture Partners]] — lead investor
- [[Khosla Ventures]] — investor
- [[Google]] — Sundar Pichai expressed public interest
- [[DeepSeek]] — Chinese peer in efficient open-source AI models

---

*Updated 2026-03-05*
