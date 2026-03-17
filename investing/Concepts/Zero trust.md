---
aliases: [Zero Trust, ZTA, Zero Trust Architecture]
tags:
  - concept
  - cybersecurity
---

# Zero trust

Security architecture that eliminates implicit trust -- every access request is authenticated, authorized, and continuously verified regardless of network location. Identity becomes the perimeter, replacing the old castle-and-moat model where anything inside the firewall was trusted.

## Synopsis

Zero trust emerged from a 2010 Forrester Research paper by John Kindervag but took a decade to move from theory to procurement priority. The catalysts were the 2020 SolarWinds breach (which compromised "trusted" internal networks across US government agencies) and the COVID-era shift to remote work (which dissolved the concept of a corporate network perimeter entirely). NIST codified the framework in SP 800-207 (2020), and Executive Order 14028 (May 2021) mandated federal agencies adopt zero trust architectures, converting a security philosophy into a multi-billion-dollar government procurement wave.

The market runs through three layers: identity ([[CrowdStrike]], [[Okta]], [[Microsoft]] Entra ID), network access ([[Cloudflare]], [[Zscaler]], [[Palo Alto Networks]]), and endpoint verification ([[CrowdStrike]], [[SentinelOne]]). The TAM estimates vary wildly ($30-60B by 2028 depending on the analyst) because zero trust is less a product category than an architecture that touches every security budget line. The real investment question is whether zero trust spending is incremental to existing cybersecurity budgets or a reallocation within them. The [[Agentic AI security]] frontier adds a new dimension: when AI agents act autonomously across systems, zero trust principles (verify every request, assume breach) become the only viable security model.

Core principles: verify explicitly, use least privilege, assume breach.

## Quick stats

| Metric | Value |
|--------|-------|
| Coined by | John Kindervag, Forrester Research (2010) |
| NIST framework | SP 800-207 (August 2020) |
| Federal mandate | Executive Order 14028 (May 2021) |
| Market size | ~$30-60B by 2028 (estimates vary) |
| Key catalysts | SolarWinds breach (2020), remote work shift |

## Related

- [[Identity and Access Management]] — enforcement layer for zero trust
- [[Cybersecurity]] — parent sector
- [[Cloudflare]] — zero trust network access provider
- [[Zscaler]] — pure-play zero trust network security
- [[CrowdStrike]] — identity and endpoint verification
- [[Palo Alto Networks]] — network-layer zero trust
- [[Agentic AI security]] — zero trust principles applied to AI agents
- [[Okta]] — identity provider, zero trust enabler
