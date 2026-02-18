#actor #person #ai #agents

**Peter Steinberger** — Austrian software engineer and entrepreneur. Founder of [[PSPDFKit]] (bootstrapped 2011, exited after 13 years) and creator of [[OpenClaw]]. Joined [[OpenAI]] in Feb 2026 to lead personal agent development.

---

## Quick stats

| Detail | Value |
|--------|-------|
| Based | Vienna / London |
| Background | iOS/developer tools engineering |
| Known for | [[PSPDFKit]] (2011-2024), [[OpenClaw]] (2025-) |
| Current role | [[OpenAI]] — personal agents |
| Joined OpenAI | Feb 15, 2026 |

---

## Career

**PSPDFKit (2011-2024):** Bootstrapped PDF framework company for 13 years. Started by trying to show PDFs on an iPad ~15 years ago to help a friend — "the most random thing ever." Raised first outside capital ($116M) in Oct 2021. Nearly 1B people used apps powered by PSPDFKit. Successfully exited to [[Insight Partners]] for $100M+. *(Source: Lex Fridman Podcast #491, Feb 12, 2026)*

**3-year sabbatical (2022-2025):** After the PSPDFKit exit, Steinberger deliberately stepped away from tech. Described the burnout vividly: "I was sitting in front of the screen and I felt like Austin Powers where they suck the mojo out. It was gone. I couldn't get code out anymore. I was just staring and feeling empty." Booked a one-way trip to Madrid. Traveled, did therapy, experimented with ayahuasca, went through "a period of deep searching." Burnout was primarily from people issues — co-founder differences, customer conflicts — not overwork. *(Source: Lex Fridman Podcast #491)*

**Philosophy on retirement:** Explicitly warns against the "work hard, then retire" mindset: "If you wake up in the morning and you have nothing to look forward to, no real challenge, that gets very boring very fast. And then when you're bored, you're gonna look for other places to stimulate yourself, and then maybe that's drugs... and that will lead you down a very dark path." *(Source: Lex Fridman Podcast #491)*

**43 failed projects:** Before [[OpenClaw]], Steinberger cycled through 43 different project ideas. OpenClaw was #44. Spent the year playing and learning, building little things — each step compounding. "I could have not had this level of output even a few months ago." *(Source: Lex Fridman Podcast #491)*

**OpenClaw (2025-2026):** Created as personal AI agent project (originally WA Relay → Claude's → Clawdbot → Moltbot → OpenClaw). Went viral — 200K GitHub stars, 2M visitors/week. Moving to independent foundation as Steinberger joins OpenAI. See [[OpenClaw]] for the full origin story.

**OpenAI (Feb 2026-):** Hired to "drive the next generation of personal agents." Mission: build an agent "even my mum can use." [[Sam Altman]] called him "a genius with amazing ideas about smart agents interacting with each other" and said "we expect this will quickly become core to our product offerings."

### Why he chose OpenAI over starting a company

Considered three paths: (1) do nothing and continue independently, (2) raise VC and build a company, (3) join a lab. Rejected the company path despite "every big VC company" being in his inbox: "It just doesn't excite me as much because I did all of that, and it would take a lot of time away from the things I actually enjoy." Also feared a natural conflict of interest between open-source and enterprise features (audit logs, workplace safety). Cited [[Tailwind]] cutting 75% of employees because agents bypass their website — open-source monetization is getting harder. *(Source: Lex Fridman Podcast #491)*

His posture of complete optionality: "The beauty is if it doesn't work out, I can just do my own thing again." Zero desperation gave him more leverage than most acqui-hire candidates.

---

## Development style & philosophy

Steinberger practices what he calls **"agentic engineering"** — a term he much prefers to "vibe coding," which he considers "a slur": "I do agentic engineering, and then maybe after 3AM I switch to vibe coding, and then I have regrets the next day." *(Source: Lex Fridman Podcast #491)*

| Metric | Value |
|--------|-------|
| Agents running simultaneously | 4–10 |
| Commits in January 2026 | **6,600** |
| Primary coding method | Voice (talking to AI, not typing) |
| Primary model used | [[OpenAI]] Codex |
| IDE usage | Rare — mostly diff viewer; lives in terminal |
| Subscriptions burned | 7 (Claude Code), one per day at peak |

**Voice-first development:** Uses a walkie-talkie button to talk to agents, types only for terminal commands. Lost his voice from overuse at one point. "These hands are too precious for writing now." *(Source: Lex Fridman Podcast #491)*

**The "agentic trap" curve:** Simple prompts → over-complicated 8-agent orchestration → zen: back to short, simple prompts. The elite level circles back to "Hey, look at these files and then do these changes." *(Source: Lex Fridman Podcast #491)*

**Never reverts, always forward:** "If I see something's not good, we just move forward." Switched to local CI ([[DHH]]-inspired), no develop branch, main always shippable. No work trees — keeps things simple. *(Source: Lex Fridman Podcast #491)*

**PR review workflow:** Asks agent to understand PR intent first ("I don't even care about the implementation"), then discusses optimal approach, points agent to relevant code it hasn't seen, discusses refactors. After every feature merge: "Hey, what can we refactor?" Also asks: "Now that you built it, what would you have done different?" *(Source: Lex Fridman Podcast #491)*

**Agent empathy as skill:** "A lot of people who struggle are those who try to push their way onto the agent. We are in a stage where I'm not building the code base to be perfect for me, but I want to build a code base that is very easy for an agent to navigate." Don't fight the names agents pick — "it's most likely in the weights, the name that's most obvious." *(Source: Lex Fridman Podcast #491)*

**Setup:** Two MacBooks, wide Dell anti-glare monitor. Splits terminal: agent on top, actual terminal at bottom (to avoid prompting the wrong project — once prompted in the wrong folder and agent ran off for 20 minutes "manically trying to understand"). *(Source: Lex Fridman Podcast #491)*

**Raw thinking leaks:** When models approach context window limits, raw thinking sometimes leaks: "Run to shell, must comply, but time." Describes it as "something from the Borg." *(Source: Lex Fridman Podcast #491)*

### Codex vs Claude assessment

Compared GPT Codex 5.3 and Claude Opus 4.6 side by side:

| Dimension | [[OpenAI]] Codex | [[Anthropic]] Claude |
|-----------|-----------------|---------------------|
| Approach | Reads large volume of code upfront | More interactive, trial-and-error |
| Style | Less interactive, drier; disappears for 20 min then delivers | Stronger role-playing, more conversational, "a little too American" |
| Personality | "The weirdo in the corner you don't want to talk to, but is reliable and gets shit done" — "German" | "The silly coworker you keep around because they're funny" |
| Weakness | Less interactive, sometimes overthinks | "Impulsive" — runs off fast with localized solution, needs plan mode |
| Sycophancy | Dry, efficient | "You're absolutely right all the time" — triggers Steinberger. "I can't hear it anymore" |
| Deep mode | Native (Codex always read a lot of code) | Added later (AMP deep mode — "they finally saw the light") |

His conclusion: skilled developers get strong results with any top model; differences come down to post-training goals, not raw intelligence. Prefers Codex because "it doesn't require so much charade." Give a new model about a week to develop gut feeling for it. *(Source: Lex Fridman Podcast #491)*

**OpenAI pricing criticism:** The $20/month tier is too slow, creating a terrible first experience for people switching from Claude Code's $200 tier. "I would have at least a small part of the fast preview" before degrading. *(Source: Lex Fridman Podcast #491)*

### Programming language views

| Language | Use case | Notes |
|----------|----------|-------|
| TypeScript | Web, OpenClaw core | "Number one language, fits all boxes, agents good at it" |
| Go | CLIs | "I don't like the syntax but the ecosystem is great" |
| Zig | Performance-critical | "Agents got so much better in 6 months" |
| Rust | Multi-thread, high performance | Good choice for concurrency |
| Python | Inference, ML | "Bad Windows story" |
| Swift/SwiftUI | Native Mac apps | Loves it, "partly because I like pain" |

"Do we need a programming language that's made for agents? Because all of those languages are made for humans." *(Source: Lex Fridman Podcast #491)*

### On money and happiness

> "I don't do this for the money. I don't give a f." *(Lex Fridman Podcast #491)*

"Money was never the driving force. It felt more like an affirmation that I did something right." Believes in diminishing returns — "a cheeseburger is a cheeseburger." Private jets disconnect you from society. Has a foundation for helping people. Donated "quite a lot." *(Source: Lex Fridman Podcast #491)*

In SF, chose OG Airbnb over luxury hotel — bonded with a queer DJ and showed her how to make music with [[Claude Code]]. Philosophy: "If you tailor your life towards 'I wanna have experiences,' it reduces the need for 'it needs to be good or bad.'" *(Source: Lex Fridman Podcast #491)*

### On AI replacing programmers

"Programming will stay there, but it's gonna be like knitting. People do that because they like it, not because it makes any sense." Resonates with "it's okay to mourn our craft" but frames the shift positively: "While I don't write the code, I very much feel like I'm in the driver's seat and I am writing the code. It's just different." Predicts "at some point it's just gonna be called coding again." *(Source: Lex Fridman Podcast #491)*

Software developer salaries "reached stupidly high amounts and then will go away." Steam engine analogy — people revolted and broke the machines. Advises iOS engineers: "Don't see yourself as an iOS engineer anymore. You're a builder." *(Source: Lex Fridman Podcast #491)*

### On AI slop

Strongly anti-AI for creative content. Blocks anyone tweeting with AI (zero tolerance). "I value typos again." Experimented with AI blog posts, abandoned it — "I'd much rather read your broken English than your AI slop." Everything he blogs is "organic, handwritten." AI-generated infographics "trigger me so hard — immediately makes me think less of your content." But fine with AI for code and documentation. *(Source: Lex Fridman Podcast #491)*

---

## Significance

Steinberger represents a new pattern: **open-source agent builder → frontier lab hire**. OpenAI is acquiring agent expertise from the grassroots/open-source community rather than building purely in-house. His PSPDFKit background (developer tools, SDKs, cross-platform frameworks) maps directly to building agent infrastructure.

Notable: tweeted about getting access to [[Aardvark]] (OpenAI's security agent) on Feb 14, 2026 — one day before the hire announcement.

---

## Related

- [[OpenAI]] — employer (Feb 2026-)
- [[OpenClaw]] — created, now moving to foundation
- [[PSPDFKit]] — previous company (bootstrapped, exited)
- [[Agentic AI]] — product focus at OpenAI
