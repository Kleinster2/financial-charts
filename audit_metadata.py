"""
Audit coverage of ticker names in ticker_metadata vs columns in stock_prices_daily.
Prints a JSON summary with counts and a sample list of missing tickers (if any).
"""
import json
import sqlite3
from constants import DB_PATH


def audit(limit: int = 25):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # Collect price table columns (tickers)
    cur.execute("PRAGMA table_info(stock_prices_daily)")
    cols = [r[1] for r in cur.fetchall() if r[1] != "Date"]
    total_cols = len(cols)

    # Missing names via left join against ticker_metadata
    cur.execute(
        """
        WITH cols AS (
          SELECT name AS ticker FROM pragma_table_info('stock_prices_daily') WHERE name <> 'Date'
        )
        SELECT c.ticker
        FROM cols c
        LEFT JOIN ticker_metadata t
          ON t.ticker = c.ticker
          AND COALESCE(NULLIF(t.name,''), NULL) IS NOT NULL
        WHERE t.ticker IS NULL
        ORDER BY c.ticker
        """
    )
    missing = [row[0] for row in cur.fetchall()]

    named_count = total_cols - len(missing)

    summary = {
        "db_path": DB_PATH,
        "total_price_columns": total_cols,
        "metadata_named_count": named_count,
        "metadata_missing_count": len(missing),
        "sample_missing": missing[:limit],
    }

    conn.close()
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    audit()
