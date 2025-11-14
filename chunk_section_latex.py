## code for chunk latex per section -> subsection -> subsubsection
import re
import json
from pathlib import Path

# Regex pattern untuk semua level
PATTERN = r'(\\section\{(.+?)\}|\\subsection\{(.+?)\}|\\subsubsection\{(.+?)\})'

def chunk_latex_by_levels(text: str):
    """
    Memecah LaTeX menjadi chunk per section, subsection, dan subsubsection.
    """

    chunks = []
    matches = list(re.finditer(PATTERN, text))

    for i, match in enumerate(matches):
        full_cmd = match.group(1)

        # Tentukan level
        if full_cmd.startswith(r"\section"):
            level = "section"
            title = match.group(2)
        elif full_cmd.startswith(r"\subsection"):
            level = "subsection"
            title = match.group(3)
        else:
            level = "subsubsection"
            title = match.group(4)

        start = match.start()

        # Tentukan akhir chunk
        if i < len(matches) - 1:
            end = matches[i + 1].start()
        else:
            end = len(text)

        content = text[start:end].strip()

        chunks.append({
            "id": len(chunks) + 1,
            "level": level,
            "title": title,
            "content": content
        })

    return chunks


def process_latex_to_json(file_path: str, output_path="latex_chunks.json"):
    text = Path(file_path).read_text(encoding="utf-8")
    chunks = chunk_latex_by_levels(text)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(chunks, f, ensure_ascii=False, indent=2)

    print(f"✅ {len(chunks)} chunks (section / subsection / subsubsection) disimpan ke {output_path}")


if __name__ == "__main__":
    path = "arXiv-2511.08585v1/main.tex"
    process_latex_to_json(path, output_path="latex_chunks_persection.json")
