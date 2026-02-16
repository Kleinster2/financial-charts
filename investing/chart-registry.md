---
charts:
  skhynix-vs-peers.png:
    tickers: 000660.KS,SMH
    normalize: true
    start: 2019-01-01
  skhynix-fundamentals.png:
    skip: true
  hyperscaler-capex.png:
    tickers: AMZN,GOOG,META,MSFT
    metrics: capex
    skip: true
  gpu-memory-scaling.png:
    skip: true
  brazil-2026-ipo-comparison.png:
    tickers: PICS,NU,STNE,PAGS
    normalize: true
    start: 2026-01-29
    primary: PICS
  brazil-fintech-comparison.png:
    tickers: NU,STNE,PAGS,PICS
    normalize: true
    start: 2021-12-09
    primary: NU
  bptrx-vs-spacex_private-price-chart.png:
    skip: true
---

# Chart Registry

Fallback configuration for charts that can't be parsed from filename.

## How it works

1. Plugin detects `![[chart.png]]` in a note
2. Tries to parse ticker from filename (e.g., `aapl-vs-qqq.png` → AAPL, QQQ)
3. If parsing fails, checks this registry
4. If found here, uses these parameters
5. If `skip: true`, no auto-refresh

## Adding entries

```yaml
charts:
  my-custom-chart.png:
    tickers: AAPL,MSFT,GOOG
    normalize: true
    start: 2020-01-01
```

## Skipping charts

For fundamentals or custom charts that shouldn't auto-refresh:

```yaml
charts:
  nvda-fundamentals.png:
    skip: true
```
