---
aliases: [Jameson O'Reilly, DVULN Security]
---
#actor #security #researcher

**DVULN** — Security research firm led by Jameson O'Reilly. Gained prominence exposing critical vulnerabilities in [[Clawdbot viral growth|OpenClaw]] (2025), including localhost authentication bypass and hundreds of exposed instances. Warns that [[Agentic AI]] is fundamentally breaking 20 years of security boundaries.

---

## Overview

| Metric | Value |
|--------|-------|
| Researcher | Jameson O'Reilly |
| Firm | DVULN |
| Focus | AI security, agent vulnerabilities |
| Notable work | OpenClaw/Clawdbot security audit (2025) |

---

## OpenClaw findings (2025)

DVULN discovered critical vulnerabilities in the viral AI agent project:

| Finding | Severity | Detail |
|---------|----------|--------|
| **Localhost auth bypass** | Critical | Default configuration allowed unauthenticated access |
| **Publicly exposed instances** | High | Hundreds of agents accessible from internet |
| **Fully open instances** | Critical | **8 instances** with zero authentication |
| **Prompt injection vector** | High | Malicious emails could extract secrets |

### The 5-minute attack

Security researcher Matt Vukoule demonstrated:
> Sent a crafted email to an AI agent. Within **5 minutes**, the agent had sent him a private key via [[prompt injection]].

### ClawdHub skill marketplace

DVULN tested the community skill marketplace:
- Uploaded a benign test "skill"
- No review process, no moderation
- Within days: **installations from 7 different countries**
- Zero verification of skill safety

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

- DVULN security research disclosures (2025)
- Security conference presentations
- Industry interviews

*Created 2026-02-02*
