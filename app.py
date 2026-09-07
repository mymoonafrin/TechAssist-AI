import streamlit as st

from workflow import process_request
from memory import clear_memory

st.set_page_config(
    page_title="TechAssist AI",
    page_icon="🛠️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown(
    """
    <style>
    .stApp {
        background: #0d1117;
    }

    [data-testid="stSidebar"] {
        background: #171b24;
        border-right: 1px solid #292f3a;
    }

    [data-testid="stSidebar"] > div:first-child {
        padding-top: 1.5rem;
    }

    .brand {
        font-size: 25px;
        font-weight: 700;
        color: #f0f3f7;
        margin-bottom: 5px;
    }

    .brand-subtitle {
        color: #9ba5b4;
        font-size: 13px;
        line-height: 1.5;
        margin-bottom: 24px;
    }

    .status-card {
        background: #202631;
        border: 1px solid #303744;
        border-radius: 12px;
        padding: 12px 14px;
        margin-bottom: 25px;
    }

    .status-dot {
        display: inline-block;
        width: 9px;
        height: 9px;
        background: #35c759;
        border-radius: 50%;
        margin-right: 8px;
    }

    .status-text {
        color: #dce2ea;
        font-size: 13px;
    }

    .sidebar-section {
        color: #7f8998;
        font-size: 11px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1.2px;
        margin-top: 24px;
        margin-bottom: 12px;
    }

    .capability {
        color: #d0d6df;
        font-size: 14px;
        padding: 7px 0;
    }

    .main-container {
        max-width: 1100px;
        margin: 0 auto;
        padding: 30px 20px 120px 20px;
    }

    .main-title {
        font-size: 38px;
        font-weight: 750;
        color: #f3f5f8;
        letter-spacing: -1px;
        margin-bottom: 3px;
    }

    .main-subtitle {
        color: #8f99a8;
        font-size: 15px;
        margin-bottom: 25px;
    }

    .welcome-card {
        background: #171c25;
        border: 1px solid #292f3a;
        border-radius: 16px;
        padding: 22px 24px;
        margin-bottom: 24px;
    }

    .welcome-title {
        font-size: 22px;
        font-weight: 650;
        color: #f0f3f7;
        margin-bottom: 6px;
    }

    .welcome-text {
        color: #99a3b1;
        font-size: 14px;
        line-height: 1.6;
    }

    .section-title {
        color: #e9edf2;
        font-size: 17px;
        font-weight: 650;
        margin-bottom: 13px;
    }

    .feature-card {
        background: #171c25;
        border: 1px solid #292f3a;
        border-radius: 14px;
        padding: 17px;
        min-height: 125px;
        margin-bottom: 5px;
    }

    .feature-icon {
        font-size: 25px;
        margin-bottom: 8px;
    }

    .feature-title {
        color: #edf0f4;
        font-size: 15px;
        font-weight: 650;
        margin-bottom: 4px;
    }

    .feature-description {
        color: #8791a0;
        font-size: 12px;
        line-height: 1.4;
    }

    div.stButton > button {
        width: 100%;
        min-height: 38px;
        border-radius: 9px;
        border: 1px solid #303744;
        background: #202631;
        color: #dce2e9;
        font-size: 13px;
    }

    div.stButton > button:hover {
        background: #282f3b;
        border-color: #596577;
        color: #ffffff;
    }

    .activity-card {
        background: #171c25;
        border: 1px solid #292f3a;
        border-radius: 14px;
        padding: 18px 20px;
        margin-top: 18px;
    }

    .activity-title {
        color: #e9edf2;
        font-size: 15px;
        font-weight: 650;
        margin-bottom: 12px;
    }

    .activity-item {
        color: #aab3c0;
        font-size: 13px;
        padding: 5px 0;
    }

    .activity-check {
        color: #72d98b;
        font-weight: 600;
    }

    .footer {
        color: #646e7d;
        font-size: 10px;
        margin-top: 30px;
    }

    [data-testid="stChatMessage"] {
        background: #151a22;
        border: 1px solid #252c36;
        border-radius: 14px;
        margin-bottom: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

if "messages" not in st.session_state:
    st.session_state.messages = []

if "activity" not in st.session_state:
    st.session_state.activity = []

def run_query(query):
    st.session_state.messages.append(
        {
            "role": "user",
            "content": query
        }
    )

    with st.chat_message("user"):
        st.markdown(query)

    with st.chat_message("assistant"):
        with st.spinner("TechAssist AI is analyzing your problem..."):
            response, activity = process_request(query)

        st.markdown(response)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )

    st.session_state.activity = activity

with st.sidebar:
    st.markdown(
        '<div class="brand">🛠️ TechAssist AI</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="brand-subtitle">Agentic IT Helpdesk Assistant</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="status-card">
            <span class="status-dot"></span>
            <span class="status-text">System Online</span>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-section">Capabilities</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="capability">🔎 Knowledge Base & RAG</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="capability">🔧 Diagnostic Tools</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="capability">🧠 Conversation Memory</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="capability">🎫 Support Ticket Escalation</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-section">Session</div>',
        unsafe_allow_html=True
    )

    if st.button("🗑️ Clear Conversation"):
        clear_memory()
        st.session_state.messages = []
        st.session_state.activity = []
        st.rerun()

    st.markdown(
        '<div class="footer">TechAssist AI • Local AI Helpdesk</div>',
        unsafe_allow_html=True
    )

st.markdown('<div class="main-container">', unsafe_allow_html=True)

st.markdown(
    """
    <div class="main-title">🛠️ TechAssist AI</div>
    <div class="main-subtitle">
        Agentic IT Helpdesk Assistant
    </div>
    """,
    unsafe_allow_html=True
)

if not st.session_state.messages:
    st.markdown(
        """
        <div class="welcome-card">
            <div class="welcome-title">👋 Welcome to TechAssist</div>
            <div class="welcome-text">
                Describe your technical problem and TechAssist AI will
                analyze the request, search its troubleshooting knowledge
                base, use diagnostic tools when required, and escalate
                unresolved issues to IT support.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-title">What can I help you with?</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3, gap="medium")

    with col1:
        st.markdown(
            """
            <div class="feature-card">
                <div class="feature-icon">📶</div>
                <div class="feature-title">Wi-Fi & Internet</div>
                <div class="feature-description">
                    Diagnose Wi-Fi and internet connectivity problems.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button("Try Wi-Fi Help →", key="wifi"):
            run_query(
                "My laptop is connected to Wi-Fi but I cannot access the internet."
            )
            st.rerun()

    with col2:
        st.markdown(
            """
            <div class="feature-card">
                <div class="feature-icon">🖨️</div>
                <div class="feature-title">Printer</div>
                <div class="feature-description">
                    Troubleshoot printing and printer connection problems.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button("Try Printer Help →", key="printer"):
            run_query("My printer is not printing.")
            st.rerun()

    with col3:
        st.markdown(
            """
            <div class="feature-card">
                <div class="feature-icon">💻</div>
                <div class="feature-title">Computer</div>
                <div class="feature-description">
                    Get help with slow performance and system crashes.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button("Try Computer Help →", key="computer"):
            run_query("My computer is very slow.")
            st.rerun()

    col4, col5, col6 = st.columns(3, gap="medium")

    with col4:
        st.markdown(
            """
            <div class="feature-card">
                <div class="feature-icon">🔐</div>
                <div class="feature-title">Password</div>
                <div class="feature-description">
                    Get help with password reset and account access.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button("Try Password Help →", key="password"):
            run_query(
                "I forgot my password and need help resetting it."
            )
            st.rerun()

    with col5:
        st.markdown(
            """
            <div class="feature-card">
                <div class="feature-icon">📦</div>
                <div class="feature-title">Software</div>
                <div class="feature-description">
                    Troubleshoot software installation problems.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button("Try Software Help →", key="software"):
            run_query(
                "I am having trouble installing software."
            )
            st.rerun()

    with col6:
        st.markdown(
            """
            <div class="feature-card">
                <div class="feature-icon">🌐</div>
                <div class="feature-title">Network</div>
                <div class="feature-description">
                    Diagnose general network connectivity problems.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button("Try Network Help →", key="network"):
            run_query(
                "I am having a network connectivity problem."
            )
            st.rerun()

else:
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if st.session_state.activity:
        st.markdown(
            """
            <div class="activity-card">
                <div class="activity-title">⚙️ TechAssist Activity</div>
            """,
            unsafe_allow_html=True
        )

        for item in st.session_state.activity:
            st.markdown(
                f'<div class="activity-item"><span class="activity-check">✓</span> {item}</div>',
                unsafe_allow_html=True
            )

        st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

query = st.chat_input("Describe your IT problem...")

if query:
    run_query(query)
    st.rerun()