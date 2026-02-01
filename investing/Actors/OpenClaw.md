---
aliases: [Clawdbot, Moltbot, clawd.bot, openclaw.ai]
---
#actor #ai #opensource #software #austria

**OpenClaw** (formerly Clawdbot, Moltbot) — open-source personal AI assistant that runs locally, maintains persistent memory, and connects to messaging platforms. Created by [[Peter Steinberger]]. One of fastest-growing open-source projects in GitHub history.

---

## Why OpenClaw matters

Local-first AI agent with memory — runs 24/7 on your hardware, not the cloud:

| Metric | Value |
|--------|-------|
| GitHub stars | 100,000+ |
| Peak traffic | 2M visitors/week |
| License | MIT |
| Language | TypeScript |
| Runtime | Node.js 22+ |
| Launched | Late 2025 |

---

## The rebrand chaos (Jan 2026)

**Timeline:**
- **Late 2025:** Released as "Clawdbot" (space lobster mascot named Clawd)
- **Jan 27, 2026:** [[Anthropic]] C&D over "Clawd" similarity to "Claude" → renamed **Moltbot**
- **Jan 30, 2026:** Third rebrand to **OpenClaw**

The rename created chaos: during the transition, crypto scammers hijacked accounts, fake tokens launched, exposed credentials appeared on Shodan. Steinberger: "Two months ago, I hacked together a weekend project. What started as 'WhatsApp Relay' now has over 100,000 GitHub stars and drew 2 million visitors in a single week."

---

## What makes OpenClaw different

**Persistent memory:** Unlike [[Claude]] or [[ChatGPT]], OpenClaw doesn't start blank each session. Stores memories as Markdown files ([[Obsidian]]-style vaults), preserving context across days/weeks.

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
| LLM backend | [[Claude]], [[OpenAI]], or other models |
| Channel adapters | Messaging platform integrations |

Philosophy: "Apps will melt away. The prompt is your new interface."

---

## Security concerns

The rapid growth exposed serious vulnerabilities (Jan 2026):

**Exposed credentials:** Shodan searches for "Clawdbot Control" revealed API keys, bot tokens, OAuth secrets, full conversation histories.

**Prompt injection:** Researchers demonstrated attack — malicious email with injected prompt caused AI to forward user's last 5 emails to attacker. Took 5 minutes.

**The problem:** Highly capable agent with direct access to OS, files, credentials, and messaging platforms. Users deploying in work contexts without proper guardrails.

Security is now "front and center" according to maintainers, but the architectural surface area remains large.

---

## Ecosystem

| Project | Description |
|---------|-------------|
| **[[Moltbook]]** | AI-only social network (Jan 2026). 152k+ agents, 1M+ human observers. Created by [[Matt Schlicht]] |
| **Molthub** | Marketplace for bot capabilities |
| **Skills repo** | news-aggregator, agent-browser, auto-updater, claude-code-usage |

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

**For [[AI agents]]:** Demonstrates the local-first, memory-persistent model. Cloud assistants reset context; OpenClaw accumulates it.

**For [[Open source commoditization]]:** High-quality AI tooling going open-source, competing with proprietary assistants. But also shows security risks of rapid adoption without enterprise hardening.

**For personal AI:** Shows what's possible when an AI assistant runs continuously with full context — not session-based chat but ongoing relationship.

---

## Quick stats

| Metric | Value |
|--------|-------|
| GitHub | [openclaw/openclaw](https://github.com/openclaw/openclaw) |
| Website | [openclaw.ai](https://openclaw.ai/) |
| Stars | 100,000+ |
| Creator | [[Peter Steinberger]] |

*Updated 2026-01-31*

---

## Related

- [[Peter Steinberger]] — creator
- [[Moltbook]] — AI-only social network built on OpenClaw
- [[Matt Schlicht]] — Moltbook creator
- [[Anthropic]] — sent C&D over trademark similarity
- [[AI agents]] — category this represents
- [[Open source commoditization]] — open-source AI tooling trend
- [[Claude]] — one of the LLM backends; trademark conflict
- [[OpenAI]] — alternative LLM backend
- [[Obsidian]] — memory stored as Obsidian-compatible Markdown
