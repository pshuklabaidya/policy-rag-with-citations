from src.citations import answer_from_retrieved_context


def test_answer_abstains_when_no_chunks_are_available():
    answer = answer_from_retrieved_context(
        query="What is the company stock price?",
        chunks=[],
    )

    assert "cannot be answered" in answer


def test_answer_abstains_when_retrieval_score_is_too_low():
    chunks = [
        {
            "title": "Remote Work Policy",
            "section": "RW-1 Eligibility",
            "source": "data/policies/remote_work_policy.md",
            "text": "Full-time employees may request remote work eligibility after 90 days.",
            "score": 0.0,
        }
    ]

    answer = answer_from_retrieved_context(
        query="What is the company stock price?",
        chunks=chunks,
        min_score=0.05,
    )

    assert "do not contain enough relevant evidence" in answer


def test_answer_includes_citation_when_score_is_sufficient():
    chunks = [
        {
            "title": "Expense Reimbursement Policy",
            "section": "EX-3 Submission Deadline",
            "source": "data/policies/expense_policy.md",
            "text": "## EX-3 Submission Deadline\nExpense reports must be submitted within 30 days.",
            "score": 0.42,
        }
    ]

    answer = answer_from_retrieved_context(
        query="What is the expense submission deadline?",
        chunks=chunks,
        min_score=0.05,
    )

    assert "30 days" in answer
    assert "[1]" in answer
    assert "Expense Reimbursement Policy" in answer
