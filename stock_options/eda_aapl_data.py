# ---------------------------
# IMPORTS
# ---------------------------
import pandas as pd
import matplotlib.pyplot as plt


# ---------------------------
# LOAD DATA
# ---------------------------
csv_filename = 'AAPL_data.csv'
print(f"📂 Loading data from {csv_filename}...")

# Read CSV with Date as index
data = pd.read_csv(csv_filename, index_col='Date', parse_dates=True)

# Quick preview
print("\n✅ First 5 rows:")
print(data.head())


# ---------------------------
# FEATURE ENGINEERING
# ---------------------------

# Moving Averages
data['MA20'] = data['Close_AAPL'].rolling(window=20).mean()
data['MA50'] = data['Close_AAPL'].rolling(window=50).mean()

# Daily Returns
data['Returns'] = data['Close_AAPL'].pct_change()

# RSI Calculation (14-day)
delta = data['Close_AAPL'].diff()
gain = delta.where(delta > 0, 0)
loss = -delta.where(delta < 0, 0)
avg_gain = gain.rolling(window=14).mean()
avg_loss = loss.rolling(window=14).mean()
rs = avg_gain / avg_loss
data['RSI'] = 100 - (100 / (1 + rs))

# Bollinger Bands (20-day)
data['BB_MA20'] = data['Close_AAPL'].rolling(window=20).mean()
data['BB_STD20'] = data['Close_AAPL'].rolling(window=20).std()
data['BB_Upper'] = data['BB_MA20'] + 2 * data['BB_STD20']
data['BB_Lower'] = data['BB_MA20'] - 2 * data['BB_STD20']


# ---------------------------
# CHECK DATAFRAME STRUCTURE
# ---------------------------
print("\n✅ Columns in DataFrame:")
print(data.columns)
print("\n✅ Updated first 5 rows:")
print(data.head())


# ---------------------------
# PLOTS
# ---------------------------

# Plot Closing Price
plt.figure(figsize=(12, 6))
plt.plot(data['Close_AAPL'])
plt.title('AAPL Closing Price (2018-2024)')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.grid()
plt.show()

# Plot Volume
plt.figure(figsize=(12, 6))
plt.plot(data['Volume_AAPL'], color='orange')
plt.title('AAPL Trading Volume (2018-2024)')
plt.xlabel('Date')
plt.ylabel('Volume')
plt.grid()
plt.show()

# Plot Daily Returns
plt.figure(figsize=(12, 6))
plt.plot(data['Returns'], color='green')
plt.title('AAPL Daily Returns (2018-2024)')
plt.xlabel('Date')
plt.ylabel('Returns')
plt.grid()
plt.show()

# Plot RSI
plt.figure(figsize=(12, 6))
plt.plot(data['RSI'], label='14-Day RSI', color='purple')
plt.axhline(70, color='red', linestyle='--', label='Overbought (70)')
plt.axhline(30, color='green', linestyle='--', label='Oversold (30)')
plt.title('AAPL 14-Day Relative Strength Index (RSI)')
plt.xlabel('Date')
plt.ylabel('RSI')
plt.legend()
plt.grid()
plt.show()

# Plot Bollinger Bands
plt.figure(figsize=(12, 6))
plt.plot(data['Close_AAPL'], label='Close Price', color='blue')
plt.plot(data['BB_MA20'], label='20-Day MA', color='orange')
plt.plot(data['BB_Upper'], label='Upper Band', color='green')
plt.plot(data['BB_Lower'], label='Lower Band', color='red')
plt.fill_between(data.index, data['BB_Lower'], data['BB_Upper'], color='grey', alpha=0.1)
plt.title('AAPL Closing Price with Bollinger Bands (2018-2024)')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid()
plt.show()
