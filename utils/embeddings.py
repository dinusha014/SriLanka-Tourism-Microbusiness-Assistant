"""
Embedding Utility

This module loads the embedding model used to convert tourism
documents into vector embeddings for Retrieval-Augmented Generation (RAG).

Model:
BAAI/bge-small-en-v1.5
"""


from langchain_community.embeddings import HuggingFaceEmbeddings

# Load HuggingFace embedding model for semantic search
def get_embeddings():
# Return embedding model instance
    return HuggingFaceEmbeddings(
        model_name="BAAI/bge-small-en-v1.5",
        model_kwargs={"device": "cpu"},
        encode_kwargs={"normalize_embeddings": True}
    )