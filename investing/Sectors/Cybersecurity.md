---
aliases: [Cyber security, Cyber, InfoSec, Security software]
---
#sector #tech #cybersecurity

# Cybersecurity

Overview of the cybersecurity industry.

---

## Market structure

| Segment | Key players | Trend |
|---------|-------------|-------|
| **Network security** | [[Palo Alto Networks]], [[Fortinet]], Cisco | Platform consolidation |
| **Endpoint/XDR** | [[CrowdStrike]], SentinelOne, Microsoft | Cloud-native winning |
| **Identity** | Okta, CyberArk, Microsoft | Zero trust adoption |
| **Cloud security** | Palo Alto (Prisma), Wiz, Orca | Fastest growth |
| **SIEM/SOAR** | Splunk (Cisco), Palo Alto, Microsoft | AI automation |
| **Email security** | Proofpoint, Mimecast, Microsoft | Commoditizing |

---

## Key players

| Company | Market cap | Focus | Model |
|---------|------------|-------|-------|
| [[Palo Alto Networks]] | ~$120B | Enterprise platform | Platformization |
| [[CrowdStrike]] | ~$90B | Endpoint, cloud | Cloud-native |
| [[Fortinet]] | ~$75B | Mid-market, firewall | Hardware + subscription |
| Zscaler | ~$30B | Zero trust, SASE | Cloud proxy |
| Okta | ~$15B | Identity | IAM platform |
| SentinelOne | ~$8B | Endpoint AI | Autonomous |

---

## Industry dynamics

### Consolidation trend

**"Platformization"** — enterprises reducing vendor count:

| Approach | Leader |
|----------|--------|
| Network → cloud → SOC | Palo Alto |
| Endpoint → cloud → identity | CrowdStrike |
| Identity → governance | Okta |

Winners: Platform vendors
Losers: Point solutions

### Microsoft factor

Microsoft Defender becoming viable:
- Free/bundled with E5
- Good enough for many enterprises
- Compresses pure-play valuations

---

## AI: the dual disruption

AI is hitting cybersecurity from both sides simultaneously — amplifying attackers *and* threatening to displace incumbent vendors.

### AI as threat amplifier (bullish for spend)

AI collapses the time-to-breach and the skill threshold. A single operator with an LLM can now execute what previously required a team of specialists.

| Event | Date | Detail |
|-------|------|--------|
| **[[Amazon]] / 600 firewalls** | Feb 2026 | Russian-speaking hackers (possibly one person) used commercial GenAI tools to breach 600+ firewalls across 55 countries in weeks. Exploited weak credentials/single-factor auth at scale. Staging for ransomware. |
| **[[AWS]] 8-minute breach** | Nov 2025 (disclosed Feb 2026) | Attackers found creds in public S3 bucket, used LLM-generated code (Serbian, AI-generated exception handling patterns) to go from initial access to full exfiltration across Secrets Manager, EC2, CloudWatch, S3 — in ~8 minutes. Sysdig research. |
| **Skill floor collapse** | Ongoing | ~3.5M unfilled cyber jobs globally. AI lets unskilled attackers punch above their weight — reconnaissance, exploit generation, lateral movement all accelerated. |

Implication: attack surface growing faster than human defenders can scale → structural demand driver for security spend regardless of macro.

### AI as vendor disruptor (bearish for incumbents)

AI labs entering security directly, threatening to commoditize the detection layer.

| Event | Date | Detail |
|-------|------|--------|
| **[[Claude Code Security]]** | Feb 20, 2026 | [[Anthropic]]'s AI vulnerability scanner. Opus 4.6 found 500+ bugs undetected for decades. Reasons about code contextually vs. pattern matching. Free for open-source. |
| **[[Aardvark]]** | Oct 2025 | [[OpenAI]]'s autonomous vulnerability hunter. |
| **Sector selloff** | Feb 20, 2026 | OKTA -9.2%, NET -8.1%, CRWD -8.0%, S -7.5% despite broader market rising. |

See [[AI cybersecurity disruption basket]] for the full selloff breakdown and bear/bull cases.

**Net read:** AI is both the disease and the cure. Spending *must* rise (bullish TAM), but it may flow to AI-native tools rather than legacy vendors (bearish for incumbents without AI integration).

---

## Growth drivers

| Driver | Impact |
|--------|--------|
| **AI-powered attacks** | Force multiplier — single operator = team-scale campaigns (see above) |
| **Cloud migration** | New attack surface |
| **Remote work** | Zero trust adoption |
| **Regulatory compliance** | Mandatory spend |
| **AI-native defense tools** | Commoditization risk for detection layer |
| **Skill shortage** | 3.5M unfilled jobs → automation tailwind |

---

## Business model

| Metric | Healthy range |
|--------|---------------|
| ARR growth | 20-30%+ |
| Net retention | 115-130% |
| Gross margin | 70-80% |
| FCF margin | 20-35% |
| Rule of 40 | 40%+ |

Subscription/recurring = high visibility.

---

## Investment positioning

| Company | Bull case | Bear case |
|---------|-----------|-----------|
| [[Palo Alto Networks]] | Platform leader, AI | Execution risk, free trials |
| [[CrowdStrike]] | Cloud-native, endpoint leader | Valuation, July 2024 outage |
| [[Fortinet]] | Mid-market, margins | Enterprise weakness |
| Zscaler | Zero trust leader | Competition, growth slowing |

---

## Risks

| Risk | Impact |
|------|--------|
| **Microsoft bundling** | Pricing pressure |
| **Economic slowdown** | IT budget cuts |
| **Breach at vendor** | Reputation (see CrowdStrike outage) |
| **AI labs entering security** | [[Claude Code Security]], [[Aardvark]] — commoditize detection layer |
| **AI-accelerated attacks** | Faster breach cycles force faster vendor response or lose relevance |

---

## Related

- [[Palo Alto Networks]] — platform leader
- [[CrowdStrike]] — endpoint leader
- [[Fortinet]] — mid-market leader
- [[Microsoft]] — bundling threat
- [[Long defense AI]] — government cyber spend
- [[AI cybersecurity disruption basket]] — tracks vendor disruption from AI labs
- [[AI workflow disruption basket]] — sibling basket (SaaS disruption)
- [[Claude Code Security]] — Anthropic's AI vulnerability scanner (Feb 2026 catalyst)
- [[Aardvark]] — OpenAI's autonomous vulnerability hunter
- [[Cybersecurity consolidation]] — sector M&A dynamics
- [[Zero trust]] — architectural trend
- [[Identity and Access Management]] — subsector

## Sources

- Bloomberg, "Hackers Used AI to Breach 600 Firewalls in Weeks, Amazon Says" (Feb 20, 2026)
- Sysdig, "Attackers Used AI to Breach an AWS Environment in 8 Minutes" (Feb 2026)

*Updated 2026-02-21*
