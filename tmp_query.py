import sqlite3
conn = sqlite3.connect('market_data.db')
cur = conn.cursor()
cur.execute("SELECT fiscal_date_ending, total_revenue, gross_profit, operating_income, net_income, eps FROM income_statement_annual WHERE ticker='PLTR' ORDER BY fiscal_date_ending")
for row in cur.fetchall():
    rev_b = row[1]/1e9 if row[1] else 0
    gp_b = row[2]/1e9 if row[2] else 0
    oi_b = row[3]/1e9 if row[3] else 0
    ni_b = row[4]/1e9 if row[4] else 0
    eps = row[5] if row[5] else 0
    gm = (row[2]/row[1]*100) if row[1] and row[2] else 0
    om = (row[3]/row[1]*100) if row[1] and row[3] else 0
    print(f"{row[0][:4]}  Rev: ${rev_b:.2f}B  GP: ${gp_b:.2f}B  OI: ${oi_b:.2f}B  NI: ${ni_b:.2f}B  EPS: ${eps:.2f}  GM: {gm:.1f}%  OM: {om:.1f}%")
