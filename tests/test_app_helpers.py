from src.app_utils import SAMPLE_QUESTIONS, confidence_label


def test_confidence_label_high():
    assert confidence_label(0.30) == "High"


def test_confidence_label_medium():
    assert confidence_label(0.10) == "Medium"


def test_confidence_label_low():
    assert confidence_label(0.01) == "Low"


def test_sample_questions_include_supported_and_unsupported_examples():
    assert "What is the deadline for submitting an expense report?" in SAMPLE_QUESTIONS
    assert "What is the company stock price?" in SAMPLE_QUESTIONS
