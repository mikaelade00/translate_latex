import re
import json
from pathlib import Path

def clean_latex(text: str) -> str:
    """
    Membersihkan teks dari syntax LaTeX menjadi teks biasa.
    """
    text = re.sub(r'%.*', '', text)  # komentar
    text = re.sub(r'\\begin\{.*?\}.*?\\end\{.*?\}', '', text, flags=re.DOTALL)  # environment
    text = re.sub(r'\\[a-zA-Z]+(\[[^\]]*\])?(\{[^\}]*\})?', '', text)  # command
    text = re.sub(r'\$.*?\$', '', text)  # inline math
    text = re.sub(r'\\\(.*?\\\)', '', text)
    text = re.sub(r'\\\[.*?\\\]', '', text, flags=re.DOTALL)
    text = re.sub(r'[{}\\_&^#]', ' ', text)  # simbol
    text = re.sub(r'\s+', ' ', text)  # spasi berlebih
    return text.strip()

def chunk_text(text: str, chunk_size: int = 1000, overlap: int = 100) -> list:
    """
    Membagi teks panjang menjadi beberapa chunk.
    """
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end].strip()
        if chunk:
            chunks.append({
                "id": len(chunks) + 1,
                "content": chunk
            })
        start += chunk_size - overlap
    return chunks

def process_latex_to_json(file_path: str, output_path: str = "chunks.json",
                          chunk_size: int = 1000, overlap: int = 100):
    """
    Membaca file LaTeX, membersihkan, melakukan chunking, dan menyimpan ke JSON.
    """
    text = Path(file_path).read_text(encoding="utf-8")
    cleaned = clean_latex(text)
    chunks = chunk_text(cleaned, chunk_size, overlap)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(chunks, f, ensure_ascii=False, indent=2)

    print(f"✅ Total chunks: {len(chunks)} disimpan ke {output_path}")

if __name__ == "__main__":
    # Ganti path file sesuai kebutuhan
    path = "arXiv-2511.08585v1/main.tex"
    process_latex_to_json(path, output_path="paper_chunks.json",
                          chunk_size=1000, overlap=100)
