import streamlit as st
import pandas as pd
import os
from PIL import Image

# Page configuration
st.set_page_config(page_title="Showcase", layout="centered")

# CSS for heading animation and hover
st.markdown("""
<style>
@keyframes fadeInUp {
  0% { opacity: 0; transform: translateY(30px); }
  100% { opacity: 1; transform: translateY(0); }
}

.fade-in {
  animation: fadeInUp 1s ease-out;
  transition: all 0.3s ease-in-out;
}

.fade-in h1:hover {
  color: #2c6e49;
  transform: scale(1.05);
  cursor: pointer;
}
</style>
""", unsafe_allow_html=True)

# Load product data
@st.cache_data
def load_data():
    return pd.read_csv("gi_tags.csv")

data = load_data()
image_folder = "images"
product_list = data['Product'].tolist()

# Track current index in session state
if 'index' not in st.session_state:
    st.session_state.index = 0

# Navigation buttons
col1, col2, col3 = st.columns([1, 2, 1])
with col1:
    if st.button("⬅️ Previous"):
        st.session_state.index = (st.session_state.index - 1) % len(product_list)
with col3:
    if st.button("Next ➡️"):
        st.session_state.index = (st.session_state.index + 1) % len(product_list)

# Heading with hover
st.markdown("<div class='fade-in'><h1 style='text-align: center;'>Authentic Himachal GI Product</h1></div>", unsafe_allow_html=True)

# Get current product and image
current_product = product_list[st.session_state.index]
img_filename = current_product.lower().replace(" ", "_")
img_path = None

# Support multiple formats
for ext in ['.jpg', '.jpeg', '.png', '.webp']:
    path = os.path.join(image_folder, f"{img_filename}{ext}")
    if os.path.exists(path):
        img_path = path
        break

# Show image or warning
if img_path:
    st.image(Image.open(img_path), use_column_width=True)
else:
    st.warning("📷 Image not available")
