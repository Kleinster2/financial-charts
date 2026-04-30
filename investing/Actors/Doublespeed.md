---
aliases: [doublespeed.ai, Doublespeed AI]
tags: [actor, ai, marketing, social-media, startup, private, usa]
---
#actor #ai #marketing #socialmedia #startup #private #usa

**Doublespeed** — San Francisco AI marketing startup that operates [[Phone farm|phone farms]] of real smartphones to run thousands of AI-generated social media accounts on behalf of paying clients. Founded 2025; in [[a16z]] [[Speedrun]] cohort SR005; ~4 employees; $2M raised. Pitched as an "attention intelligence platform" for [[Synthetic creators|synthetic creators]] — the operating layer for what the founders call "[[Agentic AI|agentic]] social accounts." Drew unusual press attention in late 2025 because the model is, in plain terms, [[Astroturfing|astroturfing]]-as-a-service, and because a hacker accessed the back-end and exposed which products the bots were promoting on [[TikTok]].

Doublespeed is a small but unusually visible test case for several questions the [[Creator economy]] and [[Agentic AI]] threads have left open: can a vendor run hundreds or thousands of AI-operated [[Synthetic creators|synthetic personas]] cheaply enough to undercut human influencers; can a [[Phone farm]] of real devices stay ahead of platform detection long enough to make that economics durable; and what happens when [[a16z]] writes a $1M check from its [[Speedrun]] program for a product whose stated mode of operation violates the terms of service of every platform it touches. The October 2025 back-end breach — disclosed by [[404 Media]] in December — turned the company from a pitch deck into a public dossier of named clients, named personas, and missing #ad disclosures, which is why the [[FTC]] enforcement question is no longer hypothetical. The note below tracks the company at the level of detail the breach disclosure now permits. The build itself leans heavily on [[Anthropic]]'s [[Claude|Claude Code]], which Lakhani has publicly credited as the company's "third cofounder" — a clean illustration of how frontier model labs are now upstream of products that violate platform policy at scale.

---

## Quick stats

| Metric | Value |
|--------|-------|
| Founded | 2025 |
| Headquarters | San Francisco |
| Employees | ~4 |
| Total raised | $2M (per StartupHub.ai) |
| Lead investor | [[Andreessen Horowitz]] ([[a16z]] [[Speedrun]] SR005) |
| Pricing | $1,500–$7,500 / month |
| Devices under management | ~1,100 smartphones (per Oct 2025 hack) |
| Accounts per the hack | 400+ TikTok accounts; ~200 actively promoting |
| Primary platform | [[TikTok]] |
| Status | Private |
| Website | doublespeed.ai |

---

## Leadership

| Name | Role | Background |
|------|------|------------|
| Zuhair Lakhani | Co-founder, growth | Ran growth at [[Cosmos]] (Series A consumer app); before that grew consumer apps and CPG brands at USC; dropped out to start Doublespeed |
| Hassan Syed | Co-founder, technical | Former ML engineer at [[Google]] (search ads infrastructure), [[Microsoft]], and [[Amazon]]; CTO at RoamAround (acquired 2024) |

Two-person founding team plus two early hires; total headcount ~4 as of late 2025 per a16z's company page.

---

## Evolution

The story is short because the company is six months old, but the arc is already legible:

- 2025 (formation): Lakhani and Syed leave their prior roles ([[Cosmos]] growth and RoamAround CTO respectively) and incorporate Doublespeed in San Francisco. The pitch from day one is a single-operator orchestration platform for "[[Synthetic creators|agentic social accounts]]" — explicitly a [[Phone farm]] play, not a pure-software bot. They build the back-end, called the "Doublespeed TERMINAL," with heavy use of [[Anthropic]]'s [[Claude Code]]; Lakhani would later credit Claude Code on X (October 22, 2025) as "truly our third cofounder."
- October 2025 (a16z and the first wave of press): a16z's [[Speedrun]] program admits Doublespeed into the SR005 cohort with a $1M check. The company starts speaking openly about the model — phone farms, ~95% AI / ~5% human, "one video, 100 ways" — through founder posts on X and a Substack interview. [[404 Media]] publishes the first major piece on October 24, 2025, framing the service as "synthetic influencers as a service." Futurism, BizTechWeekly, and Ynet pick up the story over the following days.
- October 31, 2025 (the breach reported): An anonymous researcher reports a vulnerability that gives them ongoing back-end access to the fleet manager — including device control links, proxy credentials, pending tasks, and the live client roster. They retain access for weeks.
- December 17, 2025 (the breach published): 404 Media publishes the inventory: 1,100+ smartphones, 400+ TikTok accounts, ~200 active campaigns, named brands (Vibit, Rosabella), named personas ("Chloe Davis," "pattyluvslife"), category mix (language-learning apps, dating apps, a Bible app, supplements, massage devices, pharma-adjacent). Doublespeed declines to comment. Slashdot, Gigazine, and others syndicate the story.
- Q1 2026 (quiet): No new round is announced. No follow-on press from the company. No public regulatory action — yet.

The shape this is settling into looks more like a regulated-or-shut-down startup than a venture growth story.

---

## Cap table / funding history

Doublespeed is a privately held Delaware C-corp (per a16z Speedrun company page). The cap table is not public, and the company has not disclosed a valuation. The structure below is what is publicly knowable.

| Date | Round | Amount | Investor / source | Notes |
|------|-------|--------|--------------------|-------|
| 2025 | Pre-seed | $1M | [[a16z]] [[Speedrun]] SR005 | Fast-track accelerator; SR005 is the fifth Speedrun cohort |
| 2025 | Other (undisclosed) | ~$1M | Not publicly named | StartupHub.ai reports $2M total raised; only the a16z tranche is individually attributed |

Implied ownership table (qualitative — exact percentages not disclosed):

| Holder | Stake | Notes |
|--------|-------|-------|
| Founders (Lakhani, Syed) | Majority | Standard pre-seed founder retention |
| [[a16z]] [[Speedrun]] | Single-digit % (estimate) | Speedrun standard terms are SAFE notes at uncapped or modestly capped valuations |
| Other pre-seed investors | Minority | One additional ~$1M tranche, identity not disclosed |

No follow-on round announced as of late April 2026.

---

## Historical financials

Not publicly disclosed. The visible inputs to a rough run-rate estimate:

| Input | Value |
|-------|-------|
| Pricing tiers | $1,500–$7,500 / month |
| Active campaigns at the time of the Oct 2025 breach | ~200 (one persona ≠ one client; multiple personas typically run per client) |
| Implied client count | Roughly tens, not hundreds — a $1.5K–$7.5K subscription with ~200 personas could be ~20–100 clients |
| Implied annual run-rate | Order of $1M–$5M / year, before churn from the breach |

These figures are derived from public reporting, not from disclosed financials. Treat as bounds, not estimates.

---

## What Doublespeed sells

A subscription product the company calls the "Doublespeed TERMINAL." A single marketer logs in and orchestrates bulk content creation (videos, image slideshows, captions) plus deployment across hundreds of social accounts. The pitch: replace "a 30-person social team and a $40,000 budget" with one person at roughly 10% of that cost.

Two design choices distinguish the product from prior bot tooling:

1. Real devices, not emulators. Platforms like [[TikTok]] aggressively detect and block emulator-based automation, so Doublespeed runs each managed account on a physical smartphone in its own [[Phone farm|phone farm]]. Each device sits behind a residential or mobile proxy. The system pushes synthetic actions — taps, swipes, watch time, posts — through layers designed to mimic human use.
2. AI-first content with human "touch up." Co-founder Zuhair Lakhani has stated publicly that "AI does 95% of the work and humans the remaining 5%." Posts are generated, A/B tested by the platform's own algorithms, and iterated on. One [[Anthropic]] product gets a credit by name: in an October 22, 2025 post on X (formerly Twitter), Lakhani called Anthropic's [[Claude|Claude Code]] "truly our third cofounder."

Public performance claims (per founder statements and press coverage):

- One unnamed client: "millions of views in an automated way without getting taken down" using a handful of accounts.
- Another: 4.7 million views in under one month from 15 fake accounts.
- Premium tier output: up to 3,000 posts per month per client.

These figures are founder-sourced and have not been independently verified.

---

## Pricing

| Tier | Monthly | Implied output |
|------|---------|----------------|
| Basic | $1,500 | Tens to hundreds of posts per month |
| Premium | $7,500 | Up to 3,000 posts / month |

Subscription model. Client list is not public; the breach disclosure (below) is the only public window into who pays.

---

## Phone farm operating model

A "[[Phone farm]]" — a shelf or rack of physical smartphones, each running one social account, managed centrally — is an old technique in the gray market for engagement and reviews. Doublespeed's variant is engineered for scale and platform evasion:

| Layer | Function |
|-------|----------|
| Hardware | ~1,100 physical smartphones (per Oct 2025 hack disclosure) |
| Network | Per-device proxies (residential/mobile IPs) so each account looks geographically authentic |
| Control | "Manager" PCs each driving a subset of devices |
| Content | Bulk AI-generated images, slideshows, short-form videos |
| Deployment | Orchestration platform sequences posts/replies/watch time across the fleet |
| Account warming | New accounts are "raised" — given organic-looking behavior before being asked to promote anything |

The unit economics work because the smartphones are cheap and replaceable, residential proxies are commoditized, and the AI content pipeline is near-zero-marginal-cost. The persistent cost is the moderation arms race with [[TikTok]] and other platforms.

---

## Clients exposed by the October 2025 hack

On October 31, 2025 a hacker reported a vulnerability that gave them ongoing back-end access to Doublespeed's fleet manager. [[404 Media]] published the disclosure on December 17, 2025; Slashdot, Gigazine, BizTechWeekly, and Futurism followed.

What the breach revealed:

| Detail | Per breach disclosure |
|--------|------------------------|
| Devices visible | 1,100+ smartphones |
| TikTok accounts visible | 400+ |
| Accounts actively promoting | ~200 |
| Credentials exposed | Proxy logins, manager-PC control links, pending-task queues |
| Categories promoted | Language-learning apps, dating apps, a Bible app, dietary supplements, massage devices, pharma-adjacent products |

Two named brands surfaced in reporting:

- Vibit — massage roller maker. One AI persona, "Chloe Davis," posted ~200 health-themed images of an AI-generated middle-aged woman discussing physical ailments while promoting massage rollers.
- Rosabella — supplement brand. A persona "pattyluvslife" falsely claimed UCLA student status while promoting supplements.

Most posts lacked the #ad disclosures required by [[FTC]] endorsement guidelines. Doublespeed declined to comment to 404 Media. The hacker, anonymous and citing retaliation concerns, said they retained back-end access at the time of publication.

---

## Platform and regulatory exposure

Doublespeed's product, by design, violates the inauthentic-behavior policies of every major social platform it uses or has plans to use:

| Platform | Status |
|----------|--------|
| [[TikTok]] | Primary deployment surface; inauthentic-amplification policy explicitly prohibits coordinated bot operations |
| [[Instagram]] ([[Meta]]) | Announced future surface |
| X (formerly Twitter) | Announced future surface |
| [[Reddit]] | Has stated publicly that Doublespeed's service violates Reddit's terms of use |

US regulatory exposure runs along three lines: (1) [[FTC]] undisclosed-endorsement enforcement (the persona accounts identified in the hack were paid promoters without disclosure); (2) potential state-level deceptive-practice statutes; (3) platform-side civil action, which is rare but possible (precedent: [[Meta]] v. Bright Data and similar scraper/abuse cases).

[[Marc Andreessen]] sits on the board of [[Meta]], whose [[Instagram]] product is one of Doublespeed's announced future targets — a governance overlap that has been noted in the press but not formally raised by Meta.

---

## Why it shows up in this vault

Doublespeed is a small company, but it is a clean reference point for several themes already tracked here:

- a16z portfolio risk profile. The firm's [[Speedrun]] program writes small checks at high velocity; Doublespeed is the public face of what that velocity selects for. Reputational fallout (if any) sits at [[a16z]], not at the LPs.
- Hardware moat against algorithmic detection. Phone farms are an answer to "how do you scale AI-generated activity once detection improves?" — a recurring question across [[Synthetic creators]], [[AI Video Generation]], and [[Agentic AI security]].
- Authenticity as the contested attribute. [[Creator-Led Media Scaling]] documents the creator-economy bet on human-first formats; Doublespeed is the explicit counter-trade — synthetic distribution priced at $1,500–$7,500 / month.
- Paying customer of frontier AI labs. Lakhani's "third cofounder" credit to [[Claude Code]] means [[Anthropic]] is, indirectly, in the supply chain for an astroturfing platform. This is the kind of downstream-use case that the lab's responsible-scaling framework will eventually have to address by policy or by detection rather than by hope.
- FTC enforcement test case. A breach has now produced a publicly enumerated list of undisclosed paid promoters operating at scale on a US platform. Whether the [[FTC]] moves on this is a near-term signal on how disclosure rules apply to AI-operated personas.

---

## Related

- [[a16z]] — lead investor via [[Speedrun]] SR005 ($1M)
- [[Andreessen Horowitz]] — parent firm
- [[Marc Andreessen]] — co-founder of a16z, [[Meta]] board member
- [[Speedrun]] — a16z's accelerator program
- [[Anthropic]] — supplier; [[Claude Code]] credited by founders as a primary build tool
- [[TikTok]] — primary deployment platform
- [[Meta]] — announced future deployment platform via [[Instagram]]
- [[Reddit]] — has flagged the service as a TOS violation
- [[Claude]] — frontier model used to build Doublespeed's back-end (per Lakhani's public statement)
- [[Claude Code]] — the specific [[Anthropic]] product cited as the company's "third cofounder"
- [[404 Media]] — broke the synthetic-influencer story (Oct 24, 2025) and the hack disclosure (Dec 17, 2025)
- [[FTC]] — relevant US regulator for endorsement-disclosure violations
- [[Media]] — sector hub

### Concepts

- [[Synthetic creators]] — broader category Doublespeed sits in
- [[Phone farm]] — operational technique
- [[Astroturfing]] — historical antecedent and policy framing
- [[Agentic AI]] — the autonomy layer on which "synthetic creator" pitches rest
- [[Agentic AI security]] — adjacent risk surface (the Doublespeed hack is a live example)
- [[Creator-Led Media Scaling]] — the human-authentic counter-trade
- [[Influencer-to-brand playbook]] — the legitimate end of the same distribution thesis
- [[AI Video Generation]] — content layer enabling cheap synthetic posts
- [[Celebrity AI Adoption]] — adjacent demand-side case for synthetic media

---

## Sources

- [404 Media — "a16z-Backed Startup Sells Thousands of 'Synthetic Influencers'…"](https://www.404media.co/a16z-backed-startup-sells-thousands-of-synthetic-influencers-to-manipulate-social-media-as-a-service/) (Oct 24, 2025)
- [404 Media — "Hack Reveals the a16z-Backed Phone Farm Flooding TikTok with AI Influencers"](https://www.404media.co/hack-reveals-the-a16z-backed-phone-farm-flooding-tiktok-with-ai-influencers/) (Dec 17, 2025)
- [Futurism — "AI 'Phone Farm' Startup Gets Funding from Marc Andreessen…"](https://futurism.com/artificial-intelligence/doublespeed-ai-phone-farm) (Oct 27, 2025)
- [BizTechWeekly — "Doublespeed's AI-Powered Phone Farm Sparks Ethical Debate…"](https://biztechweekly.com/doublespeeds-ai-powered-phone-farm-sparks-ethical-debate-over-social-media-spam-and-platform-integrity/)
- [Slashdot — "Doublespeed Hack Reveals What Its AI-Generated Accounts Are Promoting"](https://tech.slashdot.org/story/25/12/17/236241/doublespeed-hack-reveals-what-its-ai-generated-accounts-are-promoting) (Dec 17, 2025)
- [Gigazine — "Hacking exposes the reality of startup 'Doublespeed'…"](https://gigazine.net/gsc_news/en/20251218-doublespeed-ai-promoting/) (Dec 18, 2025)
- [a16z Speedrun — Doublespeed company page](https://speedrun.a16z.com/companies/doublespeed)
- [StartupHub.ai — Doublespeed profile](https://www.startuphub.ai/startups/doublespeed)
- [Lucas Masoero on [[Substack]] — "Attention meets AI: How Doublespeed is rewriting the rules of social media marketing"](https://lucasmasoero.substack.com/p/attention-meets-ai-how-doublespeed)

---

*Created 2026-04-27.*
