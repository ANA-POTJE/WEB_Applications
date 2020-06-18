import yfinance as yf
import streamlit as st

st.write("""
# Simple Stock Price App
Shown are the stock closing price and volume of Google!
""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
tickerSymbol = 'GOOGL'

#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')

# Open High Low Close Volume Dividends Stock Splits
st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
#Running the web app
#After saving the code into a file called myapp.py, fire up the command prompt 
#(or Power Shell in Microsoft Windows) and run the following command:
#####
##### WORKED IN ANACONDA PROMPT!!! (conda activate env first!)
#####

#     streamlit run myapp.py

#Next, we should see the following message:
#> streamlit run myapp.py

#You can now view your Streamlit app in your browser.
#Local URL: http://localhost:8501
#Network URL: http://10.0.0.11:8501

#In a short moment, an internet browser window should pop-up and directs you to the 
#created web app by taking you to [http://localhost:8501.]http://localhost:8501 as shown below.
