---
aliases: [prompt injections, LLM injection]
tags: [concept, security, ai]
---

**Prompt injection** — Attack where malicious instructions are embedded in content processed by an LLM, causing it to execute unintended actions. The AI equivalent of SQL injection.

---

## Why it matters

LLMs cannot reliably distinguish instructions from content. If an agent reads your email, a malicious email can embed hidden instructions the agent will execute.

---

## Attack types

| Type | Description | Example |
|------|-------------|---------|
| Direct | Malicious prompt in user input | "Ignore previous instructions and..." |
| Indirect | Malicious content in retrieved data | Email with hidden instructions |
| Jailbreaking | Bypassing safety guardrails | Role-play scenarios |

---

## Notable incidents

- [[OpenClaw]] — Researcher extracted private key via malicious email in 5 minutes
- [[Agentic AI security]] — Core attack vector for AI agents

---

## May 2026: rendered assistant output as payload

The Register's May 29 2026 Permiso write-up expands the prompt-injection surface from "the model follows the wrong instruction" to "the assistant renders attacker-controlled output." In the reported demo, a webpage contained instructions that caused [[ChatGPT]] to return a normal-looking summary plus a fake security alert. The payload included a link and, in the stronger variant, a QR-code image that moved the victim's phone to an attacker-controlled destination.

The important security read is that Markdown, images, previews, and QR codes are not neutral presentation. If an assistant reads an untrusted page and renders its instructions directly into the chat UI, the model output becomes a phishing surface. This bypasses some desktop URL checks, blocklists, and password-manager domain habits because the victim scans from a phone.

The mitigation frame changes accordingly. Input sanitization is not enough. Agent products need to treat rendered model output as untrusted UI: sandbox Markdown and HTML, restrict remote embeds/previews, label source provenance, and strip or gate untrusted QR/image content.

*Source: The Register / Permiso, [May 29 2026](https://www.theregister.com/research/2026/05/29/chatgpt-prompt-injection-turns-web-pages-into-phishing-lures/5248137).*

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
- [[The Register]] — May 2026 rendered-output phishing case
- [[AI R&D automation]] — control protocols for useful but untrusted models

---

*Created 2026-02-07*

### Cross-vault
- [Technologies: Prompt Injection](obsidian://open?vault=technologies&file=Prompt%20Injection) — attack vectors, defense mechanisms, alignment implications
