---
aliases:
  - behavioral portability
  - behavioral lock-in
  - intelligence lock-in
  - context portability
tags:
  - concept
  - ai
  - platform
---

# Intelligence portability

The question of whether users can take the behavioral model an AI agent builds of them when they switch providers. Distinct from data portability (which concerns files, messages, records) — intelligence portability concerns the accumulated understanding of how a user works, thinks, and prioritizes.

---

## Why it differs from data portability

| Dimension | Data portability | Intelligence portability |
|-----------|-----------------|------------------------|
| What moves | Files, messages, records, contacts | Behavioral patterns, decision tendencies, communication style |
| Technical format | CSV, JSON, API exports | No standard format exists |
| Legal framework | GDPR, CCPA, data export rights | None |
| Migration path | Export tools, consultants, weeks of work | No migration path exists |
| Switching cost | Painful but finite | Potentially unbounded (user loses compounding) |

Every previous form of platform lock-in attached to stuff:
- [[Microsoft]]: files (Word, Excel, PowerPoint)
- [[Salesforce]]: customer records
- [[Slack]]: communication history

Always-on AI agents (see [[Conway]], [[OpenClaw]]) lock in something different: the accumulated model of how you work. Not your calendar, but the knowledge that you always reschedule your 2 PM on Thursdays. Not your Slack messages, but which ones you respond to in 5 minutes vs. ignore for 3 days. Not your emails, but which three matter to you this morning — learned from months of watching.

---

## The compounding problem

When a user switches away from a persistent agent after months of use, they lose the compounding that made the agent useful. They start over with what analyst Nate B Jones called "a brilliant stranger you have to explain everything to."

The value of a persistent agent is a function of three inputs:
1. User's data (portable)
2. Provider's compute (replaceable)
3. Months of inference and behavioral observation (not portable)

The third component has no owner, no format, and no legal framework.

---

## Unresolved questions

| Question | Status |
|----------|--------|
| Who owns the behavioral model? | No legal precedent |
| Can it be exported? | No technical standard |
| What format would it take? | Undefined |
| Should providers be required to make it portable? | No regulation addresses this |
| Can employers claim employee behavioral models? | Untested |

The employer dimension is particularly acute: if an enterprise deploys a persistent agent and the agent learns how an employee works, that behavioral model becomes an enterprise asset. The enterprise can quantify employee effectiveness through the agent — prove 2x productivity, use it as a retention lever. When the employee leaves, the behavioral model stays. The enterprise retains a partial copy of the employee's working intelligence.

Jones argues behavioral context portability policies should ship before persistent agent products like [[Conway]], not after. Whether the industry self-regulates, whether regulators act, or whether convenience overwhelms the question remains open.

---

## Three eras framing

| Era | Period | Competition axis |
|-----|--------|-----------------|
| Models | 2023-2024 | Benchmarks, training runs, context windows (GPT vs Claude vs Gemini) |
| Interfaces | 2025 | Who owns the surface where people work ([[Claude Code]], [[Cursor]], [[OpenClaw]], Windsurf) |
| Persistence | 2026+ | Who owns the always-on layer — the agent that accumulates context, wakes on events, acts autonomously |

All three major labs ([[Anthropic]], [[OpenAI]], [[Google]]) have converged on the same insight: the model is a loss leader. The persistent agent layer — the thing that holds memory, context, workflows, integrations — is the money product. Whoever owns that layer has customer lock-in unlike anything seen before.

*Source: Nate B Jones, "I Analyzed 512,000 Lines of Leaked Code" (Apr 8 2026)*

---

## Quick stats

| Metric | Value |
|--------|-------|
| Legal framework | None |
| Technical standard | None |
| Regulatory attention | None |
| Key products | [[Conway]] (Anthropic, unreleased), [[OpenClaw]] (open-source) |

---

## Related

- [[Conway]] — [[Anthropic]]'s unreleased always-on agent that would create this lock-in
- [[OpenClaw]] — open-source alternative with user-owned persistence
- [[Anthropic]] — building proprietary persistence layer
- [[OpenAI]] — converging on same strategy
- [[Google]] — converging on same strategy
- [[AI extensibility]] — technical layer where portability breaks down
- [[Model Context Protocol]] — open standard, but proprietary layers sit on top
- [[Agent harnesses]] — current-era competition being superseded by persistence
- [[Agentic AI]] — broader category
- [[Platform economics]] — historical parallels (Microsoft 1990s, Apple App Store 2008)
