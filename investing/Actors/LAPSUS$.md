---
aliases: [Lapsus$, Lapsus, DEV-0537, Strawberry Tempest]
tags: [actor, threat-actor, cybercrime, extortion, the-com]
---
#actor #threat-actor #cybercrime

**LAPSUS$** — extortion-focused cybercrime group that emerged December 10, 2021 with a breach of the Brazilian Ministry of Health and rapidly escalated through the first quarter of 2022 into one of the most consequential threat-actor brands of the modern era. Tracked by Microsoft as DEV-0537 (later renamed Strawberry Tempest under Microsoft's revised threat-actor taxonomy). The group's defining innovation was the abandonment of conventional ransomware in favor of pure data-theft extortion announced through a public Telegram channel — a model later inherited by [[ShinyHunters]] and the broader [[Scattered Lapsus$ Hunters]] alliance. LAPSUS$'s 2022 spree compromised [[NVIDIA]], Samsung, Vodafone, Ubisoft, Microsoft, [[Okta]], Mercado Libre, T-Mobile, and Globant — including the leak of NVIDIA driver source code and code-signing certificates and a screenshot dump from Microsoft's internal Azure DevOps server. Members included a 16-year-old British teen (Arion Kurtaj) operating from his mother's home in Oxford, and a Brazilian member arrested in São Paulo. After the original UK / Brazil arrest waves of 2022 and the August 2023 London convictions, the LAPSUS$ brand continued to surface in connection with high-profile breaches — notably the September 2023 [[MGM Resorts International|MGM]] / [[Caesars Entertainment|Caesars]] intrusions in partnership with [[Scattered Spider]] — and re-emerged in August 2025 as one of the three pillars of the [[Scattered Lapsus$ Hunters]] federated cybercrime alliance.

## Quick stats

| Metric | Value |
|--------|-------|
| Origin | December 10, 2021 (Brazilian Ministry of Health breach) |
| Tracking IDs | DEV-0537 / Strawberry Tempest (Microsoft) |
| Affiliation | Loose connection to [[The Com]] from inception; co-founder of [[Scattered Lapsus$ Hunters]] (Aug 2025) |
| Composition | Predominantly teenagers based in the UK and Brazil; founding leadership included a 16-year-old in Oxford (Arion Kurtaj) and a 17-year-old of unidentified gender |
| Tactics | SIM swapping; insider recruitment ("we want to give your employees / insiders a way to make extra money"); MFA fatigue; voice phishing of help desks; data theft only — no encryption deployed; public Telegram-channel extortion announcements; theatrical victim taunting |
| Notable 2021-22 victims | Brazilian Ministry of Health (Dec 2021); Mercado Libre / Mercado Pago (Mar 2022); [[NVIDIA]] (Feb 2022, ~1 TB exfiltrated incl. driver source + code-signing certs); Samsung (Mar 2022, 190 GB Galaxy device source code); Vodafone (Mar 2022); Ubisoft (Mar 2022); [[Microsoft]] Azure DevOps (Mar 2022); [[Okta]] (Jan 2022, via [[Sitel]] support engineer); Globant (Mar 2022, 70 GB customer code repos); T-Mobile (Mar 2022) |
| Notable 2023-25 activity | [[MGM Resorts International|MGM]] / [[Caesars Entertainment|Caesars]] intrusions (Sep 2023, in partnership with [[Scattered Spider]]); brand-name appearances in The Com adjacent campaigns; co-founder of [[Scattered Lapsus$ Hunters]] (Aug 2025) |
| Encryption | None — pure data-theft extortion; established the model later adopted by [[ShinyHunters]] |
| Convictions | Aug 2023 London: Arion Kurtaj (founding member, 18) and a co-defendant aged 17 convicted of conspiracy to commit fraud, conspiracy to make / supply articles for use in fraud, blackmail, and computer misuse offenses; Kurtaj ordered to remain indefinitely in a secure psychiatric facility |

## Tradecraft

LAPSUS$ pioneered the "extortion-only, no-encryption" model that has since become a multi-billion-dollar threat-actor specialty. The group's standard chain ran: (1) recruit insiders through public posts on the LAPSUS$ Telegram channel offering payment for credentials / VPN access / source-code theft, (2) supplement insider recruitment with SIM swapping against employees identified through OSINT to intercept SMS-based MFA, (3) compromise an upstream supplier or support-services provider rather than the target directly (the [[Okta]] breach was via a [[Sitel]] customer-service contractor; the [[Microsoft]] breach reused stolen credentials), (4) exfiltrate large volumes of source code, internal documents, and credentials, (5) post taunting Telegram-channel announcements with samples of stolen data, and (6) demand ransom under threat of full release.

The group dispensed with virtually all the operational discipline that conventional cybercrime groups practice. Rather than maintaining anonymity, members boasted about breaches in real time on Telegram, took live polls of their followers ("which company should we leak next?"), and conducted operations from home networks reachable by law enforcement. The 2022 UK arrest of Kurtaj and the Brazilian arrest of an alleged member followed in months, not years, because the operational security was nearly absent. The combination of high-impact breaches and amateur OPSEC made LAPSUS$ the canonical case study for "kid hackers" — except that the kid hackers compromised NVIDIA, Microsoft, Okta, and Samsung in approximately 90 days.

The Telegram-channel-as-extortion-platform innovation has proven structurally durable. Where conventional ransomware groups operated through Tor-hosted leak sites with controlled access, LAPSUS$'s public Telegram model demonstrated that extortion could be conducted directly in the open, with the channel serving as a hybrid of brand marketing, victim-pressure mechanism, and recruiting funnel. [[ShinyHunters]] later adopted the same architecture, and the August 2025 [[Scattered Lapsus$ Hunters]] alliance is operationally a federation of public Telegram channels rather than a private cybercrime forum.

## Notable campaigns

### Dec 2021 — Brazilian Ministry of Health

The group's debut. LAPSUS$ defaced the Brazilian Ministry of Health website, claimed to have stolen ~50 TB of data including COVID-19 vaccination records, and demanded ransom. The Brazilian government refused; some data was subsequently released. The breach occurred during the high-stakes 2021-22 window of national vaccination rollout under the Bolsonaro administration and exposed the operational immaturity of Brazilian federal cybersecurity. The early Brazil-centered activity is part of why the group's membership skewed Brazilian / UK in the early phase.

### Jan 2022 — Okta via Sitel

LAPSUS$ obtained access to Okta's internal systems through a compromised laptop belonging to a customer-support engineer at [[Sitel]] — an Okta third-party vendor providing support-tier services. The group accessed the Sitel engineer's Okta tenant credentials and could have viewed approximately 366 Okta customer environments. Okta's January 21, 2022 detection lagged its January 25, 2022 public confirmation by four days; LAPSUS$ posted screenshots in March 2022 to demonstrate access, prompting the public crisis. The incident became a textbook case for supply-chain risk in the identity-provider category and shaped subsequent SOC2 Type 2 audit scope.

### Feb 2022 — NVIDIA

LAPSUS$ exfiltrated approximately 1 TB of [[NVIDIA]] data, including hashed credentials for ~71,000 employees, proprietary GPU driver source code, and code-signing certificates. The code-signing certificates posed a separate downstream threat: malware signed with stolen NVIDIA certificates could pass Windows authentication checks. NVIDIA disclosed the breach quickly, declined to pay, and absorbed the operational cost of certificate revocation and credential rotation. The leak was made public on the LAPSUS$ Telegram channel.

### Mar 2022 — Microsoft Azure DevOps

The group posted a 9 GB partial archive of source code from Microsoft's internal Azure DevOps server, claimed to contain code for Bing, Bing Maps, and Cortana. Microsoft confirmed a "single account had been compromised, granting limited access" through a March 22, 2022 blog post that introduced the DEV-0537 designation. The breach demonstrated that even Microsoft's internal source-code repositories were reachable via the standard credential-theft / MFA-bypass playbook, and shaped subsequent identity-hardening across the Microsoft tenant graph.

### Mar 2022 — Samsung, Vodafone, Ubisoft, Globant

A four-week sequence of source-code exfiltration breaches: 190 GB of Galaxy device source code from Samsung, internal source from Vodafone, internal Ubisoft systems with limited customer-data exposure, and 70 GB of Globant customer source repositories. The cumulative impact across Q1 2022 was the disclosure or destruction of source code for products serving billions of users. The Globant leak in particular contained code repositories for Globant's enterprise clients (DHL, Stanley Black & Decker, Arcserve, Citi, Facebook), making it a multi-tenant exposure event.

### Sep 2023 — MGM and Caesars (alongside Scattered Spider)

LAPSUS$-aligned operators (whether the original UK / Brazil group or successor brand-users is contested in attribution reporting) participated in the Sep 2023 [[MGM Resorts International|MGM]] / [[Caesars Entertainment|Caesars]] intrusions led by [[Scattered Spider]]. The cross-pollination between the two groups, both rooted in The Com, is part of why the August 2025 [[Scattered Lapsus$ Hunters]] alliance was operationally feasible — the personnel pool and tradecraft overlap had been compounding for two years.

### Aug 2025 — SLSH co-founding role

LAPSUS$-branded operators became one of three pillars of the [[Scattered Lapsus$ Hunters]] alliance announced on Telegram on August 8, 2025. Within SLSH, LAPSUS$-aligned members handle public-facing extortion theatrics, victim harassment, and the "Trinity of Chaos" branding push — roles that match the original LAPSUS$ Telegram-channel-as-extortion-platform DNA.

## Law enforcement actions

| Date | Action |
|------|--------|
| Mar 2022 | City of London Police arrests seven individuals connected to LAPSUS$, ages 16-21; one minor in Oxford (later identified as Arion Kurtaj) believed to be a leader |
| Oct 2022 | Brazilian Federal Police arrests a 19-year-old in São Paulo on charges connected to LAPSUS$ activity |
| Apr 2023 | Kurtaj's UK trial begins after he is arrested again on a separate charge while on bail |
| Aug 2023 | London jury convicts Kurtaj and a 17-year-old co-defendant of conspiracy to commit fraud and computer-misuse offenses; Kurtaj ordered to remain indefinitely in a secure psychiatric facility on the basis of an autism diagnosis and the court's assessment that he intended to return to cybercrime |
| Oct 2025 | Multiple unconfirmed reports of additional [[Scattered Lapsus$ Hunters]] arrests claiming connection to LAPSUS$-branded activity; SLSH extortion portal goes inaccessible later that month, reportedly tied to operator arrests |

## Status

LAPSUS$ as a discrete operational entity effectively ended with the August 2023 convictions. The brand persists as an identity used by successor operators within The Com and as a co-equal banner within the [[Scattered Lapsus$ Hunters]] alliance. Whether 2024-26 LAPSUS$-branded activity reflects the original membership pool, post-arrest successor cells, or pure brand appropriation by adjacent The Com operators is contested in threat-intelligence reporting; the practical effect for victims is the same. The brand's durability reflects the value of the established public-Telegram extortion model — successor operators inherit the audience, the credibility, and the harassment infrastructure rather than rebuilding from scratch.

## Related

- [[ShinyHunters]] — co-pillar of the [[Scattered Lapsus$ Hunters]] alliance; inherited LAPSUS$'s extortion-only / Telegram-channel model
- [[Scattered Spider]] — co-pillar of the SLSH alliance; cross-pollinated with LAPSUS$ since 2023
- [[Scattered Lapsus$ Hunters]] — August 2025 federated cybercrime brand co-founded by LAPSUS$-aligned operators
- [[The Com]] — broader English-speaking cybercrime community LAPSUS$ overlaps with
- [[NVIDIA]] — Feb 2022 victim
- [[Microsoft]] — Mar 2022 victim (Azure DevOps source-code exposure)
- [[Okta]] — Jan 2022 victim (via [[Sitel]] supply-chain compromise)
- [[Sitel]] — Okta third-party vendor compromised as the entry vector
- [[Mandiant]] — incident-response firm involved in multiple LAPSUS$ engagements
- [[MGM Resorts International]] — Sep 2023 victim alongside [[Scattered Spider]]
- [[Caesars Entertainment]] — Sep 2023 victim alongside Scattered Spider

### Cross-vault

- [Technologies: SaaS API abuse](obsidian://open?vault=technologies&file=SaaS%20API%20abuse) — the structural threat pattern LAPSUS$'s 2022 campaign helped establish
- [Brazil: Bolsonaro government cybersecurity posture](obsidian://open?vault=Brazil%20News%20%26%20Analysis&file=Concepts%2FBolsonaro%20government%20cybersecurity%20posture) — context for the December 2021 Ministry of Health breach (stub-target if not yet present)
