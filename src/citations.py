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


def answer_from_retrieved_context(query: str, chunks: List[Dict[str, str]]) -> str:
    if not chunks:
        return "No relevant policy evidence was retrieved."

    strongest = chunks[0]
    section = strongest["section"]
    title = strongest["title"]

    answer = (
        f"The most relevant policy evidence is found in {title}, section {section} [1]. "
        f"Based on that section, {strongest['text'].replace(chr(10), ' ')}"
    )

    if len(chunks) > 1:
        answer += " Additional supporting policy sections are listed in the retrieved sources."

    return answer
