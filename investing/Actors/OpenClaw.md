#actor #ai #agents #opensource

**OpenClaw** (formerly Clawdbot, Moltbot) — Open-source autonomous AI agent platform created by [[Peter Steinberger]]. Uses LLMs to execute tasks via messaging platforms (Telegram, Discord, etc.). Can manage emails, book flights, deal with insurers, and perform agentic workflows.

---

## Quick stats

| Metric | Value |
|--------|-------|
| Creator | [[Peter Steinberger]] |
| Founded | Nov 2025 |
| GitHub stars | **200,000+** (fastest-growing repo in GitHub history) |
| Peak traffic | 2M visitors/week |
| Contributors | 600+ |
| Total commits | 10,000+ in 3 months |
| License | Open source |
| Status | **Moving to independent foundation** (Feb 2026) |

---

## Foundation transition (Feb 15, 2026)

[[Sam Altman]] announced OpenClaw will become an independent foundation, with [[OpenAI]] continuing to support it. Steinberger simultaneously joins OpenAI to work on personal agents.

**Altman:** "OpenClaw will live in a foundation as an open source project that OpenAI will continue to support. The future is going to be extremely multi-agent and it's important to us to support open source as part of that."

**Steinberger:** "It's always been important to me that OpenClaw stays open source and given the freedom to flourish."

**Strategic parallel:** Mirrors [[Anthropic]]'s [[MCP]] and [[Skills]] open-standard strategy. Both frontier labs now backing open agent infrastructure — competing for ecosystem gravity rather than platform lock-in.

---

## Anthropic conflict timeline

| Date | Event |
|------|-------|
| Nov 2025 | Launched as "Clawdbot" — personal project by [[Peter Steinberger]] |
| Jan 9, 2026 | [[Anthropic]] restricted Claude Code OAuth access, breaking Clawdbot integrations. This was the initial disruption — 18 days before any naming dispute |
| Jan 27, 2026 | Anthropic sent cease-and-desist over "Clawdbot" name (trademark claim on "Claude") |
| Jan 2026 | Rebranded Clawdbot → Moltbot → OpenClaw |
| Feb 15, 2026 | [[Sam Altman]] announced Steinberger joining [[OpenAI]]; OpenClaw moving to independent foundation |

The OAuth cutoff preceded and was distinct from the naming dispute. Anthropic's crackdown on third-party Claude Code access (targeting tools like OpenCode, Clawdbot) broke integrations before any trademark action. This sequence drew significant developer community backlash (Craig Weiss tweet: "Anthropic messed up so badly with how they handled Clawdbot" — 580 likes, 27K views, Feb 2026).

## Viral growth

- Launched Nov 2025 as a personal project
- 100K+ GitHub stars in weeks
- 2M visitors in single week
- China's industry ministry warned about security risks from improperly configured instances (Feb 5, 2026)

---

## Architecture & capabilities

*(Source: Lex Fridman interview, Feb 2026)*

| Component | Detail |
|-----------|--------|
| Gateway architecture | Central hub for agent communication |
| Skills marketplace | [[ClawHub]] — community-built extensions |
| Browser control | Can operate web browsers autonomously |
| Cron scheduling | Timed/recurring task execution |
| Multi-model | Supports Claude, ChatGPT, Grok, Deepseek, open-source LLMs |
| Messaging | WhatsApp, Telegram, Slack, Discord, Signal, iMessage |
| Platforms | macOS, Linux, Docker |
| Self-modification | **Can modify its own source code** — most unsettling feature per researchers |

---

## "Kill 80% of apps" prediction

Steinberger told [[Lex Fridman]] that OpenClaw-style agents would kill 80% of apps. Logic: every app is just a slow API to what the user wants. An agent that knows your location, sleep patterns, stress levels, and calendar doesn't need separate apps for fitness tracking, food ordering, or scheduling. *(Source: Lex Fridman interview, Feb 2026)*

---

## Delegation as third UI paradigm

The broader significance per the Lex Fridman analysis: OpenClaw demonstrated a **third interface paradigm** after GUIs (30 years) and touch interfaces (15 years) — **delegation**. You don't tap an icon or type a query; you tell the agent what you want done, and it figures out which APIs to call, which tools to use, which steps to take. *(Source: Lex Fridman interview, Feb 2026)*

---

## Chrome/Chromium model

Steinberger floated a **Chrome/Chromium analogy** for OpenClaw's future: OpenClaw as the open-source foundation (like Chromium), with [[OpenAI]]'s consumer products as the polished commercial layer (like Chrome). Risk: Google's influence on Chromium is dominant — Google engineers contribute the majority of commits and set architectural priorities. Independent Chromium-based browsers (Brave, Edge) operate within Google's framework. Same risk applies to OpenClaw with Steinberger now inside OpenAI. *(Source: Lex Fridman interview, Feb 2026)*

---

## Security concerns

China MIIT flagged OpenClaw as potential security risk when improperly configured — could expose users to cyberattacks and data breaches. Highlights tension between open-source agent autonomy and enterprise security requirements. See [[Agentic AI security]].

---

## Related

- [[Peter Steinberger]] — creator, now at [[OpenAI]]
- [[OpenAI]] — supporting foundation, hired Steinberger
- [[Agentic AI]] — product category
- [[Agentic AI security]] — security concerns
- [[MCP]] — Anthropic's open agent protocol (parallel strategy)
- [[Skills]] — Anthropic's open instruction standard
