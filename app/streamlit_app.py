import sys
from pathlib import Path

import pandas as pd
import streamlit as st

ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT_DIR))

from src.app_utils import SAMPLE_QUESTIONS, confidence_label
from src.rag_pipeline import PolicyRAGPipeline


st.set_page_config(
    page_title="Policy RAG With Citations",
    page_icon="📚",
    layout="wide",
)

st.title("Policy RAG With Citations")
st.caption(
    "Synthetic workplace policy assistant with retrieval evidence, source citations, "
    "confidence scoring, and abstention behavior."
)

with st.sidebar:
    st.header("Demo Settings")
    top_k = st.slider("Retrieved sources", min_value=1, max_value=5, value=3)
    min_score = st.slider(
        "Minimum citation confidence",
        min_value=0.00,
        max_value=0.50,
        value=0.05,
        step=0.01,
    )
    st.info("Synthetic data only. No real company policy data is used.")

if "pipeline" not in st.session_state:
    st.session_state.pipeline = PolicyRAGPipeline()

if "query" not in st.session_state:
    st.session_state.query = SAMPLE_QUESTIONS[0]

st.subheader("Sample Questions")
cols = st.columns(2)

for index, sample_question in enumerate(SAMPLE_QUESTIONS):
    with cols[index % 2]:
        if st.button(sample_question, use_container_width=True):
            st.session_state.query = sample_question

query = st.text_input(
    "Ask a policy question",
    key="query",
)

if st.button("Answer Question", type="primary"):
    result = st.session_state.pipeline.answer(
        query=query,
        top_k=top_k,
        min_score=min_score,
    )

    top_score = result["sources"][0]["score"] if result["sources"] else 0.0

    metric_cols = st.columns(3)
    metric_cols[0].metric("Top source score", f"{top_score:.4f}")
    metric_cols[1].metric("Confidence", confidence_label(top_score))
    metric_cols[2].metric("Retrieved sources", len(result["sources"]))

    st.subheader("Answer")
    st.write(result["answer"])

    st.subheader("Sources")
    source_df = pd.DataFrame(result["sources"])
    st.dataframe(source_df, use_container_width=True, hide_index=True)

    st.subheader("Retrieved Evidence")
    for source, chunk in zip(result["sources"], result["retrieved_chunks"]):
        title = f"{source['citation']} {source['title']} - {source['section']}"
        with st.expander(title):
            st.write(chunk["text"])
            st.caption(f"Source file: {source['source']} | Retrieval score: {source['score']}")
else:
    st.write("Select a sample question or enter a policy question, then run the assistant.")
