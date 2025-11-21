"""
Update IV charts in workspace to use dataType: "iv"
"""

import json

WORKSPACE_PATH = 'charting_app/workspace.json'

# Load workspace
with open(WORKSPACE_PATH, 'r') as f:
    workspace = json.load(f)

# Find all IV charts on page 42 and update them
updated_count = 0

for card in workspace['cards']:
    # Check if this is an IV chart (on page 42 and has "Implied Volatility" or "IV" in title)
    if card.get('page') == '42':
        title = card.get('title', '')

        # Don't update the VIX chart - it's a CBOE index, not stock IV
        if '^VIX' in card.get('tickers', []) and len(card.get('tickers', [])) == 1:
            print(f"Skipping VIX chart (uses regular price data)")
            continue

        # Add dataType for stock IV charts
        if 'Implied Volatility' in title or 'IV' in title:
            card['dataType'] = 'iv'
            card['ivMetric'] = 'average_iv'  # Can be: average_iv, call_iv, or put_iv
            updated_count += 1
            print(f"Updated: {title}")

# Save updated workspace
with open(WORKSPACE_PATH, 'w') as f:
    json.dump(workspace, f, indent=2)

print(f"\n[OK] Updated {updated_count} charts to use IV data type")
print("\nNext steps:")
print("1. Refresh browser (Ctrl+Shift+R)")
print("2. Navigate to page 42 (Implied Volatility)")
print("3. Charts should now display implied volatility percentages")
print("\nExpected values:")
print("- AAPL: ~30%")
print("- NVDA: ~93% (very high!)")
print("- TSLA: ~63%")
print("- SPY: ~19%")
