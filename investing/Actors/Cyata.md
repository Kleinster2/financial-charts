---
aliases: [Cyata Security]
---
#actor #cybersecurity #israel #acquired #ai

# Cyata

[[Tel Aviv]]-based agentic identity security startup — the first control plane for AI agent identities in the enterprise. Founded 2024, emerged from stealth July 2025, acquired by [[Check Point]] ~7 months later (Feb 2026).

---

## Quick stats

| Metric | Value |
|--------|-------|
| HQ | Tel Aviv, [[Israel]] |
| Founded | 2024 |
| Stealth exit | July 2025 |
| Seed | $8.5M (led by [[TLV Partners]]) |
| Acquired | Feb 12, 2026 by [[Check Point]] |
| Deal value | Part of ~$150M three-startup package (Cyata + Cyclops Security + Rotate) |
| Employees at acquisition | ~12 |

---

## What it does

Traditional [[Identity and Access Management]] handles human identities. Non-human identity (NHI) tools handle service accounts and API keys. Neither was designed for autonomous AI agents that chain tools, create accounts, and trigger business actions on their own.

Cyata fills that gap:

| Capability | Detail |
|------------|--------|
| Discovery | Scans cloud and SaaS environments, surfaces all AI agents, maps each to a human owner |
| Monitoring | Tracks agent behavior for risky access patterns and anomalies |
| Governance | Enforces granular access controls — which systems/servers an agent can reach |
| Interrogation | Prompts agents in natural language to explain their reasoning before allowing execution |
| Audit | Logs every interaction (identity, intent, outcome), integrates with SIEM/SOAR/compliance (PCI, SOC 2, ISO 27001) |
| Intervention | Blocks out-of-bounds activity or requires human approval |

The natural-language interrogation feature is the distinctive technical contribution — using AI to audit AI, forcing agents to justify actions in real time.

---

## Team

All [[Unit 8200]] / [[Cellebrite]] alumni. 60% of management from Cellebrite.

| Name | Role | Background |
|------|------|------------|
| Shahar Tal | CEO | 20-year security vet, led malware/vuln research at [[Check Point]], 8 years at [[Cellebrite]] |
| Dror Roth | VP R&D | [[Talpiot]] graduate, tech leader at [[Cellebrite]] and Talon Cyber Security |
| Baruch Weizman | CTO | [[Unit 8200]] section head, early employee at Paragon |
| Gilad Roth | Chief Engineer | [[Talpiot]] graduate, founding engineer at Argus Security and Talon Cyber Security |

Angel investors included former [[Cellebrite]] CEOs Ron Serber and Yossi Carmil.

---

## Acquisition by Check Point (Feb 2026)

[[Check Point]] acquired Cyata alongside Cyclops Security (~$85M) and Rotate ([[acquihire]]) on Feb 12, 2026. Combined deal ~$150M. CEO Nadav Zafrir framed it as expanding Check Point's AI security stack for agentic governance.

Seed-to-acquisition in ~7 months — textbook Israeli cyber velocity. The speed reflects both the urgency of the [[Agentic AI security]] category and Check Point's need to stay relevant against platform players like [[Palo Alto Networks]] and [[CrowdStrike]].

Shahar Tal's prior Check Point tenure likely accelerated diligence. Founder-acquirer familiarity is a recurring pattern in Israeli cyber M&A.

---

## Why it matters

Cyata is an early signal that [[Agentic AI security]] is becoming a real market, not just a concept. The category is bifurcating:

| Layer | Focus | Examples |
|-------|-------|---------|
| Prompt security | Prevent injection, misuse | Prompt Armor, Lakera |
| Agent identity/governance | Control what agents can do | Cyata |
| Infrastructure security | Secure the compute layer | [[Cloudflare]], Zero Networks |

Cyata occupies the governance layer — the most enterprise-friendly and compliance-aligned, which explains why [[Check Point]] (enterprise DNA) bought it rather than a prompt-security startup.

---

## Related

- [[Check Point]] — acquirer
- [[Unit 8200]] — team origin
- [[Cellebrite]] — team origin, angel investors
- [[TLV Partners]] — seed investor
- [[Agentic AI security]] — category
- [[Israel]] — ecosystem
- [[Cybersecurity]] — sector
- [[CyberTech Global Tel Aviv 2026]] — context (Israeli cyber at record funding)

---

*Created 2026-02-15*
