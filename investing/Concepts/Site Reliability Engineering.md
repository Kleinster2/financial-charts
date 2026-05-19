---
aliases:
  - SRE
  - Site Reliability Engineering
tags:
  - concept
  - operations
  - google
  - software
---
#concept #operations #google #software

# Site Reliability Engineering

Software-engineering discipline applied to operations. Founded at [[Google]] in 2003 by [[Benjamin Treynor Sloss]], who coined the term. Treats reliability — uptime, latency, performance, capacity, observability — as a software-engineering problem rather than a traditional operations function. The SRE team writes its own software, owns the production stack, and uses error budgets to balance feature velocity against reliability targets.

---

## Why SRE matters for this vault

SRE is the operational architecture that makes hyperscale clouds run. [[Google Cloud]] uses it as a differentiator versus [[AWS]] and Microsoft Azure; the practice has spread to every large software shop. The relevance to AI infrastructure is concrete: the [[Google-Blackstone TPU cloud venture 2026|Google-Blackstone TPU cloud JV]] (May 2026) hired [[Benjamin Treynor Sloss]] as CEO, which means the SRE operating model goes with him to the new external TPU-cloud venture.

---

## Core ideas

| Idea | Description |
|---|---|
| Error budgets | Reliability target (e.g. 99.9% uptime) translates into an explicit budget of allowable failures; the budget gates how aggressively the team ships new features |
| SLOs / SLIs | Service-level objectives and indicators replace softer "reliability" goals |
| Toil reduction | Manual, repetitive operations work is automated away; SRE engineers spend at most ~50% on operations and the rest on engineering |
| Postmortems | Blameless review after incidents, with structural fixes rather than process fixes |
| Production ownership | SRE owns production, not just monitors it |

---

## Books

- *Site Reliability Engineering: How Google Runs Production Systems* (2016)
- *The Site Reliability Workbook: Practical Ways to Implement SRE* (2018)
- *Building Secure & Reliable Systems* (2020) — co-authored with the security team

The two SRE books became canonical industry references. Sloss wrote the introduction to both.

---

## Related

- [[Benjamin Treynor Sloss]] — founder of the discipline at Google
- [[Google]] — origin
- [[Google Cloud]] — where SRE is a public differentiator
- [[Google-Blackstone TPU cloud venture 2026]] — extending the SRE model to an external TPU-cloud venture
