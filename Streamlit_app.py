# importing the libraries
import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import datetime

df = pd.read_csv('D:\\Extra_projects\\Streamlit Project\\NVidia_stock_history.csv')
df.head(5)

# Delete rows where date is before 1/1/2019.
df['Date'] = pd.to_datetime(df['Date'])
df = df[~(df['Date'] < '2019-01-01')]
print(df.head())
print(df.info())


# Reset the index to the Date Column.
df['Date'] = pd.to_datetime(df['Date'], format='%Y/%m/%d')
df.reset_index(drop=True, inplace=True)
df.set_index('Date', inplace=True)

print(df.head())

# Design and configure the web page
# Specify the title and logo for the web page
st.set_page_config(page_title='Nvidia Stock Prices', page_icon = 'D:\\Extra_projects\\Streamlit Project\\Nvidia-logo.png',
                   layout="wide")

# Display the Data in the App
st.subheader('Looking at the Data')
st.dataframe(df.head())


# Display statistical information on the dataset
st.subheader('Statistical Info about the Data')
st.write(df.describe())

# Selection for a specific time frame
st.subheader('Select a Date Range')
df_select = df

col1, col2 = st.columns(2)

with col1:
    st.write('Select a Start Date')
    Start_date = st.date_input('Start Date', min_value=datetime.date(2019,1,2), max_value=datetime.date(2021,11,12), value=datetime.date(2019,1,2))

with col2:
    st.write('Select a End Date')
    End_date = st.date_input('End Date', min_value=datetime.date(1999,1,22), max_value=datetime.date(2021,11,12), value=datetime.date(2021,11,12))


if(Start_date != None or End_date !=None):
    if(Start_date < End_date):
        df_select = df[Start_date:End_date]
    else:
        st.warning("Invalid Date Range - Re-enter Dates")


# Visualizing the Stock Data
# Open and close Prices

st.subheader("Open & Close Prices for Nvidia Stock")
st.markdown("\n\n")
st.line_chart(df_select[['Open','Close']])


# High and Low Prices
st.subheader("High and Low Prices for Nvidia Stock")
st.markdown("\n\n")
st.line_chart(df_select[['High', "Low"]])


# Volume of Stock Traded

st.subheader("Volume Traded for Nvidia Stock")
st.markdown("\n\n")
st.bar_chart(df_select['Volume'])

# Moving Average from 50 days to 250 days
st.subheader('Moving Averages of Open and Closing Stock Prices')
movevage_len = st.slider('Select the number of Days for moving Averages', min_value=0, max_value=250, value = 50)
moveavg_oc = df_select[['Open', 'Close']].rolling(50).mean()
st.line_chart(moveavg_oc)





