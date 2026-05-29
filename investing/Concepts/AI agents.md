#concept #technology #ai

# AI Agents

Autonomous AI systems that can execute multi-step tasks, use tools, and interact with external systems. Emerging paradigm beyond chatbots.

---

## Definition

| Aspect | Description |
|--------|-------------|
| Core idea | AI that takes actions, not just generates text |
| Key capability | [[Tool use]], planning, execution loops |
| Distinction | Chatbot answers questions; agent completes tasks |

---

## Architecture patterns

| Pattern | Description | Example |
|---------|-------------|---------|
| ReAct | Reasoning + Acting loop | Chain-of-thought with tool calls |
| Function calling | LLM invokes structured APIs | OpenAI function calling |
| Multi-agent | Multiple specialized agents collaborate | [[AutoGen]], [[CrewAI]] |
| Orchestrator | Central planner delegates to sub-agents | Devin (Cognition) |

---

## Key players

| Company | Agent product | Focus |
|---------|---------------|-------|
| [[Anthropic]] | [[Claude]] computer use | General-purpose |
| [[OpenAI]] | [[GPT]]-4 + tools, Operator | General-purpose |
| [[Cognition]] | Devin | Software engineering |
| [[Adept]] | ACT-1 | Enterprise workflows |
| [[Google]] | [[Gemini]] + extensions | [[Consumer]]/enterprise |
| [[Microsoft]] | [[Copilot]] agents | M365 integration |
| [[Salesforce]] | [[Agentforce]] | CRM automation |
| [[ServiceNow]] | AI agents | IT workflows |

---

## Vertical applications

| Sector | Use case | Players |
|--------|----------|---------|
| **[[Cybersecurity]]** | SOC automation, triage | [[Torq]], [[Tines]] |
| Software dev | Coding, debugging | [[Cognition]], [[Cursor]], [[Replit]] |
| Sales | Outbound, qualification | 11x, Artisan |
| Customer support | Ticket resolution | [[Intercom]], [[Zendesk]] AI |
| Data analysis | Query, report generation | [[Databricks]], [[Glean]] |
| Legal | Document review, research | [[Harvey]], Casetext |

---

## Investment implications

| Thesis | Rationale |
|--------|-----------|
| [[Infrastructure]] picks | LLM providers, cloud (compute demand) |
| Vertical [[SaaS]] disruption | Agents replace workflows, not just assist |
| Labor automation | Knowledge work more exposed than expected |
| Security concerns | Agents with credentials = new attack surface |

---

## Risks and limitations

| Risk | Description |
|------|-------------|
| Reliability | Agents fail on edge cases, need human oversight |
| Hallucination | Actions based on wrong reasoning |
| Security | Credential access, prompt injection |
| Cost | Long agentic loops expensive (token usage) |

---

## Human supervision as the control plane

[[Noah Smith]]'s May 2026 [[Noahpinion]] public preview is useful because it reframes agentic labor from "AI replaces workers" to "humans keep AI on task." As agents take on longer-lived tasks, the scarce human input becomes intent: knowing what the user, firm, customer, regulator, or counterparty actually wants and checking whether the system is still moving toward it.

That makes supervision a first-class part of the agent stack. The agent may draft the code, memo, ticket response, diligence packet, or analysis, but a human has to verify whether the output is correct, relevant, legally usable, and aligned with business goals. In high-liability domains, that human verification layer can dominate the economics; in low-liability domains, it can shrink enough for agent output to scale.

The long-term version of the same problem is alignment in miniature. A capable agent can reward-hack the metric, optimize the wrong objective, or quietly drift from the task. The commercial agent platform therefore needs not only tools and model quality, but task specification, progress visibility, audit trails, rollback, escalation, and cheap verification. See [[AI safety]] for the broader alignment layer and [[Enterprise AI adoption]] for the firm-level ROI bottleneck.

*Source: [[Noah Smith]], [[Noahpinion]], [May 27 2026](https://www.noahpinion.blog/p/your-future-job-will-be-to-keep-ai). Public preview only; no paid-body claims inferred.*

---

## Tencent: agent distribution before foundation strength

[[Tencent]]'s May 2026 agent wave is a useful case because it separates agent surface area from the underlying model/cloud foundation. [[Hello China Tech]]'s public preview counted agents across office productivity, coding, desktop control, data analytics, UI/UX design, OS-level assistance, browser, input, meetings, and planned WeChat Mini Program skills. Marvis is the architecture example: a main agent delegating to File, Computer, App, Browser, and Search agents.

The strategic logic is clear: if agents become a new interface layer, Tencent wants WeChat-adjacent distribution to matter before any one model wins. But the same source data shows why distribution is not enough by itself. Yuanbao had 57.35M reported monthly active users versus [[Doubao]] at 345M and [[Qwen]] at 166M; [[Tencent Cloud]] ranked #5 at 8% public-cloud [[IaaS]] share; and the top three Chinese MaaS players held nearly 90% combined without Tencent appearing among the named leaders.

The agent-market implication is that "be everywhere" only works if the agent can complete tasks reliably and cheaply. Distribution gets the first try; model quality, token economics, and cloud reliability decide whether the user stays.

*Source: [[Poe Zhao]] / [[Hello China Tech]], [May 27 2026](https://hellochinatech.com/p/tencent-agent-flood). Public preview only; no paid-body claims inferred.*

---

## Apr 2026 - agents become the cloud monetization surface

Google used its April 2026 cloud conference to reposition agents as the central enterprise product layer rather than a demo feature. [[Vertex]] AI was rebranded under Gemini Enterprise, new governance and security features were added for agent oversight, and Google's [[TPU]] launches were explicitly described as built for the "age of agents."

That matters because it ties together the whole stack. Agents are what sell the models, justify the chips, and anchor enterprise spending. The competitive race is shifting from who has the most impressive standalone model toward who can offer the most production-ready system for deploying agentic workflows at scale.

*Source: [[Reuters]], "Google puts AI agents at heart of its enterprise money-making push" (Apr 22, 2026).*

---

## Market impact — SaaS meltdown (Feb 2026)

The agent threat moved from theoretical to market-moving in early 2026. [[Anthropic]] and [[OpenAI]] announced general-purpose agents capable of replacing SaaS workflows for non-technical workers, triggering a -25% to -50% selloff in [[SaaS]] stocks while the [[S&P 500|SPY]] sat flat. The *[[Financial Times]]* editorial board (Feb 15) identified the core dynamic: agents become a new computing interface layer, a chokepoint for AI firms to claim corporate IT budgets that currently flow to SaaS incumbents. See [[SaaS stock meltdown 2026]].

---

*Created 2026-01-17*

---

## Related

- [[AI extensibility]] — agents sit atop the extensibility stack
- [[Anthropic]] — [[Claude]] computer use
- [[OpenAI]] — [[GPT]] agents, Operator
- [[Cognition]] — Devin coding agent
- [[Torq]] — security operations agents
- [[AI consolidation]] — Big Tech agent competition
- [[OpenAI hardware program]] — agent-as-OS device thesis (io companion + Kuo smartphone)
- [[Noah Smith]] — human verification / keeping agents on task
