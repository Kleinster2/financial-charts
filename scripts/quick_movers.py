"""Quick vault mover check — scans actor aliases against market data.

Uses beta-adjusted excess returns to flag statistically unusual *idiosyncratic*
moves. A stock that rises 5% on a +3% market day when its beta is 1.2 had an
excess return of +1.4% — that's what gets z-scored, not the raw +5%.

Beta is computed over a longer window (120 days) for stability; idiosyncratic
volatility uses a shorter window (60 days) for responsiveness.

Supports both DuckDB (long format: Date/Ticker/Close) and SQLite (wide format:
Date + ticker columns). Tries DuckDB first if it has fresher data.
"""
import argparse
import re
import sqlite3
import sys
import math
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover - repo tooling normally has PyYAML
    yaml = None

try:
    import duckdb
    HAS_DUCKDB = True
except ImportError:
    HAS_DUCKDB = False

ACTORS = Path(__file__).parent.parent / "investing" / "Actors"
SQLITE_DB = Path(__file__).parent.parent / "market_data.db"
DUCK_DB = Path(__file__).parent.parent / "market_data.duckdb"
SKIP = {"AI","US","UK","EU","HQ","PE","RE","DC","VC","CEO","CTO","COO","CFO","IPO",
        "SA","SE","AG","NV","AB","LP","NA","AM","GP","BE","IT","OR","ON","TD","BN","BAM"}
DEFAULT_SIGMA = 2.5
DEFAULT_PCT_FLOOR = 6.0  # always-on absolute-% backstop (catches borderline-sigma names like CHYM at -7.5% / 1.71s)
HIGH_VOL_THRESHOLD = 50.0  # idiosyncratic vol % above which a lower sigma applies
HIGH_VOL_SIGMA = 2.0       # sigma threshold for high-vol names (vs DEFAULT_SIGMA for the rest)
VOL_LOOKBACK = 60    # trading days for idiosyncratic volatility
BETA_LOOKBACK = 120  # trading days for beta estimation
BENCHMARK = "SPY"


def _frontmatter(text):
    """Return YAML frontmatter as a dict when present."""
    if yaml is None or not text.startswith("---"):
        return {}
    match = re.match(r"^---\s*\n(.*?)\n---\s*", text, re.DOTALL)
    if not match:
        return {}
    try:
        data = yaml.safe_load(match.group(1)) or {}
    except Exception:
        return {}
    return data if isinstance(data, dict) else {}


def _list_field(data, key):
    value = data.get(key)
    if isinstance(value, list):
        return [str(item).strip().strip("'\"") for item in value if str(item).strip()]
    if isinstance(value, str):
        text = value.strip()
        if text.startswith("[") and text.endswith("]"):
            text = text[1:-1]
        return [item.strip().strip("'\"") for item in text.split(",") if item.strip()]
    return []


def extract_alias_tickers(text):
    """Extract ticker-like aliases/ticker fields from YAML frontmatter."""
    fm = _frontmatter(text)
    raw = _list_field(fm, "aliases") + _list_field(fm, "ticker")
    if not raw:
        # Legacy fallback for malformed notes without parseable frontmatter.
        match = re.search(r"aliases:\s*\[(.*?)\]", text)
        if match:
            raw = [a.strip().strip("'\"") for a in match.group(1).split(",") if a.strip()]
    found = set()
    for item in raw:
        token = item.upper()
        for candidate in (token, re.split(r"[-.]", token)[0]):
            if re.match(r"^[A-Z]{1,6}$", candidate) and candidate not in SKIP:
                found.add(candidate)
    return found


def get_vault_tickers():
    """Extract ticker candidates from vault actor notes."""
    candidates = {}
    for f in ACTORS.glob("*.md"):
        try:
            text = f.read_text(encoding="utf-8", errors="ignore")[:2000]
        except Exception:
            continue
        for ticker in extract_alias_tickers(text):
            candidates[ticker] = f.stem
        tm = re.search(r"\|\s*Tickers?\s*\|\s*([^\|]+)\|", text, re.IGNORECASE)
        if tm:
            for part in re.split(r"[,;]", tm.group(1).strip()):
                # Strip parenthetical exchange tags before ticker validation, e.g.
                # "F34 (SGX)" → "F34", "AAPL (NASDAQ)" → "AAPL". Then accept only
                # pure-letter tickers — F34 fails the anchor, preventing it from
                # masquerading as 'F' and overwriting Ford in `candidates`.
                cleaned = re.sub(r"\s*\([^)]*\)\s*", "", part).strip()
                m = re.match(r"^([A-Z]{1,6})$", cleaned)
                if m and m.group(1) not in SKIP and m.group(1) not in candidates:
                    candidates[m.group(1)] = f.stem
    return candidates


def pick_backend():
    """Choose DuckDB or SQLite based on data freshness."""
    duck_date = None
    sqlite_date = None

    if HAS_DUCKDB and DUCK_DB.exists():
        try:
            conn = duckdb.connect(str(DUCK_DB), read_only=True)
            r = conn.execute("SELECT MAX(Date) FROM prices").fetchone()
            duck_date = str(r[0]) if r and r[0] else None
            conn.close()
        except Exception:
            pass

    if SQLITE_DB.exists():
        try:
            conn = sqlite3.connect(str(SQLITE_DB))
            has_narrow = conn.execute(
                "SELECT 1 FROM sqlite_master WHERE type='table' AND name='prices_long'"
            ).fetchone() is not None
            if has_narrow:
                r = conn.execute(
                    "SELECT MAX(substr(Date, 1, 10)) FROM prices_long WHERE Ticker = ?",
                    (BENCHMARK,),
                ).fetchone()
                sqlite_date = str(r[0])[:10] if r and r[0] else None
            if not sqlite_date:
                r = conn.execute("SELECT MAX(date) FROM stock_prices_daily").fetchone()
                sqlite_date = str(r[0])[:10] if r and r[0] else None
            conn.close()
        except Exception:
            pass

    if duck_date and sqlite_date:
        if duck_date >= sqlite_date:
            return "duckdb", duck_date
        else:
            return "sqlite", sqlite_date
    elif duck_date:
        return "duckdb", duck_date
    elif sqlite_date:
        return "sqlite", sqlite_date
    else:
        return None, None


def compute_sigma_duckdb(candidates, vol_lookback=VOL_LOOKBACK, beta_lookback=BETA_LOOKBACK):
    """Compute sigma moves using DuckDB long-format prices table."""
    conn = duckdb.connect(str(DUCK_DB), read_only=True)

    db_tickers = set(r[0] for r in conn.execute("SELECT DISTINCT Ticker FROM prices").fetchall())
    ticker_map = {t: a for t, a in candidates.items() if t in db_tickers}

    if not ticker_map:
        conn.close()
        return ticker_map, [], []

    # Need enough days for beta window
    fetch_days = beta_lookback + 2
    tickers = list(ticker_map.keys())
    dates = conn.execute(
        f"SELECT DISTINCT Date FROM prices ORDER BY Date DESC LIMIT {fetch_days}"
    ).fetchall()
    if len(dates) < 10:
        conn.close()
        return ticker_map, [], []

    min_date = dates[-1][0]

    # Fetch stock prices
    ticker_list = ", ".join(f"'{t}'" for t in tickers)
    rows = conn.execute(f"""
        SELECT Ticker, Date, Close FROM prices
        WHERE Ticker IN ({ticker_list}) AND Date >= '{min_date}'
        ORDER BY Ticker, Date DESC
    """).fetchall()

    # Fetch benchmark prices
    bench_rows = conn.execute(f"""
        SELECT Date, Close FROM prices
        WHERE Ticker = '{BENCHMARK}' AND Date >= '{min_date}'
        ORDER BY Date DESC
    """).fetchall()
    conn.close()

    from collections import defaultdict
    by_ticker = defaultdict(list)
    for ticker, date, close in rows:
        if close is not None:
            by_ticker[ticker].append((str(date), close))

    bench_prices = [(str(d), c) for d, c in bench_rows if c is not None]

    results, skipped = _compute_from_prices(by_ticker, ticker_map, bench_prices,
                                            vol_lookback, beta_lookback)
    return ticker_map, results, skipped


def compute_sigma_sqlite(candidates, vol_lookback=VOL_LOOKBACK, beta_lookback=BETA_LOOKBACK):
    """Compute sigma moves using SQLite prices_long when available, else wide prices."""
    conn = sqlite3.connect(str(SQLITE_DB))
    has_narrow = conn.execute(
        "SELECT 1 FROM sqlite_master WHERE type='table' AND name='prices_long'"
    ).fetchone() is not None

    if has_narrow:
        try:
            db_tickers = set(
                r[0] for r in conn.execute("SELECT DISTINCT Ticker FROM prices_long").fetchall()
            )
            ticker_map = {t: a for t, a in candidates.items() if t in db_tickers}

            if not ticker_map:
                conn.close()
                return ticker_map, [], []

            fetch_days = beta_lookback + 2
            tickers = list(ticker_map.keys())
            dates = conn.execute(
                """
                SELECT DISTINCT substr(Date, 1, 10) AS session_date
                FROM prices_long
                ORDER BY session_date DESC
                LIMIT ?
                """,
                (fetch_days,),
            ).fetchall()
            if len(dates) < 10:
                conn.close()
                return ticker_map, [], []

            min_date = dates[-1][0]
            placeholders = ", ".join("?" for _ in tickers)
            rows = conn.execute(
                f"""
                SELECT Ticker, substr(Date, 1, 10) AS session_date, Close
                FROM prices_long
                WHERE Ticker IN ({placeholders}) AND substr(Date, 1, 10) >= ?
                ORDER BY Ticker, session_date DESC
                """,
                [*tickers, min_date],
            ).fetchall()
            bench_rows = conn.execute(
                """
                SELECT substr(Date, 1, 10) AS session_date, Close
                FROM prices_long
                WHERE Ticker = ? AND substr(Date, 1, 10) >= ?
                ORDER BY session_date DESC
                """,
                (BENCHMARK, min_date),
            ).fetchall()
            conn.close()

            from collections import defaultdict
            by_ticker = defaultdict(list)
            for ticker, date, close in rows:
                if close is not None:
                    by_ticker[ticker].append((date, close))

            bench_prices = [(d, c) for d, c in bench_rows if c is not None]
            results, skipped = _compute_from_prices(by_ticker, ticker_map, bench_prices,
                                                    vol_lookback, beta_lookback)
            return ticker_map, results, skipped
        except Exception:
            # Fall back to the legacy wide table if the narrow path is unavailable
            # or has an unexpected schema.
            try:
                conn.close()
            except Exception:
                pass
            conn = sqlite3.connect(str(SQLITE_DB))

    cols = set(r[1] for r in conn.execute("PRAGMA table_info(stock_prices_daily)").fetchall())
    ticker_map = {t: a for t, a in candidates.items() if t in cols}

    if not ticker_map:
        conn.close()
        return ticker_map, [], []

    # Need enough days for beta window
    fetch_days = beta_lookback + 2
    tickers = list(ticker_map.keys())

    # Always include benchmark
    need_bench = BENCHMARK not in tickers
    all_cols = tickers + ([BENCHMARK] if need_bench and BENCHMARK in cols else [])
    col_str = ", ".join(f"[{t}]" for t in all_cols)

    rows = conn.execute(
        f'SELECT date, {col_str} FROM stock_prices_daily ORDER BY date DESC LIMIT {fetch_days}'
    ).fetchall()
    conn.close()

    if len(rows) < 10:
        return ticker_map, [], []

    from collections import defaultdict
    by_ticker = defaultdict(list)
    bench_prices = []

    for row in rows:
        date = str(row[0])[:10]
        for idx, ticker in enumerate(all_cols):
            val = row[idx + 1]
            if val is not None:
                if ticker == BENCHMARK and need_bench:
                    bench_prices.append((date, val))
                else:
                    by_ticker[ticker].append((date, val))
        # If benchmark is also a vault ticker, grab it for bench_prices too
        if not need_bench and BENCHMARK in tickers:
            bench_idx = tickers.index(BENCHMARK)
            val = row[bench_idx + 1]
            if val is not None:
                bench_prices.append((date, val))

    results, skipped = _compute_from_prices(by_ticker, ticker_map, bench_prices,
                                            vol_lookback, beta_lookback)
    return ticker_map, results, skipped


def _compute_returns(price_list):
    """Compute returns from a price list in date-descending order."""
    prices = [p for _, p in price_list]
    returns = []
    for i in range(len(prices) - 1):
        if prices[i + 1] and prices[i + 1] > 0:
            returns.append((prices[i] - prices[i + 1]) / prices[i + 1])
        else:
            returns.append(None)
    return returns


def _date_key(value):
    """Normalize date or datetime strings to YYYY-MM-DD for session matching."""
    return str(value)[:10]


def _compute_beta(stock_returns, bench_returns, n):
    """Compute beta using up to n historical return pairs (skipping today's return)."""
    # stock_returns[0] is today, [1:] is history (most recent first)
    pairs = []
    for i in range(1, min(len(stock_returns), len(bench_returns), n + 1)):
        sr = stock_returns[i]
        br = bench_returns[i]
        if sr is not None and br is not None:
            pairs.append((sr, br))

    if len(pairs) < 20:
        return None

    mean_s = sum(s for s, _ in pairs) / len(pairs)
    mean_b = sum(b for _, b in pairs) / len(pairs)

    cov = sum((s - mean_s) * (b - mean_b) for s, b in pairs) / len(pairs)
    var_b = sum((b - mean_b) ** 2 for _, b in pairs) / len(pairs)

    if var_b < 1e-12:
        return None

    return cov / var_b


def _compute_from_prices(by_ticker, ticker_map, bench_prices, vol_lookback, beta_lookback):
    """Compute beta-adjusted sigma moves from per-ticker price lists."""
    # Compute benchmark returns
    bench_returns = _compute_returns(bench_prices) if bench_prices else []
    expected_date = _date_key(bench_prices[0][0]) if bench_prices else None

    results = []
    skipped = []
    for ticker, price_list in by_ticker.items():
        if ticker == BENCHMARK:
            continue
        if len(price_list) < 10:
            continue

        date = _date_key(price_list[0][0])
        if expected_date and date != expected_date:
            skipped.append((ticker, ticker_map.get(ticker, ticker), date, expected_date))
            continue

        stock_returns = _compute_returns(price_list)
        if len(stock_returns) < 5:
            continue

        today_return = stock_returns[0]
        if today_return is None:
            continue

        curr, prev = price_list[0][1], price_list[1][1]
        pct = today_return * 100

        # Compute beta over longer window
        beta = _compute_beta(stock_returns, bench_returns, beta_lookback)

        # Compute excess returns
        excess_returns = []
        for i in range(len(stock_returns)):
            sr = stock_returns[i]
            br = bench_returns[i] if i < len(bench_returns) else None
            if sr is not None and br is not None and beta is not None:
                excess_returns.append(sr - beta * br)
            elif sr is not None:
                # Fallback: use raw return if no benchmark data
                excess_returns.append(sr)

        if len(excess_returns) < 5:
            continue

        today_excess = excess_returns[0]

        # Use vol_lookback window for idiosyncratic vol (skip today)
        hist_excess = excess_returns[1:vol_lookback + 1]
        if len(hist_excess) < 5:
            continue

        mean_ex = sum(hist_excess) / len(hist_excess)
        variance = sum((r - mean_ex) ** 2 for r in hist_excess) / len(hist_excess)
        std_ex = math.sqrt(variance)

        if std_ex < 1e-10:
            continue

        z_score = (today_excess - mean_ex) / std_ex
        annualized_vol = std_ex * math.sqrt(252) * 100

        # Also compute raw annualized vol for display
        raw_hist = [r for r in stock_returns[1:vol_lookback + 1] if r is not None]
        raw_vol = math.sqrt(sum(r ** 2 for r in raw_hist) / len(raw_hist)) * math.sqrt(252) * 100 if raw_hist else annualized_vol

        actor = ticker_map.get(ticker, ticker)
        results.append((ticker, actor, prev, curr, pct, z_score, annualized_vol, date,
                         beta if beta is not None else 0.0, raw_vol))

    return results, skipped


def main():
    parser = argparse.ArgumentParser(description="Check vault actors for statistically unusual moves.")
    parser.add_argument("--sigma", type=float, default=DEFAULT_SIGMA,
                        help=f"Standard deviation threshold (default: {DEFAULT_SIGMA})")
    parser.add_argument("--vol-lookback", type=int, default=VOL_LOOKBACK,
                        help=f"Rolling window for idiosyncratic vol (default: {VOL_LOOKBACK} days)")
    parser.add_argument("--beta-lookback", type=int, default=BETA_LOOKBACK,
                        help=f"Window for beta estimation (default: {BETA_LOOKBACK} days)")
    parser.add_argument("--pct", type=float, default=None,
                        help="Optional: also flag moves above this %% regardless of sigma (legacy alias for --pct-floor)")
    parser.add_argument("--pct-floor", type=float, default=DEFAULT_PCT_FLOOR,
                        help=f"Always-on absolute-%% backstop (default: {DEFAULT_PCT_FLOOR:.1f}%%). Catches borderline-sigma names. Set to 999 to disable.")
    parser.add_argument("--high-vol-sigma", type=float, default=HIGH_VOL_SIGMA,
                        help=f"Lower sigma threshold for high-vol names (idiosyncratic vol > {HIGH_VOL_THRESHOLD:.0f}%%). Default: {HIGH_VOL_SIGMA}")
    parser.add_argument("--high-vol-threshold", type=float, default=HIGH_VOL_THRESHOLD,
                        help=f"Annualized idiosyncratic vol %% above which --high-vol-sigma applies (default: {HIGH_VOL_THRESHOLD:.0f})")
    parser.add_argument("--raw", action="store_true",
                        help="Use raw returns instead of beta-adjusted (original behavior)")
    parser.add_argument("--show-stale", action="store_true",
                        help=f"List tickers skipped because their latest close is not on the {BENCHMARK} session date")
    args = parser.parse_args()

    backend, latest_date = pick_backend()
    if not backend:
        print("No market data found (checked DuckDB and SQLite).")
        return

    mode = "raw" if args.raw else f"beta-adjusted (beta:{args.beta_lookback}d, vol:{args.vol_lookback}d)"
    print(f"Using {backend} (latest data: {latest_date}) — {mode}")
    candidates = get_vault_tickers()

    if backend == "duckdb":
        ticker_map, all_results, skipped = compute_sigma_duckdb(candidates, args.vol_lookback, args.beta_lookback)
    else:
        ticker_map, all_results, skipped = compute_sigma_sqlite(candidates, args.vol_lookback, args.beta_lookback)

    print(f"Found {len(ticker_map)} trackable tickers (in DB + vault).")
    if skipped:
        expected_date = skipped[0][3]
        print(f"Skipped {len(skipped)} off-session tickers (latest close not on {BENCHMARK} session {expected_date}).")
        if args.show_stale:
            for ticker, actor, date, _ in sorted(skipped, key=lambda x: (x[2], x[0])):
                print(f"  {ticker:<8} {actor:<30} latest close {date}")

    # Get benchmark return for display
    bench_return = None
    if all_results:
        # Pull benchmark from the data we already have
        conn = sqlite3.connect(str(SQLITE_DB)) if backend == "sqlite" else None
        if conn:
            try:
                has_narrow = conn.execute(
                    "SELECT 1 FROM sqlite_master WHERE type='table' AND name='prices_long'"
                ).fetchone() is not None
                if has_narrow:
                    rows = conn.execute(
                        "SELECT Close FROM prices_long WHERE Ticker = ? ORDER BY Date DESC LIMIT 2",
                        (BENCHMARK,),
                    ).fetchall()
                else:
                    rows = conn.execute(
                        f"SELECT [{BENCHMARK}] FROM stock_prices_daily ORDER BY date DESC LIMIT 2"
                    ).fetchall()
                if len(rows) == 2 and rows[0][0] and rows[1][0]:
                    bench_return = (rows[0][0] - rows[1][0]) / rows[1][0] * 100
            except Exception:
                pass
            finally:
                conn.close()

    if bench_return is not None:
        print(f"{BENCHMARK}: {bench_return:+.1f}% on {latest_date}")

    # Resolve effective floor: explicit --pct overrides --pct-floor for backward-compat
    effective_pct_floor = args.pct if args.pct is not None else args.pct_floor

    movers = []
    flag_reasons = {}  # ticker -> list of reasons triggered
    for item in all_results:
        ticker, actor, prev, curr, pct, z_score, vol, date = item[:8]
        beta = item[8] if len(item) > 8 else 0.0
        raw_vol = item[9] if len(item) > 9 else vol

        reasons = []
        # Primary: standard sigma threshold
        if abs(z_score) >= args.sigma:
            reasons.append(f">={args.sigma}s")
        # High-vol adjustment: high idiosyncratic vol names get a lower sigma bar
        elif vol >= args.high_vol_threshold and abs(z_score) >= args.high_vol_sigma:
            reasons.append(f">={args.high_vol_sigma}s (high-vol)")
        # Always-on absolute-% backstop
        if abs(pct) >= effective_pct_floor:
            reasons.append(f">={effective_pct_floor:.1f}%")

        if reasons:
            flag_reasons[ticker] = reasons
            movers.append((ticker, actor, prev, curr, pct, z_score, vol, date, beta, raw_vol))
    movers.sort(key=lambda x: abs(x[5]), reverse=True)

    if movers:
        print(f"\n** VAULT ACTORS WITH UNUSUAL MOVES (>={args.sigma}s, or >={args.high_vol_sigma}s if vol>{args.high_vol_threshold:.0f}%, or >={effective_pct_floor:.1f}% absolute):\n")
        hdr = f"{'Ticker':<8} {'Actor':<30} {'Prev':>8} {'Last':>8} {'Change':>8} {'Sigma':>7} {'Beta':>6} {'IdioVol':>8} Trigger"
        print(hdr)
        print("-" * len(hdr))
        for t, a, p, c, pct, z, vol, d, beta, raw_vol in movers:
            sign = "+" if pct > 0 else ""
            zsign = "+" if z > 0 else ""
            trigger = ", ".join(flag_reasons.get(t, []))
            print(f"{t:<8} {a:<30} ${p:>7.2f} ${c:>7.2f} {sign}{pct:>6.1f}% {zsign}{z:>5.1f}s {beta:>5.2f}x {vol:>6.0f}% {trigger}")
    else:
        print(f"\nNo vault actors exceeded thresholds (>={args.sigma}s, high-vol-s {args.high_vol_sigma}, pct floor {effective_pct_floor:.1f}%).")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        import traceback
        traceback.print_exc()
        sys.exit(1)
