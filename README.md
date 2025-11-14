# LaTeX Chunking & Translation Pipeline

This repository provides a Python-based pipeline to process LaTeX documents for **chunking** and **translation**. It is designed to:

- Split LaTeX documents into structured chunks based on `\section`, `\subsection`, and `\subsubsection`.
- Preserve the original LaTeX commands and structure while translating the textual content.
- Reconstruct the translated chunks back into a complete `.tex` file.

This is useful for preparing LaTeX documents for multilingual publications, research paper translation, or integration with language models (LLMs) for translation or summarization tasks.

---

## Features

- **Chunking by Section**: Automatically splits LaTeX documents into sections, subsections, and subsubsections.
- **LaTeX-Preserving Translation**: Ensures that LaTeX commands, math formulas, citations, and environments remain unchanged.
- **JSON Output**: Chunks are saved in JSON format for easy processing.
- **Reconstruction**: Translated chunks can be merged back into a full LaTeX file.
- **LLM-Ready**: Prepared for translation using any LLM API (OpenAI, HuggingFace, etc.).

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/latex-chunk-translation.git
cd latex-chunk-translation
