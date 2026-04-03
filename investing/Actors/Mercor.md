---
aliases: [Mercor AI]
---
#actor #ai #data #startup #private

Mercor — AI hiring and data labeling platform. Recruits domain experts (medicine, law, literature, coding) to produce training data for frontier AI labs. Valued at $10B. Customers include [[OpenAI]], [[Anthropic]], and [[Meta]].

---

## Quick stats

| Metric | Value |
|--------|-------|
| Founded | 2023 |
| Founders | Brendan Foody, Adarsh Hiremath, Surya Midha (Thiel Fellows, youngest self-made billionaires 2025) |
| Valuation | $10B (Series C, Oct 2025) |
| Total raised | ~$519M |
| Key customers | [[OpenAI]], [[Anthropic]], [[Meta]] |
| Business | Recruits human experts → produces AI training data |
| Domain coverage | Medicine, law, literature, software engineering |

---

## Funding rounds

| Round | Date | Amount | Valuation | Lead |
|-------|------|--------|-----------|------|
| Seed | 2023 | — | — | Soma Capital, Link Ventures, 2.12 Angels |
| Series B | Nov 2024 | $100M | $2B | [[Felicis Ventures]] |
| Series C | Oct 2025 | $350M | $10B | [[Felicis Ventures]] |

Angels include [[Bill Gurley]]. Other investors: [[Benchmark]], [[General Catalyst]], [[Robinhood]] Ventures. 5x valuation jump from Series B to C in eight months.

---

## Mar 31, 2026 — supply chain breach (4 TB exfiltrated)

Mercor confirmed a major data breach originating from a supply chain attack on [[LiteLLM]], an open-source LLM proxy library. The group TeamPCP compromised LiteLLM's [[PyPI]] publishing credentials and injected a three-stage backdoor into versions 1.82.7-1.82.8 — harvesting credentials and establishing persistent system access.

[[Lapsus$]] subsequently claimed the breach and listed the data for live dark web auction.

### Data exfiltrated

| Category | Size |
|----------|------|
| Platform source code | 939 GB |
| User database | 211 GB |
| Video interviews + identity verification (passports) | 3 TB |
| Total | ~4 TB |

### Why this matters

The breach exposes two categories of sensitive data:

1. Identities and personal documents of thousands of domain experts who produce training data — passport scans, video interviews, professional credentials. These are real people who signed up to label data, not public figures.

2. Potentially proprietary training datasets produced for [[OpenAI]], [[Anthropic]], and [[Meta]]. If buyer-specific labeled data was in the exfiltrated storage buckets, this leaks the fine-tuning strategies and data curation approaches of frontier labs.

### Company response

Mercor framed it as a supply chain issue, saying it was "one of thousands of companies" affected by the LiteLLM compromise. A class action investigation is underway (ClaimDepot).

### Supply chain attack vector

The LiteLLM compromise is a textbook [[software supply chain attack]]: popular open-source library → compromised PyPI credentials → malicious package version → downstream consumers auto-update → attacker gains access to production environments. Mercor was the highest-profile victim, but the attack surface was every company that had LiteLLM as a dependency.

---

## Investment implications

The breach highlights a structural vulnerability in the AI training data supply chain. Companies like Mercor, [[Scale AI]], and [[Surge AI]] sit between frontier labs and the human experts who produce training data. They hold both personally identifiable information (PII) and commercially sensitive datasets — a combination that makes them high-value targets.

For [[Anthropic]] and [[OpenAI]], the question is whether Mercor-produced training data was exposed and whether this creates IP or competitive concerns. For investors in the upcoming [[SpaceX IPO 2026|mega-IPO wave]], this is a reminder that AI companies carry cybersecurity tail risk proportional to the value of the data they handle.

---

## Related

- [[OpenAI]] — customer
- [[Anthropic]] — customer
- [[Meta]] — customer
- [[Scale AI]] — competitor (AI data labeling)
- [[LiteLLM]] — attack vector (open-source LLM proxy)
- [[Lapsus$]] — threat actor claiming breach

---

## Sources

- [TechCrunch: Mercor cyberattack via LiteLLM](https://techcrunch.com/2026/03/31/mercor-says-it-was-hit-by-cyberattack-tied-to-compromise-of-open-source-litellm-project/)
- [Fortune: Mercor confirms major breach](https://fortune.com/2026/04/02/mercor-ai-startup-security-incident-10-billion/)
- [CybersecurityNews: Lapsus$ claims 4TB theft](https://cybersecuritynews.com/mercor-ai-data-breach/)
- [The Register: Supply chain attack details](https://www.theregister.com/2026/04/02/mercor_supply_chain_attack/)

*Created 2026-04-03*
