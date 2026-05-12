import streamlit as st
import pandas as pd
import plotly.express as px

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="AMIVERSE Rewards",
    page_icon="🏆",
    layout="wide"
)

# =====================================================
# LOAD CSS
# =====================================================

with open("assets/style.css") as f:

    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# =====================================================
# SESSION STATE
# =====================================================

if "username" not in st.session_state:

    st.session_state.username = "student@amity.edu"

if "coins" not in st.session_state:

    st.session_state.coins = 1250

if "logged_in" not in st.session_state:

    st.session_state.logged_in = True

# =====================================================
# SESSION
# =====================================================

if "coins" not in st.session_state:
    st.session_state.coins = 1250

# =====================================================
# BADGES
# =====================================================

badges = [

    {
        "title": "Resume Expert",
        "icon": "📄",
        "coins": 100,
        "description": "Upload and optimize resume successfully"
    },

    {
        "title": "Blockchain Verified",
        "icon": "🔗",
        "coins": 150,
        "description": "Verify certificates on blockchain"
    },

    {
        "title": "Placement Ready",
        "icon": "🚀",
        "coins": 200,
        "description": "Achieve high placement prediction score"
    },

    {
        "title": "AI Explorer",
        "icon": "🤖",
        "coins": 80,
        "description": "Use AMIVERSE AI Assistant"
    },

    {
        "title": "Hackathon Hero",
        "icon": "🏆",
        "coins": 250,
        "description": "Participate in coding competitions"
    },

    {
        "title": "Internship Star",
        "icon": "💼",
        "coins": 300,
        "description": "Complete internship verification"
    }
]

# =====================================================
# SIDEBAR
# =====================================================

with st.sidebar:

    st.markdown("""
    <div style="text-align:center;">

    <img src="https://cdn-icons-png.flaticon.com/512/1055/1055687.png"
    width="90">

    <h1 style="
    color:white;
    font-size:48px;
    font-weight:800;
    margin-top:15px;
    margin-bottom:10px;
    letter-spacing:2px;
    ">
    AMIVERSE
    </h1>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.page_link(
        "app.py",
        label="Dashboard"
    )

    st.page_link(
        "pages/Prediction.py",
        label="Prediction"
    )

    st.page_link(
        "pages/Analytics.py",
        label="Analytics"
    )

    st.page_link(
        "pages/Resume.py",
        label="Resume"
    )

    st.page_link(
        "pages/Verification.py",
        label="Verification"
    )

    st.page_link(
        "pages/Assistant.py",
        label="Assistant"
    )

    st.page_link(
        "pages/Wallet.py",
        label="Wallet"
    )

    st.page_link(
        "pages/Rewards.py",
        label="Rewards"
    )

    st.page_link(
        "pages/Profile.py",
        label="Profile"
    )

    st.page_link(
        "pages/Leaderboard.py",
        label="Leaderboard"
    )

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(f"""
    <div class="card" style="
    text-align:center;
    padding:20px;
    ">

    <h3 style="
    color:white;
    margin-bottom:10px;
    ">
    👤 {st.session_state.username}
    </h3>

    <p style="
    color:#94a3b8;
    font-size:14px;
    margin-bottom:15px;
    ">
    AI Student Wallet
    </p>

    <h2 style="
    color:#3b82f6;
    font-size:30px;
    ">
    🪙 {st.session_state.coins}
    </h2>

    <p style="
    color:white;
    letter-spacing:2px;
    ">
    AMICOINS
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button(
        "Logout",
        key="logout_button"
    ):

        st.session_state.logged_in = False
        st.rerun()

# =====================================================
# PAGE TITLE
# =====================================================

st.markdown("""
<h1 class="main-title">
🏆 AMIVERSE Rewards Hub
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<p class="subtitle">
Gamified AI & Blockchain Student Reward Ecosystem
</p>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# =====================================================
# METRICS
# =====================================================

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.metric(
        "AMICOINS",
        f"{st.session_state.coins}"
    )

with col2:

    st.metric(
        "Badges",
        "6"
    )

with col3:

    st.metric(
        "Reward Rank",
        "#24"
    )

with col4:

    st.metric(
        "XP Level",
        "12"
    )

st.markdown("<br>", unsafe_allow_html=True)

# =====================================================
# BADGES SECTION
# =====================================================

st.markdown("""
<div class="card">

<h2 style="
color:white;
margin-bottom:20px;
">
🎖 Achievement Badges
</h2>

<p style="
color:#cbd5e1;
line-height:1.9;
font-size:16px;
">

Unlock badges by interacting with
AMIVERSE features and improving your career profile.

</p>

</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# =====================================================
# BADGE CARDS
# =====================================================

col1, col2 = st.columns(2)

for index, badge in enumerate(badges):

    card = f"""
    <div class="card">

    <h1 style="
    font-size:50px;
    margin-bottom:10px;
    ">
    {badge['icon']}
    </h1>

    <h2 style="
    color:white;
    margin-bottom:15px;
    ">
    {badge['title']}
    </h2>

    <p style="
    color:#cbd5e1;
    line-height:1.8;
    font-size:15px;
    ">

    {badge['description']}

    </p>

    <h3 style="
    color:#3b82f6;
    margin-top:20px;
    ">
    🪙 +{badge['coins']} AMICOINS
    </h3>

    </div>
    """

    if index % 2 == 0:

        with col1:
            st.markdown(
                card,
                unsafe_allow_html=True
            )

    else:

        with col2:
            st.markdown(
                card,
                unsafe_allow_html=True
            )

# =====================================================
# REWARD ANALYTICS
# =====================================================

st.markdown("<br>", unsafe_allow_html=True)

reward_data = pd.DataFrame({

    "Activity": [
        "Resume",
        "Certificates",
        "Prediction",
        "AI Usage",
        "Hackathons",
        "Internships"
    ],

    "Coins": [
        120,
        300,
        80,
        60,
        250,
        350
    ]
})

st.markdown("""
<div class="card">
<h2 style="
color:white;
margin-bottom:20px;
">
📈 Reward Analytics
</h2>
</div>
""", unsafe_allow_html=True)

fig = px.bar(

    reward_data,

    x="Activity",

    y="Coins",

    color="Activity",

    text="Coins",

    height=450
)

fig.update_layout(

    paper_bgcolor="#0f172a",

    plot_bgcolor="#0f172a",

    font_color="white"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# =====================================================
# LEADERBOARD
# =====================================================

st.markdown("<br>", unsafe_allow_html=True)

leaderboard = pd.DataFrame({

    "Student": [
        "Anshika",
        "Aryan",
        "Priya",
        "Rahul",
        "Aman"
    ],

    "AMICOINS": [
        4250,
        3980,
        3720,
        3400,
        3150
    ]
})

st.markdown("""
<div class="card">

<h2 style="
color:white;
margin-bottom:20px;
">
🏅 Top Student Leaderboard
</h2>

</div>
""", unsafe_allow_html=True)

st.dataframe(
    leaderboard,
    use_container_width=True
)

# =====================================================
# DAILY MISSIONS
# =====================================================

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div class="card">

<h2 style="
color:white;
margin-bottom:20px;
">
🎯 Daily Missions
</h2>

<p style="
color:#cbd5e1;
line-height:2;
font-size:16px;
">

✅ Upload Resume → +40 Coins  

✅ Verify Certificate → +75 Coins  

✅ Use AI Assistant → +10 Coins  

✅ Run Placement Prediction → +25 Coins  

✅ Daily Login Bonus → +20 Coins  

</p>

</div>
""", unsafe_allow_html=True)

# =====================================================
# ABOUT SECTION
# =====================================================

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div class="card">

<h2 style="
color:white;
margin-bottom:20px;
">
🌌 About Reward Ecosystem
</h2>

<p style="
color:#cbd5e1;
line-height:2;
font-size:16px;
">

The AMIVERSE Reward Ecosystem introduces
gamification into student learning and placement preparation.

Students earn AMICOINS and achievement badges
through productive academic and career activities.

The reward ecosystem encourages:

• Skill Development  

• Resume Building  

• Blockchain Verification  

• AI Engagement  

• Placement Preparation  

• Student Motivation  

This creates an engaging,
future-ready university ecosystem.

</p>

</div>
""", unsafe_allow_html=True)