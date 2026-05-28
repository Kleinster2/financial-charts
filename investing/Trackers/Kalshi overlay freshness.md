#tracker #kalshi #polymarket #prediction-markets

**Prediction-market overlay freshness** — Tracker for [[Kalshi]] and [[Polymarket]] markets that have been written into durable vault notes. The operating rule is simple: prediction-market prices are expiring overlays, not timeless facts.

---

## Operating rule

Every prediction-market section in a durable note should carry:

| Field | Purpose |
|-------|---------|
| Provider | Distinguishes [[Kalshi]]'s CFTC-regulated API from [[Polymarket]]'s Gamma/CLOB stack. |
| Market or event ticker | Makes the source reproducible. |
| API URL | Lets the watchlist refresh the same market. |
| Read date | Separates "market-implied as of date" from current truth. |
| Bid / ask / last | Prevents stale midpoints from becoming prose facts. |
| Volume / open interest | Distinguishes liquid signal from novelty contracts. |
| Close or resolution date | Tells when the overlay should become historical evidence. |

---

## Refresh workflow

The live state is in `kalshi_watchlist.yml` (legacy name, now provider-aware). Run:

```bash
python scripts/refresh_kalshi_watchlist.py
python scripts/refresh_kalshi_watchlist.py --refresh
python scripts/refresh_kalshi_watchlist.py --refresh --update-state
```

Offline mode flags stale `last_read` dates. `--refresh` fetches public provider APIs and flags representative contract moves above the configured threshold. `--update-state` records a reviewed snapshot back into the YAML file after the daily note has captured the alert.

The same watchlist can also define `comparisons` for matching Kalshi/Polymarket thesis legs. Each comparison names two or more tracked contracts and a divergence threshold. The refresh script reports the current spread and raises a `provider-divergence` material alert when the cross-venue gap is large enough to deserve a durable-note reread.

For outcome-slicing markets, do not treat the highest-priced bucket as the forecast. When contracts divide a numeric outcome into bands (for example IPO closing market cap buckets such as `$1.25T-$1.5T`), calculate the 50% cumulative point and linearly interpolate inside the bucket where the cumulative distribution crosses 50%. That interpolated median is the market-implied best prediction guess as of the read date. Individual bucket prices are supporting distribution shape, not the headline estimate. If the market includes a non-numeric outcome such as "no IPO by deadline," cite that probability separately and compute the numeric median conditional on the numeric event happening.

The watchlist supports this through `derived_metrics`:

```yaml
derived_metrics:
  - id: openai-ipo-implied-median-market-cap
    label: OpenAI IPO implied median closing market cap
    method: bands
    percentile: 0.5
    unit: T
    condition: conditional on IPO by Dec. 31, 2026; excludes the no-IPO leg
    bins:
      - slug: will-openais-market-cap-be-between-1pt25t-and-1pt5t-at-market-close-on-ipo-day
        outcome: 'Yes'
        lower: 1.25
        upper: 1.5
```

For threshold ladders such as "market cap above $1T / $2T / $3T," use `method: thresholds`; the script interpolates where the cumulative `P(outcome > threshold)` curve crosses 50%.

For Polymarket candidate discovery, run:

```bash
python scripts/discover_polymarket_markets.py openai tesla brazil
python scripts/discover_polymarket_markets.py --yaml-stubs --max-candidates 5
```

The discovery script uses Polymarket Gamma `public-search`, filters existing watchlist slugs by default, skips events ending inside seven days unless `--min-days-to-end` is overridden, and prints event slugs plus representative market prices. Promote only the candidates that map to durable vault notes; the script is a triage tool, not an auto-ingester.

Supported providers:

| Provider | Source kinds | Notes |
|----------|--------------|-------|
| `kalshi` | `series_ticker`, `event_ticker` | Default for legacy entries; fetches Kalshi's public markets API. |
| `polymarket` | `event_slug`, `market_slug`, `market_id` | Uses Polymarket Gamma API. Track individual markets by `slug` inside `tracked_markets`. |

---

## Cross-venue comparisons

Current comparison set:

| Comparison | Note | Why it matters |
|------------|------|----------------|
| `bitcoin-150k-2026-cross-venue` | [[Bitcoin]] | Checks whether Kalshi and Polymarket agree on the 2026 $150K right tail. |
| `spacex-june-ipo-cross-venue` | [[SpaceX IPO 2026]] | Checks whether both venues still price a June IPO as the base case. |
| `openai-no-2026-ipo-cross-venue` | [[2026 IPO pipeline]] | Compares Kalshi's inverted "IPO before Jan. 1, 2027" leg with Polymarket's direct "no IPO by Dec. 31, 2026" leg. |

Small spreads are useful confirmation. Large spreads are a research prompt: check contract definitions first, then decide whether the note needs a cross-venue disagreement paragraph.

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
| "Polymarket prices X at 45c" | "On May 20, 2026, Polymarket traders priced X at 45c; the market resolved Yes/No on DATE." |
| Current overlay | Forecast audit / signal quality |

---

## Related

- [[Kalshi]] — platform actor
- [[Polymarket]] — crypto-native platform actor
- [[Prediction markets]] — concept
- [[Valve]] — first Steam Machine price overlay that triggered this tracker
- [[2026 Brazil presidential election]] — first Polymarket event added to the provider-aware watchlist
- [[US-China tariffs]] — tariff markets now tracked through the watchlist
- [[Fed independence]] — institutional-risk markets now tracked through the watchlist
