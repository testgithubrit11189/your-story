# app.py

import streamlit as st

# Set up page configuration
st.set_page_config(
    page_title="GI Tags Explorer",
    page_icon="🗺️",
    layout="wide",
)

# App title and intro
st.title("GI Tags Explorer Portal")
st.markdown("### Welcome to the GI Tag Visual Explorer")

st.write("""
Use the sidebar to navigate through different pages:
- 🏨 Accommodation Finder  
- 🛕 GI Tags  founder
- 🏰 Adventure
""")

st.info("Select a page from the sidebar to begin exploring.")
