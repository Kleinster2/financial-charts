---
aliases: [GenAI, generative artificial intelligence, foundation models, generative models]
tags: [concept, ai, technology, framework]
---

# Generative AI

Generative AI is the class of AI models that produce new content — text, code, images, video, audio, 3D, molecular structures — rather than classifying or predicting from existing inputs. The 2022-2026 wave is built on transformer-based foundation models trained on internet-scale data using high-end accelerators ([[NVIDIA]] H100 / H200 / B200 / Rubin) at enormous compute scale. The category sits at the centre of the broader AI investment narrative — driving [[AI infrastructure financing]], the [[Defense primes basket|defense reshape]], the [[AI cybersecurity disruption basket|cybersecurity disruption]], and the [[AI Video Generation|video-generation race]] tracked elsewhere in the vault.

This note exists as a stub concept for the foundational technology; deeper threads are in dedicated notes below.

---

## Capability stack

The investing-vault treatment of generative AI splits across capability modalities, each of which has its own market structure, leading players, and vault-thread depth:

| Modality | Status (May 2026) | Vault thread |
|---|---|---|
| Text / chat / coding | US labs lead — [[Anthropic]] ([[Claude]] family + [[Claude Mythos]]), [[OpenAI]] (GPT family), [[Google]] ([[Gemini]]) | [[Claude]], [[AI cybersecurity disruption basket]] |
| Code agents | US labs lead — [[Claude Code]], [[Devin]], Cursor | [[Claude Code]], [[Agentic AI]] |
| Image | Mixed — Midjourney, [[DALL-E]], Stable Diffusion, Chinese models | (limited vault coverage) |
| Video | Chinese labs lead — [[Kling]] ([[Kuaishou]]), [[Seedance]] ([[ByteDance]]), HappyHorse vs [[Veo]] ([[Google]]); [[Sora]] discontinued March 2026 | [[AI Video Generation]] |
| Audio / voice | Mixed — ElevenLabs, [[OpenAI]] voice, Chinese options | (limited vault coverage) |
| 3D / molecular | Specialized — Genie 3 (Google), AlphaFold lineage (Isomorphic Labs) | (limited vault coverage) |

The geographic asymmetry per modality is structural rather than incidental. US labs have a research / talent / capital edge in modalities anchored to text-and-code training data (the public internet); Chinese labs have a data edge in modalities anchored to short-video, image, and consumer-app data they own. The [[AI producer-evaluator asymmetry#The Sora inversion — same pattern, different axis|Sora inversion]] frames this asymmetry analytically.

---

## Economic structure

The market is organized in vertical layers:

| Layer | Role | Leading firms |
|---|---|---|
| Hardware | AI accelerators + networking + memory + power | [[NVIDIA]], [[AMD]], [[Broadcom]], [[TSMC]] (manufacturing), [[SK Hynix]] / [[Micron]] / [[Samsung]] (HBM) |
| Cloud / infrastructure | Compute + storage + orchestration | [[AWS]], [[Microsoft]] Azure, [[Google]] Cloud, [[CoreWeave]], [[Crusoe Energy]], sovereign-AI hyperscalers |
| Foundation models | Training + inference of base models | [[OpenAI]], [[Anthropic]], [[Google]] (DeepMind), [[Meta]] (Llama), [[xAI]], [[DeepSeek]], [[ByteDance]], [[Alibaba]] (Qwen), [[MiniMax]] |
| Tooling / agents / applications | Productize the base capability | [[Claude Code]], [[Cursor]], [[Perplexity]], domain-specific verticals |
| End-user products | Consumer or enterprise-facing | [[ChatGPT]], [[Claude]], [[Gemini]], domain SaaS plus AI |

The [[Inference economics]] note covers the unit-economics layer that constrains how much of the value created flows back to which layer. As of May 2026 the dominant pattern is: hardware captures the largest profit pool short-term ([[NVIDIA]] margins); foundation model labs are still consuming capital faster than they generate revenue; tooling / applications are in the early-monetisation phase with widely-varying margins.

---

## Three central narratives shaping AI investment exposure

The vault's generative-AI threads cluster around three central narratives, each with its own basket exposure and timing:

1. **AI infrastructure buildout** — the hyperscaler + sovereign capex cycle requires hardware, power, and real estate. Tracked through [[AI infrastructure financing]], [[Defense Autonomous Warfare Group]], [[Crusoe Energy]], [[CoreWeave]], [[Anduril]], [[Defense procurement reform]]. The infrastructure-narrative cycle has run far enough that the [[AI-attached unit IPO playbook|peak-narrative monetisation pattern]] is now operative — see [[Cerebras IPO revival April 2026]] for the standalone case.
2. **AI capability disruption** — generative AI eating existing software product categories. Tracked through [[AI cybersecurity disruption basket]], [[Claude Cowork disruption February 2026]], [[AI disintermediation]], [[February 2026 AI Disruption Cascade]]. Adjacent: [[AI producer-evaluator asymmetry]] which generalises the disruption pattern across markets where input cost was the implicit filter.
3. **Geographic / sovereign AI** — US-China divergence by modality, plus sovereign-AI infrastructure projects ([[UAE G42]] / [[MBZUAI]], Saudi Arabia, India). Tracked through [[Sovereign AI race]], [[Sovereign AI stack]], [[Export controls]], [[Operation Epic Fury|2026 Iran conflict]] adjacent sovereign-AI exposures.

The three narratives reinforce each other but have different timing: infrastructure-buildout was the 2023-2025 dominant trade; capability-disruption is the 2025-2026 wave; geographic / sovereign AI is the multi-year structural story that compounds with both.

---

## Risks to the overall thesis

- **Unit economics** — inference costs at scale may not fall fast enough for the consumer-facing products to be cleanly profitable. [[Sora]]'s discontinuation is the cleanest single example.
- **Multiple compression** — the [[AI-attached unit IPO playbook]] is itself a leading indicator that insiders are choosing to capture multiples rather than continue holding them. Peak-narrative IPO waves typically front-run multiple contraction by 6-18 months.
- **Regulatory action** — EU AI Act, US export controls, Chinese content-moderation rules. [[Export controls]] is the most active near-term variable.
- **Energy-grid bottleneck** — AI capex is constrained by power availability. [[Clean energy for AI]] is the relevant thread.
- **Copyright / data-access litigation** — multiple cases pending in US courts ([[Disney]] v [[OpenAI]] / training-data cases). Outcome shapes which labs can train on which corpora.

---

## Related

### Capability threads
- [[AI Video Generation]] — video modality; Chinese lead
- [[AI cybersecurity disruption basket]] — cybersecurity disruption
- [[Claude Code]] — code-agent leader
- [[Claude Mythos]] — cyber AI agent
- [[Agentic AI]] — autonomous workflow agents
- [[Sovereign AI race]] — geography-axis competitive picture
- [[Sovereign AI stack]] — sovereign infrastructure layer

### Frameworks
- [[AI producer-evaluator asymmetry]] — market-structure framework for AI-disrupted markets
- [[AI-attached unit IPO playbook]] — peak-narrative monetisation pattern
- [[AI disintermediation]] — adjacent professional-services thesis
- [[Inference economics]] — unit-economics layer
- [[AI infrastructure financing]] — capex-cycle financing structure
- [[Inference-time scaling]] — model improvement via test-time compute

### Hardware / infrastructure
- [[NVIDIA]] — dominant accelerator supplier
- [[TSMC]] — foundry partner
- [[SK Hynix]], [[Micron]] — HBM memory
- [[CoreWeave]], [[Crusoe Energy]] — AI-native cloud
- [[Cerebras]] — wafer-scale AI hardware (IPO May 14 2026)

### Foundation model labs
- [[OpenAI]], [[Anthropic]], [[Google]] (DeepMind), [[Meta]], [[xAI]] — US
- [[ByteDance]], [[Kuaishou]], [[MiniMax]], [[DeepSeek]], [[Alibaba]] — China

### Cross-vault

- [Technologies: Generative AI](obsidian://open?vault=technologies&file=Generative%20AI) — technology fundamentals (stub candidate)

---

*Created 2026-05-18. Stub-tier concept note filling a long-standing wikilink target gap. Substantive thread depth lives in the dedicated capability / framework notes linked above; this note is the navigation hub.*
