# Tourism Knowledge Base

This directory contains tourism-related documents used by the Retrieval-Augmented Generation (RAG) pipeline.

## Document Categories

- Tourist attractions
- Heritage sites
- National parks
- Hotels and accommodation
- Transportation
- Local food
- Cultural experiences

## Usage

These PDF documents are processed using:

- LangChain
- HuggingFace Embeddings
- FAISS Vector Database

To rebuild the vector database:

```bash
python build_vectorstore.py
```
