---
name: deepdive
description: "Deep-dive entity research and note creation pipeline. Use for any entity the user wants a comprehensive vault note on — companies, people, concepts, countries, products. Triggers on /deepdive ENTITY or when the user names an entity and wants thorough research + vault note creation/expansion. The skill adds SEC filing protocols, full chart sets, stale-reference scanning, and entity-type branching that CLAUDE.md's general vault instructions don't sequence."
---

# Deep-Dive Entity Research

Create or expand a comprehensive vault note. Usage: `/deepdive ENTITY NAME`

CLAUDE.md already defines note structure (Synopsis, Evolution, Core thesis, etc.), formatting rules, and vault conventions. This skill does NOT repeat those — it adds the research protocols, data integration steps, and quality gates that CLAUDE.md doesn't sequence.

## Phase 1: Vault Reconnaissance

Most entities already have some vault presence. The default path is expansion, not creation.

1. **Hard gate** — check for existing notes and aliases:
   ```bash
   python scripts/check_before_create.py "ENTITY NAME"
   ```

2. **Vault search** — find all mentions across the investing vault:
   ```bash
   "/c/Users/klein/AppData/Local/Programs/Obsidian/Obsidian.com" vault=investing search query="ENTITY NAME"
   ```
   Also search by ticker, product names, key people — anything that might surface references the entity name misses.

3. **Geopolitics vault search** — if the entity touches defense, trade, sanctions, diplomacy, energy security, or industrial policy:
   ```bash
   "/c/Users/klein/AppData/Local/Programs/Obsidian/Obsidian.com" vault=geopolitics search query="ENTITY NAME"
   ```
   Note specific counterpart notes for cross-vault linking later.

4. **Branch on what you find:**
   - **Full note exists** → read it, assess gaps against the gold standard (see `investing/Actors/Block.md` for actor notes), then expand. Tell the user what's there and what's missing.
   - **Stub exists** → read it, proceed to Phase 2 to expand.
   - **Nothing exists** → proceed to Phase 2 to create from scratch.

## Phase 2: Research (entity-type-aware)

### All entity types:
- Multiple web searches to triangulate: identity, recent developments, hard numbers
- Search the vault for related concepts, sectors, and themes — not just the entity itself but adjacent ideas
- Gather and attribute hard numbers. No "significant" or "substantial."

### Public companies — additional steps:
- **SEC filings** — always pull the latest 10-K and most recent 10-Q:
  ```bash
  python scripts/parse_sec_filing.py TICKER --type 10-K --save /tmp/TICKER-10k.txt
  python scripts/parse_sec_filing.py TICKER --type 10-Q --save /tmp/TICKER-10q.txt
  ```
  These are primary sources. Extract revenue segments, risk factors, insider transactions, guidance language.

- **Database setup** — check if ticker exists, add if missing, ensure fundamentals are loaded:
  ```bash
  python scripts/add_ticker.py TICKER
  python fetch_fundamentals.py TICKER
  ```

- **Price freshness** — update before generating charts:
  ```bash
  python update_market_data.py --lookback 10 --assets stocks
  ```

- **Price verification** — before writing any stock price into the note, verify against actual DB closing prices. Never trust secondary sources for price data.

### Private companies — additional steps:
- Search for funding rounds, valuations, investor names
- No SEC filings, no ticker to add, no price chart
- The funding rounds table and cap table estimates replace financial data sections

### Concepts — structural differences:
- Route to `investing/Concepts/`, not `Actors/`
- Use Synthesis (not Synopsis) — interpretive framing of where the concept stands now
- No Evolution section — organize by analytical dimension (pathways, economics, regulatory, demand)
- No ticker, no Quick stats with financial metrics — use concept-relevant metrics (production volumes, cost curves, mandate timelines)
- The note's value is connecting actors to a theme — wikilink every relevant company, regulator, and policy

## Phase 3: Write the Note

CLAUDE.md defines note structure, formatting, and quality standards in detail. Follow those. Key reminders the skill adds:

- **If expanding an existing note**: use Edit operations to add/update sections. Preserve all existing content. Never overwrite — augment.
- **If the note is mature enough** (3+ substantive sections, 100+ lines): add an Analysis section. This is interpretation derived strictly from facts in the note — structural tensions, open questions, what the data reveals that isn't obvious. See CLAUDE.md's vault philosophy: "The vault earns its value by being more thorough than what's freely available."
- **Quotes**: extract and date every relevant quote from sources. Format: `[[Firm]] analyst Name (Feb 13): *"quote text"*`

## Phase 4: Charts (public companies only)

Generate the full chart set — not just a price chart. Each chart reveals something different.

1. **Peer comparison price chart** (required) — always compare to 2-3 peers, never solo:
   ```
   /api/chart/lw?tickers=TICKER,PEER1,PEER2&start=...&normalize=true&primary=TICKER
   ```
   Save as `ticker-vs-peer1-price-chart.png`. Choose peers that illuminate the investment question.

2. **Fundamentals chart** (required if fundamentals are in DB):
   ```
   /api/chart/image?ticker=TICKER&metrics=revenue,net_income&start=...
   ```

3. **Sankey diagram** (required if income statement data exists in DB):
   ```
   /api/chart/sankey?ticker=TICKER
   ```
   Save as `ticker-sankey.png`. Caption format: fiscal year, revenue → net income, net margin, major cost buckets as % of revenue.

4. **Waterfall chart** (if income statement data exists):
   ```
   /api/chart/waterfall?ticker=TICKER
   ```
   Save as `ticker-waterfall.png`

Verify every chart with `wc -c` — files under 1KB are errors, not PNGs. Embed each in the note with an italic interpretation caption and a corresponding data table.

Skip charts entirely for private companies and concepts. For concepts, harvest source charts (IEA forecasts, industry reports) if found during research.

## Phase 5: Stubs and Vault Maintenance

1. **Compliance check**:
   ```bash
   python scripts/check_note_compliance.py investing/TYPE/ENTITY.md
   ```

2. **Create stubs** for every dead-linked entity. Run `check_before_create.py` for each before creating — don't create stubs for entities that already have notes. Parallelize with sub-agents.

3. **Stale reference scan** — search the vault for other notes that mention this entity:
   ```bash
   "/c/Users/klein/AppData/Local/Programs/Obsidian/Obsidian.com" vault=investing search query="ENTITY NAME"
   ```
   Check if any of those notes contain stale data (old valuations, outdated revenue figures, wrong status). If you find stale references, update them. This is vault maintenance — data consistency across the entire vault matters.

## Phase 6: Daily Note

1. Confirm today's date: `date +%Y-%m-%d`
2. Update today's daily note (`investing/Daily/YYYY-MM-DD.md`):
   - `## Notes created/expanded`: every note created or expanded, with brief description
   - `## Edit log`: every file touched
3. Create the daily note with `#daily` tag if it doesn't exist

## Phase 7: Final Compliance and Cross-Vault

1. Re-run compliance on the main note. Fix any remaining errors.
2. **Cross-vault gate**: Does this entity warrant a geopolitics vault counterpart? Defense, sanctions, trade policy, diplomatic precedent, infrastructure competition → flag to user. Don't skip silently.
3. **Concept extraction**: Scan for terms that deserve their own concept note. If a reader would benefit from a dedicated note on a term used in this note, create and wikilink it.
