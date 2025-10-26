import yfinance as yf

print("Stock Market App")
print("Type a stock symbol below to see its current details.")
print("Example: AAPL (Apple), TSLA (Tesla), INFY.NS (Infosys NSE)\n")

symbol = input("Enter stock symbol: ")

if symbol:
    try:
        stock = yf.Ticker(symbol)
        data = stock.history(period="1d")

        if data.empty:
            print(" Oops! Invalid symbol or no data found.")
        else:
            info = stock.info
            price = data["Close"].iloc[-1]

            print(f"\n{info.get('shortName', symbol)} ({symbol.upper()})")
            print(f"Current Price: {round(price, 2)} {info.get('currency', '')}")
            print(f"Previous Close: {info.get('previousClose', 'N/A')}")
            print(f"Open Price: {info.get('open', 'N/A')}")
            print(f"Day High: {info.get('dayHigh', 'N/A')}")
            print(f"Day Low: {info.get('dayLow', 'N/A')}")
            print(f"Volume: {info.get('volume', 'N/A')}")

    except Exception as e:
        print(f"⚠️ Something went wrong: {e}")

print("\n---\n👋 Made by Your Name")
# stock_app.py
import yfinance as yf
import streamlit as st

# App header
st.title(" Stock Market App")
st.write("Type a stock symbol below to see its current details.")
st.write("Example: AAPL (Apple), TSLA (Tesla), INFY.NS (Infosys NSE)")

# Get stock symbol from user
symbol = st.text_input("Enter stock symbol:")

if symbol:  # if user entered something
    try:
        stock = yf.Ticker(symbol)  # get stock info
        data = stock.history(period="1d")  # get latest day data

        if data.empty:
            st.error("Oops! Invalid symbol or no data found.")
        else:
            info = stock.info
            price = data["Close"].iloc[-1]

            # Show stock info
            st.subheader(f"{info.get('shortName', symbol)} ({symbol.upper()})")
            st.write(f"**Current Price:** {round(price, 2)} {info.get('currency', '')}")
            st.write(f"**Previous Close:** {info.get('previousClose', 'N/A')}")
            st.write(f"**Open Price:** {info.get('open', 'N/A')}")
            st.write(f"**Day High:** {info.get('dayHigh', 'N/A')}")
            st.write(f"**Day Low:** {info.get('dayLow', 'N/A')}")
            st.write(f"**Volume:** {info.get('volume', 'N/A')}")

    except Exception as e:
        st.error(f" Something went wrong: {e}")

st.write("---")
st.write(" Made by Your Name")
