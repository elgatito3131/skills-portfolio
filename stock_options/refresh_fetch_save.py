import pandas as pd
import yfinance as yf

print("✅ Downloading AAPL stock data...")
data = yf.download('AAPL', start='2018-01-01', end='2024-12-31', auto_adjust=False)

print("\n✅ Raw Downloaded Data:")
print(data.head())

# FIX: Flatten multi-level columns if necessary
if isinstance(data.columns, pd.MultiIndex):
    print("\n⚙️ Flattening multi-level columns...")
    data.columns = ['_'.join(col).strip() for col in data.columns.values]

print("\n✅ Final Columns:")
print(data.columns)

# Save to CSV with proper index label
data.to_csv('AAPL_data.csv', index_label='Date')
print("\n✅ Data saved as AAPL_data.csv")
