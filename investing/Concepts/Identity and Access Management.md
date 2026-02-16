---
aliases: [IAM]
---
#concept #cybersecurity #infrastructure

# Identity and Access Management

The systems that control who — or what — can access which resources in an enterprise. IAM is the foundational layer of cybersecurity: before you can protect anything, you need to know who's asking.

---

## Core components

| Layer | What it does | Key vendors |
|-------|-------------|-------------|
| Authentication | Proves identity (passwords, MFA, SSO, biometrics) | [[Microsoft]] Entra ID, [[Okta]] |
| Authorization | Determines permissions (roles, policies, least privilege) | [[Okta]], [[CyberArk]] |
| Directory | Stores identity records | [[Microsoft]] Active Directory/Entra, [[Okta]] Universal Directory |
| Privileged access (PAM) | Controls admin/root/superuser credentials | [[CyberArk]], BeyondTrust, Delinea |
| Governance (IGA) | Reviews, certifies, audits access over time | [[SailPoint]], Saviynt |
| Customer identity (CIAM) | Manages external user login/registration | [[Okta]] (Auth0), ForgeRock |

---

## Market size

~$26B in 2025, growing at 10-15% CAGR depending on source. Projected $43-68B by 2030. North America ~37% of market, Asia-Pacific fastest growing.

US market specifically: ~$7.3B in 2025, projected ~$11.1B by 2030.

---

## The identity stack is expanding

IAM was originally built for one thing: human employees logging into on-premises systems. Each expansion created a new market layer:

| Era | Identity type | Challenge |
|-----|--------------|-----------|
| Pre-cloud | Employees on-prem | Active Directory solved it |
| Cloud migration | Employees across SaaS/cloud | SSO, federation (Okta, Entra ID) |
| API economy | Service accounts, API keys | Non-human identity (NHI) management |
| Zero trust | Every request verified | Context-aware, continuous authentication |
| Agentic AI | Autonomous AI agents | Agents chain tools, create credentials, act independently |

Each layer is additive — enterprises need all of them simultaneously.

---

## The agentic identity gap

The newest expansion is the most disruptive. AI agents don't fit existing IAM or NHI models:

| Dimension | Human identity | Service account (NHI) | AI agent |
|-----------|---------------|----------------------|----------|
| Behavior | Predictable patterns | Deterministic | Non-deterministic |
| Permissions | Role-based | Scoped to function | Needs broad access to be useful |
| Credential use | Logs in once | Static token/key | May create new credentials dynamically |
| Decision-making | Human judgment | None (executes code) | Autonomous, opaque reasoning |
| Audit | User explains actions | Logs suffice | Agent must justify intent |

This gap is why [[Cyata]] existed — and why [[Check Point]] acquired it within 7 months of stealth exit. See [[Agentic AI security]] for the full category breakdown.

[[CyberArk]] launched its Secure AI Agents Solution in Nov 2025, signaling incumbents are also moving into this space.

---

## Key competitive dynamics

The IAM market is consolidating around platform plays:

| Company       | Ticker | Strength                                                             | Recent moves                                                           |
| ------------- | ------ | -------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| [[Microsoft]] | MSFT   | Entra ID (formerly Azure AD), dominant in enterprise via M365 bundle | Copilot integration, conditional access                                |
| [[Okta]]      | OKTA   | Cloud-native workforce + customer identity (Auth0)                   | Palo Alto partnership (Jul 2025), AI-driven threat signals             |
| [[CyberArk]]  | CYBR   | Privileged access management leader                                  | Secure AI Agents Solution (Nov 2025), part of Israeli $72.6B exit wave |
| [[SailPoint]] | SAIL   | Identity governance                                                  | Healthcare IGA (Imprivata acquisition), machine identity governance    |
| Ping Identity | —      | Federation, API security                                             | Acquired by [[Thales]] (2023)                                          |
| ForgeRock     | —      | Customer/workforce identity                                          | Acquired by Ping/Thales                                                |

The [[Microsoft]] bundle threat is the structural bear case for every independent IAM vendor — Entra ID comes free with M365, and most enterprises already have it.

---

## Zero trust and IAM

[[Zero trust]] architecture makes IAM the enforcement point for every access decision. The old model (firewall = perimeter, inside = trusted) is dead. In zero trust, identity is the perimeter:

- Every request authenticated and authorized, regardless of network location
- Continuous verification, not one-time login
- Least privilege by default, just-in-time access elevation

This is structurally bullish for IAM vendors — more verification points = more IAM surface area to sell into.

---

## Related

- [[Agentic AI security]] — newest IAM expansion (agent identity governance)
- [[Cyata]] — first agentic identity startup acquired
- [[CyberArk]] — PAM leader, Israeli origin
- [[Check Point]] — acquired [[Cyata]] for agentic identity
- [[Cybersecurity]] — parent sector
- [[Zero trust]] — architectural driver of IAM expansion

---

*Created 2026-02-15*
