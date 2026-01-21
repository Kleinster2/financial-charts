# Obsidian Chart Refresh Plugin

**Status:** Planned
**Created:** 2026-01-20

## Problem

Charts in the vault are static PNGs generated via the chart API. They become stale as prices update. Currently requires manual re-generation via curl.

## Goal

Automatically refresh chart images when a note is opened, fetching fresh data from the local chart API.

## Requirements

### Must have
- On note open, detect chart images (e.g., `![[*-chart.png]]`, `![[*-capex.png]]`)
- Extract parameters (ticker, metrics, date range) from filename or frontmatter
- Fetch fresh PNG from `localhost:5000/api/chart/lw?...`
- Update cached image in `investing/attachments/`
- Refresh the view to show new image
- Only refresh if Flask app is running (fail silently otherwise)

### Should have
- Settings toggle: auto-refresh on/off
- Settings: API base URL (default `http://localhost:5000`)
- Settings: image pattern to match
- Visual indicator while refreshing (subtle)
- Cache TTL — don't refresh if image is < N minutes old

### Could have
- Manual refresh command (palette: "Refresh charts in current note")
- Batch refresh command ("Refresh all charts in vault")
- Frontmatter override for per-note settings

## Design

### Decision: Hybrid approach

**Filename parsing first, registry fallback.** Most charts are simple enough to parse from filename. Complex cases go in a central registry.

### Filename conventions

**Auto-refresh (price charts):**

| Pattern | Example | Result |
|---------|---------|--------|
| Single ticker | `aapl-price-chart.png` | `tickers=AAPL` |
| With start year | `aapl-price-chart-2020.png` | `tickers=AAPL&start=2020-01-01` |
| 2-way comparison | `aapl-vs-qqq.png` | `tickers=AAPL,QQQ&normalize=true` |
| 2-way + year | `aapl-vs-qqq-2020.png` | `tickers=AAPL,QQQ&normalize=true&start=2020-01-01` |
| N-way comparison | `nvda-vs-amd-vs-intc.png` | `tickers=NVDA,AMD,INTC&normalize=true` |
| N-way + year | `amzn-vs-goog-vs-meta-vs-msft-2019.png` | `tickers=AMZN,GOOG,META,MSFT&normalize=true&start=2019-01-01` |

**Excluded from auto-refresh (fundamentals charts):**

| Pattern | Example | Why excluded |
|---------|---------|--------------|
| Fundamentals | `aapl-fundamentals.png` | Data only changes on earnings |
| Fundamentals + year | `aapl-fundamentals-2019.png` | Regenerate manually via curl |

**Parsing rules:**
- `-fundamentals` in filename → skip auto-refresh
- Split on `-vs-` → each segment is a ticker (implies `normalize=true`)
- Four-digit suffix → start year (January 1)
- `-price-chart` suffix → price only (no metrics)
- Ticker extracted from first segment, uppercased

### Registry fallback

For price charts that can't be parsed (ambiguous tickers, non-January start), use `investing/chart-registry.md`:

```yaml
---
charts:
  arm-holdings-price-chart.png:
    tickers: ARM
    start: 2023-09-14
  hyperscaler-price-comparison.png:
    tickers: AMZN,GOOG,META,MSFT
    normalize: true
    start: 2020-01-01
---
```

Note: Fundamentals charts don't go in the registry — they're excluded from auto-refresh entirely.

**Resolution order:**
1. Has `metrics` or `-fundamentals` in filename → skip (no auto-refresh)
2. Check registry — if found, use those params
3. Parse filename — if parseable, use inferred params
4. Skip — log warning, don't refresh

### Plugin structure

```
obsidian-chart-refresh/
├── main.ts           # Plugin entry, registers events
├── settings.ts       # Settings tab
├── chart-fetcher.ts  # API calls, image writing
├── parser.ts         # Frontmatter/filename parsing
├── manifest.json
└── package.json
```

### Key events

```typescript
// On file open
this.registerEvent(
  this.app.workspace.on('file-open', async (file) => {
    if (file && this.settings.autoRefresh) {
      await this.refreshChartsInNote(file);
    }
  })
);
```

### API integration

```typescript
async function fetchChart(params: ChartParams): Promise<ArrayBuffer> {
  const url = new URL('/api/chart/lw', this.settings.apiBase);
  url.searchParams.set('tickers', params.tickers);
  if (params.metrics) url.searchParams.set('metrics', params.metrics);
  if (params.start) url.searchParams.set('start', params.start);
  if (params.normalize) url.searchParams.set('normalize', 'true');
  if (params.forecast_start) url.searchParams.set('forecast_start', params.forecast_start);

  const response = await fetch(url.toString());
  if (!response.ok) throw new Error(`Chart API error: ${response.status}`);
  return response.arrayBuffer();
}
```

### Error handling

- API not running → fail silently, log to console
- Invalid params → log warning, skip chart
- Network error → retry once, then skip

## Implementation estimate

~150-200 lines TypeScript. 2-4 hours to build and test.

## Dependencies

- Obsidian API (`obsidian` package)
- Flask chart app running on localhost

## Decisions made

1. **Filename vs frontmatter?** → Hybrid. Filename parsing for common cases, registry fallback for complex ones.
2. **Refresh on open vs on interval?** → On-open. Simpler, no background work.
3. **Offline behavior?** → Skip refresh, use cached image, fail silently.
4. **Price vs fundamentals charts?** → Only price charts auto-refresh. Fundamentals charts are static — regenerated manually after earnings updates via curl.
5. **forecast_start?** → Not the plugin's concern. Handled manually when regenerating fundamentals charts.

## Open questions

None. Ready for implementation.

## Next steps

1. ~~Decide filename vs frontmatter approach~~ ✓
2. ~~Decide forecast_start handling~~ ✓
3. Scaffold plugin with `npm init obsidian-plugin`
4. Implement filename parser
5. Implement core refresh logic (price charts only)
6. Add settings UI
7. Test with vault charts
8. Consider publishing to community plugins
