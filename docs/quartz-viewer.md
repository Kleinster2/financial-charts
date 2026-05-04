# Quartz viewer

Quartz v4 serves the investing vault as a local website at `localhost:8080`, replacing Obsidian as the *reading* surface (editing still flows through Claude Code; Obsidian stays installed only for sibling-vault navigation per the original plan). Live interactive lightweight-charts widgets render inline via iframes hitting the local Flask charting engine.

## Layout

| Path | Role |
|------|------|
| `C:\Users\klein\quartz-investing\` | Quartz install (sibling to `financial-charts/`, **outside this repo**). Has its own `.git/` from the upstream clone. |
| `C:\Users\klein\quartz-investing\content\` | Symlink → `C:\Users\klein\financial-charts\investing\`. Created via PowerShell-as-admin (`New-Item -ItemType SymbolicLink`). |
| `C:\Users\klein\quartz-investing\quartz\plugins\transformers\lwcharts.ts` | Custom transformer (~210 lines). Rewrites `<img src="*-chart.png">` to `<iframe src="http://localhost:5000/api/chart/lw?...&format=html">`. |
| `investing/chart-registry.md` (in this repo) | Canonical source for charts whose filenames don't match parser patterns (sector charts, custom names). |
| `charting_app/chart_routes.py` (in this repo) | Hosts the `_render_chart_html` helper + 3 short-circuits at the Playwright sites in `/api/chart/lw`. |
| `charting_app/templates/chart_render.html` (in this repo) | Template with `window.INTERACTIVE`-conditional behavior. |

## Dependency: live Flask

Quartz iframes hit `http://localhost:5000/api/chart/lw?...&format=html` on every page load. **Flask must be running** for charts to render — if it's down, iframes show "site can't be reached." Start with `python charting_app/app.py` from `financial-charts/`.

## Run

```bash
cd /c/Users/klein/quartz-investing
npx quartz build --serve --concurrency 4
```

First build: ~30 minutes wall time on the full vault (~6,000 markdown files). Subsequent edits are sub-second incremental hot-reloads.

Skip the rebuild for serving an existing `public/`:

```bash
cd /c/Users/klein/quartz-investing/public && python ../serve_static.py 8080
```

`serve_static.py` is a small `SimpleHTTPRequestHandler` subclass that maps `/Foo` → `Foo.html` (Quartz emits flat HTML files but renders extensionless `<a href>`s). Plain `python -m http.server` returns 404 for those URLs and is only useful as a sanity check.

For Tailscale / phone access, set `Plugin.LightweightCharts({ apiBaseUrl: "http://gilssurface:5000", ... })` in `quartz.config.ts` and rebuild. Iframe URLs are baked into the static HTML at build time.

## Auto-restart

Both servers are wrapped by a Task Scheduler watchdog that re-spawns whichever is missing every 5 minutes (and at logon). See [`ops/server-watchdog.md`](ops/server-watchdog.md).

## Nightly rebuild

A separate scheduled task `FinancialCharts-Quartz-Rebuild` fires `scripts/rebuild_quartz.ps1` daily at 3 AM. The script builds into `public-next/`, then atomic-swaps it into `public/` (`public/` → `public-old/` → delete; `public-next/` → `public/`). `serve_static.py` keeps serving the previous build throughout — users only see a brief swap at the end.

For same-session freshness (rare — you usually edit in Claude Code and read Quartz against older threads), invoke `/rebuild-quartz-now`. The skill fires the same script in the background. Build takes ~30-40 minutes for the full ~6,300-file vault.

A lockfile at `logs/quartz-rebuild.lock` prevents the nightly job and a manual fire from racing. Stale locks (>2h) are auto-cleared.

### Why not `--serve` mode

Tested 2026-05-04. `npx quartz build --serve` advertises sub-second hot-reload, but on this vault it actually takes ~1 minute per single-file edit (6s parse + ~1m emit, because Quartz rebuilds search index, breadcrumbs, etc. on any change). More damaging: the initial build is the same 38-minute cost as `npx quartz build`, so spawning `--serve` from the watchdog meant 38 minutes of unreachable site on every reboot, lid-cycle, or crash recovery. The atomic-swap nightly path keeps `public/` always available with a fast cold start, at the cost of "today's edits visible tomorrow morning" — acceptable since Quartz is a thread-pulling surface, not the editing surface.

## Local Quartz patches

These don't survive a re-clone of upstream Quartz. Re-apply if reinstalling:

### `quartz/plugins/transformers/lwcharts.ts` — new file

Custom rehype transformer. Walks HAST, finds `<img>` whose filename matches a chart pattern (parser logic ported from `obsidian-chart-refresh/src/parser.ts`), replaces with `<iframe>`. Falls through to registry lookup for unparseable filenames. Falls through to static `<img>` for unmatched. Source-of-truth lives in this repo's docs/scripts referenced from session memory; current copy in the install is the one to reproduce.

Key options (set in `quartz.config.ts`):
```ts
Plugin.LightweightCharts({
  apiBaseUrl: "http://localhost:5000",
  contentDir: "./content",
  height: 420,
}),
```

The transformer normalizes CRLF → LF before parsing the registry — without this, regex patterns silently fail on Windows-saved files. (Discovered the hard way: registry was being read but parsed as empty for hours.)

The transformer caches the parsed registry by mtime — re-edits to `chart-registry.md` propagate without restart.

### `quartz/plugins/transformers/frontmatter.ts` — wrap matter() in try/catch

45+ vault notes have wikilinks inside YAML `aliases:` arrays (e.g. `aliases: [[[Burlington]] Northern Santa Fe]`), which strict YAML doesn't parse. Without the patch, the entire build aborts on the first such file. With the patch, we log a warning and proceed with empty frontmatter (filename-as-title). Side effect: those notes lose their aliases in the rendered site. **Real fix: clean the source files** to use proper YAML strings (`aliases: ["Burlington Northern Santa Fe"]`).

### `quartz/plugins/emitters/helpers.ts` — sanitize Windows-illegal filename chars

Aliases containing `<>:"|?*` (e.g. `Israel "Izzy" Englander`) cause `ENOENT` writing the alias-redirect HTML on Windows. Patched `write()` to replace illegal chars with `_` before constructing the path. Aliases with quoted nicknames will write to a sanitized URL slug; the canonical note still resolves correctly.

### `quartz.config.ts`

- `LightweightCharts` plugin registered after `ObsidianFlavoredMarkdown` (OFM converts `![[...]]` to `<img>` first; we need that to have happened before our transformer fires).
- `Plugin.Latex(...)` commented out — KaTeX runs on every paragraph looking for math, which floods the build with warnings on a vault that uses `$` for currency. Disable saves time + log noise.
- `ignorePatterns` extended: `["private", "templates", ".obsidian", "Drafts/**", "Meta/**", "Trackers/**", "scripts/**", "nul", "**/.trash/**"]`. The `nul` entry is critical on Windows — `nul` is a reserved device name; without ignoring it Quartz crashes on file enumeration.

### `quartz.layout.ts` — `Component.TagList()` removed from `defaultContentPageLayout.beforeBody`

The vault uses inline `#sector #drones ...` hashtag lines at the top of note bodies (Obsidian convention). ObsidianFlavoredMarkdown extracts those into `file.data.frontmatter.tags` AND renders them inline in the body as `<a class="tag-link">` chips. Quartz's `Component.TagList()` then displays the same set above the title — producing two identical rows of tag chips. Removing `Component.TagList()` from the layout keeps the inline tags in the body (still navigable to `/tags/<name>`) and drops the duplicate header row.

## chart-registry.md

The fallback for charts whose filenames don't match parser patterns. Format:

```yaml
---
charts:
  filename.png:
    tickers: TICK1,TICK2,TICK3
    normalize: true
    start: 2024-01-01
    primary: TICK1
  custom-chart.png:
    skip: true   # Custom-generated; do not auto-refresh
---
```

`skip: true` entries fall through to static `<img>` (the existing PNG in `attachments/`). Normalized comparisons (`-vs-`) and single-ticker price charts (`-price-chart`) parse from filename without needing registry entries.

## Known issues

- **Homepage 404** at `localhost:8080/` — Quartz expects `index.md`; the vault has `Home.md`/`Dashboard.md`. Fix: symlink or rename. Direct URLs (`localhost:8080/Sectors/AI-Compute`) work fine.
- **First build is slow** (~30 min). Incremental edits after that are sub-second. If a full rebuild is needed (plugin code changed, config changed), block out the time.
- **Aliases lost on broken-YAML notes** — see `frontmatter.ts` patch. Track the 45 affected files (`grep -rE "^aliases:.*\[\[" investing/`) and clean as a follow-up.

## When to rebuild from scratch

- Plugin code changed (`lwcharts.ts` or any patched Quartz file)
- `quartz.config.ts` changed
- Quartz upgraded

Otherwise the running `--serve` picks up content edits + registry edits incrementally.

## Verification

Quick health check:

```bash
# Flask serving HTML mode
curl -s "http://localhost:5000/api/chart/lw?tickers=AAPL,QQQ&start=2024-01-01&format=html" | grep -c "window.INTERACTIVE"
# Expected: 1

# Quartz serving + rendering iframes for the AI Compute sector chart
curl -s "http://localhost:8080/Sectors/AI-Compute" | grep -c "iframe.*api/chart/lw"
# Expected: 1 (or more if multiple charts)
```
