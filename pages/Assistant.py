import streamlit as st

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="AMIVERSE Assistant",
    page_icon="🤖",
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
🤖 AMIVERSE AI Assistant
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<p class="subtitle">
AI Powered Career Guidance & Student Support
</p>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# =====================================================
# AI INPUT CARD
# =====================================================

st.markdown("""
<div class="card">

<h2 style="
color:white;
margin-bottom:15px;
">
💬 Ask AMIVERSE AI
</h2>

<p style="
color:#94a3b8;
font-size:16px;
line-height:1.8;
">

Get smart AI-powered recommendations for:

• Placements  
• Resume Building  
• Interviews  
• Skills  
• Machine Learning  
• Projects  
• Career Growth  

</p>

</div>
""", unsafe_allow_html=True)

question = st.text_input(
    "",
    placeholder="Ask anything about placements, resumes, interviews, skills..."
)

st.markdown("<br>", unsafe_allow_html=True)

# =====================================================
# AI RESPONSE
# =====================================================

if question:

    question = question.lower()

    st.markdown("""
    <div class="card">
    """, unsafe_allow_html=True)

    st.subheader("📌 AMIVERSE AI Response")

    # =====================================================
    # PLACEMENT
    # =====================================================

    if "placement" in question:

        st.success("""
🎯 Placement Improvement Strategy

• Practice DSA consistently

• Improve communication skills

• Build strong real-world projects

• Participate in hackathons

• Add internships and certifications

• Improve aptitude and problem-solving

🪙 Reward:
+20 AMICOINS for career activity
""")

    # =====================================================
    # RESUME
    # =====================================================

    elif "resume" in question:

        st.success("""
📄 Resume Improvement Tips

• Add technical projects

• Mention internships clearly

• Keep resume ATS-friendly

• Add GitHub & LinkedIn links

• Highlight achievements

• Keep formatting clean and modern

🪙 Reward:
+15 AMICOINS for resume activity
""")

    # =====================================================
    # SKILLS
    # =====================================================

    elif "skills" in question:

        st.success("""
🚀 Recommended Skills

• Python

• SQL

• Machine Learning

• Web Development

• Data Structures & Algorithms

• Blockchain Basics

• Communication Skills

• Cloud Computing

🪙 Reward:
+10 AMICOINS for skill exploration
""")

    # =====================================================
    # INTERVIEW
    # =====================================================

    elif "interview" in question:

        st.success("""
🎤 Interview Preparation Roadmap

• Practice coding rounds daily

• Revise DBMS, OS, CN, OOPs

• Solve aptitude questions

• Prepare HR interview answers

• Give mock interviews

• Improve confidence and speaking

🪙 Reward:
+20 AMICOINS for interview preparation
""")

    # =====================================================
    # MACHINE LEARNING
    # =====================================================

    elif "machine learning" in question:

        st.success("""
🧠 Machine Learning Roadmap

1. Python Fundamentals

2. NumPy & Pandas

3. Data Visualization

4. Scikit-learn

5. Deep Learning Basics

6. Build Real-World Projects

7. Learn Deployment

🪙 Reward:
+25 AMICOINS for AI learning
""")

    # =====================================================
    # BLOCKCHAIN
    # =====================================================

    elif "blockchain" in question:

        st.success("""
🔗 Blockchain Learning Path

• Learn blockchain basics

• Understand hashing

• Learn smart contracts

• Explore Ethereum & Solidity

• Build certificate verification systems

• Learn Web3 wallets

🪙 Reward:
+30 AMICOINS for Web3 learning
""")

    # =====================================================
    # PROJECTS
    # =====================================================

    elif "project" in question:

        st.success("""
💻 Best Projects for Placements

• AMIVERSE Ecosystem

• Blockchain Verification System

• AI Resume Analyzer

• Placement Prediction Platform

• Chatbot Application

• Portfolio Website

• Face Recognition Attendance System

🪙 Reward:
+15 AMICOINS for project activity
""")

    # =====================================================
    # DEFAULT
    # =====================================================

    else:

        st.success("""
🌌 AMIVERSE AI Recommendation

Continue improving your:

• Technical Skills  
• Communication Skills  
• Projects  
• Resume Quality  
• Coding Practice  

Stay consistent and keep learning.

🪙 Reward:
+5 AMICOINS for AI interaction
""")

    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# =====================================================
# AI FEATURES
# =====================================================

col1, col2 = st.columns(2)

with col1:

    st.markdown("""
    <div class="card">

    <h2 style="
    color:white;
    margin-bottom:20px;
    ">
    🤖 AI Features
    </h2>

    <p style="
    color:#cbd5e1;
    line-height:2;
    font-size:16px;
    ">

    • Smart Career Guidance  

    • AI Skill Recommendations  

    • Resume Improvement Suggestions  

    • Interview Preparation  

    • Placement Readiness Analysis  

    • Blockchain Career Insights  

    </p>

    </div>
    """, unsafe_allow_html=True)

with col2:

    st.markdown("""
    <div class="card">

    <h2 style="
    color:white;
    margin-bottom:20px;
    ">
    💡 Suggested Questions
    </h2>

    <p style="
    color:#cbd5e1;
    line-height:2;
    font-size:16px;
    ">

    • How can I improve placements?  

    • What skills should I learn?  

    • How to improve my resume?  

    • How to prepare for interviews?  

    • How to start Machine Learning?  

    • Explain blockchain basics  

    • Best projects for placements?  

    </p>

    </div>
    """, unsafe_allow_html=True)