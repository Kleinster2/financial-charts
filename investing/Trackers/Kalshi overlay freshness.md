#tracker #kalshi #prediction-markets

**Kalshi overlay freshness** — Tracker for [[Kalshi]] markets that have been written into durable vault notes. The operating rule is simple: Kalshi prices are expiring overlays, not timeless facts.

---

## Operating rule

Every Kalshi section in a durable note should carry:

| Field | Purpose |
|-------|---------|
| Market or event ticker | Makes the source reproducible. |
| API URL | Lets the watchlist refresh the same market. |
| Read date | Separates "market-implied as of date" from current truth. |
| Bid / ask / last | Prevents stale midpoints from becoming prose facts. |
| Volume / open interest | Distinguishes liquid signal from novelty contracts. |
| Close or resolution date | Tells when the overlay should become historical evidence. |

---

## Refresh workflow

The live state is in `kalshi_watchlist.yml`. Run:

```bash
python scripts/refresh_kalshi_watchlist.py
python scripts/refresh_kalshi_watchlist.py --refresh
python scripts/refresh_kalshi_watchlist.py --refresh --update-state
```

Offline mode flags stale `last_read` dates. `--refresh` fetches Kalshi and flags representative contract moves above the configured threshold. `--update-state` records a reviewed snapshot back into the YAML file after the daily note has captured the alert.

---

## Cadence

| Cadence | Stale after | Use case |
|---------|-------------|----------|
| Daily | 2 days | Weekly commodities, CPI, rates, labor releases. |
| Weekly | 8 days | Policy, macro, AI/labor, tariff, and regulatory overlays. |
| Monthly | 35 days | Long-dated thematic markets such as IPO timing, AI products, geopolitical tails, and Big Tech antitrust. |
| Quarterly | 100 days | Slow structural markets where the note already frames the value as historical color. |

---

## Promotion rule

Do not auto-rewrite every touched note. The watchlist should first create a daily-note alert: stale, material move, status change, or finalized market. Only fold the update into the durable note when the move changes the note's live read-through.

When a market resolves, rewrite the note section from live-pricing language to historical evidence:

| Before resolution | After resolution |
|-------------------|------------------|
| "Kalshi prices X at 33c" | "On May 20, 2026, traders priced X at 33c; the market resolved No on DATE." |
| Current overlay | Forecast audit / signal quality |

---

## Related

- [[Kalshi]] — platform actor
- [[Prediction markets]] — concept
- [[Valve]] — first Steam Machine price overlay that triggered this tracker
- [[US-China tariffs]] — tariff markets now tracked through the watchlist
- [[Fed independence]] — institutional-risk markets now tracked through the watchlist
