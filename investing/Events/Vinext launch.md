---
aliases: [Vinext, Cloudflare Vinext, Cloudflare vs Vercel]
tags:
  - event
  - developer-tools
  - ai-coding
  - infrastructure
---

# Vinext launch

#event #developer-tools #ai-coding #infrastructure

**Feb 24, 2026** — [[Cloudflare]] launches **Vinext**, an open-source reimplementation of the [[Vercel|Next.js]] public API built on Vite instead of Turbopack. Almost entirely AI-generated: one engineer directing Claude through 800+ coding sessions, ~$1,100 in tokens, one week.

---

## What it is

| Metric | Value |
|--------|-------|
| API coverage | 94% of Next.js surface |
| Build speed | 4.4× faster than Next.js 16 + Turbopack |
| Bundle size | ~56% smaller client bundles |
| Tests | 1,700+ unit, 380 E2E (ported from Next.js suite) |
| Cost to build | ~$1,100 (Claude tokens) |
| Timeline | One week |
| Builder | Steve Faulkner (Cloudflare engineering director) |
| Deploy target | Cloudflare Workers (others planned) |
| Production user | CIO.gov |
| GitHub | [cloudflare/vinext](https://github.com/cloudflare/vinext) |

---

## Why it matters

Next.js has long been criticized for tight coupling to Vercel's infrastructure. Deploying on Cloudflare, Netlify, or AWS Lambda requires painful workarounds. [[OpenNext]] (sponsored by SST, Cloudflare, Netlify) exists to convert Next.js build output for other platforms but breaks unpredictably between versions.

Vercel promised deployment adapters ("Vercel will use the same adapter API as every partner") but Faulkner called these an "early effort" — still dependent on Turbopack and lacking platform-specific API support during development.

**Vinext's approach:** Instead of adapting Next.js *output* (fragile), reimplement the *public API* (stable). Decouples entirely from Vercel's internal decisions.

---

## The AI angle

Faulkner's process was structured, not "vibe coded":
- Spent hours with Claude in OpenCode defining architecture
- Implemented API piece by piece
- Used Next.js's own test suite to validate
- "Had to course-correct regularly"
- No human code review yet (per README disclaimer)

Previous Cloudflare AI-coding project (Matrix server on Workers, Jan 2026) drew criticism for overclaiming scope. Vinext appears more substantive.

---

## Vercel's response

[[Guillermo Rauch]] fired back within hours (Feb 26):

1. Posted "Migrate to Vercel from Cloudflare" guide on X
2. Disclosed **7 security vulnerabilities** in Vinext (2 critical, 2 high, 2 medium, 1 low) — responsibly disclosed to Cloudflare
3. Called it a **"vibe-coded framework"** — deliberately weaponizing the term

The "vibe coded" label invokes research (Tenzai, Jan 2026) showing AI-coded apps contain significant vulnerabilities in authorization logic and business logic. Rauch applied this framing to production infrastructure, not a weekend project.

**Counter:** Seven bugs in a week-old reimplementation of one of the most complex web frameworks isn't shocking. The structured process (800+ sessions, ported test suite, CI) differs meaningfully from unreviewed AI output.

---

## Strategic implications

### For Cloudflare
- Demonstrates AI can replicate complex framework APIs faster than incumbents build adapters
- Strengthens Workers platform stickiness
- Proves Cloudflare is serious about competing for frontend developer mindshare
- Risk: maintaining a parallel framework is expensive long-term

### For Vercel
- **Platform lock-in exposed.** The fact that Cloudflare felt compelled to *rewrite the entire framework* rather than use adapters highlights how coupled Next.js is to Vercel
- $9.3B valuation depends partly on Next.js being the gateway to Vercel's paid platform
- If Vinext matures, developers get Next.js DX without Vercel vendor lock-in

### For the industry
- First major example of AI being used to clone a competitor's framework API surface
- Raises questions about defensibility of open-source frameworks as business moats
- If 94% API coverage costs $1,100 and a week, what else can be replicated?

---

## Related

- [[Cloudflare]] — builder, Workers deployment target
- [[Vercel]] — Next.js creator, direct competitor
- [[Guillermo Rauch]] — Vercel CEO, "vibe-coded framework" response
- [[Cloudflare agentic infrastructure]] — broader Cloudflare developer platform thesis
- [[AI adoption curve]] — AI coding tools adoption context
- [[Anthropic]] — Claude used as the AI coding engine

---

Sources:
- [Cloudflare blog — Vinext](https://blog.cloudflare.com/vinext/)
- [The Register — Cloudflare vibe codes 94% of Next.js API](https://www.theregister.com/2026/02/25/cloudflare_nextjs_api_ai/)
- [OfficeChai — Vercel discloses 7 bugs](https://officechai.com/ai/after-cloudflare-created-vercels-next-js-in-a-week-using-ai-vercel-discloses-7-bugs-in-the-new-framework/)
- [@rauchg on X](https://twitter.com/rauchg/status/2026864132423823499)

*Created 2026-02-26*
