import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
import os
import numpy as np
import seaborn as seaborn
import io


# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "Iris.png")
DATA_PATH = os.path.join(dir_of_interest, "data", "iris.csv")

st.title(":red[ Iris Data Analysis]")

img = image.imread(IMAGE_PATH)
st.image(img)
st.subheader(":blue[ Iris Dataset]")
df = pd.read_csv(DATA_PATH)
st.dataframe(df)








df = pd.read_csv("resources\data\iris.csv")

st.header(":blue[Details of the Dataset]")

data_info = st.radio('Click to view the Details of the Dataset:',
                      ('Head', 'Tail','Sample', 'Columns', 'Shape', 'Info', 'Describe'),
                      horizontal=True)

if data_info == 'Shape':
    st.write(f"Number of Rows:  {df.shape[0]}")
    st.write(f"Number of Columns:  {df.shape[1]}")
elif data_info == 'Head':
    st.write(df.head())
elif data_info == 'Tail':
    st.write(df.tail())
elif data_info == 'Sample':
    st.write(df.sample(10))  
elif data_info == 'Columns':
    for column in list(df.columns):
        st.write(column)
elif data_info == 'Info':
    buffer = io.StringIO()
    df.info(buf=buffer)
    s = buffer.getvalue()
    st.text(s)
else:
    st.write(df.describe())


@st.cache_data
def convert_df(df):
    return df.to_csv().encode('utf-8')

csv = convert_df(df)



st.markdown("<br>",unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center';><b>Click to Downlaod the Dataset</b></h5>",unsafe_allow_html=True)
col1, col2, col3 , col4, col5 = st.columns(5)

with col1:
    pass
with col2:
    pass
with col4:
    pass
with col5:
    pass
with col3 :
    center_button = st.download_button(
     label="Download",
     data=csv,
     file_name='iris.csv',
     mime='text/csv',
 )




