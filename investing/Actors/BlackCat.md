---
aliases: [ALPHV, ALPHV/BlackCat, Noberus]
tags: [actor, threat-actor, cybercrime, ransomware, raas]
---
#actor #threat-actor #cybercrime #ransomware

**BlackCat** — Ransomware-as-a-Service operation active from late 2021 through early 2024, also tracked as ALPHV and Noberus. Russian-speaking operators are widely assumed (the leak-site infrastructure, affiliate-recruitment posts, and target-set patterns are consistent with prior Russian-language RaaS lineage including DarkSide and BlackMatter). BlackCat's distinguishing technical signature was its written-in-Rust ransomware payload — a deliberate move away from the C/C++ toolchains used by predecessor families to evade signature-based detection and to support cross-platform compilation (Windows, ESXi, Linux). The group's most prominent affiliate operations were the August / September 2023 [[Caesars Entertainment]] and [[MGM Resorts International|MGM Resorts]] intrusions executed in partnership with [[Scattered Spider]] — Scattered Spider supplied initial access via social engineering, BlackCat affiliates handled the encryption phase. BlackCat's operations effectively ended in March 2024 after the FBI seized infrastructure and the operators executed a "$22M exit scam" against an affiliate (the Change Healthcare attacker), failing to pay the affiliate's share of the negotiated ransom. The group's positioning has been partially absorbed by RansomHub, [[DragonForce]], and successor RaaS programs including the in-development shinysp1d3r operated by [[Scattered Lapsus$ Hunters]].

## Quick stats

| Metric | Value |
|--------|-------|
| Active period | Approximately Nov 2021 to Mar 2024 |
| Tracking IDs | ALPHV, BlackCat, Noberus |
| Origin | Russian-language affiliate program; lineage to DarkSide / BlackMatter |
| Technical signature | Rust-written ransomware payload; cross-platform (Win / Linux / ESXi) support |
| Notable affiliated breaches | [[Caesars Entertainment]] (Aug 2023), [[MGM Resorts International|MGM Resorts]] (Sep 2023) — both with [[Scattered Spider]] as access broker; Change Healthcare (Feb 2024, ~$22M ransom and subsequent exit scam) |
| End of operations | Mar 2024 (FBI infrastructure seizure + exit scam) |

## Related

- [[Scattered Spider]] — primary 2023 affiliate access broker
- [[MGM Resorts International|MGM Resorts]] — Sep 2023 victim
- [[Caesars Entertainment]] — Aug 2023 victim
- [[DragonForce]] — successor RaaS positioning
- [[Scattered Lapsus$ Hunters]] — successor alliance with shinysp1d3r RaaS in development

*Stub — created 2026-05-08 during SLSH ingest.*
