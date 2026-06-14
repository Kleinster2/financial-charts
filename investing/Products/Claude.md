---
aliases:
  - Claude AI
  - Claude 3
  - Claude 3.5
  - Claude 4
  - Claude 4.5
  - Claude 4.6
  - Claude 4.8
tags:
  - product-family
  - ai
parent_actor: "Anthropic"
parent_concept: "Frontier models"
---

# Claude

[[Anthropic]]'s AI assistant family. Known for reasoning, coding, and safety. Competes with [[ChatGPT]].

Structure: One model family with generations (3, 3.5, 4, 4.5, 4.6, 4.8) and capability tiers:
- [[Claude Fable 5]] / [[Claude Mythos]] — Capybara tier, above Opus (Mythos-class). Fable 5 is the safety-gated public model (Jun 9 2026); Mythos 5 the restricted [[Project Glasswing]] sibling
- [[Claude Opus]] — Deep reasoning; prior public flagship (Opus 4.8)
- [[Claude Sonnet]] — Balanced performance/cost
- [[Claude Haiku]] — Fastest, cheapest

---

## Scale

| Metric | Value |
|--------|-------|
| Professional users | ~18.9M |
| Annualized revenue | $6B+ ARR added in Feb 2026 alone (All-In pod, Mar 27). $3B+ (summer 2025) |
| Context window | 200K tokens (500K enterprise) |
| Launch | March 2023 |

Enterprise-focused: 80% of Anthropic's revenue from enterprise customers. [[Chamath Palihapitiya]] (8090 Capital, Mar 27 2026): *"From an enterprise lens, particularly through 8090, it's all Anthropic all the time... the quality of that technical team and what they create, it's head and shoulders above anything else."* [[Michael Dell]] called [[Claude Opus|Opus 4.6]] a model that *"hit a threshold that we haven't seen before in terms of real productivity in teams."*

---

## Version history

| Version | Release | Key changes |
|---------|---------|-------------|
| Claude | Mar 2023 | Initial launch |
| Claude 2 | Jul 2023 | 100K context, improved coding |
| Claude 2.1 | Nov 2023 | 200K context, reduced hallucination |
| Claude 3 | Mar 2024 | Opus/Sonnet/Haiku tiers, vision |
| Claude 3.5 Sonnet | Jun 2024 | Matched Opus quality at Sonnet speed |
| Claude 3.5 Haiku | Oct 2024 | Faster, cheaper |
| Claude 3.5 Sonnet v2 | Oct 2024 | Computer use, improved coding |
| Claude 4 | 2025 | Agentic capabilities, extended thinking |
| Claude 4.5 Opus | Feb 2025 | Previous flagship |
| Claude 4.5 Sonnet | 2025 | Balanced tier |
| Claude 4.5 Haiku | 2025 | Fast/cheap tier |
| [[Claude Opus\|Claude Opus 4.6]] | Feb 5 2026 | 1M context, agent teams, 65.4% Terminal-Bench |
| [[Claude Sonnet\|Claude Sonnet 4.6]] | Feb 17 2026 | Opus-level reasoning at Sonnet pricing, 1M context (beta), 72.5% OSWorld |
| [[Claude Opus\|Claude Opus 4.7]] | Apr 16 2026 | Stronger coding, vision, and complex multi-step tasks |
| [[Claude Opus\|Claude Opus 4.8]] | May 28 2026 | Most capable generally available Opus; stronger coding/agentic/professional work, dynamic workflows, effort control, 1M context |
| [[Claude Mythos\|Claude Mythos (Capybara)]] | Apr 2026 preview; Mythos 5 Jun 9 2026 | New tier above Opus. Mythos Preview / Mythos 5 restricted to [[Project Glasswing]] (cyber capability). |
| [[Claude Fable 5]] | Jun 9 2026 | First public Mythos-class model; safety-gated GA sibling of Mythos 5. 1M context, $10/$50, classifiers fall back to Opus 4.8. Suspended for all customers Jun 12 2026 (US export-control ban). |

---

## Current model family

| Model | Positioning | API pricing (per M tokens) |
|-------|-------------|---------------------------|
| [[Claude Fable 5]] | Most capable widely released; Mythos-class (suspended Jun 12 2026, US export ban) | $10 input / $50 output |
| [[Claude Opus\|Opus 4.8]] | Opus-tier flagship; reasoning and agents (refusal fallback for Fable 5) | $5 input / $25 output; fast mode $10 / $50 |
| [[Claude Sonnet\|Sonnet 4.6]] | Balanced, default (free + pro) | $3 input / $15 output |
| [[Claude Haiku\|Haiku 4.5]] | Fastest, cheapest | $0.80 input / $4 output |

Batch API offers 50% discount for async processing. 1M context window is available for Opus 4.8; Anthropic also offers US-only inference at 1.1x pricing.

As of June 12, 2026, [[Claude Fable 5|Fable 5]] and [[Claude Mythos|Mythos 5]] are suspended for all customers under a US [[Export controls|export-control]] directive (a [[Howard Lutnick|Commerce]] letter to [[Dario Amodei]]); [[Claude Opus|Opus 4.8]], [[Claude Sonnet|Sonnet 4.6]], and [[Claude Haiku|Haiku 4.5]] remain available. See [[Anthropic#Jun 12 — Commerce export ban; Fable 5 / Mythos 5 taken offline|Anthropic]].

---

## [[Consumer]] pricing

| Plan | Price | Usage |
|------|-------|-------|
| Free | $0 | 30-100 messages/day |
| Pro | $17-20/mo | 5x Free usage |
| Max 5x | $100/mo | 5x Pro |
| Max 20x | $200/mo | 20x Pro, priority |

---

## Enterprise & Team

| Plan | Price | Notes |
|------|-------|-------|
| Team | $25-30/user/mo | Min 5 users |
| Enterprise | Custom | SSO, 500K context, GitHub integration |

---

## Key products

Claude.ai — Web/mobile chat interface (consumer, teams, enterprise)

[[Claude Code]] — Terminal-based coding agent. Agentic, can edit files, run commands, create PRs. Hit $2.5B run rate. See [[Anthropic]] for harness crackdown details.

[[Claude Cowork]] — Enterprise collaboration agent (Jan 2026). Triggered [[Claude Cowork disruption February 2026|$285B software selloff]] when plugins launched Jan 30. Native macOS desktop app announced Feb 17 2026.

Agent SDK — Platform for building custom agents on Claude

---

## Capabilities

- Extended thinking — Multi-step reasoning before responding
- 1M context (beta) — Available on [[Claude Opus|Opus 4.6]] and [[Claude Sonnet|Sonnet 4.6]]
- [[Google]] Workspace — Read/edit Docs, Gmail, Drive (2026)
- Computer use — Can control desktop applications

---

## Distribution

Available through:
- claude.ai (direct)
- AWS Bedrock
- [[Google]] [[Vertex]] AI
- [[Microsoft]] Foundry

Multi-cloud strategy reduces single-vendor dependency.

---

## Competitive position

| vs | Claude advantage | Claude weakness |
|----|-----------------|-----------------|
| [[ChatGPT]] | Reasoning, coding, enterprise trust | Smaller consumer base |
| [[Gemini]] | Independent, safety reputation | Less multimodal |
| Open source | Quality, support, safety | Cost |

---

## Quick stats

| Metric | Value |
|--------|-------|
| Parent | [[Anthropic]] |
| Users | ~18.9M professional |
| Pro price | $20/mo |
| Context | 200K-1M tokens (1M beta) |

*Updated 2026-06-13*

---

## Related

- [[Anthropic]] — parent company
- [[Claude Opus]] — most capable tier
- [[Claude Sonnet]] — balanced tier
- [[Claude Haiku]] — fastest/cheapest tier
- [[Claude Code]] — terminal-based coding agent
- [[Claude Cowork]] — enterprise collaboration agent
- [[ChatGPT]] — primary competitor
- [[Gemini]] — [[Google]] competitor
- [[OpenClaw]] — open-source agent that uses Claude as backend; Anthropic C&D forced rebrand from "Clawdbot"
- [[Agentic AI]] — Claude Code's category
- [[AI agents]] — broader category
- [[Claude Fable 5]] — first public Mythos-class model (Jun 9 2026); safety-gated Capybara tier
- [[Claude Mythos]] — Capybara tier; Mythos 5 restricted to [[Project Glasswing]], Fable 5 the public sibling
- [[Claude Cowork disruption February 2026]] — $285B selloff catalyst
- [[February 2026 AI Disruption Cascade]] — software disruption exposure tracked in the event note
