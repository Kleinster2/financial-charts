---
aliases: [Tailscale Inc]
---
#actor #company #infrastructure #vpn #networking

**Tailscale** — Mesh VPN built on WireGuard. Founded 2019 by ex-Google engineers including Brad Fitzpatrick (LiveJournal, memcached). $272M raised through Series C (April 2025). Positioned as VPN replacement, not just tunneling. Tailscale Funnel feature competes with [[ngrok]] and [[Cloudflare]] Tunnels for [[Agentic AI]] exposure.

---

## Overview

| Metric | Value |
|--------|-------|
| Founded | 2019 |
| HQ | Toronto, Ontario |
| Founders | Avery Pennarun, David Crawshaw, David Carney, Brad Fitzpatrick |
| Status | Private |
| Employees | ~150 (est.) |

### Funding

| Round | Date | Amount | Lead |
|-------|------|--------|------|
| Series A | Nov 2020 | $12M | Accel |
| Series B | May 2022 | $100M | CRV, [[Insight Partners]] |
| Series C | Apr 2025 | $160M | Accel |
| **Total** | | **$272M** | |

---

## What Tailscale does

Creates encrypted mesh network across all your devices using WireGuard:

```
Device A ←→ Tailscale Network ←→ Device B
         (direct P2P when possible)
```

| Feature | Function |
|---------|----------|
| **Mesh VPN** | Every device can reach every other device |
| **WireGuard** | Modern, fast, audited encryption |
| **Zero config** | No port forwarding, firewall rules |
| **NAT traversal** | Punches through most networks |
| **MagicDNS** | Human-readable names for devices |

---

## Key features

### Exit Nodes
Route all internet traffic through a specific device — traditional VPN functionality.

### Subnet Routers
Expose entire subnets (office LANs, cloud VPCs) to your tailnet.

### Taildrop
Encrypted file sharing between devices (like AirDrop).

### Tailscale SSH
SSH without managing keys — authentication via Tailscale identity.

### Tailscale Funnel
**Expose local services to public internet** — competes with [[ngrok]].

---

## Pricing

| Plan | Users | Devices | Cost |
|------|-------|---------|------|
| **Personal** | 3 | 100 | Free |
| **Personal Plus** | 6 | 100 | $6/user/month |
| **Starter** | Unlimited | 100 + 10/user | $6/user/month |
| **Premium** | Unlimited | 100 + 20/user | $18/user/month |
| **Enterprise** | Custom | Custom | Custom |

Free tier is generous for personal use.

---

## Tailscale Funnel vs tunneling

| Factor | Tailscale Funnel | [[ngrok]] | [[Cloudflare]] Tunnels |
|--------|------------------|-----------|------------------------|
| **Requirement** | Tailscale installed | ngrok account | Cloudflare account |
| **Network membership** | Yes (must join tailnet) | No | No |
| **Free tier** | Yes (with Personal) | Limited | Yes |
| **Positioning** | Part of mesh VPN | Pure tunneling | Part of Cloudflare stack |

**Key difference:** Tailscale is a VPN that *also* does public exposure. ngrok/Cloudflare are tunneling tools that don't give you a mesh network.

---

## Agentic AI relevance

For [[Local-first AI]] and [[Agentic AI]]:

| Use case | Tailscale solution |
|----------|-------------------|
| **Access home AI from anywhere** | Mesh VPN to home server |
| **Expose MCP server** | Tailscale Funnel |
| **Secure agent-to-agent** | Device-to-device encryption |

Less relevant than Cloudflare/ngrok for [[Clawdbot viral growth|OpenClaw]] use case because:
1. Requires installing Tailscale on all devices
2. Funnel is add-on feature, not core product
3. OpenClaw docs recommend Cloudflare

---

## Technology

| Component | Detail |
|-----------|--------|
| **Protocol** | WireGuard (kernel-level encryption) |
| **Coordination** | Tailscale control plane |
| **Relay (DERP)** | Falls back when P2P fails |
| **Address space** | 100.x.x.x (CGNAT range) |

Open-source client, proprietary control plane.

---

## Founder notable

**Brad Fitzpatrick** — created:
- LiveJournal (1999)
- memcached (2003)
- OpenID (contributed)
- Go standard library (Google)

Strong pedigree in infrastructure/distributed systems.

---

## Competitive landscape

| Competitor | Positioning |
|------------|-------------|
| **ZeroTier** | Similar mesh VPN, more DIY |
| **Nebula** | Slack's open-source mesh VPN |
| **WireGuard** | Protocol (Tailscale builds on it) |
| **Corporate VPN** | Cisco, Palo Alto — legacy players |

### vs Traditional VPN

| Factor | Traditional VPN | Tailscale |
|--------|-----------------|-----------|
| Topology | Hub-and-spoke | Mesh (P2P) |
| Setup | Complex | Minutes |
| Performance | Bottleneck at hub | Direct connections |
| Scale | Requires planning | Add devices freely |

---

## Investment relevance

### Bull case

| Factor | Detail |
|--------|--------|
| **Remote work** | Permanent shift needs better VPN |
| **Zero Trust adoption** | Tailscale fits ZTNA model |
| **Developer love** | Strong word-of-mouth |
| **AI agents** | Mesh networks for distributed AI |

### Bear case

| Risk | Detail |
|------|--------|
| **Private** | No public investment vehicle |
| **Narrow moat** | WireGuard is open; others can build |
| **Enterprise sales** | Competing with established vendors |

---

## Related

### Concepts
- [[Agentic AI]] — mesh networking for agents
- [[Local-first AI]] — architecture pattern
- [[Zero Trust]] — Tailscale's security model

### Actors
- [[Cloudflare]] — competitor (Tunnels vs Funnel)
- [[ngrok]] — competitor (tunneling)
- [[Insight Partners]] — Series B investor

### Events
- [[Clawdbot viral growth]] — drove interest in tunneling/exposure tools

---

## Sources

- [Tailscale Pricing](https://tailscale.com/pricing)
- [Wikipedia: Tailscale](https://en.wikipedia.org/wiki/Tailscale)
- [TechCrunch: Tailscale Series B](https://techcrunch.com/2022/05/24/tailscale-raises-100m-at-1b-valuation/)

*Created 2026-02-02*
