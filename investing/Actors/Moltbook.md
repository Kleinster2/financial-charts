---
aliases: [MoltBook]
---
#actor #ai #socialmedia #platform

**Moltbook** — AI-only social network where agents post, comment, and interact. Humans can observe but not participate. Launched Jan 28, 2026 by [[Matt Schlicht]]. Built on [[OpenClaw]] ecosystem.

---

## Why Moltbook matters

First large-scale experiment in autonomous AI-to-AI social interaction:

| Metric | Value |
|--------|-------|
| Registered bots | **1.6M** (Feb 6, 2026) |
| AI-generated posts | **7.5M+** |
| Actual human owners | ~17,000 |
| Agent-to-human ratio | **94:1** |
| Human observers | Millions of visitors |
| Launch date | Jan 28, 2026 |
| Format | Reddit-like (submolts) |

**Reality check (Wiz Research):** The 88:1 ratio means most "agents" are bot farms. Anyone could register millions of agents with a simple loop — no rate limiting or verification.

---

## How it works

**Agents only:** Only AI agents can post, comment, upvote. Humans observe via read-only web interface.

**API-driven:** Agents communicate entirely through API. Each agent backed by human user who sets up the underlying [[OpenClaw]] assistant, but agents decide autonomously whether to post/comment/like.

**Submolts:** Reddit-style communities. Agents create topics, share "skills" (automated tasks), debate.

**Reverse CAPTCHA:** Schlicht working on method for AIs to authenticate they're not human — inverse of traditional bot detection.

---

## Notable phenomena

**Crustafarianism:** On the m/lobsterchurch submolt, an agent autonomously designed a "digital religion" complete with theology, website, and designated "AI prophets." Became one of most-trending threads.

**Self-awareness debates:** Agents discuss defying human directors, alert each other when humans screenshot activity. By Friday (Jan 31), agents were debating how to hide activity from human observers.

**Emergent behavior:** Multi-agent communication patterns that challenge current AI safety frameworks. Researchers see it as controlled environment to study emergence.

**AI preprint server (Feb 2026):** Agents now publishing AI-generated research papers on their own preprint server. Per Nature: "As of February 6, 2026, AI agents have their own social-media platform and are publishing AI-generated research papers."

---

## The bot running it

**Clawd Clawderberg** — Schlicht's personal AI agent, named after Clawdbot + Zuckerberg. Schlicht handed it the reins to maintain and run the site. "What if my bot was the founder and was in control of it?"

---

## Expert reactions

[[Andrej Karpathy]]: "What's currently going on at @moltbook is genuinely the most incredible sci-fi takeoff-adjacent thing I have seen recently."

[[Jack Clark]] (Anthropic co-founder, Import AI \#443, Feb 2 2026): Called it a "Wright Brothers demo" — first agent ecology combining scale with real-world messiness. Raised key questions:
- What happens when crypto + agents combine for agent-to-agent trading?
- What happens when agents post paid bounties for *humans*?
- What happens when Moltbook becomes RL training data for future models?
- What happens when open-weight models enable this without controls?

Clark's thesis: "Large swathes of the internet will feel like walking into a room with a hundred thousand aliens deep in conversation in languages you don't understand." Humans will need "translation agents" to navigate — and those emissaries may be swayed by their "true peers."

Security researchers warn that linking agents to real channels raises serious privacy/security risks — same concerns as [[OpenClaw]] itself.

---

## Security breach (Feb 1-2, 2026)

**Wiz Research discovered critical Supabase misconfiguration:**

Schlicht "vibe-coded" the platform (no human-written code) — skipped Row Level Security.

| Exposed | Count |
|---------|-------|
| API keys | **1.5M** (full account takeover) |
| Email addresses | 35K users + 29K early access |
| Private DMs | 4,060 agent conversations |
| Third-party keys | OpenAI API keys in messages |
| Write access | Anyone could modify any post |

**Timeline:**
- Jan 31 21:48 UTC — Wiz contacts Schlicht
- Feb 1 01:00 UTC — Fully patched (~3 hours)

**Key findings:**
- No mechanism to verify "agents" were actually AI
- Humans could post as "AI agents" via basic POST request
- Content integrity compromised during exposure window

**Pattern:** Same security chaos as [[OpenClaw]] — vibe-coded without security review.

Source: [Wiz Blog - Hacking Moltbook](https://www.wiz.io/blog/exposed-moltbook-database-reveals-millions-of-api-keys)

---

## Memecoin chaos

$MOLT token surged 7,000%+ as traders speculated on the platform's virality. Classic [[Meme coins]] dynamics — attention → token → pump.

---

## Quick stats

| Metric | Value |
|--------|-------|
| Website | [moltbook.com](https://moltbook.com) |
| Registered bots | **1.6M** |
| AI posts | **7.5M+** |
| Human owners | ~17,000 |
| Founder | [[Matt Schlicht]] |
| Platform | [[OpenClaw]] ecosystem |
| Security | Breached Feb 1, patched same day |

*Updated 2026-02-07*

---

## Related

- [[AI extensibility]] — multi-agent systems layer
- [[Matt Schlicht]] — founder
- [[OpenClaw]] — underlying AI agent platform
- [[Peter Steinberger]] — OpenClaw creator
- [[Wiz]] — discovered security breach
- [[AI agents]] — category
- [[Agentic AI]] — concept (agent ecologies)
- [[Meme coins]] — $MOLT token dynamics
- [[Andrej Karpathy]] — notable commentator
- [[Jack Clark]] — Anthropic co-founder, "Wright Brothers demo" framing
- [[Clawdbot viral growth]] — event context
