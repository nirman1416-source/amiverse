import streamlit as st
import sqlite3
import uuid
import hashlib
import qrcode
import os
import pandas as pd

from blockchain import Blockchain

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="AMIVERSE Verification",
    page_icon="🔗",
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
# BLOCKCHAIN
# =====================================================

blockchain = Blockchain()

# =====================================================
# DATABASE
# =====================================================

conn = sqlite3.connect(
    "database.db",
    check_same_thread=False
)

cursor = conn.cursor()

cursor.execute("""

CREATE TABLE IF NOT EXISTS certificates (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    student_name TEXT,

    course TEXT,

    certificate_id TEXT,

    certificate_hash TEXT,

    block_hash TEXT
)

""")

conn.commit()

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
🔗 Blockchain Verification Engine
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<p class="subtitle">
AI & Blockchain Powered Certificate Authentication System
</p>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# =====================================================
# METRICS
# =====================================================

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        "Certificates Verified",
        "1200+"
    )

with col2:

    st.metric(
        "Blockchain Blocks",
        "350+"
    )

with col3:

    st.metric(
        "Fraud Prevention",
        "99.9%"
    )

st.markdown("<br>", unsafe_allow_html=True)

# =====================================================
# TABS
# =====================================================

tab1, tab2 = st.tabs([
    "Upload Certificate",
    "Verify Certificate"
])

# =====================================================
# UPLOAD CERTIFICATE
# =====================================================

with tab1:

    st.markdown("""
    <div class="card">
    """, unsafe_allow_html=True)

    st.subheader("📤 Upload Blockchain Certificate")

    student_name = st.text_input(
        "Student Name"
    )

    course = st.text_input(
        "Course Name"
    )

    uploaded_file = st.file_uploader(
        "Upload Certificate",
        type=[
            "pdf",
            "png",
            "jpg",
            "jpeg"
        ]
    )

    # =====================================================
    # FILE PREVIEW
    # =====================================================

    if uploaded_file is not None:

        file_extension = uploaded_file.name.split(".")[-1].lower()

        # IMAGE PREVIEW

        if file_extension in [
            "png",
            "jpg",
            "jpeg"
        ]:

            st.image(
                uploaded_file,
                width=500
            )

        # PDF PREVIEW

        elif file_extension == "pdf":

            st.success(
                "✅ PDF Certificate Uploaded Successfully"
            )

    st.markdown("<br>", unsafe_allow_html=True)

    # =====================================================
    # GENERATE CERTIFICATE
    # =====================================================

    if st.button(
        "Generate Blockchain Certificate",
        key="generate_certificate"
    ):

        if uploaded_file:

            # =====================================================
            # CREATE USER FOLDER
            # =====================================================

            user_folder = f"""
certificates/{st.session_state.username}
""".strip()

            os.makedirs(
                user_folder,
                exist_ok=True
            )

            # =====================================================
            # SAVE FILE
            # =====================================================

            file_path = f"""
{user_folder}/{uploaded_file.name}
""".strip()

            with open(
                file_path,
                "wb"
            ) as f:

                f.write(
                    uploaded_file.getbuffer()
                )

            # =====================================================
            # REWARD SYSTEM
            # =====================================================

            st.session_state.coins += 75

            if "transactions" not in st.session_state:

                st.session_state.transactions = []

            st.session_state.transactions.append({

                "activity":
                "Certificate Verification",

                "coins":
                75
            })

            if "verified_certificates" not in st.session_state:

                st.session_state.verified_certificates = []

            st.session_state.verified_certificates.append(
                uploaded_file.name
            )

            # =====================================================
            # FILE DATA
            # =====================================================

            file_data = uploaded_file.getvalue()

            # =====================================================
            # HASH
            # =====================================================

            certificate_hash = hashlib.sha256(
                file_data
            ).hexdigest()

            # =====================================================
            # BLOCKCHAIN
            # =====================================================

            previous_block = blockchain.get_previous_block()

            previous_proof = previous_block['proof']

            proof = blockchain.proof_of_work(
                previous_proof
            )

            previous_hash = blockchain.hash(
                previous_block
            )

            block = blockchain.create_block(

                proof,

                previous_hash,

                certificate_hash
            )

            block_hash = blockchain.hash(
                block
            )

            # =====================================================
            # CERTIFICATE ID
            # =====================================================

            certificate_id = str(
                uuid.uuid4()
            )[:8]

            # =====================================================
            # DATABASE STORAGE
            # =====================================================

            cursor.execute(
                """
                INSERT INTO certificates
                (
                    student_name,
                    course,
                    certificate_id,
                    certificate_hash,
                    block_hash
                )

                VALUES (?,?,?,?,?)
                """,
                (
                    student_name,
                    course,
                    certificate_id,
                    certificate_hash,
                    block_hash
                )
            )

            conn.commit()

            # =====================================================
            # QR CODE
            # =====================================================

            os.makedirs(
                "qrcodes",
                exist_ok=True
            )

            qr_data = f"""

Certificate ID: {certificate_id}

Student: {student_name}

Course: {course}

Uploaded By:
{st.session_state.username}

Blockchain Hash:
{block_hash}

"""

            qr = qrcode.make(qr_data)

            qr_path = f"""
qrcodes/{certificate_id}.png
""".strip()

            qr.save(qr_path)

            # =====================================================
            # SUCCESS
            # =====================================================

            st.success(
                "✅ Blockchain Certificate Generated Successfully"
            )

            st.info(
                f"🆔 Certificate ID: {certificate_id}"
            )

            st.info(
                "🪙 +75 AMICOINS Added To Wallet"
            )

            # =====================================================
            # RESULT DISPLAY
            # =====================================================

            col1, col2 = st.columns(2)

            with col1:

                st.markdown("""
                ### 🔐 Certificate Hash
                """)

                st.code(
                    certificate_hash[:60]
                )

                st.markdown("""
                ### ⛓ Blockchain Hash
                """)

                st.code(
                    block_hash[:60]
                )

            with col2:

                st.markdown("""
                ### 📱 QR Verification
                """)

                st.image(
                    qr_path,
                    width=260
                )

            st.markdown("<br>", unsafe_allow_html=True)

            # =====================================================
            # FILE SAVED INFO
            # =====================================================

            st.markdown(f"""
            <div class="card">

            <h2 style="
            color:white;
            margin-bottom:15px;
            ">
            📂 Certificate Stored
            </h2>

            <p style="
            color:#cbd5e1;
            line-height:2;
            ">

            Uploaded By:
            <b>{st.session_state.username}</b>

            <br><br>

            File Name:
            <b>{uploaded_file.name}</b>

            <br><br>

            Storage Path:
            <b>{file_path}</b>

            </p>

            </div>
            """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# =====================================================
# VERIFY CERTIFICATE
# =====================================================

with tab2:

    st.markdown("""
    <div class="card">
    """, unsafe_allow_html=True)

    st.subheader("🔍 Verify Blockchain Certificate")

    verify_id = st.text_input(
        "Enter Certificate ID"
    )

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button(
        "Verify Certificate",
        key="verify_certificate"
    ):

        cursor.execute(
            """
            SELECT * FROM certificates
            WHERE certificate_id=?
            """,
            (verify_id,)
        )

        result = cursor.fetchone()

        # =====================================================
        # VALID CERTIFICATE
        # =====================================================

        if result:

            st.success(
                "✅ Valid Blockchain Certificate"
            )

            st.markdown(f"""
            <div class="card">

            <h2 style="
            color:white;
            margin-bottom:20px;
            ">
            🎓 Certificate Details
            </h2>

            <p style="
            color:#cbd5e1;
            line-height:2;
            font-size:16px;
            ">

            👤 Student Name:
            <b>{result[1]}</b>

            <br><br>

            📘 Course:
            <b>{result[2]}</b>

            <br><br>

            🆔 Certificate ID:
            <b>{result[3]}</b>

            <br><br>

            🔐 Certificate Hash:
            <b>{result[4][:35]}...</b>

            <br><br>

            ⛓ Blockchain Hash:
            <b>{result[5][:35]}...</b>

            </p>

            </div>
            """, unsafe_allow_html=True)

            qr_path = f"qrcodes/{verify_id}.png"

            if os.path.exists(qr_path):

                st.image(
                    qr_path,
                    width=250
                )

        # =====================================================
        # INVALID CERTIFICATE
        # =====================================================

        else:

            st.error(
                "❌ Invalid or Fake Certificate"
            )

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
🌌 About Verification Engine
</h2>

<p style="
color:#cbd5e1;
line-height:2;
font-size:16px;
">

The AMIVERSE Blockchain Verification Engine
uses decentralized blockchain technology
to create tamper-proof academic certificates.

Features include:

• Blockchain Certificate Hashing  

• QR Code Verification  

• Fraud Prevention  

• Tamper-Proof Records  

• Secure Digital Authentication  

• Student Reward System  

This system ensures trust, authenticity,
and transparency in academic verification.

</p>

</div>
""", unsafe_allow_html=True)