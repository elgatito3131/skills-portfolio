import streamlit as st
import yfinance as yf
import pandas as pd


st.set_page_config(page_title="Options Trading Simulator", layout="wide")

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
        # Show more useful columns
        columns_to_show = ['Open', 'High', 'Low', 'Close', 'Volume', 'Returns']
        available_columns = [col for col in columns_to_show if col in data.columns]

        st.dataframe(data[available_columns].tail(10))

        # ---------------------------
        # Price Chart
        # ---------------------------
        st.subheader(f"{ticker} Closing Price Chart")

        if 'Close' in data.columns:
            st.line_chart(data['Close'])
        else:
            st.warning("No 'Close' column found in data to plot.")

    else:
        st.warning("No data found for this ticker. Please try a valid symbol.")
except Exception as e:
    st.error(f"Error fetching data: {e}")



st.write("""
Welcome to the Options Trading Simulator App!  
This is the MVP skeleton. More features coming soon.
""")
