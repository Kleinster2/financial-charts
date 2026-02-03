---
aliases: [ngrok Inc]
---
#actor #company #infrastructure #developer-tools

**ngrok** — Secure tunneling platform that exposes local servers to the internet. Founded 2015 by Alan Shreve. Raised $50M from Lightspeed (2022). Standard tool for webhook testing, demos, and increasingly for [[Agentic AI]] infrastructure. Competes with [[Cloudflare]] Tunnels.

---

## Overview

| Metric | Value |
|--------|-------|
| Founded | 2015 |
| Founder/CEO | Alan Shreve |
| HQ | San Francisco |
| Funding | $50M Series A (Dec 2022) |
| Lead investor | [[Lightspeed Venture Partners]] |
| Status | Private |

---

## What ngrok does

Creates encrypted tunnels from public URLs to local services:

```
Internet → ngrok URL → encrypted tunnel → localhost:3000
```

| Use case | Example |
|----------|---------|
| **Webhook testing** | Stripe, GitHub callbacks to local dev |
| **Demos** | Share localhost with clients |
| **IoT/device access** | Reach devices behind NAT |
| **AI agents** | Expose local agent to internet |

---

## Pricing

| Plan | Cost | Features |
|------|------|----------|
| **Free** | $0 | 1 online endpoint, random URLs, rate limited |
| **Personal** | $8/month | 3 endpoints, static domains |
| **Pro** | $20/month | 10 endpoints, custom domains, no interstitial |
| **Pay-as-you-go** | $20/month + usage | Unlimited endpoints, enterprise features |
| **Enterprise** | Custom | SSO, SCIM, SLA, support |

Key limitation: Free tier shows interstitial warning page to visitors.

---

## Product evolution

Originally just tunneling. Now positioning as "API gateway + secure access":

| Feature | Added |
|---------|-------|
| Traffic inspector | 2024 |
| Replay for debugging | 2024 |
| Static domains (free) | 2024 |
| OAuth/OIDC integration | 2023 |
| IP restrictions | 2023 |

---

## Competitive landscape

| Competitor | Comparison |
|------------|------------|
| **[[Cloudflare]] Tunnels** | Free, but requires Cloudflare account; more enterprise-focused |
| **[[Tailscale]] Funnel** | Requires Tailscale network; mesh VPN positioning |
| **localhost.run** | Simpler, SSH-based |
| **Expose** | Open-source alternative |

### vs Cloudflare Tunnels

| Factor | ngrok | Cloudflare |
|--------|-------|------------|
| Free tier | Limited (1 endpoint, interstitial) | More generous |
| Setup | Faster (one command) | Requires account + config |
| Pricing | $20/month for serious use | Free for basic, paid for enterprise |
| Network | ngrok infrastructure | Cloudflare's 300+ PoPs |
| Developer love | High (original player) | Growing |

**Agentic AI context:** [[Clawdbot viral growth|OpenClaw]] recommends Cloudflare Tunnels over ngrok because it's free. This is a competitive threat for ngrok.

---

## Recognition

- **2025 Microsoft Store Awards winner** — Developer tools category
- **Stack Overflow "Most Useful Developer Tools 2024"** — Listed

---

## Investment relevance

### Thesis: Agentic infrastructure

As [[Local-first AI]] and [[Agentic AI]] grow, developers need to expose local services:
- AI agents receiving webhooks
- MCP servers for Claude/GPT
- Self-hosted tools

ngrok is incumbant but faces free competition from Cloudflare.

### Concerns

| Risk | Detail |
|------|--------|
| **Cloudflare competition** | Free tunnels eroding paid market |
| **Commoditization** | Tunneling is a feature, not a product |
| **Private** | No public investment vehicle |

---

## Related

### Concepts
- [[Agentic AI]] — driving tunnel demand
- [[Local-first AI]] — architecture requiring exposure

### Actors
- [[Cloudflare]] — primary competitor (Tunnels)
- [[Tailscale]] — mesh VPN with Funnel feature
- [[Lightspeed Venture Partners]] — lead investor

### Events
- [[Clawdbot viral growth]] — drove awareness but recommended Cloudflare

### Theses
- [[Cloudflare agentic infrastructure]] — Cloudflare's angle on this market

---

## Sources

- [ngrok Pricing](https://ngrok.com/pricing)
- [TechCrunch: ngrok raises $50M](https://techcrunch.com/2022/12/13/ngrok-a-service-to-help-devs-deploy-sites-services-and-apps-raises-50m/)
- [Lightspeed investment thesis](https://lsvp.com/stories/secure-scalable-frictionless-access-to-web-apps-why-lightspeed-invested-in-ngrok/)
- [Wikipedia: ngrok](https://en.wikipedia.org/wiki/Ngrok)

*Created 2026-02-02*
