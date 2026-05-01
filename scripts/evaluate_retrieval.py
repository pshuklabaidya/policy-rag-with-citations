import argparse
import json
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT_DIR))

from src.rag_pipeline import PolicyRAGPipeline


def load_eval_questions(path: str = "data/eval/eval_questions.json"):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def evaluate_items(eval_items, top_k: int = 3):
    pipeline = PolicyRAGPipeline()

    results = []
    correct_top_1 = 0

    for item in eval_items:
        question = item["question"]
        expected_source = item["expected_source"]

        result = pipeline.answer(question, top_k=top_k)
        top_source = result["sources"][0]
        predicted_source = f"{top_source['title']} - {top_source['section']}"

        is_correct = predicted_source == expected_source
        correct_top_1 += int(is_correct)

        results.append(
            {
                "question": question,
                "expected_source": expected_source,
                "predicted_source": predicted_source,
                "top_score": top_source["score"],
                "passed": is_correct,
            }
        )

    total = len(eval_items)
    accuracy = correct_top_1 / total if total else 0

    return {
        "total_questions": total,
        "top_1_correct": correct_top_1,
        "top_1_accuracy": accuracy,
        "results": results,
    }


def print_report(metrics):
    print("\nPolicy RAG Retrieval Evaluation")
    print("=" * 40)

    for item in metrics["results"]:
        status = "PASS" if item["passed"] else "FAIL"

        print(f"\n{status}: {item['question']}")
        print(f"Expected:  {item['expected_source']}")
        print(f"Predicted: {item['predicted_source']}")
        print(f"Score:     {item['top_score']}")

    print("\nSummary")
    print("=" * 40)
    print(f"Total questions: {metrics['total_questions']}")
    print(f"Top-1 correct:   {metrics['top_1_correct']}")
    print(f"Top-1 accuracy:  {metrics['top_1_accuracy']:.2%}")


def main():
    parser = argparse.ArgumentParser(description="Evaluate policy retrieval quality.")
    parser.add_argument(
        "--eval-file",
        default="data/eval/eval_questions.json",
        help="Path to retrieval evaluation questions.",
    )
    parser.add_argument(
        "--top-k",
        type=int,
        default=3,
        help="Number of retrieved chunks to evaluate.",
    )
    parser.add_argument(
        "--output",
        default=None,
        help="Optional path for JSON evaluation metrics.",
    )

    args = parser.parse_args()

    eval_items = load_eval_questions(args.eval_file)
    metrics = evaluate_items(eval_items=eval_items, top_k=args.top_k)

    print_report(metrics)

    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(json.dumps(metrics, indent=2), encoding="utf-8")
        print(f"\nSaved metrics to {output_path}")


if __name__ == "__main__":
    main()
