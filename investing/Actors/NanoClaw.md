#actor #startup #ai #opensource

**NanoClaw** — Open-source, security-first personal AI assistant built by [[Gavriel Cohen]] and [[Lazer Cohen]] (now operating as **NanoCo**). Started as a 500-line weekend project to replace [[OpenClaw]] after Cohen discovered it had silently downloaded all his WhatsApp messages. In six weeks, it went from couch-coding to 22k GitHub stars, an [[Andrej Karpathy]] endorsement, and an integration deal with [[Docker]]. The thesis: container isolation is the correct security model for AI agents, and OpenClaw's 800k-line codebase with unvetted dependencies is an unacceptable attack surface. Now NanoCo is shutting down a $1M ARR marketing agency to go full-time on this, living on friends-and-family money while VCs circle.

## Quick stats

| Metric | Value |
|--------|-------|
| **GitHub** | [github.com/qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) |
| **Stars** | 22k+ |
| **Forks** | 4.6k+ |
| **Contributors** | 50+ |
| **Founded** | Jan 31, 2026 (MIT license) |
| **Company** | NanoCo (Gavriel Cohen CEO, Lazer Cohen President) |
| **Prior company** | Qwibit (AI marketing agency, ~$1M ARR trajectory, shut down Mar 2026) |
| **Funding** | Friends & family round (undisclosed) |
| **Codebase** | ~500 lines (vs OpenClaw's ~800k) |
| **Website** | [nanoclaw.dev](https://nanoclaw.dev) |

## Synopsis

NanoClaw is the security-first fork of the personal AI agent movement. Gavriel Cohen, a former [[Wix]] engineer running an AI marketing agency (Qwibit), built it in a 48-hour weekend sprint after discovering OpenClaw had stored all his WhatsApp messages — personal included — in unencrypted plaintext. His solution: each agent conversation runs in its own Linux container, so a compromised session can't access anything beyond its explicit authorization. The project is intentionally tiny (~500 lines vs OpenClaw's 800k), auditable by one person, and now ships with [[Docker]] Sandboxes as the default isolation backend after a deal announced March 13, 2026.

The bull case: container isolation becomes the industry standard for AI agents (Cisco called OpenClaw a "security nightmare"), Docker partnership gives NanoClaw instant enterprise credibility, and the 50+ contributor community is building at startup velocity with zero VC pressure. The bear case: NanoCo has no revenue model, the Cohens are living on friends-and-family money, enterprise agent security is an increasingly crowded space, and OpenClaw is iterating fast on its own security (the advantage may be temporary).

## Evolution

The story of NanoClaw is the story of security anxiety converting into a movement.

- **Late 2025:** Gavriel Cohen and his brother Lazer launch Qwibit, an "AI-native marketing agency" using Claude Code agents for research, client work, and pipeline management. The business model — humans managing AI agents to deliver services at software margins — hits traction quickly, tracking toward $1M ARR. But the agents are disconnected: each does work when prompted, but there's no way to pre-schedule tasks or connect them to team communication tools like WhatsApp.
- **Jan 2026:** Cohen discovers [[OpenClaw]] and has an "aha moment" — it's the orchestration layer connecting his separate agent workflows. He immediately plans to deploy it across R&D, product, and client management. Then he finds a plaintext file where the OpenClaw agent downloaded *all* his WhatsApp messages, not just work-related ones. Investigating further, he discovers an "obscure" open-source PDF-editing project *he himself had written months ago* bundled into OpenClaw's dependency tree — he had no idea and wasn't maintaining it. The realization: nobody can audit 800k lines of code with unknown dependencies.
- **Jan 31, 2026:** Cohen builds NanoClaw in a ~48-hour coding binge ("I sat down on the couch in my sweatpants and just basically melted into it"), originally using [[Apple]]'s new container technology for isolation. Publishes on Hacker News. [The post goes viral.](https://news.ycombinator.com/item?id=46850205)
- **Late Feb 2026:** [[Andrej Karpathy]] posts praise on X, triggering a second viral wave. Stars accelerate from ~11k to 22k. YouTube reviews, news coverage, and developer community amplification follow. A domain squatter grabs a NanoClaw URL (the real one is nanoclaw.dev).
- **Early Mar 2026:** Cohen shuts down Qwibit (the $1M ARR agency) to focus full-time on NanoClaw. Forms NanoCo with Lazer as President. Living on a friends-and-family round. VCs are calling.
- **Mar 13, 2026:** [Docker deal announced.](https://nanoclaw.dev/blog/nanoclaw-docker-sandboxes) Oleg Šelajev from Docker reached out, modified NanoClaw to use Docker Sandboxes instead of Apple's containers, and Cohen immediately adopted it as the standard. "This is no longer my own personal agent that I'm running on my Mac Mini. This now has a community around it."

## Market positioning

| | [[OpenClaw]] | NanoClaw | [[PicoClaw]] | [[Zo Computer]] |
|--|---------|----------|------------|-------------|
| Model | Open source | Open source | Open source | Managed cloud |
| Moat | Features, ecosystem | Security, simplicity | Hardware integration | UX, convenience |
| Target | Power users | Security-conscious | Embedded/IoT | Non-technical |
| Codebase | ~800k lines | ~500 lines | Go-based | Proprietary |

## Insights

- **The "security nightmare" thesis is real.** Cisco published a blog post calling OpenClaw exactly that. Cohen's WhatsApp discovery is a concrete example — AI agents with broad system access will inevitably hoover up data beyond their mandate. Container isolation is a genuine architectural answer, not just marketing.
- **Docker partnership = instant distribution.** Docker has millions of developers and ~80k enterprise customers. NanoClaw switching to Docker Sandboxes as default means every Docker user can run NanoClaw with production-grade isolation out of the box. That's more credibility than any seed round could buy.
- **The business model is the open question.** NanoClaw is MIT-licensed and the Cohens "vow it always will be." Commercial plans center on forward-deployed engineers helping enterprises build secure agents — a services model, not a product model. Crowded space getting more crowded by the hour.
- **Speed of community formation is remarkable.** 50+ contributors, 4.6k forks, and a Docker partnership in 6 weeks from a weekend project. The OpenClaw ecosystem is generating spinoffs the way Linux generated distributions — security (NanoClaw), embedded ([[PicoClaw]]), and managed ([[Zo Computer]]) variants are all finding their niches.

## Leadership

| Role | Name | Background |
|------|------|------------|
| CEO | [[Gavriel Cohen]] | Former [[Wix]] engineer. Built NanoClaw in a weekend. Previously co-founded Qwibit (AI marketing agency, ~$1M ARR) and Concrete Media (PR firm) |
| President | [[Lazer Cohen]] | Co-founded Qwibit and NanoCo with Gavriel |

## Related

- [[OpenClaw]] — the full-featured original; NanoClaw's security critique drove its creation
- [[Docker]] — Sandboxes integration partner (announced Mar 13, 2026)
- [[HKUDS]] — their nanobot project (34k stars) is often confused with NanoClaw; completely different teams
- [[PicoClaw]] — Go-based, embedded hardware focus
- [[Zo Computer]] — managed cloud competitor
- [[Agentic AI]] — the broader trend
- [[Andrej Karpathy]] — viral endorsement on X catalyzed growth

### Cross-vault
- [Technologies: NanoClaw](obsidian://open?vault=technologies&file=NanoClaw) — technical architecture and agent capabilities

