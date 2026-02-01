---
aliases: [diffusion LLMs, non-autoregressive LLMs]
---

Alternative to autoregressive transformers — generate multiple tokens in parallel through iterative denoising.

## How it works

Instead of generating one token at a time (autoregressive), start with random/noisy text and iteratively refine it. Similar to how image diffusion (Stable Diffusion) works, adapted for discrete text.

Like BERT's masked language modeling but applied to generation: fill in gaps across the whole sequence simultaneously.

## Promise

- **Parallel generation** — potentially much faster than autoregressive
- **Better for long outputs** — code diffs, documents
- **Different latency profile** — predictable time regardless of length

## Current limitations

- Quality requires many denoising steps → similar compute to autoregressive
- Tool use is hard — can't interrupt generation for external calls
- Reasoning chains are sequential by nature

## Google Gemini Diffusion

Google announced Gemini Diffusion in context of Nano 2 model — same quality on most benchmarks but much faster generation.

## Use cases

Best suited for:
- Long code diffs (Cursor-style workflows)
- Document generation
- Tasks without mid-generation tool calls

Not suited for:
- Reasoning requiring step-by-step verification
- Agentic workflows with tool use
- Tasks needing external API calls mid-generation

## Outlook

Won't replace autoregressive for state-of-the-art reasoning models. May become the "cheap tier" — fast, good-enough generation for specific use cases.

## Related

- [[Inference-time scaling]] — competing paradigm (more tokens = better)
- [[Google]] — Gemini Diffusion
- [[Cursor]] — potential beneficiary for code diffs
