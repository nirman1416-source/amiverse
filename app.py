import streamlit as st
import sqlite3
import bcrypt

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="AMIVERSE",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================
# DATABASE
# =====================================================

conn = sqlite3.connect(
    "database.db",
    check_same_thread=False
)

cursor = conn.cursor()

# =====================================================
# SESSION STATE
# =====================================================

if "logged_in" not in st.session_state:

    st.session_state.logged_in = False

if "coins" not in st.session_state:

    st.session_state.coins = 1250

if "username" not in st.session_state:

    st.session_state.username = "student@amity.edu"

if "verified_certificates" not in st.session_state:

    st.session_state.verified_certificates = []

if "transactions" not in st.session_state:

    st.session_state.transactions = []

# =====================================================
# LOAD CSS
# =====================================================

with open("assets/style.css") as f:

    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# =====================================================
# LOGIN / SIGNUP
# =====================================================

if st.session_state.logged_in == False:

    st.markdown("""
    <style>

    [data-testid="stSidebar"] {
        display:none;
    }

    </style>
    """, unsafe_allow_html=True)

    left, center, right = st.columns([1, 1.4, 1])

    with center:

        st.markdown("<br><br><br>", unsafe_allow_html=True)

        st.markdown("""
        <h1 style="
        text-align:center;
        color:white;
        font-size:72px;
        font-weight:800;
        letter-spacing:2px;
        ">
        🌌 AMIVERSE
        </h1>
        """, unsafe_allow_html=True)

        st.markdown("""
        <p style="
        text-align:center;
        color:#94a3b8;
        font-size:20px;
        margin-bottom:45px;
        ">
        AI & Blockchain Powered Student Ecosystem
        </p>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="card">
        """, unsafe_allow_html=True)

        option = st.selectbox(
            "Select Option",
            ["Login", "Signup"]
        )

        st.markdown("<br>", unsafe_allow_html=True)

        # =====================================================
        # LOGIN
        # =====================================================

        if option == "Login":

            st.subheader("Welcome Back")

            email = st.text_input(
                "Email Address"
            )

            password = st.text_input(
                "Password",
                type="password"
            )

            st.markdown("<br>", unsafe_allow_html=True)

            if st.button(
                "Login",
                key="login_button"
            ):

                cursor.execute(
                    "SELECT * FROM users WHERE email=?",
                    (email,)
                )

                user = cursor.fetchone()

                if user:

                    stored_password = user[3]

                    if bcrypt.checkpw(
                        password.encode(),
                        stored_password
                    ):

                        st.session_state.logged_in = True

                        st.session_state.username = user[1]

                        st.success(
                            "Login Successful"
                        )

                        st.rerun()

                    else:

                        st.error(
                            "Incorrect Password"
                        )

                else:

                    st.error(
                        "User not found"
                    )

        # =====================================================
        # SIGNUP
        # =====================================================

        else:

            st.subheader("Create Account")

            username = st.text_input(
                "Username"
            )

            email = st.text_input(
                "Email Address"
            )

            password = st.text_input(
                "Password",
                type="password"
            )

            st.markdown("<br>", unsafe_allow_html=True)

            if st.button(
                "Create Account",
                key="signup_button"
            ):

                hashed_password = bcrypt.hashpw(
                    password.encode(),
                    bcrypt.gensalt()
                )

                try:

                    cursor.execute(
                        """
                        INSERT INTO users
                        (username,email,password)

                        VALUES (?,?,?)
                        """,
                        (
                            username,
                            email,
                            hashed_password
                        )
                    )

                    conn.commit()

                    st.success(
                        "Account Created Successfully"
                    )

                except:

                    st.error(
                        "Email already exists"
                    )

        st.markdown("</div>", unsafe_allow_html=True)

# =====================================================
# MAIN DASHBOARD
# =====================================================

else:

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

        # =====================================================
        # NAVIGATION
        # =====================================================

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
            key="dashboard_logout"
        ):

            st.session_state.logged_in = False

            st.rerun()

    # =====================================================
    # HERO
    # =====================================================

    st.markdown("""
    <h1 class="main-title">
    🌌 Welcome to AMIVERSE
    </h1>
    """, unsafe_allow_html=True)

    st.markdown("""
    <p class="subtitle">
    AI & Blockchain Powered Student Ecosystem
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
            len(st.session_state.verified_certificates)
        )

    with col4:

        st.metric(
            "AMICOINS",
            st.session_state.coins
        )

    st.markdown("<br><br>", unsafe_allow_html=True)

    # =====================================================
    # ABOUT
    # =====================================================

    st.markdown("""
    <div class="card">

    <h2>
    🚀 About AMIVERSE
    </h2>

    <p>

    AMIVERSE is an AI & Blockchain powered student ecosystem
    designed for the future of education and placements.

    Features include:

    • AI Placement Prediction  
    • Resume Intelligence  
    • Blockchain Certificate Verification  
    • QR Validation  
    • AMICOINS Wallet  
    • Career Analytics  
    • Student Leaderboards  
    • AI Career Assistant  

    </p>

    </div>
    """, unsafe_allow_html=True)

    # =====================================================
    # FEATURE CARDS
    # =====================================================

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("""
        <div class="card">

        <h2>
        🏆 Student Rewards
        </h2>

        <p>

        Earn AMICOINS through:

        • Certificate Verification  
        • Resume Uploads  
        • AI Activities  
        • Placement Tasks  
        • Internships  
        • Hackathons  

        </p>

        </div>
        """, unsafe_allow_html=True)

    with col2:

        st.markdown("""
        <div class="card">

        <h2>
        🔗 Blockchain Verification
        </h2>

        <p>

        Secure student certificates using:

        • Blockchain Hashing  
        • QR Validation  
        • Tamper Proof Verification  
        • Digital Ownership  
        • Smart Authentication  

        </p>

        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # =====================================================
    # FUTURE ROADMAP
    # =====================================================

    st.markdown("""
    <div class="card">

    <h2>
    🌟 Future Vision
    </h2>

    <p>

    Future AMIVERSE integrations:

    • NFT Certificates  
    • MetaMask Wallets  
    • Recruiter Portals  
    • Smart Campus Rewards  
    • AI Skill Roadmaps  
    • Blockchain Academic Records  

    </p>

    </div>
    """, unsafe_allow_html=True)