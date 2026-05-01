import json
import sys
from collections import Counter
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT_DIR))

from src.chunking import chunk_policy_documents, load_policy_documents


def build_corpus_profile(policy_dir: str = "data/policies") -> dict:
    documents = load_policy_documents(policy_dir)
    chunks = chunk_policy_documents(documents)

    chunks_by_document = Counter(chunk["title"] for chunk in chunks)

    return {
        "policy_dir": policy_dir,
        "document_count": len(documents),
        "chunk_count": len(chunks),
        "documents": [
            {
                "doc_id": document["doc_id"],
                "title": document["title"],
                "source": document["source"],
                "character_count": len(document["text"]),
                "chunk_count": chunks_by_document[document["title"]],
            }
            for document in documents
        ],
        "chunks": [
            {
                "doc_id": chunk["doc_id"],
                "title": chunk["title"],
                "section": chunk["section"],
                "source": chunk["source"],
                "character_count": len(chunk["text"]),
            }
            for chunk in chunks
        ],
    }


def main():
    profile = build_corpus_profile()

    output_path = Path("reports/corpus_profile.json")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(profile, indent=2), encoding="utf-8")

    print("Policy Corpus Profile")
    print("=" * 40)
    print(f"Documents: {profile['document_count']}")
    print(f"Chunks:    {profile['chunk_count']}")
    print(f"Saved:     {output_path}")

    for document in profile["documents"]:
        print(
            f"- {document['title']} | chunks={document['chunk_count']} | source={document['source']}"
        )


if __name__ == "__main__":
    main()
