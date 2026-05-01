from typing import Dict, List

from src.chunking import chunk_policy_documents, load_policy_documents
from src.citations import answer_from_retrieved_context, format_sources
from src.retrieval import PolicyRetriever


class PolicyRAGPipeline:
    def __init__(self, policy_dir: str = "data/policies"):
        documents = load_policy_documents(policy_dir)
        chunks = chunk_policy_documents(documents)
        self.retriever = PolicyRetriever(chunks)

    def answer(self, query: str, top_k: int = 3) -> Dict[str, object]:
        retrieved_chunks = self.retriever.retrieve(query, top_k=top_k)
        return {
            "query": query,
            "answer": answer_from_retrieved_context(query, retrieved_chunks),
            "sources": format_sources(retrieved_chunks),
            "retrieved_chunks": retrieved_chunks,
        }
