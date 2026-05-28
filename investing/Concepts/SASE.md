---
aliases: [Secure Access Service Edge, secure access service edge, single-vendor SASE, Prisma SASE]
tags: [concept, cybersecurity]
---
#concept #cybersecurity #networking

SASE is the cloud-delivered architecture that converges wide-area networking with security enforcement. The simple version: SD-WAN handles how users, branches, workloads, and clouds connect; the security service edge handles whether the connection should be allowed, inspected, logged, or blocked.

---

## Synthesis

SASE is the commercial packaging layer for [[Zero Trust]]. It turns the zero-trust idea - never trust a location just because it is "inside" the network - into a network/security buying decision. The core market tension is not whether enterprises need secure access; cloud apps, remote work, branch simplification, [[SaaS]] sprawl, and [[AI agents]] all push traffic outside the old data-center perimeter. The question is who owns the control plane. [[Zscaler]] wants the secure-access budget to stay with a cloud-native zero-trust exchange. [[Palo Alto Networks]] wants SASE bundled into a broader security platform that also owns firewalls, cloud security, identity, endpoint telemetry, SOC automation, and AI security. [[Cloudflare]] attacks from the programmable global-edge side, while [[Fortinet]] attacks from installed firewall and branch-networking distribution.

---

## Architecture

SASE combines the networking side of SD-WAN with the security-service side usually grouped as SSE.

| Layer | Function | Typical controls |
|-------|----------|------------------|
| SD-WAN | Steers branch, user, and cloud traffic across broadband, private links, [[5G]], or backbone paths | Routing, dynamic path selection, application performance, branch connectivity |
| SSE | Applies cloud-delivered security controls close to the user or workload | ZTNA, SWG, CASB, FWaaS, DLP, RBI |
| Unified control plane | Gives security/network teams one policy and logging surface | Identity-aware rules, device posture, data policy, telemetry, digital experience monitoring |

The practical flow is: identity and device posture are checked, traffic is sent to the nearest cloud point of presence, policies are applied there, and only the permitted application path is opened. That is why SASE is different from a classic VPN. The user is not dropped onto a trusted network; each session is mediated by policy.

*Sources: [Palo Alto Networks Cyberpedia, SD-WAN vs. SASE vs. SSE](https://www.paloaltonetworks.com/cyberpedia/sdwan-vs-sase-vs-sse); [Palo Alto Networks SASE architecture guide](https://www.paloaltonetworks.com/cyberpedia/sase-architecture).*

---

## Palo Alto-style bundled SASE

Palo Alto-style bundled SASE is SASE as an extension of platformization. The pitch is not "buy a secure web gateway." It is "use one vendor for remote access, branch connectivity, web security, SaaS controls, firewall policy, browser isolation, data protection, AI access controls, and security operations telemetry."

| Bundle layer | Palo Alto product surface | Strategic meaning |
|--------------|---------------------------|-------------------|
| Remote and private-app access | Prisma Access / ZTNA | Replaces VPN-style trust with application-level access |
| Web and SaaS security | SWG, CASB, DLP, RBI | Keeps browser and SaaS activity inside the same policy plane |
| Branch and WAN | Prisma SD-WAN / remote networks | Pulls branch connectivity into the same platform sale |
| Firewall policy | FWaaS / NGFW policy heritage | Lets Palo Alto reuse firewall inspection depth in cloud-delivered form |
| User experience and telemetry | ADEM / Prisma Access Browser / Prisma Agent | Makes secure access observable and easier to manage |

This is why the [[Zscaler]] read-through matters for [[Palo Alto Networks]]. If buyers evaluate SASE as a discrete secure-access category, Zscaler's cloud-native architecture has a strong story. If buyers evaluate it as one more module in a broader cyber-platform consolidation cycle, Palo Alto's account control and product breadth become the advantage.

*Sources: [Palo Alto Networks Prisma Access](https://www.paloaltonetworks.com/sase/access); [Palo Alto Networks SASE architecture guide](https://www.paloaltonetworks.com/cyberpedia/sase-architecture).*

---

## Vendor positions

| Vendor | SASE posture | Read-through |
|--------|--------------|--------------|
| [[Palo Alto Networks]] | Platform bundle around Prisma Access, Prisma SD-WAN, browser, FWaaS, SWG, CASB, ZTNA, and AI security | Best expression of "bundled SASE" as part of security platformization |
| [[Zscaler]] | Zero Trust Exchange, historically strongest in SSE/zero-trust access; added Zero Trust SD-WAN in 2024 | Pure-play secure-access leader now defending share of wallet against broader platforms |
| [[Cloudflare]] | Cloudflare One, global edge network plus zero-trust/security services and programmable controls | Edge-network and developer-platform angle; SASE sold as composable network/security cloud |
| [[Fortinet]] | FortiSASE attached to FortiGate, FortiGuard, and branch/firewall distribution | Hardware/firewall installed base as distribution wedge into SASE |

Zscaler's January 2024 Zero Trust SASE launch is the category response to single-vendor SASE pressure: add SD-WAN to an SSE/zero-trust exchange so branch networking and secure access do not split across vendors. That narrows the gap with Palo Alto and Fortinet, but it also confirms the market direction: SASE selection increasingly rewards unified networking plus security rather than point-product excellence alone.

*Sources: [Zscaler Zero Trust SASE release, Jan 23 2024](https://ir.zscaler.com/news-releases/news-release-details/zscaler-introduces-industrys-first-zero-trust-sase-built-zero); [Cloudflare One SASE platform](https://www.cloudflare.com/sase/).*

---

## Investment read-through

SASE is a growth market but not a clean single-factor equity basket. It cuts across pure-play cybersecurity, network equipment, cloud edge, and diversified software.

The useful framing is budget control:

| Buyer question | Winner if answer is yes |
|----------------|-------------------------|
| Do we want best-of-breed cloud proxy and zero-trust access? | [[Zscaler]] |
| Do we want to reduce vendors and buy from the broadest cyber platform? | [[Palo Alto Networks]] |
| Do we want security built into a global programmable edge network? | [[Cloudflare]] |
| Do we want branch/firewall continuity with SASE attached? | [[Fortinet]] |

That makes SASE central to [[Cybersecurity consolidation]]. It is one of the control surfaces where the consolidation thesis becomes observable: the same customer can either buy SASE as a specialized zero-trust architecture or absorb it into a larger security-platform contract.

---

## Journal

| Date | Event | Read-through |
|------|-------|--------------|
| 2024-01-23 | [[Zscaler]] launches Zero Trust SASE with Zero Trust SD-WAN | SSE leader answers single-vendor SASE pressure by adding branch/networking capability |
| 2026-05-26 | [[Zscaler]] Q3 FY2026 guide prompts [[Reuters]] to cite [[Palo Alto Networks]] platform competition in SASE | Confirms demand is still growing, but budget ownership is shifting toward platform bundles |

---

## Related

- [[Zero Trust]] - security model that SASE packages into enterprise access architecture
- [[Cybersecurity consolidation]] - platformization pressure that makes bundled SASE strategically important
- [[Cybersecurity]] - sector context
- [[Palo Alto Networks]] - bundled SASE/platformization expression
- [[Zscaler]] - zero-trust/SASE pure-play
- [[Cloudflare]] - SASE through global edge network and Cloudflare One
- [[Fortinet]] - firewall/branch distribution into FortiSASE

### Cross-vault

- [Technologies: SASE](obsidian://open?vault=technologies&file=SASE) - technical architecture, traffic path, and adjacent zero-trust/security terminology
- [Technologies: Zero Trust](obsidian://open?vault=technologies&file=Zero%20Trust) - security model behind SASE access control
