import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT_DIR))

from src.rag_pipeline import PolicyRAGPipeline


DEMO_QUESTIONS = [
    {
        "question": "What is the deadline for submitting an expense report?",
        "min_score": 0.05,
    },
    {
        "question": "When must security incidents be reported?",
        "min_score": 0.05,
    },
    {
        "question": "What are the core collaboration hours for remote employees?",
        "min_score": 0.05,
    },
    {
        "question": "Which systems require multi-factor authentication?",
        "min_score": 0.05,
    },
    {
        "question": "What is the company stock price?",
        "min_score": 0.50,
    },
]


def format_demo_result(question: str, result: dict) -> str:
    lines = []
    lines.append(f"## Question: {question}")
    lines.append("")
    lines.append("### Answer")
    lines.append("")
    lines.append(result["answer"])
    lines.append("")
    lines.append("### Sources")
    lines.append("")
    lines.append("| Citation | Policy | Section | Score | Source |")
    lines.append("|---|---|---|---:|---|")

    for source in result["sources"]:
        lines.append(
            "| {citation} | {title} | {section} | {score} | {source_path} |".format(
                citation=source["citation"],
                title=source["title"],
                section=source["section"],
                score=source["score"],
                source_path=source["source"],
            )
        )

    lines.append("")
    return "\n".join(lines)


def main():
    pipeline = PolicyRAGPipeline()

    output_lines = [
        "# Policy RAG Demo Outputs",
        "",
        "Generated examples for supported and unsupported policy questions.",
        "",
        "All policy data is synthetic and used for portfolio demonstration only.",
        "",
    ]

    for item in DEMO_QUESTIONS:
        result = pipeline.answer(
            query=item["question"],
            top_k=3,
            min_score=item["min_score"],
        )
        output_lines.append(format_demo_result(item["question"], result))

    output_path = Path("reports/demo_outputs.md")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(output_lines), encoding="utf-8")

    print(f"Saved demo outputs to {output_path}")


if __name__ == "__main__":
    main()
