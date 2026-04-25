---
aliases:
  - Claude Managed Agents
  - Managed Agents
tags:
  - product
  - ai
  - agents
parent_actor: "Anthropic"
---

# Anthropic Managed Agents

[[Anthropic]]'s hosted agent runtime, launched in public beta on Apr 8, 2026. It packages the agent harness plus production infrastructure: long-lived cloud sessions, sandboxed code execution, checkpointing, credential management, scoped permissions, tracing, and evaluator loops. The pitch is straightforward: developers define the agent once, and Anthropic runs the distributed-systems layer.

---

## What it does

| Capability | What Anthropic manages |
|------------|------------------------|
| Agent definitions | Model, system prompt, tools, MCP servers, skills |
| Sessions | Long-lived cloud sessions with persistent state |
| Execution | Sandboxed code execution and tool orchestration |
| Permissions | Scoped credentials and access controls |
| Monitoring | Session tracing, tool logs, integration analytics |
| Evaluation | Outcome definitions and success-criteria loops |

---

## Architecture

Anthropic's engineering note described Managed Agents as "decoupling the brain from the hands." A planner model decides what to do, while execution workers handle tool use and code-running in parallel.

That architecture matters for two reasons:
- it turns the harness itself into a product, not just the model behind it
- it pushes more of the agent stack inside Anthropic's control plane

Anthropic said the new architecture cut time-to-first-token by 60% at p50 and 90% at p95 versus its earlier implementation. In internal structured file-generation tests, Managed Agents improved task success rates by up to 10 points on harder problems.

---

## Early use cases

| Company | Use case |
|---------|----------|
| [[Notion]] | Client onboarding workflows running through Claude-managed agents |
| [[Sentry]] | Seer handoff from root-cause analysis to code fix + PR creation |

Managed Agents are being pitched across coding, task automation, document processing, and back-office workflows where companies want agent behavior without building their own runtime stack first.

---

## Why it matters

Managed Agents moves [[Anthropic]] from model/API provider toward full agent control plane:
- model provider
- agent harness
- hosted runtime
- permissions and tracing layer

That makes it directly relevant to [[Agent harnesses]] and a close competitive analogue to [[OpenAI Frontier]]. It also explains why edge/runtime names like [[Cloudflare]], [[Fastly]], and [[Akamai]] sold off after launch: the market read Managed Agents as Anthropic internalizing part of the neutral infrastructure layer those companies hoped to own.

See [[Anthropic Managed Agents selloff April 2026]] for the market reaction.

---

## Related

- [[Anthropic]] — owner
- [[Claude]] — model family underneath the product
- [[Agent harnesses]] — concept note for the layer this product turns into a managed service
- [[MCP]] — tool/data connectivity layer Managed Agents can call into
- [[OpenAI Frontier]] — closest direct enterprise agent-platform peer
- [[Anthropic Managed Agents selloff April 2026]] — market impact

---

## Sources

- https://www.anthropic.com/engineering/managed-agents
- https://platform.claude.com/docs/en/managed-agents/overview
- https://platform.claude.com/docs/en/managed-agents/quickstart
- https://www.wired.com/story/anthropic-launches-claude-managed-agents/
- https://www.helpnetsecurity.com/2026/04/09/claude-managed-agents-bring-execution-and-control-to-ai-agent-workflows/
