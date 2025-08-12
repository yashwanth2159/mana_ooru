# app.py

import streamlit as st
from PIL import Image

# Set page config
st.set_page_config(
    page_title="Mana Ooru – Stories, Sayings, and Secrets of My Village",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Landing Banner
# Landing Banner with background image
st.markdown(r"""
<div style="
    position: relative;
    background-image: url('https://i.pinimg.com/736x/d7/c1/7d/d7c17d863e5f5e401f3b60409d6c749e.jpg');
    background-size: cover;
    background-position: center;
    height: 300px;
    border-radius: 10px;
    overflow: hidden;
">
    <div style="
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, 0.5);  /* Dark semi-transparent overlay */
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
    ">
        <h1 style="color: white; margin-bottom: 10px;">Mana Ooru</h1>
        <h4 style="color: white;">Stories, Sayings, and Secrets of My Village</h4>
    </div>
</div>
""", unsafe_allow_html=True)



st.markdown("---")

# Intro Section
st.markdown("##  Welcome to Mana Ooru")
st.write("""
**Mana Ooru** is a cultural archive where you can explore and contribute stories, proverbs, songs, festivals, and landmarks that define the spirit of your Telugu village.
This is your platform to preserve and celebrate local heritage, told by the people, for the people.
""")

st.markdown("---")

# Navigation links to other sections
st.markdown("###  Explore Sections")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("📖 Mana Katha"):
        st.switch_page("pages/Mana_Katha.py")

    if st.button("🪤 Mana Samethalu"):
        st.switch_page("pages/Mana_Samethalu.py")

with col2:
    if st.button("🎉 Mana Pandugalu"):
        st.switch_page("pages/Mana_Pandugalu.py")

    if st.button("🎶 Mana Paata"):
        st.switch_page("pages/Mana_Paata.py")

with col3:
    if st.button("📍 Mana Sthalam"):
        st.switch_page("pages/Mana_Sthalam.py")

st.markdown("---")

from PIL import Image
import os

st.markdown("##  Meet Our Team")

# Team data
team = [
    {"name": "Sai Chaithanya Adicherla", "role": "Team Lead & Deployment Manager", "image": "images/sai.jpg"},
    {"name": "Yashwanth Gangishetti", "role": "Frontend & UX Designer", "image": ""},
    {"name": "Prabhukiran", "role": "Backend & Data Handler", "image": ""},
    {"name": "Ankith", "role": "Feature Developer", "image": ""},
    {"name": "Shaik Sydavali", "role": "Outreach & Documentation Lead", "image": ""},
]

cols = st.columns(5)

for i, member in enumerate(team):
    with cols[i]:
        if os.path.exists(member["image"]):
            img = Image.open(member["image"])
            resized_img = img.resize((200, 200))  # Fixed width and height
            st.image(resized_img)
        else:
            st.warning(f"Image not found: {member['image']}")
        st.markdown(f"### {member['name']}")
        st.markdown(f"**{member['role']}**")
# Footer
st.markdown("---")
st.markdown("<footer style='text-align:center;'>© 2025 Mana Ooru | Built with ❤️ using Streamlit</footer>", unsafe_allow_html=True)
