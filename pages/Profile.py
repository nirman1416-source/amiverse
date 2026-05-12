import streamlit as st
import pandas as pd
import plotly.express as px

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="AMIVERSE Profile",
    page_icon="👤",
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
👤 Student Profile
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<p class="subtitle">
AI Powered Academic & Career Identity
</p>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# =====================================================
# PROFILE HEADER
# =====================================================

col1, col2 = st.columns([1, 3])

with col1:

    st.markdown("""
    <div class="card" style="
    text-align:center;
    padding-top:45px;
    padding-bottom:45px;
    ">

    <h1 style="
    font-size:90px;
    ">
    👩‍🎓
    </h1>

    </div>
    """, unsafe_allow_html=True)

with col2:

    st.markdown(f"""
    <div class="card">

    <h1 style="
    color:white;
    margin-bottom:15px;
    ">
    {st.session_state.username}
    </h1>

    <p style="
    color:#94a3b8;
    font-size:18px;
    line-height:2;
    ">

    🎓 B.Tech Computer Science Engineering  

    🏫 Amity University Mumbai  

    🚀 AI & Blockchain Enthusiast  

    📈 Placement Ready Student  

    🔗 Blockchain Verified Profile  

    </p>

    </div>
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
        "Resume Score",
        "88%"
    )

with col3:

    st.metric(
        "Placement Readiness",
        "91%"
    )

with col4:

    st.metric(
        "Certificates",
        len(st.session_state.verified_certificates)
    )

st.markdown("<br>", unsafe_allow_html=True)

# =====================================================
# SKILLS
# =====================================================

skills = [

    "Python",
    "Machine Learning",
    "SQL",
    "Blockchain",
    "Web Development",
    "AI",
    "Communication",
    "Leadership"
]

st.markdown("""
<div class="card">

<h2 style="
color:white;
margin-bottom:20px;
">
🛠 Skills & Technologies
</h2>

</div>
""", unsafe_allow_html=True)

cols = st.columns(4)

for index, skill in enumerate(skills):

    cols[index % 4].success(skill)

st.markdown("<br>", unsafe_allow_html=True)

# =====================================================
# SKILL ANALYTICS
# =====================================================

skill_data = pd.DataFrame({

    "Skill": skills,

    "Score": [
        90,
        85,
        80,
        75,
        88,
        84,
        92,
        86
    ]
})

st.markdown("""
<div class="card">
<h2 style="
color:white;
margin-bottom:20px;
">
📊 Skill Analytics
</h2>
</div>
""", unsafe_allow_html=True)

fig = px.bar(

    skill_data,

    x="Skill",

    y="Score",

    color="Skill",

    text="Score",

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

st.markdown("<br>", unsafe_allow_html=True)

# =====================================================
# ACHIEVEMENTS
# =====================================================

st.markdown("""
<div class="card">

<h2 style="
color:white;
margin-bottom:20px;
">
🏆 Achievements & Badges
</h2>

<p style="
color:#cbd5e1;
line-height:2;
font-size:16px;
">

🏅 Resume Expert  

🔗 Blockchain Verified  

🚀 Placement Ready  

🤖 AI Explorer  

💼 Internship Star  

🏆 Hackathon Participant  

</p>

</div>
""", unsafe_allow_html=True)

# =====================================================
# CAREER ROADMAP
# =====================================================

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div class="card">

<h2 style="
color:white;
margin-bottom:20px;
">
🧠 AI Career Roadmap
</h2>

<p style="
color:#cbd5e1;
line-height:2;
font-size:16px;
">

Recommended Next Steps:

• Learn Advanced Machine Learning  

• Build Full Stack Projects  

• Improve Blockchain Development Skills  

• Participate in Hackathons  

• Apply for AI/ML Internships  

• Strengthen DSA & Problem Solving  

• Build Open Source Contributions  

</p>

</div>
""", unsafe_allow_html=True)

# =====================================================
# VERIFIED CERTIFICATES
# =====================================================

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div class="card">

<h2 style="
color:white;
margin-bottom:20px;
">
🔐 Verified Certificates
</h2>

<p style="
color:#94a3b8;
font-size:16px;
margin-bottom:25px;
">

Blockchain verified certificates
uploaded by this student.

</p>

</div>
""", unsafe_allow_html=True)

# =====================================================
# CERTIFICATE DISPLAY
# =====================================================

if "verified_certificates" not in st.session_state:

    st.session_state.verified_certificates = []

# =====================================================
# SHOW CERTIFICATES
# =====================================================

if len(st.session_state.verified_certificates) > 0:

    for cert in st.session_state.verified_certificates:

        st.markdown(f"""
        <div class="card" style="
        padding:20px;
        ">

        <h3 style="
        color:white;
        margin-bottom:12px;
        ">
        📜 {cert}
        </h3>

        <p style="
        color:#22c55e;
        font-size:15px;
        font-weight:600;
        ">
        ✅ Blockchain Verified
        </p>

        <p style="
        color:#94a3b8;
        font-size:14px;
        margin-top:10px;
        ">
        Uploaded By:
        {st.session_state.username}
        </p>

        </div>
        """, unsafe_allow_html=True)

else:

    st.warning(
        "No verified certificates uploaded yet."
    )

# =====================================================
# ABOUT PROFILE SYSTEM
# =====================================================

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div class="card">

<h2 style="
color:white;
margin-bottom:20px;
">
🌌 About Student Identity System
</h2>

<p style="
color:#cbd5e1;
line-height:2;
font-size:16px;
">

The AMIVERSE Student Identity System
creates a unified AI-powered academic profile
for students using blockchain verification and analytics.

Features include:

• Placement Readiness  

• Resume Intelligence  

• Blockchain Verification  

• Skill Analytics  

• AI Career Guidance  

• Reward Ecosystem  

This creates a future-ready digital identity
for students and recruiters.

</p>

</div>
""", unsafe_allow_html=True)