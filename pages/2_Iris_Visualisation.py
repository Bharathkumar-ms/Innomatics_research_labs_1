import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
import os
import numpy as np
import io

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "Iris.png")
DATA_PATH = os.path.join(dir_of_interest, "data", "iris.csv")

st.title(" :blue[Data Visualisation] of :red[ Iris Flower]")

img = image.imread(IMAGE_PATH)
st.image(img)

data = pd.read_csv(DATA_PATH)
#st.dataframe(df)




#Histogram Chart
var=st.selectbox(":red[Histogram Chart]",("Species",))
fig = px.histogram(data, x=var)
st.plotly_chart(fig)

#Pie Chart
var=st.selectbox(":red[Pie Chart]",("Species",))
df=data[var].value_counts()
fig = px.pie(values=df.values, names=df.index)
st.plotly_chart(fig)

#Scatter
st.write(" :red[Scatter plots]")
fig = px.scatter(data, x="SepalWidthCm", y="SepalLengthCm", color="Species",
                 size='SepalLengthCm', hover_data=['PetalWidthCm'])
st.plotly_chart(fig)

fig = px.scatter(data, x="SepalWidthCm", y="SepalLengthCm", color="Species", symbol="Species")
st.plotly_chart(fig)






st.header(" Histogram and Box plot for :red[ Sepal length]")
species = st.selectbox("Select the Species:", data['Species'].unique(),key=1)

col1, col2 = st.columns(2)

fig_1 = px.histogram(data[data['Species'] == species], x="SepalLengthCm")
col1.plotly_chart(fig_1, use_container_width=True)

fig_2 = px.box(data[data['Species'] == species], y="SepalLengthCm")
col2.plotly_chart(fig_2, use_container_width=True)





st.header(" Histogram and Box plot for :red[ Sepal width]")
species = st.selectbox("Select the Species:", data['Species'].unique(),key=2)

col1, col2 = st.columns(2)

fig_1 = px.histogram(data[data['Species'] == species], x="SepalWidthCm")
col1.plotly_chart(fig_1, use_container_width=True)

fig_2 = px.box(data[data['Species'] == species], y="SepalWidthCm")
col2.plotly_chart(fig_2, use_container_width=True)





st.header(" Histogram and Box plot for :red[ Petal length]")
species = st.selectbox("Select the Species:", data['Species'].unique(),key=3)

col1, col2 = st.columns(2)

fig_1 = px.histogram(data[data['Species'] == species], x="PetalLengthCm")
col1.plotly_chart(fig_1, use_container_width=True)

fig_2 = px.box(data[data['Species'] == species], y="PetalLengthCm")
col2.plotly_chart(fig_2, use_container_width=True)






st.header(" Histogram and Box plot for :red[ Petal width]")
species = st.selectbox("Select the Species:", data['Species'].unique(),key=4)

col1, col2 = st.columns(2)

fig_1 = px.histogram(data[data['Species'] == species], x="PetalWidthCm")
col1.plotly_chart(fig_1, use_container_width=True)

fig_2 = px.box(data[data['Species'] == species], y="PetalWidthCm")
col2.plotly_chart(fig_2, use_container_width=True)









    


























