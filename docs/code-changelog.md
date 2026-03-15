# Code Changelog

Structured log of code changes: what changed, why, how the bug was found, and what was done about it.

Newest entries first.

---

## 2026-03-15 — `check_note_compliance.py`: `_has_tag` ignoring YAML frontmatter tags

**File:** `scripts/check_note_compliance.py`

**Bug:** `_has_tag()` only matched `#hashtag` tokens in note body text. Notes using YAML frontmatter arrays (`tags: [actor, etf]` or `tags:\n  - actor\n  - etf`) — roughly half the vault (~487 inline, ~499 block) — were never matched. This caused `_get_note_type()` to return `"unknown"`, which bailed out at line 90 (`if note_type not in ("actor", "etf", "benchmark"): return issues`), skipping all actor-specific compliance checks: price charts, fundamentals charts, sector correlation, leadership, evolution, synopsis.

**Detection:** Manual compliance check on `ALLW.md` (tags: `[actor, etf, risk-parity, bridgewater]`). The script returned 0 errors / 3 warnings (dead links only). No chart error despite the note having no price chart embed. Investigation traced through `_get_note_type()` → `_has_tag("#etf")` → regex `(?<!\w)#etf(?=\s|$)` which never fires because YAML frontmatter uses bare words without `#` prefix.

**Fix:** Rewrote `_has_tag()` to check two places:
1. Body hashtags (original regex, unchanged)
2. YAML frontmatter `tags:` field — both inline `[a, b, c]` and block (`- item`) formats

Strips the `#` prefix before frontmatter matching. Parses only within `---` fences to avoid false matches in body text.

**Verification:** After fix, `ALLW.md` correctly returns `note_type=etf`, `is_etf=True`, and surfaces `ERROR [chart] ETF missing price chart` plus 16 previously-hidden warnings (missing links, synopsis). Tested against both YAML formats: `ALLW.md` (inline) and `01.AI.md` (block) — both correctly identified as their respective types.

**Blast radius:** Every note in the vault that uses YAML frontmatter tags without body `#hashtags` was previously invisible to type-specific checks. This is a significant fix — many notes may now surface new compliance errors on their next check.

---

## 2026-03-09 — `stock_prices_daily`: date format normalization

**File:** `market_data.db` (data fix, not code)

**Bug:** `stock_prices_daily` contained mixed date formats: `2026-03-04` (date-only) alongside `2026-03-04 00:00:00` (datetime). SQLite treats these as different strings, creating duplicate rows for the same trading day. After pandas datetime parsing, the duplicate index entries caused merge operations to produce NULLs, triggering the update script's integrity check: "SPY was X, now NULL."

**Detection:** `update_market_data.py` integrity check failures. Shortening `--lookback` did not help — the root cause was malformed dates, not download issues.

**Fix:** Normalized all dates to `YYYY-MM-DD HH:MM:SS` format and deleted sparse duplicate rows. Cleaned 2,625 date-only rows + 2,622 duplicate entries. Row count dropped from ~21,871 to ~19,174.

**Verification:** `update_market_data.py --lookback 10` runs cleanly after fix.

---

## 2026-03 — App refactor: monolith to blueprints

**Files:** `charting_app/app.py`, `charting_app/*_routes.py`, `charting_app/helpers.py`

**Change:** Split monolithic `app.py` (~2000+ lines) into 10 blueprint files + shared helpers. `app.py` reduced to ~71 lines (Flask app creation, middleware, blueprint registration).

**Motivation:** File was too large to navigate and modify safely. Route changes risked breaking unrelated endpoints.

**Verification:** Flask test client (`app.test_client()`) smoke tests on all 53 routes. Background `&` processes don't work on Windows/Git Bash, so test client is the standard verification method.
