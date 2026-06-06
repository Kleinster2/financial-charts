#!/usr/bin/env python
"""
Shared utilities for FRED (Federal Reserve Economic Data) operations.
"""
import logging
from io import StringIO

import pandas as pd

from http_utils import FetchError, fetch_with_retry

logger = logging.getLogger(__name__)

# Default cache directory for FRED data (set to None to disable)
FRED_CACHE_DIR = None  # e.g., ".http_cache/fred"
FRED_CACHE_TTL = 24 * 3600  # 24 hours


def _format_fred_date(value) -> str:
    """Format date-like values for FRED graph CSV query parameters."""
    return value.strftime("%Y-%m-%d") if hasattr(value, "strftime") else str(value)[:10]


def merge_fred_series_column(existing: pd.DataFrame, series_id: str, df: pd.DataFrame) -> pd.DataFrame:
    """Merge one FRED series into a wide cache without dropping new dates."""
    if existing.empty:
        return df

    merged = existing.reindex(existing.index.union(df.index)).sort_index()
    if series_id in merged.columns:
        merged[series_id] = df[series_id].combine_first(merged[series_id])
    else:
        merged[series_id] = df[series_id]
    return merged


def download_from_fred(
    fred_code: str,
    retries: int = 3,
    timeout: float = 30.0,
    cache_dir: str = None,
    cache_ttl_s: float = None,
    start_date=None,
    end_date=None,
):
    """
    Download data from FRED with retry/backoff.

    Args:
        fred_code: FRED series code (e.g., 'DGS10', 'RVXCLS')
        retries: Number of retry attempts (default: 3)
        timeout: Request timeout in seconds (default: 30)
        cache_dir: Directory for disk cache (None to disable)
        cache_ttl_s: Cache TTL in seconds (None for module default)
        start_date: Optional first observation date. Uses FRED graph CSV's
            cosd parameter to avoid downloading full daily histories.
        end_date: Optional last observation date. Uses FRED graph CSV's coed
            parameter.

    Returns:
        DataFrame with Date index and Close column, or None on error
    """
    cache_dir = cache_dir or FRED_CACHE_DIR
    cache_ttl_s = cache_ttl_s if cache_ttl_s is not None else FRED_CACHE_TTL

    try:
        params = {"id": fred_code}
        if start_date is not None:
            params["cosd"] = _format_fred_date(start_date)
        if end_date is not None:
            params["coed"] = _format_fred_date(end_date)

        text = fetch_with_retry(
            "https://fred.stlouisfed.org/graph/fredgraph.csv",
            params=params,
            retries=retries,
            backoff=2.0,
            timeout=timeout,
            cache_dir=cache_dir,
            cache_ttl_s=cache_ttl_s if cache_dir else None,
        )
        df = pd.read_csv(StringIO(text))
        df.columns = ["Date", "Close"]
        df["Date"] = pd.to_datetime(df["Date"])
        df.set_index("Date", inplace=True)
        return df.dropna()

    except FetchError as e:
        logger.error(f"FRED fetch failed for {fred_code}: {e}")
        print(f"  ERROR: {e.kind} - {str(e)[:80]}")
        return None
    except Exception as e:
        logger.error(f"FRED parse failed for {fred_code}: {e}")
        print(f"  ERROR: {str(e)[:50]}")
        return None
