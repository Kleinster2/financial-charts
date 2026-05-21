#!/usr/bin/env python3
"""Discover Polymarket markets that may deserve vault watchlist coverage.

This is intentionally separate from refresh_kalshi_watchlist.py: discovery is
an exploratory, on-demand sweep, while freshness checks are deterministic daily
maintenance.

Usage:
  python scripts/discover_polymarket_markets.py openai tesla brazil
  python scripts/discover_polymarket_markets.py --json --max-candidates 10
  python scripts/discover_polymarket_markets.py --yaml-stubs bitcoin
"""

from __future__ import annotations

import argparse
from dataclasses import asdict, dataclass
from datetime import date, datetime
import json
from pathlib import Path
import sys
import time
from urllib.parse import urlencode
from urllib.request import Request, urlopen

import yaml


REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPTS_DIR = Path(__file__).resolve().parent
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

from refresh_kalshi_watchlist import (  # noqa: E402
    USER_AGENT,
    market_price,
    market_status,
    number,
)


DEFAULT_WATCHLIST = REPO_ROOT / "kalshi_watchlist.yml"
DEFAULT_QUERIES = [
    "OpenAI",
    "AI",
    "Tesla",
    "SpaceX",
    "Apple",
    "Bitcoin",
    "Ethereum",
    "Fed",
    "inflation",
    "tariffs",
    "Brazil election",
    "China",
    "Taiwan",
    "Ukraine",
    "oil",
    "nuclear",
]


@dataclass
class MarketSummary:
    question: str
    slug: str
    yes_price: float | None
    status: str | None
    volume: float
    liquidity: float


@dataclass
class Candidate:
    query: str
    title: str
    slug: str
    category: str
    volume: float
    volume_24h: float
    liquidity: float
    open_interest: float
    end_date: str
    market_count: int
    top_markets: list[MarketSummary]


def first_number(source: dict, *keys: str) -> float:
    for key in keys:
        value = number(source.get(key))
        if value is not None:
            return value
    return 0.0


def parse_dateish(value: object) -> date | None:
    if value is None:
        return None
    text = str(value).strip()
    if not text:
        return None
    try:
        return datetime.fromisoformat(text.replace("Z", "+00:00")).date()
    except ValueError:
        try:
            return date.fromisoformat(text[:10])
        except ValueError:
            return None


def end_date_text(source: dict) -> str:
    for key in ("endDate", "endDateIso", "closedTime", "umaEndDate", "umaEndDateIso"):
        value = source.get(key)
        if value:
            return str(value)
    return ""


def build_search_url(query: str, *, limit_per_type: int = 8, page: int = 1) -> str:
    params = {
        "q": query,
        "limit_per_type": limit_per_type,
        "page": page,
        "events_status": "active",
        "keep_closed_markets": 0,
        "search_profiles": "false",
        "cache": "true",
    }
    return "https://gamma-api.polymarket.com/public-search?" + urlencode(params)


def fetch_json(url: str) -> dict:
    req = Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
    with urlopen(req, timeout=30) as resp:
        payload = json.loads(resp.read().decode("utf-8"))
    if not isinstance(payload, dict):
        raise ValueError(f"Expected object response from {url}")
    return payload


def watched_polymarket_slugs(path: Path = DEFAULT_WATCHLIST) -> set[str]:
    if not path.exists():
        return set()
    with path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}

    watched: set[str] = set()
    for entry in data.get("markets") or []:
        if str(entry.get("provider") or "kalshi").lower() != "polymarket":
            continue
        source = str(entry.get("source_ticker") or "").strip()
        if source:
            watched.add(source)
        for tracked in entry.get("tracked_markets") or []:
            slug = str(tracked.get("slug") or "").strip()
            if slug:
                watched.add(slug)
    return watched


def event_markets(event: dict) -> list[dict]:
    markets = event.get("markets")
    if not isinstance(markets, list):
        return []
    return [
        market
        for market in markets
        if isinstance(market, dict)
        and market_status(market) == "active"
        and market.get("closed") is not True
    ]


def summarize_market(market: dict) -> MarketSummary:
    return MarketSummary(
        question=str(market.get("question") or market.get("title") or ""),
        slug=str(market.get("slug") or ""),
        yes_price=market_price(market, outcome="Yes"),
        status=market_status(market),
        volume=first_number(market, "volumeNum", "volume", "volumeClob", "volumeAmm"),
        liquidity=first_number(market, "liquidityNum", "liquidity", "liquidityClob", "liquidityAmm"),
    )


def candidate_from_event(query: str, event: dict) -> Candidate | None:
    if event.get("closed") is True or event.get("active") is False:
        return None
    slug = str(event.get("slug") or "").strip()
    title = str(event.get("title") or event.get("question") or "").strip()
    if not slug or not title:
        return None

    markets = event_markets(event)
    market_end_dates = [
        (parsed, text)
        for text in (end_date_text(market) for market in markets)
        if (parsed := parse_dateish(text)) is not None
    ]
    derived_end_date = end_date_text(event)
    if not derived_end_date and market_end_dates:
        derived_end_date = max(market_end_dates, key=lambda item: item[0])[1]
    top_markets = sorted(
        [summarize_market(market) for market in markets if market.get("slug")],
        key=lambda item: (item.volume, item.liquidity),
        reverse=True,
    )[:3]
    return Candidate(
        query=query,
        title=title,
        slug=slug,
        category=str(event.get("category") or event.get("subcategory") or ""),
        volume=first_number(event, "volume", "volumeNum"),
        volume_24h=first_number(event, "volume24hr", "volume_24hr"),
        liquidity=first_number(event, "liquidity", "liquidityNum", "liquidityClob"),
        open_interest=first_number(event, "openInterest", "open_interest"),
        end_date=derived_end_date,
        market_count=len(markets),
        top_markets=top_markets,
    )


def discover(
    queries: list[str],
    *,
    watched_slugs: set[str] | None = None,
    limit_per_type: int = 8,
    max_candidates: int = 20,
    min_volume: float = 0.0,
    min_liquidity: float = 0.0,
    min_days_to_end: int = 7,
    as_of: date | None = None,
    include_tracked: bool = False,
    delay: float = 0.2,
) -> list[Candidate]:
    watched_slugs = watched_slugs or set()
    as_of = as_of or date.today()
    by_slug: dict[str, Candidate] = {}

    for query in queries:
        payload = fetch_json(build_search_url(query, limit_per_type=limit_per_type))
        for event in payload.get("events") or []:
            if not isinstance(event, dict):
                continue
            candidate = candidate_from_event(query, event)
            if candidate is None:
                continue
            if not include_tracked and candidate.slug in watched_slugs:
                continue
            if candidate.volume < min_volume:
                continue
            if candidate.liquidity < min_liquidity:
                continue
            end_date = parse_dateish(candidate.end_date)
            if end_date is not None and (end_date - as_of).days < min_days_to_end:
                continue
            existing = by_slug.get(candidate.slug)
            if existing is None or score_candidate(candidate) > score_candidate(existing):
                by_slug[candidate.slug] = candidate
        if delay > 0:
            time.sleep(delay)

    return sorted(by_slug.values(), key=score_candidate, reverse=True)[:max_candidates]


def score_candidate(candidate: Candidate) -> tuple[float, float, float]:
    return (candidate.volume_24h, candidate.volume, candidate.liquidity)


def dollars(value: float) -> str:
    if value >= 1_000_000:
        return f"${value / 1_000_000:.1f}M"
    if value >= 1_000:
        return f"${value / 1_000:.0f}K"
    return f"${value:.0f}"


def percent(value: float | None) -> str:
    return "n/a" if value is None else f"{value:.1%}"


def clean_cell(value: str) -> str:
    return value.replace("|", "/").replace("\n", " ").strip()


def render_markdown(candidates: list[Candidate], *, as_of: date) -> str:
    lines = [
        f"### Polymarket discovery candidates ({as_of.isoformat()})",
        "",
        "| Rank | Query | Event | Slug | End | 24h Vol | Vol | Liq | Top markets |",
        "|---:|---|---|---|---|---:|---:|---:|---|",
    ]
    if not candidates:
        lines.append("| - | - | No untracked candidates matched the filters. | - | - | - | - | - | - |")
        return "\n".join(lines)

    for rank, candidate in enumerate(candidates, start=1):
        top = "; ".join(
            f"{clean_cell(market.question)} ({percent(market.yes_price)})"
            for market in candidate.top_markets
        )
        lines.append(
            "| "
            f"{rank} | "
            f"{clean_cell(candidate.query)} | "
            f"{clean_cell(candidate.title)} | "
            f"`{candidate.slug}` | "
            f"{clean_cell(candidate.end_date[:10])} | "
            f"{dollars(candidate.volume_24h)} | "
            f"{dollars(candidate.volume)} | "
            f"{dollars(candidate.liquidity)} | "
            f"{clean_cell(top)} |"
        )
    return "\n".join(lines)


def yaml_stub(candidate: Candidate, *, as_of: date) -> dict:
    return {
        "id": f"polymarket-{candidate.slug}",
        "provider": "polymarket",
        "note": "investing/Concepts/TODO.md",
        "note_link": "TODO",
        "source_kind": "event_slug",
        "source_ticker": candidate.slug,
        "cadence": "weekly",
        "last_read": as_of.isoformat(),
        "thesis": f"TODO: why {candidate.title} is a useful vault overlay.",
        "tracked_markets": [
            {
                "slug": market.slug,
                "outcome": "Yes",
                "label": market.question,
                "last_price": round(market.yes_price, 4) if market.yes_price is not None else None,
                "status": market.status,
            }
            for market in candidate.top_markets
        ],
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Discover vault-relevant Polymarket candidates")
    parser.add_argument("queries", nargs="*", help="Search terms; defaults to broad vault-relevant topics")
    parser.add_argument("--watchlist", default=str(DEFAULT_WATCHLIST), help="Existing watchlist YAML")
    parser.add_argument("--limit-per-type", type=int, default=8, help="Polymarket search results per type")
    parser.add_argument("--max-candidates", type=int, default=20, help="Maximum candidates to print")
    parser.add_argument("--min-volume", type=float, default=0.0, help="Minimum event lifetime volume")
    parser.add_argument("--min-liquidity", type=float, default=0.0, help="Minimum event liquidity")
    parser.add_argument(
        "--min-days-to-end",
        type=int,
        default=7,
        help="Skip events ending sooner than this many days from --date",
    )
    parser.add_argument("--include-tracked", action="store_true", help="Do not filter existing watchlist slugs")
    parser.add_argument("--delay", type=float, default=0.2, help="Delay between search API requests")
    parser.add_argument("--json", action="store_true", help="Print JSON instead of markdown")
    parser.add_argument("--yaml-stubs", action="store_true", help="Append watchlist YAML stubs after markdown")
    parser.add_argument("--date", default=date.today().isoformat(), help="As-of date for generated stubs")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    queries = args.queries or DEFAULT_QUERIES
    as_of = date.fromisoformat(args.date)
    watchlist = Path(args.watchlist)
    if not watchlist.is_absolute():
        watchlist = REPO_ROOT / watchlist

    candidates = discover(
        queries,
        watched_slugs=watched_polymarket_slugs(watchlist),
        limit_per_type=args.limit_per_type,
        max_candidates=args.max_candidates,
        min_volume=args.min_volume,
        min_liquidity=args.min_liquidity,
        min_days_to_end=args.min_days_to_end,
        as_of=as_of,
        include_tracked=args.include_tracked,
        delay=args.delay,
    )

    if args.json:
        print(json.dumps([asdict(candidate) for candidate in candidates], indent=2))
        return 0

    print(render_markdown(candidates, as_of=as_of))
    if args.yaml_stubs and candidates:
        print("\n```yaml")
        print(yaml.safe_dump([yaml_stub(candidate, as_of=as_of) for candidate in candidates], sort_keys=False))
        print("```")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
