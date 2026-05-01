import json
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT_DIR))

from src.rag_pipeline import PolicyRAGPipeline


def load_eval_questions(path: str = "data/eval/eval_questions.json"):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def main():
    pipeline = PolicyRAGPipeline()
    eval_items = load_eval_questions()

    total = len(eval_items)
    correct_top_1 = 0

    print("\nPolicy RAG Retrieval Evaluation")
    print("=" * 40)

    for item in eval_items:
        question = item["question"]
        expected_source = item["expected_source"]

        result = pipeline.answer(question, top_k=3)
        top_source = result["sources"][0]
        predicted_source = f"{top_source['title']} - {top_source['section']}"

        is_correct = predicted_source == expected_source
        correct_top_1 += int(is_correct)

        status = "PASS" if is_correct else "FAIL"

        print(f"\n{status}: {question}")
        print(f"Expected:  {expected_source}")
        print(f"Predicted: {predicted_source}")
        print(f"Score:     {top_source['score']}")

    accuracy = correct_top_1 / total if total else 0

    print("\nSummary")
    print("=" * 40)
    print(f"Total questions: {total}")
    print(f"Top-1 correct:   {correct_top_1}")
    print(f"Top-1 accuracy:  {accuracy:.2%}")


if __name__ == "__main__":
    main()
