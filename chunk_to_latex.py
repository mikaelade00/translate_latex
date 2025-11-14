import json

def reconstruct_latex(chunks):
    """Reconstruct the full LaTeX document from chunk list (already translated)."""
    latex_lines = []

    for item in chunks:
        level = item["level"]
        title = item["title"]
        content = item["translated_content"]

        # Rebuild LaTeX structure
        if level == "section":
            latex_lines.append(f"\\section{{{title}}}\n")
        elif level == "subsection":
            latex_lines.append(f"\\subsection{{{title}}}\n")
        elif level == "subsubsection":
            latex_lines.append(f"\\subsubsection{{{title}}}\n")

        # Add content directly
        latex_lines.append(content + "\n\n")

    return "".join(latex_lines)


# --------------------------
# MAIN SCRIPT
# --------------------------
if __name__ == "__main__":
    # Load translated chunks
    input_path = "latex_chunks_translated.json"
    with open(input_path, "r", encoding="utf-8") as f:
        translated_chunks = json.load(f)

    # Rebuild LaTeX
    reconstructed = reconstruct_latex(translated_chunks)

    # Save output .tex
    output_path = "output/reconstructed_output.tex"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(reconstructed)

    print(f"LaTeX berhasil direkonstruksi: {output_path}")
