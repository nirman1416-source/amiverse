import streamlit as st
import pandas as pd
import plotly.express as px

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="AMIVERSE Leaderboard",
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

if "username" not in st.session_state:
    st.session_state.username = "Student User"

# =====================================================
# LEADERBOARD DATA
# =====================================================

leaderboard_data = pd.DataFrame({

    "Rank": [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8
    ],

    "Student": [
        "Anshika Saini",
        "Aryan Sharma",
        "Priya Patel",
        "Rahul Verma",
        "Aman Singh",
        "Sneha Kapoor",
        "Rohit Mehta",
        "Neha Jain"
    ],

    "AMICOINS": [
        4250,
        3980,
        3820,
        3600,
        3450,
        3320,
        3100,
        2980
    ],

    "Level": [
        22,
        20,
        19,
        18,
        17,
        16,
        15,
        14
    ]
})

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
🏆 AMIVERSE Leaderboard
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<p class="subtitle">
AI Powered Student Ranking & Achievement System
</p>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# =====================================================
# METRICS
# =====================================================

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.metric(
        "Total Students",
        "500+"
    )

with col2:

    st.metric(
        "Highest Coins",
        "4250"
    )

with col3:

    st.metric(
        "Top Rank",
        "#1"
    )

with col4:

    st.metric(
        "Leaderboard XP",
        "22"
    )

st.markdown("<br>", unsafe_allow_html=True)

# =====================================================
# TOP 3 STUDENTS
# =====================================================

st.markdown("""
<div class="card">

<h2 style="
color:white;
margin-bottom:25px;
">
🥇 Top Performers
</h2>

</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

# =====================================================
# RANK 1
# =====================================================

with col1:

    st.markdown("""
    <div class="card" style="
    text-align:center;
    ">

    <h1 style="
    font-size:70px;
    ">
    🥇
    </h1>

    <h2 style="
    color:white;
    ">
    Anshika Saini
    </h2>

    <h3 style="
    color:#3b82f6;
    ">
    🪙 4250 AMICOINS
    </h3>

    <p style="
    color:#cbd5e1;
    ">
    Level 22
    </p>

    </div>
    """, unsafe_allow_html=True)

# =====================================================
# RANK 2
# =====================================================

with col2:

    st.markdown("""
    <div class="card" style="
    text-align:center;
    ">

    <h1 style="
    font-size:70px;
    ">
    🥈
    </h1>

    <h2 style="
    color:white;
    ">
    Aryan Sharma
    </h2>

    <h3 style="
    color:#3b82f6;
    ">
    🪙 3980 AMICOINS
    </h3>

    <p style="
    color:#cbd5e1;
    ">
    Level 20
    </p>

    </div>
    """, unsafe_allow_html=True)

# =====================================================
# RANK 3
# =====================================================

with col3:

    st.markdown("""
    <div class="card" style="
    text-align:center;
    ">

    <h1 style="
    font-size:70px;
    ">
    🥉
    </h1>

    <h2 style="
    color:white;
    ">
    Priya Patel
    </h2>

    <h3 style="
    color:#3b82f6;
    ">
    🪙 3820 AMICOINS
    </h3>

    <p style="
    color:#cbd5e1;
    ">
    Level 19
    </p>

    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# =====================================================
# LEADERBOARD TABLE
# =====================================================

st.markdown("""
<div class="card">

<h2 style="
color:white;
margin-bottom:20px;
">
📊 Global Student Rankings
</h2>

</div>
""", unsafe_allow_html=True)

st.dataframe(
    leaderboard_data,
    use_container_width=True
)

st.markdown("<br>", unsafe_allow_html=True)

# =====================================================
# ANALYTICS CHART
# =====================================================

st.markdown("""
<div class="card">
<h2 style="
color:white;
margin-bottom:20px;
">
📈 Student Reward Analytics
</h2>
</div>
""", unsafe_allow_html=True)

fig = px.bar(

    leaderboard_data,

    x="Student",

    y="AMICOINS",

    color="Student",

    text="AMICOINS",

    height=500
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

st.markdown("<br>", unsafe_allow_html=True)

# =====================================================
# RANKING FACTORS
# =====================================================

st.markdown("""
<div class="card">

<h2 style="
color:white;
margin-bottom:20px;
">
🎯 Ranking Factors
</h2>

<p style="
color:#cbd5e1;
line-height:2;
font-size:16px;
">

Students earn ranking points through:

• Resume Uploads  

• Blockchain Certificate Verification  

• Placement Prediction Activities  

• AI Assistant Usage  

• Hackathons & Internships  

• Daily Engagement  

• Skill Development  

• Academic Achievements  

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
🌌 About AMIVERSE Rankings
</h2>

<p style="
color:#cbd5e1;
line-height:2;
font-size:16px;
">

The AMIVERSE Leaderboard System
gamifies placement preparation and skill development.

Students are ranked based on:

• AMICOINS Rewards  

• Verified Skills  

• Academic Activities  

• AI Engagement  

• Blockchain Certifications  

• Placement Readiness  

The system motivates students
through healthy competition and recognition.

</p>

</div>
""", unsafe_allow_html=True)