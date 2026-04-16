---
aliases:
  - Claude Code CLI
tags:
  - product
  - ai
parent_actor: "[[Anthropic]]"
---

# Claude Code

[[Anthropic]]'s terminal-based coding agent. Agentic AI that edits files, runs commands, creates PRs. Part of the [[Claude]] product family. Hit $2.5B run rate by Feb 2026 — more than half from enterprise. Created by [[Boris Cherny]], who built it as a side project in 2024 and shared it via Slack — it spread organically inside Anthropic before launching publicly in May 2025.

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

## Enterprise adoption signals (Feb 2026)

Bloomberg Businessweek (Feb 26 2026) profiled how coding agents — Claude Code and [[OpenAI]] Codex specifically — are reshaping engineering culture:

| Company | Signal |
|---------|--------|
| **[[Intuit]]** | Engineers 30% more productive (code velocity). CTO Alex Balazs "up at 5 AM writing code" with agents. Product managers vibe-coding [[QuickBooks]] features |
| **DocuSketch** | Tracks "interactions per day" per engineer. Claude Code publishes weekly efficiency reports per engineer |
| **Arcade.dev** | CEO tracks Claude Code bills, pressures engineers to spend more. Bills rose 10x after internal push |

The pattern: senior leaders using coding agents to build things themselves, then raising expectations for engineering teams. [[Vibe coding]] promise of leisure inverted into productivity mandate.

UC Berkeley study (200-person org): workers offloading to AI agents but simultaneously working longer hours. "Task expansion" — non-technical staff vibe-coding creates cleanup work for engineers.

*Source: Bloomberg Businessweek (Feb 26 2026)*

---

## Origin

[[Boris Cherny]] built Claude Code as an internal tool in 2024 and shared it on Slack: "I wanted to show off a new tool I've been hacking on." It spread organically — "before long, everyone inside the company was using his new tool." Anthropic's existing focus on coders and enterprise meant Cherny had clarity on the user base from the start. WSJ's Ben Cohen (Mar 20 2026): Claude Code "conquered Silicon Valley, jolted Wall Street and even managed to scramble Anthropic's fiercest rival." Cherny is now head of Claude Code.

*Source: WSJ (Ben Cohen, Mar 20 2026)*

---

## Channels (Q1 2026)

Claude Code Channels allows users to message Claude Code through Discord and Telegram and receive notifications when tasks finish. This extends Claude Code from a terminal tool to an async messaging-based workflow — users can assign tasks, go about their day, and get notified of results.

The feature neutralized [[OpenClaw]]'s core appeal of agent interaction through everyday messaging platforms. Analyst Nate B Jones called it part of Anthropic's pattern: first copy community-built features into their closed harness, then lock out the open-source alternative.

The Mar 31 2026 source leak that exposed Claude Code's architecture also revealed [[Conway]] — an unreleased always-on agent with its own extension ecosystem (CNW.zip format). Conway extends the Channels concept further: persistent, event-driven, browser-connected, with automatic triggers from external services.

---

## Quick stats

| Metric | Value |
|--------|-------|
| Creator | [[Boris Cherny]] |
| Parent | [[Anthropic]] |
| Product family | [[Claude]] |
| Category | AI coding agent |
| Run rate | $2.5B (Feb 2026) |
| Revenue mix | >50% enterprise |
| Prototype | 2024 (internal Slack) |
| Public launch | May 2025 |

*Updated 2026-03-21*

---

## Related

- [[Anthropic]] — parent company
- [[Boris Cherny]] — creator and head
- [[Claude]] — product family
- [[Codex]] — [[OpenAI]] competitor
- [[Cursor]] — competitor
- [[GitHub Copilot]] — competitor
- [[Conway]] — unreleased always-on agent (discovered in same source leak)
- [[Agentic AI]] — category
- [[AI agents]] — broader category
- [[Ridges AI]] — decentralized competitor ([[Bittensor]] SN62, ~$12/mo)
- [[Cognition]] — autonomous-agent competitor
