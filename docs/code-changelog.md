# Code Changelog

Project evolution journal — what changed, why, and how.

Newest entries first.

---

## 2026-03-18 — Intraday chart blueprint

**Files:** `charting_app/intraday_routes.py` (new, 267 lines), `charting_app/app.py`

**Change:** Added two new endpoints for sub-daily charting:
- `/api/chart/intraday` — line chart overlay of 30-minute candles, supports ETFs and Hyperliquid perps (`HL:` prefix routes to `perp_candles` table, everything else to `intraday_candles`)
- `/api/chart/intraday/funding` — funding rate chart for Hyperliquid perps, converts raw hourly rates to basis points, drops outliers >10 bps/hr

Both endpoints reuse the existing Playwright + `chart_render.html` pipeline with an `isIntraday: true` flag. Follows the blueprint pattern from the March refactor.

**Motivation:** Perpetuals dashboard work needed intraday price overlays (ETF vs perp) and funding rate visualization. Daily candles too coarse for funding rate analysis.

---

## 2026-03-16 — Narrow-format migration (Phases 0–2)

**Files:** `scripts/add_ticker.py`, `scripts/download_all_assets.py`, `charting_app/helpers.py`, multiple route files

**Change:** Migrated price storage from wide format (`stock_prices_daily` — one column per ticker) to narrow/long format (`prices_long` — ticker as a row field). Three phases:
1. Phase 0: Created `prices_long` table, backfilled from wide table
2. Phase 1: `add_ticker.py` writes to narrow table when `USE_NARROW=1`
3. Phase 2: `download_all_assets.py` flipped to write narrow-first; read path defaults to `USE_NARROW=1`

**Motivation:** Wide table hit ~2000 columns — SQLite practical limit. Every new ticker required an `ALTER TABLE ADD COLUMN`. Narrow format scales indefinitely.

---

## 2026-03-16 — `quick_movers`: sigma-based detection + DuckDB backend

**Files:** `scripts/quick_movers.py`

**Change:** Two improvements:
1. Replaced fixed 8% threshold with sigma-based detection — each ticker's move is measured against its own rolling standard deviation, surfacing unusual moves even for low-vol names
2. Added DuckDB backend with auto-selection (uses DuckDB if available, falls back to SQLite)

**Motivation:** Fixed threshold missed meaningful moves in low-vol stocks and flagged routine moves in high-vol names. DuckDB speeds up the scan across the full ticker universe.

---

## 2026-03-16 — `/replicate` skill + replication utilities

**Files:** `.claude/skills/replicate/SKILL.md` (new), `scripts/replicate_fund.py` (new)

**Change:** Added a skill and shared utilities for ETF/fund replication analysis — maps holdings to available tickers, builds replicating portfolios, compares tracking error. Used for ALLW and RPAR analysis.

---

## 2026-03-15 — Cross-vault link detection in compliance checker

**Files:** `scripts/check_note_compliance.py`

**Change:** Added detection of cross-vault `obsidian://` URI links. The compliance checker now recognizes these as valid links rather than flagging them as dead. Includes false-positive filtering for URL-encoded vault paths.

**Motivation:** After adding 20 cross-vault links (investing ↔ technologies), the compliance checker was treating them all as dead links, generating noise.

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
