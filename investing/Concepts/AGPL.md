---
aliases: [GNU Affero General Public License, Affero GPL, AGPLv3]
tags: [concept, opensource, licensing, software]
---
#concept #opensource #licensing #software

**AGPL** (GNU Affero General Public License) — strong copyleft open-source license maintained by the [[Free Software Foundation]]. The defining feature versus the standard GPL is that the AGPL extends copyleft obligations to network-deployed software: if a service operator runs AGPL-licensed code as part of a network service (for example a SaaS application), they are obligated to make the source code of any modifications available to users of that service. This closes the "SaaS loophole" in GPL.

## Synthesis

The AGPL matters in the SaaS era because it is the only widely-recognized open-source license that meaningfully constrains the commercial cloud-service model. A company that builds a SaaS product on top of GPL code is generally not required to share source modifications because the GPL's copyleft trigger is distribution and SaaS users do not "receive" a copy of the software. The AGPL was designed to fix this — under AGPL, running a modified version of the software as a network-accessible service triggers the source-disclosure obligation, regardless of whether anyone downloads the code.

This has two practical consequences. First, AGPL is favored by open-source projects that want to prevent commercial vendors from building closed, value-extracted SaaS layers on top of community work without contributing modifications back — [[MongoDB]] famously moved off AGPL to its own SSPL because even AGPL was insufficient to prevent AWS-style hosted-service commercialization. Second, AGPL is sometimes cited as a "viral" license that complicates corporate adoption, because legal teams at enterprises are reluctant to entangle proprietary infrastructure with AGPL obligations.

[[Canvas LMS]] is licensed under AGPL, which is part of the architectural disruption story against [[Blackboard]] — institutional IT teams could read the source, modify it for their environments, and trust that no commercial vendor could fork Canvas into a closed-source competitor without contributing changes back to the upstream community.

## Related

- [[Canvas LMS]] — AGPL-licensed LMS
- [[GPL]] — parent license family
- [[Free Software Foundation]] — license maintainer
- [[MongoDB]] — moved off AGPL to SSPL
