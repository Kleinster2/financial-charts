# Agent harnesses

The infrastructure layer that makes AI agents actually work. "2025 was agents. 2026 is agent harnesses."

---

## The stack

Three layers emerging in agent infrastructure:

| Layer | Role | Examples |
|-------|------|----------|
| **Runtime** | Execution, state management | LangGraph |
| **Framework** | Abstractions, building blocks | LangChain, AutoGen, CrewAI |
| **Harness** | Batteries-included, production-ready | Claude Code, Codex, Devin |

**Analogy:** Model = CPU, context window = RAM, harness = operating system.

---

## What harnesses provide

| Capability | Why it matters |
|------------|----------------|
| **Planning tools** | To-do lists for long-term coherence |
| **Filesystem/memory** | Context management across sessions |
| **Subagent spawning** | Task delegation, parallel work |
| **Human-in-the-loop** | Approval gates for critical actions |
| **Tool orchestration** | Right tools, right order, error handling |
| **Self-testing loops** | Autonomous debugging and iteration |

**Key insight:** You can't download harnesses from Hugging Face. Manus took 6 months and 5 rewrites. LangChain spent a year on 4 architectures. This is where competitive moats form.

---

## Competitive landscape

### Harnesses (production-ready agents)

| Company | Product | Valuation/Status | Notes |
|---------|---------|------------------|-------|
| [[Anthropic]] | Claude Code, Agent SDK | Private | Production, proven |
| [[OpenAI]] | Codex | Private | GPT-5-Codex, 7+ hr autonomous runs |
| [[Meta]] | Manus | Acquired ~$2B+ | **Uses Claude as core engine** |
| Cognition | Devin + Windsurf | $4B | SWE-1.5 model, 13x faster than Sonnet |
| [[Anysphere]] | Cursor | $29.3B | $1B ARR, acquired Graphite |
| [[Amazon]] | Q Developer | AWS | Agentic coding in IDE |
| Replit | Agent 3 | Private | 200 min autonomous, self-testing |
| [[Google]] | (building) | — | Acqui-hired Windsurf team $2.4B |

### Frameworks (building blocks)

| Company | Product | Notes |
|---------|---------|-------|
| LangChain | LangChain + LangGraph | Most adopted, runtime + framework |
| LangChain | DeepAgents | Their harness layer |
| [[Microsoft]] | AutoGen | Multi-agent collaboration |
| CrewAI | CrewAI | Role-based, lower learning curve |

### Adjacent

| Company | Product | Notes |
|---------|---------|-------|
| Harness Inc. | AI DevOps | $5.5B, "after-code" automation |

---

## Why harnesses win

| Factor | Framework | Harness |
|--------|-----------|---------|
| Time to production | Weeks/months | Hours/days |
| Reliability | You build it | Battle-tested |
| Maintenance | Your problem | Provider's problem |
| Customization | Maximum | Constrained but sufficient |

**The shift:** As models improve, harnesses matter more. Better models make the "smart logic" developers wrote yesterday obsolete — harnesses let you rip it out and upgrade.

---

## Investment implications

**Where value accrues:**
- Harness layer captures most value (direct user relationship)
- Framework layer may commoditize (open source pressure)
- Runtime layer is infrastructure (lower margins)

**Winners likely:**
- Vertically integrated (model + harness): Anthropic, OpenAI, Google
- Category leaders with distribution: Cursor, Replit
- Enterprise-focused: Amazon Q Developer

**Watch for:**
- Consolidation (Google acqui-hiring Windsurf team, Meta buying Manus)
- Open source harnesses threatening proprietary ones
- Model providers competing with their own customers

---

## Key metrics to track

| Metric | Why |
|--------|-----|
| Autonomous runtime | How long can agent work without human? |
| Task completion rate | % of tasks finished without intervention |
| Tool call efficiency | Fewer tools = better orchestration |
| Time to production | How fast can devs ship with it? |

---

*Updated 2026-01-11*

## Related

- [[Agentic AI]] — parent concept (market, use cases)
- [[Anthropic]] — Claude Code harness
- [[OpenAI]] — Codex harness
- [[Anysphere]] — Cursor harness ($29B)
- [[Meta]] — acquired Manus
- [[Amazon]] — Q Developer
- [[Google]] — building harness (Windsurf team)
- [[Model Context Protocol]] — agent-tool connectivity standard
