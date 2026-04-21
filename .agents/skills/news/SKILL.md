---
name: news
description: "Full daily news ingestion pipeline: volatility-aware mover cross-check (quick_movers, fallback +/-8%), 8-analyst watchlist, newsletter scan, source discovery with 48h date gate, article ingestion with entity linking and compliance, earnings calendar check, and downstream impact analysis. Use whenever the user mentions news, daily sweep, market movers, what happened today, updating the vault from articles, ingesting Bloomberg/Reuters/FT/WSJ, checking analyst commentary, or asks about significant stock moves. Also triggers on /news."
---

# Daily News Ingestion

Ingest news articles into the Obsidian vault. Sources: Bloomberg, Reuters, FT, WSJ, or whatever the user specifies.

**Before any vault edit**: read `CLAUDE.md` in the vault root.

**Run ALL 5 phases on every invocation**, even when the user specifies a narrow source or sector. A user asking "check Reuters for energy news" still needs the movers cross-check (Phase 0), analyst scan (Phase 0.5), earnings check (Phase 3), and downstream impact (Phase 4). The phases exist because humans forget to ask for them.

## Phase 0: Major Movers Cross-Check (NEVER SKIP)

Before looking at any articles, check yesterday's/today's major stock movers against existing vault actor notes.

1. Preferred path: run `python scripts/quick_movers.py` to get vault actors with statistically unusual moves (>=2.5 sigma, 60-day rolling volatility). This is better than a fixed +/-8% threshold because it adjusts for each stock's normal volatility. A 3% move on a low-vol name can matter more than an 8% move on a volatile one.
2. If the script's data is stale, run `python update_market_data.py --lookback 5 --assets stocks etfs adrs` first.
3. As of March 2026, `quick_movers.py` reads from the wide table (`stock_prices_daily`). If that table is stale but `prices_long` has fresh data, use the narrow table directly.
4. If the script is unavailable or still stale, fall back to web search for biggest stock movers and cross-reference any name that moved **+/-8% or more** against vault actors.
5. For every vault actor that had a major move:
   - Check if the actor note already covers the catalyst.
   - If not, **auto-add it to the candidate list** with highest priority, regardless of which news source is being scanned.
6. Present these as **"🔴 Major mover — vault actor needs update"** at the top of the candidate table.
7. **Subsector dispersion**: When multiple vault actors in the same sector move, report dispersion by subsector in the daily note. The dispersion is the insight, it reveals what the market is actually pricing.

This prevents missing stories like IBM -13% that were not on a chosen source's article list but still mattered to the vault.

## Phase 0.25: Newsletter / Substack Check (NEVER SKIP)

Check tracked newsletters and Substacks for new posts in the last 48 hours. These are high-signal, low-noise sources that often publish analysis before or instead of mainstream outlets.

| Publication | URL | Focus |
|-------------|-----|-------|
| **Vizier Report** | https://vizier.report | Middle East, Iran, strategic analysis |
| **Robin J. Brooks** | https://robinjbrooks.substack.com | Macro, trade flows, energy markets, AIS shipping data |
| **Chips and Wafers** | https://chipsandwafers.substack.com | Semiconductor equipment, test ecosystem, packaging |
| **Ideas in Development** | https://ideasindevelopment.substack.com | Development economics, AI + emerging markets |
| **Jason's Chips** | https://jasonschips.substack.com | Semiconductor technology primers, packaging, process nodes |
| **Jimi Finance** | https://jimifinance.substack.com | Taiwan/Asia semi analysis, ASIC test, AI chip supply chain |
| **Sergey Vakulenko** | https://svakulenko.substack.com | Russian oil/energy sector, upstream economics, OPEC+ |
| **Zero to Pete** | https://www.zerotopete.com | AI tools, coding workflows, founder/operator lessons |
| **Gianluca Benigno** | https://gianlucabenigno.substack.com | Central bank policy, monetary economics, inflation, oil/geopolitics |
| **Escalation Trap** | https://escalationtrap.substack.com | Conflict escalation dynamics, Iran war analysis, strategic patterns |
| **Chartbook** | https://adamtooze.substack.com | Macro history, geopolitics, financial crises |
| **Shanaka Anslem Perera** | https://shanakaanslemperera.substack.com | Macro, development economics, inference economics, structural fractures |
| **Alex Epstein** | https://alexepstein.substack.com | Energy policy, fossil fuels, energy security |
| **FT Alphaville** | https://ftav.substack.com | Markets, financial analysis, macro |
| **Alap Shah** | https://alapshah1.substack.com | AI infrastructure, semiconductor strategy, intelligence economics |
| **Quiet Capital** | https://michaelxbloch.substack.com | AI investment themes, intelligence economics |
| **Recode China AI** | https://recodechinaai.substack.com | China AI industry, labor displacement, tech policy |
| **The Register** | https://www.theregister.com/security/ | Cybersecurity, AI infrastructure breaches, supply chain attacks |
| **BleepingComputer** | https://www.bleepingcomputer.com/news/ | Data breaches, ransomware, vulnerability disclosures |
| **David Oks** | https://davidoks.blog | Economic development, tech and society, AI and labor |
| **Critical Supply** | https://substack.com/@criticalsupply | Trade policy, supply chains, EU-US-China economic relations |
| **Gridlocked and Unlocked** | https://gridlockedunlocked.substack.com | Power markets, grid modernization, data center electricity demand |
| **Carolyn Kissane (Energy Common Sense)** | https://carolynkissane157206.substack.com | Energy geopolitics, oil/LNG markets, energy security |
| **Aurelion Research** | https://aurelionresearch.substack.com | Independent equity research, chemicals, fertilizers, oil |
| **Inverteum Capital** | https://blog.inverteum.com | Long-short market commentary, geopolitics, China/Taiwan |
| **Principled Perspectives** | https://raydalio.substack.com | Global macro, world order, debt cycles, AI |
| **China Uncensored** | https://chinauncensored.substack.com | Chinese politics, economy, CCP analysis |
| **The More Things Change** | https://normanricklefs.substack.com | History, geopolitics, complex systems, military strategy |
| **ChinaTalk** | https://www.chinatalk.media | China tech, US policy, war, policymaker interviews |
| **Hey AI News** | https://heyainews.substack.com | AI news, robotics, LLMs |
| **War and Peace** | https://markurban.substack.com | Defence, diplomacy, intelligence, military history |
| **ENERGY Pipeline** | https://fgermini.substack.com | Brazil energy, oil trading, gas markets, power dynamics |
| **Jared Bernstein** | https://econjared.substack.com | US economic and fiscal policy, crypto regulation, budgeting |

For each:
1. Check the archive/homepage for posts in the last 48 hours.
2. Cross-reference against vault daily notes and relevant actor/concept notes.
3. If new material is found, add it to the Phase 1 candidate table with source and date.
4. Newsletter posts often contain charts and data tables, always extract and embed per vault rules.

**Maintenance**: This list is mirrored in the OpenClaw workspace (`~/clawd/TOOLS.md`). When adding or removing a source, update both locations.

## Phase 0.5: Key Analyst Check (NEVER SKIP)

After the major movers cross-check, search for new commentary from these analysts.

| Analyst | Firm | Focus | Search pattern |
|---------|------|-------|----------------|
| [[Helima Croft]] | [[RBC Capital]] | Oil, MENA, energy geopolitics | `"Helima Croft" OR "RBC commodities"` |
| [[Jeff Currie]] | [[Carlyle]] | Commodities supercycle, metals, macro regime | `"Jeff Currie" OR "Currie Carlyle"` |
| [[Natasha Kaneva]] | [[JPMorgan]] | Commodities | `"Natasha Kaneva" OR "JPMorgan commodities"` |
| [[Francisco Blanch]] | [[Bank of America]] | Commodities, oil | `"Francisco Blanch" OR "BofA commodities"` |
| [[Lyn Alden]] | Independent | Macro, fiscal dominance, energy-to-rates | `"Lyn Alden"` |
| [[Zoltan Pozsar]] | Ex Uno Plures | Rates, monetary plumbing, petrodollar | `"Zoltan Pozsar" OR "Ex Uno Plures"` |
| [[Ed Yardeni]] | Yardeni Research | Equity strategy, macro | `"Ed Yardeni" OR "Yardeni Research"` |
| [[Mike Wilson]] | [[Morgan Stanley]] | US equity strategy | `"Mike Wilson" OR "Morgan Stanley equity strategy"` |

For each:
1. Search for appearances in the last 48 hours, CNBC, Bloomberg, FT, research notes, interviews.
2. Check against the actor note to see if the commentary is already captured.
3. If new material is found, add it to the candidate table with source and date.
4. Ingest quotes, data points, and price calls into both the analyst note and the relevant concept/event notes.

## Phase 1: Source Discovery

1. Search for recent articles from the specified source, focused on vault areas: AI, semiconductors, energy, China, robotics, macro, SaaS, markets, cybersecurity/data breaches at AI companies, and AI infrastructure or supply-chain security.
2. **Date gate**: check the publication date of every candidate. Only include articles from the last 48 hours. If an older article appears in a sidebar or recommendation module, skip it unless the user specifically requests historical ingestion.
3. Check each candidate against the vault, search daily notes and actor notes for existing coverage.
4. Present the candidate list to the user as a numbered table:

| # | Article | Date | Status |
|---|---------|------|--------|
| 1 | Title | Feb 8 | New |
| 2 | Title | Feb 7 | Already in 2026-02-07.md |

**Always include publication dates so the user can spot strays.**

Wait for the user to select which articles to ingest.

## Phase 2: Article Ingestion

For each selected article:

### Read & Extract
1. Navigate to the article and extract full text via `get_page_text`.
2. If extraction fails, use browser screenshots, visual scrolling, or page-source fallbacks.
3. Capture key data points, short quotes, tables, and named entities.

### Update Vault
1. **Daily note** (by article publication date, not ingestion date):
   - Add a section with summary, data tables, and thesis implications.
   - Add source URLs to the `## Sources` section.
   - Create the daily note if it doesn't exist yet.
2. **Actor/concept notes**:
   - Update existing notes with new data, never replace, always add.
   - Check for existing notes before creating: `python scripts/check_before_create.py "Name"`.
   - Create stubs for new entities when needed.
3. **Entity linking**:
   - Every entity gets a `[[wikilink]]`.
   - Check for existing notes and aliases before linking.

### Event Notes
4. When a single news event touches **3+ actor notes**, create a dedicated event note in `Events/` with the full detail. Actor notes should carry short summaries plus a `[[link]]` to the event note.
5. Always run `python scripts/check_before_create.py "Event Name"` before creating.

### Compliance
6. Run `python scripts/check_note_compliance.py <file> --fix` on every modified note.
7. Fix errors before moving on. Warnings such as dead links are expected for new notes.

## Phase 3: Earnings Check

**Always check the earnings calendar when doing daily news.** Major earnings move markets and affect actors.

1. Search for `"earnings reports week [date]"` or check Yahoo Finance's calendar.
2. Capture all relevant earnings, not just the focus sector.
3. For each earnings report:
   - Add a section to the actor note with key metrics, guidance, and stock reaction.
   - Add it to the daily note.
   - Note any CEO changes, guidance surprises, or strategic shifts.
4. Do not wait for the next trading day, search for prior after-hours and pre-market results too.

Earnings that matter beyond focus areas:
- Mag 7
- Major financials
- Consumer bellwethers
- Industrial and macro signal names

## Phase 4: Downstream Impact Check

After ingesting articles that update a crisis or event note, check for untracked second-order effects.

1. Look for a `## Watch for` section in the updated note.
2. If one exists, scan each untracked item against the articles just ingested and run a quick web search for the top 2-3 most likely items.
3. If new coverage is found, ingest it and update the watch-list status.
4. If no watch list exists but the note covers an ongoing crisis, war, supply shock, or policy shift, ask: *What downstream effects of this story haven't we tracked yet?* Then propose a watch list.

This prevents the vault from tracking only the first-order supply shock while missing the demand response, consumer impact, or industrial second-order effects.

## Rules

- **Copyright**: never reproduce 20+ word chunks from articles. Short quotes only, under 15 words.
- **Cause -> context -> consequence**: for breaking news, research why before analyzing impact.
- **No info outside note**: all research findings go in the vault, not just chat.
- **Numbers matter**: use exact figures with sources.
- **Never replace, always add**: augment existing content.
- **No ephemeral standalone notes**: data releases and earnings previews/calendars are data points, not standalone notes. Fold them into the relevant actor, concept, or existing event note.
- **Charts must live in notes**: never save them without embedding.
- **Every chart needs a data table**: the reader should see the underlying numbers.
