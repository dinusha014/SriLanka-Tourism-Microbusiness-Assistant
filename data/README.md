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
## Project Folder Structure

```
SriLanka-Tourism/
│
├── agents/
├── data/
├── diagrams/
├── images/
├── pages/
├── utils/
├── vectorstore/
├── app.py
├── build_vectorstore.py
├── README.md
└── requirements.txt
```
## Data Sources

The tourism knowledge base was created using publicly available Sri Lankan tourism information.

Example sources include:

- Sri Lanka Tourism Development Authority
- Department of Wildlife Conservation
- National Museum information
- Public tourism brochures
