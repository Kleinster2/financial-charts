# S&P 500 Data Downloader

This script downloads historical stock price data for all S&P 500 companies and stores it in a SQLite database.

## Steps

1.  **Fetches S&P 500 Companies**: Retrieves the list of S&P 500 companies from Wikipedia.
2.  **Downloads Price Data**: Downloads daily historical stock prices for each company from Yahoo Finance.
3.  **Data Cleaning**: Processes the data, handles missing values, and filters out tickers with insufficient data.
4.  **Stores Data**: Saves the cleaned price data and company metadata into an SQLite database file (`sp500_data.db`).

## Usage

1.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Run the script:**
    ```bash
    python download_sp500.py
    ```

This will create the `sp500_data.db` file in the same directory.
