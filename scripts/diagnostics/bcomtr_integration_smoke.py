"""Smoke checks for BCOM/BCOMTR ingestion and charting integration."""

from __future__ import annotations

import sys
from datetime import datetime, timezone
from pathlib import Path
from types import SimpleNamespace


ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "charting_app"))


def assert_true(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def unix_date(value: int | float) -> str:
    return datetime.fromtimestamp(value, tz=timezone.utc).strftime("%Y-%m-%d")


def check_update_market_data_wiring() -> None:
    import update_market_data as umd

    calls = []
    original_run = umd.subprocess.run
    original_history = umd.bcom_indices_have_history

    def fake_run(args, **kwargs):
        calls.append((args, kwargs))
        return SimpleNamespace(returncode=0, stderr=b"")

    try:
        umd.subprocess.run = fake_run

        umd.bcom_indices_have_history = lambda: True
        assert_true(umd.update_bcom_indices_data(verbose=False, lookback_days=5), "incremental BCOM update failed")
        assert_true(calls, "incremental BCOM update did not invoke importer")
        assert_true("--start-date" in calls[-1][0], "incremental BCOM update should pass --start-date")

        calls.clear()
        umd.bcom_indices_have_history = lambda: False
        assert_true(umd.update_bcom_indices_data(verbose=False, lookback_days=5), "full BCOM update failed")
        assert_true(calls, "full BCOM update did not invoke importer")
        assert_true("--start-date" not in calls[-1][0], "full BCOM update should omit --start-date")
    finally:
        umd.subprocess.run = original_run
        umd.bcom_indices_have_history = original_history


def check_charting_api_bcomtr() -> None:
    from charting_app.app import app
    import chart_routes

    chart_routes._check_playwright = lambda: True
    client = app.test_client()

    ticker_resp = client.get("/api/tickers")
    assert_true(ticker_resp.status_code == 200, f"/api/tickers returned {ticker_resp.status_code}")
    tickers = ticker_resp.get_json()
    assert_true("BCOMTR" in tickers, "BCOMTR missing from /api/tickers")

    metadata_resp = client.get("/api/metadata?tickers=BCOMTR")
    assert_true(metadata_resp.status_code == 200, f"/api/metadata returned {metadata_resp.status_code}")
    metadata = metadata_resp.get_json()
    assert_true(
        "Bloomberg Commodity Index" in metadata.get("BCOMTR", ""),
        "BCOMTR metadata does not resolve to Bloomberg Commodity Index",
    )

    data_resp = client.get("/api/data?tickers=BCOMTR&start=2026-01-01&end=2026-05-19")
    assert_true(data_resp.status_code == 200, f"/api/data returned {data_resp.status_code}")
    data = data_resp.get_json()
    points = data.get("BCOMTR", [])
    assert_true(points, "BCOMTR /api/data returned no points")
    assert_true(unix_date(points[0]["time"]) >= "2026-01-01", "BCOMTR start filter was not applied")
    assert_true(unix_date(points[-1]["time"]) <= "2026-05-19", "BCOMTR end filter was not applied")

    chart_resp = client.get("/api/chart/lw?tickers=BCOMTR&start=2026-01-01&format=html")
    assert_true(chart_resp.status_code == 200, f"/api/chart/lw returned {chart_resp.status_code}")
    html = chart_resp.get_data(as_text=True)
    assert_true("window.CHART_CONFIG" in html, "chart HTML did not include CHART_CONFIG")
    assert_true("BCOMTR" in html, "chart HTML did not include BCOMTR")


def main() -> int:
    checks = [
        check_update_market_data_wiring,
        check_charting_api_bcomtr,
    ]
    for check in checks:
        check()
        print(f"[OK] {check.__name__}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
