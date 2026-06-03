---
aliases: [Glasswing]
tags: [product, ai, cybersecurity]
parent_actor: "Anthropic"
---

Project Glasswing — Anthropic's controlled deployment program for [[Claude Mythos|Claude Mythos Preview]], giving selected companies and critical-software defenders early access to the unreleased model for defensive cybersecurity work.

---

## Synopsis

Project Glasswing is Anthropic's answer to the problem of releasing a frontier model that is simultaneously useful for defense and dangerous for offense. Instead of shipping [[Claude Mythos]] broadly, Anthropic put it behind a curated access program for large technology companies and operators of critical software infrastructure, arguing that defenders need a head start before Mythos-class cyber capability becomes widely available. The important signal is not just the partner list, though it is formidable, but the institutional reaction: within days, U.S. and UK financial authorities were treating the model as an operational-resilience issue for major banks and market infrastructure.

---

## Quick stats

| Detail | Value |
|--------|-------|
| Parent | [[Anthropic]] |
| Launch date | 2026-04-07 |
| Model | [[Claude Mythos|Claude Mythos Preview]] |
| Access model | Controlled early access |
| Primary use case | Defensive cybersecurity |
| Partner count | Roughly 50 partners after first month |
| Additional cohort | ~40 critical-software organizations at launch; expanded through Linux Foundation / OpenSSF and other open-source maintainers |
| Support package | Up to $100M usage credits + $4M open-source security donations |
| One-month partner findings | More than 10,000 high- or critical-severity vulnerabilities reported by partners |
| Open-source scan | 1,000+ projects; 23,019 estimated vulnerabilities, including 6,202 high/critical |
| Disclosure progress | 530 high/critical bugs disclosed to maintainers; 75 patched and 65 public advisories by May 22 2026 |

---

## Launch structure

Anthropic's launch page named [[Amazon]], [[Microsoft]], [[Apple]], [[Broadcom]], [[Cisco]], [[CrowdStrike]], [[Google]], [[JPMorgan Chase]], Linux Foundation, [[NVIDIA]], and [[Palo Alto Networks]] among the program's launch partners, while extending access to roughly 40 additional organizations responsible for critical software infrastructure.

Anthropic said the model had already found thousands of major vulnerabilities across operating systems, web browsers, and other widely used software. The company framed Glasswing as a controlled defensive rollout rather than a public launch.

---

## One-month update (May 22, 2026)

Anthropic's first Glasswing update shows the program has become a coordinated-disclosure operating problem, not just a model-access program. After one month, Anthropic said roughly 50 partners had used Mythos Preview and collectively found more than ten thousand high- or critical-severity vulnerabilities. Several partners said their bug-finding rate increased by more than 10x; Cloudflare reported 2,000 bugs across critical-path systems, including 400 high- or critical-severity findings, with a false-positive rate the team considered better than human testers.

The open-source scan is the strongest measurable dataset:

| Metric | Value |
|--------|-------|
| Open-source projects scanned | 1,000+ |
| Total Mythos-estimated vulnerabilities | 23,019 |
| Estimated high/critical vulnerabilities | 6,202 |
| High/critical findings assessed | 1,752 |
| Valid true positives after assessment | 90.6% (1,587) |
| Confirmed high/critical after assessment | 62.4% (1,094) |
| High/critical bugs disclosed to maintainers | 530 |
| Patched | 75 |
| Public advisories | 65 |

The key line is the bottleneck shift. Mythos Preview makes discovery cheap enough that the scarce resource becomes human triage, maintainer review, coordinated disclosure, patch design, and deployment. Anthropic says even its relatively slow disclosure pace is adding to an already overloaded security ecosystem, and some maintainers have asked it to slow down.

*Source: [Anthropic, Project Glasswing initial update](https://www.anthropic.com/research/glasswing-initial-update), May 22 2026.*

---

## Why it matters

Glasswing is the first clear example in the vault of a frontier foundation model being distributed like a dual-use cyber capability rather than a normal software product. Anthropic is effectively saying that the right comparison for Mythos is not a better chatbot or coding model, but a capability that can change the offense-defense balance in software security.

That matters for three reasons. First, it deepens Anthropic's relationship with regulated enterprises and governments, because the value of the model rises when the user sits on critical infrastructure. Second, it raises the threshold for full commercialization, because once access is mediated by regulators, banks, and cyber agencies, release timing becomes a policy question as much as a product question. Third, it reveals a new security-market constraint: vulnerability discovery is no longer the bottleneck; verified disclosure and patching are.

---

## Regulatory reaction

Within two days of the launch, Reuters reported that U.S. officials had briefed major bank CEOs on the model's cyber-risk potential. By April 12, the [[Bank of England]], [[Financial Conduct Authority]], and the [[UK National Cyber Security Centre]] were reported to be coordinating on whether Mythos-class models could expose vulnerabilities in critical financial IT systems.

That sequence is the real story. Glasswing pushed Anthropic's cyber work into the financial-stability perimeter.

---

## Industry color (Patel, Apr 23, 2026)

[[Dylan Patel]] on [[Invest Like the Best]] (Apr 23, 2026) added two pieces of context on Glasswing's gating dynamic that complement the regulatory reaction:

- **Patel's running nickname.** "Anthropic's project ... it's not called earwig, but I troll Anthropic people by calling it earwig. Glasswig, Anthropic earwig." Patel and others in the industry routinely refer to the program by joking variants — a small detail that marks how culturally distinctive the selective-deployment posture is in an industry where broad release was previously the norm
- Selective deployment as the new pattern — "Models will have less broad and less broad deployment. I know I know [[OpenAI]] and [[Anthropic|Enthropic]] and all these people are like, 'we want to have great AI for everyone.' AI is very [&nbsp;__&nbsp;] expensive ... you don't want people to distill your models. So you don't release them broadly. You release them to a fewer and fewer set of customers." Patel reads Glasswing as a leading indicator rather than a one-off — the gating logic generalizes to capacity scarcity, model-distillation defense, and capability-control concerns
- Begging-for-access anecdote — Patel and [[Leopold Aschenbrenner|Leopold]] "on our knees in front of an Anthropic co-founder begging him for access to Mythos and then pretending it doesn't exist cuz we knew it existed." Even high-profile industry figures with deep [[SemiAnalysis]] customer relationships were initially excluded — illustrating how narrow the early Glasswing perimeter actually was

The Patel framing connects Glasswing to the broader [[Inference economics#Permanent-underclass thesis (Patel, Apr 2026)|permanent-underclass thesis]]: capacity rationing favors customers with existing enterprise relationships and large capital commitments. The pattern, once established, propagates to other frontier capabilities; a competitor without Glasswing-style access faces a cyber-defense gap that scales with how widely Mythos-class models are eventually deployed.

*Source: [[Dylan Patel]] on [[Invest Like the Best]] (Apr 23, 2026)*

---

## Related

- [[Anthropic]] — parent company
- [[Claude Mythos]] — model distributed through Glasswing
- [[AI cybersecurity disruption basket]] — equity basket tracking the security-vendor disruption side
- [[AI producer-evaluator asymmetry]] — framework for the discovery/triage/patching bottleneck
- [[Bank of England]] — UK regulator drawn into the response
- [[Financial Conduct Authority]] — UK conduct regulator involved in the talks
- [[UK National Cyber Security Centre]] — UK cyber agency involved in the talks
- [[Cybersecurity]] — sector most directly affected
