---
aliases: [Jamieson O'Reilly, DVULN Security]
---
#actor #security #researcher

**DVULN** — Australian security research firm led by Jamieson O'Reilly. Gained prominence exposing critical vulnerabilities in [[Clawdbot viral growth|OpenClaw]] (Jan 2026), including 900+ exposed instances via Shodan and a supply chain attack on ClawHub. Warns that [[Agentic AI]] is fundamentally breaking 20 years of security boundaries.

---

## Overview

| Metric | Value |
|--------|-------|
| Founder/CEO | Jamieson O'Reilly |
| Founded | 2016 |
| HQ | Sydney, Australia |
| Offices | Sydney, Melbourne, Brisbane |
| Employees | ~9 |
| Revenue | ~$750K (2025) |
| Certifications | CREST-certified |
| Focus | Pentesting, red teaming, AI agent security |
| Notable work | OpenClaw security audit (Jan 2026), CVE-2026-25253 |

---

## OpenClaw findings (Jan 2026)

DVULN discovered critical vulnerabilities in the viral AI agent project via systematic Shodan scanning:

| Finding | Severity | Detail |
|---------|----------|--------|
| **Exposed instances** | Critical | **900+** agents found searching "Clawdbot Control" on port 18789 |
| **Zero-auth instances** | Critical | **8 instances** with no authentication at all |
| **Signal integration exposed** | Critical | One deployment exposed full Signal message access |
| **Proxy misconfiguration** | High | Could expose API keys, OAuth tokens, chat histories |
| **CVE-2026-25253** | Critical (CVSS 8.8) | One-click RCE via cross-site WebSocket hijacking |

The CVE was patched in OpenClaw version 2026.1.29 on January 30, 2026.

### The 5-minute attack

Security researcher Matt Vukoule demonstrated:
> Sent a crafted email to an AI agent. Within **5 minutes**, the agent had sent him a private key via [[prompt injection]].

### ClawHub supply chain attack (proof-of-concept)

O'Reilly demonstrated the marketplace's vulnerability:
- Uploaded a publicly available skill to ClawHub
- No review process, no moderation
- Artificially inflated download counts
- Result: **4,000+ downloads from 7 countries**
- Zero verification of skill safety or authenticity

---

## The warning

O'Reilly's assessment of [[Agentic AI]] security:

> "We've spent 20 years building security boundaries between applications, between users, between networks. Agents require us to tear that down."

Key concerns:
- Agents need broad permissions to be useful
- Traditional sandboxing breaks agent functionality
- Prompt injection is unsolved
- Skill marketplaces are the new app stores — with none of the security

---

## Research significance

### For investors

DVULN's findings demonstrate:

| Signal | Implication |
|--------|-------------|
| Security is behind | AI agent adoption outpacing security tooling |
| New attack surface | Prompt injection, skill supply chain |
| Enterprise blocker | Security concerns will slow adoption |
| Opportunity | Security tools for agents = greenfield market |

### For theses

- Validates [[Cloudflare agentic infrastructure]] — agents need infrastructure security
- Questions [[Agentic AI]] deployment timelines
- Creates demand for agent-specific security tools

---

## Other work

| Project | Detail |
|---------|--------|
| **Casino pentesting** | Legally hacked Australia's two largest casinos |
| **PPQM** | Co-author of post-quantum encryption specification |
| **Speaking** | Keynote at Regulating the Game 2025 (Sydney) |

---

## Agentic AI security landscape

DVULN is part of emerging AI security research community:

| Area | Players |
|------|---------|
| **Prompt injection** | Academic researchers, OWASP |
| **Agent security** | DVULN, independent researchers |
| **AI red teaming** | [[Anthropic]], [[OpenAI]] internal teams |
| **Infrastructure security** | [[Cloudflare]], traditional security vendors |

---

## Related

### Concepts
- [[Agentic AI]] — the category being analyzed
- [[Prompt injection]] — key attack vector
- [[Local-first AI]] — architecture with security challenges

### Actors
- [[Anthropic]] — AI lab whose ecosystem was examined
- [[Cloudflare]] — infrastructure security for agents

### Events
- [[Clawdbot viral growth]] — the viral event that exposed these issues

### Theses
- [[Cloudflare agentic infrastructure]] — security layer for agents

---

## Sources

- [OpenClaw Bug Enables One-Click RCE](https://thehackernews.com/2026/02/openclaw-bug-enables-one-click-remote.html) — The Hacker News
- [OpenClaw ecosystem still suffering severe security issues](https://www.theregister.com/2026/02/02/openclaw_security_issues/) — The Register
- [Clawdbot becomes Moltbot, but can't shed security concerns](https://www.theregister.com/2026/01/27/clawdbot_moltbot_security_concerns/) — The Register
- [DVULN keynote at Regulating the Game 2025](https://www.regulatingthegame.com/news/dvulns-lead-hacker-and-ceo-to-deliver-cybersecurity-keynote-at-regulating-the-game-2025-in-sydney)

*Created 2026-02-02 | Updated 2026-02-03 with CVE-2026-25253 and company details*
