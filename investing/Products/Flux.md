---
aliases:
  - Flux
  - FLUX
  - FLUX.1
  - FLUX.2
  - Flux.2
tags:
  - product-family
  - ai
  - image-generation
  - open-source
parent_actor: "[[Black Forest Labs]]"
parent_concept: "[[Generative AI]]"
---

# Flux

[[Black Forest Labs]]' image generation models. FLUX.2 (Nov 2025) is 32B parameter frontier model. [klein] variant runs in <1 second on consumer GPUs.

## Quick stats

| Metric | Value |
|--------|-------|
| Current version | FLUX.2 (Nov 2025) |
| Largest model | 32B parameters |
| Smallest | 4B (klein) |
| License | Apache 2.0 (klein 4B) |
| Key strength | Open source, speed |

---

## Version history

| Model | Release | Key changes |
|-------|---------|-------------|
| FLUX.1 [pro] | Aug 2024 | Initial release |
| FLUX.1 [dev] | Aug 2024 | Open weights |
| FLUX.1 [schnell] | Aug 2024 | Fast generation |
| FLUX.1 Kontext | Sep 2025 | Adobe Photoshop integration |
| **FLUX.2 [dev]** | Nov 2025 | 32B, editing capabilities |
| FLUX.2 [max] | Nov 2025 | Photorealism |
| FLUX.2 [pro] | Nov 2025 | Commercial |
| **FLUX.2 [klein]** | Jan 2026 | Sub-second, 4B/9B |

---

## Model tiers

| Tier | Params | Use case |
|------|--------|----------|
| [max] | 32B | Maximum quality |
| [pro] | 32B | Commercial |
| [dev] | 32B | Open weights |
| [klein] 9B | 9B | Fast, high quality |
| [klein] 4B | 4B | Consumer GPU (~8GB VRAM) |

---

## FLUX.2 [klein] features

| Feature | Details |
|---------|---------|
| Speed | <1 second on GB200 |
| VRAM | ~8GB (4B on RTX 3090/4070+) |
| Capabilities | Text-to-image, editing, multi-reference |
| License | Apache 2.0 (4B version) |

---

## Partnerships

| Partner | Deal |
|---------|------|
| [[Meta]] | $140M multi-year ($35M Y1, $105M Y2) |
| [[Adobe]] | Photoshop Generative Fill integration |
| Cloudflare | Workers AI deployment |
| [[NVIDIA]] | FP8 quantization collaboration |

---

## Hardware requirements

| Model | VRAM |
|-------|------|
| FLUX.2 32B (full) | 90GB |
| FLUX.2 32B (FP8) | ~54GB |
| FLUX.2 [klein] 4B | ~8GB |

---

## Competitive position

| vs | Flux advantage | Weakness |
|----|---------------|----------|
| [[Stable Diffusion]] | Speed, quality | Ecosystem maturity |
| [[DALL-E]] | Open source, local | Integration |
| [[Midjourney]] | Open, customizable | Community size |

---

## Related

- [[Black Forest Labs]] — parent actor
- [[Stable Diffusion]] — competitor
- [[DALL-E]] — competitor
- [[Firefly]] — Adobe partner
- [[Generative AI]] — category
