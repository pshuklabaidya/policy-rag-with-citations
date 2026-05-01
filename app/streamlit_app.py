import sys
from pathlib import Path

import pandas as pd
import streamlit as st

ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT_DIR))

from src.rag_pipeline import PolicyRAGPipeline


st.set_page_config(
    page_title="Policy RAG With Citations",
    page_icon="📚",
    layout="wide",
)

st.title("Policy RAG With Citations")
st.caption("Synthetic workplace policy assistant with retrieval evidence and source citations.")

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
    st.markdown("Synthetic data only. No real company policy data is used.")

query = st.text_input(
    "Ask a policy question",
    value="What is the deadline for submitting an expense report?",
)

if "pipeline" not in st.session_state:
    st.session_state.pipeline = PolicyRAGPipeline()

if st.button("Answer Question", type="primary"):
    result = st.session_state.pipeline.answer(
        query=query,
        top_k=top_k,
        min_score=min_score,
    )

    st.subheader("Answer")
    st.write(result["answer"])

    st.subheader("Sources")
    st.dataframe(pd.DataFrame(result["sources"]), use_container_width=True)

    st.subheader("Retrieved Evidence")
    for source, chunk in zip(result["sources"], result["retrieved_chunks"]):
        with st.expander(f"{source['citation']} {source['title']} - {source['section']}"):
            st.write(chunk["text"])
