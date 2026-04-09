"""Correlation cluster analysis on beta-adjusted excess returns.

Finds groups of stocks that co-move on idiosyncratic (non-market) factors,
then flags clusters with statistically unusual group moves — even when no
individual member hits the single-stock sigma threshold.

Complements quick_movers.py: that script catches individual outliers, this
one catches coordinated sector/theme moves that individual screening misses.

Example: 10 SaaS names each at -1.8 sigma = individually ignorable.
As a cluster = 4+ sigma event.
"""
import argparse
import math
import re
import sqlite3
import sys
from collections import defaultdict
from pathlib import Path

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
BENCHMARK = "SPY"

VOL_LOOKBACK = 60
BETA_LOOKBACK = 120
CORR_LOOKBACK = 120
MIN_CLUSTER = 3
CORR_THRESHOLD = 0.30
CLUSTER_SIGMA = 1.5


def get_vault_tickers():
    """Extract ticker candidates from vault actor notes."""
    candidates = {}
    for f in ACTORS.glob("*.md"):
        try:
            text = f.read_text(encoding="utf-8", errors="ignore")[:2000]
        except Exception:
            continue
        am = re.search(r"aliases:\s*\[(.*?)\]", text)
        if am:
            for a in am.group(1).split(","):
                a = a.strip().strip("'\"")
                if re.match(r"^[A-Z]{1,6}$", a) and a not in SKIP:
                    candidates[a] = f.stem
        tm = re.search(r"\|\s*Tickers?\s*\|\s*([^\|]+)\|", text, re.IGNORECASE)
        if tm:
            for part in re.split(r"[,;]", tm.group(1).strip()):
                m = re.match(r"([A-Z]{1,6})", part.strip())
                if m and m.group(1) not in SKIP:
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


def fetch_prices_sqlite(candidates, n_days):
    """Fetch price data from SQLite wide table."""
    conn = sqlite3.connect(str(SQLITE_DB))
    cols = set(r[1] for r in conn.execute("PRAGMA table_info(stock_prices_daily)").fetchall())
    ticker_map = {t: a for t, a in candidates.items() if t in cols}
    if not ticker_map:
        conn.close()
        return {}, [], {}

    tickers = list(ticker_map.keys())
    need_bench = BENCHMARK not in tickers
    all_cols = tickers + ([BENCHMARK] if need_bench and BENCHMARK in cols else [])
    col_str = ", ".join(f"[{t}]" for t in all_cols)

    rows = conn.execute(
        f'SELECT date, {col_str} FROM stock_prices_daily ORDER BY date DESC LIMIT {n_days}'
    ).fetchall()
    conn.close()

    # Build per-ticker price series {ticker: [(date, price), ...]} date-desc
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
        if not need_bench and BENCHMARK in tickers:
            bench_idx = tickers.index(BENCHMARK)
            val = row[bench_idx + 1]
            if val is not None:
                bench_prices.append((date, val))

    return ticker_map, bench_prices, by_ticker


def fetch_prices_duckdb(candidates, n_days):
    """Fetch price data from DuckDB long table."""
    conn = duckdb.connect(str(DUCK_DB), read_only=True)
    db_tickers = set(r[0] for r in conn.execute("SELECT DISTINCT Ticker FROM prices").fetchall())
    ticker_map = {t: a for t, a in candidates.items() if t in db_tickers}
    if not ticker_map:
        conn.close()
        return {}, [], {}

    tickers = list(ticker_map.keys())
    dates = conn.execute(
        f"SELECT DISTINCT Date FROM prices ORDER BY Date DESC LIMIT {n_days}"
    ).fetchall()
    if len(dates) < 10:
        conn.close()
        return ticker_map, [], {}

    min_date = dates[-1][0]
    all_tickers = list(set(tickers + [BENCHMARK]))
    ticker_list = ", ".join(f"'{t}'" for t in all_tickers)

    rows = conn.execute(f"""
        SELECT Ticker, Date, Close FROM prices
        WHERE Ticker IN ({ticker_list}) AND Date >= '{min_date}'
        ORDER BY Ticker, Date DESC
    """).fetchall()
    conn.close()

    by_ticker = defaultdict(list)
    bench_prices = []
    for ticker, date, close in rows:
        if close is None:
            continue
        if ticker == BENCHMARK:
            bench_prices.append((str(date), close))
        else:
            by_ticker[ticker].append((str(date), close))

    return ticker_map, bench_prices, by_ticker


def compute_returns(price_list):
    """Returns list from date-descending prices. returns[0] = today."""
    prices = [p for _, p in price_list]
    returns = []
    for i in range(len(prices) - 1):
        if prices[i + 1] and prices[i + 1] > 0:
            returns.append((prices[i] - prices[i + 1]) / prices[i + 1])
        else:
            returns.append(None)
    return returns


def compute_beta(stock_rets, bench_rets, n):
    """Beta from up to n historical return pairs (skip today)."""
    pairs = []
    for i in range(1, min(len(stock_rets), len(bench_rets), n + 1)):
        s, b = stock_rets[i], bench_rets[i]
        if s is not None and b is not None:
            pairs.append((s, b))
    if len(pairs) < 20:
        return None
    ms = sum(s for s, _ in pairs) / len(pairs)
    mb = sum(b for _, b in pairs) / len(pairs)
    cov = sum((s - ms) * (b - mb) for s, b in pairs) / len(pairs)
    var = sum((b - mb) ** 2 for _, b in pairs) / len(pairs)
    return cov / var if var > 1e-12 else None


def compute_excess_returns(by_ticker, bench_prices, ticker_map, beta_lookback):
    """Compute beta-adjusted excess return series for each ticker.

    Returns:
        excess: {ticker: [excess_ret_day0, excess_ret_day1, ...]}  (day0=today)
        betas: {ticker: beta}
        raw_returns: {ticker: [ret_day0, ...]}
        bench_today: float (benchmark return today)
    """
    bench_rets = compute_returns(bench_prices) if bench_prices else []
    bench_today = bench_rets[0] if bench_rets else 0.0

    excess = {}
    betas = {}
    raw_returns = {}

    for ticker in ticker_map:
        if ticker not in by_ticker or len(by_ticker[ticker]) < 10:
            continue
        stock_rets = compute_returns(by_ticker[ticker])
        if len(stock_rets) < 5 or stock_rets[0] is None:
            continue

        beta = compute_beta(stock_rets, bench_rets, beta_lookback)
        if beta is None:
            continue

        ex = []
        for i in range(len(stock_rets)):
            sr = stock_rets[i]
            br = bench_rets[i] if i < len(bench_rets) else None
            if sr is not None and br is not None:
                ex.append(sr - beta * br)
            else:
                ex.append(None)

        excess[ticker] = ex
        betas[ticker] = beta
        raw_returns[ticker] = stock_rets

    return excess, betas, raw_returns, bench_today


def correlation(xs, ys, n):
    """Pearson correlation on first n non-None overlapping values (skip index 0 = today)."""
    pairs = []
    for i in range(1, min(len(xs), len(ys), n + 1)):
        if xs[i] is not None and ys[i] is not None:
            pairs.append((xs[i], ys[i]))
    if len(pairs) < 20:
        return 0.0
    mx = sum(x for x, _ in pairs) / len(pairs)
    my = sum(y for _, y in pairs) / len(pairs)
    cov = sum((x - mx) * (y - my) for x, y in pairs) / len(pairs)
    sx = math.sqrt(sum((x - mx) ** 2 for x, _ in pairs) / len(pairs))
    sy = math.sqrt(sum((y - my) ** 2 for _, y in pairs) / len(pairs))
    if sx < 1e-10 or sy < 1e-10:
        return 0.0
    return cov / (sx * sy)


def build_clusters(excess, tickers, corr_lookback, corr_threshold, min_cluster):
    """Average-linkage clustering on excess return correlation.

    A stock joins a cluster only if its average correlation with existing
    members exceeds the threshold. Prevents single-linkage chaining where
    distant stocks get linked through intermediaries.

    Algorithm:
    1. Precompute pairwise correlation matrix
    2. Seed clusters from highest-correlated pairs
    3. Grow clusters by adding stocks whose avg corr with members > threshold
    4. Repeat until stable
    """
    n = len(tickers)
    if n < min_cluster:
        return []

    # Step 1: Precompute pairwise correlations (upper triangle)
    # Store as dict for sparse access
    corr_cache = {}
    ticker_idx = {t: i for i, t in enumerate(tickers)}

    # Compute all pairs — O(n^2) correlations
    # For 480 tickers this is ~115K pairs, each scanning 120 days = ~14M ops
    # Feasible but let's batch efficiently
    for i in range(n):
        for j in range(i + 1, n):
            c = correlation(excess[tickers[i]], excess[tickers[j]], corr_lookback)
            if c >= corr_threshold * 0.5:  # cache anything remotely relevant
                corr_cache[(i, j)] = c
                corr_cache[(j, i)] = c

    def avg_corr_with_cluster(stock_idx, cluster_indices):
        """Average correlation of a stock with all cluster members."""
        vals = []
        for ci in cluster_indices:
            key = (stock_idx, ci)
            if key in corr_cache:
                vals.append(corr_cache[key])
            else:
                vals.append(0.0)  # below cache threshold = low correlation
        return sum(vals) / len(vals) if vals else 0.0

    # Step 2: Seed from highest-correlated pairs
    pairs = []
    for (i, j), c in corr_cache.items():
        if i < j and c >= corr_threshold:
            pairs.append((c, i, j))
    pairs.sort(reverse=True)

    assigned = {}  # stock_idx -> cluster_id
    clusters_idx = {}  # cluster_id -> set of stock indices
    next_id = 0

    for _, i, j in pairs:
        if i in assigned and j in assigned:
            continue
        if i not in assigned and j not in assigned:
            # New cluster
            cid = next_id
            next_id += 1
            clusters_idx[cid] = {i, j}
            assigned[i] = cid
            assigned[j] = cid
        elif i in assigned and j not in assigned:
            cid = assigned[i]
            if avg_corr_with_cluster(j, clusters_idx[cid]) >= corr_threshold:
                clusters_idx[cid].add(j)
                assigned[j] = cid
        elif j in assigned and i not in assigned:
            cid = assigned[j]
            if avg_corr_with_cluster(i, clusters_idx[cid]) >= corr_threshold:
                clusters_idx[cid].add(i)
                assigned[i] = cid

    # Step 3: Try to assign remaining stocks to existing clusters
    changed = True
    while changed:
        changed = False
        for idx in range(n):
            if idx in assigned:
                continue
            best_cid = None
            best_avg = 0
            for cid, members in clusters_idx.items():
                ac = avg_corr_with_cluster(idx, members)
                if ac >= corr_threshold and ac > best_avg:
                    best_avg = ac
                    best_cid = cid
            if best_cid is not None:
                clusters_idx[best_cid].add(idx)
                assigned[idx] = best_cid
                changed = True

    # Convert to ticker lists, filter by min size
    result = []
    for cid, members in clusters_idx.items():
        if len(members) >= min_cluster:
            result.append([tickers[i] for i in members])

    return result


def score_cluster(cluster, excess, vol_lookback):
    """Score a cluster's coordinated move.

    Computes the average excess return of cluster members today,
    then z-scores it against the historical distribution of cluster
    average excess returns.
    """
    # Collect today's excess returns
    today_vals = []
    for t in cluster:
        if excess[t][0] is not None:
            today_vals.append(excess[t][0])
    if not today_vals:
        return None

    today_avg = sum(today_vals) / len(today_vals)

    # Historical cluster average excess returns
    hist_avgs = []
    for day in range(1, vol_lookback + 1):
        day_vals = []
        for t in cluster:
            if day < len(excess[t]) and excess[t][day] is not None:
                day_vals.append(excess[t][day])
        if len(day_vals) >= len(cluster) // 2:  # need at least half the cluster
            hist_avgs.append(sum(day_vals) / len(day_vals))

    if len(hist_avgs) < 10:
        return None

    mean_h = sum(hist_avgs) / len(hist_avgs)
    var_h = sum((x - mean_h) ** 2 for x in hist_avgs) / len(hist_avgs)
    std_h = math.sqrt(var_h)

    if std_h < 1e-10:
        return None

    z = (today_avg - mean_h) / std_h
    return today_avg, z, std_h, len(today_vals)


def label_cluster(cluster, ticker_map):
    """Try to auto-label a cluster from common vault note patterns."""
    actors = [ticker_map.get(t, t) for t in cluster]
    return ", ".join(f"{t} ({ticker_map.get(t, '?')})" for t in cluster[:6])


def main():
    parser = argparse.ArgumentParser(
        description="Find correlation clusters with unusual coordinated moves.")
    parser.add_argument("--corr-threshold", type=float, default=CORR_THRESHOLD,
                        help=f"Min correlation to link two stocks (default: {CORR_THRESHOLD})")
    parser.add_argument("--min-cluster", type=int, default=MIN_CLUSTER,
                        help=f"Minimum cluster size (default: {MIN_CLUSTER})")
    parser.add_argument("--cluster-sigma", type=float, default=CLUSTER_SIGMA,
                        help=f"Sigma threshold for cluster flag (default: {CLUSTER_SIGMA})")
    parser.add_argument("--vol-lookback", type=int, default=VOL_LOOKBACK,
                        help=f"Vol lookback for z-scoring (default: {VOL_LOOKBACK})")
    parser.add_argument("--beta-lookback", type=int, default=BETA_LOOKBACK,
                        help=f"Beta lookback (default: {BETA_LOOKBACK})")
    parser.add_argument("--corr-lookback", type=int, default=CORR_LOOKBACK,
                        help=f"Correlation lookback (default: {CORR_LOOKBACK})")
    parser.add_argument("--show-all", action="store_true",
                        help="Show all clusters, not just flagged ones")
    parser.add_argument("--verbose", action="store_true",
                        help="Show individual member details for flagged clusters")
    args = parser.parse_args()

    backend, latest_date = pick_backend()
    if not backend:
        print("No market data found.")
        return

    print(f"Using {backend} (latest data: {latest_date})")
    print(f"Params: corr>={args.corr_threshold}, min_size={args.min_cluster}, "
          f"cluster_sigma>={args.cluster_sigma}")

    candidates = get_vault_tickers()
    n_days = max(args.beta_lookback, args.corr_lookback) + 2

    if backend == "duckdb":
        ticker_map, bench_prices, by_ticker = fetch_prices_duckdb(candidates, n_days)
    else:
        ticker_map, bench_prices, by_ticker = fetch_prices_sqlite(candidates, n_days)

    print(f"Found {len(ticker_map)} trackable tickers.")

    # Compute excess returns
    excess, betas, raw_returns, bench_today = compute_excess_returns(
        by_ticker, bench_prices, ticker_map, args.beta_lookback)

    valid_tickers = [t for t in excess if len(excess[t]) >= args.vol_lookback]
    print(f"Computing correlations for {len(valid_tickers)} tickers with sufficient history...")

    print(f"{BENCHMARK}: {bench_today * 100:+.1f}%")

    # Build clusters
    clusters = build_clusters(excess, valid_tickers, args.corr_lookback,
                              args.corr_threshold, args.min_cluster)

    print(f"Found {len(clusters)} clusters (>={args.min_cluster} members)\n")

    # Score and display
    scored = []
    for cluster in clusters:
        result = score_cluster(cluster, excess, args.vol_lookback)
        if result is None:
            continue
        avg_ex, z, std, n_members = result
        scored.append((cluster, avg_ex, z, std, n_members))

    scored.sort(key=lambda x: abs(x[2]), reverse=True)

    flagged_count = 0
    for cluster, avg_ex, z, std, n_members in scored:
        is_flagged = abs(z) >= args.cluster_sigma
        if not is_flagged and not args.show_all:
            continue
        if is_flagged:
            flagged_count += 1

        direction = "UP" if avg_ex > 0 else "DOWN"
        marker = ">>>" if is_flagged else "   "
        avg_pct = avg_ex * 100

        # Compute average raw return and average beta for context
        raw_today = []
        cluster_betas = []
        for t in cluster:
            if raw_returns.get(t) and raw_returns[t][0] is not None:
                raw_today.append(raw_returns[t][0] * 100)
            if t in betas:
                cluster_betas.append(betas[t])
        avg_raw = sum(raw_today) / len(raw_today) if raw_today else 0
        avg_beta = sum(cluster_betas) / len(cluster_betas) if cluster_betas else 0

        print(f"{marker} CLUSTER [{n_members} members] -- {direction} {abs(avg_pct):.2f}% excess "
              f"(z={z:+.1f}, raw={avg_raw:+.1f}%, avg_beta={avg_beta:.2f})")

        # Show top members by individual excess return
        members = []
        for t in cluster:
            ex_today = excess[t][0] if excess[t][0] is not None else 0
            raw_today_val = raw_returns[t][0] * 100 if raw_returns.get(t) and raw_returns[t][0] is not None else 0
            members.append((t, ticker_map.get(t, t), raw_today_val, ex_today * 100, betas.get(t, 0)))
        members.sort(key=lambda x: x[3])  # sort by excess return

        if is_flagged or args.verbose:
            for t, actor, raw, ex, beta in members:
                print(f"      {t:<8} {actor:<28} raw={raw:+5.1f}%  excess={ex:+5.1f}%  beta={beta:.2f}")
        else:
            # Just show the ticker list
            tickers_str = ", ".join(t for t, _, _, _, _ in members[:8])
            if len(members) > 8:
                tickers_str += f" +{len(members) - 8} more"
            print(f"      {tickers_str}")
        print()

    if flagged_count == 0:
        print(f"No clusters exceeded {args.cluster_sigma} sigma.")
    else:
        print(f"--- {flagged_count} cluster(s) flagged at >={args.cluster_sigma} sigma ---")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        import traceback
        traceback.print_exc()
        sys.exit(1)
