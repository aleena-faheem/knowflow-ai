
import streamlit as st

st.set_page_config(
    page_title="AI Assistant | KnowFlow AI",
    page_icon="💬",
    layout="wide"
)

st.title("💬 AI Knowledge Assistant")

st.write(
    "Interact with your uploaded documents using natural language. "
    "Ask questions, explore complex topics and receive context-aware "
    "answers generated using Retrieval-Augmented Generation (RAG). "
    "Every answer is designed to include relevant source citations "
    "so you can verify the information."
)

st.info(
    "This feature is under development. "
    "Document-based conversations and citation-backed answers "
    "will be implemented soon."
)
