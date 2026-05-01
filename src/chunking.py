from pathlib import Path
from typing import Dict, List


def load_policy_documents(policy_dir: str = "data/policies") -> List[Dict[str, str]]:
    documents = []

    for path in sorted(Path(policy_dir).glob("*.md")):
        text = path.read_text(encoding="utf-8")
        title = "Untitled Policy"

        for line in text.splitlines():
            if line.startswith("# "):
                title = line.replace("# ", "").strip()
                break

        documents.append(
            {
                "doc_id": path.stem,
                "title": title,
                "source": str(path),
                "text": text,
            }
        )

    return documents


def chunk_policy_documents(documents: List[Dict[str, str]]) -> List[Dict[str, str]]:
    chunks = []

    for doc in documents:
        current_section = doc["title"]
        current_lines = []

        for line in doc["text"].splitlines():
            if line.startswith("## "):
                if current_lines:
                    chunks.append(
                        {
                            "doc_id": doc["doc_id"],
                            "title": doc["title"],
                            "section": current_section,
                            "source": doc["source"],
                            "text": "\n".join(current_lines).strip(),
                        }
                    )
                    current_lines = []

                current_section = line.replace("## ", "").strip()
                current_lines.append(line)
            else:
                if line.strip():
                    current_lines.append(line)

        if current_lines:
            chunks.append(
                {
                    "doc_id": doc["doc_id"],
                    "title": doc["title"],
                    "section": current_section,
                    "source": doc["source"],
                    "text": "\n".join(current_lines).strip(),
                }
            )

    return chunks
