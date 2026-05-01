SAMPLE_QUESTIONS = [
    "What is the deadline for submitting an expense report?",
    "When must security incidents be reported?",
    "What are the core collaboration hours for remote employees?",
    "Which systems require multi-factor authentication?",
    "Are personal devices allowed for regular remote work?",
    "What is the company stock price?",
]


def confidence_label(score: float) -> str:
    if score >= 0.30:
        return "High"
    if score >= 0.10:
        return "Medium"
    return "Low"
