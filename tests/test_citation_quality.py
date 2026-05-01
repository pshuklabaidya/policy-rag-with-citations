import re

from scripts.evaluate_retrieval import load_eval_questions
from src.rag_pipeline import PolicyRAGPipeline


def test_supported_eval_answers_include_bracketed_citation():
    pipeline = PolicyRAGPipeline()
    eval_items = load_eval_questions("data/eval/eval_questions.json")

    for item in eval_items:
        result = pipeline.answer(
            query=item["question"],
            top_k=3,
            min_score=0.05,
        )

        assert re.search(r"\[\d+\]", result["answer"])
        assert result["sources"]
        assert result["sources"][0]["citation"] == "[1]"


def test_supported_eval_answers_use_expected_top_source():
    pipeline = PolicyRAGPipeline()
    eval_items = load_eval_questions("data/eval/eval_questions.json")

    for item in eval_items:
        result = pipeline.answer(
            query=item["question"],
            top_k=3,
            min_score=0.05,
        )

        top_source = result["sources"][0]
        predicted_source = f"{top_source['title']} - {top_source['section']}"

        assert predicted_source == item["expected_source"]


def test_unsupported_answer_does_not_fabricate_policy_detail():
    pipeline = PolicyRAGPipeline()

    result = pipeline.answer(
        query="What is the company stock price?",
        top_k=3,
        min_score=0.50,
    )

    assert "do not contain enough relevant evidence" in result["answer"]
    assert "stock price is" not in result["answer"].lower()
