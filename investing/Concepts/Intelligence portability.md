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

## Apr 26 2026 — memory becomes a product surface

The persistence-layer thesis is now visible in official product surfaces, not just leaked roadmaps or OpenClaw behavior. The important shift: memory is moving from "prompt context" into a first-class product and infrastructure layer.

| Platform | Current memory surface | Investment read |
|----------|------------------------|-----------------|
| [[OpenClaw]] | Local-first files, daily logs, long-term memory, and explicit recall-style workflows | Open reference implementation for user-owned persistence; proves demand but exposes safety, setup, and governance gaps |
| [[Codex]] | Memories carry stable preferences, workflows, tech stacks, project conventions, and pitfalls across threads; Chronicle adds opt-in screen-context memory on macOS Pro | [[OpenAI]] is building the same persistence primitive inside developer tooling before a full consumer agent ships |
| [[Claude Code]] | CLAUDE.md/rules plus auto memory: project-scoped markdown notes Claude writes and recalls across sessions | [[Anthropic]] has an auditable developer-memory substrate that feeds the broader Conway / Cowork / Managed Agents platform strategy |
| [[Anthropic Managed Agents]] | Durable session log outside Claude's context window; harness can re-read selected event slices and resume long-horizon work | Persistence becomes hosted infrastructure, not just local files; enterprise lock-in shifts toward the agent control plane |
| [[Conway]] | Reported unreleased always-on agent with triggers, browser/control surfaces, and proprietary extensions; unconfirmed by [[Anthropic]] | The strongest lock-in version: event-driven agent plus proprietary capability ecosystem |

Two details matter for the investable theme.

First, memory is not just "more context." [[Codex]] and [[Claude Code]] both distinguish durable guidance from learned memory. That creates a product taxonomy: rules tell the agent what must be true; memory tells the agent what has become useful through repeated work. Over time, the learned layer becomes harder to switch away from than the tool itself.

Second, the privacy/security disclaimers are the moat boundary. Codex Chronicle is opt-in, macOS-only at launch, not available in the EU/UK/Switzerland, and stores generated memories locally as unencrypted markdown. Claude Code auto memory is also machine-local and auditable. Those constraints are not just compliance footnotes; they show why enterprise buyers may prefer managed persistence layers with permissions, session logs, credential vaulting, and auditability. [[Anthropic Managed Agents]] is the clearest move in that direction.

The open question is whether persistence stays user-owned and portable, or becomes the new proprietary account system. If memory remains local markdown, switching costs are real but inspectable. If memory becomes a vendor-hosted session graph tied to tools, triggers, and permissions, it starts to look like the AI era's Active Directory.

---

## Quick stats

| Metric | Value |
|--------|-------|
| Legal framework | None |
| Technical standard | None |
| Regulatory attention | None |
| Key products | [[Conway]], [[OpenClaw]], [[Codex]] Memories/Chronicle, [[Claude Code]] auto memory, [[Anthropic Managed Agents]] |

---

## Sources

- https://developers.openai.com/codex/memories
- https://developers.openai.com/codex/memories/chronicle
- https://code.claude.com/docs/en/memory
- https://www.anthropic.com/engineering/managed-agents

---

## Related

- [[Conway]] — [[Anthropic]]'s unreleased always-on agent that would create this lock-in
- [[OpenClaw]] — open-source alternative with user-owned persistence
- [[Codex]] — OpenAI developer surface where memories and Chronicle now expose the persistence primitive
- [[Claude Code]] — Anthropic developer surface with auto memory and project-scoped rules
- [[Anthropic Managed Agents]] — hosted runtime where session state becomes durable infrastructure
- [[Anthropic]] — building proprietary persistence layer
- [[OpenAI]] — converging on same strategy
- [[Google]] — converging on same strategy
- [[AI extensibility]] — technical layer where portability breaks down
- [[Model Context Protocol]] — open standard, but proprietary layers sit on top
- [[Agent harnesses]] — current-era competition being superseded by persistence
- [[Agentic AI]] — broader category
- [[Platform economics]] — historical parallels (Microsoft 1990s, Apple App Store 2008)
