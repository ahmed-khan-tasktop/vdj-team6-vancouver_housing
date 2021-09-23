# resources: https://docs.streamlit.io/en/latest/tutorial/create_a_data_explorer_app.html

import streamlit as st
import pandas as pd
import numpy as np

st.title('Vancouver housing')

#getting data:
df = pd.read_csv (r'/Users/ahmed.khan/Documents/personal/vancouver_datajam/property-tax-report.csv',sep=';')
# print (df)


st.write(df)

