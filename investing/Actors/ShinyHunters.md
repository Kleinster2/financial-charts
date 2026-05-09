---
aliases: [Shiny Hunters, UNC6040, Bling Libra]
tags: [actor, threat-actor, cybercrime, ransomware, extortion, the-com]
---
#actor #threat-actor #cybercrime

**ShinyHunters** — financially motivated cybercrime group active since 2020, classified by [[Mandiant]] as UNC6040 in some campaigns and tracked by Palo Alto Unit 42 as Bling Libra. Known for large-scale data exfiltration and extortion across cloud SaaS platforms — notably the 2024 [[Snowflake]] credential-theft campaign affecting up to 165 customer organizations (including [[Live Nation Entertainment|Ticketmaster]] and Santander Bank), the 2025 [[Salesforce]] vishing campaign that impersonated IT support to install malicious Data Loader, the March 2026 [[European Commission]] data leak (350 GB claimed), the April 2026 [[Rockstar Games]] breach via the [[Anodot]] / [[Snowflake]] supply chain (~80M records claimed), and the May 2026 [[Canvas Instructure security incident May 2026|Canvas / Instructure breach]] claiming 3.65 TB across 8,809 educational institutions. ShinyHunters' tactical signature is data theft alone (no encryption) — leverage is purely informational, with no decryption pathway available even if a ransom is paid. The group has historically used voice phishing (vishing), victim-branded credential-harvesting pages, and stolen SSO/MFA tokens to reach SaaS APIs. Since August 2025, ShinyHunters operates primarily as the data-exfiltration pillar of the [[Scattered Lapsus$ Hunters]] alliance (Trinity of Chaos), in which [[Scattered Spider]] supplies initial access and [[LAPSUS$]]-aligned operators handle public extortion and harassment. The alliance also began marketing a Ransomware-as-a-Service offering called shinysp1d3r in November 2025, signaling an expansion from the data-theft-only model into hybrid encrypt-and-extort operations.

## Quick stats

| Metric | Value |
|--------|-------|
| Origin | 2020 (forum-based data-theft activity) |
| Tracking IDs | UNC6040 ([[Mandiant]], Salesforce campaign); Bling Libra (Palo Alto Unit 42) |
| Affiliation | [[The Com]] adjacent; co-pillar of [[Scattered Lapsus$ Hunters]] (Aug 2025) |
| Tactics | Data exfiltration without encryption; vishing; credential theft via supply-chain compromise; abuse of legitimate cloud APIs; victim-branded credential-harvesting pages; public Telegram-channel extortion announcements |
| Key operator alias | "shinycorp" (a.k.a. @sp1d3rhunters, @sloke48, @shinyc0rp) — principal orchestrator of breach claims and SLSH coordination |
| Notable 2020 victims | Tokopedia, Nitro PDF, Pixlr |
| Notable 2024 victims | [[Snowflake]] customers (165 orgs incl. [[Live Nation Entertainment|Ticketmaster]], Santander Bank); supply-chain via [[EPAM Systems]] |
| Notable 2025 victims | [[Salesforce]] customers (luxury goods, airlines, insurance, e-commerce) |
| Notable 2025 (separate) | [[University of Pennsylvania]] direct breach — $1M ransom refused, files released |
| Notable 2026 victims | March: [[European Commission]] (350 GB / 42 internal clients / 29 EU entities); April: [[Rockstar Games]] (~80M records via [[Anodot]] / [[Snowflake]]); May: [[Instructure]] / [[Canvas LMS]] (275M records / 3.65 TB across 8,809 schools) |
| Encryption | None historically — pure data theft + extortion. shinysp1d3r RaaS announced Nov 2025 (in development) signals expansion into hybrid encrypt-and-extort |

## Alliance: Scattered Lapsus$ Hunters

On August 8, 2025, ShinyHunters formalized a federated cybercrime alliance with [[Scattered Spider]] and [[LAPSUS$]]-aligned operators under the [[Scattered Lapsus$ Hunters]] (SLSH) brand — also referenced in industry threat intelligence as the "Trinity of Chaos" (Resecurity, Trustwave). The alliance operationalized a division of labor that had been emerging informally since the 2024 [[Snowflake]] campaign:

| Function | Pillar | Role |
|----------|--------|------|
| Initial access | [[Scattered Spider]] | Vishing of IT help desks; SIM swapping; MFA fatigue; identity-provider compromise; insider recruitment |
| Data exfiltration | ShinyHunters | SaaS-API enumeration; bulk data-export endpoint abuse; supply-chain pivots through integrators |
| Extortion / harassment | [[LAPSUS$]]-aligned | Public Telegram-channel extortion announcements; victim taunting; harassment of executives and incident responders |
| Brand and PR | "shinycorp" / @sp1d3rhunters | Press contact; takedown responses; data-leak-site curation |

Within the SLSH structure, ShinyHunters retains a distinct brand identity for breach claims (the May 2026 Canvas / Instructure ransom letters are signed ShinyHunters, the March 2026 European Commission claim was made under the ShinyHunters banner) but operates inside an alliance pipeline rather than as a standalone group. The arrangement maximizes specialization — SaaS-API exfiltration is what ShinyHunters does best, and the alliance lets the group monetize access to victims it would otherwise lack the social-engineering depth to compromise directly.

The November 19, 2025 BleepingComputer reporting on the shinysp1d3r RaaS — an alliance-developed Ransomware-as-a-Service offering still in active development as of May 2026 — signals an expansion from the data-theft-only model that has defined ShinyHunters for five years. If shinysp1d3r ships and recruits affiliates, the alliance becomes a multi-tier criminal enterprise on the LockBit / [[BlackCat]] organizational template, broadening the threat surface ShinyHunters represents.

The federated brand has proven structurally hard to disrupt. October 2025 saw the SLSH extortion portal go intermittently inaccessible amid reports of additional alliance-affiliated arrests, but the breach tempo continued through Q1 2026 (EU Commission, Rockstar) and into Q2 (Canvas / Instructure). The April 2026 [[Tyler Buchanan]] guilty plea and Peter Stokes ("Bouquet") arrest at Helsinki Airport on April 10 marked a temporary slowdown in SLSH-attributed activity that observers read as a tactical pause rather than dissolution.

## Notable 2026 incidents

### March 2026 — European Commission, 350 GB

The European Commission detected a breach of its cloud system on March 24, 2026; ShinyHunters claimed responsibility three days later and published an initial 90 GB archive, claiming exfiltration of more than 350 GB total — including email backups, databases, contractual documents, full SSO user directory, DKIM signing keys, AWS configuration snapshots, NextCloud / Athena data, and internal admin URLs. CERT-EU subsequently confirmed PII exposure for 42 internal clients and at least 29 EU entities and attributed the breach to ShinyHunters. The breach is the largest publicly-claimed European-government cyber incident attributed to The Com / SLSH and raises potential GDPR enforcement implications across the entire EU institutional perimeter.

### April 2026 — Rockstar Games, ~80M records

ShinyHunters breached cloud-linked systems of [[Rockstar Games]] in April 2026 via a third-party service (Anodot → Snowflake supply chain), claiming theft of approximately 80M records. The group issued a ransom deadline of April 14 and, after expiry, leaked portions of the data online — including internal analytics and business metrics for GTA Online and Red Dead Online, plus claims of GTA 6 development data. Rockstar confirmed the breach but characterized the impact as limited and non-material. The breach demonstrated that the [[Snowflake]] supply-chain attack surface remained exposed two years after the original 2024 campaign — Rockstar's data-warehouse integration through [[Anodot]] was the same architectural pattern that had been exploited in 2024.

### May 2026 — Canvas / Instructure, 3.65 TB / 275M records

The May 2026 [[Canvas Instructure security incident May 2026|Canvas / Instructure breach]] is the most consequential publicly-claimed ShinyHunters operation to date, affecting an estimated 8,809 educational institutions globally including the entire higher-ed customer base of [[Canvas LMS]]. The attack vector was abuse of Canvas Free-For-Teacher account-tier credentials to access DAP queries, provisioning reports, and user APIs — a textbook execution of the SaaS-API-abuse playbook. Initial access reportedly involved vishing-style social engineering of partner integrators, consistent with [[Scattered Spider]] tradecraft within the SLSH division of labor. Ransom deadline May 12, 2026. Ransom decision flows through [[KKR]] as Instructure's controlling shareholder.

## Related

- [[Scattered Lapsus$ Hunters]] — August 2025 federated cybercrime alliance ShinyHunters co-founded
- [[Scattered Spider]] — initial-access pillar of the SLSH alliance
- [[LAPSUS$]] — extortion / harassment pillar of the SLSH alliance
- [[The Com]] — adjacent English-speaking cybercrime community
- [[Canvas Instructure security incident May 2026]] — major 2026 victim
- [[Instructure]] — May 2026 victim
- [[Canvas LMS]] — affected platform
- [[European Commission]] — March 2026 victim, 350 GB claimed
- [[Rockstar Games]] — April 2026 victim, ~80M records claimed via [[Anodot]] / [[Snowflake]] supply chain
- [[Snowflake]] — 2024 campaign target and recurring supply-chain attack surface
- [[EPAM Systems]] — 2024 supply-chain intermediary
- [[Anodot]] — 2026 supply-chain intermediary in the Rockstar campaign
- [[Salesforce]] — 2025 campaign target
- [[University of Pennsylvania]] — late 2025 direct victim ($1M ransom refused)
- [[Mandiant]] — incident-response firm tracking ShinyHunters as UNC6040
- [[Tyler Buchanan]] — Scattered Spider operator (alliance partner) extradited Apr 2025
- [[KKR]] — Instructure controlling shareholder; ransom decision flows through PE owner
- [[BlackCat]] — predecessor RaaS template the shinysp1d3r model is positioning against

### Cross-vault

- [Technologies: SaaS API abuse](obsidian://open?vault=technologies&file=SaaS%20API%20abuse) — multi-year playbook documented as a generalized threat pattern
