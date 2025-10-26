import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

st.title("Stock Market App")
st.write("Type a stock symbol below to see its current details.")
st.write("Example: AAPL (Apple), TSLA (Tesla), INFY.NS (Infosys NSE)")

ticker = st.text_input("Enter stock symbol:", "AAPL")
st.success("App loaded successfully!")

if ticker:
    try:
        data = yf.download(ticker, period="6mo")
        if not data.empty:
            st.subheader(f"Showing data for {ticker.upper()}")
            st.dataframe(data.tail())
            st.line_chart(data["Close"])
            last_price = data["Close"][-1]
            st.metric("Latest Closing Price", f"${last_price:,.2f}")
        else:
            st.warning("No data found for that symbol.")
    except Exception as e:
        st.error(f"Error fetching data: {e}")
else:
    st.info("Please enter a stock symbol above to begin.")


