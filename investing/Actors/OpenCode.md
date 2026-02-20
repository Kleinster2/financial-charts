---
aliases: [opencode, OpenCode AI, opencode-ai]
---
#actor #ai #devtools #opensource

**OpenCode** — Open-source AI coding agent built for the terminal. 100K+ GitHub stars, 700 contributors, 2.5M monthly developers. Created by the team behind SST (serverless framework). The leading open-source alternative to [[Cursor]] and Claude Code.

---

## Quick stats

| Metric | Value |
|--------|-------|
| GitHub stars | 100K+ |
| Monthly developers | 2.5M+ |
| Contributors | 700+ |
| Commits | 9,000+ |
| Founded | June 19, 2025 |
| HQ | San Francisco (distributed) |
| Funding | Unfunded (bootstrapped from SST profits) |
| Language | Go |
| License | Open source |

---

## Founders

| Name | Role | Background |
|------|------|------------|
| **Jay V** | CEO | Co-creator of SST framework |
| **Frank Wang** | CTO | Co-creator of SST framework |
| **Dax Raad** | Co-founder | Early SST user (joined 2021), also created Zen |
| **Adam Elmore** | Co-founder | Friend of founding team |

The team previously built **SST** — an open-source framework for building cloud applications that raised $1M after demo day, grew to 25K GitHub stars, and turned profitable in 2025.

---

## Products

| Product | Description | Pricing |
|---------|-------------|---------|
| **OpenCode** (core) | Open-source terminal coding agent | Free (BYOK — bring your own API key) |
| **Zen** | Curated set of optimized coding models hosted by OpenCode | Paid subscription |
| **Black** | Premium tier with access to all top models | $20/mo base (matches Cursor Pro) |
| **Desktop app** | GUI version of the coding agent | Included |
| **IDE extension** | Editor integration | Included |

**Business model:** Open-source core (free) + hosted model service (Zen/Black). Similar to the open-core model — give away the agent, monetize the model routing.

---

## Key features

- **Model agnostic** — 75+ LLM providers through Models.dev, including local models
- **LSP enabled** — automatically loads the right language servers for the LLM
- **Multi-session** — run multiple agents in parallel on the same project
- **Share links** — share session links for debugging/reference
- **GitHub Copilot integration** — use your existing Copilot subscription
- **ChatGPT Plus/Pro** — use your OpenAI subscription
- **Privacy-first** — does not store code or context data

---

## Origin story

The SST team noticed that developers were spending more time working with AI models than writing code directly. Jay V saw that existing tools (Cursor, GitHub Copilot) were closed-source and locked to specific providers. The insight: developers want an agent they can trust, modify, and run with any model — including local ones.

OpenCode launched June 19, 2025 and hit viral adoption immediately, reaching 60K GitHub stars by January 2026 and 100K+ by February. Unlike Cursor (IDE-based) or Claude Code (Anthropic-only), OpenCode was designed from day one to be provider-agnostic and terminal-native.

---

## Competitive landscape

| Tool | Model lock-in | Open source | Interface | Price |
|------|--------------|-------------|-----------|-------|
| **OpenCode** | None (any model) | ✅ Yes | Terminal + Desktop + IDE | Free (BYOK) or $20/mo (Zen) |
| **Cursor** | Multi-model | ❌ No | IDE (VS Code fork) | $20/mo |
| **Claude Code** | Anthropic only | ❌ No | Terminal | $20/mo (Max plan) |
| **GitHub Copilot** | OpenAI/GitHub | ❌ No | IDE extension | $10-19/mo |
| **Windsurf** (Codeium) | Multi-model | ❌ No | IDE | $10-15/mo |
| **Codex CLI** | OpenAI only | ✅ Yes | Terminal | API costs |

**OpenCode's moat:** Open source + model agnostic. Developers who don't want vendor lock-in gravitate here. The 100K star count and community momentum create a self-reinforcing adoption loop.

---

## Investment angle

**Not directly investable** (private, unfunded). But relevant as:
- Threat to [[Cursor]] (Anysphere), Windsurf/Codeium, and GitHub Copilot revenue
- Validation of open-source AI tooling winning developer mindshare
- Potential acqui-hire target for cloud/AI companies
- Signal that developer tools may commoditize faster than expected — bad for closed-source coding tool valuations

---

## Related

- [[Cursor]] — primary competitor (closed-source IDE)
- [[Anthropic]] — Claude models used via OpenCode
- [[OpenAI]] — GPT/Codex models used via OpenCode
- [[OpenRouter]] — alternative model routing layer
- [[GitHub Copilot]] — competitor (Microsoft/OpenAI)
- [[AI agents]] — category context

*Created 2026-02-19*
