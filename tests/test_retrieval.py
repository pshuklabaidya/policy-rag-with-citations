from src.chunking import chunk_policy_documents, load_policy_documents
from src.retrieval import PolicyRetriever


def test_retriever_returns_ranked_policy_chunks():
    documents = load_policy_documents("data/policies")
    chunks = chunk_policy_documents(documents)

    retriever = PolicyRetriever(chunks)
    results = retriever.retrieve("expense report submission deadline", top_k=3)

    assert len(results) == 3
    assert results[0]["rank"] == 1
    assert "score" in results[0]
    assert results[0]["title"] == "Expense Reimbursement Policy"
