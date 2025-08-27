import streamlit as st 
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import numpy as np
import seaborn as sns

st.title("Stock Price Analysis")
# st.header("Analyze historical stock prices and visualize trends.")
# st.subheader("Enter a stock ticker symbol to get started.")

start_date = st.date_input("Start Date", pd.to_datetime("2020-01-01"))

end_date = st.date_input("End Date", pd.to_datetime("today"))

# symbol = 'AAPL'  # Default symbol
#ticker_symbol = st.text_input("Stock Ticker Symbol", value=symbol)


ticker_symbol = st.selectbox("Select Stock Ticker Symbol", 
                             options=['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA', 'META', 'NVDA', 'NFLX', 'INTC', 'AMD'])


ticker_data = yf.Ticker(ticker_symbol)
ticker_df = ticker_data.history(start=start_date, end=end_date)

st.dataframe(ticker_df)

#Lets create sum graphs

st.write(f"### Closing Price of {ticker_symbol}")
st.line_chart(ticker_df['Close'])

st.write(f"### Volume of {ticker_symbol}")
st.bar_chart(ticker_df['Volume'])

col1, col2 = st.columns(2)
with col1:
    st.write(f"### Moving Average (20 days) of {ticker_symbol}")
    ticker_df['MA20'] = ticker_df['Close'].rolling(window=20).mean()
    st.line_chart(ticker_df[['Close', 'MA20']])

with col2:
    st.write(f"### Moving Average (50 days) of {ticker_symbol}")
    ticker_df['MA50'] = ticker_df['Close'].rolling(window=50).mean()
    st.line_chart(ticker_df[['Close', 'MA50']])
    