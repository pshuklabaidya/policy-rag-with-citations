from typing import Dict, List


def citation_label(chunk: Dict[str, str], number: int) -> str:
    return f"[{number}] {chunk['title']} - {chunk['section']}"


def format_context_with_citations(chunks: List[Dict[str, str]]) -> str:
    context_blocks = []

    for index, chunk in enumerate(chunks, start=1):
        label = citation_label(chunk, index)
        context_blocks.append(f"{label}\n{chunk['text']}")

    return "\n\n".join(context_blocks)


def format_sources(chunks: List[Dict[str, str]]) -> List[Dict[str, str]]:
    sources = []

    for index, chunk in enumerate(chunks, start=1):
        sources.append(
            {
                "citation": f"[{index}]",
                "title": chunk["title"],
                "section": chunk["section"],
                "source": chunk["source"],
                "score": round(float(chunk.get("score", 0.0)), 4),
            }
        )

    return sources


def clean_policy_text(text: str) -> str:
    lines = []

    for line in text.splitlines():
        stripped = line.strip()

        if not stripped:
            continue

        if stripped.startswith("#"):
            continue

        if stripped.lower().startswith("synthetic document"):
            continue

        lines.append(stripped)

    return " ".join(lines)


def answer_from_retrieved_context(
    query: str,
    chunks: List[Dict[str, str]],
    min_score: float = 0.05,
) -> str:
    if not chunks:
        return (
            "No relevant policy evidence was retrieved. "
            "The question cannot be answered from the available policy documents."
        )

    strongest = chunks[0]
    strongest_score = float(strongest.get("score", 0.0))

    if strongest_score < min_score:
        return (
            "The available policy documents do not contain enough relevant evidence "
            "to answer this question with a citation-grounded response."
        )

    strongest_text = clean_policy_text(strongest["text"])

    answer = (
        f"{strongest_text} [1] "
        f"This answer is grounded in {strongest['title']}, section {strongest['section']}."
    )

    supporting_chunks = [
        chunk for chunk in chunks[1:]
        if float(chunk.get("score", 0.0)) >= min_score
    ]

    if supporting_chunks:
        supporting_refs = ", ".join(
            f"[{index}]"
            for index, chunk in enumerate(chunks[1:], start=2)
            if float(chunk.get("score", 0.0)) >= min_score
        )
        answer += f" Supporting retrieved sections: {supporting_refs}."

    return answer
