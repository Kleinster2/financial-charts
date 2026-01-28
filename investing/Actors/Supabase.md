# Supabase

#actor #startup #private #usa #developer-tools #database

**Supabase** — Open-source Firebase alternative built on Postgres. Backend-as-a-service (BaaS) offering database, auth, storage, edge functions, and realtime subscriptions. **$70M ARR (2025), growing 250% YoY. $5B valuation.** YC W20. Benefiting massively from "vibe coding" boom — ~40% of recent YC batches build on Supabase.

---

## Key facts

| Metric | Value |
|--------|-------|
| Founded | 2020 |
| HQ | San Francisco, CA (remote-first) |
| Batch | [[Y Combinator]] W20 |
| Employees | ~230 |
| Developers | 2M+ |
| Databases hosted | 3.5M+ |
| GitHub stars | 81K+ |

---

## Founders

| Person | Role | Background |
|--------|------|------------|
| **[[Paul Copplestone]]** | CEO | Serial founder, YC W20 |
| **[[Ant Wilson]]** | CTO | Liverpool → Singapore, 10 years trying startups |

Both founders met at Entrepreneur First (Singapore); company is remote-first with no central office.

---

## Financials

### Revenue

| Year | ARR | Growth |
|------|-----|--------|
| 2021 | ~$50K | — |
| 2023 | ~$4M | — |
| 2024 | ~$20-30M | — |
| 2025 | **$70M** | **250% YoY** |

*Source: Sacra estimates, Oct 2025*

Revenue model: Usage-based pricing (compute, storage, bandwidth) + subscription tiers.

---

## Cap table

### Funding rounds

| Round | Date | Amount | Valuation | Lead |
|-------|------|--------|-----------|------|
| Seed | 2020 | $6M | — | Y Combinator |
| Series A | May 2021 | $30M | — | Coatue |
| Series B | Aug 2022 | $80M | $520M | Felicis |
| Series C | Aug 2024 | $80M | $900M | Peak XV, [[Craft Ventures]] |
| Series D | Apr 2025 | $200M | $2B | Accel |
| Series E | Oct 2025 | $120M | **$5B** | Peak XV, Accel |

**Total raised: ~$500M+**

### Key investors

| Investor | Role |
|----------|------|
| [[Y Combinator]] | Seed, W20 batch |
| [[Coatue]] | Series A lead |
| [[Felicis Ventures]] | Series B lead |
| [[Peak XV Partners]] | Series C, E lead |
| [[Craft Ventures]] ([[David Sacks]]) | Series C |
| [[Accel]] | Series D, E lead |
| Mozilla Ventures | Participant |

### Notable angels

| Person | Affiliation |
|--------|-------------|
| [[Guillermo Rauch]] | CEO, [[Vercel]] |
| [[Tom Preston-Werner]] | Co-founder, GitHub |
| [[Nat Friedman]] | Former CEO, GitHub |
| [[Kevin Weil]] | CPO, [[OpenAI]] |
| Taylor Otwell | Creator, Laravel |

---

## Product

### Core offering

Supabase provides a complete backend stack on top of Postgres:

| Component | What it does |
|-----------|--------------|
| **Database** | Dedicated Postgres instance per project |
| **Auth** | JWT-based, OAuth, email, SSO |
| **Storage** | S3-compatible file storage with CDN |
| **Edge Functions** | TypeScript/Deno serverless functions |
| **Realtime** | WebSocket subscriptions to DB changes |
| **Vector** | pgvector for AI embeddings |

### Key differentiators vs Firebase

| Dimension | Supabase | Firebase |
|-----------|----------|----------|
| Database | Postgres (SQL) | Firestore (NoSQL) |
| Open source | Yes (self-hostable) | No |
| Vendor lock-in | Low (standard Postgres) | High |
| Pricing | Usage-based, predictable | Can spike unpredictably |
| SQL support | Full | None |

### Auto-generated APIs

Every Supabase project automatically gets:
- RESTful API (PostgREST)
- GraphQL API (pg_graphql)
- Realtime subscriptions

No backend code required for basic CRUD.

---

## Growth drivers

### The "vibe coding" boom

Supabase found extreme product-market fit in 2024-2025 as the default backend for AI-assisted development:

| Tool | How it uses Supabase |
|------|---------------------|
| **Bolt.new** | Auto-provisions Supabase for generated apps |
| **[[Lovable]]** | Default backend integration |
| **[[Cursor]]** | Frequently suggested for AI-built apps |
| **v0 (Vercel)** | Common pairing |

**Key stat:** AI coding tools generate apps that need backends. Supabase is the path of least resistance — instant provisioning, no config, SQL-based.

### YC adoption

~40% of recent YC batches build on Supabase. The YC → Supabase pipeline:
1. YC companies move fast, need instant backend
2. Supabase is YC-backed (W20), trusted in ecosystem
3. Founders recommend to other founders

### Developer love

- 81K+ GitHub stars (top 100 on GitHub)
- Strong documentation, tutorials
- Active [[Discord]] community
- Open source = trust, transparency

---

## What makes Supabase work

### The Postgres bet

**Core insight:** Postgres is eating the database world. By building on Postgres (not a proprietary DB), Supabase:
- Inherits 30+ years of ecosystem (tools, extensions, talent)
- Provides zero vendor lock-in (export and run anywhere)
- Gets pgvector for AI "for free"
- Attracts developers who already know SQL

### Flywheel

```
More developers → More GitHub stars/content → More discovery
     ↑                                              ↓
Better docs/DX ← More revenue ← More projects hosted
```

### Structural advantages

| Advantage | Why it matters |
|-----------|----------------|
| **Open source** | Trust, community contributions, self-host option |
| **Postgres standard** | No lock-in, familiar to millions of devs |
| **Full-stack BaaS** | One platform vs stitching 5 services |
| **AI coding symbiosis** | Default backend for Bolt/[[Lovable]]/[[Cursor]] |
| **YC network** | 40% of batches = massive distribution |

### What's hard to copy

| Moat | Durability |
|------|-----------|
| GitHub mindshare (81K stars) | Years of community building |
| AI tool integrations | First-mover, default status |
| YC ecosystem position | [[Network effects]] |
| Postgres ecosystem depth | 30+ years, hard to replicate |

---

## Competitive landscape

| Competitor | Positioning | Difference |
|------------|-------------|------------|
| **Firebase** ([[Google]]) | Incumbent BaaS | NoSQL, closed source, lock-in |
| **[[PlanetScale]]** | Managed MySQL | MySQL-based, no auth/storage |
| **[[Neon]]** | Serverless Postgres | DB-only, no BaaS features |
| **Railway** | App deployment | Broader focus, less BaaS |
| **Convex** | Reactive backend | TypeScript-native, different model |
| **Appwrite** | Open source BaaS | Smaller scale, less Postgres-native |

**Key distinction:** Supabase is Postgres-first, full-stack BaaS. Most competitors are either DB-only (Neon, PlanetScale) or non-Postgres (Firebase, Convex).

---

## Risks

| Risk | Severity | Notes |
|------|----------|-------|
| **Firebase response** | Medium | Google could improve Firebase, but hasn't aggressively |
| **Neon competition** | Medium | Serverless Postgres, but DB-only |
| **Margin pressure** | Medium | Postgres hosting is commoditizing |
| **AI code tool dependency** | High | If Bolt/[[Lovable]] fade, growth slows |
| **Enterprise sales** | Medium | [[Consumer]]/SMB strong, enterprise unproven |

---

## Investment relevance

**Why track Supabase:**

1. **AI infrastructure play** — Not an AI company, but critical infrastructure for AI-built apps. Proxy for "vibe coding" trend.

2. **Postgres ecosystem bet** — If Postgres continues winning, Supabase wins.

3. **YC signal** — 40% YC adoption = early indicator of startup infrastructure trends.

4. **Pre-IPO optionality** — $5B valuation, $70M ARR, 250% growth. IPO candidate 2026-2027.

5. **Developer sentiment** — 81K GitHub stars = genuine love, not hype.

---

## Related

### Ecosystem
- [[Y Combinator]] — W20 batch, 40% of batches use Supabase
- [[Postgres]] — underlying database technology
- [[Databases]] — sector context

### Investors
- [[Coatue]] — Series A lead
- [[Sequoia Capital]] — via [[Peak XV Partners]] spinoff
- [[Felicis Ventures]] — Series B lead
- [[Accel]] — Series D/E lead

### Competitors
- [[Google]] — Firebase parent
- [[Amazon]] — AWS Amplify
- [[MongoDB]] — document DB alternative
- [[Neon]] — serverless Postgres competitor
- [[PlanetScale]] — managed MySQL

### Adjacent
- [[Vercel]] — often paired ([[Guillermo Rauch]] is angel investor)
- [[OpenAI]] — [[Kevin Weil]] (CPO) is angel; AI coding tools drive Supabase growth

### Angels
- [[Guillermo Rauch]] — Vercel CEO
- [[Tom Preston-Werner]] — GitHub co-founder
- [[Nat Friedman]] — former GitHub CEO
- [[Kevin Weil]] — OpenAI CPO

### Concepts
- [[Vibe coding]] — growth driver (41% of code now AI-generated)
- [[Open source commoditization]] — strategic dynamic
- [[SaaS]] — business model category

---

Sources:
- [Sacra - Supabase at $70M ARR](https://sacra.com/research/supabase-at-70m-arr-growing-250-yoy/)
- [TechCrunch - Series D announcement](https://techcrunch.com/2025/04/22/vibe-coding-helps-supabase-nab-200m-at-2b-valuation-just-seven-months-after-its-last-raise/)
- [Fortune - Series D exclusive](https://fortune.com/2025/04/22/exclusive-supabase-raises-200-million-series-d-at-2-billion-valuation/)
- [Supabase official site](https://supabase.com/)
- [GitHub - supabase/supabase](https://github.com/supabase/supabase)

*Created 2026-01-14*
