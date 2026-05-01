from typing import Dict

from src.chunking import chunk_policy_documents, load_policy_documents
from src.citations import answer_from_retrieved_context, format_sources
from src.retrieval import PolicyRetriever


class PolicyRAGPipeline:
    def __init__(self, policy_dir: str = "data/policies"):
        documents = load_policy_documents(policy_dir)
        chunks = chunk_policy_documents(documents)
        self.retriever = PolicyRetriever(chunks)

    def answer(
        self,
        query: str,
        top_k: int = 3,
        min_score: float = 0.05,
    ) -> Dict[str, object]:
        retrieved_chunks = self.retriever.retrieve(query, top_k=top_k)

        return {
            "query": query,
            "answer": answer_from_retrieved_context(
                query=query,
                chunks=retrieved_chunks,
                min_score=min_score,
            ),
            "sources": format_sources(retrieved_chunks),
            "retrieved_chunks": retrieved_chunks,
        }
