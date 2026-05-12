import streamlit as st
import pandas as pd
import plotly.express as px
import random

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="AMIVERSE Wallet",
    page_icon="🪙",
    layout="wide",
    initial_sidebar_state="expanded"
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

if "verified_certificates" not in st.session_state:

    st.session_state.verified_certificates = []

if "transactions" not in st.session_state:

    st.session_state.transactions = [

        {
            "activity": "Resume Upload",
            "coins": 40
        },

        {
            "activity": "Prediction Analysis",
            "coins": 25
        },

        {
            "activity": "Blockchain Certificate",
            "coins": 75
        },

        {
            "activity": "AI Assistant Usage",
            "coins": 10
        }
    ]

# =====================================================
# SIDEBAR
# =====================================================

with st.sidebar:

    st.markdown("""
    <div class="sidebar-logo">

    <img src="https://cdn-icons-png.flaticon.com/512/3135/3135715.png"
    width="90">

    <h1 class="sidebar-title">
    AMIVERSE
    </h1>

    <p style="
    color:#94a3b8;
    font-size:14px;
    margin-top:-5px;
    ">
    Student AI Ecosystem
    </p>

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

    # =====================================================
    # USER CARD
    # =====================================================

    st.markdown(f"""
    <div class="sidebar-card">

    <h3 style="
    text-align:center;
    margin-bottom:10px;
    ">
    👤 {st.session_state.username}
    </h3>

    <p class="sidebar-email">
    Logged into AMIVERSE
    </p>

    <br>

    <h1 style="
    color:#3b82f6;
    text-align:center;
    ">
    🪙 {st.session_state.coins}
    </h1>

    <p style="
    text-align:center;
    color:#94a3b8;
    ">
    AMICOINS
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button(
        "Logout",
        key="wallet_logout"
    ):

        st.session_state.logged_in = False
        st.rerun()

# =====================================================
# PAGE TITLE
# =====================================================

st.markdown("""
<h1 class="main-title">
🪙 AMICOINS Wallet
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<p class="subtitle">
Blockchain Powered Student Reward Ecosystem
</p>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# =====================================================
# WALLET METRICS
# =====================================================

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.metric(
        "Wallet Balance",
        f"{st.session_state.coins}"
    )

with col2:

    st.metric(
        "Certificates",
        len(st.session_state.verified_certificates)
    )

with col3:

    wallet_rank = max(
        1,
        100 - int(st.session_state.coins / 50)
    )

    st.metric(
        "Reward Rank",
        f"#{wallet_rank}"
    )

with col4:

    st.metric(
        "Transactions",
        len(st.session_state.transactions)
    )

st.markdown("<br>", unsafe_allow_html=True)

# =====================================================
# MAIN WALLET CARD
# =====================================================

st.markdown(f"""
<div class="card">

<h2 style="
color:white;
margin-bottom:20px;
">
💳 Student Wallet
</h2>

<h1 style="
font-size:70px;
font-weight:800;
color:#3b82f6;
margin-bottom:10px;
">
🪙 {st.session_state.coins}
</h1>

<p style="
color:#94a3b8;
font-size:18px;
">
Current AMICOINS Balance
</p>

</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# =====================================================
# TRANSACTION DATAFRAME
# =====================================================

transaction_df = pd.DataFrame(
    st.session_state.transactions
)

# =====================================================
# CHARTS
# =====================================================

col1, col2 = st.columns(2)

# =====================================================
# BAR CHART
# =====================================================

with col1:

    st.markdown("""
    <div class="card">
    <h3 style="color:white;">
    📈 Reward Activity
    </h3>
    </div>
    """, unsafe_allow_html=True)

    fig1 = px.bar(

        transaction_df,

        x="activity",

        y="coins",

        color="activity",

        text="coins",

        height=420
    )

    fig1.update_layout(

        paper_bgcolor="#0f172a",

        plot_bgcolor="#0f172a",

        font_color="white"
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

# =====================================================
# PIE CHART
# =====================================================

with col2:

    st.markdown("""
    <div class="card">
    <h3 style="color:white;">
    🪙 Reward Distribution
    </h3>
    </div>
    """, unsafe_allow_html=True)

    fig2 = px.pie(

        transaction_df,

        names="activity",

        values="coins",

        hole=0.55,

        height=420
    )

    fig2.update_layout(

        paper_bgcolor="#0f172a",

        font_color="white"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

# =====================================================
# TRANSACTION HISTORY
# =====================================================

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div class="card">

<h2 style="
color:white;
margin-bottom:20px;
">
📜 Transaction History
</h2>

</div>
""", unsafe_allow_html=True)

for transaction in reversed(
    st.session_state.transactions
):

    activity = transaction["activity"]

    coins = transaction["coins"]

    st.markdown(f"""
    <div class="card" style="
    padding:18px;
    ">

    <h3 style="
    color:white;
    margin-bottom:10px;
    ">
    {activity}
    </h3>

    <p style="
    color:#3b82f6;
    font-size:22px;
    font-weight:700;
    ">
    +{coins} AMICOINS
    </p>

    </div>
    """, unsafe_allow_html=True)

# =====================================================
# DAILY BONUS
# =====================================================

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div class="card">

<h2 style="
color:white;
margin-bottom:20px;
">
🎁 Daily Reward
</h2>

<p style="
color:#cbd5e1;
font-size:16px;
line-height:1.8;
">

Claim daily AMICOINS rewards
for staying active on AMIVERSE.

</p>

</div>
""", unsafe_allow_html=True)

if st.button(
    "Claim Daily Reward",
    key="daily_reward"
):

    reward = random.randint(
        20,
        80
    )

    st.session_state.coins += reward

    st.session_state.transactions.append({

        "activity":
        "Daily Reward",

        "coins":
        reward
    })

    st.success(
        f"🎉 You earned {reward} AMICOINS"
    )

    st.rerun()

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
📜 Verified Certificates
</h2>

</div>
""", unsafe_allow_html=True)

if len(st.session_state.verified_certificates) > 0:

    for cert in st.session_state.verified_certificates:

        st.success(
            cert
        )

else:

    st.warning(
        "No verified certificates yet"
    )

# =====================================================
# WALLET LEVEL
# =====================================================

st.markdown("<br>", unsafe_allow_html=True)

wallet_level = int(
    st.session_state.coins / 250
)

st.markdown(f"""
<div class="card">

<h2 style="
color:white;
margin-bottom:20px;
">
🚀 Wallet Level
</h2>

<h1 style="
color:#3b82f6;
font-size:55px;
">
LEVEL {wallet_level}
</h1>

<p style="
color:#cbd5e1;
font-size:16px;
">

Earn more AMICOINS
to unlock higher levels and rewards.

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
🌌 About AMICOINS
</h2>

<p style="
color:#cbd5e1;
line-height:2;
font-size:16px;
">

AMICOINS is the digital reward currency
of the AMIVERSE ecosystem.

Students earn AMICOINS for:

• Uploading Resumes  

• Blockchain Certificate Verification  

• AI Interactions  

• Placement Activities  

• Hackathons & Internships  

• Daily Platform Usage  

The wallet system promotes
student engagement, learning,
and career growth through gamification.

</p>

</div>
""", unsafe_allow_html=True)