# resources: https://docs.streamlit.io/en/latest/tutorial/create_a_data_explorer_app.html

import streamlit as st
import pandas as pd
import numpy as np

st.title('Vancouver housing')

#getting data:
df = pd.read_csv (r'/Users/ahmed.khan/Documents/personal/vancouver_datajam/property-tax-report.csv',sep=';')
# print (df)


st.text('sample data')
st.write(df.head())


import io
buffer = io.StringIO()
df.info(buf=buffer)
s = buffer.getvalue()
st.write(s)
# with open("df_info.txt", "w",
#      encoding="utf-8") as f:
#      f.write(s)