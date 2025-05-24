import streamlit as st

# Page config
st.set_page_config(page_title="Himachal Adventures", layout="wide")

# Custom CSS for background and text
st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(rgba(0,0,0,0.8), rgba(0,0,0,0.8)),
                    url("https://images.unsplash.com/photo-1611132251536-0d9fe8c5c660?ixlib=rb-4.0.3&auto=format&fit=crop&w=1650&q=80");
        background-size: cover;
        background-position: center;
    }
    .main-content {
        color: white;
        padding: 2rem;
    }
    h1, h2, h3, h4 {
        color: #f8f8f8;
    }
    </style>
""", unsafe_allow_html=True)

# Container
st.markdown("<div class='main-content'>", unsafe_allow_html=True)

# Header
st.markdown("<h1 style='text-align:center;'>🏔 Explore Himachal Adventures</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align:center;'>Discover thrilling activities with local guides</h4><br>", unsafe_allow_html=True)

# Reliable image source (picsum.photos for demo)
adventures = [
    {
        "title": "Paragliding in Bir Billing",
        "location": "Bir Billing",
        "cost": "₹2,500",
        "desc": "Soar through the skies and feel the freedom.",
        "image": "https://picsum.photos/id/1005/800/400"
    },
    {
        "title": "River Rafting in Kullu",
        "location": "Kullu",
        "cost": "₹1,000",
        "desc": "Ride the rapids of the Beas River.",
        "image": "https://picsum.photos/id/1015/800/400"
    },
    {
        "title": "Trekking to Kheerganga",
        "location": "Kasol",
        "cost": "₹1,200",
        "desc": "Hike to natural hot springs in the Parvati Valley.",
        "image": "https://picsum.photos/id/1040/800/400"
    },
    {
        "title": "Skiing in Solang Valley",
        "location": "Manali",
        "cost": "₹2,000",
        "desc": "Ski on the snow-covered Himalayan slopes.",
        "image": "https://picsum.photos/id/1011/800/400"
    },
    {
        "title": "Camping in Tirthan Valley",
        "location": "Tirthan Valley",
        "cost": "₹1,500",
        "desc": "Camp under stars in a peaceful green valley.",
        "image": "https://picsum.photos/id/1018/800/400"
    },
]

# Display each adventure
for adv in adventures:
    st.image(adv["image"], use_container_width=True, caption=adv["title"])
    st.markdown(f"### 📍 {adv['title']}")
    st.markdown(f"*Location:* {adv['location']}")
    st.markdown(f"*Cost:* {adv['cost']} per person")
    st.markdown(f"💬 {adv['desc']}")
    st.markdown("---")

# Footer
st.markdown("## 🤝 Support Local Adventure Tourism")
col1, col2, col3 = st.columns(3)
col1.success("✅ Eco Certified")
col2.success("🧭 Trusted Local Guides")
col3.success("🎒 Adventure Verified")

st.markdown("<br><hr>", unsafe_allow_html=True)
st.markdown("📞 *Contact us:* explore@himadventure.com | 📍 Himachal Pradesh, India")

# Close container
st.markdown("</div>", unsafe_allow_html=True)