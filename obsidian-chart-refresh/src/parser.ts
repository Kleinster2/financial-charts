/**
 * Chart parameters extracted from filename or registry
 */
export interface ChartParams {
  tickers: string[];
  normalize: boolean;
  start?: string; // ISO date string, e.g., "2020-01-01"
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

  // Unknown pattern
  return { type: "unknown", filename };
}

/**
 * Parse comparison chart: aapl-vs-qqq-2020.png
 */
function parseComparisonChart(name: string): ParseResult {
  // Extract year suffix if present (last segment that's 4 digits)
  const yearMatch = name.match(/-(\d{4})$/);
  const startYear = yearMatch ? yearMatch[1] : null;

  // Remove year suffix for ticker parsing
  const nameWithoutYear = startYear ? name.replace(/-\d{4}$/, "") : name;

  // Split on -vs- to get tickers
  const segments = nameWithoutYear.split("-vs-");

  // Clean up each segment (remove -price-chart suffix if present)
  const tickers = segments.map((seg) =>
    seg.replace(/-price-chart$/, "").toUpperCase()
  );

  // Validate: need at least 2 tickers
  if (tickers.length < 2) {
    return { type: "unknown", filename: name };
  }

  // Validate: tickers should look like tickers (alphanumeric, reasonable length)
  for (const ticker of tickers) {
    if (!/^[A-Z0-9]{1,10}$/.test(ticker)) {
      return { type: "unknown", filename: name };
    }
  }

  const params: ChartParams = {
    tickers,
    normalize: true,
  };

  if (startYear) {
    params.start = `${startYear}-01-01`;
  }

  return { type: "parsed", params };
}

/**
 * Parse single ticker price chart: aapl-price-chart-2020.png
 */
function parsePriceChart(name: string): ParseResult {
  // Extract year suffix if present
  const yearMatch = name.match(/-(\d{4})$/);
  const startYear = yearMatch ? yearMatch[1] : null;

  // Remove year and -price-chart suffix
  let ticker = name;
  if (startYear) {
    ticker = ticker.replace(/-\d{4}$/, "");
  }
  ticker = ticker.replace(/-price-chart$/, "").toUpperCase();

  // Validate ticker
  if (!/^[A-Z0-9]{1,10}$/.test(ticker)) {
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

  return url.toString();
}
