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

def card(label, emoji, link):
    return f"""
    <a href="{link}" target="_self" style="
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-decoration: none;
        color: black;
        width: 120px; /* ensures same width for all cards */
    ">
        <div style="
            font-size: 32px;
            background-color: #f4f4f4;
            padding: 14px;
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            width: 60px;
            height: 60px;
            margin-bottom: 8px;
        ">{emoji}</div>
        <div style="
            font-size: 16px;
            font-weight: 500;
            text-align: center;
            width: 100%;
        ">
            {label}
        </div>
    </a>
    """

explore_items = [
    ("Mana Katha", "📖", "pages/Mana_Katha"),
    ("Mana Samethalu", "🪤", "pages/Mana_Samethalu"),
    ("Mana Pandugalu", "🎉", "pages/Mana_Pandugalu"),
    ("Mana Paata", "🎶", "pages/Mana_Paata"),
    ("Mana Sthalam", "📍", "pages/Mana_Sthalam"),
]

# First row - 3 items
cols1 = st.columns(3, gap="large")
for col, (label, emoji, link) in zip(cols1, explore_items[:3]):
    col.markdown(card(label, emoji, link), unsafe_allow_html=True)

# Second row - 2 items centered
cols2 = st.columns([0.5, 1, 1, 0.5], gap="large")
for col, (label, emoji, link) in zip(cols2[1:3], explore_items[3:]):
    col.markdown(card(label, emoji, link), unsafe_allow_html=True)


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
