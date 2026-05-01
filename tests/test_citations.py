from src.citations import citation_label, format_sources


def test_citation_label_uses_title_and_section():
    chunk = {
        "title": "Expense Reimbursement Policy",
        "section": "EX-3 Submission Deadline",
    }

    assert citation_label(chunk, 1) == "[1] Expense Reimbursement Policy - EX-3 Submission Deadline"


def test_format_sources_returns_traceable_metadata():
    chunks = [
        {
            "title": "Remote Work Policy",
            "section": "RW-3 Core Collaboration Hours",
            "source": "data/policies/remote_work_policy.md",
            "score": 0.91,
        }
    ]

    sources = format_sources(chunks)

    assert sources[0]["citation"] == "[1]"
    assert sources[0]["title"] == "Remote Work Policy"
    assert sources[0]["section"] == "RW-3 Core Collaboration Hours"
    assert sources[0]["source"] == "data/policies/remote_work_policy.md"
    assert sources[0]["score"] == 0.91
