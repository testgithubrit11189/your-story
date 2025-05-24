import streamlit as st

# Page config
st.set_page_config(page_title="Routed Roots", layout="centered")

# Styling
st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Lobster&display=swap" rel="stylesheet">

    <style>
        .main-title {
            font-family: 'Lobster', cursive;
            font-size: 50px;
            color: #2d6a4f;
            text-align: center;
            margin-bottom: 20px;
            transition: all 0.3s ease-in-out;                         
            cursor: pointer;
        }
        .main-title:hover {
            color: #40916c;
            text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);
            transform: scale(1.05);
        }
        .place-name {
            text-align: center;
            font-weight: bold;
            font-size: 18px;
            margin-top: 5px;
        }
    </style>
""", unsafe_allow_html=True)

# Title with hover effect
st.markdown('<div class="main-title">Routed Roots</div>', unsafe_allow_html=True)

# Search Bar
search_query = st.text_input("", placeholder="Search for destinations...", key="search")

# Popular Places Header
st.markdown("### Popular Places in India")

# Image URLs
popular_places = {"Himachal Pradesh" : r"search\hm.jpg",
    "Rajasthan": r"search\rj.jpg",           
    "Kerala": r"search\ker.jpg",
    "Uttarakhand": r"search\uk.jpg"
    
}

# Display images in 2 columns
cols = st.columns(2)
for i, (place, img_url) in enumerate(popular_places.items()):
    with cols[i % 2]:
        st.image(img_url, use_container_width=True)
        st.markdown(f"<div class='place-name'>{place}</div>", unsafe_allow_html=True)
