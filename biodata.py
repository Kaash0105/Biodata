import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="My Biodata",
    layout="wide"
)

st.title("Ahgaash A/L Sigamani 😎")
image = Image.open("me.jpeg")
st.image(image, caption="This is Me!!", width=500)
st.header("About Me")

# 3 facts about me
st.text("1. I am a student in Taylor's University")
st.text("2. I love travelling, gaming and coding 👾")
st.text("3. I am so drawn into new growing technologies")

st.success("Welcome to my Biodata!!")
st.balloons()