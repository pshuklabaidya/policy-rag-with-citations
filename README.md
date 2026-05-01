# Policy RAG With Citations

[![CI](https://github.com/pshuklabaidya/policy-rag-with-citations/actions/workflows/ci.yml/badge.svg)](https://github.com/pshuklabaidya/policy-rag-with-citations/actions/workflows/ci.yml)

A lightweight retrieval-augmented generation demo for answering questions over synthetic workplace policy documents with source citations, confidence scoring, retrieval evaluation, and abstention behavior.

## Overview

Policy RAG With Citations demonstrates citation-grounded document intelligence over a synthetic workplace policy corpus. The system loads markdown policy documents, chunks them by section, retrieves relevant sections with TF-IDF cosine similarity, and returns answers tied to traceable source metadata.

## Features

- Synthetic workplace policy corpus
- Section-based markdown chunking
- Lightweight TF-IDF retrieval
- Citation-grounded answers
- Source metadata with policy title, section, file path, and retrieval score
- Low-confidence abstention behavior
- Streamlit demo interface
- Command-line query demo
- Retrieval evaluation script
- Corpus profiling script
- Pytest coverage
- GitHub Actions CI

## Synthetic Data Disclosure

All policy documents in this repository are synthetic and created for portfolio demonstration purposes only. No real company policy, employee data, customer data, or proprietary internal data is used.

## Architecture Documentation

Detailed architecture notes are available in `docs/architecture.md`.

## Data And Corpus Profile

The synthetic policy corpus is documented in `docs/data_dictionary.md`.

Generate a corpus profile:

```bash
python scripts/profile_corpus.py
```

The generated report is saved to `reports/corpus_profile.json`.

## Project Structure

```text
policy-rag-with-citations/
├── .github/
│   └── workflows/
│       └── ci.yml
├── .streamlit/
│   └── config.toml
├── app/
│   └── streamlit_app.py
├── data/
│   ├── eval/
│   │   └── eval_questions.json
│   └── policies/
│       ├── expense_policy.md
│       ├── remote_work_policy.md
│       └── security_policy.md
├── docs/
│   ├── architecture.md
│   ├── data_dictionary.md
│   └── demo_questions.md
├── reports/
│   ├── corpus_profile.json
│   ├── demo_outputs.md
│   └── retrieval_eval.json
├── scripts/
│   ├── evaluate_retrieval.py
│   ├── generate_demo_outputs.py
│   ├── profile_corpus.py
│   └── query_policy.py
├── src/
│   ├── app_utils.py
│   ├── chunking.py
│   ├── citations.py
│   ├── rag_pipeline.py
│   └── retrieval.py
├── tests/
├── Makefile
├── pytest.ini
├── requirements.txt
└── README.md
```

## Setup

```bash
python -m pip install -r requirements.txt
```

## Developer Commands

Common project commands are available through `make`.

| Command | Purpose |
|---|---|
| `make install` | Install project dependencies |
| `make test` | Run pytest suite |
| `make eval` | Run retrieval evaluation and save metrics |
| `make demo` | Generate portfolio demo outputs |
| `make app` | Launch the Streamlit app |
| `make all` | Run tests, retrieval evaluation, and demo generation |

## Run Tests

```bash
pytest -q
```

## Run Retrieval Evaluation

```bash
python scripts/evaluate_retrieval.py
```

Generate a saved JSON metrics report:

```bash
python scripts/evaluate_retrieval.py --output reports/retrieval_eval.json
```

Current baseline target:

```text
Top-1 accuracy: 100.00%
```

## Command-Line Demo

Ask a policy question directly from the terminal:

```bash
python scripts/query_policy.py "What is the deadline for submitting an expense report?"
```

Run an unsupported question with stricter abstention behavior:

```bash
python scripts/query_policy.py "What is the company stock price?" --min-score 0.50
```

Additional examples are available in `docs/demo_questions.md`.

## Run Streamlit App

```bash
python -m streamlit run app/streamlit_app.py
```

The Streamlit app includes:

- Quick-question buttons for common policy questions
- Top-source confidence display
- Retrieved-source table with policy title, section, file path, and score
- Expandable evidence panels for citation traceability
- Configurable retrieval count and confidence threshold

## Example Questions

```text
What is the deadline for submitting an expense report?
```

```text
When must security incidents be reported?
```

```text
What are the core collaboration hours for remote employees?
```

```text
Which systems require multi-factor authentication?
```

```text
What is the company stock price?
```

## Retrieval Evaluation

The repository includes a small retrieval evaluation set that checks whether the top-ranked source matches the expected policy section.

The saved baseline report is available at:

```text
reports/retrieval_eval.json
```

## Portfolio Evidence

The repository includes generated demo and evaluation artifacts:

- `reports/demo_outputs.md` shows example questions, citation-grounded answers, source sections, retrieval scores, and abstention behavior.
- `reports/retrieval_eval.json` stores retrieval evaluation metrics for the baseline question set.
- `reports/corpus_profile.json` stores document and chunk metadata for the synthetic policy corpus.

Regenerate demo outputs:

```bash
python scripts/generate_demo_outputs.py
```

## Continuous Integration

GitHub Actions runs tests and retrieval evaluation on every push and pull request.

```text
.github/workflows/ci.yml
```

## Architecture

The system loads markdown policy documents, splits them into policy-section chunks, ranks chunks against a user query with TF-IDF cosine similarity, and formats the answer with citation metadata. Each citation includes the policy title, section ID, source file, and retrieval score.

## Portfolio Value

This project highlights practical RAG implementation skills:

- Document ingestion
- Chunking strategy
- Retrieval ranking
- Citation formatting
- Evidence transparency
- Abstention behavior
- Evaluation design
- Streamlit demo development
- CLI tooling
- CI automation
- Responsible synthetic-data disclosure

## Suggested Repository Topics

Recommended GitHub topics for this project:

```text
rag, retrieval-augmented-generation, citations, streamlit, synthetic-data, document-ai, ai-portfolio
```

## Limitations

The baseline uses TF-IDF retrieval rather than hosted embeddings or a vector database. This keeps the demo lightweight and easy to run, while preserving the core citation-grounded RAG workflow.

The answer generator is intentionally simple and extractive. A production version would use a stronger language model with stricter prompt controls, citation validation, access controls, logging, and human review workflows.

## Future Enhancements

- Add embedding-based retrieval as an optional backend
- Add vector database support
- Add richer answer synthesis with citation validation
- Add per-query retrieval diagnostics
- Add user feedback capture
- Add document upload support
- Add deployment configuration
