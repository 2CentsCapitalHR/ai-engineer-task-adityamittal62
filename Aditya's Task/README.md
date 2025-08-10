# ADGM Corporate Agent

A document review system that:
- Parses `.docx` corporate documents
- Detects document types (AoA, MoA, Board Resolution, etc.)
- Runs rule-based & AI checks against ADGM standards
- Inserts comments into `.docx` files
- Outputs a JSON compliance report
- Uses RAG (Retrieval-Augmented Generation) with ADGM reference docs

## Quick Start

```bash
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
.\.venv\Scripts\activate   # Windows

pip install -r requirements.txt

# (Optional) Set OpenAI API key
export OPENAI_API_KEY="sk-..."
export USE_OPENAI_EMBEDDINGS=1

# Download ADGM reference docs
python download_adgm_refs.py

# Download model
python download_model.py

# Ingest reference docs for RAG
python rag.py --ingest ./adgm_corpus --persist ./db

# Run the Gradio app
python app.py



CREATED BY ADITYA MITTAL
ADI