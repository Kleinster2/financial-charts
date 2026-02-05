/**
 * Index tickers that use ^ prefix but can't have ^ in filenames
 */
const INDEX_ALIASES: Record<string, string> = {
  "VIX": "^VIX",
  "VIX1D": "^VIX1D",
  "VIX3M": "^VIX3M",
  "VIX6M": "^VIX6M",
  "VIX9D": "^VIX9D",
  "VVIX": "^VVIX",
  "GSPC": "^GSPC",
  "DJI": "^DJI",
  "IXIC": "^IXIC",
  "TNX": "^TNX",
};

/**
 * Resolve a ticker, applying index aliases where needed
 */
function resolveTicker(ticker: string): string {
  return INDEX_ALIASES[ticker] ?? ticker;
}

/**
 * Chart parameters extracted from filename or registry
 */
export interface ChartParams {
  tickers: string[];
  normalize: boolean;
  start?: string; // ISO date string, e.g., "2020-01-01"
  sortByLast?: boolean; // Sort legend by last value (high to low)
}

/**
 * Parse result with status
 */
export type ParseResult =
  | { type: "skip"; reason: string }
  | { type: "parsed"; params: ChartParams }
  | { type: "unknown"; filename: string };

/**
 * Parse a chart filename to extract parameters.
 *
 * Patterns:
 * - aapl-price-chart.png → single ticker
 * - aapl-price-chart-2020.png → single ticker with start year
 * - aapl-vs-qqq.png → comparison (normalized)
 * - aapl-vs-qqq-2020.png → comparison with start year
 * - nvda-vs-amd-vs-intc.png → N-way comparison
 * - usdjpy-vs-eurusd-fx-2025.png → forex pairs (adds =X suffix)
 * - tlt-vs-2510_t-vs-iglt_l-2025.png → international (underscores → dots)
 * - aapl-fundamentals.png → SKIP (no auto-refresh)
 */
export function parseChartFilename(filename: string): ParseResult {
  // Remove extension
  const name = filename.replace(/\.png$/i, "");

  // Skip fundamentals charts
  if (name.includes("-fundamentals") || name.includes("fundamentals")) {
    return { type: "skip", reason: "fundamentals chart" };
  }

  // Check for comparison pattern (-vs-)
  if (name.includes("-vs-")) {
    return parseComparisonChart(name);
  }

  // Check for single ticker price chart
  if (name.includes("-price-chart")) {
    return parsePriceChart(name);
  }

  // Check for YTD pattern (e.g., vix-ytd)
  const ytdResult = parseYtdChart(name);
  if (ytdResult) {
    return ytdResult;
  }

  // Check for duration pattern (e.g., goog-90d, aapl-30d, msft-1y)
  const durationResult = parseDurationChart(name);
  if (durationResult) {
    return durationResult;
  }

  // Unknown pattern
  return { type: "unknown", filename };
}

/**
 * Parse comparison chart: aapl-vs-qqq-2020.png
 * Also supports:
 * - usdjpy-vs-eurusd-fx-2025.png → forex pairs (adds =X to each ticker)
 * - tlt-vs-2510_t-vs-iglt_l-2025.png → international (underscores → dots)
 */
function parseComparisonChart(name: string): ParseResult {
  // Extract year suffix if present (last segment that's 4 digits)
  const yearMatch = name.match(/-(\d{4})$/);
  const startYear = yearMatch ? yearMatch[1] : null;

  // Remove year suffix for ticker parsing
  let nameWithoutYear = startYear ? name.replace(/-\d{4}$/, "") : name;

  // Check for -fx suffix (forex pairs)
  const isForex = nameWithoutYear.endsWith("-fx");
  if (isForex) {
    nameWithoutYear = nameWithoutYear.replace(/-fx$/, "");
  }

  // Split on -vs- to get tickers
  const segments = nameWithoutYear.split("-vs-");

  // Clean up each segment:
  // - Remove -price-chart suffix if present
  // - Convert underscores to dots (for international tickers like 2510.T)
  // - Uppercase
  // - Add =X suffix for forex
  const tickers = segments.map((seg) => {
    let ticker = seg
      .replace(/-price-chart$/, "")
      .replace(/_/g, ".")
      .toUpperCase();
    if (isForex) {
      ticker = ticker + "=X";
    }
    return resolveTicker(ticker);
  });

  // Validate: need at least 2 tickers
  if (tickers.length < 2) {
    return { type: "unknown", filename: name };
  }

  // Validate: tickers should look like tickers
  // Allow alphanumeric, dots, ^ prefix (indices), and =X suffix (forex)
  for (const ticker of tickers) {
    if (!/^\^?[A-Z0-9.]{1,15}(=X)?$/.test(ticker)) {
      return { type: "unknown", filename: name };
    }
  }

  const params: ChartParams = {
    tickers,
    normalize: true,
    sortByLast: true,
  };

  if (startYear) {
    params.start = `${startYear}-01-01`;
  }

  return { type: "parsed", params };
}

/**
 * Parse single ticker price chart: aapl-price-chart-2020.png
 * Also supports underscores → dots for international tickers
 */
function parsePriceChart(name: string): ParseResult {
  // Extract year suffix if present
  const yearMatch = name.match(/-(\d{4})$/);
  const startYear = yearMatch ? yearMatch[1] : null;

  // Remove year and -price-chart suffix, convert underscores to dots
  let ticker = name;
  if (startYear) {
    ticker = ticker.replace(/-\d{4}$/, "");
  }
  ticker = resolveTicker(
    ticker
      .replace(/-price-chart$/, "")
      .replace(/_/g, ".")
      .toUpperCase()
  );

  // Validate ticker (allow dots, ^ prefix for indices)
  if (!/^\^?[A-Z0-9.]{1,15}$/.test(ticker)) {
    return { type: "unknown", filename: name };
  }

  const params: ChartParams = {
    tickers: [ticker],
    normalize: false,
  };

  if (startYear) {
    params.start = `${startYear}-01-01`;
  }

  return { type: "parsed", params };
}

/**
 * Parse YTD chart: vix-ytd.png → single ticker from Jan 1 of current year
 * Also supports comparison: aapl-vs-qqq-ytd.png
 */
function parseYtdChart(name: string): ParseResult | null {
  if (!name.endsWith("-ytd")) return null;

  const base = name.replace(/-ytd$/, "");
  const startYear = new Date().getFullYear().toString();

  // Could be a comparison (aapl-vs-qqq-ytd)
  if (base.includes("-vs-")) {
    const result = parseComparisonChart(base + `-${startYear}`);
    return result;
  }

  // Single ticker
  const ticker = resolveTicker(base.replace(/_/g, ".").toUpperCase());
  if (!/^\^?[A-Z0-9.]{1,15}$/.test(ticker)) return null;

  return {
    type: "parsed",
    params: {
      tickers: [ticker],
      normalize: false,
      start: `${startYear}-01-01`,
    },
  };
}

/**
 * Parse duration chart: goog-90d.png, aapl-30d.png, msft-1y.png
 * Supported durations: 30d, 60d, 90d, 180d, 1y, 2y, 3y, 5y
 */
function parseDurationChart(name: string): ParseResult | null {
  // Match pattern: ticker-NNd or ticker-Ny
  const match = name.match(/^(.+)-(\d+)(d|y)$/i);
  if (!match) {
    return null;
  }

  const [, tickerPart, num, unit] = match;
  const duration = parseInt(num, 10);

  // Convert underscores to dots, uppercase, resolve aliases
  const ticker = resolveTicker(tickerPart.replace(/_/g, ".").toUpperCase());

  // Validate ticker
  if (!/^\^?[A-Z0-9.]{1,15}$/.test(ticker)) {
    return null;
  }

  // Calculate start date
  const now = new Date();
  let daysBack: number;

  if (unit.toLowerCase() === "y") {
    daysBack = duration * 365;
  } else {
    daysBack = duration;
  }

  const startDate = new Date(now.getTime() - daysBack * 24 * 60 * 60 * 1000);
  const startStr = startDate.toISOString().split("T")[0];

  return {
    type: "parsed",
    params: {
      tickers: [ticker],
      normalize: false,
      start: startStr,
    },
  };
}

/**
 * Registry entry from chart-registry.md frontmatter
 */
export interface RegistryEntry {
  tickers?: string;
  normalize?: boolean;
  start?: string;
  skip?: boolean;
}

/**
 * Parse chart-registry.md frontmatter to extract chart configurations
 */
export function parseRegistry(content: string): Map<string, RegistryEntry> {
  const registry = new Map<string, RegistryEntry>();

  // Extract YAML frontmatter between ---
  const match = content.match(/^---\n([\s\S]*?)\n---/);
  if (!match) return registry;

  const yaml = match[1];

  // Find charts: section
  const chartsMatch = yaml.match(/charts:\n([\s\S]*?)(?=\n[^\s]|$)/);
  if (!chartsMatch) return registry;

  const chartsSection = chartsMatch[1];

  // Parse each chart entry (simple YAML parsing)
  // Pattern: "  filename.png:\n    key: value"
  const entryRegex = /^\s{2}([^\s:]+\.png):\n((?:\s{4}[^\n]+\n?)*)/gm;
  let entryMatch;

  while ((entryMatch = entryRegex.exec(chartsSection)) !== null) {
    const filename = entryMatch[1];
    const propsText = entryMatch[2];

    const entry: RegistryEntry = {};

    // Parse properties
    const tickersMatch = propsText.match(/tickers:\s*([^\n]+)/);
    if (tickersMatch) entry.tickers = tickersMatch[1].trim();

    const normalizeMatch = propsText.match(/normalize:\s*(true|false)/);
    if (normalizeMatch) entry.normalize = normalizeMatch[1] === 'true';

    const startMatch = propsText.match(/start:\s*([^\n]+)/);
    if (startMatch) entry.start = startMatch[1].trim();

    const skipMatch = propsText.match(/skip:\s*(true|false)/);
    if (skipMatch) entry.skip = skipMatch[1] === 'true';

    registry.set(filename, entry);
  }

  return registry;
}

/**
 * Convert registry entry to ChartParams
 */
export function registryEntryToParams(entry: RegistryEntry): ChartParams | null {
  if (entry.skip || !entry.tickers) return null;

  return {
    tickers: entry.tickers.split(',').map(t => t.trim()),
    normalize: entry.normalize ?? false,
    start: entry.start,
  };
}

/**
 * Build API URL from chart params
 */
export function buildApiUrl(baseUrl: string, params: ChartParams): string {
  const url = new URL("/api/chart/lw", baseUrl);
  url.searchParams.set("tickers", params.tickers.join(","));

  if (params.normalize) {
    url.searchParams.set("normalize", "true");
  }

  if (params.start) {
    url.searchParams.set("start", params.start);
  }

  if (params.sortByLast) {
    url.searchParams.set("sort_by_last", "true");
  }

  return url.toString();
}
