import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
from pathlib import Path

# Set the title and favicon that appear in the Browser's tab bar.
st.set_page_config(
    page_title='🍿Blockbuster Bytes',
    page_icon=':movie_camera:', # Movie camera emoji
)


st.title("🌍 Blockbuster Bytes: What the World Watches & Pays For 🎥")
st.markdown("### Trends in International TV shows and movies with interactive visuals! 📊") 
st.markdown("")
st.markdown("Our platform allows users to clearly visualize data on the popularity of international TV shows and movies and the revenue they brought in.")
st.markdown("This allows streaming platforms to decide what media to bring onto their platforms that will generate the most profit from its users.")
#what people like to watch what people pay to watch

#tabs for categories
tab1, tab2, = st.tabs(["🎞️ Movies", "📺 TV Shows"])

# Movies tab
with tab1:
    st.header("Movie Data") 
    genre = st.selectbox("Choose a Category:", ["Comedy", "Rom-Com", "Horror", "Action"])
    
    if genre == "Comedy":
        st.subheader("Comedy Movies")
        st.write("description of section")
        
    if genre == "Rom-Com":
        st.subheader("Rom-Com Movies")        



# TV shows
with tab2:
    st.header("TV Shows")
    maps = st.selectbox("What information are you interested in?", ["World Map"])

