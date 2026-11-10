
import streamlit as st

from api_client import get_health, get_dashboard_stats

# Page configuration
st.set_page_config(
    page_title="KnowFlow AI",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom styling
st.markdown("""
<style>
.stApp {
    background-color: #0B1120;
    color: #E2E8F0;
}

[data-testid="stSidebar"] {
    background-color: #111827;
}

h1, h2, h3 {
    color: #E2E8F0;
}

[data-testid="stMetric"] {
    background-color: #17243A;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #263B59;
}

[data-testid="stMetricValue"] {
    color: #38BDF8;
}

.stButton button {
    background-color: #0284C7;
    color: white;
    border-radius: 8px;
    border: none;
}
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("🧠 KnowFlow AI")
    st.caption("Your intelligent knowledge assistant")
    st.divider()

    st.subheader("Navigation")
    st.page_link("app.py", label="Dashboard", icon="🏠")
    st.page_link(
        "pages/1_Knowledge_Library.py",
        label="Knowledge Library",
        icon="📚"
    )
    st.page_link(
        "pages/2_AI_Assistant.py",
        label="AI Assistant",
        icon="💬"
    )
    st.page_link(
        "pages/3_Document_Comparison.py",
        label="Document Comparison",
        icon="📄"
    )
    st.page_link(
        "pages/4_Evaluation_Center.py",
        label="Evaluation Center",
        icon="📊"
    )
    st.page_link(
        "pages/5_Settings.py",
        label="Settings",
        icon="⚙️"
    )

    st.divider()
    st.caption("KnowFlow AI v1.0 | Development")

# Main dashboard
st.title("Welcome to KnowFlow AI")
st.write(
    "Your centralized AI-powered knowledge management workspace."
)

# Check backend health
health = get_health()

if health:
    st.success("System operational — Backend connected")
else:
    st.error(
        "Backend unavailable. Start the FastAPI server "
        "to load dashboard statistics."
    )

# Retrieve actual database statistics
stats = get_dashboard_stats()

st.divider()
st.subheader("Workspace Overview")

if stats:
    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Total Documents",
        stats["total_documents"]
    )

    col2.metric(
        "Processed Chunks",
        stats["processed_chunks"]
    )

    col3.metric(
        "Conversations",
        stats["total_conversations"]
    )

    col4.metric(
        "Messages",
        stats["total_messages"]
    )
else:
    st.info("Statistics will appear when the backend is available.")

st.divider()

left, right = st.columns([2, 1])

with left:
    st.subheader("Recent Activity")
    st.info(
        "No recent activity yet. Upload your first document "
        "to get started."
    )

with right:
    st.subheader("Quick Actions")

    if st.button("📚 Open Knowledge Library", use_container_width=True):
        st.switch_page("pages/1_Knowledge_Library.py")

    if st.button("💬 Open AI Assistant", use_container_width=True):
        st.switch_page("pages/2_AI_Assistant.py")

    if st.button("📊 View Evaluation Center", use_container_width=True):
        st.switch_page("pages/4_Evaluation_Center.py")

st.divider()

st.caption(
    "KnowFlow AI — Transform your documents into intelligent knowledge."
)
