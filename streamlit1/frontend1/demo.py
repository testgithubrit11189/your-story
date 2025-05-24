import streamlit as st
from PIL import Image
import base64
from io import BytesIO
import os

st.set_page_config(page_title="Sustainable Tourism App", layout="wide")

# Add custom font and hover effects for headings
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;700&display=swap');

h1, h2, h3, h4, h5, h6 {
    font-family: 'Poppins', sans-serif !important;
}

h2:hover {
    color: #2a9d8f;
    cursor: pointer;
    transition: all 0.3s ease;
    transform: scale(1.05);
}

h3:hover {
    color: #e76f51;
    cursor: pointer;
    transition: all 0.3s ease;
    transform: scale(1.05);
}

.intro-img {
    width: 100%; height: 80vh; max-height: 600px;
    background-size: cover; background-position: center;
    display: flex; flex-direction: column; align-items: center;
    justify-content: center; text-align: center; color: white;
    padding: 0 20px; box-sizing: border-box;
}

.intro-img.shrink {
    height: 150px !important;
}

.intro-img h2 {
    font-size: 2.8rem; text-shadow: 2px 2px 4px #000;
    margin-bottom: 10px;
}

.intro-img.shrink h2 {
    font-size: 1.5rem !important;
}

.intro-img p {
    font-size: 1.2rem; text-shadow: 1px 1px 3px #000;
    margin-bottom: 20px;
}

.intro-img.shrink p {
    font-size: 0.9rem !important;
}

.btn-container {
    display: flex; gap: 15px; justify-content: center;
    margin-top: 10px;
}

.btn {
    background-color: #2a9d8f;
    color: white;
    padding: 12px 28px;
    border-radius: 30px;
    font-weight: 600;
    font-family: 'Poppins', sans-serif;
    cursor: pointer;
    transition: background-color 0.3s ease;
    border: none;
    box-shadow: 0 4px 8px rgba(42, 157, 143, 0.3);
}

.btn:hover {
    background-color: #21867a;
}
</style>
""", unsafe_allow_html=True)

# Initialize session state variables
if "show_login" not in st.session_state:
    st.session_state.show_login = False
if "user_db" not in st.session_state:
    st.session_state.user_db = {}
if "logged_in_user" not in st.session_state:
    st.session_state.logged_in_user = None

# Function to load image and return base64 string
def get_base64_image(path):
    if os.path.exists(path):
        try:
            img = Image.open(path)
            buffered = BytesIO()
            img.save(buffered, format="PNG")
            return base64.b64encode(buffered.getvalue()).decode()
        except Exception as e:
            st.error(f"Error loading image {path}: {e}")
            return None
    else:
        return None

# Helper to rerun safely
def safe_rerun():
    try:
        st.experimental_rerun()
    except AttributeError:
        st.stop()

# Load images
intro_base64 = get_base64_image("img/intro.jpg")
about_base64 = get_base64_image("img/about.jpg")

# Load AOS CSS and JS for animations
st.markdown("""
<link href="https://cdnjs.cloudflare.com/ajax/libs/aos/2.3.4/aos.css" rel="stylesheet">
<script src="https://cdnjs.cloudflare.com/ajax/libs/aos/2.3.4/aos.js"></script>
<script>
AOS.init({ duration: 1200 });
</script>
""", unsafe_allow_html=True)

# --- If logged in, show welcome and logout option ---
if st.session_state.logged_in_user:
    user = st.session_state.logged_in_user
    user_info = st.session_state.user_db.get(user, {})
    st.sidebar.success(f"Logged in as: {user} ({user_info.get('role','')})")
    if st.sidebar.button("Logout"):
        st.session_state.logged_in_user = None
        st.session_state.show_login = False
        safe_rerun()

    # Main content after login
    st.title("Welcome to Sustainable Tourism App 🌿")
    st.write(f"Hello **{user_info.get('name','')}**, explore the app content below!")

else:
    # --- Intro Section with buttons ---
    if intro_base64:
        st.markdown(f"""
        <div class="intro-img" id="introSection" style="background-image: url('data:image/png;base64,{intro_base64}');">
            <h2>Travel Meaningfully. Discover Authentically.</h2>
            <p>Trusted Travel Companion powered by GI Tags 🇮🇳</p>
            <div class="btn-container">
                <button class="btn" onclick="window.open('https://your-map-link.com', '_blank')">Explore the Map</button>
                <button class="btn" onclick="window.open('https://your-download-link.com', '_blank')">Download Now</button>
            </div>
        </div>
        <script>
        window.addEventListener('scroll', function() {{
            var intro = document.getElementById('introSection');
            var scrollTop = window.pageYOffset || document.documentElement.scrollTop;
            if (scrollTop > 150) {{ intro.classList.add('shrink'); }}
            else {{ intro.classList.remove('shrink'); }}
        }});
        </script>
        """, unsafe_allow_html=True)
    else:
        st.warning("⚠️ 'intro.jpg' not found or failed to load.")

    # --- About Section ---
    st.markdown("### About the Project")
    if about_base64:
        about_html = f"""
        <div class="about-block" style="display: flex; align-items: center; justify-content: space-between; background-color: #d4edda; padding: 20px; border-radius: 12px; gap: 30px; margin-bottom: 40px; color: black;">
            <div style="flex: 2; font-size: 1.1rem; line-height: 1.6;">
                Our app promotes eco-tourism, supports local businesses, and highlights authentic handicrafts 
                using GI tags issued by the Government of India. We aim to make travel more meaningful, reduce scams, 
                and empower the local economy.
            </div>
            <div style="flex: 1; max-width: 180px; max-height: 180px; border-radius: 16px; overflow: hidden;">
                <img src="data:image/png;base64,{about_base64}" alt="About Image" style="width: 100%; height: 100%; object-fit: cover; border-radius: 16px;"/>
            </div>
        </div>
        """
        st.markdown(about_html, unsafe_allow_html=True)
    else:
        st.warning("⚠️ 'about.jpg' not found or failed to load.")

    st.markdown("---")

    # --- GI-Tagged Products ---
    st.markdown("### Discover GI-Tagged Products")
    col1, col2 = st.columns(2)
    with col1:
        if os.path.exists("img/Kanchipuram.jpg"):
            st.image("img/Kanchipuram.jpg", caption="Kancheepuram Silk - Chennai", width=250)
            st.success("GI Tag Verified ✅")
        else:
            st.warning("⚠️ 'Kanchipuram.jpg' not found.")
    with col2:
        if os.path.exists("img/Bhadohi.jpg"):
            st.image("img/Bhadohi.jpg", caption="Bhadohi Carpet - Bhadohi", width=250)
            st.success("GI Tag Verified ✅")
        else:
            st.warning("⚠️ 'Bhadohi.jpg' not found.")

    st.markdown("---")

    # --- Local Festivals ---
    st.markdown("### Celebrate Local Festivals")
    col1, col2 = st.columns(2)
    with col1:
        if os.path.exists("img/budhi.jpg"):
            st.image("img/budhi.jpg", caption="Budhi Diwali - Himachal Pradesh", width=250)
            st.info("Celebrate the harvest with flower carpets, boat races, and cultural dances.")
        else:
            st.warning("⚠️ 'budhi.jpg' not found.")
    with col2:
        if os.path.exists("img/pongal.jpg"):
            st.image("img/pongal.jpg", caption="Pongal - Tamil Nadu", width=250)
            st.info("A thanksgiving festival for the Sun God with traditional cooking and decorations.")
        else:
            st.warning("⚠️ 'pongal.jpg' not found.")

    st.markdown("---")

    # --- Adventure Activities ---
    st.markdown("### 🧷 Adventure Activities")
    col1, col2, col3 = st.columns(3)
    with col1:
        if os.path.exists("img/fort.jpg"):
            st.image("img/fort.jpg", caption="Neemrana Fort Palace - Rajasthan", width=200)
        else:
            st.warning("⚠️ 'fort.jpg' not found.")
    with col2:
        if os.path.exists("img/safari.jpg"):
            st.image("img/safari.jpg", caption="Camel Safari - Rajasthan", width=200)
        else:
            st.warning("⚠️ 'safari.jpg' not found.")
    with col3:
        if os.path.exists("img/raft.jpg"):
            st.image("img/raft.jpg", caption="River Rafting - Arunachal Pradesh", width=200)
        else:
            st.warning("⚠️ 'raft.jpg' not found.")

    st.markdown("---")

    # --- Top Staying Places (Hotels & Hostels) ---
    st.markdown("### Top Staying Places (Hotels & Hostels)")
    col1, col2, col3 = st.columns(3)
    with col1:
        if os.path.exists("img/hotel2.jpg"):
            st.image("img/hotel2.jpg", caption="Heritage Hotel - Jaipur", width=250)
        else:
            st.warning("⚠️ 'hotel2.jpg' not found.")
    with col2:
        if os.path.exists("img/hotel1.jpg"):
            st.image("img/hotel1.jpg", caption="Backpacker Hostel - Goa", width=250)
        else:
            st.warning("⚠️ 'hotel1.jpg' not found.")
    with col3:
        if os.path.exists("img/hotel3.jpg"):
            st.image("img/hotel3.jpg", caption="Luxury Resort - Kerala", width=250)
        else:
            st.warning("⚠️ 'hotel3.jpg' not found.")

    st.markdown("---")

    # --- Get Started / Login / Register ---
    if not st.session_state.show_login:
        if st.button("Get Started 🚀"):
            st.session_state.show_login = True
            safe_rerun()
    else:
        st.markdown("## 🔐 Login or Register")
        tab1, tab2 = st.tabs(["Login", "Register"])

        with tab1:
            st.markdown("### Existing User Login")
            username = st.text_input("Username", key="login_user")
            password = st.text_input("Password", type="password", key="login_pass")

            if st.button("Login"):
                user_db = st.session_state.user_db
                if username in user_db and user_db[username]["password"] == password:
                    st.session_state.logged_in_user = username
                    st.success(f"✅ Logged in as {username} ({user_db[username]['role']})")
                    safe_rerun()
                else:
                    st.error("❌ Invalid username or password")

        with tab2:
            st.markdown("### New User Registration")
            role = st.selectbox("Register as", ["Traveler", "Vendor"])
            name = st.text_input("Full Name")
            email = st.text_input("Email")
            contact = st.text_input("Contact Number")
            new_username = st.text_input("Choose a Username")
            new_password = st.text_input("Choose a Password", type="password")

            if st.button("Register"):
                user_db = st.session_state.user_db
                if new_username in user_db:
                    st.warning("⚠️ Username already taken. Please choose another.")
                elif not all([name, email, contact, new_username, new_password]):
                    st.warning("⚠️ Please fill in all fields.")
                else:
                    st.session_state.user_db[new_username] = {
                        "name": name,
                        "email": email,
                        "contact": contact,
                        "password": new_password,
                        "role": role
                    }
                    st.success("✅ Registration successful! You can now login.")
                    safe_rerun()
