import pandas as pd
import matplotlib.pyplot as plt

# 1️⃣ Load the CSV
csv_filename = 'AAPL_data.csv'
print(f"📂 Loading data from {csv_filename}...")
print("\n🟢 CSV Raw Preview:")
with open(csv_filename, 'r') as f:
    for _ in range(5):
        print(f.readline().strip())


data = pd.read_csv(csv_filename, index_col='Date', parse_dates=True)
# Calculate Moving Averages
data['MA20'] = data['Close_AAPL'].rolling(window=20).mean()
data['MA50'] = data['Close_AAPL'].rolling(window=50).mean()

# 2️⃣ Preview the data
print("\n✅ First 5 rows:")
print(data.head())

plt.figure(figsize=(12, 6))
plt.plot(data['Close_AAPL'])
plt.title('AAPL Closing Price (2018-2024)')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.grid()
plt.show()

plt.figure(figsize=(12, 6))
plt.plot(data['Volume_AAPL'], color='orange')
plt.title('AAPL Trading Volume (2018-2024)')
plt.xlabel('Date')
plt.ylabel('Volume')
plt.grid()
plt.show()

data['Returns'] = data['Close_AAPL'].pct_change()

plt.figure(figsize=(12, 6))
plt.plot(data['Returns'], color='green')
plt.title('AAPL Daily Returns (2018-2024)')
plt.xlabel('Date')
plt.ylabel('Returns')
plt.grid()
plt.show()

# Plot Closing Price with Moving Averages
plt.figure(figsize=(12, 6))
plt.plot(data['Close_AAPL'], label='Close Price', color='blue')
plt.plot(data['MA20'], label='20-Day MA', color='orange')
plt.plot(data['MA50'], label='50-Day MA', color='green')
plt.title('AAPL Closing Price with Moving Averages (2018-2024)')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid()
plt.show()
