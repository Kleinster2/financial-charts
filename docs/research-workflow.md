# Research Workflow

## Sourcing Standards

**Prefer official sources for hard data:**

| Data type | Primary source | Fallback |
|-----------|----------------|----------|
| Revenue, Net Income, EPS | 10-K, 10-Q | Earnings releases |
| Employee headcount | 10-K (annual), proxy | News (flag as estimate) |
| Segment breakdown | 10-K, 10-Q | Investor presentations |
| Guidance | Earnings calls, 8-K | News coverage |
| Ownership/cap table | Proxy (DEF 14A), 13-F | News (flag as estimate) |

Non-filing sources: note it — "~210k employees (company website, Jan 2026)"

**SEC EDGAR shortcuts:**
- All filings: `https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=TICKER&type=10-K`
- Recent 10-K: search `"[company] 10-K 2024 filetype:pdf"`

---

## Daily News Search

**CRITICAL: Use exact date format.** `"January 27 2026"` not `"January 2026"`.

| Category | Search terms |
|----------|--------------|
| **Market movers** | "biggest stock gainers losers [date]" |
| **Macro** | "markets treasury dollar Fed [date]" |
| **Semiconductors** | "semiconductor chip memory [date]" |
| **AI** | "AI artificial intelligence [date]" |
| **China** | "China economy tech [date]" |
| **Asia semis** | "Japan Korea semiconductor [date]" |
| **Trade/Policy** | "tariffs trade regulation policy [date]" |
| **Defense** | "Pentagon military defense tech [date]" |
| **Energy** | "energy power grid nuclear [date]" |
| **Europe** | "Europe economy tech [date]" (weekly) |
| **Earnings** | Check calendar |

**Market movers catch what categories miss.** Corning +17% on Meta deal wouldn't appear in "semiconductor" searches.

**Don't miss:** China domestic news (GDP, NDRC, stimulus) — often absent from US-focused searches.

---

## Verify Before Reporting

**Summary articles recycle recent news as "context."** This pollutes results.

**For any major deal/announcement:**
1. Search `"[company] [deal] announcement date"` to verify timing
2. If older than 3 days, classify as "Recent" not "Today"

**Present news in two sections:**

| Section | Criteria |
|---------|----------|
| **Confirmed Today** | Verified same-day (earnings, FOMC, stock moves with %) |
| **Recent (Not Today)** | Announced earlier — include actual date |

**Red flags for recycled news:**
- Acquisitions/deals (often announced weeks ago)
- "Landmark" or "historic" framing
- Round-number valuations without transaction details

---

## Follow Up on Big Movers

**Any stock move >10% needs a "why" search.**

1. Search `"[ticker] stock why up/down [date]"`
2. Identify catalyst (earnings, deal, upgrade, macro)
3. Include in report with context

---

## Earnings Searches

**General searches miss forward guidance.** Run two searches:

1. General: `"[company] earnings [date]"` — headline results
2. Guidance: `"[company] Q1/FY guidance [date]"` — forward estimates

Forward guidance often moves stocks more than backward-looking beats.

---

## Processing New Information

**Every piece of news needs an atomic home — daily notes are never the only location.**

1. **Check existing notes first** — search vault before web
2. **Find the right home** — actors taking actions, not catch-all concepts
3. **Regional actors stay high-level** — specific news → specific actors
4. **Always update daily notes** — use event date, not article date
5. **Check for events** — M&A, bankruptcy, IPO → create Event note
6. **Recognize systemic events** — if same news hits 2+ actors, create Concept/Event note first
7. **Trace repercussions** — how did markets react?

### Tracing Market Repercussions

| Asset class | What to look for |
|-------------|------------------|
| Treasuries | Yield curve shifts (2Y, 10Y, 30Y) |
| Equities | Index moves, sector rotation |
| FX | Dollar, relevant currency pairs |
| Commodities | Gold, oil if macro-relevant |
| Sector ETFs | Rate-sensitive (XLF, XLU, XLRE) |

**Process:**
1. Update primary actor note(s)
2. Search for market reaction
3. Add to daily note Markets section
4. Add to Journal sections of affected concept/sector notes

### Systemic vs Company-specific

| Signal | Action |
|--------|--------|
| Same news hits 2+ companies | Create concept/event note first |
| Policy/regulatory change | Concept note for the policy |
| Sector-wide selloff | Concept note for the catalyst |
| Macro event | Concept note |

Actor notes answer "how does this affect THIS company specifically?" — don't re-explain sector-wide context.
