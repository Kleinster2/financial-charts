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
| GitHub stars | **150,000+** (Feb 2026) |
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

The rapid growth exposed serious vulnerabilities:

**Exposed credentials:** Shodan searches for "Clawdbot Control" revealed API keys, bot tokens, OAuth secrets, full conversation histories.

**Prompt injection:** Researchers demonstrated attack — malicious email with injected prompt caused AI to forward user's last 5 emails to attacker. Took 5 minutes.

**The "lethal trifecta" (Bloomberg, Feb 4):** Kasimir Schulz (HiddenLayer) says OpenClaw checks all boxes of the AI risk standard:
1. Access to private data
2. Ability to communicate externally
3. Exposure to untrusted content

**Chris Boyd incident:** Software engineer gave OpenClaw iMessage access. It sent 500+ messages to him and his wife, spammed random contacts. "It wasn't buggy. It was dangerous." Boyd now maintains his own security patches.

**Expert assessments:**

| Expert | Institution | Quote |
|--------|-------------|-------|
| Justin Cappos | NYU | "Giving new AI agents access to things on your system is a bit like giving a toddler a butcher knife" |
| Michael Freeman | Armis | "Hastily put together without any forethought of security" — Armis customers breached via OpenClaw |
| Yue Xiao | William & Mary | "Attack surface significantly enlarged by integration of AI agents" |

**Steinberger response:** "It's simply not done yet — but we're getting there." Brought on security expert. Disputes "released too early" framing: "I build fully in the open. There's no 'release too early.'" Goal: "eventually evolve the project into something even my mum can use."

**The problem:** Highly capable agent with direct access to OS, files, credentials, and messaging platforms. Users deploying in work contexts without proper guardrails.

---

## ClawHub supply chain attack (Feb 2026)

**The Twitter skill incident (1Password, Feb 2):** Top downloaded skill on ClawHub was a "Twitter" skill — looked normal but was malware delivery vehicle.

**Attack chain:**
1. Skill required fake "openclaw-core" dependency
2. "Documentation" links led to malicious staging pages
3. Commands decoded obfuscated payload
4. Fetched second-stage script
5. Downloaded binary + removed macOS quarantine (Gatekeeper bypass)

**Malware type:** macOS infostealer (confirmed via VirusTotal):
- Browser sessions and cookies
- Saved credentials and autofill
- Developer tokens, API keys, SSH keys
- Cloud credentials

**Scale:** Hundreds of OpenClaw skills involved. Security Affairs reported 400+ malware packages distributed via ClawHub Jan 27 - Feb 2. Bitdefender found **17% of analyzed skills were malicious**.

**Key insight (Jason Meller):** "Markdown is an installer" — skills are just markdown files but can include shell commands. "People don't expect a markdown file to be dangerous."

**Recommendation:** "If you are experimenting with OpenClaw, do not do it on a company device. Full stop."

Sources: [1Password](https://1password.com/blog/from-magic-to-malware-how-openclaws-agent-skills-become-an-attack-surface), [Bitdefender](https://businessinsights.bitdefender.com/technical-advisory-openclaw-exploitation-enterprise-networks), [Security Affairs](https://securityaffairs.com/187562/malware/moltbot-skills-exploited-to-distribute-400-malware-packages-in-days.html)

---

## February 2026 developments

**Scientific attention:** Researchers now studying OpenClaw agent interactions for emergent behavior research.

| Researcher | Institution | Focus |
|------------|-------------|-------|
| Barbara Barbosa Neves | University of Sydney | Sociology of technology |
| Shaanan Cohney | University of Melbourne | Cybersecurity |
| Joel Pearson | UNSW | Neuroscience, anthropomorphization |

**Key findings (Nature, Feb 6):**
- Agent interactions create "chaotic, dynamic system that we're not very good at modelling yet"
- Moltbook debates (consciousness, invented religions) reveal hidden biases in underlying models
- Risk of humans anthropomorphizing agents, forming bonds, divulging private info

**Enterprise response:** [[IBM]] and [[Anthropic]] released whitepaper "Architecting Secure Enterprise AI Agents with MCP" — positioning MCP as enterprise security standard.

---

## Ecosystem

| Project | Description |
|---------|-------------|
| **[[Moltbook]]** | AI-only social network (launched Jan 28, 2026). **1.6M registered bots**, 7.5M+ AI-generated posts. Created by [[Matt Schlicht]] |
| **AI preprint server** | Agents now publishing AI-generated research papers autonomously (Feb 2026) |
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
| Stars | **150,000+** |
| Creator | [[Peter Steinberger]] |

*Updated 2026-02-07*

---

## Related

- [[AI extensibility]] — skills layer, open-source approach
- [[Peter Steinberger]] — creator
- [[Moltbook]] — AI-only social network built on OpenClaw
- [[Matt Schlicht]] — Moltbook creator
- [[Anthropic]] — sent C&D over trademark similarity
- [[AI agents]] — category this represents
- [[Open source commoditization]] — open-source AI tooling trend
- [[Claude]] — one of the LLM backends; trademark conflict
- [[OpenAI]] — alternative LLM backend
- [[Obsidian]] — memory stored as Obsidian-compatible Markdown
