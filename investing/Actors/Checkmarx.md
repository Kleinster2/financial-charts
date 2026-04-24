---
aliases: []
---
#actor #cybersecurity #software #israel #us #private

**Checkmarx** — Application security testing (SAST). Legacy player vs [[Snyk]]. $150M+ ARR. Owned by Hellman & Friedman (90%). On the block for ~$2.5B.

---

## Quick stats

| Metric | Value |
|--------|-------|
| Founded | 2006 |
| HQ | Paramus, New Jersey (origins: Israel) |
| Founders | Emmanuel Benzaquen (CEO), Maty Siman (CTO) |
| Employees | ~900 |
| ARR | $150M+ (Checkmarx One, Oct 2025) |
| Status | Private, PE-owned |

---

## Ownership

| Owner | Stake | Notes |
|-------|-------|-------|
| Hellman & Friedman | 90% | Acquired 2020 for $1.15B |
| TPG | Minority | Co-investor with H&F |
| Insight Partners | Minority | Former majority owner |
| Employees/founders | ~10% | |

---

## Acquisition history

| Date | Event | Value |
|------|-------|-------|
| 2020 | H&F acquired from Insight Partners | $1.15B |
| 2024 | H&F exploring sale | Asking $2.5B |

Revenue doubled under H&F ownership (slight decline 2023). Now seeking exit at 2x+ entry.

---

## Product

| Product | Function |
|---------|----------|
| Checkmarx One | Unified AppSec platform |
| SAST | Static application security testing |
| SCA | Software composition analysis |
| DAST | Dynamic testing |
| API Security | |

Legacy positioning — Snyk framed itself as the "modern" alternative.

---

## Competitive landscape

| Competitor | Notes |
|------------|-------|
| [[Snyk]] | Developer-first, higher valuation but struggling |
| Veracode | TA Associates bought for $2.5B (2022) |
| Synopsys SIG | Francisco/Clearlake bought for $2.1B (2024) |
| GitHub Advanced Security | Native to [[GitHub]]/[[Microsoft]] |
| SonarQube | Code quality + security |

---

## Valuation context

| Company | Valuation | Owner |
|---------|-----------|-------|
| Checkmarx | $2.5B (ask) | H&F |
| [[Snyk]] | $3-8.5B (range) | Various |
| Veracode | $2.5B | TA Associates |
| [[Wiz]] | $32B | [[Google]] |

Snyk valued at nearly 3x Checkmarx despite similar revenue scale — reflects "modern vs legacy" perception.

---

## KICS supply-chain compromise (Apr 22, 2026)

Checkmarx took a credibility hit when attackers compromised distribution channels for its open-source KICS scanner (Keeping Infrastructure as Code Secure). The incident matters beyond one free tool because KICS is used precisely in environments that process sensitive infrastructure configs, tokens, and cloud credentials.

| Element | What happened |
|---------|----------------|
| Affected channels | Docker Hub images, VS Code extension, Open VSX extension |
| Malicious feature | Hidden "MCP addon" downloader fetching `mcpAddon.js` from GitHub |
| Stolen targets | GitHub tokens, AWS/Azure/GCP creds, npm tokens, SSH keys, Claude configs, env vars |
| Exfiltration | `audit.checkmarx.cx` impersonation domain + public GitHub repos |
| Docker exposure window | 2026-04-22 14:17:59 UTC to 15:41:31 UTC |
| Safe versions cited by researchers | KICS Docker v2.1.20, ast-github-action v2.3.36, VS Code ext v2.64.0, Developer Assist v1.18.0 |

The strategic problem is not just remediation. It is that Checkmarx is already fighting the "legacy AppSec platform" discount while owner [[Hellman & Friedman]] explores a sale around $2.5B. A supply-chain compromise in a developer-security product sharpens the exact bear case buyers already worry about: slower product velocity, weaker trust, and less developer mindshare than newer platforms like [[Snyk]].

Researchers at Socket said the malicious artifacts have been removed. But any developer who pulled the affected images or extensions during the exposure window has to assume secrets are compromised, rotate credentials, and rebuild from a known-safe state.

---

## Investment case

**Bull:**
- Revenue doubled under H&F
- AppSec market growing (shift-left trend)
- Checkmarx One platform consolidation
- Strategic value to larger security players

**Bear:**
- Legacy perception vs Snyk
- PE exit pressure
- Competitive market (Snyk, GitHub, Wiz adjacency)
- Slight revenue decline in 2023
- KICS supply-chain breach damages trust during sale process

---

## Related

- [[Snyk]] — primary competitor
- [[Wiz]] — cloud security (now [[Google]])
- [[Cybersecurity]] — sector
- [[GitHub]] — owns competing product

---

## Sources

- [Bank Info Security: H&F selling Checkmarx](https://www.bankinfosecurity.com/blogs/hellman-friedman-wants-to-unload-checkmarx-for-25b-p-3715)
- [Calcalist: Checkmarx $2.5B](https://www.calcalistech.com/ctechnews/article/byr00iua2c)

*Created 2026-02-01*
