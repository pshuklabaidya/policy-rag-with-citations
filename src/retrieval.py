from typing import Dict, List

import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


class PolicyRetriever:
    def __init__(self, chunks: List[Dict[str, str]], model_name: str = "all-MiniLM-L6-v2"):
        if not chunks:
            raise ValueError("PolicyRetriever requires at least one chunk.")

        self.chunks = chunks
        self.model = SentenceTransformer(model_name)
        self.texts = [chunk["text"] for chunk in chunks]
        self.embeddings = self.model.encode(self.texts, normalize_embeddings=True)

    def retrieve(self, query: str, top_k: int = 3) -> List[Dict[str, str]]:
        query_embedding = self.model.encode([query], normalize_embeddings=True)
        scores = cosine_similarity(query_embedding, self.embeddings)[0]
        top_indices = np.argsort(scores)[::-1][:top_k]

        results = []
        for rank, index in enumerate(top_indices, start=1):
            chunk = dict(self.chunks[index])
            chunk["score"] = float(scores[index])
            chunk["rank"] = rank
            results.append(chunk)

        return results
