# Note Completion Checklist

Run before marking any vault note "done" (actors, concepts, events, theses, sectors).

## 1. Run automated check FIRST

```bash
python scripts/check_note_compliance.py investing/Actors/NewNote.md
```

Fix all errors before proceeding to manual checks.

**Automated checks:**
- Frontmatter (exists, has aliases)
- Dead links (wikilinks to non-existent notes)
- Missing price/fundamentals charts
- Missing chart captions
- Missing Related section
- Missing Quick stats section
- Missing Leadership section with CEO
- Missing historical financials (10-year for public)
- Missing cap table (private)
- Funding rounds table — exists, complete (no gaps/catch-all rows), individual rounds listed
- Missing ownership % estimates table (private)
- Table formatting (blank lines before tables)

**Exit codes:** 0 = pass, 1 = errors

---

## 2. Manual checks

These cannot be automated. Review each one.

### Currency

- [ ] **Web search for recent news** — verify note reflects current reality
- [ ] Key facts are current (not stale by weeks/months)
- [ ] Numbers are latest available (MAU, revenue, valuations, ownership stakes)

### Completeness

- [ ] **No info left outside note** — all research findings go in the note, not just conversation
- [ ] Board table exists (companies) — Chair, independent vs insider, notable affiliations
- [ ] Principals table exists (funds) — PE/VC: founding partners; sovereign funds: CEO, CIO; hedge funds: founder, PM

### Specificity

- [ ] **No lazy shorthand** — "American-owned" needs: who owns what %, board composition, economic rights vs equity
- [ ] Ownership changes include: exact stakes, governance, economic rights, compliance concerns
- [ ] Revenue/valuation claims have exact figures, not "significant" or "major"
- [ ] Partnerships/deals specify: terms, duration, exclusivity, economics

### Charts

- [ ] Price chart has actor + peers/benchmark (not just actor alone)
- [ ] **Open and verify chart images** — confirm legend matches caption
- [ ] **No chart titles** — legend suffices
- [ ] **Research major moves** — don't fabricate explanations; web search actual causes
- [ ] Link captions to vault notes

### Links

- [ ] Every entity in tables is `[[wikilinked]]`
- [ ] Every entity in body text is `[[wikilinked]]`
- [ ] Related section includes all linked entities

Quick link audit:
```bash
grep -oE '\b[A-Z][a-z]+\b' note.md | sort -u
```
Compare against wikilinks. If proper noun appears without `[[brackets]]`, fix it.

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
| Crypto | Bitcoin, Ethereum, token economics, unlock schedules |
| Semiconductors | Foundry, fabless, memory, logic |
| AI infrastructure | Training, inference, GPUs |
| Banking | Deposits, lending, capital ratios |

**When exploring a domain:**
1. Search what exists
2. Enumerate what must exist
3. Check the gap
4. Flag missing

Don't confuse infrastructure with foundations. Coinbase is crypto infrastructure; Bitcoin is a crypto foundation.
