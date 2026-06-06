import unittest
from datetime import datetime
from unittest.mock import patch

import pandas as pd

from fred_utils import download_from_fred, merge_fred_series_column


class FredUtilsTests(unittest.TestCase):
    def test_download_from_fred_passes_incremental_dates(self):
        csv = "observation_date,DGS10\n2026-06-04,4.40\n"

        with patch("fred_utils.fetch_with_retry", return_value=csv) as fetch:
            df = download_from_fred(
                "DGS10",
                retries=2,
                timeout=30,
                start_date=datetime(2026, 6, 1),
                end_date="2026-06-05",
            )

        self.assertEqual(fetch.call_args.kwargs["params"]["id"], "DGS10")
        self.assertEqual(fetch.call_args.kwargs["params"]["cosd"], "2026-06-01")
        self.assertEqual(fetch.call_args.kwargs["params"]["coed"], "2026-06-05")
        self.assertEqual(df.index[-1].strftime("%Y-%m-%d"), "2026-06-04")
        self.assertEqual(float(df.iloc[-1]["Close"]), 4.4)

    def test_merge_fred_series_column_expands_index_for_new_dates(self):
        existing = pd.DataFrame(
            {"AAA10Y": [1.17]},
            index=pd.to_datetime(["2025-12-11"]),
        )
        update = pd.DataFrame(
            {"AAA10Y": [1.18, 1.02]},
            index=pd.to_datetime(["2025-12-12", "2026-06-04"]),
        )

        merged = merge_fred_series_column(existing, "AAA10Y", update)

        self.assertEqual(merged.index[-1].strftime("%Y-%m-%d"), "2026-06-04")
        self.assertEqual(float(merged.loc[pd.Timestamp("2026-06-04"), "AAA10Y"]), 1.02)
        self.assertEqual(float(merged.loc[pd.Timestamp("2025-12-11"), "AAA10Y"]), 1.17)


if __name__ == "__main__":
    unittest.main()
