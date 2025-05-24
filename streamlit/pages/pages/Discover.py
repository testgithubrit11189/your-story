import streamlit as st
import pandas as pd
import os
from PIL import Image
import pydeck as pdk

# Page config
st.set_page_config(page_title="Discover GI Tags", layout="wide")  # ✅ first Streamlit command

# CSS for hover animation on headings
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

.fade-in h2:hover {
  color: #2c6e49;
  transform: scale(1.03);
  cursor: pointer;
}
</style>
""", unsafe_allow_html=True)

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("gi_tags.csv")

data = load_data()

# Title with hover effect
st.markdown("<div class='fade-in'><h1>Discover GI Products by Location</h1></div>", unsafe_allow_html=True)

# Sidebar Filters
st.sidebar.header("🔍 Filter Products")
category_filter = st.sidebar.selectbox("Select Category", ["All"] + sorted(data["Category"].unique()))
location_filter = st.sidebar.selectbox("Select Location", ["All"] + sorted(data["Location"].unique()))

# Filtering
filtered_data = data.copy()
if category_filter != "All":
    filtered_data = filtered_data[filtered_data["Category"] == category_filter]
if location_filter != "All":
    filtered_data = filtered_data[filtered_data["Location"] == location_filter]

# Map Section
map_data = filtered_data[['Latitude', 'Longitude', 'Product', 'Location', 'Category']].dropna().copy()
map_data['Color'] = map_data['Category'].apply(
    lambda x: [0, 200, 0, 160] if x == 'Handicraft' else [0, 0, 200, 160]
)

# Map subheader with hover effect
st.markdown("<div class='fade-in'><h2>🗺️ GI-Tagged Product Map</h2></div>", unsafe_allow_html=True)
if not map_data.empty:
    layer = pdk.Layer(
        'ScatterplotLayer',
        data=map_data,
        get_position='[Longitude, Latitude]',
        get_fill_color='Color',
        get_radius=50000,
        pickable=True
    )

    tooltip = {
        "html": "<b>{Product}</b><br>{Location}<br>{Category}",
        "style": {"backgroundColor": "steelblue", "color": "white"}
    }

    st.markdown("**Legend:** 🟢 Handicraft &nbsp;&nbsp;&nbsp; 🔵 Agriculture")
    st.pydeck_chart(pdk.Deck(
        initial_view_state=pdk.ViewState(
            latitude=31.5,
            longitude=77.0,
            zoom=6,
            pitch=0
        ),
        layers=[layer],
        tooltip=tooltip
    ))
else:
    st.info("No products to show on map.")

# Products subheader with hover effect
st.markdown("<div class='fade-in'><h2>📋 GI Products Matching Your Selection</h2></div>", unsafe_allow_html=True)
if not filtered_data.empty:
    for _, row in filtered_data.iterrows():
        emoji = "🧶" if "shawl" in row['Product'].lower() else \
                "🧦" if "sock" in row['Product'].lower() else \
                "☕" if "tea" in row['Product'].lower() else \
                "🍎" if "apple" in row['Product'].lower() else "🛍️"

        with st.expander(f"{emoji} {row['Product']}"):
            img_path = f"images/{row['Product'].lower().replace(' ', '_')}.jpg"
            if os.path.exists(img_path):
                st.image(Image.open(img_path), use_column_width=True)
            else:
                st.info("📷 Image not available")

            cat_icon = "🧶" if row['Category'] == "Handicraft" else "🌾"
            category_badge = f"<span style='background-color:#d1e7dd;color:#0f5132;padding:4px 10px;border-radius:5px;'>{cat_icon} {row['Category']}</span>"
            location_badge = f"<span style='background-color:#cfe2ff;color:#084298;padding:4px 10px;border-radius:5px;'>📍 {row['Location']}</span>"
            st.markdown(category_badge + " &nbsp;&nbsp;" + location_badge, unsafe_allow_html=True)

            st.write(f"**Description:** {row['Description']}")
else:
    st.warning("No products found.")
