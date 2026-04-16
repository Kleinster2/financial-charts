---
aliases: [Cyber AI disruption basket, AICD basket]
tags: [basket/internal, ai, disruption, cybersecurity]
---

# AI cybersecurity disruption basket

Cybersecurity stocks that sell off on AI capability announcements threatening traditional security tooling. The basket crystallized on Feb 20, 2026, when [[Anthropic]]'s [[Claude Code Security]] launch — an AI-powered vulnerability scanner that reasons about code like a human researcher — sent the sector sharply lower despite broader indices rising.

This is the security-specific counterpart to the broader software selloff in [[February 2026 AI Disruption Cascade]]. The thesis: if AI models can autonomously find and patch vulnerabilities better than rule-based static analysis tools, the moat around traditional AppSec/vulnerability management vendors narrows significantly.

---

## Catalyst: Claude Code Security (Feb 20, 2026)

[[Anthropic]] announced [[Claude Code Security]] — built on Opus 4.6, which found 500+ vulnerabilities in production open-source code that went undetected for decades. The tool reasons about code contextually rather than matching patterns, catching business logic flaws and broken access control that static analysis misses.

This was the second AI-driven selloff in the enterprise software sector in February 2026, following the [[Claude Cowork disruption February 2026|Claude Cowork SaaSpocalypse]] on Feb 3-4.

---

## Constituents

Weights derived from Feb 20 selloff magnitude — bigger drop = higher disruption exposure as revealed by the market.

### Most exposed — AppSec / vulnerability management (45%)

These companies compete most directly with AI-powered code scanning:

| Ticker | Company | Weight | Feb 20 move | Why exposed |
|--------|---------|--------|-------------|-------------|
| OKTA | [[Okta]] | 12% | -9.2% | Identity/access management — Claude Code Security catches broken access control |
| NET | [[Cloudflare]] | 11% | -8.1% | Application security (WAF, bot management) — AI could reduce need for rule-based WAFs |
| CRWD | [[CrowdStrike]] | 10% | -8.0% | Endpoint + cloud security — largest pure-play, bellwether for sector sentiment |
| S | [[SentinelOne]] | 7% | -7.5% | AI-native endpoint — ironically, AI disrupting an AI security company |
| QLYS | [[Qualys]] | 5% | ~-6% | Pure vulnerability management — most directly threatened by AI scanning |

### Moderately exposed — network / cloud security (35%)

Less direct competition but investors pricing in broader AI disruption of security:

| Ticker | Company | Weight | Feb 20 move | Why exposed |
|--------|---------|--------|-------------|-------------|
| ZS | [[Zscaler]] | 8% | -5.5% | Cloud security — zero trust architecture less affected but sentiment-driven |
| FTNT | [[Fortinet]] | 7% | -4.8% | Network security + FortiGuard threat intelligence |
| DDOG | [[Datadog]] | 7% | -4.5% | Observability/monitoring — adjacent to security scanning |
| RPD | [[Rapid7]] | 7% | ~-5% | Vulnerability management + SIEM — directly threatened |
| TENB | [[Tenable]] | 6% | ~-5% | Vulnerability management — core business at risk |

### Less exposed — platform / diversified (20%)

| Ticker | Company | Weight | Feb 20 move | Why exposed |
|--------|---------|--------|-------------|-------------|
| PANW | [[Palo Alto Networks]] | 8% | -0.6% | Diversified platform — CEO Arora pushed back on AI threat narrative days before |
| CYBR | [[CyberArk]] | 6% | ~-3% | Identity security — specialized enough to resist |
| SNYK | Snyk (private) | 3% | N/A | Developer security — most directly comparable to Claude Code Security |
| GEN | Gen Digital | 3% | ~-2% | Consumer security (Norton, Avast) — less enterprise overlap |

---

## Persistence check (2020-2026)

Pairwise excess-return correlation (vs [[SPY]]) across multi-year periods. Uses 10 of the 13 constituents with sufficient history ([[Okta]], [[Cloudflare]], [[CrowdStrike]], [[SentinelOne]], [[Qualys]], [[Zscaler]], [[Fortinet]], [[Datadog]], [[Rapid7]], [[Tenable]], [[Palo Alto Networks]], [[CyberArk]], Gen Digital). Benchmark: [[Security control points]] core runs 0.30-0.51 historically.

| Period | Avg pair corr | Read |
|--------|---------------|------|
| 2020 H2 | 0.43 | Moderate |
| 2021 | 0.38 | Moderate |
| 2022 | 0.40 | Moderate |
| 2023 | 0.30 | Moderate |
| 2024 H1 | 0.26 | Mild |
| 2024 H2 | 0.35 | Moderate |
| 2025 H1 | 0.23 | Weak |
| 2025 H2 | 0.26 | Mild |
| 2026 YTD | 0.55 | Elevated |

AICD is a looser cluster than [[Security control points]]. The six-name SCP core ([[CrowdStrike]], [[Fortinet]], [[Cloudflare]], [[Palo Alto Networks]], [[Rubrik]], [[Zscaler]]) sits inside AICD; the extra names ([[Okta]], [[SentinelOne]], [[Qualys]], [[Datadog]], [[Rapid7]], [[Tenable]], [[CyberArk]], Gen Digital) dilute the average pairwise correlation by 5 to 15 points across every period tested.

That is the expected result. AICD is catalyst-derived from the Feb 20, 2026 selloff — it captures which names sold off on a single AI-security announcement, which is a broader group than the names that structurally co-move. Running cluster derivation on this basket would trim it toward the SCP composition. AICD stays useful as a disruption-event basket, but it is not a tight structural cluster.

---

## The bear thesis (for traditional security vendors)

1. AI models can now find vulnerabilities that rule-based tools miss — and Opus 4.6 proved it by finding 500+ bugs undetected for decades
2. Claude Code Security is free for open-source, low-cost for Enterprise — puts price pressure on incumbents charging $100K+/year
3. The attack surface is expanding faster than human security teams can scale (~3.5M unfilled cyber jobs globally) — AI is the only answer that scales
4. AI vulnerability scanning will commoditize the detection layer, compressing margins for pure-play AppSec vendors
5. [[OpenAI]] already launched Aardvark (Oct 2025) for autonomous vulnerability hunting — this is a multi-player race, not Anthropic alone
6. If AI scans all the world's code (Anthropic's stated goal), the volume play belongs to AI labs with compute advantage, not legacy security vendors

## The bull case (for traditional security vendors)

1. Claude Code Security is AppSec only — doesn't touch endpoint, network, cloud, identity, or SOC
2. Real-world security requires real-world data (telemetry, threat intel, customer environments) — AI labs don't have this
3. Palo Alto CEO Arora: "LLMs aren't accurate enough to fully replace key segments such as security operations"
4. Enterprise sales cycles, compliance requirements, and existing vendor relationships create switching costs
5. Security vendors are integrating AI into their own products — they can buy/build the same capabilities
6. AppSec is a small slice of the $200B+ cybersecurity TAM — most of the market is untouched

---

## Tracking

Monitor for:
- Next AI security product launches ([[OpenAI]] Aardvark expansion, [[Google]] security AI)
- Claude Code Security moving beyond AppSec into endpoint/cloud/network
- Traditional vendors' AI integration announcements (defensive responses)
- Vulnerability management vendor earnings (Qualys, Rapid7, Tenable) for AI-driven churn signals
- Expansion of free/low-cost AI security tools eroding pricing power

---

## Related

- [[February 2026 AI Disruption Cascade]] — broader software repricing that this basket sits inside
- [[Claude Code Security]] — catalyst (Feb 20 announcement)
- [[Claude Cowork disruption February 2026]] — prior AI-driven software selloff
- [[Anthropic]] — disruptor
- [[Cybersecurity consolidation]] — sector dynamics
- [[CrowdStrike]] — bellwether constituent
- [[Palo Alto Networks]] — bull case spokesperson
- [[Inference economics]] — AI cost structure enables low-cost security tooling
