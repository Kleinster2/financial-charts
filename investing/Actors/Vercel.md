---
aliases:
  - ZEIT
tags:
  - actor
  - startup
  - private
  - usa
  - developer-tools
  - frontend
---

# Vercel

#actor #startup #private #usa #developer-tools #frontend

**Vercel** — Frontend cloud platform, creator of Next.js. Founded by [[Guillermo Rauch]] (2015). **$200M+ ARR, $9.3B valuation (Sept 2025).** Powers deployments for [[Nike]], [[Walmart]], [[PayPal]]. v0 AI tool has 3.5M+ users. Often paired with [[Supabase]] for full-stack apps.

---

## Key facts

| Metric | Value |
|--------|-------|
| Founded | Nov 2015 (as ZEIT) |
| Co-founders | [[Guillermo Rauch]], Tony Kovanen, Naoyuki Kanezawa |
| Rebranded | April 2020 |
| HQ | San Francisco, CA |
| CEO | [[Guillermo Rauch]] |
| ARR | ~$200M (May 2025) |
| Valuation | **$9.3B** (Sept 2025) |
| Total raised | $863M |

---

## Leadership

| Role | Name | Background |
|------|------|------------|
| CEO | [[Guillermo Rauch]] | Co-founder; previously created Socket.io, Mongoose; early employee at Cloudup (acquired by Automattic) |
| Co-founder | Tony Kovanen | — |
| Co-founder | Naoyuki Kanezawa | — |

---

## Financials

### Revenue growth

| Metric | 2024 | 2025 |
|--------|------|------|
| Revenue | $144M | $200M+ |
| YoY growth | — | 82% |

*ARR (Annual Recurring Revenue) for SaaS business.*

*Note: Vercel is SaaS; ARR = Annual Recurring Revenue. Source: Sacra estimates.*

### Valuation progression

| Date | Valuation | Round |
|------|-----------|-------|
| June 2021 | $1.1B | Series C (unicorn) |
| Nov 2021 | $2.5B | Series D |
| May 2024 | $3.25B | Series E |
| Sept 2025 | **$9.3B** | Series F |

Nearly 3x valuation increase in 16 months (Series E → F).

---

## Cap table

### Funding rounds

| Round | Date | Amount | Valuation | Lead |
|-------|------|--------|-----------|------|
| Series F | Sept 2025 | $300M | $9.3B | [[Accel]], [[GIC]] |
| Series E | May 2024 | $250M | $3.25B | [[Accel]] |
| Series D | Nov 2021 | $150M | $2.5B | [[GGV Capital]] |
| Series C | June 2021 | $102M | $1.1B | [[Salesforce Ventures]], [[Tiger Global]] |
| Series B | Dec 2020 | $40M | — | [[GV]] |
| Series A | Apr 2020 | $21M | — | [[Accel]] |
| Pre-A | 2015-2020 | — | — | Bootstrapped/angel |

**Total raised: $863M**

*ZEIT operated 5 years (2015-2020) before Series A with no formal VC rounds. The company struggled with investor perception during this period — seen more as a developer tool than a fundable startup. Series A coincided with ZEIT → Vercel rebrand in April 2020, which repositioned the company as an enterprise platform.*

**Secondary:** ~$300M tender offer for employees/early investors (Nov 2025).

### Key investors

| Investor | Rounds | Notes |
|----------|--------|-------|
| [[Accel]] | A, E, F | Series F co-lead; longest relationship |
| [[GIC]] | F | Series F co-lead (Singapore sovereign wealth) |
| [[GV]] | B | Google Ventures; Series B lead |
| [[Tiger Global]] | C | Series C co-lead |
| [[Salesforce Ventures]] | C | Series C co-lead |
| [[GGV Capital]] | D | Series D lead |
| [[BlackRock]] | F | First Vercel investment |
| [[General Catalyst]] | F | — |

### Ownership estimates

| Holder | Est. stake | Notes |
|--------|-----------|-------|
| [[Guillermo Rauch]] | 15-20% | Founder, likely largest individual holder |
| [[Accel]] | 10-15% | Multi-round investor, Series F co-lead |
| [[GIC]] | 5-10% | Series F co-lead |
| [[a16z]] | 5-10% | Early investor |
| Other VCs | 20-30% | Khosla, General Catalyst, BlackRock, etc. |
| Employees | 15-25% | Option pool, reduced by Nov 2025 tender |

*Estimates based on funding history and typical VC ownership patterns. Not confirmed.*

---

## Products

### Next.js

Open-source React framework created by Vercel (2016):

| Metric | Value |
|--------|-------|
| GitHub stars | 130K+ |
| Weekly downloads | Record-breaking |
| 2024 downloads | More than 2016-2024 combined |

**Key features:** Server-side rendering, static generation, API routes, edge functions. De facto standard for React production apps.

### v0

AI-powered web development tool (launched 2023):

| Metric | Value |
|--------|-------|
| Users | 3.5M+ unique |
| Revenue mix | 50%+ from Teams/Enterprise |
| Award | 2025 Webby (developer tools) |

Generates web applications from natural language prompts. Part of the "vibe coding" wave alongside Bolt.new, [[Lovable]], [[Cursor]].

### AI SDK

Developer toolkit for building AI applications:

| Metric | Value |
|--------|-------|
| Weekly downloads | 3M+ |

---

## Key customers

| Tier | Companies |
|------|-----------|
| Enterprise | [[Nike]], [[Walmart]], [[Target]], [[PayPal]], [[AT&T]], Hulu |
| AI/Tech | Midjourney, [[Grok]], [[Notion]] |
| Startups | Thousands via free tier |

---

## What makes Vercel work

### The Next.js flywheel

```
Next.js adoption → Developers learn Vercel →
Vercel deployments → Revenue →
Invest in Next.js → More adoption
```

**Key insight:** By open-sourcing Next.js and making it the best React framework, Vercel created massive top-of-funnel for its paid deployment platform.

### Structural advantages

| Advantage | Why it matters |
|-----------|----------------|
| **Own the framework** | Next.js is the standard; Vercel is optimized for it |
| **Developer love** | 130K GitHub stars, massive community |
| **AI timing** | v0 caught the vibe coding wave early |
| **Enterprise motion** | [[Nike]], [[Walmart]] validate for other enterprises |

---

## Vinext feud (Feb 2026)

[[Cloudflare]] launched **[[Vinext launch|Vinext]]** — an AI-generated reimplementation of the Next.js API on Vite. One engineer, $1,100, one week. [[Guillermo Rauch]] responded by disclosing 7 security vulnerabilities (2 critical) and branding it a "vibe-coded framework." Also posted a "Migrate to Vercel from Cloudflare" guide. The episode highlights Next.js's tight coupling to Vercel as both a strength (ecosystem control) and vulnerability (competitors motivated to rewrite rather than adapt).

---

## Apr 19-20, 2026 — security incident via [[Context.ai]]

Vercel disclosed a security incident in a bulletin first published on Apr 19 and updated on Apr 20. The company said unauthorized access reached certain internal systems, initially compromising a limited subset of customer credentials, while services remained operational.

### What happened

Vercel traced the incident to [[Context.ai]], a third-party AI tool used by a Vercel employee. According to the bulletin, the attacker used that compromise to take over the employee's Vercel Google Workspace account, which then provided access to some Vercel environments and environment variables that were not marked as sensitive.

Vercel said it had no evidence that values stored with its "sensitive environment variables" feature were accessed.

### Response

The company told customers to review activity logs, rotate any non-sensitive environment variables that may actually contain secrets, inspect recent deployments, and rotate Deployment Protection tokens. It also published the compromised OAuth app ID as an IOC and said it was working with Mandiant, law enforcement, and Context.ai.

### Why it matters

The important readthrough is structural, not just operational. Vercel sits in the deployment path for a large share of the modern JavaScript stack, and the breach path ran through an employee's AI-tool workflow rather than through a classic Vercel software exploit. That makes this a live example of AI tooling becoming part of the enterprise identity and supply-chain surface.

---

## Competitive landscape

| Competitor | Positioning |
|------------|-------------|
| Netlify | Similar (frontend platform), smaller |
| AWS Amplify | [[Amazon]]'s version, less DX-focused |
| [[Cloudflare]] Pages | Edge-first, CDN heritage |
| Railway | Broader backend focus |

---

## Quick stats

| Metric | Value |
|--------|-------|
| Status | Private |
| Valuation | $9.3B (Sept 2025) |
| ARR | ~$200M |
| Total raised | $863M |
| Founded | 2015 |
| HQ | San Francisco |
| Key product | Next.js |

---

## Related

- [[Guillermo Rauch]] — founder/CEO
- [[Supabase]] — often paired for full-stack (Rauch is angel investor)
- [[Accel]] — Series A, E, F investor; longest VC relationship
- [[GIC]] — Series F co-lead (Singapore sovereign wealth)
- [[Tiger Global]] — Series C co-lead
- [[Salesforce Ventures]] — Series C co-lead
- [[GGV Capital]] — Series D lead
- [[OpenAI]] — AI tools (v0) powered by OpenAI models
- [[Context.ai]] — third-party AI tool identified as the initial compromise vector in Apr 2026
- [[Y Combinator]] — many YC companies deploy on Vercel

---

Sources:
- [Vercel Series F blog](https://vercel.com/blog/series-f)
- [Business Wire - Series F announcement](https://www.businesswire.com/news/home/20250930898216/en/)
- [Sacra - Vercel profile](https://sacra.com/c/vercel/)
- [TapTwice - Vercel statistics](https://taptwicedigital.com/stats/vercel)
- [Tracxn - Vercel funding](https://tracxn.com/d/companies/vercel/__uPuJfXzfvAQs0wmUuqRiXFxW4uGbcaKUHjHks8VPbrI/funding-and-investors)
- [TechCrunch - Series D](https://techcrunch.com/2021/11/23/vercel-raises-150m-series-d-as-it-looks-to-build-an-end-to-end-front-end-development-platform/)
- [Vercel April 2026 security incident bulletin](https://vercel.com/kb/bulletin/vercel-april-2026-security-incident)

*Created 2026-01-14*
