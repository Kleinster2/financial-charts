#!/usr/bin/env python3
"""Check and optionally refresh prediction-market overlay freshness.

The watchlist treats Kalshi and Polymarket data as expiring note overlays.
Offline mode checks whether stored snapshots are stale. Live mode fetches public
APIs and flags material price moves, status changes, or missing contracts.

Usage:
  python scripts/refresh_kalshi_watchlist.py
  python scripts/refresh_kalshi_watchlist.py --refresh
  python scripts/refresh_kalshi_watchlist.py --refresh --update-state
  python scripts/refresh_kalshi_watchlist.py --json
"""

from __future__ import annotations

import argparse
from dataclasses import asdict, dataclass
from datetime import date, datetime
import json
from pathlib import Path
import sys
import time
from urllib.parse import quote, urlencode
from urllib.error import HTTPError
from urllib.request import Request, urlopen

import yaml


REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_CONFIG = REPO_ROOT / "kalshi_watchlist.yml"
DEFAULT_STALE_AFTER = {
    "daily": 2,
    "weekly": 8,
    "monthly": 35,
    "quarterly": 100,
}
USER_AGENT = "financial-charts-prediction-market-watchlist/1.0"


@dataclass
class Alert:
    level: str
    kind: str
    watch_id: str
    note: str
    message: str


def parse_iso_date(value: object) -> date | None:
    if value is None:
        return None
    if isinstance(value, date) and not isinstance(value, datetime):
        return value
    text = str(value).strip()
    if not text:
        return None
    return datetime.strptime(text, "%Y-%m-%d").date()


def number(value: object) -> float | None:
    if value is None:
        return None
    if isinstance(value, (int, float)):
        return float(value)
    text = str(value).replace("$", "").replace(",", "").strip()
    if not text:
        return None
    try:
        return float(text)
    except ValueError:
        return None


def parse_json_array(value: object) -> list[object]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    text = str(value).strip()
    if not text:
        return []
    try:
        parsed = json.loads(text)
    except json.JSONDecodeError:
        return []
    return parsed if isinstance(parsed, list) else []


def market_status(market: dict) -> str | None:
    if market.get("status") is not None:
        return str(market["status"])
    if market.get("closed") is True:
        return "closed"
    if market.get("active") is True:
        return "active"
    if market.get("active") is False:
        return "inactive"
    return None


def market_ids(market: dict) -> list[str]:
    ids: list[str] = []
    for key in ("ticker", "slug", "id", "conditionId", "condition_id"):
        value = market.get(key)
        if value:
            ids.append(str(value))
    return ids


def tracked_market_id(tracked_market: dict) -> str:
    for key in ("ticker", "slug", "id", "condition_id", "conditionId"):
        value = tracked_market.get(key)
        if value:
            return str(value).strip()
    return ""


def market_close_time(market: dict) -> str | None:
    for key in ("close_time", "closedTime", "endDate", "endDateIso"):
        value = market.get(key)
        if value:
            return str(value)
    return None


def market_price(market: dict, *, outcome: str | None = None) -> float | None:
    outcomes = [str(item) for item in parse_json_array(market.get("outcomes"))]
    prices = parse_json_array(market.get("outcomePrices"))
    if prices:
        desired = outcome or "Yes"
        index = 0
        for i, item in enumerate(outcomes):
            if item.lower() == desired.lower():
                index = i
                break
        if index < len(prices):
            value = number(prices[index])
            if value is not None:
                return value

    for key in ("last_price_dollars", "last_price"):
        value = number(market.get(key))
        if value is not None:
            return value

    value = number(market.get("lastTradePrice"))
    if value is not None:
        return value

    bid = number(market.get("yes_bid_dollars") or market.get("yes_bid"))
    ask = number(market.get("yes_ask_dollars") or market.get("yes_ask"))
    if bid is None and ask is None:
        bid = number(market.get("bestBid"))
        ask = number(market.get("bestAsk"))
    if bid is not None and ask is not None:
        return (bid + ask) / 2
    return bid if bid is not None else ask


def build_api_url(entry: dict) -> str:
    if entry.get("api_url"):
        return str(entry["api_url"])

    provider = str(entry.get("provider") or "kalshi").lower()
    source_kind = entry.get("source_kind")
    source_ticker = entry.get("source_ticker")
    if not source_ticker:
        raise ValueError(f"{entry.get('id', '<unknown>')}: provide api_url or source_ticker")

    if provider == "kalshi":
        if source_kind not in {"series_ticker", "event_ticker"}:
            raise ValueError(
                f"{entry.get('id', '<unknown>')}: Kalshi requires series_ticker or event_ticker"
            )
        params = {"limit": 1000, source_kind: source_ticker}
        return "https://external-api.kalshi.com/trade-api/v2/markets?" + urlencode(params)

    if provider == "polymarket":
        slug = quote(str(source_ticker).strip(), safe="")
        if source_kind == "event_slug":
            return f"https://gamma-api.polymarket.com/events/slug/{slug}"
        if source_kind == "market_slug":
            return f"https://gamma-api.polymarket.com/markets/slug/{slug}"
        if source_kind == "market_id":
            return f"https://gamma-api.polymarket.com/markets/{slug}"
        raise ValueError(
            f"{entry.get('id', '<unknown>')}: Polymarket requires event_slug, market_slug, or market_id"
        )

    raise ValueError(f"{entry.get('id', '<unknown>')}: unsupported provider {provider}")


def fetch_markets(api_url: str, *, retries: int = 2) -> list[dict]:
    req = Request(api_url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
    for attempt in range(retries + 1):
        try:
            with urlopen(req, timeout=30) as resp:
                payload = json.loads(resp.read().decode("utf-8"))
            break
        except HTTPError as exc:
            if exc.code != 429 or attempt >= retries:
                raise
            retry_after = number(exc.headers.get("Retry-After")) or (2.0 * (attempt + 1))
            time.sleep(float(retry_after))
    if isinstance(payload, list):
        markets = payload
    elif isinstance(payload, dict) and isinstance(payload.get("markets"), list):
        markets = payload["markets"]
    elif isinstance(payload, dict) and (payload.get("slug") or payload.get("conditionId")):
        markets = [payload]
    else:
        raise ValueError(f"Prediction-market response missing market data for {api_url}")
    return markets


def load_config(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    if not isinstance(data.get("markets"), list):
        raise ValueError(f"{path} must contain a top-level markets list")
    return data


def stale_after_days(entry: dict, defaults: dict) -> int:
    if entry.get("stale_after_days") is not None:
        return int(entry["stale_after_days"])
    cadence = entry.get("cadence", defaults.get("cadence", "weekly"))
    by_cadence = defaults.get("stale_after_by_cadence", DEFAULT_STALE_AFTER)
    return int(by_cadence.get(cadence, DEFAULT_STALE_AFTER["weekly"]))


def material_move_pp(entry: dict, market: dict, defaults: dict) -> float:
    if market.get("material_move_pp") is not None:
        return float(market["material_move_pp"])
    if entry.get("material_move_pp") is not None:
        return float(entry["material_move_pp"])
    return float(defaults.get("material_move_pp", 10.0))


def note_label(entry: dict) -> str:
    if entry.get("note_link"):
        return str(entry["note_link"])
    if entry.get("note"):
        return Path(str(entry["note"])).stem
    return ""


def evaluate_entry(
    entry: dict,
    *,
    as_of: date,
    defaults: dict,
    fetched_markets: list[dict] | None = None,
) -> list[Alert]:
    alerts: list[Alert] = []
    watch_id = str(entry.get("id") or entry.get("source_ticker") or "<unknown>")
    note = note_label(entry)

    last_read = parse_iso_date(entry.get("last_read"))
    if last_read is None:
        alerts.append(Alert("stale", "missing-read-date", watch_id, note, "missing last_read"))
    else:
        age = (as_of - last_read).days
        allowed = stale_after_days(entry, defaults)
        if age > allowed:
            alerts.append(
                Alert(
                    "stale",
                    "stale",
                    watch_id,
                    note,
                    f"last read {age} days ago; cadence allows {allowed}",
                )
            )

    if fetched_markets is None:
        return alerts

    by_id: dict[str, dict] = {}
    for market in fetched_markets:
        for identifier in market_ids(market):
            by_id[identifier] = market
    tracked = entry.get("tracked_markets") or []
    if not tracked:
        active = sum(1 for m in fetched_markets if market_status(m) == "active")
        if active == 0:
            alerts.append(
                Alert("review", "no-active-markets", watch_id, note, "source returned no active markets")
            )
        return alerts

    for tracked_market in tracked:
        identifier = tracked_market_id(tracked_market)
        if not identifier:
            continue
        current = by_id.get(identifier)
        if current is None:
            alerts.append(Alert("review", "missing-contract", watch_id, note, f"{identifier} not found"))
            continue

        old_status = tracked_market.get("status")
        new_status = market_status(current)
        if old_status and new_status and str(old_status) != str(new_status):
            alerts.append(
                Alert(
                    "material",
                    "status-change",
                    watch_id,
                    note,
                    f"{identifier} status changed {old_status} -> {new_status}",
                )
            )

        old_price = number(tracked_market.get("last_price"))
        new_price = market_price(current, outcome=tracked_market.get("outcome"))
        if old_price is None or new_price is None:
            continue

        delta_pp = (new_price - old_price) * 100
        threshold = material_move_pp(entry, tracked_market, defaults)
        if abs(delta_pp) >= threshold:
            alerts.append(
                Alert(
                    "material",
                    "price-move",
                    watch_id,
                    note,
                    f"{identifier} moved {old_price:.1%} -> {new_price:.1%} ({delta_pp:+.1f}pp)",
                )
            )

    return alerts


def build_report(
    config: dict,
    *,
    as_of: date,
    refresh: bool = False,
    delay: float = 0.5,
) -> tuple[dict, dict[str, list[dict]]]:
    defaults = config.get("defaults") or {}
    fetched_by_id: dict[str, list[dict]] = {}
    alerts: list[Alert] = []

    api_cache: dict[str, list[dict]] = {}
    for entry in config["markets"]:
        watch_id = str(entry.get("id") or entry.get("source_ticker") or "<unknown>")
        fetched_markets = None
        if refresh:
            try:
                url = build_api_url(entry)
                if url not in api_cache:
                    api_cache[url] = fetch_markets(url)
                    if delay > 0:
                        time.sleep(delay)
                fetched_markets = api_cache[url]
                fetched_by_id[watch_id] = fetched_markets
            except Exception as exc:
                alerts.append(
                    Alert("review", "fetch-error", watch_id, note_label(entry), str(exc))
                )

        alerts.extend(
            evaluate_entry(
                entry,
                as_of=as_of,
                defaults=defaults,
                fetched_markets=fetched_markets,
            )
        )

    serialized = [asdict(alert) for alert in alerts]
    report = {
        "as_of": as_of.isoformat(),
        "entries": len(config["markets"]),
        "alerts": serialized,
        "counts": {
            "stale": sum(1 for alert in alerts if alert.level == "stale"),
            "material": sum(1 for alert in alerts if alert.level == "material"),
            "review": sum(1 for alert in alerts if alert.level == "review"),
        },
    }
    return report, fetched_by_id


def update_state(config: dict, *, as_of: date, fetched_by_id: dict[str, list[dict]]) -> None:
    for entry in config["markets"]:
        watch_id = str(entry.get("id") or entry.get("source_ticker") or "<unknown>")
        markets = fetched_by_id.get(watch_id)
        if markets is None:
            continue
        entry["last_read"] = as_of.isoformat()
        by_id: dict[str, dict] = {}
        for market in markets:
            for identifier in market_ids(market):
                by_id[identifier] = market
        for tracked in entry.get("tracked_markets") or []:
            current = by_id.get(tracked_market_id(tracked))
            if current is None:
                continue
            price = market_price(current, outcome=tracked.get("outcome"))
            if price is not None:
                tracked["last_price"] = round(price, 4)
            status = market_status(current)
            if status:
                tracked["status"] = status
            close_time = market_close_time(current)
            if close_time:
                tracked["close_time"] = close_time


def markdown_report(report: dict) -> str:
    counts = report["counts"]
    lines = [
        f"### Prediction-market watchlist freshness ({report['as_of']})",
        "",
        (
            f"- Tracked overlays: {report['entries']}; "
            f"stale: {counts['stale']}; material: {counts['material']}; review: {counts['review']}."
        ),
    ]
    if not report["alerts"]:
        lines.append("- No stale or material prediction-market overlay alerts.")
        return "\n".join(lines)

    lines.extend(
        [
            "",
            "| Level | Kind | Watch | Note | Message |",
            "|---|---|---|---|---|",
        ]
    )
    for alert in report["alerts"]:
        note = f"[[{alert['note']}]]" if alert.get("note") else ""
        lines.append(
            f"| {alert['level']} | {alert['kind']} | `{alert['watch_id']}` | {note} | {alert['message']} |"
        )
    return "\n".join(lines)


def append_daily(markdown: str, as_of: date) -> Path:
    path = REPO_ROOT / "investing" / "Daily" / f"{as_of.isoformat()}.md"
    if path.exists():
        content = path.read_text(encoding="utf-8")
    else:
        content = "#daily\n\n## Notes created/expanded\n\n"

    insert = "\n" + markdown.rstrip() + "\n"
    marker = "\n## Edit log"
    if marker in content:
        content = content.replace(marker, insert + marker, 1)
    else:
        content = content.rstrip() + "\n" + insert
    path.write_text(content, encoding="utf-8")
    return path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Check prediction-market overlay freshness")
    parser.add_argument("--config", default=str(DEFAULT_CONFIG), help="Watchlist YAML path")
    parser.add_argument("--date", default=date.today().isoformat(), help="As-of date, YYYY-MM-DD")
    parser.add_argument("--refresh", action="store_true", help="Fetch public APIs and compare prices/status")
    parser.add_argument("--delay", type=float, default=0.5, help="Delay between live API requests in seconds")
    parser.add_argument("--update-state", action="store_true", help="Write refreshed prices/read date back to YAML")
    parser.add_argument("--append-daily", action="store_true", help="Append markdown alert report to today's daily note")
    parser.add_argument("--json", action="store_true", help="Print machine-readable JSON")
    parser.add_argument("--strict", action="store_true", help="Exit 1 when any alert is present")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    config_path = Path(args.config)
    if not config_path.is_absolute():
        config_path = REPO_ROOT / config_path

    as_of = parse_iso_date(args.date)
    if as_of is None:
        raise SystemExit(f"Invalid --date: {args.date}")

    if args.update_state and not args.refresh:
        raise SystemExit("--update-state requires --refresh")

    config = load_config(config_path)
    report, fetched_by_id = build_report(
        config,
        as_of=as_of,
        refresh=args.refresh,
        delay=args.delay,
    )

    if args.update_state:
        update_state(config, as_of=as_of, fetched_by_id=fetched_by_id)
        config_path.write_text(
            yaml.safe_dump(config, sort_keys=False, allow_unicode=True, width=120),
            encoding="utf-8",
        )

    if args.json:
        print(json.dumps(report, indent=2))
    else:
        rendered = markdown_report(report)
        print(rendered)
        if args.append_daily:
            path = append_daily(rendered, as_of)
            print(f"\nAppended to {path.relative_to(REPO_ROOT).as_posix()}")

    if args.strict and report["alerts"]:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
