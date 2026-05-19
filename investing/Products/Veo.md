---
aliases:
  - Veo
  - Veo 2
  - Veo 3
  - Veo 3.1
  - Google Veo
tags:
  - product-family
  - ai
  - video-generation
parent_actor: "Google DeepMind"
parent_concept: "Generative AI"
---

# Veo

[[Google DeepMind]]'s video generation model. Veo 3.1 (Oct 2025) generates 1080p video up to 60 seconds with native audio. Integrated into Gemini and Google Vids.

## Quick stats

| Metric | Value |
|--------|-------|
| Current version | Veo 3.1 (Oct 2025) |
| Max duration | 60 seconds |
| Resolution | Up to 4K |
| Native audio | Yes |
| Access | Gemini API, Vertex AI |

---

## Version history

| Version | Release | Key changes |
|---------|---------|-------------|
| Veo | May 2024 | Initial announcement |
| **Veo 2** | Dec 2024 | Quality improvements |
| **Veo 3** | May 2025 | Native audio generation |
| Veo 3.1 | Oct 2025 | 1080p, 60s, improved control |
| Veo 3.1 Fast | Oct 2025 | Speed-optimized |

---

## Pricing (API)

| Model | Price |
|-------|-------|
| Veo 3.1 Fast | $0.15/second |
| Veo 3.1 Standard | $0.40/second |

---

## Features

| Feature | Details |
|---------|---------|
| Native audio | Dialogue, SFX, ambient |
| Ingredients to Video | Multi-reference images |
| Frames to Video | Start/end frame bridging |
| Scene extension | Maintain continuity |
| Vertical video | YouTube Shorts support |
| Identity consistency | Character persistence |
| 4K upscale | Resolution enhancement |

---

## Integration

| Platform | Usage |
|----------|-------|
| Gemini API | Developer access |
| Vertex AI | Enterprise |
| Gemini app | Consumer |
| Google Vids | Workspace avatars |
| Flow | Creative editing |

---

## Competitive position

| vs | Veo advantage | Weakness |
|----|--------------|----------|
| [[Sora]] | Google integration, audio | Brand perception |
| [[Runway Gen]] | Resources, scale | Creative community |
| [[Kling]] | Quality, integration | Duration (Kling: 3 min) |

---

## YouTube training-data edge

Per the FT (Eleanor Olcott, May 17 2026), experts attribute Veo's competitive-but-not-leading position to its access to YouTube footage — the single largest curated video library on the internet. Training video models requires vast amounts of high-quality footage, and YouTube gives [[Google]] a data advantage that [[OpenAI]] could not replicate (one of the structural reasons [[Sora]] was discontinued in March 2026 — see [[Sora]]).

But the advantage is bounded by [[Google]]'s safety/IP posture: Veo carries more safeguards and content limits than Chinese competitors, which trades raw capability for legal defensibility. Several developers and creators in the FT piece noted US tools "constantly run into errors" denying requests for violating usage terms — a usability friction that pushes professional users toward [[Seedance]] and [[Kling]].

The data-advantage asymmetry is the geographic-axis variant of [[AI producer-evaluator asymmetry]]: whoever has the producer-side data abundance (short-video apps in China, YouTube at [[Google]]) wins the video segment, while pure model-quality leaders without proprietary video corpora ([[OpenAI]], [[Anthropic]]) are structurally disadvantaged.

---

## Arena rankings (May 2026)

Per the Arena user-voted blind-test leaderboard published in the FT (May 17 2026):

| Category | Veo placement | Score |
|---|---|---|
| Text-to-Video | #3 (Veo 3.1 audio), #4 (Veo 3.1 fast) | 1,375 / 1,368 |
| Image-to-Video | #4 (Veo 3.1 audio) | 1,402 |
| Video edit | Not in top 4 | — |

In image-to-video Veo 3.1 audio (1,402) sits behind [[Grok Imagine Video]] (1,421) — meaning [[xAI]]'s product, not Google's, is the strongest non-Chinese model in that category. In text-to-video Veo 3.1 audio (1,375) and Veo 3.1 fast (1,368) are #3 and #4, both behind [[Seedance]] 2.0 and HappyHorse 1.0. Veo's best showing is text-to-video where YouTube data probably contributes most.

See [[AI Video Generation#May 17, 2026 — Chinese groups pull ahead of US rivals (FT)|AI Video Generation hub]] for the full market structure.

*Source: [FT](https://www.ft.com/content/9804b1de-653b-40b2-bffb-17c76ebebe34), May 17, 2026.*

---

## Related

- [[Google DeepMind]] — parent actor
- [[Google]] — parent company
- [[Gemini]] — sibling model
- [[Sora]] — competitor (discontinued March 2026)
- [[Seedance]] — competitor — currently #1 on Arena leaderboards
- [[Happy Horse|HappyHorse]] — competitor ([[Alibaba]]) — currently #2 on Arena
- [[Kling]] — competitor ([[Kuaishou]])
- [[Grok Imagine Video]] — competitor ([[xAI]]) — only non-Chinese top-3 model
- [[Hailuo]] — competitor ([[MiniMax]])
- [[Runway Gen]] — competitor
- [[Generative AI]] — category
- [[AI Video Generation]] — concept hub with full leaderboard
- [[AI producer-evaluator asymmetry]] — framework for the data-advantage dynamic
