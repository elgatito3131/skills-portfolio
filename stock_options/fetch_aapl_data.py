import pandas as pd
import yfinance as yf

ticker = 'AAPL'
csv_filename = f"{ticker}_data.csv"

print(f"📈 Downloading data for {ticker}...")
data = yf.download(ticker, start='2018-01-01', end='2024-12-31')

print("\n✅ Preview of downloaded data:")
print(data.head())

data.to_csv(csv_filename, index_label='Date')
print(f"\n✅ Data saved to {csv_filename}")
