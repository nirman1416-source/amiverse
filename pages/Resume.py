import streamlit as st
from PyPDF2 import PdfReader
import plotly.express as px
import pandas as pd

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="AMIVERSE Resume Analyzer",
    page_icon="📄",
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
📄 Resume Intelligence Engine
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<p class="subtitle">
AI Powered Resume Analysis & Career Intelligence
</p>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# =====================================================
# UPLOAD CARD
# =====================================================

st.markdown("""
<div class="card">

<h2 style="
color:white;
margin-bottom:15px;
">
📤 Upload Resume
</h2>

<p style="
color:#94a3b8;
font-size:16px;
line-height:1.8;
">

Upload your resume PDF to get:

• AI Resume Analysis  
• ATS Score  
• Skill Detection  
• Placement Readiness  
• Career Recommendations  
• AMICOINS Rewards  

</p>

</div>
""", unsafe_allow_html=True)

uploaded_file = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)

# =====================================================
# RESUME ANALYSIS
# =====================================================

if uploaded_file is not None:

    st.success(
        "✅ Resume Uploaded Successfully"
    )

    # =====================================================
    # REWARD SYSTEM
    # =====================================================

    st.session_state.coins += 40

    # =====================================================
    # READ PDF
    # =====================================================

    pdf_reader = PdfReader(
        uploaded_file
    )

    text = ""

    for page in pdf_reader.pages:

        extracted = page.extract_text()

        if extracted:

            text += extracted

    st.markdown("<br>", unsafe_allow_html=True)

    # =====================================================
    # EXTRACTED TEXT
    # =====================================================

    st.markdown("""
    <div class="card">
    """, unsafe_allow_html=True)

    st.subheader("📌 Extracted Resume Content")

    st.text_area(
        "",
        text,
        height=250
    )

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # =====================================================
    # SKILL DETECTION
    # =====================================================

    skill_keywords = [

        "Python",
        "Machine Learning",
        "SQL",
        "Java",
        "C++",
        "HTML",
        "CSS",
        "JavaScript",
        "Leadership",
        "Communication",
        "Data Science",
        "AI",
        "Deep Learning",
        "Problem Solving",
        "Teamwork",
        "React",
        "Node.js",
        "Blockchain",
        "Cloud",
        "AWS",
        "Cybersecurity",
        "GitHub"
    ]

    skills = []

    for skill in skill_keywords:

        if skill.lower() in text.lower():

            skills.append(skill)

    # =====================================================
    # SKILLS CARD
    # =====================================================

    st.markdown("""
    <div class="card">
    """, unsafe_allow_html=True)

    st.subheader("🛠 Detected Skills")

    if skills:

        cols = st.columns(3)

        for index, skill in enumerate(skills):

            cols[index % 3].success(skill)

    else:

        st.warning(
            "No matching skills detected."
        )

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # =====================================================
    # SCORE CALCULATION
    # =====================================================

    score = len(skills) * 6

    if score > 100:
        score = 100

    # =====================================================
    # SCORE CARD
    # =====================================================

    st.markdown("""
    <div class="card">
    """, unsafe_allow_html=True)

    st.subheader("📊 Resume ATS Score")

    st.progress(score)

    st.markdown(
        f"""
        <h1 style="
        color:#3b82f6;
        font-size:50px;
        font-weight:800;
        ">
        {score}%
        </h1>
        """,
        unsafe_allow_html=True
    )

    # SCORE STATUS

    if score >= 80:

        st.success(
            "🚀 Excellent Resume Profile"
        )

    elif score >= 60:

        st.warning(
            "⚡ Good Resume — Add More Projects & Skills"
        )

    else:

        st.error(
            "⚠️ Resume Needs Improvement"
        )

    st.info("""
🪙 Reward Earned:
+40 AMICOINS
""")

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # =====================================================
    # SKILL CHART
    # =====================================================

    skill_chart = pd.DataFrame({

        "Skills": skills,
        "Value": [10] * len(skills)
    })

    if len(skills) > 0:

        fig = px.bar(

            skill_chart,

            x="Skills",

            y="Value",

            color="Skills",

            height=420
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
    # RECOMMENDATIONS
    # =====================================================

    recommendations = []

    if "Python" not in skills:
        recommendations.append(
            "Add Python skills"
        )

    if "Machine Learning" not in skills:
        recommendations.append(
            "Add Machine Learning projects"
        )

    if "SQL" not in skills:
        recommendations.append(
            "Learn SQL"
        )

    if "Leadership" not in skills:
        recommendations.append(
            "Add leadership activities"
        )

    if "Communication" not in skills:
        recommendations.append(
            "Improve communication skills"
        )

    if "GitHub" not in skills:
        recommendations.append(
            "Add GitHub profile"
        )

    if "Blockchain" not in skills:
        recommendations.append(
            "Learn Blockchain fundamentals"
        )

    # =====================================================
    # RECOMMENDATION CARD
    # =====================================================

    st.markdown("""
    <div class="card">
    """, unsafe_allow_html=True)

    st.subheader("💡 AI Recommendations")

    if len(recommendations) == 0:

        st.success(
            "Your resume is highly placement-ready 🚀"
        )

    else:

        for rec in recommendations:

            st.warning(rec)

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
📘 About Resume Intelligence Engine
</h2>

<p style="
color:#cbd5e1;
line-height:2;
font-size:16px;
">

The AMIVERSE Resume Intelligence Engine uses AI
to analyze resumes and evaluate placement readiness.

The system performs:

• ATS Resume Analysis  

• Skill Detection  

• Technical Keyword Analysis  

• Resume Scoring  

• Career Recommendations  

• Placement Readiness Evaluation  

Students also earn AMICOINS rewards
for improving resumes and interacting with the platform.

</p>

</div>
""", unsafe_allow_html=True)