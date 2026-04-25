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
  es-vs-nq-vs-cl-vs-gc-futures-2025.png:
    skip: true
  fed-rate-expectations.png:
    skip: true
  fed-fomc-probabilities.png:
    skip: true
  cl-contango-spread.png:
    skip: true
  cl-term-structure.png:
    skip: true
  ai-compute-sector-chart.png:
    tickers: TSM,NVDA,AMD
    normalize: true
    start: 2024-01-01
    primary: TSM
  alt-managers-sector-chart.png:
    tickers: KKR,APO,ARES,BX,CG,TPG
    normalize: true
    start: 2024-01-01
    primary: KKR
  connectivity-sector-chart.png:
    tickers: AVGO,QCOM,MRVL
    normalize: true
    start: 2024-01-01
    primary: AVGO
  crypto-to-ai-sector-chart.png:
    tickers: CORZ,HUT,IREN,WULF
    normalize: true
    start: 2024-01-01
    primary: CORZ
  dc-reits-sector-chart.png:
    tickers: EQIX,DLR
    normalize: true
    start: 2024-01-01
    primary: EQIX
  defense-it-services-sector-chart.png:
    tickers: LDOS,CACI,SAIC,BAH
    normalize: true
    start: 2024-01-01
    primary: LDOS
  defense-primes-sector-chart.png:
    tickers: LMT,RTX,NOC,GD,LHX
    normalize: true
    start: 2024-01-01
    primary: LMT
  korea-memory-sector-chart.png:
    tickers: 000660.KS,005930.KS
    normalize: true
    start: 2024-01-01
    primary: 000660.KS
  life-insurance-sector-chart.png:
    tickers: MET,PRU,AFL
    normalize: true
    start: 2024-01-01
    primary: MET
  payments-networks-sector-chart.png:
    tickers: V,MA
    normalize: true
    start: 2024-01-01
    primary: V
  pc-insurance-sector-chart.png:
    tickers: TRV,HIG,CB,ALL
    normalize: true
    start: 2024-01-01
    primary: TRV
  us-memory-sector-chart.png:
    tickers: MU,SNDK,WDC
    normalize: true
    start: 2024-01-01
    primary: MU
  us-retail-trading-sector-chart.png:
    tickers: HOOD,COIN,SOFI
    normalize: true
    start: 2024-01-01
    primary: HOOD
  wfe-sector-chart.png:
    tickers: ASML,AMAT,LRCX,KLAC
    normalize: true
    start: 2024-01-01
    primary: ASML
  coinbase-price.png:
    tickers: COIN
    normalize: false
  pm-price.png:
    tickers: PM
    normalize: false
  cg-price.png:
    tickers: CG
    normalize: false
  pypl-price.png:
    tickers: PYPL
    normalize: false
  usdinr-chart.png:
    tickers: USDINR=X
    normalize: false
  india-rupee-usd.png:
    tickers: USDINR=X
    normalize: false
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
