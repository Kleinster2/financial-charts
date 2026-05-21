import unittest
from datetime import date
from pathlib import Path
import sys
from urllib.parse import parse_qs, urlparse

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.refresh_kalshi_watchlist import build_api_url, build_report, evaluate_entry, market_price
from scripts.discover_polymarket_markets import (
    build_search_url,
    candidate_from_event,
    yaml_stub,
)


DEFAULTS = {
    "stale_after_by_cadence": {"weekly": 8},
    "material_move_pp": 10,
}


class KalshiWatchlistTests(unittest.TestCase):
    def test_flags_stale_overlay(self) -> None:
        entry = {
            "id": "test-market",
            "note_link": "Test note",
            "cadence": "weekly",
            "last_read": "2026-05-01",
        }

        alerts = evaluate_entry(
            entry,
            as_of=date(2026, 5, 20),
            defaults=DEFAULTS,
        )

        self.assertEqual(len(alerts), 1)
        self.assertEqual(alerts[0].kind, "stale")
        self.assertIn("19 days", alerts[0].message)

    def test_flags_material_price_move(self) -> None:
        entry = {
            "id": "test-market",
            "note_link": "Test note",
            "cadence": "weekly",
            "last_read": "2026-05-20",
            "tracked_markets": [
                {"ticker": "KXTEST", "last_price": 0.25, "status": "active"}
            ],
        }
        fetched = [
            {
                "ticker": "KXTEST",
                "status": "active",
                "last_price_dollars": "0.38",
            }
        ]

        alerts = evaluate_entry(
            entry,
            as_of=date(2026, 5, 20),
            defaults=DEFAULTS,
            fetched_markets=fetched,
        )

        self.assertEqual(len(alerts), 1)
        self.assertEqual(alerts[0].kind, "price-move")
        self.assertIn("+13.0pp", alerts[0].message)

    def test_reads_polymarket_outcome_prices_by_slug(self) -> None:
        entry = {
            "id": "brazil-election",
            "provider": "polymarket",
            "source_kind": "event_slug",
            "source_ticker": "brazil-presidential-election",
            "note_link": "Prediction markets",
            "cadence": "weekly",
            "last_read": "2026-05-20",
            "tracked_markets": [
                {
                    "slug": "will-luiz-incio-lula-da-silva-win-the-2026-brazilian-presidential-election",
                    "outcome": "Yes",
                    "last_price": 0.455,
                    "status": "active",
                }
            ],
        }
        fetched = [
            {
                "slug": "will-luiz-incio-lula-da-silva-win-the-2026-brazilian-presidential-election",
                "active": True,
                "closed": False,
                "outcomes": '["Yes", "No"]',
                "outcomePrices": '["0.58", "0.42"]',
            }
        ]

        alerts = evaluate_entry(
            entry,
            as_of=date(2026, 5, 20),
            defaults=DEFAULTS,
            fetched_markets=fetched,
        )

        self.assertEqual(len(alerts), 1)
        self.assertEqual(alerts[0].kind, "price-move")
        self.assertIn("+12.5pp", alerts[0].message)

    def test_builds_polymarket_event_slug_url(self) -> None:
        url = build_api_url(
            {
                "id": "brazil-election",
                "provider": "polymarket",
                "source_kind": "event_slug",
                "source_ticker": "brazil-presidential-election",
            }
        )

        self.assertEqual(
            url,
            "https://gamma-api.polymarket.com/events/slug/brazil-presidential-election",
        )

    def test_polymarket_price_falls_back_to_bid_ask(self) -> None:
        price = market_price({"bestBid": 0.45, "bestAsk": 0.47})

        self.assertAlmostEqual(price, 0.46)

    def test_build_report_counts_alerts(self) -> None:
        config = {
            "defaults": DEFAULTS,
            "markets": [
                {
                    "id": "fresh",
                    "note_link": "Fresh",
                    "last_read": "2026-05-20",
                },
                {
                    "id": "stale",
                    "note_link": "Stale",
                    "last_read": "2026-04-01",
                },
            ],
        }

        report, _ = build_report(config, as_of=date(2026, 5, 20), refresh=False)

        self.assertEqual(report["entries"], 2)
        self.assertEqual(report["counts"]["stale"], 1)
        self.assertEqual(report["counts"]["material"], 0)

    def test_builds_polymarket_search_url(self) -> None:
        url = build_search_url("OpenAI hardware", limit_per_type=3)
        parsed = urlparse(url)
        params = parse_qs(parsed.query)

        self.assertEqual(parsed.netloc, "gamma-api.polymarket.com")
        self.assertEqual(parsed.path, "/public-search")
        self.assertEqual(params["q"], ["OpenAI hardware"])
        self.assertEqual(params["limit_per_type"], ["3"])
        self.assertEqual(params["events_status"], ["active"])

    def test_summarizes_polymarket_discovery_candidate(self) -> None:
        candidate = candidate_from_event(
            "OpenAI",
            {
                "slug": "openai-ipo-before-2027",
                "title": "OpenAI IPO before 2027?",
                "active": True,
                "closed": False,
                "volume": "1500000",
                "volume24hr": "25000",
                "liquidity": "75000",
                "openInterest": "5000",
                "markets": [
                    {
                        "slug": "will-openai-ipo-before-2027",
                        "question": "Will OpenAI IPO before 2027?",
                        "active": True,
                        "closed": False,
                        "endDateIso": "2026-12-31T23:59:59Z",
                        "outcomes": '["Yes", "No"]',
                        "outcomePrices": '["0.32", "0.68"]',
                        "volumeNum": "1500000",
                        "liquidityNum": "75000",
                    }
                ],
            },
        )

        self.assertIsNotNone(candidate)
        assert candidate is not None
        self.assertEqual(candidate.slug, "openai-ipo-before-2027")
        self.assertEqual(candidate.market_count, 1)
        self.assertEqual(candidate.end_date, "2026-12-31T23:59:59Z")
        self.assertEqual(candidate.top_markets[0].yes_price, 0.32)

    def test_generates_polymarket_watchlist_stub(self) -> None:
        candidate = candidate_from_event(
            "Tesla",
            {
                "slug": "tesla-deliveries",
                "title": "Tesla deliveries?",
                "active": True,
                "closed": False,
                "markets": [
                    {
                        "slug": "tesla-deliveries-over-2m",
                        "question": "Tesla deliveries over 2M?",
                        "active": True,
                        "closed": False,
                        "outcomes": '["Yes", "No"]',
                        "outcomePrices": '["0.41", "0.59"]',
                    }
                ],
            },
        )

        assert candidate is not None
        stub = yaml_stub(candidate, as_of=date(2026, 5, 20))

        self.assertEqual(stub["provider"], "polymarket")
        self.assertEqual(stub["source_kind"], "event_slug")
        self.assertEqual(stub["source_ticker"], "tesla-deliveries")
        self.assertEqual(stub["tracked_markets"][0]["last_price"], 0.41)


if __name__ == "__main__":
    unittest.main()
