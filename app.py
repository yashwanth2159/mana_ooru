# app.py
import streamlit as st

# -----------------------------
# Basic Page Setup
# -----------------------------
st.set_page_config(
    page_title="Mana Ooru – Stories, Sayings, and Secrets of My Village",
    page_icon="🏡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# -----------------------------
# Minimal Global Styles
# -----------------------------
st.markdown("""
<style>
html, body, [class*="css"]  { font-family: 'Inter', system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif; }
.main > div { max-width: 1100px; margin: 0 auto; }
.hero {
  position: relative;
  height: 320px;
  border-radius: 16px;
  overflow: hidden;
  background-image: url('https://i.pinimg.com/736x/d7/c1/7d/d7c17d863e5f5e401f3b60409d6c749e.jpg');
  background-size: cover;
  background-position: center;
}
.hero::after {
  content: "";
  position: absolute; inset: 0;
  background: rgba(0,0,0,0.25);
}
.hero-inner {
  position: absolute; inset: 0;
  display: flex; flex-direction: column;
  align-items: center; justify-content: center;
  text-align: center; padding: 0 18px;
}
.hero h1, .hero p {
  text-shadow: 2px 2px 6px rgba(0,0,0,0.6); 
  color: #ffffff;   /* change text color here */
}

.hero p { color: #ffffff;
  margin: 0; 
  font-size: 18px; 
}
.team-item {
  padding: 10px 14px;
  border: 1px solid #efefef;
  border-radius: 12px;
  background: #fff;
}
footer small { color: #666; }
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Hero Banner
# -----------------------------
st.markdown("""
<div class="hero">
  <div class="hero-inner">
    <h1>Mana Ooru</h1>
    <p>Stories, Sayings, and Secrets of My Village</p>
  </div>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# Intro
# -----------------------------
st.subheader("Welcome to Mana Ooru")
st.write(
    "Mana Ooru is a digital space dedicated to capturing the stories, sayings, and secrets of our village. " 
    "It celebrates the essence of rural life by preserving local tales, age-old proverbs, and hidden gems  " 
    "know only to the community. Visitors can explore, share, and contribute their memories through text,  " 
    "image, and audio. Together, we create a lasting treasure of our village heritage for future generation"
)

st.markdown("---")

# -----------------------------
# Explore Sections
# -----------------------------
st.subheader("Explore Sections")

# CSS styling for rounded-square cards
st.markdown("""
    <style>
        .explore-container {
            display: grid;
            grid-template-columns: repeat(5, 1fr);
            gap: 30px;
            padding: 20px;
            justify-items: left;
        }
        .explore-card {
            width: 200px;
            height: 200px;
            background-color: #f8f9fa;
            border-radius: 70px;
            display: flex;
            align-items: left;
            justify-content: left;
            font-size: 40px;
            box-shadow: 0 12px 16px rgba(0,0,0,0.2);
            transition: all 0.2s ease-in-out;
            cursor: pointer;
        }
        .explore-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 16px rgba(0,0,0,0.2);
        }
        .explore-label {
            text-align: left;
            margin-top: 10px;
            font-size: 16px;
            font-weight: bold;
            color: #333;
        }
    </style>
""", unsafe_allow_html=True)

# Layout for clickable cards
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    if st.button("📖", key="katha_btn"):
        st.switch_page("pages/Mana_Katha.py")
    st.markdown('<div class="explore-label">Mana Katha</div>', unsafe_allow_html=True)

with col2:
    if st.button("🪤", key="samethalu_btn"):
        st.switch_page("pages/Mana_Samethalu.py")
    st.markdown('<div class="explore-label">Mana Samethalu</div>', unsafe_allow_html=True)

with col3:
    if st.button("🎉", key="pandugalu_btn"):
        st.switch_page("pages/Mana_Pandugalu.py")
    st.markdown('<div class="explore-label">Mana Pandugalu</div>', unsafe_allow_html=True)

with col4:
    if st.button("🎶", key="paata_btn"):
        st.switch_page("pages/Mana_Paata.py")
    st.markdown('<div class="explore-label">Mana Paata</div>', unsafe_allow_html=True)

with col5:
    if st.button("📍", key="sthalam_btn"):
        st.switch_page("pages/Mana_Sthalam.py")
    st.markdown('<div class="explore-label">Mana Sthalam</div>', unsafe_allow_html=True)







st.markdown("---")

# -----------------------------
# Team
# -----------------------------
st.subheader("Meet Our Team")
team = [
    {"name": "Sai Chaithanya Adicherla", "role": "Team Lead & Deployment Manager"},
    {"name": "Yashwanth Gangishetti", "role": "Frontend & UX Designer"},
    {"name": "Prabhukiran", "role": "Backend & Data Handler"},
    {"name": "Ankith", "role": "Feature Developer"},
    {"name": "Shaik Sydavali", "role": "Outreach & Documentation Lead"},
]
t1, t2 = st.columns(2, gap="large")
for i, member in enumerate(team):
    with (t1 if i % 2 == 0 else t2):
        st.markdown(
            f"""<div class="team-item"><strong>{member['name']}</strong><br><span>{member['role']}</span></div>""",
            unsafe_allow_html=True
        )

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.markdown(
    "<footer style='text-align:center; margin: 8px 0 18px;'><small>© 2025 Mana Ooru • Built with ❤️ using Streamlit</small></footer>",
    unsafe_allow_html=True
)