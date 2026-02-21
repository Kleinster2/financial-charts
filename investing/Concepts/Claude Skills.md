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

### Critical technical rules

From Anthropic's official guide:
- SKILL.md must be exactly `SKILL.md` (case-sensitive — no SKILL.MD, skill.md, etc.)
- Folder naming: kebab-case only (e.g. `notion-project-setup`), no spaces, no underscores, no capitals
- No README.md inside the skill folder (all docs go in SKILL.md or references/)
- YAML frontmatter: no XML angle brackets (`<` or `>`), no "claude" or "anthropic" in skill name (reserved)
- Description field must include both what the skill does AND when to use it (trigger phrases), under 1024 characters

### YAML frontmatter (minimal required format)

```yaml
---
name: your-skill-name
description: What it does. Use when user asks to [specific phrases].
---
```

Optional fields: `license` (MIT, Apache-2.0), `compatibility` (1-500 chars, environment requirements), `metadata` (author, version, mcp-server).

### API surface

| Endpoint | Purpose |
|----------|---------|
| `/v1/skills` | Skills CRUD — create, list, update, delete |
| `container.skills` | Messages API parameter — attach skills to conversations |

Skills in the API require the Code Execution Tool beta. Available on Claude.ai, [[Claude]] Code, and API.

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

| Pattern | Use when | Key technique |
|---------|----------|---------------|
| Sequential workflow | Multi-step processes in specific order | Explicit step ordering, dependencies, rollback instructions |
| Multi-MCP coordination | Workflows span multiple services (e.g., Figma → Drive → Linear → Slack) | Clear phase separation, data passing between MCPs, validation before next phase |
| Iterative refinement | Output quality improves with iteration | Generate → validate via script → fix issues → re-validate loop |
| Context-aware tool selection | Same outcome but different tools depending on context | Decision trees, fallback options, transparency about choices |
| Domain-specific intelligence | Specialized knowledge beyond tool access (e.g., compliance, finance) | Domain expertise embedded in logic, compliance-before-action, audit trails |

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

- skill-creator: Meta-skill built into Claude.ai that helps users build new skills interactively. 15-30 minutes to build and test a first working skill. Can generate skills from natural language descriptions, review skills for common issues, and help iterate based on edge cases.

### Testing approach (from guide)

Three levels of rigor:
1. Manual testing in Claude.ai — run queries and observe behavior
2. Scripted testing in Claude Code — automate test cases
3. Programmatic testing via Skills API — evaluation suites against defined test sets

Three types of tests:
- Triggering tests — does the skill load when it should? Does it NOT load when it shouldn't?
- Functional tests — are outputs correct? Do API calls succeed? Are edge cases covered?
- Performance comparison — fewer messages, fewer tool calls, fewer tokens vs. baseline without skill

Pro tip from the guide: iterate on a single challenging task until Claude succeeds, then extract the winning approach into a skill. Faster signal than broad testing.

### Distribution (current model, Jan 2026)

For individual users:
1. Download/clone skill folder
2. Zip the folder
3. Upload to Claude.ai via Settings > Capabilities > Skills
4. Or place in Claude Code skills directory

Organization-level: admins deploy workspace-wide with automatic updates and centralized management (shipped Dec 18, 2025).

### Common troubleshooting

| Problem | Cause | Fix |
|---------|-------|-----|
| "Could not find SKILL.md" | File not named exactly SKILL.md | Rename (case-sensitive) |
| "Invalid frontmatter" | YAML formatting — missing delimiters or unclosed quotes | Ensure `---` delimiters wrap frontmatter |
| Skill doesn't trigger | Description too vague or missing trigger phrases | Add specific phrases users would say; ask Claude "when would you use this skill?" |
| Skill triggers too often | Description too broad | Add negative triggers ("Do NOT use for..."), be more specific about scope |
| MCP calls fail | Server disconnected, auth expired, missing permissions | Check Settings > Extensions > connection status |

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
