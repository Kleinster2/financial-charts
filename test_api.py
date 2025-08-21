import requests
import json

# Test /api/tickers
print("Testing /api/tickers...")
r = requests.get('http://localhost:5000/api/tickers')
print(f"Status: {r.status_code}")
tickers = r.json()
print(f"Tickers count: {len(tickers)}")
if tickers:
    print(f"First 5 tickers: {tickers[:5]}")
    print(f"RSP in tickers: {'RSP' in tickers}")
else:
    print("ERROR: No tickers returned!")

# Test /api/data with RSP
if 'RSP' in tickers:
    print("\nTesting /api/data?tickers=RSP...")
    r = requests.get('http://localhost:5000/api/data?tickers=RSP')
    print(f"Status: {r.status_code}")
    data = r.json()
    if 'RSP' in data and len(data['RSP']) > 0:
        print(f"RSP data points: {len(data['RSP'])}")
        print(f"First data point: {data['RSP'][0]}")
    else:
        print("ERROR: No RSP data returned!")

# Test /api/health
print("\nTesting /api/health...")
r = requests.get('http://localhost:5000/api/health')
print(f"Status: {r.status_code}")
print(f"Response: {r.json()}")
