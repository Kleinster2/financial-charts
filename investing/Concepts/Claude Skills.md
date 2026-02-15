---
aliases: [Skills, Anthropic Skills, Claude Skills platform, AI Skills]
tags: [concept, technology, ai, platform]
---

# Claude Skills

Packaged instruction folders that teach [[Claude]] repeatable workflows. [[Anthropic]]'s developer ecosystem play — published as an open standard portable across AI platforms, not Claude-locked.

Skills complete Anthropic's three-layer developer platform: [[MCP]] (what Claude connects to) → Skills (what Claude knows how to do) → Code Execution (where Claude runs). Anthropic's analogy: MCP = kitchen tools, Skills = recipes.

---

## Timeline

| Date | Milestone |
|------|-----------|
| Oct 2025 | Skills launch announced |
| Dec 18, 2025 | Organization-level deployment shipped |
| Jan 29, 2026 | 32-page "Complete Guide to Building Skills for Claude" published |
| Feb 2026 | Partner directory live: [[Asana]], [[Atlassian]], [[Canva]], [[Figma]], [[Sentry]], [[Zapier]] |

---

## Architecture

### Skill structure

Every skill is a folder:

```
📁 my-skill/
├── SKILL.md        ← Required: YAML frontmatter + instructions
├── scripts/        ← Optional: executable code
├── references/     ← Optional: loaded on-demand docs
├── templates/      ← Optional: output templates
└── assets/         ← Optional: icons, images
```

### Three-level progressive disclosure

| Level | What loads | When |
|-------|-----------|------|
| Frontmatter | YAML metadata (name, description) | Always — scanned for relevance |
| SKILL.md body | Full instructions, rules, workflow steps | When user intent matches skill description |
| References/scripts | Supporting docs, executable code | On-demand during execution |

A project with 20 skills doesn't waste tokens loading all 20 — only matching skills activate. This is the key efficiency insight vs. traditional system prompts that load everything always.

### API surface

| Endpoint | Purpose |
|----------|---------|
| `/v1/skills` | Skills CRUD — create, list, update, delete |
| `container.skills` | Messages API parameter — attach skills to conversations |

Available on Claude.ai, [[Claude]] Code, and API.

---

## Skill categories

| Category | Description | Example |
|----------|-------------|---------|
| Document/Asset Creation | Generate formatted outputs from templates | Brand voice checker, quarterly report generator |
| Workflow Automation | Multi-step procedural tasks | Data pipeline, deployment workflow |
| MCP Enhancement | Add workflow knowledge to MCP tool integrations | CRM update + notification sequence via [[Zapier]] |

---

## Five reusable patterns

From Anthropic's guide and early adopter experience:

| Pattern | Description |
|---------|-------------|
| Sequential workflow | Step-by-step execution (A → B → C) |
| Multi-MCP coordination | Orchestrate across multiple tool integrations |
| Iterative refinement | Generate → evaluate → improve loops |
| Context-aware tool selection | Dynamically pick tools based on task context |
| Domain-specific intelligence | Embed expert knowledge for specialized domains |

---

## Before vs. after

| Dimension | Traditional prompts | Skills |
|-----------|-------------------|--------|
| Structure | Flat text | Organized folder |
| Loading | Always loaded | On-demand |
| Code | No execution | Scripts included |
| Sharing | Copy-paste | Share folder |
| Versioning | Manual | Git-friendly |
| Testing | Ad-hoc | Systematic |
| Composability | Difficult | Built-in |

---

## Competitive positioning

| Platform | Approach | Lock-in |
|----------|----------|---------|
| Anthropic Skills | Open standard, folder-based | None — portable by design |
| [[OpenAI]] Custom GPTs | Proprietary, GPT Store marketplace | High — OpenAI platform only |
| [[OpenAI]] Agent SDK | Framework-level | Medium — framework dependency |
| [[Microsoft]] Copilot plugins | Graph API + M365 | High — Microsoft ecosystem |
| [[Google]] Gemini extensions | First-party integrations | High — Google Workspace |

Key differentiation: Anthropic is the only major lab publishing its customization system as an open standard. Same playbook as [[MCP]] — originate the standard, benefit from ecosystem gravity without requiring lock-in. This is the strategic inverse of [[OpenAI]]'s marketplace approach.

---

## Ecosystem

### Partner directory

| Partner | Integration type |
|---------|-----------------|
| [[Asana]] | Project management workflows |
| [[Atlassian]] | Jira/Confluence automation |
| [[Canva]] | Design asset creation |
| [[Figma]] | Design workflow automation |
| [[Sentry]] | Error triage and debugging |
| [[Zapier]] | Cross-app workflow orchestration |

### Built-in tooling

- skill-creator: Meta-skill built into Claude.ai that helps users build new skills interactively. 15-30 minutes to build and test a first working skill.

---

## Strategic significance

Skills are Anthropic's answer to the platform layer question: how does a model lab become a platform company?

Platform stack:

| Layer | Product | Role |
|-------|---------|------|
| Models | Claude Opus, Sonnet, Haiku | Raw intelligence |
| Connectivity | [[MCP]] | What Claude can connect to |
| Knowledge | Skills | What Claude knows how to do |
| Environment | Claude Code, API | Where Claude runs |

This positions [[Anthropic]] as a full-stack AI developer platform, not just a model provider. Skills create switching costs through workflow accumulation — once an organization has 50+ custom skills, migrating is painful regardless of model quality.

The open standard bet: if Skills become a cross-platform specification (like MCP is becoming for tool connectivity), Anthropic benefits from being the originator and best-optimized runtime, while avoiding the "walled garden" critique that dogs [[OpenAI]]'s GPT Store.

---

## Investment implications

| Signal | What to watch |
|--------|---------------|
| Partner directory growth | Ecosystem health — are major SaaS vendors shipping skills? |
| Skills API adoption | Developer lock-in metric — skills created per organization |
| Cross-platform adoption | Does the open standard actually get adopted by other models? |
| Enterprise skill libraries | Org-level deployment = enterprise stickiness |
| skill-creator usage | Self-serve developer onboarding velocity |

Skills don't generate direct revenue — they're a retention and expansion mechanism. Organizations that build custom skills are less likely to churn from Claude, and more likely to expand usage across teams.

---

## Related

### Concepts
- [[AI extensibility]] — broader concept; Skills are one layer
- [[MCP]] — complementary standard (connectivity vs. knowledge)
- [[Agentic AI]] — Skills enable more reliable agent workflows
- [[Platform economics]] — Skills create switching costs

### Actors
- [[Anthropic]] — originator and primary runtime
- [[OpenAI]] — competitor approach (Custom GPTs, agent SDK)
- [[Asana]] — launch partner
- [[Atlassian]] — launch partner
- [[Canva]] — launch partner
- [[Figma]] — launch partner
- [[Sentry]] — launch partner
- [[Zapier]] — launch partner

---

*Source: Anthropic "Complete Guide to Building Skills for Claude" (Jan 29, 2026), claude.com/blog*
*Created 2026-02-15*
