from pathlib import Path

from scripts.profile_corpus import build_corpus_profile
from src.chunking import chunk_policy_documents, load_policy_documents


def test_policy_documents_include_synthetic_disclosure():
    for path in Path("data/policies").glob("*.md"):
        text = path.read_text(encoding="utf-8").lower()
        assert "synthetic document" in text


def test_policy_chunks_include_traceable_metadata():
    documents = load_policy_documents("data/policies")
    chunks = chunk_policy_documents(documents)

    assert len(chunks) >= 10

    for chunk in chunks:
        assert chunk["doc_id"]
        assert chunk["title"]
        assert chunk["section"]
        assert chunk["source"].startswith("data/policies/")
        assert chunk["text"]


def test_corpus_profile_counts_documents_and_chunks():
    profile = build_corpus_profile("data/policies")

    assert profile["document_count"] == 3
    assert profile["chunk_count"] >= 15
    assert len(profile["documents"]) == profile["document_count"]
    assert len(profile["chunks"]) == profile["chunk_count"]
