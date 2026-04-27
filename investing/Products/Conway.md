---
aliases:
  - Conway agent
  - Anthropic Conway
tags:
  - product
  - ai
  - agents
parent_actor: "Anthropic"
status: unreleased
---

# Conway

[[Anthropic]]'s reported unreleased always-on agent environment, discovered in the [[Claude Code]] source leak (Mar 31 2026). Not announced by Anthropic or on its public roadmap — an internal project revealed when a packaging error pushed ~512,000 lines of TypeScript to the public npm registry.

Conway operates as a standalone sidebar inside the [[Claude]] interface — not a chat window, a full agentic environment. It opens a dedicated page tied to a Conway instance.

---

## Reported architecture (Apr 2026 leak snapshot)

Three core sections:

| Section | Function |
|---------|----------|
| Search | Discovery and retrieval |
| Chat | Conversational interface |
| System | Extensions, connectors, triggers |

### Extensions (CNW.zip format)

Conway uses a proprietary extension format — CNW.zip — that sits on top of [[Model Context Protocol|MCP]]. Extensions include custom interface panels, information handlers, and tools that run specifically inside Conway's environment. They are not portable MCP tools — they are Conway-only.

The extension ecosystem functions as an app store for agent capabilities. If Anthropic launches Conway to [[Claude]] subscribers, extensions would be discoverable inside the environment where users already work — no separate installation required.

This creates a developer choice parallel to the iPhone App Store in 2008:

| Path | Portability | Distribution |
|------|-------------|-------------|
| Standard MCP tool | Works with Claude, [[ChatGPT]], [[Gemini]] | No built-in discovery mechanism |
| Conway extension (CNW.zip) | Conway-only | Built-in extensions directory |

The pattern mirrors [[Google]] Play Services on Android: MCP is the open foundation, Conway's extension ecosystem is the proprietary layer on top. [[Anthropic]] gets the credibility of publishing an open standard and the commercial advantage of building valuable tooling in a format that runs only in their environment.

### Connectors and tools

Services plugged into the Conway instance, including a toggle that lets Claude-in-Chrome connect directly. Shows which external services are integrated. Reporting on the leaked interface also described Conway as able to run [[Claude Code]] directly from the instance, making it a background agent surface rather than just a Claude chat sidebar.

### Automatic triggers

Public web addresses that outside services can ping to wake the agent. Toggleable per service — determines which external events can activate Conway without user initiation. Notification support makes the loop useful: Conway can wake on an event, work in the background, and alert the user when a task completes or a condition is met.

---

## Platform strategy context

Conway is not an isolated product. It is the capstone of a platform strategy [[Anthropic]] executed across Q1 2026:

| Surface | Product | Function |
|---------|---------|----------|
| Developer tool | [[Claude Code]] (+ Channels) | Discord/Telegram notifications for async task management |
| Enterprise tool | [[Claude Cowork]] | Non-technical user agent (~95% of enterprise workforce) |
| Always-on agent | Conway | Persistent, event-driven, extension ecosystem |
| Distribution | Claude Marketplace | Enterprise procurement — partner apps ([[GitLab]], [[Harvey]], [[Snowflake]]) billed through Anthropic; no commission yet |
| Enforcement | Third-party tool ban | Subscription access restricted to Anthropic-built surfaces |

Each piece pushes in the same direction: if you use [[Claude]], you use it through Anthropic-built surfaces.

Analyst Nate B Jones compared this to [[Microsoft]]'s 1990s arc — DOS to Windows to Office to Active Directory in ~15 years — but compressed to ~15 months. Conway is the Active Directory play: the piece that makes the stack sticky because the persistent agent knows the organization in a way nothing else does.

---

## Lock-in implications

Previous platform lock-in attached to data: [[Microsoft]] locked in files, [[Salesforce]] locked in customer records, [[Slack]] locked in communication history. Data is painful to migrate but technically possible.

Conway would lock in the accumulated behavioral model of how a user works — which emails get immediate responses vs. three-day ignores, which meetings get rescheduled, how decisions are prioritized under noise. This model does not export. There is no CSV of "how this person thinks," no migration consultant for behavioral context.

After 6 months of use, switching means losing the compounding that made the agent useful — starting over with what Jones called "a brilliant stranger you have to explain everything to."

See [[Intelligence portability]] for the concept and its unresolved legal/regulatory questions.

---

## Status

Unreleased. Discovered via leaked source code, not announced by [[Anthropic]]. Feature flags in the leaked code also referenced "persistent assistant" background mode and remote phone/browser control capabilities that align with Conway's architecture.

All three major labs ([[Anthropic]], [[OpenAI]], [[Google]]) appear to be converging on the same insight: the model is a loss leader, the persistent agent layer is the money product. Conway is Anthropic's entry in this race.

*Sources: Nate B Jones analysis of Claude Code source leak (Apr 8 2026); TestingCatalog / Dataconomy reporting on Conway interface details (Apr 1-3 2026); Roborhythms Conway summary (Apr 14 2026). Original leak Mar 31 2026.*

---

## Quick stats

| Metric | Value |
|--------|-------|
| Parent | [[Anthropic]] |
| Product family | [[Claude]] |
| Status | Unreleased (reported internal project) |
| Confirmation | Not officially announced by [[Anthropic]] |
| Discovered | Mar 31 2026 (source leak) |
| Extension format | CNW.zip (proprietary, on top of MCP) |
| Architecture | Standalone sidebar — search, chat, system |

---

## Related

- [[Anthropic]] — parent company
- [[Claude]] — product family
- [[Claude Code]] — source leak that revealed Conway
- [[Claude Cowork]] — sister product (non-technical agent)
- [[Model Context Protocol]] — open standard Conway builds proprietary layer on
- [[AI extensibility]] — Conway's extension model
- [[Agent harnesses]] — Conway as next evolution: persistence layer
- [[OpenClaw]] — open-source competitor with similar always-on architecture
- [[Intelligence portability]] — the lock-in concept Conway creates
- [[Long Anthropic]] — Conway strengthens platform moat thesis
- [[OpenAI personal agent moat]] — competing always-on agent vision
