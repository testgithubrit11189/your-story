import streamlit as st

st.set_page_config(page_title="About GI Tags", layout="centered")

# CSS for animation and hover effect
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

.fade-in h3:hover {
  color: #2c6e49;
  transform: scale(1.03);
  cursor: pointer;
}
</style>
""", unsafe_allow_html=True)

# Title
st.markdown("<div class='fade-in'><h1 style='text-align: center;'>About Geographical Indications (GI Tags)</h1></div>", unsafe_allow_html=True)

# Introduction
st.markdown("""
<div class='fade-in'>
<p style='text-align: justify; font-size: 18px;'>
A <strong>Geographical Indication (GI)</strong> is a name or sign used on products that have a specific geographical origin and possess qualities or a reputation due to that origin.

GI Tags are granted under the <strong>Geographical Indications of Goods (Registration and Protection) Act, 1999</strong> in India.
</p>
</div>
""", unsafe_allow_html=True)

# Why GI Tags Matter
st.markdown("""
<div class='fade-in'>
<h3>🎯 Why GI Tags Are Important</h3>
<ul style='font-size: 17px;'>
    <li>✅ They protect the unique identity of local goods</li>
    <li>✅ They ensure authenticity for customers</li>
    <li>✅ They support local economies, artisans & farmers</li>
    <li>✅ They prevent misuse or imitation of traditional names</li>
    <li>✅ They preserve cultural heritage and craft knowledge</li>
</ul>
</div>
""", unsafe_allow_html=True)

# Examples Section
st.markdown("""
<div class='fade-in'>
<h3>🌿 Examples of GI-Tagged Products in Himachal</h3>
<ul style='font-size: 17px;'>
    <li>🧶 <strong>Kullu Shawl</strong> – traditional handwoven woolen shawls</li>
    <li>☕ <strong>Kangra Tea</strong> – aromatic tea from the Kangra valley</li>
    <li>🧦 <strong>Lahauli Socks</strong> – warm woolen socks with local patterns</li>
</ul>
</div>
""", unsafe_allow_html=True)

# Ending Note
st.markdown("""
<div class='fade-in'>
<p style='text-align: justify; font-size: 17px;'>
By recognizing and promoting GI-tagged products, we not only preserve culture but also encourage sustainable economic growth for the communities of Himachal Pradesh.
</p>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center;'>🧭 Navigate to <strong>Showcase</strong> or <strong>Discover</strong> from the sidebar to explore more.</p>", unsafe_allow_html=True)
