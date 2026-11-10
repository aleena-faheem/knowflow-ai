
import streamlit as st

st.set_page_config(
    page_title="Evaluation Center | KnowFlow AI",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Evaluation Center")

st.write(
    "Measure and monitor the performance of the KnowFlow AI "
    "RAG pipeline. Evaluate retrieval quality, answer correctness, "
    "citation accuracy and response latency using test datasets "
    "and performance metrics. Track improvements and identify "
    "areas that need optimization."
)

st.info(
    "This feature is under development. "
    "Evaluation datasets, performance metrics and analytics "
    "will be implemented soon."
)
