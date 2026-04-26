"""
Short-interest synthetic ticker helpers.

Synthetic tickers:
    AAPL_SI_PCT  -> short_percent_float, displayed as percent points
    AAPL_SI_DAYS -> days_to_cover
"""
import logging
import os
import sqlite3
import sys
from dataclasses import dataclass
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

import pandas as pd

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from constants import get_db_connection, resolve_ticker_alias

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class SISyntheticTicker:
    ticker: str
    base_ticker: str
    db_ticker: str
    suffix: str
    column: str
    scale: float


SI_SYNTHETIC_METRICS = {
    "_SI_PCT": {"column": "short_percent_float", "scale": 100.0},
    "_SI_DAYS": {"column": "days_to_cover", "scale": 1.0},
}


def parse_si_ticker(ticker: str) -> Optional[SISyntheticTicker]:
    """Parse AAPL_SI_PCT style tickers into DB lookup details."""
    normalized = (ticker or "").strip().upper()
    for suffix, config in SI_SYNTHETIC_METRICS.items():
        if normalized.endswith(suffix) and len(normalized) > len(suffix):
            base = normalized[:-len(suffix)]
            return SISyntheticTicker(
                ticker=normalized,
                base_ticker=base,
                db_ticker=resolve_ticker_alias(base),
                suffix=suffix,
                column=config["column"],
                scale=config["scale"],
            )
    return None


def split_si_tickers(tickers: Iterable[str]) -> Tuple[List[str], List[str]]:
    """Return (si_tickers, regular_tickers), preserving input order."""
    si_tickers = []
    regular_tickers = []
    for ticker in tickers:
        normalized = (ticker or "").strip().upper()
        if not normalized:
            continue
        if parse_si_ticker(normalized):
            si_tickers.append(normalized)
        else:
            regular_tickers.append(normalized)
    return si_tickers, regular_tickers


def get_si_synthetic_tickers(conn=None) -> List[str]:
    """Return available synthetic SI tickers for metrics that have data."""
    close_conn = conn is None
    if conn is None:
        conn = get_db_connection(row_factory=None)

    try:
        rows = conn.execute(
            """
            SELECT ticker,
                   MAX(CASE WHEN short_percent_float IS NOT NULL THEN 1 ELSE 0 END) AS has_pct,
                   MAX(CASE WHEN days_to_cover IS NOT NULL THEN 1 ELSE 0 END) AS has_days
            FROM short_interest
            GROUP BY ticker
            ORDER BY ticker
            """
        ).fetchall()
    except sqlite3.OperationalError:
        return []
    finally:
        if close_conn:
            conn.close()

    tickers = []
    for ticker, has_pct, has_days in rows:
        if has_pct:
            tickers.append(f"{ticker}_SI_PCT")
        if has_days:
            tickers.append(f"{ticker}_SI_DAYS")
    return sorted(set(tickers))


def get_si_chart_data(
    synthetic_tickers: Sequence[str],
    start_date: str = "",
    end_date: str = "",
    time_format: str = "timestamp",
    align_dates_by_base: Optional[Dict[str, Sequence[str]]] = None,
) -> Dict[str, List[dict]]:
    """Return chart-ready data for synthetic SI tickers."""
    result: Dict[str, List[dict]] = {}
    if not synthetic_tickers:
        return result

    conn = get_db_connection(row_factory=None)
    try:
        for ticker in synthetic_tickers:
            parsed = parse_si_ticker(ticker)
            if not parsed:
                continue

            date_points = None
            if align_dates_by_base:
                date_points = (
                    align_dates_by_base.get(parsed.base_ticker)
                    or align_dates_by_base.get(parsed.db_ticker)
                )

            result[parsed.ticker] = get_si_series(
                parsed,
                start_date=start_date,
                end_date=end_date,
                time_format=time_format,
                date_points=date_points,
                conn=conn,
            )
    finally:
        conn.close()

    return result


def get_si_series(
    parsed: SISyntheticTicker,
    start_date: str = "",
    end_date: str = "",
    time_format: str = "timestamp",
    date_points: Optional[Sequence[str]] = None,
    conn=None,
) -> List[dict]:
    """Forward-fill a short-interest metric onto trading dates."""
    close_conn = conn is None
    if conn is None:
        conn = get_db_connection(row_factory=None)

    try:
        si_points = _get_si_points(conn, parsed, end_date=end_date)
        if not si_points:
            return []

        if date_points is None:
            dates = _get_trading_dates(
                conn,
                parsed.db_ticker,
                start_date=start_date,
                end_date=end_date,
            )
        else:
            dates = [_normalize_date(d) for d in date_points]
            dates = [d for d in dates if d]
            dates = _filter_dates(dates, start_date=start_date, end_date=end_date)

        if not dates:
            dates = _filter_dates([d for d, _ in si_points], start_date=start_date, end_date=end_date)

        dates = sorted(set(dates))
        result = []
        si_idx = 0
        current_value = None

        for date_str in dates:
            while si_idx < len(si_points) and si_points[si_idx][0] <= date_str:
                current_value = si_points[si_idx][1]
                si_idx += 1

            if current_value is not None:
                chart_time = _format_time(date_str, time_format)
                if chart_time is not None:
                    result.append({"time": chart_time, "value": current_value})

        return result
    except sqlite3.OperationalError as e:
        logger.warning("SI synthetic query failed for %s: %s", parsed.ticker, e)
        return []
    finally:
        if close_conn:
            conn.close()


def _get_si_points(conn, parsed: SISyntheticTicker, end_date: str = "") -> List[Tuple[str, float]]:
    query = f"""
        SELECT settlement_date, {parsed.column}
        FROM short_interest
        WHERE ticker = ? AND {parsed.column} IS NOT NULL
    """
    params = [parsed.db_ticker]
    if end_date:
        query += " AND date(settlement_date) <= date(?)"
        params.append(end_date)
    query += " ORDER BY date(settlement_date) ASC"

    rows = conn.execute(query, params).fetchall()
    points = []
    for settlement_date, value in rows:
        date_str = _normalize_date(settlement_date)
        if date_str and value is not None:
            points.append((date_str, float(value) * parsed.scale))
    return points


def _get_trading_dates(conn, ticker: str, start_date: str = "", end_date: str = "") -> List[str]:
    dates: List[str] = []

    for table in ("prices_long", "futures_prices_long"):
        dates.extend(_get_long_table_dates(conn, table, ticker, start_date, end_date))

    if not dates:
        for table in ("stock_prices_daily", "futures_prices_daily", "bond_prices_daily"):
            dates.extend(_get_wide_table_dates(conn, table, ticker, start_date, end_date))

    return sorted(set(dates))


def _get_long_table_dates(conn, table: str, ticker: str, start_date: str, end_date: str) -> List[str]:
    query = f"""
        SELECT date(Date) AS d
        FROM {table}
        WHERE Ticker = ? AND Close IS NOT NULL
    """
    params = [ticker]
    if start_date:
        query += " AND date(Date) >= date(?)"
        params.append(start_date)
    if end_date:
        query += " AND date(Date) <= date(?)"
        params.append(end_date)
    query += " ORDER BY date(Date)"

    try:
        return [row[0] for row in conn.execute(query, params).fetchall() if row[0]]
    except sqlite3.OperationalError:
        return []


def _get_wide_table_dates(conn, table: str, ticker: str, start_date: str, end_date: str) -> List[str]:
    if not _table_has_column(conn, table, ticker):
        return []

    safe_ticker = ticker.replace('"', '""')
    query = f'SELECT date(Date) AS d FROM {table} WHERE "{safe_ticker}" IS NOT NULL'
    params = []
    if start_date:
        query += " AND date(Date) >= date(?)"
        params.append(start_date)
    if end_date:
        query += " AND date(Date) <= date(?)"
        params.append(end_date)
    query += " ORDER BY date(Date)"

    try:
        return [row[0] for row in conn.execute(query, params).fetchall() if row[0]]
    except sqlite3.OperationalError:
        return []


def _table_has_column(conn, table: str, column: str) -> bool:
    try:
        rows = conn.execute(f"PRAGMA table_info({table})").fetchall()
    except sqlite3.OperationalError:
        return False
    return column in {row[1] for row in rows}


def _filter_dates(dates: Sequence[str], start_date: str = "", end_date: str = "") -> List[str]:
    start_norm = _normalize_date(start_date) if start_date else ""
    end_norm = _normalize_date(end_date) if end_date else ""
    filtered = []
    for date_str in dates:
        normalized = _normalize_date(date_str)
        if not normalized:
            continue
        if start_norm and normalized < start_norm:
            continue
        if end_norm and normalized > end_norm:
            continue
        filtered.append(normalized)
    return filtered


def _normalize_date(value) -> str:
    if value in (None, ""):
        return ""
    try:
        return pd.to_datetime(value).strftime("%Y-%m-%d")
    except Exception:
        return ""


def _format_time(date_str: str, time_format: str):
    if time_format == "date":
        return date_str
    try:
        return int(pd.Timestamp(date_str).value // 10**9)
    except Exception:
        return None
