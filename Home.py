import streamlit as st
from matplotlib import image
import os


st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.title(":green[Welcome to Homepage! 👋]")
st.snow()


st.image("img.png")

st.title(":red[Innomatics Research Labs]")

st.title(":violet[ Data science Internship]")

#original_title = '<h1 style="font-family:Courier; color:Blue; font-size: 40px;">I am a Data Science Enthusiast</h1>'
#st.markdown(original_title, unsafe_allow_html=True)


btn_click = st.button("Click me to Know Who I am")

if btn_click == True:
    st.subheader("You clicked me :cry:")
    st.balloons()
    st.title("I am :red[Bharathkumar M S]")
    st.title("I am a  :violet[ Data Science Enthusiast]")
    st.write("## Connect me on Linkedin [link](https://www.linkedin.com/in/bharathkumar-m-s-1736221b0/)")


