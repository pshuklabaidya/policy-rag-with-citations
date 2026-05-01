from src.rag_pipeline import PolicyRAGPipeline


def test_pipeline_answers_supported_policy_question_with_citation():
    pipeline = PolicyRAGPipeline()

    result = pipeline.answer(
        query="What is the deadline for submitting an expense report?",
        top_k=3,
        min_score=0.05,
    )

    assert "30 days" in result["answer"]
    assert "[1]" in result["answer"]
    assert result["sources"][0]["title"] == "Expense Reimbursement Policy"
    assert result["sources"][0]["section"] == "EX-3 Submission Deadline"


def test_pipeline_abstains_on_unsupported_question():
    pipeline = PolicyRAGPipeline()

    result = pipeline.answer(
        query="What is the company stock price?",
        top_k=3,
        min_score=0.50,
    )

    assert "do not contain enough relevant evidence" in result["answer"]
