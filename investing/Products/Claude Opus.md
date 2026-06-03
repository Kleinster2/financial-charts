---
aliases:
  - Opus
  - Claude Opus 4.5
  - Claude Opus 4.6
  - Claude Opus 4.7
  - Claude Opus 4.8
  - Opus 4.5
  - Opus 4.6
  - Opus 4.7
  - Opus 4.8
tags:
  - product
  - ai
parent_actor: "Anthropic"
---

# Claude Opus

[[Anthropic]]'s most capable generally available [[Claude]] tier — deep reasoning, complex analysis, agentic tasks. Premium pricing.

---

## Version history

| Version | Release | Notes |
|---------|---------|-------|
| Opus 3 | Mar 2024 | First Opus tier, with Claude 3 launch |
| Opus 4 | 2025 | Extended thinking, agentic capabilities |
| Opus 4.5 | Feb 2025 | Previous flagship |
| Opus 4.6 | Feb 5 2026 | 1M context, agent teams, 65.4% Terminal-Bench |
| Opus 4.7 | Apr 16 2026 | Stronger coding, vision, and complex multi-step tasks |
| Opus 4.8 | May 28 2026 | Most capable generally available Opus; stronger coding/agentic/professional work, dynamic workflows, effort control, improved honesty |

---

## Opus 4.8 launch (May 28, 2026)

[[Claude Opus|Opus 4.8]] is the public bridge between Opus 4.7 and [[Claude Mythos|Mythos-class]] capability. Anthropic positions it as a modest but tangible upgrade over Opus 4.7, with stronger coding, agentic tasks, computer-use/browser-agent performance, financial analysis, legal work, and long-running professional workflows.

The release matters for three reasons:

1. Opus 4.8 is available everywhere immediately — claude.ai, Claude Platform, Amazon Web Services, Google Cloud, and Microsoft Foundry — at unchanged standard pricing of $5/M input tokens and $25/M output tokens.
2. It ships with product-surface upgrades: effort control on claude.ai and Cowork, dynamic workflows for Claude Code, and Messages API support for system entries inside the messages array.
3. Anthropic says Opus 4.8's alignment profile is close to [[Claude Mythos|Claude Mythos Preview]], and that Mythos-class models are expected for all customers in the coming weeks once cyber safeguards are stronger.

For investing-vault purposes, Opus 4.8 is not the main capability shock; it is the public commercialization step that tells us Anthropic is preparing the path for a broader Mythos-class release.

*Source: [Anthropic, Claude Opus 4.8](https://www.anthropic.com/news/claude-opus-4-8), May 28 2026.*

---

## Opus 4.6 benchmarks

| Benchmark | Opus 4.6 | Opus 4.5 | Notes |
|-----------|----------|----------|-------|
| [[Terminal-Bench]] 2.0 | 65.4% | — | #1 agentic coding eval |
| [[Humanity's Last Exam]] | #1 | — | Multidisciplinary reasoning |
| GDPval-AA | +190 Elo vs 4.5 | — | Also +144 Elo vs GPT-5.2 |
| [[ARC-AGI]]-2 | 68.8% | 37.6% | Near-doubling |
| [[OSWorld]] | 72.7% | — | Best computer-use model |
| MRCR v2 (long context) | 76% | 18.5% | 8-needle, 1M token |

---

## Opus 4.6 new capabilities

- 1M token context window (beta, API) — first for Opus-class. Premium pricing above 200K: $10/$37.50 per MTok
- Agent teams — multiple agents splitting tasks in parallel (research preview in [[Claude Code]])
- Adaptive thinking — model picks up contextual cues on extended thinking usage
- Context compaction — auto-summarizes older context during long conversations
- Effort controls — four levels (low/medium/high/max)
- Fast mode — up to 2.5x faster output generation at premium pricing

---

## Pricing

| Tier | Input (per MTok) | Output (per MTok) |
|------|-------------------|-------------------|
| Standard | $5 | $25 |
| Fast mode | $10 | $50 |
| Batch (50% off) | $2.50 | $12.50 |
| US-only inference | 1.1x standard pricing | 1.1x standard pricing |

---

## Quick stats

| Metric | Value |
|--------|-------|
| Parent | [[Anthropic]] |
| Product family | [[Claude]] |
| Current version | Opus 4.8 (May 28 2026) |
| Context | 1M |
| Positioning | Most capable, premium |

*Updated 2026-06-02*

---

## Related

- [[Anthropic]] — parent company
- [[Claude]] — product family
- [[Claude Mythos]] — restricted tier above Opus; expected commercial path in coming weeks
- [[Claude Sonnet]] — balanced tier
- [[Claude Haiku]] — fast/cheap tier
- [[Claude Code]] — primary agentic surface
