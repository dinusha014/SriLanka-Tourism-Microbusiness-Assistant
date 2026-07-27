"""
Vector Database Builder

Reads tourism PDFs,
splits documents into chunks,
creates embeddings,
stores vectors in FAISS.
"""


from langchain_community.vectorstores import FAISS

from utils.loader import load_documents
from utils.embeddings import get_embeddings

# Load all tourism documents
def main():
    print("Loading documents...")

    documents = load_documents("data/pdfs")
# Split documents into smaller chunks
    print(f"Loaded {len(documents)} document chunks.")

    print("Creating embeddings...")
# Generate vector embeddings
    embeddings = get_embeddings()

    print("Building FAISS vector store...")
# Save vector database locally
    vectorstore = FAISS.from_documents(
        documents,
        embeddings
    )

    vectorstore.save_local("vectorstore")

    print("✅ Vector database created successfully!")


if __name__ == "__main__":
    main()