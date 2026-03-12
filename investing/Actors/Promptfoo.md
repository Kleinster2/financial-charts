---
aliases: [promptfoo, Promptfoo Inc]
tags: [actor, ai, security, usa, private, acquired]
---

# Promptfoo

**Promptfoo** — open-source AI security testing platform acquired by [[OpenAI]] (announced Mar 9, 2026) to bolster the security layer of [[OpenAI Frontier]], its enterprise agent platform. Founded in 2024 by [[Ian Webster]] (ex-[[Discord]]) and [[Michael D'Angelo]] (ex-Smile Identity), Promptfoo built both an MIT-licensed CLI/framework for red-teaming LLM applications (12.6k GitHub stars, 350k+ developers) and a commercial enterprise platform for automated pentesting, guardrails, and compliance monitoring. Used by 25%+ of the Fortune 500. Last valued at $86M post-money (Series A, Jul 2025). Total funding: $23.6M from [[Andreessen Horowitz]] and [[Insight Partners]]. Deal price undisclosed but almost certainly a significant premium — 8 months of growth between Series A and acquisition (from 100k to 350k+ developers, from 30 to 125+ Fortune 500 teams). The acquisition pattern is familiar — OpenAI buying security and agent expertise externally rather than building in-house (cf. [[Steinberger OpenAI acqui-hire]], Statsig acquisition) — and the timing tracks with the broader AI agent security arms race: [[Anthropic]] launched Claude Code Security in Feb 2026, and enterprise CIOs consistently cite security/governance as the #1 barrier to scaling AI deployments.

---

## Quick stats

| Metric | Value |
|--------|-------|
| Founded | 2024 (project started 2022) |
| HQ | San Mateo, California |
| CEO / Co-founder | [[Ian Webster]] |
| CTO / Co-founder | [[Michael D'Angelo]] |
| Employees | 23 |
| Last valuation | $86M post-money (Series A, Jul 2025) |
| Total funding | $23.6M |
| GitHub stars | 12.6k |
| Contributors | 248+ |
| Developer adoption | 350k+ |
| Fortune 500 penetration | 25%+ (~125 teams) |
| Certifications | SOC2, ISO 27001 |
| Acquirer | [[OpenAI]] |
| Deal announced | Mar 9, 2026 |
| Deal price | Undisclosed |

---

## Synopsis

Promptfoo is the most widely adopted open-source framework for testing and red-teaming LLM applications. The core product is a CLI and library (MIT-licensed, provider-agnostic — supports 50+ model providers including [[GPT]], Claude, Gemini, Llama) that lets developers evaluate prompts, agents, and RAG systems against adversarial attacks: prompt injection, data leakage, jailbreak attacks, unsafe tool execution, and out-of-policy agent behavior. The commercial enterprise platform adds automated red-team simulations, real-time guardrails, code scanning for LLM vulnerabilities, compliance monitoring with audit trails, and CI/CD pipeline integration.

The strategic logic of the [[OpenAI]] acquisition is straightforward. As OpenAI pushes agents (via Frontier) into production enterprise workflows — where they access CRMs, data warehouses, internal tools — the attack surface enlarges dramatically. 78% of CIOs cite governance, compliance, and data security as the top barrier to scaling AI solutions (Futurum research). Promptfoo's 25%+ Fortune 500 penetration gives OpenAI an instant enterprise security credibility layer. The team of 23 — both founders, engineers, go-to-market, operations — all join OpenAI. Promptfoo's capabilities will be integrated directly into Frontier: automated red-teaming for agent workflows, shift-left security evaluation, and compliance monitoring. OpenAI pledged the open-source framework will remain MIT-licensed with continued multi-provider support — though the inherent tension between an open-source community tool and integration into one of the most powerful enterprise AI platforms is real and unresolved.

---

## Product

### Open-source framework (free, MIT license)

CLI and library for evaluating LLM applications. Install via `npm`, `brew`, or `pip`. Supports:
- Prompt evaluation and comparison across 50+ providers
- Red-team attack simulation (prompt injection, jailbreaks, data exfiltration)
- Agent and RAG system testing
- Custom evaluation metrics and assertions
- CI/CD integration for regression testing across model versions

### Enterprise platform (commercial)

- Automated red-team simulations using specialized adversary models/agents
- Real-time guardrails for production LLM applications
- Code scanning for LLM vulnerabilities
- Compliance monitoring and audit trails
- Model Security product
- MCP Proxy
- Industry-specific solutions (financial services, insurance, telecom, real estate)

---

## Funding

| Round | Date | Amount | Lead | Key Participants |
|-------|------|--------|------|-----------------|
| Seed | Jul 28, 2024 | $5.18M | [[Andreessen Horowitz]] | Tobi Lutke (CEO, [[Shopify]]), Stanislav Vishnevskiy (CTO, [[Discord]]), Frederic Kerrest (co-founder, [[Okta]]), Adam Ely (EVP/CISO, [[Fidelity]]) |
| Series A | Jul 2025 | $18.4M | [[Insight Partners]] (Ganesh Bell) | [[Andreessen Horowitz]] (Zane Lackey, Joel de la Garza) |
| Total | | $23.6M | | Post-money: $86M at Series A |

Seed to acquisition: ~20 months. Series A to acquisition: ~8 months.

Key a16z investors were security-domain specialists: Zane Lackey (GP; founder of Signal Sciences, acquired by [[Fastly]]) and Joel de la Garza (Investment Partner; former CISO of [[Box]]).

---

## Founders

[[Ian Webster]] — CEO & Co-founder
- Dartmouth College
- Led LLM engineering and developer platform teams at [[Discord]], scaling AI products to 200M users
- Started building Promptfoo in 2022 as a solo project while still at Discord
- At launch (Jul 2024), already had 25,000 developers using the open-source tool at companies including [[Shopify]], [[Amazon]], and [[Anthropic]]

[[Michael D'Angelo]] — CTO & Co-founder
- BS Electrical/Computer Engineering, University at Buffalo; MS Computational & Mathematical Engineering, Stanford
- Former VP of Engineering & Head of ML at Smile Identity — scaled identity verification APIs serving 160M+ people across Africa
- Co-founded Arthena (quantitative art investment platform, acquired by [[Masterworks]]) and Matroid
- Longtime friend of Webster

---

## OpenAI acquisition (Mar 9, 2026)

### Deal structure

Full acquisition, not an acqui-hire. Entire product, team, IP, open-source project, and enterprise customer base transfer to [[OpenAI]]. All 23 employees absorbed. Both founders continue in leadership roles. Deal price undisclosed. Subject to customary closing conditions.

### Integration plan

Promptfoo capabilities will be built directly into [[OpenAI Frontier]]:
- Automated red-teaming for enterprise agent workflows
- Shift-left security evaluation during development
- Compliance monitoring and audit trails for governance
- Regression testing across model versions

Early Frontier customers: [[Uber]], [[State Farm]], [[Intuit]], [[Thermo Fisher Scientific]]. Consulting partners: [[Accenture]], [[BCG]], [[Capgemini]], [[McKinsey]].

### Open-source commitment

OpenAI pledged Promptfoo will "remain open source under its current licence, with continued support for existing customers." Multi-provider support (not just OpenAI models) will continue. Founders stated: "We will continue to maintain the open-source suite as a best-in-class red teaming, static scanning, and evals tool for any AI model or application."

### Strategic context

Srinivas Narayanan (OpenAI's B2B applications CTO): "Promptfoo brings deep engineering expertise in evaluating, securing and testing AI systems" at enterprise scale.

Mitch Ashley (Futurum Group, VP Practice Lead): "Adoption precedes the acquisition rationale" — the market validated the need before OpenAI confirmed it. Enterprise procurement is a "governance gate, not preference." Sees "accelerating pattern among AI platform vendors acquiring governance and security capabilities."

Concurrent moves in AI agent security:
- [[OpenAI]] released Codex Security (AI-powered application security agent for software repos)
- [[Anthropic]] launched Claude Code Security (Feb 2026) for vulnerability scanning
- Agent security described as "defining commercial battleground in enterprise AI"

---

## Related

### Actors
- [[OpenAI]] — acquirer, integrating into Frontier enterprise platform
- [[Andreessen Horowitz]] — seed lead, continued at Series A
- [[Insight Partners]] — Series A lead
- [[Ian Webster]] — CEO/co-founder
- [[Michael D'Angelo]] — CTO/co-founder
- [[Discord]] — where Webster built the initial project

### Events
- [[Steinberger OpenAI acqui-hire]] — prior OpenAI acquisition in agent/security space (Feb 2026)

### Concepts
- [[Agentic AI]] — the threat model Promptfoo addresses
- [[AI extensibility]] — agent security as the governance layer

### Theses
- [[OpenAI personal agent moat]] — Promptfoo adds the enterprise security layer needed for agent deployment at scale

---

## Sources

- [OpenAI official announcement](https://openai.com/index/openai-to-acquire-promptfoo/) — Mar 9, 2026
- [Promptfoo blog: "Promptfoo is joining OpenAI"](https://www.promptfoo.dev/blog/promptfoo-joining-openai/) — Mar 9, 2026
- [TechCrunch: OpenAI acquires Promptfoo](https://techcrunch.com/2026/03/09/openai-acquires-promptfoo-to-secure-its-ai-agents/) — Mar 9, 2026
- [CNBC: OpenAI to buy cybersecurity startup Promptfoo](https://www.cnbc.com/2026/03/09/open-ai-cybersecurity-promptfoo-ai-agents.html) — Mar 9, 2026
- [Bloomberg: OpenAI Buying AI Security Startup Promptfoo](https://www.bloomberg.com/news/articles/2026-03-09/openai-buying-ai-security-startup-promptfoo-to-safeguard-ai-agents) — Mar 9, 2026
- [Futurum Group: OpenAI Acquires Promptfoo](https://futurumgroup.com/insights/openai-acquires-promptfoo-gaining-25-foothold-in-fortune-500-enterprises/) — Mar 2026
- [Insight Partners: Promptfoo Series A](https://www.insightpartners.com/ideas/promptfoo-raises-18-4-million-series-a-to-build-definitive-ai-security-stack/) — Jul 2025

*Created 2026-03-12*
