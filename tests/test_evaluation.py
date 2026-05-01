from scripts.evaluate_retrieval import evaluate_items, load_eval_questions


def test_retrieval_eval_questions_load_successfully():
    eval_items = load_eval_questions("data/eval/eval_questions.json")

    assert len(eval_items) >= 5
    assert "question" in eval_items[0]
    assert "expected_source" in eval_items[0]


def test_retrieval_eval_reaches_full_accuracy_on_baseline_questions():
    eval_items = load_eval_questions("data/eval/eval_questions.json")
    metrics = evaluate_items(eval_items=eval_items, top_k=3)

    assert metrics["total_questions"] == len(eval_items)
    assert metrics["top_1_accuracy"] == 1.0
    assert all(item["passed"] for item in metrics["results"])
