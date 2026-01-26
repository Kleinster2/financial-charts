---
aliases: [Clawd, clawd.bot]
---
#actor #ai #opensource #software #austria

**Clawdbot** — open-source personal AI assistant that runs locally, maintains persistent memory, and connects to messaging platforms. Created by [[Peter Steinberger]].

---

## Why Clawdbot matters

Local-first AI agent with memory — runs 24/7 on your hardware, not the cloud:

| Metric | Value |
|--------|-------|
| GitHub stars | ~18,500 |
| License | MIT |
| Language | TypeScript |
| Runtime | Node.js 22+ |
| Launched | Late 2025 |

---

## What makes Clawdbot different

**Persistent memory:** Unlike [[Claude]] or [[ChatGPT]], Clawdbot doesn't start blank each session. Stores memories as Markdown files (Obsidian-style vaults), preserving context across days/weeks.

**Multi-channel:** Connects to [[WhatsApp]], [[Telegram]], [[Slack]], [[Discord]], [[iMessage]], [[Signal]], [[Teams]], [[Google Chat]], [[Matrix]] — wherever you already communicate.

**Agentic:** Handles multi-day tasks autonomously:
- Email monitoring and responses
- Calendar management
- Browser automation
- Newsletter drafting (runs at 3 AM while you sleep)

**Self-hosted:** Runs as background daemon (launchd/systemd) on macOS, Linux, Windows (WSL2). Your data stays local.

---

## Architecture

| Component | Function |
|-----------|----------|
| Gateway daemon | Background service, always running |
| Memory store | Markdown files (Obsidian-compatible) |
| LLM backend | Claude, OpenAI, or other models |
| Channel adapters | Messaging platform integrations |

Philosophy: "Apps will melt away. The prompt is your new interface."

---

## Creator

**[[Peter Steinberger]]** ([@steipete](https://twitter.com/steipete)):
- Vienna-based developer
- Founded [[PSPDFKit]] (PDF SDK)
- Known for high-quality macOS/iOS development

**Core team:**
- Peter Steinberger — creator, "lobster whisperer"
- Mario Zechner (@badlogicc) — security, Pi creator

---

## Origin story

Started as Steinberger's personal assistant named "Clawd" — a space lobster character. His Mac Mini in Vienna runs at 3 AM drafting newsletters and responding to messages while he sleeps. Personal tool → open-source phenomenon.

Mascot: Space lobster named Clawd. Tagline references Doctor Who's TARDIS. Leans into absurdism.

---

## Implications

**For [[AI agents]]:** Demonstrates the local-first, memory-persistent model. Cloud assistants reset context; Clawdbot accumulates it.

**For [[Open source commoditization]]:** High-quality AI tooling going open-source, competing with proprietary assistants.

**For personal AI:** Shows what's possible when an AI assistant runs continuously with full context — not session-based chat but ongoing relationship.

---

## Quick stats

| Metric | Value |
|--------|-------|
| GitHub | [clawdbot/clawdbot](https://github.com/clawdbot/clawdbot) |
| Website | [clawd.bot](https://clawd.bot/) |
| Stars | ~18,500 |
| Creator | [[Peter Steinberger]] |

*Updated 2026-01-25*

---

## Related

- [[Peter Steinberger]] — creator
- [[AI agents]] — category this represents
- [[Open source commoditization]] — open-source AI tooling trend
- [[Claude]] — one of the LLM backends
- [[OpenAI]] — alternative LLM backend
- [[Obsidian]] — memory stored as Obsidian-compatible Markdown
