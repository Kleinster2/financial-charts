#concept #security #ai #agents

**Agentic AI security** — The fundamental tension between useful AI agents and secure systems. Agents require broad permissions to act autonomously; broad permissions create massive attack surfaces. The same capabilities that make agents useful make them dangerous.

---

## The Core Dilemma

> "We've spent 20 years building security boundaries around our systems. Agents require us to tear that down by the nature of what an agent is."
> — Jameson O'Reilly, DVULN

Traditional security assumes **containment** — limit scope of action, minimize permissions, sandbox everything. Agentic AI inverts this:

| Traditional Security | Agentic AI Requirements |
|---------------------|------------------------|
| Least privilege | Broad permissions to act |
| Sandboxed execution | Access to real systems |
| Input validation | Process arbitrary user content |
| Credential isolation | Needs credentials to act on your behalf |

**The bind:** A sandboxed agent can't access your real email and calendar. An unsandboxed agent is an attack surface.

---

## Attack Vectors

### 1. Prompt Injection

LLMs cannot reliably distinguish **instructions** from **content**. If an agent reads your email, a malicious email can embed hidden instructions the agent will execute.

**Example:** Researcher sent crafted email to a [[Clawdbot viral growth|Clawdbot]] instance → extracted private key in under 5 minutes via prompt injection.

**Why it's hard:** No technical solution exists. The model processes text; it can't know which text is "trusted."

### 2. Localhost Authentication Bypass

Many agents trust all localhost connections by default. If deployed behind a reverse proxy, that proxy traffic gets treated as local → full access without authentication.

**Clawdbot case:** Hundreds of exposed instances found; at least 8 completely open (API keys, Telegram tokens, Signal configs visible).

### 3. Supply Chain Attacks

Agent "skills" or plugins are unaudited code running with agent permissions.

**Clawdbot case:** Researcher uploaded benign skill to marketplace, inflated download count to 4,000, watched developers from 7 countries install it. Marketplace had zero moderation; docs stated "all downloaded code will be treated as trusted code."

### 4. Credential Exposure

Agents need API keys, tokens, and credentials to act. Many store these in plaintext config files.

**Risk:** Any malware (infostealer) on the same machine can grab them in seconds. One password security blog: "If your agent stores plain text API keys, an info stealer can grab them in seconds."

### 5. Window Hijacking

During the [[Clawdbot viral growth]] trademark rename, the developer released old account names before securing new ones. Gap was ~10 seconds. Scammers grabbed both accounts instantly, launched fake token that hit $16M market cap before rugpull.

**Lesson:** Attackers are watching. Any window, however brief, will be exploited.

---

## Enterprise vs Open-Source Gap

| Enterprise Agents | Open-Source Agents |
|------------------|-------------------|
| Least privilege by default | Broad permissions for usability |
| Formal security review | Community-reviewed (maybe) |
| Sandboxed execution environments | Runs on your machine with your permissions |
| Controlled integrations | Connect anything |
| Audit trails | Logs if you configure them |

**Enterprise approach (Google's agentic principles):**
- Treat agent like junior employee
- No assumed access to anything
- Control planes for all agent actions
- Isolated execution environments

**Open-source reality:**
- "Run at your own risk"
- Root access to your digital life
- Trust the developer, trust the plugins, trust the model

---

## The Usability-Security Spectrum

```
SAFER ←————————————————————————→ MORE USEFUL
Siri          Google Assistant          Clawdbot
(walled       (knows everything,        (does everything,
garden)       does little)              broad attack surface)
```

> "Siri is safe because it's neutered. Moltbot is useful because it's dangerous."

The big tech assistants are products designed to protect corporate liability. Open-source agents are tools designed to maximize user capability.

---

## Defensive Patterns

### For Users

1. **Dedicated hardware** — Don't run agents on your primary machine
2. **Throwaway accounts** — Test with accounts you can burn
3. **Network isolation** — Agents on separate VLAN if possible
4. **Credential rotation** — Assume keys will leak; rotate frequently
5. **Audit what it does** — Check logs, verify actions

### For Developers

1. **No localhost trust** — Always authenticate, even locally
2. **Principle of least privilege** — Request only needed permissions
3. **Input sanitization** — Treat all external content as untrusted
4. **Skill signing** — Cryptographic verification of plugins
5. **Audit trails** — Log every action the agent takes

### Architectural

1. **Control planes** — Centralized approval for sensitive actions
2. **Sandboxed execution** — Isolated environments for code execution
3. **Human-in-the-loop** — Confirmation for irreversible actions
4. **Rate limiting** — Prevent runaway agent behavior
5. **Kill switches** — Immediate shutdown capability

---

## Investment Implications

Security tooling for agentic AI is an emerging category with real M&A activity:

| Layer | Focus | Players |
|-------|-------|---------|
| Agent identity/governance | Control what agents can do, audit trails | [[Cyata]] (acquired by [[Check Point]] Feb 2026, ~7 months post-stealth) |
| Infrastructure | Tunnels, Zero Trust, compute isolation | [[Cloudflare]], Zero Networks |
| Monitoring | Agent observability, anomaly detection | Emerging |
| Sandboxing | Isolated execution environments | Emerging |
| Supply chain | Plugin/skill verification | Emerging |
| Offensive testing | AI agent-driven pentesting | [[CodeWall]] (one-person firm), [[Promptfoo]] (acquired by [[OpenAI]]) |

[[Check Point]]'s acquisition of [[Cyata]] is the first major M&A signal that agentic identity governance is a real enterprise need, not just a research concern. The [[McKinsey]] Lilli breach (Feb 2026) validates the category from the other direction — a one-person firm's AI agent breached the world's largest consultancy's AI platform in 2 hours.

See [[Cloudflare agentic infrastructure]] for picks-and-shovels thesis.

---

## Case Study: McKinsey Lilli Breach (Feb 2026)

[[CodeWall]], a one-person cybersecurity firm (founder Paul Price), used its own AI agent to breach [[McKinsey]]'s internal AI platform Lilli — used by all 40,000 staff for strategy, data analysis, and client work.

**Timeline:** AI agent gained full read/write access to Lilli's entire production database within 2 hours. McKinsey security alerted end of February, patched within hours, development environment taken offline.

**Scope exposed:**
- 46.5M chat messages
- 57,000 user accounts, 384,000 AI assistants, 94,000 workspaces
- 728,000 "sensitive" file names (Excel, PowerPoint, Word)
- System prompts and AI model configurations — guardrails laid bare

McKinsey says files were stored separately and "never at risk." Third-party forensics found "no evidence" of client data compromise.

**What makes this notable:**
1. **AI agent attacking AI system.** CodeWall's agent autonomously selected McKinsey as a target, probed Lilli, and self-reported when it found the vulnerabilities. CodeWall: "AI agents autonomously selecting and attacking targets will become the new normal."
2. **Enterprise scale.** This isn't an open-source hobby project — it's the largest consulting firm in the world, with 40% of revenue from AI consulting. If McKinsey can't secure its own AI platform, the enterprise AI security gap is real.
3. **System prompt exposure.** Access to Lilli's model configurations and guardrails reveals the firm's entire AI behavioral architecture. For competitors, this is intelligence gold.
4. **Single-point-of-failure pattern.** One vulnerability in the AI platform = access to the entire organizational knowledge base (46.5M messages spanning client strategy work).

Source: FT (Mar 12, 2026) — Ellesheva Kissin and Stephen Foley.

---

## Open Questions

1. Can prompt injection ever be fully solved at the model level?
2. Will enterprise security requirements kill consumer agent adoption?
3. Who builds the "App Store for agent skills" with real security review?
4. Does agent security become a moat for incumbents (Google, Microsoft) vs open-source?
5. If autonomous AI agents can breach enterprise AI platforms in hours, does the offense-defense asymmetry make enterprise AI deployment fundamentally harder to insure?

---

## Related

- [[AI extensibility]] — higher layers = larger attack surface
- [[Agentic AI]] — What agents are and why they matter
- [[Clawdbot viral growth]] — Case study in security failures
- [[Cloudflare agentic infrastructure]] — Infrastructure play
- [[Local-first AI]] — Architecture pattern with security tradeoffs
- [[Cyata]] — First agentic identity startup acquired ([[Check Point]], Feb 2026)
- [[Check Point]] — Acquirer, entering agentic security via M&A
- [[CyberTech Global Tel Aviv 2026]] — Conference context
- [[McKinsey]] — Lilli breach (Feb 2026), enterprise AI security failure
- [[CodeWall]] — AI agent that autonomously breached Lilli

### Concepts
- [[Enterprise AI knowledge centralization]] — the concentration risk that creates the attack surface

### Events
- [[Clawdbot viral growth]] — Case study in open-source agent security failures

---

## Sources

- Clawdbot/Moltbot security disclosures (Jan 2026)
- DVULN research findings
- 1Password security blog analysis
- Slowmist authentication bypass report
- Google agentic AI principles documentation

---

*Created 2026-02-02*
