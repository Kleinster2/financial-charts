#!/usr/bin/env python3
import sys
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

import json

with open('charting_app/workspace.json', 'r') as f:
    data = json.load(f)

# Add the Delisted EV chart back to Page 36
new_card = {
    'page': '36',
    'title': 'Delisted EV Companies (Historical)',
    'tickers': ['ARVL', 'FFIE', 'FSR', 'MULN', 'NKLA']
}

data['cards'].append(new_card)

with open('charting_app/workspace.json', 'w') as f:
    json.dump(data, f, indent=2)

print('Added "Delisted EV Companies (Historical)" chart to Page 36')
print(f'  Tickers: {new_card["tickers"]}')
print(f'  Total cards: {len(data["cards"])}')
