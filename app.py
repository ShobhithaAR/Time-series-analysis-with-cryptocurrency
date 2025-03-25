import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load Bitcoin Price Data
df_prices = pd.read_csv("bitcoin_prices.csv", parse_dates=["Date"], index_col="Date")

st.title("Cryptocurrency Price Forecasting & Sentiment Analysis")
st.subheader("Bitcoin Price Trend")
st.line_chart(df_prices["Price"])

st.write("This dashboard shows Bitcoin price trends, forecasts, and sentiment analysis.")
