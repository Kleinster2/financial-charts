import requests
import pandas as pd
import io

# Download the file
url = "https://www.ssga.com/us/en/intermediary/etfs/library-content/products/fund-data/etfs/us/holdings-daily-us-en-allw.xlsx"
headers = {"User-Agent": "Mozilla/5.0"}

print("Downloading ALLW holdings file...")
resp = requests.get(url, headers=headers)
print(f"Downloaded {len(resp.content)} bytes")

# Read Excel file
df = pd.read_excel(io.BytesIO(resp.content), sheet_name=None)
sheets = list(df.keys())
print(f"Sheets found: {sheets}")

# Get first sheet
raw_df = df[sheets[0]]

# Look for date information in first 20 rows
print("\nSearching for date information in file...")
for i in range(min(20, len(raw_df))):
    row_vals = raw_df.iloc[i].values
    row_str = ' '.join(str(v) for v in row_vals if pd.notna(v))
    
    # Check for date patterns
    if any(word in row_str.lower() for word in ['date', '2025', 'aug', 'jul', 'as of']):
        print(f"Row {i}: {row_str[:300]}")

# Also check column headers
print("\nColumn headers:")
print(list(raw_df.columns))

# Check if there's metadata in the first few cells
print("\nFirst cell values:")
for i in range(min(5, len(raw_df))):
    for j in range(min(5, len(raw_df.columns))):
        val = raw_df.iloc[i, j]
        if pd.notna(val) and str(val).strip():
            val_str = str(val)[:100]
            if any(word in val_str.lower() for word in ['date', '2025', 'aug', 'jul']):
                print(f"Cell [{i},{j}]: {val_str}")
