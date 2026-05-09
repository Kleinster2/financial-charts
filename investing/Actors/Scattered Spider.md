---
aliases: [UNC3944, Muddled Libra, Octo Tempest, 0ktapus, Star Fraud, Scatter Swine]
tags: [actor, threat-actor, cybercrime, social-engineering, the-com]
---
#actor #threat-actor #cybercrime

**Scattered Spider** — financially motivated cybercrime collective active since at least May 2022, tracked by [[Mandiant]] as UNC3944, by Palo Alto Unit 42 as Muddled Libra, by Microsoft as Octo Tempest, and by CrowdStrike under its native name. The group is composed primarily of native-English-speaking teens and young adults from the United States, United Kingdom, and Canada, organized loosely through the broader cybercriminal community known as "[[The Com]]" (specifically a subset called Hacker Com). Scattered Spider's tactical signature is exceptionally sophisticated social engineering — voice phishing of IT help desks, SIM swapping, MFA fatigue, and impersonation of employees scraped from LinkedIn — used to bypass identity controls and gain initial access to enterprise environments. The group's most consequential 2023 campaign hit [[MGM Resorts International]] (10-day operational shutdown, ~$100M EBITDA impact) and [[Caesars Entertainment]] ($15M ransom paid, half the original $30M demand). Since August 2025 the group operates primarily as the access-broker leg of the [[Scattered Lapsus$ Hunters]] alliance, supplying initial intrusions to [[ShinyHunters]] for exfiltration and to [[LAPSUS$]] for harassment / public-pressure operations.

## Quick stats

| Metric | Value |
|--------|-------|
| Origin | May 2022 (telecom-sector SIM swapping) |
| Tracking IDs | UNC3944 ([[Mandiant]]); Muddled Libra (Palo Alto Unit 42); Octo Tempest (Microsoft); 0ktapus (Group-IB); Star Fraud; Scatter Swine |
| Affiliation | The Com / Hacker Com (loose collective of English-speaking cybercriminals) |
| Composition | Teens and young adults, US / UK / Canada |
| Tactics | Voice phishing of IT help desks; SIM swapping; MFA fatigue / push bombing; LinkedIn-based employee impersonation; victim-branded credential-harvesting pages; targeting of identity providers (Okta, Azure AD); deployment of partner ransomware ([[BlackCat]] / ALPHV through 2023, [[DragonForce]] in 2025, shinysp1d3r RaaS in development) |
| Notable 2022 victims | Twilio, Cloudflare (failed), Mailchimp, DoorDash — early 0ktapus phishing campaign |
| Notable 2023 victims | [[MGM Resorts International]] (Sep 2023, ~$100M operational impact); [[Caesars Entertainment]] (Aug 2023, $15M ransom paid); Reddit (2022-23); Riot Games |
| Notable 2024-25 victims | UK retail wave: [[Marks & Spencer]] (Apr 2025), Co-op, Harrods; US insurance: [[Aflac]], Erie Insurance, Philadelphia Insurance; aviation sector: WestJet, Hawaiian Airlines, Qantas; [[Snowflake]]-stage support to [[ShinyHunters]] |
| Notable 2026 victims | Via [[Scattered Lapsus$ Hunters]] alliance: [[Salesforce]] customer base, [[Canvas Instructure security incident May 2026|Canvas / Instructure]], EU Commission, [[Rockstar Games]] |
| Encryption | Hybrid — historically deployed [[BlackCat]] then [[DragonForce]] for encryption phase; access-only role within SLSH alliance since Aug 2025 |

## Tradecraft

Scattered Spider's distinguishing capability is human-channel social engineering rather than technical exploitation. The group's typical operation begins by scraping LinkedIn for employees of a target organization (preferred profiles: IT support, helpdesk, sysadmin, identity / IAM staff), then placing voice calls to internal IT help desks impersonating those employees. The vishing operator requests an MFA reset, a password rotation, or enrollment of a new device — using detailed personal information (job title, manager name, recent project) sourced from LinkedIn and OSINT to defeat the help desk's verification challenges. Where multi-factor authentication is enforced, the group either pivots to MFA fatigue (repeated push notifications until the legitimate user accepts) or executes SIM swaps against the target employee's mobile carrier to intercept SMS-based 2FA codes.

Once initial access is obtained, the group pivots aggressively toward the identity provider — typically [[Okta]] or Azure AD — to escalate privileges, create persistent backdoor accounts, and disable security tooling. Scattered Spider has demonstrated a working knowledge of cloud-native identity systems that is unusual for a cybercrime group; the 2023 [[MGM Resorts International|MGM]] intrusion involved Okta superuser permissions used to spawn additional federated identities, then propagation to Azure tenant administration, then deployment of [[BlackCat]] ransomware against ESXi hypervisors hosting hundreds of MGM systems. The technical depth is uneven — the group is skilled at identity-layer attacks and weak at conventional malware development — which is part of why the 2025 alliance with [[ShinyHunters]] (data exfiltration specialists) and [[LAPSUS$]] (extortion / harassment) resolves a capability gap rather than duplicating effort.

A second tactical signature is overt taunting and harassment of victims and incident responders. Scattered Spider operators have used phone calls to executive home numbers, family-member doxxing, and threats of physical violence as part of extortion negotiations. This crosses into the [[LAPSUS$]] operational style and reflects the cultural overlap within The Com between data-extortion groups and the more sociopathic harassment subculture associated with SIM-swapping crews.

## Notable campaigns

### 2022 — 0ktapus / Twilio campaign

Phishing campaign targeting Twilio, Cloudflare, Mailchimp, DoorDash, and ~130 other organizations through a victim-branded credential-harvesting infrastructure dubbed 0ktapus. Cloudflare blunted the attack with hardware security keys; Twilio was breached and disclosed customer-account exposure. The campaign established the group's use of typosquatted Okta-branded login pages as an initial-access mechanic — a pattern that recurred through 2026.

### 2023 — MGM and Caesars

[[Caesars Entertainment]] disclosed the breach in August 2023 and paid approximately $15M of an initial $30M demand to prevent customer-data release. [[MGM Resorts International]] disclosed in September 2023, refused payment, and absorbed roughly $100M in operational impact across a 10-day shutdown of slot machines, hotel keycards, ATMs, and reservation systems. The MGM intrusion reportedly began with a 10-minute phone call to MGM's IT help desk impersonating an employee identified through LinkedIn. Scattered Spider partnered with [[BlackCat]] / ALPHV affiliate operators for the encryption phase. The Caesars-paid / MGM-refused asymmetric outcome shaped subsequent corporate ransom-decision discussions across the gaming and hospitality sectors.

### 2025 — UK retail wave and US insurance pivot

A coordinated April-May 2025 UK retail campaign affected [[Marks & Spencer]] (online operations disrupted for ~6 weeks, retail-platform engineering rebuilt), Co-op (~9M member records exposed), and Harrods (limited internal disruption). M&S subsequently disclosed roughly £300M in operating-profit impact and absorbed material reputation damage in the UK consumer base. The group then pivoted to the US insurance sector mid-2025, hitting [[Aflac]], Erie Insurance, and Philadelphia Insurance before shifting to aviation in mid-to-late 2025 (WestJet, Hawaiian Airlines, Qantas). The sector-rotation pattern (telecom → entertainment → retail → insurance → aviation) reflects the group's adaptive targeting based on which sectors had not yet hardened against the help-desk-vishing playbook.

### 2025-26 — SLSH alliance and the access-broker role

The August 2025 formation of the [[Scattered Lapsus$ Hunters]] Telegram channel formalized a division of labor that had been emerging informally during the 2024 [[Snowflake]] campaign: Scattered Spider supplies initial access via social engineering and identity-layer compromise, [[ShinyHunters]] handles bulk data exfiltration through the victim's own SaaS APIs, and [[LAPSUS$]]-aligned operators handle public-facing extortion and harassment. The arrangement maximizes specialization — the access-broker role is what Scattered Spider does best, and the alliance lets the group monetize access to victims it would otherwise lack the operational discipline to fully exploit.

## Law enforcement actions

| Date | Action |
|------|--------|
| Jun 2024 | [[Tyler Buchanan]] (TylerB), alleged group leader, arrested in Spain attempting to board a flight to Italy; ~$27M in Bitcoin seized |
| Jul 2024 | West Midlands Police, with FBI assistance, arrests a 17-year-old juvenile in connection with [[MGM Resorts International|MGM]] intrusion |
| Apr 2025 | Tyler Buchanan extradited from Spain to the United States; charged with wire fraud, conspiracy, identity theft; alleged personal control of $26M+ stolen from victims |
| Apr 2026 | Peter Stokes ("Bouquet"), 19-year-old Estonian / US dual citizen, apprehended at Helsinki Airport attempting to board a flight to Japan; US prosecutors request extradition to Chicago on wire fraud / conspiracy / computer intrusion charges across at least four Scattered Spider operations |
| Apr 2026 | Tyler Buchanan pleads guilty to major crypto theft and conspiracy charges in US federal court |

The arrests have visibly slowed but not stopped the group's tempo. The decentralized nature of Hacker Com / The Com — peer recruitment through Discord, Telegram, and gaming communities — means new operators continue to take up the brand and tradecraft as members are arrested or roll over. The April 2026 simultaneous Buchanan plea / Stokes arrest sequence coincided with a temporary slowdown in SLSH-attributed activity that observers read as a tactical pause rather than dissolution.

## Related

- [[ShinyHunters]] — exfiltration partner in the [[Scattered Lapsus$ Hunters]] alliance
- [[LAPSUS$]] — extortion / harassment partner in the SLSH alliance
- [[Scattered Lapsus$ Hunters]] — the August 2025 federated cybercrime brand
- [[The Com]] — the loose English-speaking cybercrime community Scattered Spider operates within
- [[MGM Resorts International]] — Sep 2023 victim
- [[Caesars Entertainment]] — Aug 2023 victim ($15M ransom)
- [[Marks & Spencer]] — Apr 2025 victim, ~£300M operating impact
- [[Aflac]] — 2025 US insurance victim
- [[Snowflake]] — supplied initial access to [[ShinyHunters]] for the 2024 campaign
- [[Salesforce]] — 2025 vishing campaign target
- [[Canvas Instructure security incident May 2026]] — 2026 victim via SLSH alliance
- [[Tyler Buchanan]] — alleged group leader, extradited Apr 2025
- [[Mandiant]] — incident-response firm tracking the group as UNC3944
- [[Okta]] — common identity-provider pivot target
- [[BlackCat]] — 2023 ransomware partner (ALPHV)
- [[DragonForce]] — 2025 ransomware partner (UK retail wave)

### Cross-vault

- [Technologies: SaaS API abuse](obsidian://open?vault=technologies&file=SaaS%20API%20abuse) — the broader threat pattern Scattered Spider participates in via the SLSH access-broker role
