import sqlite3
import os
from constants import DB_PATH, get_db_connection


def table_exists(conn, name: str) -> bool:
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (name,))
    return cur.fetchone() is not None


def get_latest_date(conn, table: str) -> str:
    cur = conn.cursor()
    # Find a date-like column
    cur.execute(f"PRAGMA table_info({table})")
    cols = [r[1] for r in cur.fetchall()]
    if not cols:
        return 'missing table or no columns'
    date_col = None
    for c in ('Date', 'date', 'DATE', 'timestamp', 'Timestamp', 'index'):
        if c in cols:
            date_col = c
            break
    if not date_col:
        return 'no date column'
    try:
        cur.execute(f"SELECT MAX({date_col}) FROM {table}")
        row = cur.fetchone()
        return str(row[0]) if row and row[0] is not None else 'empty'
    except Exception as e:
        return f'error: {e}'


def main():
    print(f"Using database: {DB_PATH}")
    if not os.path.exists(DB_PATH):
        print(f'Database not found: {DB_PATH}')
        return
    conn = get_db_connection()
    try:
        for t in ['stock_prices_daily', 'stock_volumes_daily', 'etf_holdings_daily']:
            status = 'missing'
            if table_exists(conn, t):
                status = get_latest_date(conn, t)
            print(f"{t}: {status}")
    finally:
        conn.close()

if __name__ == '__main__':
    main()
