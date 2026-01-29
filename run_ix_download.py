"""Directly download ORIX data"""
import sys
sys.path.insert(0, r'C:\Users\klein\financial-charts')

from download_single_ticker import download_and_save_ticker

# Download IX data
print("Downloading ORIX (IX) data...")
download_and_save_ticker("IX", "2019-12-31")
print("Done!")
