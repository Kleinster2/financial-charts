# Movers Screening Logic

`/morning-scan` runs the sigma screen plus three audit scripts in parallel. The screen alone misses three structural failure modes; the audits exist to catch them.

## Three-trigger sigma screen

Post the May 7, 2026 Chime / HawkEye 360 / Kalshi misses, `quick_movers.py` fires on any of:

| Trigger | Threshold | What it catches |
|---|---|---|
| Standard sigma | ≥2.5σ beta-adjusted | Most material moves on liquid names |
| High-vol sigma | ≥2.0σ if idiosyncratic vol > 50% | Recent IPOs and small-cap fintechs with wide vol bands |
| Absolute backstop | ≥6.0% raw move | Borderline-sigma names (e.g., CHYM -7.5% / -2.1σ on May 7) |

Default invocation: `python scripts/quick_movers.py` (no args — the flag-set above is the default). Each output row shows which trigger fired in the trailing "Trigger" column.

## Three audit scripts (parallel to the sigma screen)

These address structural failure modes from May 7, 2026:

### 1. Ticker audit

```
python scripts/audit_vault_tickers.py --only-gaps
```

Catches actor notes that mention NYSE/NASDAQ tickers in the body but don't expose them in `aliases:`. Those notes are Phase-0-invisible — the sigma screen never sees the ticker.

[[Chime]] had this gap on May 7 (CHYM mentioned in body, not in aliases).

### 2. IPO debut tracker

```
python scripts/ipo_debut_tracker.py --tickers TICK1 TICK2 --scan-stale-private
```

- Pass any candidate IPO tickers from the day's news scan.
- Scans vault for `#private` notes whose body mentions a NYSE/NASDAQ ticker pattern (likely IPO'd, status stale).

[[HawkEye 360]] May 7 IPO would have surfaced via `--tickers HAWK`.

### 3. Private capital watch

```
python scripts/ipo_debut_tracker.py --private-watch
```

Shows last funding round + age for ~30 tracked pre-IPO actors (Kalshi, Anthropic, OpenAI, Stripe, SpaceX, xAI, Cursor, etc.). Highlights rounds older than 120 days as candidates for fresh-activity web search.

[[Kalshi]] $22B Series F (May 7) would have surfaced via `--private-watch` (last round Dec 2025 / 5 months stale → flag for verify).

## Fallback

If `quick_movers.py` data is stale, refresh first:

```
python update_market_data.py --lookback 5 --assets stocks etfs adrs
```

As of March 2026, `quick_movers.py` reads from `stock_prices_daily` (wide) when DuckDB is unavailable, with a SQLite fallback to `prices_long` (narrow). If both surfaces are stale, refresh before running the screen.

If the script is unavailable entirely, fall back to web search for biggest stock movers and cross-reference any name that moved **±8% or more** against vault actors.

## Output handling

- For every vault actor with a major move: check whether the actor note already covers the catalyst. If not, **auto-add to the candidate list** with highest priority, regardless of which news source is being scanned later in the day.
- Present in the briefing as **"🔴 Major mover — vault actor needs update"** at the top of the candidate table.
- **Subsector dispersion**: when multiple vault actors in the same sector move, report dispersion by subsector in the daily note. The dispersion is the insight — it reveals what the market is actually pricing.

## Why three triggers, not one

A single sigma threshold is brittle:

- Pure 2.5σ misses borderline-but-material moves on names with stretched vol bands (the CHYM case — fintech IPO with wide idiosyncratic vol).
- Pure percent threshold (the old ±8%) ignores per-stock volatility — a 3% move on a low-vol industrial can be a 4σ event, and an 8% move on a volatile biotech might be routine.

The 2.5σ-standard + 2.0σ-high-vol + 6%-absolute combination is calibrated to the specific failure modes that have actually surfaced in this vault, not to a generic statistical principle. Revisit thresholds only when new failure cases motivate the change.
