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

### Filename convention

Charts encode parameters in filename:

```
{ticker}-price-chart.png          → /api/chart/lw?tickers={ticker}
{ticker}-vs-{ticker2}.png         → /api/chart/lw?tickers={ticker},{ticker2}&normalize=true
{ticker}-fundamentals.png         → /api/chart/lw?tickers={ticker}&metrics=revenue,netincome
hyperscaler-capex.png             → /api/chart/lw?tickers=AMZN,GOOG,META,MSFT&metrics=capex
```

### Alternative: Frontmatter mapping

```yaml
---
charts:
  aapl-price-chart.png:
    tickers: AAPL
    start: 2020-01-01
  aapl-vs-qqq.png:
    tickers: AAPL,QQQ
    normalize: true
---
```

Frontmatter is more explicit but requires maintenance.

**Recommendation:** Start with frontmatter mapping for explicitness. Consider filename parsing later.

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

## Open questions

1. **Filename vs frontmatter?** Frontmatter is safer but more friction.
2. **Refresh on open vs on interval?** On-open is simpler, avoids background work.
3. **What about forecast_start?** Should auto-advance as time passes?
4. **Offline behavior?** Skip refresh, use cached image.

## Next steps

1. Decide filename vs frontmatter approach
2. Scaffold plugin with `npm init obsidian-plugin`
3. Implement core refresh logic
4. Add settings UI
5. Test with vault charts
6. Consider publishing to community plugins
