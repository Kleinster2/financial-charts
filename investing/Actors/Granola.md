---
aliases:
  - Granola AI
  - Granola Inc
tags:
  - actor
  - ai
  - saas
  - private
---

Granola — London-based AI meeting notes startup. No-bot architecture captures device audio without joining calls as a visible participant. Founded 2023, valued at $1.5B (March 2026).

One-line read: priced as a context-infrastructure company, growing like one in the Feb 2026 cohort, but the moat is untested across a renewal cycle and the platform gap ([[Android]], web) is real. The [[Index Ventures]] round is a directional bet that the next three [[YipitData]] readings confirm Feb 2026 was the inflection, not the noise.

---

## Why Granola matters

| Metric | Value |
|--------|-------|
| Founded | 2023 |
| Headquarters | London, [[UK]] |
| Founders | Chris Pedregal (CEO), Sam Stephenson |
| Valuation | $1.5B (Mar 2026) |
| Total raised | $192M |
| Status | Private |
| Key investors | [[Index Ventures]], [[Kleiner Perkins]], [[Lightspeed Venture Partners]], [[Spark Capital]], NFDG ([[Nat Friedman]] + [[Daniel Gross]]) |
| Enterprise customers | Vanta, [[Gusto]], Thumbtack, [[Asana]], [[Cursor]], [[Lovable]], Decagon, [[Mistral]] |

Differentiator: no bot in the meeting. Granola transcribes via local device audio capture, then enhances with AI. Other tools (Otter, Fireflies, tl;dv) drop a visible bot participant into calls — many organizations ban this.

---

## Founders

Chris Pedregal (CEO) — previously built Socratic, an education app acquired by [[Google]]. Serial founder with consumer-to-enterprise arc.

Sam Stephenson — design-first co-founder. Met Pedregal through a community comparing productivity tools.

---

## Funding history

| Round | Date | Amount | Valuation | Lead |
|-------|------|--------|-----------|------|
| Seed | May 2023 | $4.25M | — | [[Lightspeed Venture Partners]] |
| Series A | Oct 2024 | $20M | — | [[Spark Capital]] |
| Series B | May 2025 | $43M | $250M | NFDG ([[Nat Friedman]] + [[Daniel Gross]]) |
| Series C | Mar 2026 | $125M | $1.5B | [[Index Ventures]] (Danny Rimer) |

Valuation trajectory: $250M → $1.5B in under a year (6× step-up). Claimed 10% weekly growth in active users at Series B.

Total raised: $192M across four rounds.

---

## Growth signals (Feb 2026)

Granola is private and does not publish revenue. [[YipitData]] card-panel and signals data (published Apr 2026, covering Feb 2026 cohort) provide the cleanest third-party read.

| Metric | Value | Window |
|--------|-------|--------|
| Net new customers | 4× prior six-month average | Feb 2026 |
| Gross adds | 9× | Jan 2026 → Feb 2026 |
| Customer count, month-over-month | +25% | Feb 2026 |
| Mid-market spend per customer | ~$6K | Feb 2026 |
| Mid-market spend trajectory | 3× | prior 6 months |
| Churn | Near zero | trailing |
| Headcount growth | +49% | prior 6 months |

[[YipitData]] also reports that customers adopting Granola frequently drop competing tools ([[Fathom AI]], [[Fireflies.ai]], [[Otter.ai]]) while the reverse pattern is rarely observed — a displacement signal, not coexistence.

The Feb 2026 acceleration sits between two product milestones: the [[MCP]] server (Feb 2026) and the personal + enterprise APIs (Mar 2026). The growth surge is contemporaneous with — not subsequent to — the platform-positioning shift.

---

## Product

Core: AI notepad that transcribes meetings and generates structured notes without a bot.

| Feature | Detail |
|---------|--------|
| Architecture | Local device audio capture (macOS, Windows, iOS) |
| Audio storage | None — deleted after transcription |
| Output | Structured notes, action items, summaries |
| Templates | Customizable per meeting type |
| Recipes | Automated post-call actions (follow-ups, CRM updates) |
| [[MCP]] server | Feb 2026 — exposes notes to AI tools ([[Claude]], [[ChatGPT]], [[Replit]], v0, etc.) |
| APIs | Mar 2026 — personal + enterprise programmatic access |
| Spaces | Mar 2026 — team workspaces with granular access |
| SOC 2 Type 2 | Jul 2025 |

### Pricing

| Plan | Price | Key features |
|------|-------|-------------|
| Free | $0 | Unlimited meetings, limited history |
| Business | $14/user/month | CRM integrations, [[Slack]]/[[Notion]], MCP, team folders |
| Enterprise | $35+/user/month | SSO, admin controls, public API, usage analytics |

CRM integrations: [[HubSpot]], Affinity, Attio (native); [[Salesforce]] via [[Zapier]].

---

## Competitive position

AI meeting notes is a crowded, commoditizing category. The differentiation axis is bot vs. no-bot:

| Competitor | Bot? | Notes |
|-----------|------|-------|
| [[Otter.ai]] | Yes | Established, enterprise |
| [[Fireflies.ai]] | Yes | Mini-apps, insight extraction |
| tl;dv | Yes | Video clips, timestamps |
| Read AI | Yes | Email "digital twin" |
| [[Fathom AI]] | Hybrid (Apr 2026) | Bot + bot-free with speaker diarization; 500K+ users, $30M ARR (CY25); shipped "Fathom 3.0" Apr 15 2026 explicitly framed as Granola response |
| Quill | No | Privacy-first, newer |
| Talat | No | Fully on-device |

[[YipitData]] customer-baseline comparison (Apr 2026 read):

| Peer | Customer count vs Granola | Trend | Last disclosed round |
|------|---------------------------|-------|----------------------|
| [[Fathom AI]] | +20% | Growth slowing; headcount −6% | $17M Series A (Sep 2024) |
| [[Otter.ai]] | +20% | Spend plateauing; 278 employees (Apr 2026) | $50M Series B (Feb 2021) |
| [[Fireflies.ai]] | +40% | Spend declining; +5% headcount | $1B+ valuation (Jun 2025) |
| Avoma | 13 mid-market customers | Flat adoption; +14% headcount | $12M Series A (Dec 2021) |

Granola has the smallest installed base among the named peers but the steepest acquisition curve and the highest mid-market ARPU signal. [[Fireflies.ai]] sits at $1B+ with ~40% more customers than Granola — implying Granola's $1.5B price tag is being underwritten by growth and ARPU, not installed base.

Granola's bet: meeting notes are becoming a commodity — the value is in context-as-infrastructure ([[MCP]], APIs) that feeds downstream AI workflows. This is why the valuation jumped 6× in a year despite the category being crowded.

---

## Investment case

Bull:
- 6× valuation increase in <1 year signals strong traction
- No-bot approach = frictionless enterprise adoption
- [[MCP]] server + APIs = platform play, not just a tool
- Enterprise customers include AI-native companies ([[Cursor]], [[Lovable]], [[Mistral]])
- Chris Pedregal has a successful exit (Socratic → [[Google]])
- SOC 2 in 3 months (vs 12-18 typical) — clean architecture

Bear:
- AI meeting notes is commoditizing fast (many free/cheap alternatives)
- $1.5B valuation on unstated revenue — likely aggressive multiple
- Local audio capture = potential legal liability in two-party consent jurisdictions
- [[a16z]] partner incident: locking local database broke agent workflows, risking developer trust
- Android planned for later 2026 with [[Google]] Drive sync and Google Assistant integration; web client still absent — installed-base gap vs [[Otter.ai]]/[[Fireflies.ai]] continues until ship
- Competitors ([[Otter.ai]], [[Fireflies.ai]]) have 20–40% larger customer counts; head start on enterprise procurement cycles

Private: no public market exposure. Watch for potential IPO if AI [[SaaS]] IPO window opens.

---

## Analysis

The $1.5B mark is a growth multiple, not a footprint multiple. [[Fireflies.ai]] disclosed $1B+ in June 2025 with roughly 40% more customers than Granola; on a customer basis Granola is priced ~2× richer than its larger-installed-base peer. The [[Index Ventures]]-led round is therefore underwritten by the Feb 2026 inflection — net new customers at 4× the prior six-month average, gross adds 9× month-on-month, mid-market ARPU at ~$6K and 3× over six months — rather than by current installed base. If that acceleration normalises, the multiple compresses.

The platform shift sits at the centre of the bet. The Feb 2026 customer surge is contemporaneous with the [[MCP]] server launch and pre-empts the Mar 2026 personal + enterprise API release; the acquisition layer is responding to platform positioning ahead of any platform revenue. Granola is selling a notepad and pricing a context-infrastructure layer. The Spaces tier and the $35+/user/month Enterprise plan are where that thesis has to materialise — at acquisition the story is working, but the Enterprise ARPU per seat needs to hold across renewal cycles to justify the step-up.

Two structural tensions sit in the data. First, near-zero churn alongside displacement of [[Fathom AI]], [[Fireflies.ai]] and [[Otter.ai]] suggests the category was migrating to bot-free capture rather than fragmenting. As of April 15 2026, that tension shifted: [[Fathom AI]] shipped "Fathom 3.0" with bot-free transcription and speaker diarization, explicitly framed by [[TechCrunch]] as a Granola response, with [[Richard White]] pitching accuracy ("who said what") plus Fathom's distribution depth ([[HubSpot]] 2025 Most Used App, 8,500+ active installs, 500K+ users) as the differentiation. The "architecture moat" assumption now needs a Fathom-specific carve-out — what remains is the question of whether [[Otter.ai]] and [[Fireflies.ai]] can do the same retrofit before the customer cohort migrates further. Second, the platform gap is real: no Android, no web. The Android client is planned for later 2026 with [[Google]] Drive and Google Assistant integration but is undated; until ship, [[Otter.ai]] and [[Fireflies.ai]] retain a structural advantage in mixed-device enterprises and on-the-go capture. The valuation assumes the platform gap closes before the larger competitors close the architecture gap — and Fathom shipping bot-free in April shortened the runway on the latter.

The Pedregal signal matters here. Socratic was a consumer education app that [[Google]] acquired — a successful exit on a smaller scale, with a Google-shaped buyer at the end. [[Google]] is also the platform owner Granola is most exposed to (Android, Workspace, Meet). The structural question for late-cycle [[SaaS]] is whether Granola becomes the canonical context layer for the [[MCP]] ecosystem or the canonical acquisition target when [[Google]] decides meeting notes belong in Workspace. The platform-positioning shift makes both outcomes more likely simultaneously.

The bear case for the multiple is no longer just "the data will revert" — it now also includes "competitors are catching up faster than the platform gap closes." Fathom's April 15 2026 architecture absorption is the first concrete data point on competitor-retrofit speed; if [[Otter.ai]] or [[Fireflies.ai]] ships bot-free in Q2 or Q3 2026, the differentiation axis collapses to accuracy + distribution rather than architecture. The Feb 2026 cohort is one month; the next three months of [[YipitData]] readings determine whether $1.5B is conservative or reflexive, and the May–Jun 2026 reads in particular are the first to fall *after* Fathom 3.0 shipped.

---

## What to watch

| Signal | Why it matters | Trigger |
|--------|----------------|---------|
| Next two [[YipitData]] reads (May–Jun 2026 cohorts) | Tests whether Feb 2026 was inflection or noise; the entire $1.5B underwrite hinges on the curve holding | New customer-acquisition or spend readouts published Q2 2026 |
| [[Android]] ship date | Every quarter of slip is a quarter [[Otter.ai]] and [[Fireflies.ai]] can retrofit local-capture; closes the platform gap that the bear case hinges on | Granola product blog / Pedregal interviews; integration with [[Google]] Drive + Google Assistant |
| Competitor architecture retrofit speed | [[Fathom AI]] shipped bot-free Apr 15 2026 ("Fathom 3.0"); test is whether [[Otter.ai]] and [[Fireflies.ai]] follow in Q2–Q3 2026 | Product announcements; capture-mode menus on competitor apps; third-party accuracy testing of new bot-free modes |
| Enterprise renewal data on the $35+/user Spaces tier | Spaces stickiness is the real test of the context-infrastructure thesis; high acquisition with weak renewals = commodity, not platform | First full renewal cohort lands H2 2026 |
| [[MCP]]-ecosystem retention | Whether meeting context actually shows up in downstream AI products ([[Claude]], [[ChatGPT]], [[Cursor]], [[Lovable]], [[Replit]], v0) validates the platform thesis; absence keeps it a notepad | MCP usage data, customer references for API-driven workflows |
| AI [[SaaS]] IPO window | If the window opens, Granola is plausibly in the second wave; tests both the price and the public-market read on context-infrastructure | Sector IPO comps re-rate; bookrunner mandates |
| [[Google]] strategic posture | Whether Workspace bundles a no-bot meeting layer, or [[Google]] approaches Granola for acquisition — both outcomes consistent with the same investor case | [[Workspace]] product announcements; Pedregal–[[Google]] proximity signals |

---

## Quick stats

| Metric | Value |
|--------|-------|
| Founded | 2023 |
| HQ | London |
| Founders | Chris Pedregal, Sam Stephenson |
| Valuation | $1.5B (Mar 2026) |
| Total raised | $192M |
| Last round | $125M Series C ([[Index Ventures]]) |
| Status | Private |

*Created 2026-03-31*

---

## Related

- [[Index Ventures]] — Series C lead
- [[Kleiner Perkins]] — Series C participant
- [[Lightspeed Venture Partners]] — seed investor
- [[Spark Capital]] — Series A lead
- [[Google]] — acquired Pedregal's previous company Socratic; also Android/Workspace platform owner
- [[Mistral]] — enterprise customer
- [[Fireflies.ai]], [[Otter.ai]], [[Fathom AI]] — competitive customer-base benchmarks
- [[YipitData]] — third-party signals source for growth metrics
- [[MCP]] — context-infrastructure layer Granola is positioning on

### Cross-vault
- [Technologies: Granola](obsidian://open?vault=technologies&file=Granola) — technical architecture, competitive landscape
