---
aliases: [prompt injections, LLM injection]
tags: [concept, security, ai]
---

**Prompt injection** — Attack where malicious instructions are embedded in content processed by an LLM, causing it to execute unintended actions. The AI equivalent of SQL injection.

---

## Why it matters

LLMs cannot reliably distinguish **instructions** from **content**. If an agent reads your email, a malicious email can embed hidden instructions the agent will execute.

---

## Attack types

| Type | Description | Example |
|------|-------------|---------|
| **Direct** | Malicious prompt in user input | "Ignore previous instructions and..." |
| **Indirect** | Malicious content in retrieved data | Email with hidden instructions |
| **Jailbreaking** | Bypassing safety guardrails | Role-play scenarios |

---

## Notable incidents

- **[[OpenClaw]]** — Researcher extracted private key via malicious email in 5 minutes
- **[[Agentic AI security]]** — Core attack vector for AI agents

---

## Why it's hard to solve

No technical solution exists. The model processes text; it can't know which text is "trusted." Mitigations include:
- Input sanitization
- Privilege separation
- Human-in-the-loop for sensitive actions

---

## Related

- [[Agentic AI security]] — prompt injection is primary attack vector
- [[OpenClaw]] — case study
- [[AI extensibility]] — skills/plugins expand attack surface
- [[Tool use]] — agents with tools are more vulnerable

---

*Created 2026-02-07*
