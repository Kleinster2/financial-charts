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
| Otter.ai | Yes | Established, enterprise |
| Fireflies.ai | Yes | Mini-apps, insight extraction |
| tl;dv | Yes | Video clips, timestamps |
| Read AI | Yes | Email "digital twin" |
| Fathom | Yes | Free tier, simple UX |
| Quill | No | Privacy-first, newer |
| Talat | No | Fully on-device |

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
- No Android or web app yet
- Competitors (Otter, Fireflies) have deeper enterprise footprints

Private: no public market exposure. Watch for potential IPO if AI [[SaaS]] IPO window opens.

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
- [[Google]] — acquired Pedregal's previous company Socratic
- [[Mistral]] — enterprise customer

### Cross-vault
- [Technologies: Granola](obsidian://open?vault=technologies&file=Granola) — technical architecture, competitive landscape
