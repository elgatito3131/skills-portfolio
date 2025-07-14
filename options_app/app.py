import streamlit as st
import yfinance as yf
import pandas as pd

def calculate_rsi(series, period=14):
    delta = series.diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avg_gain = gain.rolling(window=period).mean()
    avg_loss = loss.rolling(window=period).mean()
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

st.set_page_config(page_title="Options Trading Simulator", layout="wide")

st.write("""
Welcome to the Options Trading Simulator App!  
This is the MVP skeleton. More features coming soon.
""")

st.title("📈 Options Trading Simulator")
st.subheader("Choose a Stock Ticker")

ticker = st.selectbox(
    "Select stock symbol",
    options=["AAPL", "TSLA", "MSFT", "GOOG", "AMZN"]
)

st.success(f"Selected Ticker: {ticker}")

# ---------------------------
# Fetch Historical Price Data
# ---------------------------
st.subheader(f"📈 Historical Data for {ticker}")

try:
    data = yf.download(ticker, start='2018-01-01')
    if not data.empty:
        data['Returns'] = data['Close'].pct_change()
        data['Returns'] = data['Returns'] * 100
        data['Returns'] = data['Returns'].round(2)
        data['RSI'] = calculate_rsi(data['Close'])

        # Show more useful columns
        columns_to_show = ['Open', 'High', 'Low', 'Close', 'Volume', 'Returns', 'RSI']
        available_columns = [col for col in columns_to_show if col in data.columns]

        st.dataframe(data[available_columns].tail(10))


        # ---------------------------
        # Price Chart
        # ---------------------------
        st.subheader(f"{ticker} Closing Price Chart")

        if 'Close' in data.columns:
            st.line_chart(data['Close'])
            # ---------------------------
            # RSI Chart
            # ---------------------------
            st.subheader(f"{ticker} 14-Day RSI")

            if 'RSI' in data.columns:
                st.line_chart(data['RSI'])
                st.caption('Horizontal levels at 30 (oversold) and 70 (overbought) are common RSI thresholds.')
            else:
                st.warning("RSI data not available for this ticker.")


    else:
        st.warning("No data found for this ticker. Please try a valid symbol.")
except Exception as e:
    st.error(f"Error fetching data: {e}")


