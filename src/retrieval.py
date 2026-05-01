from typing import Dict, List

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class PolicyRetriever:
    def __init__(self, chunks: List[Dict[str, str]]):
        if not chunks:
            raise ValueError("PolicyRetriever requires at least one chunk.")

        self.chunks = chunks
        self.texts = [chunk["text"] for chunk in chunks]

        self.vectorizer = TfidfVectorizer(
            lowercase=True,
            stop_words="english",
            ngram_range=(1, 2),
        )

        self.document_matrix = self.vectorizer.fit_transform(self.texts)

    def retrieve(self, query: str, top_k: int = 3) -> List[Dict[str, str]]:
        query_vector = self.vectorizer.transform([query])
        scores = cosine_similarity(query_vector, self.document_matrix)[0]
        top_indices = np.argsort(scores)[::-1][:top_k]

        results = []

        for rank, index in enumerate(top_indices, start=1):
            chunk = dict(self.chunks[index])
            chunk["score"] = float(scores[index])
            chunk["rank"] = rank
            results.append(chunk)

        return results
