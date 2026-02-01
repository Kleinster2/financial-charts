# Actor Note Completion Checklist

Run before marking any public actor note "done" (companies AND ETFs).

## Pre-flight (MUST DO FIRST)

- [ ] **Web search for recent news** — verify note reflects current reality
- [ ] Key facts are current (not stale by weeks/months)
- [ ] Numbers are latest available (MAU, revenue, valuations, ownership stakes)

## Specificity

- [ ] **No lazy shorthand** — "American-owned" needs: who owns what %, board composition, economic rights vs equity
- [ ] Ownership changes include: exact stakes, governance, economic rights, compliance concerns
- [ ] Revenue/valuation claims have exact figures, not "significant" or "major"
- [ ] Partnerships/deals specify: terms, duration, exclusivity, economics

## Leadership & Board (companies only)

- [ ] **Leadership table** — CEO, CFO (required for public/PE-backed), other C-suite
- [ ] **Board table** — Chair, independent vs insider, notable affiliations
- [ ] All names wikilinked if they have notes

## Principals (funds & asset managers)

- [ ] Leadership table with: name, role, background
- [ ] PE/VC: founding partners, managing partners
- [ ] Sovereign funds: CEO, CIO, sector heads
- [ ] Hedge funds: founder, PM, key analysts

## Charts

- [ ] Price chart exists with `primary=TICKER` (actor always blue)
- [ ] Price chart has actor + peers/benchmark
- [ ] Fundamentals chart exists (companies only, not ETFs)
- [ ] **No chart titles** — legend suffices
- [ ] Chart captions mention all tickers shown
- [ ] **Research major moves** — don't fabricate explanations; web search actual causes
- [ ] Link captions to vault notes

## Links

- [ ] Every entity in tables is `[[wikilinked]]`
- [ ] Every entity in body text is `[[wikilinked]]`
- [ ] Related section includes all linked entities

### Quick link audit

```bash
grep -oE '\b[A-Z][a-z]+\b' note.md | sort -u
```

Compare against wikilinks. If proper noun appears without `[[brackets]]`, fix it.

---

## Automated Compliance Check

**REQUIRED:** Run after creating/modifying any actor note:

```bash
python scripts/check_note_compliance.py investing/Actors/NewNote.md
```

**Checks:**
- Dead links (wikilinks to non-existent notes)
- Missing price/fundamentals charts
- Missing chart captions
- Missing Related section
- Missing Quick stats section
- Missing historical financials (10-year for public)
- Missing cap table (private)

**Does NOT check (manual):**
- Currency — is note up to date?
- Specificity — are claims drilled with detail?
- Chart titles — verify no redundant titles

**Exit codes:** 0 = pass, 1 = errors

---

## Vault-wide Orphan Detection

Find terms mentioned frequently without notes:

```bash
python scripts/check_note_compliance.py --orphans --min-mentions 50
```

Scans vault for capitalized terms appearing 50+ times without corresponding notes. Run periodically.

---

## Domain Completeness Check

**Don't just search what exists — ask what MUST exist.**

For any domain query, enumerate canonical entities:

| Domain | Must-have notes |
|--------|-----------------|
| Crypto | Bitcoin, Ethereum |
| Semiconductors | Foundry, fabless, memory, logic |
| AI infrastructure | Training, inference, GPUs |
| Banking | Deposits, lending, capital ratios |

**When exploring a domain:**
1. Search what exists
2. Enumerate what must exist
3. Check the gap
4. Flag missing

Don't confuse infrastructure with foundations. Coinbase is crypto infrastructure; Bitcoin is a crypto foundation.
