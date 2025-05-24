import streamlit as st
import pandas as pd
from datetime import datetime
import os
import numpy as np

# File paths
data_file = "accommodation_data_with_images (1).csv"
bookings_file = "bookings.csv"

# Load dataset
if os.path.exists(data_file):
    data = pd.read_csv(data_file)

    # Remove "Dorm" entries
    data = data[data["type"].str.lower() != "dorm"]

    # Add "Resort" type explicitly if not present
    if "Resort" not in data["type"].unique():
        resort_example = data.iloc[0].copy()
        resort_example["name"] = "Sample Resort"
        resort_example["type"] = "Resort"
        data = pd.concat([data, pd.DataFrame([resort_example])], ignore_index=True)
else:
    st.error(f"❌ Data file not found: `{data_file}`. Please ensure the file is in the same directory.")
    st.stop()

# Add missing columns with default or dummy values
if "description" not in data.columns:
    def get_description(row):
        t = row["type"].lower()
        if t == "hotel":
            return "Comfortable hotel with excellent amenities and friendly staff."
        elif t == "hostel":
            return "Affordable and social accommodation perfect for travelers."
        elif t == "resort":
            return "Luxury resort offering relaxing atmosphere and beautiful views."
        else:
            return "Cozy and welcoming accommodation."
    data["description"] = data.apply(get_description, axis=1)

if "num_rooms" not in data.columns:
    data["num_rooms"] = np.random.randint(1, 10, size=len(data))

if "price" not in data.columns:
    data["price"] = np.random.randint(30, 200, size=len(data))

# Create bookings.csv if missing
if not os.path.exists(bookings_file):
    pd.DataFrame(columns=["name", "address", "type", "room_type", "timestamp"]).to_csv(bookings_file, index=False)

# Streamlit app setup
st.set_page_config(page_title="Accommodation Finder", layout="wide")

# CSS styling
st.markdown("""
<style>
.card {
    background-color: #1e293b;
    padding: 1rem;
    border-radius: 12px;
    margin-bottom: 1.5rem;
    color: white;
}
.card img {
    width: 100%;
    height: 160px;
    border-radius: 8px;
    object-fit: cover;
}
</style>
""", unsafe_allow_html=True)

st.title("🏨 Accommodation Finder")

# Filters
min_rating = st.slider("Minimum rating", 0.0, 5.0, 0.0, 0.1)
max_price = st.slider("Maximum price", 30, 200, 150)

# Dropdowns
hotel_types = sorted(data["type"].unique())
selected_type = st.selectbox("Select accommodation type:", ["Any"] + hotel_types)

room_types = sorted(data["room_type"].unique())
selected_room = st.selectbox("Select room type:", ["Any"] + room_types)

search_query = st.text_input("Search by name or address").lower()

# Filter logic
filtered_data = data.copy()

if selected_type != "Any":
    filtered_data = filtered_data[filtered_data["type"] == selected_type]

if selected_room != "Any":
    filtered_data = filtered_data[filtered_data["room_type"] == selected_room]

filtered_data = filtered_data[
    (filtered_data["rating"] >= min_rating) &
    (filtered_data["price"] <= max_price) &
    (
        filtered_data["name"].str.lower().str.contains(search_query) |
        filtered_data["address"].str.lower().str.contains(search_query)
    )
]

# Display Results in Grid Layout
st.markdown("### Available accommodations:")

if filtered_data.empty:
    st.warning("No accommodations match your filters. Try adjusting the filters.")
else:
    cols = st.columns(3)  # Grid of 3 columns

    for i, (_, row) in enumerate(filtered_data.iterrows()):
        with cols[i % 3]:
            st.markdown(f"""
            <div class="card">
                <img src="{row['image_url']}" alt="Hotel Image" />
                <h4>{row['name']}</h4>
                <p>{row['address']}</p>
                <p><b>Type:</b> {row['type']} | <b>Room:</b> {row['room_type']}</p>
                <p>⭐ {row['rating']} | 💰 ₹{row['price']}</p>
                <p>{row['description']}</p>
                <p>🛏️ Available rooms: {row['num_rooms']}</p>
            </div>
            """, unsafe_allow_html=True)

            if row['num_rooms'] > 0:
                if st.button(f"Book Now - {row['name']}", key=f"book_{i}"):
                    st.success("✅ Booking confirmed! Email has been sent.")
                    data.at[row.name, 'num_rooms'] -= 1
                    booking_record = {
                        "name": row["name"],
                        "address": row["address"],
                        "type": row["type"],
                        "room_type": row["room_type"],
                        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    }
                    pd.DataFrame([booking_record]).to_csv(bookings_file, mode='a', header=False, index=False)

# Save updated room availability
data.to_csv(data_file, index=False)
