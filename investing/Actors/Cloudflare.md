---
aliases: [NET, Cloudflare Inc]
---
#actor #company #infrastructure #cybersecurity #edge

**Cloudflare** (NET) — Edge cloud platform providing CDN, DDoS protection, DNS, and Zero Trust security. Powers ~20% of websites globally. Key government vendor: .gov DNS contract, 40+ federal agencies, NYC smart city security. AI inference at edge emerging growth driver.

---

## Sector correlation

| Sector | ETF | Correlation |
|--------|-----|-------------|
| Software | IGV | 0.70 |
| Technology | XLK | 0.64 |
| [[Consumer]] | XLY | 0.60 |
| *S&P 500* | *SPY* | *0.61* |

NET trades as a core Software name (IGV r = 0.70).

---

## Quick stats

| Metric | Value |
|--------|-------|
| Ticker | NET (NYSE) |
| Founded | 2009 |
| IPO | September 2019 |
| HQ | San Francisco |
| CEO | Matthew Prince (co-founder) |
| Employees | ~4,000 |

---

## Financials

| Metric | Value |
|--------|-------|
| Market cap | ~$35B (Jan 2026) |
| Revenue (2025E) | ~$1.7B |
| Revenue growth | ~25-30% YoY |
| Gross margin | ~78% |
| Net retention | 115%+ |
| [[Free cash flow]] | Turning positive |

---

## Core services

### Security

| Service | Function |
|---------|----------|
| **DDoS protection** | Largest network (>300 Tbps capacity) |
| **WAF** | Web application firewall |
| **Bot management** | Credential stuffing, scraping defense |
| **Zero Trust** | SASE, secure access |
| **Email security** | Area 1 acquisition (2022) |

### Performance

| Service | Function |
|---------|----------|
| **CDN** | Global content delivery |
| **DNS** | 1.1.1.1 resolver, authoritative DNS |
| **Argo** | Smart routing optimization |
| **Load balancing** | Traffic distribution |

### Developer platform

| Service | Function |
|---------|----------|
| **Workers** | Serverless compute at edge |
| **R2** | S3-compatible object storage (zero egress fees) |
| **Pages** | Static site hosting |
| **D1** | Serverless SQL database |
| **KV** | Key-value storage |
| **Durable Objects** | Stateful serverless |

---

## Network scale

| Metric | Value |
|--------|-------|
| Data centers | 310+ cities |
| Countries | 120+ |
| Network capacity | 300+ Tbps |
| Websites protected | ~20% of web |
| Daily requests | Trillions |

---

## Government business

### Federal

| Contract | Detail |
|----------|--------|
| **CISA .gov DNS** | $7.2M contract (Jan 2023) |
| **Federal agencies** | 40+ using Cloudflare |
| **FedRAMP** | Authorized (Moderate) |
| **Protective DNS** | FCEB agencies since 2021 |

### State & local

| Client | Services |
|--------|----------|
| **NYC Government** | WAF, DDoS — 500M requests blocked/month |
| **Other municipalities** | Expanding footprint |

### Why government likes Cloudflare

| Factor | Detail |
|--------|--------|
| **Speed** | Deploys in hours vs weeks |
| **Scale** | Handles nation-state attacks |
| **Compliance** | FedRAMP, SOC 2, ISO 27001 |
| **Cost** | Often cheaper than legacy vendors |

---

## AI at the edge

### Workers AI

| Feature | Detail |
|---------|--------|
| Launch | 2023 |
| Models | LLMs, image, speech at edge |
| Latency | <50ms inference globally |
| Pricing | Per-request, no GPU management |

### AI Gateway

| Feature | Detail |
|---------|--------|
| Function | Proxy for AI API calls |
| Features | Caching, rate limiting, logging |
| Supported | [[OpenAI]], [[Anthropic]], etc. |

### Investment angle

Cloudflare positioning for AI inference at edge — complementary to centralized GPU clouds (hyperscalers). As AI moves to devices/edge, Cloudflare's network becomes inference infrastructure.

---

## Agentic AI infrastructure (Feb 2025)

**[[Clawdbot viral growth|Clawdbot]] adoption drove Cloudflare stock +20%** — single viral open-source project demonstrating infrastructure value.

### Why Cloudflare Tunnels

[[Agentic AI]] and [[Local-first AI]] need to expose local services safely:
- AI gateway runs on localhost
- Needs internet access for webhooks, remote triggers
- Opening ports is dangerous
- Cloudflare Tunnels = one command to secure expose

| Feature | Benefit for agents |
|---------|-------------------|
| **Authentication** | Control who accesses your agent |
| **Encryption** | HTTPS everywhere |
| **DDoS protection** | Agent endpoints will be attacked |
| **Free tier** | Developers start here |

### Thesis: [[Cloudflare agentic infrastructure]]

If local AI agents need secure tunnels to expose home networks safely, Cloudflare is picks-and-shovels winner.

**Moltworker (Jan 29, 2026):** Cloudflare published [official solution](https://blog.cloudflare.com/moltworker-self-hosted-ai-agent/) for running AI agents on their infrastructure:

> "The Internet woke up this week to a flood of people buying Mac minis to run Moltbot... But what if you don't want to buy new dedicated hardware?"

Full stack: AI Gateway → Sandboxes → R2 → Browser Rendering → Zero Trust Access. Minimum $5/month Workers plan.

**AI Agents market context:** $7.63B (2025) → $182.97B (2033), 49.6% CAGR (Grand View Research).

**Net new TAM:** Every developer running a local AI agent is a potential Cloudflare customer. This wasn't true two years ago.

---

## Anthropic Managed Agents selloff (Apr 10, 2026)

Cloudflare fell 13.5% on Apr 10, 2026, from $193.05 to $166.99, after [[Anthropic]] launched [[Anthropic Managed Agents]].

The market's concern was that Anthropic had moved beyond selling the model and into selling the runtime layer itself: long-lived sessions, sandboxed code execution, checkpointing, credential management, scoped permissions, tracing, and tool orchestration. That challenged the thesis that agent growth would automatically benefit neutral edge platforms.

Why Cloudflare got hit:
- its AI narrative had shifted toward being the neutral substrate for agentic workloads
- Anthropic's hosted runtime threatened to absorb part of that control-plane narrative upstream
- if the model vendor owns the agent runtime, networking and security vendors risk becoming lower-multiple components inside someone else's stack

What did not change:
- Managed Agents does not replace Cloudflare's global network, DDoS protection, Zero Trust edge, or multi-model traffic layer
- Cloudflare still matters for public ingress, enterprise perimeter control, caching, and vendor-neutral deployment
- the repricing was about value capture in the agent stack, not about edge demand disappearing

This partially reversed the earlier "Cloudflare as agentic picks-and-shovels winner" narrative. [[Anthropic Managed Agents selloff April 2026]] showed that even inside infrastructure software, the highest-value layer may accrue to whoever owns the agent control plane.

---

## Competitive position

| Competitor | Cloudflare advantage |
|------------|---------------------|
| **Akamai** | Simpler pricing, developer platform |
| **Fastly** | Larger network, more features |
| **AWS CloudFront** | Vendor-neutral, zero egress (R2) |
| **[[Zscaler]]** | Integrated platform (CDN + security) |

### Moat

| Factor | Detail |
|--------|--------|
| **[[Network effects]]** | More traffic → better threat intelligence |
| **Developer love** | Workers platform sticky |
| **Free tier** | Massive funnel to paid |
| **Data advantage** | Sees 20% of web traffic |

---

## Risks

| Risk | Detail |
|------|--------|
| **Concentration** | Top 10 customers ~10% revenue |
| **Controversy** | Content moderation decisions (8chan, Kiwi Farms) |
| **Competition** | Hyperscalers bundling CDN/security |
| **Profitability** | Still investing heavily |

---

## Smart city relevance

| Application | Example |
|-------------|---------|
| **City portals** | DDoS protection for .gov sites |
| **Open data** | CDN for public datasets |
| **IoT security** | Edge protection for sensors |
| **API gateway** | Securing city APIs |

Cloudflare increasingly critical infrastructure for [[Urban digitization]] — as cities digitize, attack surface grows, edge security essential.

---

## Investment relevance

| Angle | Detail |
|-------|--------|
| **Government expansion** | .gov DNS → broader federal/state |
| **AI inference** | Edge compute for AI workloads |
| **R2 disruption** | Zero egress challenging AWS |
| **Developer platform** | Workers competing with Lambda@Edge |
| **Smart cities** | Security layer for urban infrastructure |

---


![[net-employees-chart.png]]
*Headcount: 4,263 (2024) — up 15.8% YoY*

## Vinext — Next.js reimplementation (Feb 2026)

Launched **[[Vinext launch|Vinext]]** — AI-generated reimplementation of Next.js API on Vite. One engineer, Claude, 800+ sessions, $1,100, one week. 94% API coverage, 4.4× faster builds, 56% smaller bundles. [[Vercel]]'s [[Guillermo Rauch]] fired back disclosing 7 security vulnerabilities and calling it a "vibe-coded framework." See [[Vinext launch]] for full details.

---

## EmDash CMS launch (April 2026)

Announced **April 1, 2026** — [[EmDash]], an open-source TypeScript CMS built on [[Astro]] 6.0, positioned as the "spiritual successor to WordPress." v0.1.0 developer beta. Two months of AI-assisted development by Matt Kane (Astro core team member).

**Core innovations:**
- **Sandboxed plugins** — each runs in its own Worker isolate with declared permissions (capabilities manifest). Addresses WordPress's fundamental security flaw (96% of WP vulnerabilities from plugins)
- **Serverless-native** — scales to zero, runs on Workers
- **AI-native** — built-in MCP server, CLI, Agent Skills files. Designed for AI agents to build and manage sites
- **x402 payments** — HTTP-native micropayments for the agent era (no subscriptions needed)
- **MIT license** — plugins can use any license (vs WordPress GPL inheritance debate)

**Matt Mullenweg response (Apr 3):** Called it "very solid" engineering but rejected "spiritual successor" claim. Framed as Cloudflare upsell vehicle. Praised the Skills system as "brilliant." Predicted "tens of thousands of sites."

**Sequence:** Vinext (Feb 2026, rebuilt Next.js in one week) → EmDash (Apr 2026, rebuilt WordPress in two months). Pattern: AI-generated reimplementations of dominant web frameworks, each landing on Cloudflare's platform.

See [[EmDash]] for full product note.

---

## Related

### Concepts
- [[Smart cities]] — Cloudflare secures city infrastructure
- [[Urban digitization]] — edge security for retrofit cities
- [[Data gravity]] — Cloudflare R2 challenges with zero egress
- [[Zero Trust]] — SASE market
- [[Agentic AI]] — Tunnels for local agent exposure
- [[Local-first AI]] — infrastructure layer

### Actors
- [[NYC smart city]] — 500M requests blocked/month
- [[Vercel]] — uses Cloudflare, also competes (edge functions)
- Akamai — legacy CDN competitor
- Fastly — developer-focused competitor
- [[Zscaler]] — Zero Trust competitor

### Products
- [[EmDash]] — open-source CMS, WordPress successor (Apr 2026)
- [[Astro]] — web framework (acquired Jan 2026)

### Events
- [[Clawdbot viral growth]] — AI agent adoption wave (2025)

### Recent M&A
- **Astro acquisition** (Jan 16, 2026) — Web framework used by Porsche, IKEA, OpenAI
- **Human Native acquisition** (Jan 15, 2026) — AI data marketplace for content transformation

### Theses
- [[Cloudflare agentic infrastructure]] — AI agent infrastructure play

### Sectors
- [[Data Centers]] — edge vs centralized
- [[Cybersecurity]] — WAF, DDoS market

---

## Sources

- [Cloudflare NYC Government Case Study](https://www.cloudflare.com/case-studies/nyc-government-financial-agency/)
- [Cloudflare CISA DNS Contract](https://www.cloudflare.com/press-press-releases/2023/cloudflare-wins-cisa-contract-for-dns-services/)
- [Cloudflare Investor Relations](https://cloudflare.net/)

*Created 2026-01-14*
