import json
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT_DIR))

from scripts.evaluate_retrieval import evaluate_items, load_eval_questions
from scripts.profile_corpus import build_corpus_profile
from src.rag_pipeline import PolicyRAGPipeline


REQUIRED_PATHS = [
    "README.md",
    "Makefile",
    "requirements.txt",
    "pytest.ini",
    ".github/workflows/ci.yml",
    "app/streamlit_app.py",
    "src/app_utils.py",
    "src/chunking.py",
    "src/citations.py",
    "src/rag_pipeline.py",
    "src/retrieval.py",
    "scripts/query_policy.py",
    "scripts/evaluate_retrieval.py",
    "scripts/generate_demo_outputs.py",
    "scripts/profile_corpus.py",
    "docs/architecture.md",
    "docs/data_dictionary.md",
    "docs/demo_questions.md",
    "docs/project_summary.md",
    "data/policies/remote_work_policy.md",
    "data/policies/expense_policy.md",
    "data/policies/security_policy.md",
    "data/eval/eval_questions.json",
    "reports/retrieval_eval.json",
    "reports/demo_outputs.md",
    "reports/corpus_profile.json",
]


def check_required_paths() -> list[str]:
    errors = []

    for path in REQUIRED_PATHS:
        if not Path(path).exists():
            errors.append(f"Missing required path: {path}")

    return errors


def check_pipeline_behavior() -> list[str]:
    errors = []
    pipeline = PolicyRAGPipeline()

    supported = pipeline.answer(
        query="What is the deadline for submitting an expense report?",
        top_k=3,
        min_score=0.05,
    )

    if "30 days" not in supported["answer"]:
        errors.append("Supported query did not return expected deadline detail.")

    if "[1]" not in supported["answer"]:
        errors.append("Supported query did not include bracketed citation.")

    if supported["sources"][0]["section"] != "EX-3 Submission Deadline":
        errors.append("Supported query did not retrieve the expected top section.")

    unsupported = pipeline.answer(
        query="What is the company stock price?",
        top_k=3,
        min_score=0.50,
    )

    if "do not contain enough relevant evidence" not in unsupported["answer"]:
        errors.append("Unsupported query did not trigger abstention behavior.")

    return errors


def check_retrieval_eval() -> list[str]:
    errors = []
    eval_items = load_eval_questions("data/eval/eval_questions.json")
    metrics = evaluate_items(eval_items=eval_items, top_k=3)

    if metrics["top_1_accuracy"] != 1.0:
        errors.append(
            f"Retrieval evaluation accuracy expected 1.0 but got {metrics['top_1_accuracy']}"
        )

    report_path = Path("reports/retrieval_eval.json")
    if report_path.exists():
        saved_metrics = json.loads(report_path.read_text(encoding="utf-8"))
        if saved_metrics.get("top_1_accuracy") != 1.0:
            errors.append("Saved retrieval evaluation report is not at 100% top-1 accuracy.")

    return errors


def check_corpus_profile() -> list[str]:
    errors = []
    profile = build_corpus_profile("data/policies")

    if profile["document_count"] != 3:
        errors.append("Corpus profile should contain exactly 3 policy documents.")

    if profile["chunk_count"] < 15:
        errors.append("Corpus profile should contain at least 15 policy chunks.")

    return errors


def main():
    checks = {
        "required_paths": check_required_paths,
        "pipeline_behavior": check_pipeline_behavior,
        "retrieval_eval": check_retrieval_eval,
        "corpus_profile": check_corpus_profile,
    }

    all_errors = []

    print("Project Health Check")
    print("=" * 40)

    for name, check_fn in checks.items():
        errors = check_fn()

        if errors:
            print(f"FAIL: {name}")
            all_errors.extend(errors)
            for error in errors:
                print(f"  - {error}")
        else:
            print(f"PASS: {name}")

    if all_errors:
        print("\nHealth check failed.")
        raise SystemExit(1)

    print("\nHealth check passed.")


if __name__ == "__main__":
    main()
