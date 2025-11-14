import json
from openai import OpenAI

client = OpenAI(
    api_key="2a246e6202904b0a936cb6c06a1451b3.GeQLbprjUGiWApDr",
    base_url="https://api.z.ai/api/paas/v4/"
)

TRANSLATION_PROMPT = """
You are a LaTeX-preserving translation model.
Translate ONLY natural language content into Indonesian.
Do NOT change or translate any LaTeX commands, environments, math, citations, labels, or symbols.


Rules:
- Keep LaTeX commands EXACTLY the same.
- If a command contains text (e.g., \section{Introduction}), translate ONLY the text inside the braces.
- Do NOT translate math expressions ($...$).
- Preserve spacing and structure.
Return only the translated LaTeX.
"""

def translate_chunk(content: str) -> str:
    response = client.chat.completions.create(
        model="glm-4.5-Flash",
        messages=[
            {"role": "system", "content": TRANSLATION_PROMPT},
            {"role": "user", "content": content}
        ],
        temperature=0
        )
    return response.choices[0].message.content

def translate_chunks(input_file="latex_chunks.json",
                     output_file="latex_chunks_translated.json"):

    with open(input_file, "r", encoding="utf-8") as f:
        chunks = json.load(f)

    translated = []
    
    for chunk in chunks:
        for i in range(3):
            if chunk["id"] == i + 1:
                print(f"🔄 Translating: {chunk['level']} - {chunk['title']}")
                t_content = translate_chunk(chunk["content"])
        
                translated.append({
                    "id": chunk["id"],
                    "level": chunk["level"],
                    "title": chunk["title"],
                    "translated_content": t_content
                })

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(translated, f, ensure_ascii=False, indent=2)

    print(f"✅ Translation complete → saved at {output_file}")


if __name__ == "__main__":
    input_path = "latex_chunks_persection.json"
    output_path = "latex_chunks_translated.json"
    translate_chunks(input_file=input_path, output_file=output_path)