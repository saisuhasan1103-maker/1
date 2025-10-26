import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

st.title("Python Stock Market App Using Python")
st.write("Type a stock symbol below to see its current details.")
st.write("Examples: AAPL, TSLA, INFY.NS, CMR, SUHASAN, MSFT, PYPL, IBM")

companies = ["AAPL", "TSLA", "INFY.NS", "MSFT", "PYPL", "IBM"]

symbol = st.text_input("Enter stock symbol:", "")

if symbol:
    try:
        stock = yf.Ticker(symbol)
        data = stock.history(period="1mo")
        info = stock.info

        st.subheader(f"{symbol} details")
        st.write("Company Name:", info.get("longName", "N/A"))
        st.write("Market Price:", info.get("currentPrice", "N/A"))
        st.write("Market Cap:", info.get("marketCap", "N/A"))
        st.write("Previous Close:", info.get("previousClose", "N/A"))

        st.subheader("Price chart (last month)")
        if not data.empty:
            st.line_chart(data['Close'])
        else:
            st.write("No historical data available for this stock.")
    except Exception as e:
        st.write("Error fetching data. Make sure the symbol is correct.")
        st.write(e)
else:
    st.write("Please enter a stock symbol from the list above or any valid stock symbol.")
