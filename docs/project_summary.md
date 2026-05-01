# Project Summary

Policy RAG With Citations is a portfolio-ready retrieval-augmented generation demo for citation-grounded policy question answering over synthetic workplace documents.

## Core Capabilities

- Loads synthetic markdown policy documents.
- Splits policies into section-level chunks.
- Retrieves relevant policy sections with TF-IDF cosine similarity.
- Returns answers tied to bracketed citations.
- Displays source metadata including policy title, section, file path, and retrieval score.
- Abstains when evidence confidence is too low.
- Provides Streamlit and command-line demo entry points.
- Includes retrieval evaluation, corpus profiling, tests, and CI.

## Technical Skills Demonstrated

- Retrieval-augmented generation workflow design
- Document ingestion and chunking
- Lightweight information retrieval
- Citation traceability
- Confidence thresholding
- Abstention behavior
- Evaluation-driven development
- Streamlit application development
- CLI tooling
- Pytest test coverage
- GitHub Actions CI
- Synthetic-data disclosure

## Demo Entry Points

- Streamlit app: `python -m streamlit run app/streamlit_app.py`
- CLI query: `python scripts/query_policy.py "What is the deadline for submitting an expense report?"`
- Retrieval evaluation: `python scripts/evaluate_retrieval.py`
- Corpus profile: `python scripts/profile_corpus.py`
- Demo output generation: `python scripts/generate_demo_outputs.py`

## Portfolio Positioning

This project demonstrates a practical document intelligence workflow for policy, compliance, HR, security, and internal knowledge-base use cases. The design emphasizes trustworthy answers, visible evidence, and clear failure behavior when the available documents do not support an answer.

## Synthetic Data Disclosure

All policies are synthetic and created for demonstration purposes only. No real company policy, customer data, employee data, or proprietary internal data is used.
