---
aliases: [Tailscale Inc]
---
#actor #company #private #infrastructure #vpn #networking

**Tailscale** — Mesh VPN built on the WireGuard protocol. Founded 2019 by Avery Pennarun (CEO) with ex-Google engineers including Brad Fitzpatrick (LiveJournal, memcached, Go standard library). $272M raised through Series C (April 2025). Positioned as VPN replacement, not just tunneling. Tailscale Funnel feature competes with [[ngrok]] and [[Cloudflare]] Tunnels for [[Agentic AI]] exposure.

Strategic framing: WireGuard turned VPNs from a plumbing problem (packet crypto, NAT traversal, key exchange) into a thin-client problem (identity, device enrollment, coordination). Tailscale built the orchestration layer on top, user identity, device inventory, ACLs, and DNS, which is where the defensible product surface lives.

---

## Quick stats

| Metric | Value |
|--------|-------|
| Founded | 2019 |
| HQ | Toronto, Ontario |
| Founders | Avery Pennarun, David Crawshaw, David Carney, Brad Fitzpatrick |
| Status | Private |
| Employees | ~150 (est.) |

## Cap table / funding history

| Date | Event | Investors | Amount | Valuation | Notes |
|------|-------|-----------|--------|-----------|-------|
| 2019 | Founding | Avery Pennarun, David Crawshaw, David Carney, Brad Fitzpatrick | — | — | Company formed around a WireGuard-based mesh-VPN product vision |
| Nov 2020 | Series A | [[Accel]] | $12M | Not disclosed | Early institutional backing after initial developer adoption |
| May 2022 | Series B | [[CRV]], [[Insight Partners]] | $100M | ~$1B | Step-up round that established Tailscale as a unicorn |
| Apr 2025 | Series C | [[Accel]] | $160M | Not disclosed | Brought cumulative funding to $272M |

---

## What Tailscale does

Creates encrypted mesh network across all your devices using the WireGuard protocol:

```
Device A ←→ Tailscale Network ←→ Device B
         (direct P2P when possible)
```

| Feature | Function |
|---------|----------|
| Mesh VPN | Every device can reach every other device |
| WireGuard base | Modern, fast, audited encryption |
| Zero config | No port forwarding, firewall rules |
| NAT traversal | Punches through most networks |
| MagicDNS | Human-readable names for devices |

---

## Key features

### Exit Nodes
Route all internet traffic through a specific device, traditional VPN functionality.

### Subnet Routers
Expose entire subnets (office LANs, cloud VPCs) to your tailnet.

### Taildrop
Encrypted file sharing between devices (like AirDrop).

### Tailscale SSH
SSH without managing keys, authentication via Tailscale identity.

### Tailscale Funnel
Expose local services to the public internet, competes with [[ngrok]].

---

## Pricing

| Plan | Users | Devices | Cost |
|------|-------|---------|------|
| Personal | 3 | 100 | Free |
| Personal Plus | 6 | 100 | $6/user/month |
| Starter | Unlimited | 100 + 10/user | $6/user/month |
| Premium | Unlimited | 100 + 20/user | $18/user/month |
| Enterprise | Custom | Custom | Custom |

Free tier is generous for personal use.

---

## Tailscale Funnel vs tunneling

| Factor | Tailscale Funnel | [[ngrok]] | [[Cloudflare]] Tunnels |
|--------|------------------|-----------|------------------------|
| Requirement | Tailscale installed | ngrok account | Cloudflare account |
| Network membership | Yes (must join tailnet) | No | No |
| Free tier | Yes (with Personal) | Limited | Yes |
| Positioning | Part of mesh VPN | Pure tunneling | Part of Cloudflare stack |

Key difference: Tailscale is a VPN that also does public exposure. ngrok and Cloudflare are tunneling tools that do not give you a mesh network.

---

## Agentic AI relevance

For [[Local-first AI]] and [[Agentic AI]]:

| Use case | Tailscale solution |
|----------|--------------------|
| Access home AI from anywhere | Mesh VPN to home server |
| Expose MCP server | Tailscale Funnel |
| Secure agent-to-agent | Device-to-device encryption |

Less relevant than Cloudflare/ngrok for [[Clawdbot viral growth|OpenClaw]] use case because:
1. Requires installing Tailscale on all devices
2. Funnel is an add-on feature, not the core product
3. OpenClaw docs recommend Cloudflare

---

## Technology

| Component | Detail |
|-----------|--------|
| Protocol | WireGuard (kernel-level encryption) |
| Coordination | Tailscale control plane |
| Relay (DERP) | Falls back when P2P fails |
| Address space | 100.x.x.x (CGNAT range) |

Open-source client, proprietary control plane.

---

## Leadership

| Role | Name | Background |
|------|------|------------|
| CEO | Avery Pennarun | Co-founder; longtime infrastructure engineer and public face of the company |
| Co-founder | Brad Fitzpatrick | Created LiveJournal, memcached contributor, worked on Go at Google |
| Co-founder | David Crawshaw | Early engineering/founding team |
| Co-founder | David Carney | Early engineering/founding team |

---

## Founder notable

Brad Fitzpatrick created:
- LiveJournal (1999)
- memcached (2003)
- OpenID (contributed)
- Go standard library (Google)

Strong pedigree in infrastructure and distributed systems.

---

## Competitive landscape

| Competitor | Positioning |
|------------|-------------|
| ZeroTier | Similar mesh VPN, more DIY |
| Nebula | Slack's open-source mesh VPN |
| WireGuard | Protocol layer Tailscale builds on |
| Corporate VPN | Cisco, Palo Alto, legacy players |

### vs Traditional VPN

| Factor | Traditional VPN | Tailscale |
|--------|-----------------|-----------|
| Topology | Hub-and-spoke | Mesh (P2P) |
| Setup | Complex | Minutes |
| Performance | Bottleneck at hub | Direct connections |
| Scale | Requires planning | Add devices freely |

---

## Structural factors

| Factor | Detail |
|--------|--------|
| Remote work | Persistent remote and hybrid work supports VPN demand |
| Zero Trust adoption | Fits ZTNA architecture model |
| Developer channel | Bottom-up adoption via developer word-of-mouth |
| AI agents | Mesh networks can support distributed AI compute |
| Technology base | Built on WireGuard, an open protocol, so competitors can build on the same foundation |
| Enterprise competition | Established VPN and ZTNA vendors are present in the market |
| Company status | Private, no public investment vehicle |

---

## Related

### Concepts
- [[Agentic AI]] — mesh networking for agents
- [[Local-first AI]] — architecture pattern
- [[Zero Trust]] — Tailscale's security model

### Actors
- [[Cloudflare]] — competitor (Tunnels vs Funnel)
- [[ngrok]] — competitor (tunneling)
- [[Accel]] — Series A and Series C lead
- [[CRV]] — Series B co-lead
- [[Insight Partners]] — Series B co-lead

### Events
- [[Clawdbot viral growth]] — drove interest in tunneling and exposure tools

### Cross-vault
- [Technologies: WireGuard](obsidian://open?vault=technologies&file=WireGuard) — protocol internals, cryptography, and kernel integration behind Tailscale's mesh overlay

---

## Sources

- [Tailscale Pricing](https://tailscale.com/pricing)
- [Wikipedia: Tailscale](https://en.wikipedia.org/wiki/Tailscale)
- [TechCrunch: Tailscale Series B](https://techcrunch.com/2022/05/24/tailscale-raises-100m-at-1b-valuation/)

*Created 2026-02-02*
