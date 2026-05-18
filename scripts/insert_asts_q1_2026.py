"""Insert ASTS Q1 2026 row into income_statement_quarterly.

Source: 10-Q filed May 2026, three months ended March 31, 2026.
All figures in USD.

Field map (10-Q -> DB):
  Total revenues           14,735K -> total_revenue            = 14_735_000
  Cost of revenues (P+S)   11,649K -> cost_of_revenue          = 11_649_000  (products 11,063 + services 586)
  Derived gross profit      3,086K -> gross_profit             =  3_086_000
  Below-GP OpEx           152,498K -> operating_expenses       = 152_498_000  (total OpEx 164,147 - COGS 11,649; this is ASTS engineering services 84,097 + G&A 43,657 + R&D 7,129 + D&A 17,615)
  Operating loss         -149,412K -> operating_income         = -149_412_000  (revenue - total OpEx)
  EBITDA (OI + D&A)      -131,797K -> ebitda                   = -131_797_000
  Net loss to common     -191,012K -> net_income               = -191_012_000  (after NCI allocation)
  GAAP diluted EPS         -$0.66  -> eps                      = -0.66
  R&D costs                 7,129K -> research_and_development =   7_129_000
  G&A costs                43,657K -> selling_general_administrative = 43_657_000  (G&A only; ASTS engineering services 84,097K is separate, captured in operating_expenses)
  Interest expense         24,278K -> interest_expense         =  24_278_000
  Income tax expense        1,169K -> income_tax_expense       =   1_169_000
  D&A                      17,615K -> depreciation_amortization=  17_615_000

Math checks:
  COGS components: 11,063 (products) + 586 (services) = 11,649 OK
  Total OpEx: 11,063 + 586 + 84,097 + 43,657 + 7,129 + 17,615 = 164,147 OK
  Operating income: 14,735 - 164,147 = -149,412 OK
  EBITDA: -149,412 + 17,615 = -131,797 OK
"""
import sqlite3

conn = sqlite3.connect('market_data.db')
cur = conn.cursor()

cur.execute('SELECT COUNT(*) FROM income_statement_quarterly WHERE ticker=? AND fiscal_date_ending=?',
            ('ASTS', '2026-03-31'))
existing = cur.fetchone()[0]
if existing:
    print(f'ABORT: ASTS Q1 2026 row already exists ({existing} row(s))')
    raise SystemExit(1)

cur.execute('''
    INSERT INTO income_statement_quarterly (
        ticker, fiscal_date_ending, total_revenue, cost_of_revenue, gross_profit,
        operating_expenses, operating_income, ebitda, net_income, eps,
        research_and_development, selling_general_administrative,
        interest_expense, income_tax_expense, depreciation_amortization
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
''', (
    'ASTS', '2026-03-31',
    14_735_000,        # total_revenue
    11_649_000,        # cost_of_revenue
    3_086_000,         # gross_profit
    152_498_000,       # operating_expenses (below-GP)
    -149_412_000,      # operating_income
    -131_797_000,      # ebitda (OI + D&A)
    -191_012_000,      # net_income (net loss to common stockholders, after NCI)
    -0.66,             # eps (GAAP basic = diluted)
    7_129_000,         # research_and_development
    43_657_000,        # selling_general_administrative (G&A only)
    24_278_000,        # interest_expense (gross; interest income 26,998K sits in 'other income')
    1_169_000,         # income_tax_expense
    17_615_000,        # depreciation_amortization
))
conn.commit()

cur.execute('SELECT * FROM income_statement_quarterly WHERE ticker=? AND fiscal_date_ending=?',
            ('ASTS', '2026-03-31'))
r = cur.fetchone()
cur.execute('PRAGMA table_info(income_statement_quarterly)')
cols = [c[1] for c in cur.fetchall()]
print('Inserted row:')
for c, v in zip(cols, r):
    print(f'  {c}: {v}')
