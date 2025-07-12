import streamlit as st

st.set_page_config(page_title="Options Trading Simulator", layout="wide")

st.title("📈 Options Trading Simulator")
st.subheader("Choose a Stock Ticker")

ticker = st.selectbox(
    "Select stock symbol",
    options=["AAPL", "TSLA", "MSFT", "GOOG", "AMZN"]
)

st.success(f"Selected Ticker: {ticker}")


st.write("""
Welcome to the Options Trading Simulator App!  
This is the MVP skeleton. More features coming soon.
""")
