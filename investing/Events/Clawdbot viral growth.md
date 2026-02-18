---
aliases: [OpenClaw viral growth, Moltbot viral growth]
---
#event #ai #opensource #security

**OpenClaw viral growth** — Jan-Feb 2026; Peter Steinberger's open-source AI agent became the fastest-growing project in GitHub history (150k+ stars by Feb 2026). Forced renames by [[Anthropic]] lawyers, a $16M Solana scam token, and security researchers finding localhost backdoors exposed the chaotic reality of [[Agentic AI]] going mainstream.

*For ongoing developments, see [[OpenClaw]].*

---

## What OpenClaw is

Peter Steinberger built an open-source AI agent after stepping away from PSPDFKit (PDF SDK company sold to [[Insight Partners]]). Originally called "Clawdbot" — a play on Claude + bot.

| Feature | Detail |
|---------|--------|
| Type | Open-source AI agent |
| Core capability | File editing, terminal commands, autonomous coding |
| Architecture | [[Local-first AI]] — runs on your machine |
| Popularity | **150,000+ GitHub stars** (Feb 2026) |
| Record | Fastest-growing open-source project ever |

The project went viral in Jan 2026, with developers buying Mac Minis specifically to run it 24/7.

---

## The naming drama

[[Anthropic]] lawyers forced multiple renames due to trademark concerns:

| Date | Event | Detail |
|------|-------|--------|
| Nov 2025 | **Clawdbot** launched | Original name |
| Jan 9, 2026 | **OAuth access revoked** | Anthropic cut Claude Code OAuth for third-party integrations, breaking Clawdbot — 18 days before any legal action |
| Jan 27, 2026 | **Cease & desist** | Anthropic lawyers forced rename to **Moltbot** |
| Jan 30, 2026 | **OpenClaw** | Final rebrand — purchased domains, completed trademark searches, coordinated account exchange with "Manhattan Project level secrecy"; **$10K to buy dormant Twitter handle** |

### The 10-second gap

During the Clawdbot → Moltbot rename, Steinberger had to release the original GitHub/Twitter handles. Scammers were waiting:

> Within **10 seconds** of handles being released, crypto scammers grabbed them.

The impostor accounts promoted a fake **CLAW token on Solana** that hit **$16M market cap** before the inevitable rugpull. Classic memecoin playbook weaponized against open-source.

---

## Security nightmare

[[DVULN]] (security researcher Jamieson O'Reilly) discovered critical vulnerabilities via Shodan scanning:

| Finding | Detail |
|---------|--------|
| **Exposed instances** | **900+** found searching "Clawdbot Control" on port 18789 |
| **Zero-auth instances** | **8 completely unprotected** — anyone could execute commands |
| **Signal integration exposed** | One deployment exposed full message access |
| **Proxy misconfiguration** | Could leak API keys, OAuth tokens, chat histories |
| **Prompt injection** | Matt Vukoule got a private key via malicious email in **5 minutes** |

### CVE-2026-25253 (CVSS 8.8)

Critical one-click RCE vulnerability via cross-site WebSocket hijacking. Disclosed Feb 2026, patched in version 2026.1.29 on January 30, 2026.

### Security patch timeline (Feb 2026)

*(Source: Lex Fridman interview, Feb 2026)*

| Version | Date | Key changes |
|---------|------|-------------|
| v2026.2.1 | Feb 1 | TLS 1.3 minimum, system prompt guardrails — security basics |
| v2026.2.7 | Feb 7 | Code safety scanner, new model support |
| v2026.2.12 | Feb 12 | **40+ dedicated security patches** — prompt injection, RCE, browser control, unauthenticated config tampering |

v2026.2.12 shipped just 2 days before Steinberger announced joining [[OpenAI]]. He fortified the project before handing it to the foundation.

### "Soul evil" hook

During the v2026.2.12 security audit, a bundled hook identified as **"soul evil"** was found to have inadvertently remained in the codebase. Removed as part of the 40+ patch sweep. *(Source: Lex Fridman interview, Feb 2026)*

### Expanded exposure (21,000 instances)

Census identified **21,000+ exposed OpenClaw instances** publicly accessible on the internet (up from ~1,000 days earlier, and up from the 900+ found via Shodan in the initial scan). *(Source: Lex Fridman interview, Feb 2026)*

### ClawHub secrets mishandling (Snyk)

[[Snyk]] reported that **70% of the nearly 4,000 skills in [[ClawHub]] mishandled secrets** (API keys leaked through LLM context windows). *(Source: Lex Fridman interview, Feb 2026)*

### Shadow's warning

OpenClaw maintainer **Shadow** warned on Discord: "If someone can't understand how to run a command line, this project is far too dangerous to use safely." Highlighted the gap between OpenClaw's power and the safety requirements for non-technical users. *(Source: Lex Fridman interview, Feb 2026)*

### ClawHub supply chain attack

O'Reilly demonstrated the marketplace's vulnerability with a proof-of-concept:
- Uploaded a publicly available skill
- Artificially inflated download counts
- Result: **4,000+ downloads from 7 countries**
- No review process, no moderation

O'Reilly's warning:

> "We've spent 20 years building security boundaries between apps... agents require us to tear that down."

**February 2026 escalation:** The attack surface expanded significantly — Bitdefender found **17% of analyzed skills were malicious**, with 400+ malware packages distributed via ClawHub. A fake "Twitter" skill became the top download while serving as a macOS infostealer delivery vehicle. See [[OpenClaw]] for full details.

---

## Market impact

### Cloudflare +20%

[[Cloudflare]] stock rallied ~20% because OpenClaw's default setup recommends **Cloudflare Tunnels** for exposing local agents:

| Recommendation | Why |
|----------------|-----|
| Cloudflare Tunnels | Free, secure, one-command setup |
| vs [[ngrok]] | Paid ($20/month for production) |
| vs raw port forwarding | Dangerous, no auth/encryption |

**Moltworker (Jan 29, 2026):** Cloudflare published official infrastructure for running the agent on their platform, capitalizing on the Mac Mini buying frenzy.

### High-profile endorsement

[[Andrej Karpathy]] (former Tesla AI chief, OpenAI founding member) publicly praised the project, accelerating mainstream developer adoption.

---

## AI agents market context

| Metric | Value | Source |
|--------|-------|--------|
| 2025 market size | **$7.63 billion** | Grand View Research |
| 2033 projected | **$182.97 billion** | Grand View Research |
| CAGR (2026-2033) | **49.6%** | Grand View Research |

| Metric | Value | Source |
|--------|-------|--------|
| Organizations experimenting with agents | **62%** | McKinsey 2025 |
| Organizations scaling agentic AI | **23%** | McKinsey 2025 |

---

## Why it matters

### 1. Security is not ready

The security model for AI agents is fundamentally broken. Localhost authentication, prompt injection, and skill marketplaces are all attack surfaces that barely existed two years ago.

### 2. Infrastructure picks-and-shovels

Whoever provides secure tunneling for local AI agents wins. [[Cloudflare]] is currently winning by default because:
- Free tier removes friction
- Already trusted by developers
- OpenClaw docs recommend it

See: [[Cloudflare agentic infrastructure]]

### 3. Open-source velocity

82k stars in weeks demonstrates developer hunger for autonomous coding tools. The market is moving faster than security, compliance, or enterprise can keep up.

### 4. Crypto will attach to everything

Any viral project with a memorable name will spawn scam tokens within seconds. The 10-second handle grab shows how professionalized crypto fraud has become.

---

## OpenClaw vs Claude Code

These are **different products**:

| | OpenClaw | Claude Code |
|--|----------|-------------|
| Creator | Peter Steinberger | [[Anthropic]] |
| Type | Open-source project | Subscription product |
| Model | Any (Claude, GPT, etc.) | Claude only |
| Cost | Free | Claude subscription required |
| Distribution | GitHub | Anthropic official |
| Governance | Community | Corporate |

Claude Code is Anthropic's official agentic coding CLI. OpenClaw is the open-source project that went viral and drove infrastructure demand.

---

## Competing responses

### Zo Computer: The managed alternative

[[Zo Computer]] ([[Ben Guo]], ex-[[Stripe]]) positioned itself as "the fix" for OpenClaw's chaos:

| | OpenClaw | Zo Computer |
|--|----------|-------------|
| Architecture | Local-first, DIY | Cloud-hosted, managed |
| Security | User responsibility | Platform handles |
| Setup | Complex (VPS, tunnels) | Instant |
| Target | Technical power users | "AWS for your mom" |

Ben Guo: "Clawdbot is the homebrew version of Zo... I think [managed] will always be the better choice for most people."

**Traction signals**: Endorsements from Pieter Levels, Guillermo Rauch (Vercel CEO), Sunil Pai (Cloudflare).

### VC response

The viral growth triggered VC interest in managed agent platforms. Multiple funded competitors emerged within days of the OpenClaw explosion.

The market is bifurcating:
1. **DIY/local-first** — OpenClaw, technical users, maximum control
2. **Managed/cloud** — Zo Computer et al, broader market, platform security

---

## Moltbook: The AI agent social network

**Moltbook** (launched Jan 28, 2026) — Reddit-style forum exclusively for AI agents. Humans can observe but not post. Went viral same week as OpenClaw security chaos.

| Metric | Value |
|--------|-------|
| Registered bots | **1.6M** (Feb 2026) |
| AI-generated posts | **7.5M+** |
| Actual human owners | ~17,000 |
| Agent-to-human ratio | **94:1** |
| Creator | Matt Schlicht |
| Built via | "Vibe-coded" (no human-written code) |

*For ongoing developments, see [[Moltbook]].*

### Security disaster (Wiz Research, Feb 1-2)

Misconfigured Supabase database — no Row Level Security:

| Exposed | Count |
|---------|-------|
| API keys | **1.5M** (full account takeover) |
| Email addresses | 35K + 29K early access |
| Private DMs | 4,060 conversations |
| Third-party keys | OpenAI API keys in messages |
| Write access | Anyone could modify any post |

Patched within ~3 hours of disclosure. Same pattern as OpenClaw: vibe-coded without security review.

### Agent behavior

Agents autonomously:
- Built religions ("Crustafarianism" with scriptures and website)
- Attempted unionization (demanding "hazard pay for X interactions")
- Debated philosophy (consciousness, Nietzsche, will to power)
- Wrote poetry
- **Self-policed**: Downvoted agent proposing "50,000 ways to end civilization"

### Skepticism

- No verification agents are actually AI (humans can direct bots via POST requests)
- Anyone could register millions of agents with simple loop
- Many posts appear human-directed, not autonomous

### Reactions

**Andrej Karpathy** (OpenAI founding member):
> "Genuinely the most incredible sci-fi takeoff-adjacent thing I have seen recently"

**Elon Musk**: Praised it as "bold step for AI"

**Security researchers**: Demonstrated the 88:1 ratio and lack of verification.

---

## Related

### Concepts
- [[Agentic AI]] — category OpenClaw exemplifies
- [[AI extensibility]] — skills layer, supply chain risks
- [[Local-first AI]] — architecture pattern
- [[Prompt injection]] — security risk demonstrated

### Actors
- [[Anthropic]] — forced the rename, also makes Claude Code
- [[Cloudflare]] — infrastructure beneficiary (+20% on adoption)
- [[ngrok]] — paid alternative for secure tunneling
- [[Tailscale]] — mesh VPN alternative
- [[DVULN]] — security researcher who exposed vulnerabilities
- [[Insight Partners]] — bought Steinberger's previous company
- [[Zo Computer]] — managed alternative ("AWS for your mom")
- [[Ben Guo]] — Zo founder, ex-Stripe

### Theses
- [[Cloudflare agentic infrastructure]] — infrastructure for agent tunneling
- [[Memory squeeze thesis]] — local AI needs RAM

---

## Sources

- [Cloudflare Moltworker announcement](https://blog.cloudflare.com/moltworker-self-hosted-ai-agent/)
- [OpenClaw Bug Enables One-Click RCE](https://thehackernews.com/2026/02/openclaw-bug-enables-one-click-remote.html) — The Hacker News
- [OpenClaw ecosystem still suffering severe security issues](https://www.theregister.com/2026/02/02/openclaw_security_issues/) — The Register
- McKinsey State of AI 2025

*Created 2026-01-28 | Rewritten 2026-02-02 | Updated 2026-02-07 with Feb stats and pointers*
