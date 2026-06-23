---
aliases: [Cyber security, Cyber, InfoSec, Security software]
---
#sector #tech #cybersecurity

# Cybersecurity

Overview of the cybersecurity industry.

---

## [[Market structure]]

| [[Segment]] | Key players | Trend |
|---------|-------------|-------|
| **Network security** | [[Palo Alto Networks]], [[Fortinet]], [[Cisco]] | Platform consolidation |
| [[SASE]] / secure access | [[Zscaler]], [[Palo Alto Networks]], [[Fortinet]], [[Cloudflare]] | Zero trust and SD-WAN converge |
| Endpoint/XDR | [[CrowdStrike]], [[SentinelOne]], Microsoft | Cloud-native winning |
| Identity | [[Okta]], [[CyberArk]], Microsoft | Zero trust adoption |
| Cloud security | Palo Alto (Prisma), [[Wiz]], Orca | Fastest growth |
| SIEM/SOAR | Splunk ([[Cisco]]), Palo Alto, Microsoft | AI automation |
| Email security | Proofpoint, Mimecast, Microsoft | Commoditizing |

---

## Key players

| Company | Market cap | Focus | Model |
|---------|------------|-------|-------|
| [[Palo Alto Networks]] | ~$120B | Enterprise platform | Platformization |
| [[CrowdStrike]] | ~$90B | Endpoint, cloud | Cloud-native |
| [[Fortinet]] | ~$75B | Mid-market, firewall | Hardware + subscription |
| [[Zscaler]] | ~$30B | Zero trust, [[SASE]] | Cloud proxy |
| [[Okta]] | ~$15B | Identity | IAM platform |
| [[SentinelOne]] | ~$8B | Endpoint AI | Autonomous |

---

## Industry dynamics

### Consolidation trend

"Platformization" — enterprises reducing vendor count:

| Approach | Leader |
|----------|--------|
| Network → cloud → SOC | Palo Alto |
| Endpoint → cloud → identity | [[CrowdStrike]] |
| Identity → governance | [[Okta]] |

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
| [[Amazon]] / 600 firewalls | Feb 2026 | Russian-speaking hackers (possibly one person) used commercial GenAI tools to breach 600+ firewalls across 55 countries in weeks. Exploited weak credentials/single-factor auth at scale. Staging for ransomware. |
| [[AWS]] 8-minute breach | Nov 2025 (disclosed Feb 2026) | Attackers found creds in public S3 bucket, used LLM-generated code (Serbian, AI-generated exception handling patterns) to go from initial access to full exfiltration across Secrets Manager, EC2, CloudWatch, S3 — in ~8 minutes. Sysdig research. |
| Skill floor collapse | Ongoing | ~3.5M unfilled cyber jobs globally. AI lets unskilled attackers punch above their weight — reconnaissance, exploit generation, lateral movement all accelerated. |

Implication: attack surface growing faster than human defenders can scale → structural demand driver for security spend regardless of macro.

### AI as vendor disruptor (bearish for incumbents)

AI labs entering security directly, threatening to commoditize the detection layer.

| Event | Date | Detail |
|-------|------|--------|
| [[Claude Code Security]] | Feb 20, 2026 | [[Anthropic]]'s AI vulnerability scanner. Opus 4.6 found 500+ bugs undetected for decades. Reasons about code contextually vs. pattern matching. Free for open-source. |
| [[Aardvark]] | Oct 2025 | [[OpenAI]]'s autonomous vulnerability hunter. |
| Sector selloff #1 | Feb 20, 2026 | OKTA -9.2%, NET -8.1%, CRWD -8.0%, S -7.5% despite broader market rising. |
| [[Claude Mythos]] leak | Mar 27, 2026 | [[Anthropic]]'s next-gen Capybara-tier model leaked via misconfigured CMS. Internal docs describe "step change" in cybersecurity capability — model can rapidly identify and exploit software vulnerabilities. |
| Sector selloff #2 | Mar 27, 2026 | CRWD -7%, PANW -6%, ZS -4.5%, OKTA -3%, S -3%, FTNT -3%. Market logic: if AI finds vulnerabilities at scale, incumbents face both a more dangerous threat landscape and disruption by AI-native alternatives. |

See [[AI cybersecurity disruption basket]] for the full selloff breakdown and bear/bull cases.

The Feb and Mar selloffs reveal a pattern: each step-function in AI capability — first a vulnerability scanner ([[Claude Code Security]]), now a model that can autonomously find *and exploit* vulnerabilities ([[Claude Mythos]]) — triggers a fresh repricing of incumbent cyber stocks. The question is whether the sector's structural demand tailwind (AI amplifies attackers → more spend needed) can offset the disruption risk (AI labs building the tools themselves).

Net read: AI is both the disease and the cure. Spending *must* rise (bullish TAM), but it may flow to AI-native tools rather than legacy vendors (bearish for incumbents without AI integration).

### Apr 2026 - AI labs move from demos into live cyber workflows

OpenAI's [[GPT]]-5.4-Cyber briefings to U.S. agencies and Five Eyes partners show the labs are moving from "AI can find bugs" messaging into government-facing deployment. The important shift is not just capability. It is distribution. Vetted rollouts to security vendors, researchers, and state users mean the frontier labs are trying to own pieces of actual defensive workflow, not just sell generic model access.

The same week, *The Register* reported a self-propagating CanisterWorm-style npm campaign hitting packages tied to Namastex Labs, an agentic AI company. The malware stole npm, PyPI, cloud, CI/CD, [[Kubernetes]], Docker, SSH, browser-wallet, and LLM-platform secrets, then tried to republish malicious packages from compromised developer environments. That is the live version of the thesis: AI raises both the value of cyber automation and the vulnerability of software and agent toolchains.

The net read is unchanged but sharper. AI is still both the threat amplifier and the vendor disruptor, but the battleground is shifting from generic scanning into production security workflows and developer infrastructure.

*Sources: [[Reuters]], "OpenAI briefs US agencies, Five Eyes on new cybersecurity product, Axios reports" (Apr 22, 2026); The Register, "Another npm supply chain worm is tearing through dev environments" (Apr 22, 2026).*

### Apr 29-30 2026 — npm worms hit SAP and Google's Gemini CLI

Two same-week incidents hardened the developer-toolchain attack-surface thesis.

On Apr 29, attackers published malicious versions of four official [[SAP]] [[npm]] packages — `mbt@1.2.48`, `@cap-js/db-service@2.10.1`, `@cap-js/postgres@2.2.2`, and `@cap-js/sqlite@2.2.2` — between roughly 09:55 and 12:14 UTC. The malicious `preinstall` hook fetched the [[Bun]] JavaScript runtime and ran an obfuscated 11MB payload that harvested local developer credentials, [[GitHub]]/[[npm]] tokens, [[GitHub Actions]] secrets, and cloud credentials from [[AWS]], [[Microsoft Azure|Azure]], [[Google Cloud|GCP]], and [[Kubernetes]], then exfiltrated the data via newly created public [[GitHub]] repositories tagged "A Mini Shai-Hulud has Appeared." Researchers attributed the campaign to a threat actor labeled TeamPCP. The same campaign poisoned `intercom-client` (7.0.4 / 7.0.5) and the [[PyPI]] package `lightning` (2.6.2 / 2.6.3). [[SAP]] told *The Register* that a security note is available for customers and partners. Source: [The Register, "Ongoing supply chain attacks worm into SAP npm packages"](https://www.theregister.com/2026/04/30/supply_chain_attacks_sap_npm_packages/) (Apr 30, 2026).

The same day (Apr 30), [[Google]] disclosed and patched a CVSS 10.0 remote-code-execution flaw in [[Gemini CLI]] and the `run-gemini-cli` GitHub Action. In headless mode, [[Gemini CLI]] auto-trusted any workspace folders, so an attacker who controlled `.gemini/` config files in a checked-out repo could execute code before any sandbox initialized. Mitigations shipped in [[Gemini CLI]] 0.39.1 and 0.40.0-preview.3. The fix tightened the previous auto-trust default and broke workflows that relied on the old behavior, including some `--yolo` mode automations. Reported by Elad Meged (Novee Security) and Dan Lisichkin (Pillar Security). Source: [The Register, "Google fixes CVSS 10.0 vulnerability in Gemini CLI"](https://www.theregister.com/2026/04/30/googles_fix_for_critical_gemini) (Apr 30, 2026).

The pattern across [[Axios]] (Apr 4), the Apr 22 [[npm]] worm, the Apr 29 SAP packages, and the Apr 30 [[Gemini CLI]] CVE is consistent: developer-side and CI/CD toolchains are now the preferred soft entry point for credential theft and supply-chain pivots, and frontier-AI developer tooling sits squarely inside that surface. See [[Agentic AI security]] and [[AI cybersecurity disruption basket]] for the cross-vendor read.

### May 26 2026 — Glassworm developer botnet disruption

[[CrowdStrike]], [[Google]], and the Shadowserver Foundation disrupted the [[Glassworm botnet takedown May 2026]] botnet at 14:00 UTC on May 26, 2026 by hitting all four of its C2 channels at once. The campaign had used trojanized VS Code/OpenVSX extensions, compromised npm and Python packages, and more than 300 poisoned [[GitHub]] repositories to compromise developers across [[Windows]], macOS, and [[Linux]].

The Glassworm detail matters because it turns "developer toolchain risk" from a set of isolated package incidents into a multi-ecosystem operating model. The same attacker workflow can start in an IDE extension, harvest repository/package/cloud credentials, poison repositories or packages, and then use resilient public infrastructure such as [[Solana]], BitTorrent DHT, and Google Calendar as command resolution. For sector positioning, this supports the [[Software supply chain attacks]] / [[Security control points]] read: spend should keep migrating toward endpoint telemetry, developer identity, repository/package governance, secret detection, and runtime response.

*Sources: CrowdStrike, "Inside CrowdStrike's Takedown of a Developer-Targeting Botnet" (May 2026); The Register, "CrowdStrike, Google shatter Glassworm botnet" (May 27 2026); TechCrunch, "CrowdStrike and Google take down botnet used by hackers to target open source software developers" (May 27 2026).*

### May 27 2026 — shadow AI becomes an incident category

Okta's 2026 "AI Agents at Work" survey, covered by *The Register*, gives the identity/security side of the same AI adoption problem. 90% of executives said they were confident in visibility into AI tools, while 52% of employees used unapproved AI tools and 24% did so regularly. 58% of executives reported an AI-related security incident or close call in the prior year.

The sensitive-data detail is the market signal. Among employees using unapproved tools, Okta reported that 54% shared internal messages/emails, 45% HR-related information, 39% confidential company documents, more than 20% login credentials/passwords, and 28% banking/payment information. This makes [[Shadow AI]] a direct cybersecurity budget driver: AI discovery, browser/app data-loss prevention, identity governance for non-human actors, and agent access controls all move from optional policy projects into necessary control surfaces.

*Sources: Okta, "AI Agents at Work 2026: Securing the agentic enterprise" (May 27 2026); The Register, "Bosses blinded by confidence about shadow AI use by workers" (May 27 2026).*

### Jun 22 2026 — Five Eyes "months, not years" joint warning

The Five Eyes cyber agencies — US [[CISA]] and NSA, the UK's [[UK National Cyber Security Centre|NCSC]], Australia's ACSC, Canada's Cyber Centre, and New Zealand's NCSC — issued a rare joint advisory warning that frontier AI models will transform offensive cyber capability "in months, not years," exceeding current industry expectations. It is the most authoritative confirmation yet of the threat-amplifier thesis above — the policy world catching up to what [[Claude Mythos]] demonstrated in lab conditions.

- Agentic AI can run rapid automated attacks — chaining exploits, adapting to defenses in real time, scaling beyond any human team.
- Defensive guidance: limit unnecessary system access, accelerate patching, strengthen identity controls. Critically, the agencies state "breaches will occur," reframing the core problem as resilience, not prevention.
- Builds on May 2026 Five Eyes guidance cataloguing 23+ risk categories for autonomous AI systems, and on the Apr 2026 [[GPT]]-5.4-Cyber government briefings (above).

Investment read: unambiguously bullish for the structural-spend thesis (a five-government endorsement that the attack surface is about to step-change), and it sharpens the mix shift the note already tracks — "breaches will occur" pushes budget toward resilience/recovery and identity control-points ([[Rubrik]], [[CrowdStrike]], [[Okta]]/[[CyberArk]], the [[Security control points]] cluster) over pure prevention. It does not resolve the vendor-disruption risk: the same agentic capability that drives spend can be packaged by AI labs (the [[Claude Mythos]] / [[Aardvark]] commoditization vector).

*Sources: Five Eyes joint advisory (CISA / NSA / NCSC-UK / ACSC / Canadian Cyber Centre / NCSC-NZ), Jun 22 2026; [[Financial Times]], "AI-powered threats may succeed 'within months', Five Eyes warn" (Jun 22 2026); CyberScoop, Computer Weekly (Jun 22-23 2026).*

## Security control-point cluster

A separate cross-sectional read emerged on Apr 13, 2026. `scripts/cluster_movers.py` flagged a strong up-cluster in [[Fortinet]], [[Zscaler]], [[Palo Alto Networks]], [[CrowdStrike]], [[Cloudflare]], and [[Rubrik]], with [[Akamai]] screening as a looser adjacent member. Persistence checks across 60-day, 90-day, and 120-day windows suggested the durable core was not broad cybersecurity but a narrower set of names that still own traffic policy, telemetry, secure access, or recovery bottlenecks.

That distinction matters because it separates the vendors most exposed to AI commoditizing point tools from the vendors that still sit on mandatory control surfaces. See [[Security control points]].

## Correlation structure

Cybersecurity no longer trades as one clean factor. The tighter market-implied cluster is the control-point layer: policy enforcement, secure access, endpoint telemetry, and recovery. Across the durability checks, the core group's average pairwise excess-return correlation held around 0.55 over 60 days, 0.49 over 90 days, and 0.47 over 120 days. That is why names like [[CrowdStrike]], [[Fortinet]], [[Palo Alto Networks]], [[Zscaler]], [[Rubrik]], and [[Cloudflare]] can move together more tightly than the broader sector, while more specialized or edge-adjacent names trade with looser attachment.

---

## Growth drivers

| Driver | Impact |
|--------|--------|
| AI-powered attacks | Force multiplier — single operator = team-scale campaigns (see above) |
| Cloud migration | New attack surface |
| Remote work | [[SASE]] / zero trust adoption |
| Regulatory compliance | Mandatory spend |
| AI-native defense tools | Commoditization risk for detection layer |
| Skill shortage | 3.5M unfilled jobs → automation tailwind |

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
| [[Zscaler]] | Zero trust leader | Competition, growth slowing |

---

## Risks

| Risk | Impact |
|------|--------|
| Microsoft bundling | Pricing pressure |
| Economic slowdown | IT budget cuts |
| Breach at vendor | Reputation (see [[CrowdStrike]] outage) |
| AI labs entering security | [[Claude Code Security]], [[Aardvark]], [[Claude Mythos]] — commoditize detection layer; Mythos escalates from scanning to autonomous exploitation |
| AI-accelerated attacks | Faster breach cycles force faster vendor response or lose relevance |

---

## Policy & regulation

2026-04-03: [[Donald Trump|Trump]] administration proposes slashing $707M from [[CISA]] budget. Former CISA official warns the cut would weaken federal cyber risk management capabilities across critical infrastructure sectors. Source: The Register (Apr 3, 2026).

---

## Journal

| Date | Event | Impact |
|------|-------|--------|
| 2026-05-26 | [[Zscaler]] Q3 FY2026 beat revenue/EPS but guided Q4 revenue $875-878M, slightly below Reuters/LSEG consensus, and cut FY2026 FCF-margin guidance to 22.8-23.3% from 26.5-27.0% | Confirms SASE demand is still growing, but the sector read shifted toward platform competition, capex burden, and forward-growth deceleration. [[Palo Alto Networks]] platformization remains the key competitive read-through. |

---

## Related

- [[Palo Alto Networks]] — platform leader
- [[CrowdStrike]] — endpoint leader
- [[Fortinet]] — mid-market leader
- [[Microsoft]] — bundling threat
- [[Long defense AI]] — government cyber spend
- [[AI cybersecurity disruption basket]] — tracks vendor disruption from AI labs
- [[February 2026 AI Disruption Cascade]] — the broader [[SaaS]] disruption event the cyber cohort sat inside
- [[Claude Code Security]] — Anthropic's AI vulnerability scanner (Feb 2026 catalyst)
- [[Aardvark]] — OpenAI's autonomous vulnerability hunter
- [[Claude Mythos]] — Anthropic's Capybara-tier model, leaked Mar 2026 (cybersecurity selloff catalyst)
- [[OpenAI Spud]] — OpenAI's next-gen model, competing announcement same week
- [[Cybersecurity consolidation]] — sector M&A dynamics
- [[SASE]] — secure-access architecture and platform-budget battleground
- [[Security control points]] — structural cluster inside the sector
- [[Software supply chain attacks]] — developer/package/repository attack-surface concept
- [[Shadow AI]] — unapproved AI-tool and AI-agent governance risk
- [[Zero Trust|Zero trust]] — architectural trend
- [[Identity and Access Management]] — subsector

## Sources

- [[Bloomberg]], "Hackers Used AI to Breach 600 Firewalls in Weeks, Amazon Says" (Feb 20, 2026)
- Sysdig, "Attackers Used AI to Breach an AWS Environment in 8 Minutes" (Feb 2026)

- Fortune, 2026-03-26: "Anthropic 'Mythos' AI model representing 'step change' in power revealed in data leak"
- Investing.com, 2026-03-27: "Cybersecurity stocks plunge as [[Claude]] Mythos leak sparks AI fear"
- The Register, 2026-04-30: "Ongoing supply chain attacks worm into SAP npm packages" (Mini Shai-Hulud)
- The Register, 2026-04-30: "Google fixes CVSS 10.0 vulnerability in Gemini CLI"
- CrowdStrike, 2026-05: "Inside CrowdStrike's Takedown of a Developer-Targeting Botnet"
- The Register, 2026-05-27: "CrowdStrike, Google shatter Glassworm botnet"
- Okta, 2026-05-27: "AI Agents at Work 2026: Securing the agentic enterprise"
- The Register, 2026-05-27: "Bosses blinded by confidence about shadow AI use by workers"

*Updated 2026-04-05 · Updated 2026-05-01 (SAP npm Mini Shai-Hulud + Gemini CLI CVSS 10.0) · Updated 2026-05-29 (Glassworm developer botnet takedown; shadow AI survey)*
