---
aliases: [Claude AI, Claude 4.5, Opus, Sonnet, Haiku]
---
#actor #ai #product

**Claude** — [[Anthropic]]'s AI assistant. Known for reasoning, coding, and safety. Competes with [[ChatGPT]].

---

## Scale

| Metric | Value |
|--------|-------|
| Professional users | ~18.9M |
| Annualized revenue | $3B+ (summer 2025) |
| Context window | 200K tokens (500K enterprise) |
| Launch | March 2023 |

Enterprise-focused: 80% of Anthropic's revenue from enterprise customers.

---

## Model family

| Model | Positioning | API pricing (per M tokens) |
|-------|-------------|---------------------------|
| **Opus 4.5** | Most capable, reasoning | $5 input / $25 output |
| **Sonnet 4.5** | Balanced, default | $3 input / $15 output |
| **Haiku 4.5** | Fastest, cheapest | $1 input / $5 output |

Batch API offers 50% discount for async processing.

---

## [[Consumer]] pricing

| Plan | Price | Usage |
|------|-------|-------|
| Free | $0 | 30-100 messages/day |
| Pro | $17-20/mo | 5x Free usage |
| Max 5x | $100/mo | 5x Pro |
| Max 20x | $200/mo | 20x Pro, priority |

---

## Enterprise & Team

| Plan | Price | Notes |
|------|-------|-------|
| Team | $25-30/user/mo | Min 5 users |
| Enterprise | Custom | SSO, 500K context, GitHub integration |

---

## Key products

**Claude.ai** — Web/mobile chat interface (consumer, teams, enterprise)

**Claude Code** — Terminal-based coding agent. Agentic, can edit files, run commands, create PRs. Hit $1B milestone. See [[Anthropic]] for harness crackdown details.

**Claude Cowork** — Enterprise collaboration agent (Jan 2026). "Claude Code for the rest of your work." Agentic file management, document creation, multi-step tasks. Triggered [[Claude Cowork disruption February 2026|$285B software selloff]] when plugins launched Jan 30.

**Agent SDK** — Platform for building custom agents on Claude

---

## Claude Code — Deep Dive

### Current capabilities

| Feature | Description |
|---------|-------------|
| File operations | Read, edit, create files |
| Command execution | Run shell commands |
| Git integration | Commits, PRs, branch management |
| Subagents | Spawn specialized agents for tasks |
| Plan mode | Multi-step task orchestration |
| IDE integration | VS Code, JetBrains |

### TeammateTool / Swarm Mode (Feb 2026)

**Upcoming feature** — found in v2.1.19, currently feature-flagged:

| Capability | Description |
|------------|-------------|
| Role-based subagents | Specialist teammates for different tasks |
| Plan mode coordinators | Orchestration across agents |
| Broadcast messaging | Team-wide communication |
| Parallel execution | Multiple agents working simultaneously |
| tmux backend | Process isolation for teammates |

**Why it matters:**
- Single-agent Claude uses 80-90% context before reset
- Team orchestration uses ~40%, each teammate carries own context
- Tasks that take 1 agent 2 hours → swarm does in 30 minutes

**Status:** Fully implemented, gated behind feature flags. Not yet in official docs.

---

## Claude Cowork — Deep Dive

### Timeline

| Date | Event |
|------|-------|
| **Jan 12** | Cowork launches (research preview, Max subscribers) |
| Jan 16 | Expands to Pro subscribers |
| Jan 23 | Expands to Team/Enterprise |
| **Jan 30** | **Plugins launch** — 11 open-source job-specific plugins |
| Feb 3-4 | **$285B market selloff** ("SaaSpocalypse") |

### Cowork plugins (Jan 30)

| Plugin | Target |
|--------|--------|
| Legal | Contract review, legal research |
| Financial | Analysis, modeling |
| Sales | Lead gen, CRM automation |
| Marketing | Campaign creation, content |
| Data viz | Charts, reporting |
| Enterprise search | Cross-tool search |

### Market impact

See [[Claude Cowork disruption February 2026]] and [[AI workflow disruption basket]] for full analysis.

Software P/E compression: 33x → 23x (-30%). Hardest hit: [[Thomson Reuters]] (-18%), [[RELX]] (-14%), [[LegalZoom]] (-20%).

---

## Capabilities

- **Extended thinking** — Multi-step reasoning before responding
- **200K context** — Understands multi-file codebases
- **[[Google]] Workspace** — Read/edit Docs, Gmail, Drive (2026)
- **Computer use** — Can control desktop applications

---

## Distribution

Available through:
- claude.ai (direct)
- AWS Bedrock
- [[Google]] [[Vertex]] AI
- [[Microsoft]] Foundry

Multi-cloud strategy reduces single-vendor dependency.

---

## Competitive position

| vs | Claude advantage | Claude weakness |
|----|-----------------|-----------------|
| [[ChatGPT]] | Reasoning, coding, enterprise trust | Smaller consumer base |
| [[Gemini]] | Independent, safety reputation | Less multimodal |
| Open source | Quality, support, safety | Cost |

---

## Quick stats

| Metric | Value |
|--------|-------|
| Parent | [[Anthropic]] |
| Users | ~18.9M professional |
| Pro price | $20/mo |
| Context | 200K-500K tokens |

*Updated 2026-02-04*

---

## Related

- [[Anthropic]] — parent company
- [[ChatGPT]] — primary competitor
- [[Gemini]] — [[Google]] competitor
- [[OpenClaw]] — open-source agent that uses Claude as backend; Anthropic C&D forced rebrand from "Clawdbot"
- [[Agentic AI]] — Claude Code's category
- [[AI agents]] — broader category
- [[Claude Cowork disruption February 2026]] — $285B selloff catalyst
- [[AI workflow disruption basket]] — tracking software disruption exposure
