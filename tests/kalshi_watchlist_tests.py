import unittest
from datetime import date
from pathlib import Path
import sys

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.refresh_kalshi_watchlist import build_report, evaluate_entry


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


if __name__ == "__main__":
    unittest.main()
