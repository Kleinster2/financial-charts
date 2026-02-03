---
aliases: []
---
#thesis #infrastructure #ai

**Cloudflare agentic infrastructure** — If local AI agents need secure tunnels to expose home networks safely, [[Cloudflare]] is the picks-and-shovels winner.

---

## The thesis

[[Agentic AI]] is shifting from cloud-only to [[Local-first AI]] — agents run on your machine, keep credentials local, but need internet access for tool use, webhooks, and remote triggers.

Problem: Exposing localhost to the internet is dangerous. Opening ports, configuring firewalls, managing certificates — most developers can't do this safely.

Solution: **Cloudflare Tunnels** — one command to securely expose local services through Cloudflare's network, with authentication, encryption, and DDoS protection included.

---

## Evidence

### Clawdbot/Moltbot adoption (Jan-Feb 2025)

[[Clawdbot viral growth|Clawdbot]] became the fastest-growing open-source project in GitHub history (82k+ stars in weeks). The recommended setup uses Cloudflare Tunnels to expose the local agent gateway.

**Cloudflare's response was immediate and strategic:**

On **January 29, 2026**, Cloudflare published "[Introducing Moltworker: a self-hosted personal AI agent, minus the minis](https://blog.cloudflare.com/moltworker-self-hosted-ai-agent/)" — an official blog post showcasing how to run Clawdbot (now OpenClaw/Moltbot) entirely on Cloudflare's infrastructure:

> "The Internet woke up this week to a flood of people buying Mac minis to run Moltbot... But what if you don't want to buy new dedicated hardware? Meet Moltworker, a middleware Worker and adapted scripts that allows running Moltbot on Cloudflare's Sandbox SDK and our Developer Platform APIs."

This is **direct evidence** that Cloudflare is actively positioning for the AI agent infrastructure market — not just passively benefiting from developer adoption, but **building dedicated tooling** to capture this workload.

### Stock performance context

| Metric | Value |
|--------|-------|
| 2025 annual return | **+83%** ($112.54 → $197.15) |
| 52-week range | $89.42 - $260.00 |
| All-time high | $253.30 (Oct 31, 2025) |
| Current price (Feb 2026) | ~$182 |
| Market cap | ~$64B |
| P/S ratio | ~31x |

*Note: The original "20% on Clawdbot" claim needs verification against specific dates. The broader 2025 rally reflects multiple catalysts including AI/developer platform momentum.*

---

## Cloudflare Tunnels: Pricing & positioning

### Pricing tiers (as of 2026)

| Tier | Price | Tunnel limits | Users |
|------|-------|---------------|-------|
| **Free** | $0 | Up to 1,000 tunnels | 50 users |
| **Pay-as-you-go** | $7/user/month | Same | Unlimited |
| **Enterprise** | Custom | Custom | Custom + SLA |

**Key insight:** Tunnels became **free in April 2021** (renamed from "Argo Tunnel"). This was a strategic land-grab — get developers on the platform for free, upsell to Zero Trust access controls, DLP, and enterprise features.

From the [April 2021 announcement](https://blog.cloudflare.com/tunnel-for-everyone/):
> "Starting today, we're excited to announce that any organization can use the secure, outbound-only connection feature of the product at no cost."

### Why free tunnels make strategic sense

1. **Land-and-expand**: Every developer running a tunnel is a potential Zero Trust customer
2. **Network effects**: More tunnels = more traffic through Cloudflare = better optimization data
3. **Lock-in**: Once authentication/routing is configured, switching costs are high
4. **Marginal cost**: Tunnels are outbound-only connections — low infrastructure cost vs. value created

---

## Developer platform strategy

Cloudflare has assembled a **complete AI agent runtime stack**:

| Product | Purpose | Agentic AI use case |
|---------|---------|---------------------|
| **Cloudflare Tunnels** | Secure localhost exposure | Agent webhook endpoints |
| **Workers** | Serverless compute | Agent logic, routing |
| **Workers AI** | 50+ ML models, serverless GPUs | Agent inference |
| **AI Gateway** | Proxy for any AI provider | Unified billing, observability |
| **Sandboxes** | Isolated code execution | Safe agent code execution |
| **Browser Rendering** | Headless Chromium | Web automation, screenshots |
| **R2** | Object storage | Agent memory, files |
| **D1** | Serverless SQL | Agent state, conversations |
| **Durable Objects** | Stateful coordination | Long-running agent sessions |

**The Moltworker architecture demonstrates this stack in action:**
- AI Gateway for Claude API routing
- Sandboxes for running the agent runtime
- R2 for persistent storage
- Browser Rendering for web automation
- Zero Trust Access for authentication

This is **not** just tunnels — it's a full **agentic AI hosting platform**.

---

## Competitive landscape

### Cloudflare Tunnels vs. alternatives

| Solution | Free tier | Production pricing | Key limitation |
|----------|-----------|-------------------|----------------|
| **Cloudflare Tunnels** | ✅ Unlimited tunnels, 50 users | $7/user/mo | None for developers |
| **ngrok** | ❌ 1 endpoint, limited | $20/mo minimum | Expensive at scale |
| **Tailscale Funnel** | ✅ 3 users, 100 devices | $6/user/mo | Requires Tailscale network |
| **DIY (port forwarding)** | ✅ Free | Free | Security nightmare |
| **Cloud hosting** | ❌ Varies | $5-50+/mo | Defeats local-first benefits |

### Why Cloudflare wins for AI agents

1. **Free tier is actually usable**: Most developers never need to pay
2. **Integrated stack**: Tunnels → Access → Gateway → Workers — one vendor
3. **310+ data centers**: Sub-50ms latency globally
4. **DDoS protection included**: Agent endpoints will be attacked
5. **Zero Trust authentication**: Control who can access your agent

### Ngrok comparison (detailed)

**Ngrok strengths:**
- Developer brand awareness (tunnels = ngrok for many)
- Simple CLI experience
- Good webhook debugging UI

**Ngrok weaknesses:**
- $20/month minimum for production use (vs. $0 for Cloudflare)
- No integrated AI stack
- No global CDN/security platform
- No path to enterprise Zero Trust

**Verdict**: Ngrok is a point solution. Cloudflare is a platform play.

### Tailscale comparison

**Tailscale Funnel** allows exposing local services to the internet, but:
- Requires devices to be on Tailscale network
- Oriented toward enterprise VPN replacement, not developer tools
- No integrated AI/serverless platform
- Different positioning (security-first vs. developer-first)

---

## Bear case

### 1. Free tier economics

**Risk**: If 90%+ of tunnel users stay on free tier, where's the revenue?

**Counter**: 
- Free tunnels → paid Zero Trust ($7/user/mo+)
- Free tunnels → paid Workers/AI Gateway usage
- Enterprise contracts dwarf pay-as-you-go pricing
- Q3 FY25 revenue: $562M (+28% YoY) — growth is real

### 2. Enterprise shift away from local agents

**Risk**: Enterprises may ban local AI agents for security/compliance, eliminating the TAM.

**Counter**:
- Even if enterprises ban consumer use, they'll **build their own** internal agents
- Those internal agents still need secure exposure for webhooks, integrations
- Cloudflare's Zero Trust positioning is actually *more* appealing to enterprises

### 3. Hyperscaler bundling

**Risk**: AWS, Azure, Google could bundle tunnel-like features into existing services.

**Counter**:
- They already have (AWS App Mesh, Azure Private Link, etc.) — developers still choose Cloudflare
- Cloudflare is **cloud-agnostic** — works with any infrastructure
- Developer experience gap is real and persistent

### 4. Agentic AI fizzles

**Risk**: AI agents turn out to be a dead end, local-first never materializes.

**Counter**:
- Weak signal so far — Clawdbot/Moltbot growth is genuine
- Even if consumer agents fizzle, enterprise automation workflows will persist
- Cloudflare's core business (CDN, security) is unaffected

### 5. Security incident involving agents

**Risk**: A major breach via an AI agent/tunnel could create reputational damage.

**Counter**:
- Cloudflare's Zero Trust features (Access, DLP, Browser Isolation) mitigate this
- Being the security layer is better than being the thing that got breached
- They're actively building agent-specific security tooling

---

## Valuation context

| Metric | NET | DDOG | SNOW | MDB |
|--------|-----|------|------|-----|
| P/S (TTM) | 31x | 20x | 16x | 13x |
| Revenue growth (YoY) | 28% | 26% | 28% | 22% |
| Free cash flow margin | 18% | 22% | 5% | 12% |

NET trades at a premium — but it has:
- Broader TAM (security + edge compute + AI)
- Platform optionality (new products compound)
- Strongest developer brand in the cohort

---

## What to watch

| Signal | Bullish | Bearish |
|--------|---------|---------|
| Agent projects | More use Cloudflare Tunnels | Alternatives emerge |
| Developer mindshare | "Just use Cloudflare" consensus | Fragmentation |
| Tunnel usage metrics | Disclosed in earnings calls | Not mentioned (quiet) |
| Workers AI growth | Highlighted as growth driver | De-emphasized |
| Zero Trust attach rate | Tunnels → paid conversion mentioned | Free users stay free |
| Security incidents | Cloudflare prevents agent-related breaches | Cloudflare-related breaches |
| Enterprise deals | Agents in enterprise contract conversations | Enterprises ban local agents |

### Earnings call keywords to monitor

- "Tunnels" / "cloudflared" usage metrics
- "AI agents" / "agentic" mentions
- "Developer platform" revenue contribution
- "Workers AI" / "AI Gateway" adoption
- Zero Trust attach rates from free users

---

## Position sizing

This is an **incremental thesis** on top of Cloudflare's existing business (CDN, security, edge compute). The agentic infrastructure angle adds **optionality** but doesn't change the core investment case.

**Considerations:**
- Valuation is rich at 31x P/S — priced for continued execution
- The Moltworker blog post (Jan 2026) shows management is aware and executing
- AI agent infrastructure is *additive* to existing TAM, not the whole story
- Entry on pullbacks preferred; current price (~$182) is off highs ($253)

---

## Related

### Concepts
- [[Agentic AI]] — what's driving demand
- [[Local-first AI]] — architecture requiring tunnels
- [[Zero Trust]] — Cloudflare's enterprise security play

### Actors
- [[Cloudflare]] — the play
- [[Anthropic]] — Claude powers most AI agents including Clawdbot
- [[ngrok]] — competitor (point solution)
- [[Tailscale]] — competitor (different positioning)

### Events
- [[Clawdbot viral growth]] — catalyst that proved the thesis

---

*Created 2026-01-28 | Updated 2026-02-02*
