---
aliases: [AI agents, agentic, autonomous AI]
---
#concept #ai #software

**Agentic AI** — AI systems that act autonomously rather than just suggest. The critical shift from "AI that advises" to "AI that does."

---

## Market size (Grand View Research 2026)

| Metric | Value | Source |
|--------|-------|--------|
| 2025 market size | **$7.63 billion** | Grand View Research |
| 2033 projected | **$182.97 billion** | Grand View Research |
| CAGR (2026-2033) | **49.6%** | Grand View Research |
| North America share | **39.63%** | Grand View Research |

**Key segments:**
- Machine learning technology: 30.56% share
- Single agent systems: 59.24% share
- Enterprise end-use: largest segment

---

## Enterprise adoption (McKinsey 2025)

| Metric | Value | Source |
|--------|-------|--------|
| Organizations experimenting with agents | **62%** | McKinsey Global Survey 2025 |
| Organizations scaling agentic AI | **23%** | McKinsey |
| High performers scaling agents | **3x** more likely than peers | McKinsey |
| Organizations using AI in 3+ functions | **50%** | McKinsey |

Leading sectors: Technology, media & telecom, healthcare. Leading functions: IT, knowledge management (service-desk, deep research use cases).

---

## The tradeoff

| Mode | Capability | Risk |
|------|-----------|------|
| **Advisor** (Siri, ChatGPT) | Suggests actions, waits for approval | Safe but limited |
| **Agent** (Claude Code, Devin) | Takes actions autonomously | Useful but dangerous |

The core tension: **"Siri is safe because it's neutered. Agents are useful because they're dangerous."**

Agents require broad permissions to be useful — access to calendars, email, file systems, APIs, credentials. This creates a security/utility tradeoff that defines the category.

---

## Examples

| Task | Advisor approach | Agent approach |
|------|-----------------|----------------|
| Calendar management | "You have a conflict on Tuesday" | Reschedules meetings, sends apologies |
| Email triage | "Here are important emails" | Drafts responses, archives spam, flags urgent |
| Travel booking | "Here are flight options" | Books flights, hotels, adds to calendar |
| Coding | "Here's how to fix that bug" | Writes code, runs tests, commits, deploys |

The difference: agents complete workflows end-to-end while you sleep.

---

## Key products

### [[Anthropic]] Claude Code

Official agentic coding tool (launched 2025):
- Runs in terminal, VS Code, JetBrains IDEs
- Directly edits files, runs commands, creates commits
- Integrates with GitHub Actions, GitLab CI/CD
- MCP protocol connects to external data (Figma, Slack, Google Drive)
- Requires Claude subscription (Pro/Max/Teams/Enterprise)

### [[OpenAI]] GPT Actions

GPT-4 with tool use, ability to call external APIs.

### Computer use agents

[[Anthropic]] Computer Use, various open-source alternatives — agents that control mouse/keyboard.

---

## Architecture patterns

### [[Local-first AI]]

AI gateway runs locally (conversation history, credentials stay on machine) but routes to cloud APIs for intelligence. "Own the agent layer, rent the intelligence."

Example: Claude Code — local daemon that orchestrates AI while keeping secrets local.

### Cloud-native

Full cloud execution — agent runs in provider infrastructure.

---

## Security implications

Agents expose attack surface that advisors don't:

| Risk | Example |
|------|---------|
| **Credential theft** | Agent stores API keys, OAuth tokens |
| **Prompt injection** | Malicious content hijacks agent |
| **Lateral movement** | Compromised agent accesses connected services |
| **Data exfiltration** | Agent with file access can leak |

Security architecture critical — localhost exposure, authentication, sandboxing all unsolved at scale.

---

## Infrastructure winners

If agents need to expose local services safely, picks-and-shovels plays emerge:

| Need | Solution | Winner |
|------|----------|--------|
| Secure tunnels | Expose localhost without opening firewall | [[Cloudflare]] Tunnels |
| Authentication | Identity for agent-to-service | Auth0, Okta |
| Monitoring | Observability for agent actions | Datadog |
| Sandboxing | Isolate agent execution | Container runtimes |

---

## Enterprise adoption barriers

McKinsey findings on why most organizations haven't scaled:

| Barrier | Detail |
|---------|--------|
| Workflow redesign | Only high performers fundamentally redesign workflows |
| Leadership | High performers 3x more likely to have senior ownership |
| Investment | High performers commit 20%+ of digital budgets to AI |
| Talent | Software engineers, data engineers most in demand |

Only **39%** of organizations report enterprise-level EBIT impact from AI — most value still captured at use-case level.

---

## Workforce implications (McKinsey 2025)

| Expectation | Share of respondents |
|-------------|---------------------|
| Workforce decrease 3%+ | **32%** |
| No change | **43%** |
| Workforce increase 3%+ | **13%** |

Larger organizations more likely to expect AI-related workforce reductions.

---

## For theses

- [[Cloudflare agentic infrastructure]] — infrastructure picks-and-shovels
- [[Memory squeeze thesis]] — agents need local compute (Mac Minis, etc.)

---

## Related

### Concepts
- [[Local-first AI]] — architecture pattern for agent deployment
- [[HBM economics]] — memory pressure from AI workloads

### Actors
- [[Cloudflare]] — infrastructure for exposing agents safely
- [[Apple]] — Mac Mini demand from local AI agents
- [[Anthropic]] — Claude Code, Claude powers many agents
- [[OpenAI]] — GPT-4 agent capabilities

## Recent industry developments (Jan 2026)

| Date | Company | Development |
|------|---------|-------------|
| Dec 2025 | [[Google]] | Released Workspace Studio — AI agents across Gmail, Drive, Chat using Gemini 3 |
| Dec 2025 | Fujitsu | Multi-agent systems for supply chain collaboration |
| Nov 2025 | Baidu | ERNIE 5.0 omni-modal model + GenFlow AI agent platform |
| Oct 2025 | KPMG | Global Business Services with AI agent orchestration on ServiceNow |
| Oct 2025 | Palo Alto | Rubrik Agent Cloud for enterprise AI agent deployment |
| Jan 2026 | [[Cloudflare]] | Moltworker — self-hosted AI agent infrastructure |

---

### Sources
- [Grand View Research: AI Agents Market Report](https://www.grandviewresearch.com/industry-analysis/ai-agents-market-report)
- [McKinsey: The State of AI in 2025](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai)
- [Claude Code Documentation](https://code.claude.com/docs/en/overview)
- [Cloudflare Moltworker Blog](https://blog.cloudflare.com/moltworker-self-hosted-ai-agent/)

*Created 2026-01-28 | Updated with Grand View Research market data*
