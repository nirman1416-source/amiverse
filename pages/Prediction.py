import streamlit as st
import numpy as np
import joblib
import plotly.express as px
import pandas as pd

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="AMIVERSE Prediction",
    page_icon="📈",
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

    st.session_state.username = "asaini@gmail.com"

if "coins" not in st.session_state:

    st.session_state.coins = 1250

if "logged_in" not in st.session_state:

    st.session_state.logged_in = True

# =====================================================
# LOAD MODEL
# =====================================================

model = joblib.load(
    "models/Logistic Regression.pkl"
)

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
<h1 style="
font-size:70px;
font-weight:800;
margin-bottom:10px;
">
📈 Placement Prediction
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<p style="
color:#94a3b8;
font-size:20px;
margin-bottom:40px;
">
AI Powered Career Intelligence & Placement Analysis
</p>
""", unsafe_allow_html=True)

# =====================================================
# INPUT CARD
# =====================================================

st.markdown("""
<div class="card">

<h2 style="
color:white;
margin-bottom:15px;
">
🎯 Student Profile Analysis
</h2>

<p style="
color:#94a3b8;
font-size:16px;
line-height:1.8;
">

Enter your academic and communication details
to predict placement readiness using AMIVERSE AI.

</p>

</div>
""", unsafe_allow_html=True)

# =====================================================
# INPUTS
# =====================================================

col1, col2 = st.columns(2)

with col1:

    cgpa = st.slider(
        "CGPA",
        0.0,
        10.0,
        7.0
    )

    iq = st.slider(
        "IQ Score",
        50,
        150,
        100
    )

with col2:

    communication = st.slider(
        "Communication Skills",
        1,
        10,
        5
    )

    internship = st.selectbox(
        "Internship Experience",
        ["No", "Yes"]
    )

internship_value = (
    1 if internship == "Yes" else 0
)

st.markdown("<br>", unsafe_allow_html=True)

# =====================================================
# BUTTON
# =====================================================

predict = st.button(
    "Predict Placement Probability"
)

# =====================================================
# PREDICTION
# =====================================================

if predict:

    features = np.array([
        [
            cgpa,
            iq,
            communication,
            internship_value
        ]
    ])

    prediction = model.predict(features)

    probability = model.predict_proba(features)

    placement_probability = (
        probability[0][1] * 100
    )

    # =====================================================
    # COINS
    # =====================================================

    st.session_state.coins += 25

    st.markdown("<br>", unsafe_allow_html=True)

    # =====================================================
    # RESULT CARD
    # =====================================================

    st.markdown("""
    <div class="card">
    """, unsafe_allow_html=True)

    st.subheader("📌 AI Prediction Result")

    if prediction[0] == 1:

        st.success(
            f"✅ High Placement Probability ({placement_probability:.2f}%)"
        )

    else:

        st.error(
            f"❌ Low Placement Probability ({placement_probability:.2f}%)"
        )

    st.progress(
        int(placement_probability)
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # =====================================================
    # RADAR CHART
    # =====================================================

    chart_data = pd.DataFrame({

        "Skill": [
            "CGPA",
            "IQ",
            "Communication",
            "Internship"
        ],

        "Value": [
            cgpa * 10,
            iq / 1.5,
            communication * 10,
            internship_value * 100
        ]
    })

    fig = px.line_polar(
        chart_data,
        r="Value",
        theta="Skill",
        line_close=True
    )

    fig.update_layout(

        paper_bgcolor="#0f172a",

        font_color="white",

        height=450
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # =====================================================
    # RECOMMENDATIONS
    # =====================================================

    st.subheader("💡 Career Recommendations")

    if placement_probability >= 80:

        st.info("""
🚀 Excellent Profile

• Strong academics

• Excellent communication

• Great placement readiness

• Focus on advanced projects

• Apply for top internships

🪙 Reward Earned: +25 AMICOINS
""")

    elif placement_probability >= 60:

        st.warning("""
⚡ Good Profile

• Improve coding consistency

• Build practical projects

• Practice aptitude & DSA

• Participate in hackathons

🪙 Reward Earned: +25 AMICOINS
""")

    else:

        st.error("""
⚠️ Improvement Required

Focus on:

• Technical skills

• Real-world projects

• Communication skills

• Internship experience

• Coding practice

🪙 Reward Earned: +25 AMICOINS
""")

    st.markdown("</div>", unsafe_allow_html=True)

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
📘 About AMIVERSE AI
</h2>

<p style="
color:#cbd5e1;
line-height:2;
font-size:16px;
">

AMIVERSE is an AI-powered student ecosystem
built for placements, resume intelligence,
blockchain certificate verification,
and student rewards.

The platform uses Machine Learning to analyze:

• Academic Performance

• Communication Skills

• Internship Experience

• Placement Readiness

Students also earn AMICOINS
for interacting with the platform,
verifying certificates,
and improving profiles.

</p>

</div>
""", unsafe_allow_html=True)