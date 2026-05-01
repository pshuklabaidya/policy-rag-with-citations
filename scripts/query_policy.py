import argparse
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT_DIR))

from src.rag_pipeline import PolicyRAGPipeline


def main():
    parser = argparse.ArgumentParser(
        description="Ask a question against synthetic policy documents."
    )
    parser.add_argument("question", help="Policy question to answer")
    parser.add_argument("--top-k", type=int, default=3, help="Number of sources to retrieve")
    parser.add_argument(
        "--min-score",
        type=float,
        default=0.05,
        help="Minimum retrieval score required for citation-grounded answering",
    )

    args = parser.parse_args()

    pipeline = PolicyRAGPipeline()
    result = pipeline.answer(
        query=args.question,
        top_k=args.top_k,
        min_score=args.min_score,
    )

    print("\nQuestion")
    print("=" * 40)
    print(result["query"])

    print("\nAnswer")
    print("=" * 40)
    print(result["answer"])

    print("\nSources")
    print("=" * 40)

    for source in result["sources"]:
        print(
            f"{source['citation']} {source['title']} - {source['section']} "
            f"| score={source['score']} | {source['source']}"
        )


if __name__ == "__main__":
    main()
