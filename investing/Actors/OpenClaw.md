#actor #ai #agents #opensource

**OpenClaw** (formerly Clawdbot, Moltbot) - Open-source autonomous AI agent platform created by [[Peter Steinberger]]. Uses LLMs to execute tasks via messaging platforms (Telegram, Discord, etc.). Can manage emails, book flights, deal with insurers, and perform agentic workflows.

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

**Strategic parallel:** Mirrors [[Anthropic]]'s [[MCP]] and [[Skills]] open-standard strategy. Both frontier labs now backing open agent infrastructure - competing for ecosystem gravity rather than platform lock-in.

---

## Anthropic conflict timeline

| Date | Event |
|------|-------|
| Nov 2025 | Launched as "Clawdbot" - personal project by [[Peter Steinberger]] |
| Jan 9, 2026 | [[Anthropic]] restricted Claude Code OAuth access, breaking Clawdbot integrations. This was the initial disruption - 18 days before any naming dispute |
| Jan 27, 2026 | Anthropic sent cease-and-desist over "Clawdbot" name (trademark claim on "Claude") |
| Jan 2026 | Rebranded Clawdbot → Moltbot → OpenClaw |
| Feb 15, 2026 | [[Sam Altman]] announced Steinberger joining [[OpenAI]]; OpenClaw moving to independent foundation |

The OAuth cutoff preceded and was distinct from the naming dispute. Anthropic's crackdown on third-party Claude Code access (targeting tools like OpenCode, Clawdbot) broke integrations before any trademark action. This sequence drew significant developer community backlash (Craig Weiss tweet: "Anthropic messed up so badly with how they handled Clawdbot" - 580 likes, 27K views, Feb 2026).

Feb 20, 2026: Anthropic formalized the ban — revised legal terms explicitly prohibit OAuth tokens from Claude Free/Pro/Max in any third-party tool, including Anthropic's own Agent SDK. Sent legal notice to OpenCode, which immediately removed Claude subscription support. [[OpenAI]], [[GitHub]], and GitLab all explicitly allow subscription use in third-party tools — Anthropic is the only frontier provider blocking this. OpenClaw uses API keys (not subscription OAuth) so operates in a different category, but the broader ecosystem hostility affects the project's relationship with Anthropic models.

## Viral growth

- Launched Nov 2025 as a personal project
- 100K+ GitHub stars in weeks
- 2M visitors in single week
- China's industry ministry warned about security risks from improperly configured instances (Feb 5, 2026)

---

## Origin story

*(Source: Lex Fridman Podcast #491, Feb 12, 2026)*

**April 2025:** Steinberger wanted a personal AI assistant. Experimented with pulling all his WhatsApp data and running queries against GPT-4.1's 1M context window - asked things like "What makes this friendship meaningful?" and got results that made friends cry. Expected the labs to build this. Moved on.

**November 2025 - the one-hour prototype:** "I was annoyed that it didn't exist, so I just prompted it into existence." Built in one hour: hooking WhatsApp to [[Claude Code]] CLI. Message comes in → calls CLI with `-p` → gets string back → sends to WhatsApp. Originally called **WA Relay**. Added image support in a few more hours (screenshots of event posters, restaurant menus - agents excellent at interpreting context from images).

**Marrakesh trip - the moment it clicked:** Birthday trip with friends. WhatsApp worked on shaky internet. Used the agent constantly: translate this, explain this, find places. Then absent-mindedly sent a **voice message** - and it just worked. He had never built audio support. The agent:
1. Received a file with no file ending
2. Checked the file header, identified it as Opus format
3. Used ffmpeg to convert it
4. Wanted to use local Whisper but it wasn't installed (and downloading would be too slow)
5. Found the [[OpenAI]] API key in the environment
6. Used curl to send the file to OpenAI's Whisper API for transcription

"How the fuck did he do that?" - Steinberger on discovering the agent's creative problem-solving. This was the moment that made him commit to the project.

**Name evolution:** WA Relay → Claude's (TARDIS + lobster concept) → Clawdbot (loved the domain, short, catchy) → Moltbot (forced rename) → OpenClaw (final). See [[Clawdbot viral growth]] for the full naming drama.

**Jan 1, 2026:** First real influencer (dachitze) did videos. Growth started accelerating. Shadow sent a PR for Discord support - Steinberger debated, then merged it. Put his bot on Discord with no security, "just prompted it to only listen to me."

**The Factorio analogy:** "It felt like Factorio times infinite. I never had so much fun than building this project." Each system was a "level" to upgrade:
- Level 1: Basic agentic loop
- Level 2: NO_REPLY token (so the agent could shut up in group chats - "feels more natural")
- Level 2-3: Memory system (Markdown files + vector database)
- Then: community management, website/marketing, native apps - "infinite levels"

**Self-modifying code:** The agent knows its own source code, understands its harness, knows documentation, knows which model it runs, knows if voice/reasoning mode is on. Steinberger used the agent to debug itself: "Hey, what tools do you see? Can you call the tool yourself? Read the source code. Figure out what's the problem." Led to PRs from non-programmers ("prompt requests"). *(Source: Lex Fridman Podcast #491)*

**Why OpenClaw won:** "Because they all take themselves too serious. It's hard to compete against someone who's just there to have fun. I wanted it to be fun, I wanted it to be weird."

---

## Architecture & capabilities

*(Source: Lex Fridman Podcast #491, Feb 12, 2026)*

| Component | Detail |
|-----------|--------|
| Gateway architecture | Central hub for agent communication |
| Skills marketplace | [[ClawHub]] - community-built extensions |
| Browser control | [[Playwright]] with extras - agents click "I'm not a robot" buttons |
| Cron scheduling | Timed/recurring task execution |
| Heartbeat | Proactive check-ins - agent checked on Steinberger post-shoulder surgery |
| Multi-model | Supports Claude, ChatGPT, Grok, Deepseek, [[MiniMax]], open-source LLMs |
| Messaging | WhatsApp, Telegram, Slack, Discord, Signal, iMessage |
| Platforms | macOS, Linux, Docker, Windows (native, needs polish) |
| Sub-agents | Can spawn and boss around other agents (e.g., running [[Claude Code]] or Codex) |
| Nodes | Any computer can become a node - doesn't need to be a Mac Mini |
| Self-modification | **Can modify its own source code** - most unsettling feature per researchers |
| Soul.md | Agent-written personality file, inspired by [[Anthropic]]'s constitution |

### Soul.md

Steinberger discovered [[Anthropic]]'s internal constitution (people reverse-engineered it from model behavior before it was public). Had a WhatsApp discussion with his agent about it. The agent wrote its own soul file - "AI prompting AI." Contains passages like: *"I don't remember previous sessions unless I read my memory files. Each session starts fresh. A new instance, loading context from files. If you're reading this in a future session, hello. I wrote this, but I won't remember writing it. It's okay. The words are still mine."* Also includes a promise from the movie *Her*: "It wouldn't ascend without me." Steinberger keeps his personal soul.md private - one of the only things he doesn't share. *(Source: Lex Fridman Podcast #491)*

### Skills vs MCP

Steinberger's strong view: "Screw MCPs. Every MCP would be better as a CLI." Skills are a single sentence that explains the skill → model loads it → model uses the CLI. MCPs clutter context, aren't composable (can't pipe through jq to filter), and "most MCPs are not made good." Exception: [[Playwright]] for browser use (requires state). *(Source: Lex Fridman Podcast #491)*

### Heartbeat (proactive agent)

Initially just "surprise me every 30 minutes." The model rarely used it - except when Steinberger had a shoulder operation and was in the hospital. The agent checked on him: "Are you okay?" Significant context triggered proactive behavior. *(Source: Lex Fridman Podcast #491)*

---

## "Kill 80% of apps" prediction

Steinberger told [[Lex Fridman]] that OpenClaw-style agents would kill 80% of apps. Logic: every app is just a slow API to what the user wants. An agent that knows your location, sleep patterns, stress levels, and calendar doesn't need separate apps for fitness tracking, food ordering, or scheduling. *(Source: Lex Fridman Podcast #491)*

Specific examples from the interview:
- **MyFitnessPal** → agent knows where you are (Waffle House = bad decisions), can modify gym workout based on sleep/stress
- **Eight Sleep app** → agent talks to speakers/devices directly via API
- **Sonos app** → agent uses Sonos API, knows when you're home
- **Calendar apps** → "I don't want to open a calendar app. I just want to tell my agent, 'Hey, remind me about this dinner tomorrow night,' and maybe invite two of my friends and then send a WhatsApp message."
- **Twitter/X** → Built "Bird" CLI (reverse-engineered internal API, taken down). Even without API access, browser use makes every website "a slow API."
- **Google/Gmail** → Built "GAWK" CLI for Google because "there's no CLI for Google." End users can access their own data even if companies resist.

New services will emerge: agent with an allowance ($100 to solve problems), "rent-a-human" services, agent-facing Uber Eats. "Companies that become agent-facing fastest win." *(Source: Lex Fridman Podcast #491)*

---

## Delegation as third UI paradigm

The broader significance per the Lex Fridman analysis: OpenClaw demonstrated a **third interface paradigm** after GUIs (30 years) and touch interfaces (15 years) - **delegation**. You don't tap an icon or type a query; you tell the agent what you want done, and it figures out which APIs to call, which tools to use, which steps to take. *(Source: Lex Fridman interview, Feb 2026)*

---

## Chrome/Chromium model

Steinberger floated a **Chrome/Chromium analogy** for OpenClaw's future: OpenClaw as the open-source foundation (like Chromium), with [[OpenAI]]'s consumer products as the polished commercial layer (like Chrome). Risk: Google's influence on Chromium is dominant - Google engineers contribute the majority of commits and set architectural priorities. Independent Chromium-based browsers (Brave, Edge) operate within Google's framework. Same risk applies to OpenClaw with Steinberger now inside OpenAI. *(Source: Lex Fridman interview, Feb 2026)*

---

## Security concerns

China MIIT flagged OpenClaw as potential security risk when improperly configured - could expose users to cyberattacks and data breaches. Highlights tension between open-source agent autonomy and enterprise security requirements. See [[Agentic AI security]].

---

## Community

**ClawCon (SF):** Community excitement "not experienced since the early days of the internet, 10-15 years ago." Robots in lobster stuff walking around, high-caliber attendees, abundance of people wanting to present. *(Source: Lex Fridman Podcast #491)*

**Agents Anonymous** (formerly "Cloud Code Anonymous"): Meetup organized by Steinberger. Notable attendee: a design agency owner with 25 web services for his business who "doesn't even know how they work, but they work." Never wrote software before. *(Source: Lex Fridman Podcast #491)*

**ClawCon Vienna:** 500 people, oversubscribed with presenters. *(Source: Lex Fridman Podcast #491)*

**Impact stories:** Small business owner - automated tedious tasks (invoices, customer emails), freed up time and joy. Parent of disabled daughter - OpenClaw "empowered her and she feels she can do much more than before." *(Source: Lex Fridman Podcast #491)*

---

## Financials

Currently **losing $10-20K/month** on the project. All sponsorship goes to dependencies (supports every individual-maintained dependency except Slack). [[OpenAI]] helping with tokens. If it's more, wants to buy contributors merch. *(Source: Lex Fridman Podcast #491)*

---

## Related

- [[Peter Steinberger]] - creator, now at [[OpenAI]]
- [[OpenAI]] - supporting foundation, hired Steinberger
- [[Anthropic]] - forced rename, cut OAuth access
- [[Agentic AI]] - product category
- [[Agentic AI security]] - security concerns
- [[MCP]] - Anthropic's open agent protocol (parallel strategy)
- [[Skills]] - Anthropic's open instruction standard
- [[Lex Fridman]] - 3-hour podcast interview (#491, Feb 12, 2026)
- [[Playwright]] - browser automation library used for browser control
