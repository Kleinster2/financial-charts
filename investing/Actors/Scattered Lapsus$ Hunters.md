---
aliases: [SLSH, SLH, Trinity of Chaos, Scattered Lapsus Hunters, Scattered LAPSUS Hunters]
tags: [actor, threat-actor, cybercrime, alliance, the-com]
---
#actor #threat-actor #cybercrime

**Scattered Lapsus$ Hunters** — federated cybercrime alliance announced on Telegram on August 8, 2025, combining the brands and overlapping memberships of three otherwise-distinct threat-actor identities: [[Scattered Spider]] (initial access via social engineering), [[ShinyHunters]] (data exfiltration through SaaS APIs), and [[LAPSUS$]] (public extortion and harassment theatrics). Tracked by Trustwave SpiderLabs as a federated cybercriminal brand and by Resecurity as the "Trinity of Chaos." Within Palo Alto Unit 42's Libra taxonomy the alliance combines Muddled Libra (Scattered Spider) and Bling Libra (ShinyHunters) with LAPSUS$-aligned operators. SLSH operationalized a division of labor that had been emerging informally during the 2024 [[Snowflake]] and 2025 [[Salesforce]] campaigns and made it the explicit organizing principle for the next wave of high-impact breaches — including [[Canvas Instructure security incident May 2026|Canvas / Instructure]] (May 2026, 8,809 institutions claimed), the [[European Commission]] data leak (March 2026, 350 GB claimed), and [[Rockstar Games]] (April 2026, ~80M records claimed via [[Anodot]] / [[Snowflake]] supply chain). The alliance also began marketing a Ransomware-as-a-Service offering called shinysp1d3r in November 2025, signaling an expansion from data-theft extortion into encrypt-and-extort affiliate operations.

## Quick stats

| Metric | Value |
|--------|-------|
| Announced | August 8, 2025 (Telegram channel launch) |
| Branding | Scattered Lapsus$ Hunters (operators' own name); Trinity of Chaos (Resecurity / Trustwave / industry framing) |
| Composition | [[Scattered Spider]] + [[ShinyHunters]] + [[LAPSUS$]]-aligned operators, all rooted in [[The Com]] |
| Tactics | Division of labor: Scattered Spider supplies initial access via vishing / SIM swap / MFA fatigue; ShinyHunters runs bulk data exfiltration via SaaS APIs; LAPSUS$-aligned operators run public-facing extortion / harassment / Telegram-channel theatrics |
| Communications infrastructure | At least 16 Telegram channels created since August 8, 2025; data-leak portal (intermittent availability after Oct 2025) |
| Ransomware brand | shinysp1d3r RaaS — announced Nov 19, 2025, in active development per BleepingComputer / MOXFIVE / Palo Alto Unit 42 reporting |
| Key operator alias | "shinycorp" (a.k.a. @sp1d3rhunters, @sloke48, @shinyc0rp) — principal orchestrator of breach claims, takedown responses, and brand coordination |
| Status (May 2026) | Telegram channels and breach claims active; extortion portal accessibility intermittent after Oct 2025 reported arrests; recent breaches (EU Commission, Rockstar, Canvas) attributed to alliance-affiliated operators |

## Why the alliance matters

Three structural points distinguish SLSH from a conventional threat-actor merger.

First, the division of labor solves a capability gap that none of the three constituent groups individually filled well. [[Scattered Spider]] excels at human-channel social engineering and identity-layer compromise but historically struggled with bulk exfiltration discipline. [[ShinyHunters]] excels at SaaS-API enumeration and data-warehouse extraction but lacks Scattered Spider's social-engineering depth. [[LAPSUS$]]-aligned operators bring the public-extortion theatrics and harassment infrastructure inherited from the original 2022 LAPSUS$ Telegram-channel model. The federated structure allows each pillar to specialize rather than bottlenecking each campaign on the weakest leg.

Second, the federated brand is structurally hard to disrupt through arrests. Where conventional cybercrime groups maintain a tight membership boundary, SLSH operates as a brand layer over loosely-coupled operators whose primary affiliation is to [[The Com]] cybercriminal community rather than to any single named group. When operators are arrested — as Tyler Buchanan was in 2024-25, and as multiple SLSH-affiliated operators reportedly were in October 2025 — the brand persists, the channels persist, and the playbook persists. The August 2023 LAPSUS$ convictions did not end LAPSUS$-branded activity; the April 2025 Buchanan extradition did not end Scattered Spider activity; the 2026 Canvas / Instructure breach proceeded after a year of arrests against alliance operators. The federated brand is a durable threat-actor configuration even under sustained law-enforcement pressure.

Third, the alliance signals a shift in cybercrime market structure toward platform-style coordination. SLSH's shinysp1d3r RaaS announcement — a ransomware-as-a-service offering layered onto the existing exfiltration playbook — indicates the alliance is moving from a campaign-based model toward an affiliate platform that other threat actors can rent. If shinysp1d3r ships and recruits affiliates, the alliance becomes a multi-tier criminal enterprise on the LockBit / [[BlackCat]] organizational template, which historically has scaled threat-actor operational tempo by an order of magnitude relative to single-group campaigns.

## Division of labor

| Function | Pillar | Role |
|----------|--------|------|
| Initial access | [[Scattered Spider]] | Vishing of IT help desks; SIM swapping; MFA fatigue; identity-provider compromise (Okta, Azure AD); insider recruitment |
| Privilege escalation and lateral movement | [[Scattered Spider]] | Cloud-native identity-layer pivots; persistent backdoor account creation; security-tool disablement |
| Data exfiltration | [[ShinyHunters]] | SaaS-API enumeration; bulk data-export endpoint abuse; supply-chain pivots through integrators ([[EPAM Systems]], [[Anodot]], [[Sitel]]) |
| Extortion communication | [[LAPSUS$]]-aligned | Public Telegram-channel extortion announcements; victim taunting; harassment of executives and incident responders |
| Brand and PR | "shinycorp" / @sp1d3rhunters | Press contact; takedown responses; data-leak-site curation; Trinity of Chaos / SLSH coordination across channels |
| Encryption (emerging) | shinysp1d3r RaaS | In development per Nov 2025 BleepingComputer reporting; expansion from data-theft-only model into hybrid encrypt-and-extort |

The division is not absolute — operators move between roles, and individual breaches may be claimed under different brand banners depending on the public-pressure strategy of the moment — but the role specialization is the alliance's defining innovation relative to predecessor cybercrime structures.

## Notable campaigns under SLSH branding

### 2024 — Snowflake (precursor)

The 2024 [[Snowflake]] credential-theft campaign — affecting up to 165 customer organizations including [[Ticketmaster]] and Santander Bank — predates the formal SLSH announcement but established the operational template. ShinyHunters handled data exfiltration; Scattered Spider supplied initial access via social engineering of Snowflake customer accounts; LAPSUS$-aligned operators handled some of the public extortion. Supply-chain pivot was via [[EPAM Systems]] developer machines storing Jira credentials in plaintext.

### 2025 — Salesforce vishing campaign

The 2025 [[Salesforce]] campaign tracked as UNC6040 (Mandiant) involved voice phishing of Salesforce customer organizations to install a malicious Data Loader application, leading to data exfiltration from customer Salesforce instances. Affected sectors included luxury goods, airlines, insurance, and e-commerce. The campaign was the immediate operational precursor to the August 2025 SLSH formalization — the same operators executing the same playbook, with the brand consolidation following the proven model.

### Mar 2026 — European Commission, 350 GB

The European Commission detected a breach of its cloud system on March 24, 2026; SLSH-affiliated operators (claiming the [[ShinyHunters]] brand) claimed responsibility three days later and published an initial 90 GB archive, claiming exfiltration of more than 350 GB total including email backups, databases, contractual documents, full SSO user directory, DKIM signing keys, AWS configuration snapshots, NextCloud / Athena data, and internal admin URLs. CERT-EU subsequently confirmed PII exposure for 42 internal clients and at least 29 EU entities and attributed the breach to ShinyHunters. The breach is the largest publicly-claimed European-government cyber incident attributed to The Com / SLSH and raises potential GDPR enforcement implications across the entire EU institutional perimeter.

### Apr 2026 — Rockstar Games, ~80M records

In April 2026, SLSH-affiliated operators claiming the [[ShinyHunters]] brand breached cloud-linked systems of [[Rockstar Games]] via a third-party service (Anodot → Snowflake supply chain), claiming theft of approximately 80M records. The group issued a ransom deadline of April 14 and, after expiry, leaked portions of the data online, including internal analytics and business metrics for GTA Online and Red Dead Online, plus claims of GTA 6 development data. Rockstar confirmed the breach but characterized the impact as limited and non-material. The breach demonstrated that the [[Snowflake]] supply-chain attack surface remained exposed two years after the original 2024 campaign — Rockstar's data-warehouse integration through Anodot was the same architectural pattern that had been exploited in 2024.

### May 2026 — Canvas / Instructure, 3.65 TB / 275M records

The May 2026 [[Canvas Instructure security incident May 2026|Canvas / Instructure breach]] is the most consequential publicly-claimed SLSH operation to date, affecting an estimated 8,809 educational institutions globally including the entire higher-ed customer base of [[Canvas LMS]]. The attack vector was abuse of [[Canvas LMS]] Free-For-Teacher account-tier credentials to access DAP queries, provisioning reports, and user APIs — a textbook execution of the [[ShinyHunters]] SaaS-API-abuse playbook. Initial access reportedly involved vishing-style social engineering against IT help desks of partner integrators, consistent with [[Scattered Spider]] tradecraft. The breach landed during finals week, defaced Canvas login pages globally on May 7, and prompted a full Canvas outage on May 7-8. Ransom deadline May 12, 2026. Ransom decision flows through [[KKR]] as Instructure's controlling shareholder. Affected institutions include Brown, Harvard, Penn State, Penn, Columbia, Georgetown, Michigan, Rutgers, the UC system, U Chicago, Baylor, Maryland, UNC Chapel Hill, Oklahoma, Iowa, Iowa State, Texas Tech, Virginia Tech, Duke, and Illinois — effectively the full Canvas higher-ed customer base.

## shinysp1d3r RaaS

On November 19, 2025, BleepingComputer reported that SLSH was actively developing a Ransomware-as-a-Service offering branded shinysp1d3r. Subsequent reporting from MOXFIVE and Palo Alto Unit 42 ("Bling Libra and the Evolving Extortion Economy") expanded on the offering's positioning. As of May 2026, shinysp1d3r remains in development rather than active use; no public encryption-based victim claims have been confirmed under the brand. The strategic significance of the RaaS pivot is that it shifts SLSH from a small number of high-profile alliance-led campaigns toward a multi-tier affiliate-driven enterprise — affiliate operators rent the encryption capability and bring their own initial access, reducing the alliance's per-campaign operational burden and scaling the volume of victims by an order of magnitude. If the RaaS launches and recruits affiliates, the threat surface that SLSH represents broadens substantially.

## Status and law-enforcement pressure

By late October 2025, the SLSH extortion portal became intermittently inaccessible, and multiple social-media reports — some reportedly from operators within The Com adjacent communities — claimed additional SLSH-affiliated arrests. No confirmed law-enforcement statement has verified that all members are detained or that operations have ceased. The alliance's branded campaigns continued through Q1 2026 (EU Commission, Rockstar, Canvas), suggesting that even if specific operators were arrested, the brand and tradecraft transferred to successor operators within The Com fast enough to maintain campaign tempo. The combined April 2026 [[Tyler Buchanan]] guilty plea and Peter Stokes ("Bouquet") arrest at Helsinki Airport on April 10 marked a temporary slowdown in SLSH-attributed activity that observers read as a tactical pause rather than dissolution.

## Related

- [[ShinyHunters]] — exfiltration pillar of the alliance
- [[Scattered Spider]] — initial-access pillar of the alliance
- [[LAPSUS$]] — extortion / harassment pillar of the alliance
- [[The Com]] — the loose English-speaking cybercrime community all three groups are rooted in
- [[Snowflake]] — 2024 campaign that prefigured the SLSH division of labor
- [[Salesforce]] — 2025 campaign that immediately preceded the August 2025 formal alliance announcement
- [[European Commission]] — March 2026 victim, 350 GB claimed
- [[Rockstar Games]] — April 2026 victim, ~80M records claimed
- [[Canvas Instructure security incident May 2026]] — May 2026 victim, 8,809 institutions claimed
- [[Canvas LMS]] — affected platform in the May 2026 campaign
- [[Instructure]] — operator of the breached platform
- [[KKR]] — Instructure controlling shareholder; ransom decision flows through PE owner
- [[EPAM Systems]] — supply-chain intermediary in 2024 Snowflake campaign
- [[Anodot]] — supply-chain intermediary in 2026 Rockstar campaign
- [[Sitel]] — supply-chain intermediary in 2022 Okta campaign (LAPSUS$-era)
- [[Mandiant]] — incident-response firm tracking ShinyHunters as UNC6040 and adjacent operators
- [[Tyler Buchanan]] — Scattered Spider operator extradited from Spain Apr 2025
- [[BlackCat]] — predecessor RaaS template the shinysp1d3r model is positioning against

### Cross-vault

- [Technologies: SaaS API abuse](obsidian://open?vault=technologies&file=SaaS%20API%20abuse) — the structural threat pattern SLSH operationalized at industrial scale
