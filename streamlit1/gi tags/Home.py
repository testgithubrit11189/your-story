import streamlit as st

# Set page config (must be first Streamlit command)
st.set_page_config(page_title="GI Tags - Home", layout="centered")

# CSS for animation, button styling, and hover effects on headings
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

.fade-in h4:hover {
  color: #2c6e49;
  transform: scale(1.03);
  cursor: pointer;
}

.fade-in-button {
  animation: fadeInUp 1s ease-out;
  display: inline-block;
  width: 100%;
  margin-top: 20px;
}

.stButton > button {
  font-size: 16px;
  border-radius: 8px;
  padding: 0.6em 1.5em;
  transition: 0.2s ease-in-out;
  border: 1px solid #ccc;
}

.stButton > button:hover {
  background-color: #2c6e49;
  color: white;
  border: none;
}
</style>
""", unsafe_allow_html=True)

# Title and Subtitle with fade-in and hover effect
st.markdown("<div class='fade-in'><h1 style='text-align: center;'>GI Tags of Himachal Pradesh</h1></div>", unsafe_allow_html=True)
st.markdown("<div class='fade-in'><h4 style='text-align: center; color: grey;'>Explore, Discover, and Support Authentic Local Products</h4></div>", unsafe_allow_html=True)

# Optional Banner Image (safely handled)
try:
    st.image("images/himachal-banner.jpg", use_column_width=True)
except:
    st.info("🖼️ You can add an optional banner image at `images/himachal-banner.jpg`.")

# About the App
st.markdown("""
---

### ❓ What Is This App?

This platform helps you explore **Geographical Indication (GI)**-tagged products from the breathtaking state of **Himachal Pradesh**.

GI Tags are granted to traditional products that are:

- ✅ Unique to a location  
- ✅ Made using traditional techniques  
- ✅ Protected by law  
- ✅ Culturally significant

---

### 💡 How This App Helps You

- 🛍️ Discover authentic products like **Kullu Shawls**, **Kangra Tea**, and more  
- 📍 Filter by location or category  
- 🗺️ See products on a map  
- 🖼️ Enjoy beautiful images in our product showcase

---
""")
