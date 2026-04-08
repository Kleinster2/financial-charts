---
aliases:
  - Hermes AI
  - Hermes Agent Framework
tags:
  - product
  - ai
  - agent-harness
  - open-source
parent: "[[Nous Research]]"
type: product
launched: 2026-03
license: MIT
---

# Hermes Agent

Open-source persistent AI agent framework built by [[Nous Research]]. Not a developer toolkit like [[LangChain]] or [[CrewAI]] — a deployable autonomous agent that runs on your server, remembers across sessions, and generates reusable skills from completed tasks. Runs on a $5/month VPS with local inference, positioning it as the privacy-first, cost-minimized alternative to cloud-dependent harnesses.

---

## How it works

The core differentiator is the learning loop. When Hermes Agent completes a task, it creates a skill file — a reusable template that can be applied to similar future tasks without re-deriving the approach. Combined with persistent memory (context survives across sessions) and multi-model reasoning, this means the agent improves its own performance over time. LangChain and [[CrewAI]] are frameworks you build on; [[Anthropic|Claude Code]] and [[Anysphere|Cursor]] are harnesses for developers; Hermes Agent is a general-purpose autonomous agent you deploy and interact with.

The architecture connects a single gateway process to 14+ messaging platforms — [[Telegram]], [[Discord]], [[Slack]], WhatsApp, Signal, Email, CLI, Matrix, Mattermost, and more. Six terminal backends (local, Docker, SSH, Daytona, Singularity, Modal) handle execution. 40+ built-in tools cover web search, browser automation, vision, image generation, and TTS. Model-agnostic: 200+ models via [[OpenRouter]], plus native support for Nous Portal, Google AI Studio, [[xAI]], Ollama, vLLM, and llama.cpp.

---

## Quick stats

| Metric | Value |
|--------|-------|
| Parent | [[Nous Research]] |
| First release | v0.2.0 (Mar 12, 2026) |
| Current version | v0.8.0 (Apr 8, 2026) |
| GitHub stars | 36.4K |
| Forks | 4.6K |
| Open issues | 2,118 |
| Language | Python (93.6%) |
| License | MIT |
| Messaging platforms | 14+ |
| Built-in tools | 40+ |
| Supported models | 200+ (via OpenRouter) |

Release cadence: 7 releases in 4 weeks (v0.2.0 → v0.8.0), roughly one per 4 days.

---

## Competitive position

| Agent | Stars | Category | Key difference |
|-------|-------|----------|----------------|
| [[OpenClaw]] | ~349K | General-purpose persistent agent | Category creator, largest ecosystem (247K devs, 5,700+ skills on ClawHub) |
| Hermes Agent | 36.4K | General-purpose persistent agent | Self-improving learning loop, crypto-native, privacy-first, $5/mo VPS |
| [[AutoGen]] ([[Microsoft]]) | ~54.6K | Multi-agent framework | Conversation-based multi-agent orchestration |
| [[CrewAI]] | ~44.3K | Multi-agent framework | Role-playing agent crews, 5.2M monthly downloads |

Hermes Agent competes directly with [[OpenClaw]] in the persistent autonomous agent category — not with developer harnesses like [[Anthropic|Claude Code]], [[Anysphere|Cursor]], or [[OpenAI|Codex]]. The agentskills.io standard (supported by Hermes Agent) has been adopted by 11+ tools including Claude Code and Cursor.

---

## Related

- [[Nous Research]] — parent company
- [[Agent harnesses]] — landscape and taxonomy
- [[Long agent harnesses]] — investment thesis
- [[OpenClaw]] — primary competitor
- [[OpenRouter]] — model distribution

### Cross-vault
- [Technologies: Hermes Agent](obsidian://open?vault=technologies&file=Hermes%20Agent) — technical architecture, gateway, learning loop, skills hub
- [Technologies: agentskills.io](obsidian://open?vault=technologies&file=agentskills.io) — skill format standard
- [Technologies: OpenClaw](obsidian://open?vault=technologies&file=OpenClaw) — competitor architecture
