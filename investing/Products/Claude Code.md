---
aliases:
  - Claude Code CLI
tags:
  - product
  - ai
parent_actor: "[[Anthropic]]"
---

# Claude Code

[[Anthropic]]'s terminal-based coding agent. Agentic AI that edits files, runs commands, creates PRs. Part of the [[Claude]] product family. Hit $2.5B run rate by Feb 2026 — more than half from enterprise.

---

## Current capabilities

| Feature | Description |
|---------|-------------|
| File operations | Read, edit, create files |
| Command execution | Run shell commands |
| Git integration | Commits, PRs, branch management |
| Subagents | Spawn specialized agents for tasks |
| Plan mode | Multi-step task orchestration |
| IDE integration | VS Code, JetBrains |

---

## TeammateTool / Swarm Mode (Feb 2026)

Upcoming feature — found in v2.1.19, currently feature-flagged:

| Capability | Description |
|------------|-------------|
| Role-based subagents | Specialist teammates for different tasks |
| Plan mode coordinators | Orchestration across agents |
| Broadcast messaging | Team-wide communication |
| Parallel execution | Multiple agents working simultaneously |
| tmux backend | Process isolation for teammates |

Why it matters:
- Single-agent Claude uses 80-90% context before reset
- Team orchestration uses ~40%, each teammate carries own context
- Tasks that take 1 agent 2 hours → swarm does in 30 minutes

Status: Fully implemented, gated behind feature flags. Not yet in official docs.

---

## GitHub penetration (Feb 2026)

4% of GitHub public commits now authored by Claude Code. Projected to reach 20%+ of daily commits by end of 2026. Business subscriptions quadrupled since start of 2026.

---

## Quick stats

| Metric | Value |
|--------|-------|
| Parent | [[Anthropic]] |
| Product family | [[Claude]] |
| Category | AI coding agent |
| Run rate | $2.5B (Feb 2026) |
| Revenue mix | >50% enterprise |
| Launch | May 2025 (public) |

*Updated 2026-02-17*

---

## Related

- [[Anthropic]] — parent company
- [[Claude]] — product family
- [[Cursor]] — competitor
- [[GitHub Copilot]] — competitor
- [[Agentic AI]] — category
- [[AI agents]] — broader category
