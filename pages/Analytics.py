import streamlit as st
import pandas as pd
import plotly.express as px

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="AMIVERSE Analytics",
    page_icon="📊",
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
📊 AMIVERSE Analytics
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<p class="subtitle">
AI Powered Placement & Blockchain Analytics
</p>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# =====================================================
# METRICS
# =====================================================

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.metric(
        "Students",
        "500+"
    )

with col2:

    st.metric(
        "Placement Rate",
        "92%"
    )

with col3:

    st.metric(
        "Certificates",
        "1200+"
    )

with col4:

    st.metric(
        "AMICOINS",
        "50K+"
    )

st.markdown("<br>", unsafe_allow_html=True)

# =====================================================
# DATA
# =====================================================

accuracy_data = pd.DataFrame({

    "Algorithm": [
        "Logistic Regression",
        "KNN",
        "SVM",
        "Decision Tree",
        "Naive Bayes"
    ],

    "Accuracy": [
        98,
        95,
        97,
        92,
        90
    ]
})

placement_data = pd.DataFrame({

    "Category": [
        "Placed",
        "Not Placed"
    ],

    "Students": [
        460,
        40
    ]
})

trend_data = pd.DataFrame({

    "Year": [
        2021,
        2022,
        2023,
        2024,
        2025
    ],

    "Placement Rate": [
        75,
        80,
        85,
        90,
        92
    ]
})

coin_data = pd.DataFrame({

    "Activity": [
        "Certificates",
        "Resume Upload",
        "AI Usage",
        "Hackathons",
        "Internships"
    ],

    "Coins": [
        250,
        120,
        80,
        300,
        450
    ]
})

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
    📈 ML Algorithm Accuracy
    </h3>
    </div>
    """, unsafe_allow_html=True)

    fig1 = px.bar(

        accuracy_data,

        x="Algorithm",

        y="Accuracy",

        color="Algorithm",

        text="Accuracy",

        height=400
    )

    fig1.update_layout(

        paper_bgcolor="#0f172a",

        plot_bgcolor="#0f172a",

        font_color="white",

        margin=dict(
            l=20,
            r=20,
            t=30,
            b=20
        )
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
    🎯 Placement Ratio
    </h3>
    </div>
    """, unsafe_allow_html=True)

    fig2 = px.pie(

        placement_data,

        names="Category",

        values="Students",

        hole=0.55,

        height=400
    )

    fig2.update_layout(

        paper_bgcolor="#0f172a",

        font_color="white",

        margin=dict(
            l=20,
            r=20,
            t=30,
            b=20
        )
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

st.markdown("<br>", unsafe_allow_html=True)

# =====================================================
# LINE CHART
# =====================================================

st.markdown("""
<div class="card">
<h3 style="color:white;">
📉 Placement Growth Trend
</h3>
</div>
""", unsafe_allow_html=True)

fig3 = px.line(

    trend_data,

    x="Year",

    y="Placement Rate",

    markers=True,

    height=420
)

fig3.update_layout(

    paper_bgcolor="#0f172a",

    plot_bgcolor="#0f172a",

    font_color="white",

    margin=dict(
        l=20,
        r=20,
        t=30,
        b=20
    )
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

st.markdown("<br>", unsafe_allow_html=True)

# =====================================================
# AMICOINS CHART
# =====================================================

st.markdown("""
<div class="card">
<h3 style="color:white;">
🪙 AMICOINS Reward Analytics
</h3>
</div>
""", unsafe_allow_html=True)

fig4 = px.bar(

    coin_data,

    x="Activity",

    y="Coins",

    color="Activity",

    text="Coins",

    height=420
)

fig4.update_layout(

    paper_bgcolor="#0f172a",

    plot_bgcolor="#0f172a",

    font_color="white",

    margin=dict(
        l=20,
        r=20,
        t=30,
        b=20
    )
)

st.plotly_chart(
    fig4,
    use_container_width=True
)

st.markdown("<br>", unsafe_allow_html=True)

# =====================================================
# INSIGHTS
# =====================================================

st.markdown("""
<div class="card">

<h2 style="
color:white;
margin-bottom:20px;
">
📌 AI Insights
</h2>

<p style="
color:#cbd5e1;
line-height:2;
font-size:16px;
">

• Logistic Regression gives highest prediction accuracy.

• Placement growth continuously increases every year.

• More than 90% students are placed successfully.

• Blockchain verification improves certificate trust.

• AMICOINS reward system boosts student engagement.

• AI analytics improves career guidance and predictions.

</p>

</div>
""", unsafe_allow_html=True)