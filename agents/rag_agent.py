from pathlib import Path

from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate

from utils.embeddings import get_embeddings
from utils.llm import get_groq_llm


class RAGAgent:
    """
    Retrieval-Augmented Generation (RAG) Agent.

    This agent retrieves relevant Sri Lankan tourism information
    from the FAISS vector database and generates answers using Groq.
    """

    def __init__(self):

        # Find the project root folder.
        # rag_agent.py is inside the agents folder, so parent.parent
        # points to the main project folder.
        project_root = Path(__file__).resolve().parent.parent

        # Create the complete vectorstore folder path.
        vectorstore_path = project_root / "vectorstore"

        # Check whether the required FAISS files exist.
        index_file = vectorstore_path / "index.faiss"
        pickle_file = vectorstore_path / "index.pkl"

        if not index_file.exists() or not pickle_file.exists():
            raise FileNotFoundError(
                "FAISS vector database files were not found. "
                f"Expected files:\n"
                f"- {index_file}\n"
                f"- {pickle_file}\n"
                "Run build_vectorstore.py and push the vectorstore folder "
                "to the GitHub main branch."
            )

        # Load embedding model.
        self.embeddings = get_embeddings()

        # Load FAISS vector database using the absolute project path.
        self.vectorstore = FAISS.load_local(
            str(vectorstore_path),
            self.embeddings,
            allow_dangerous_deserialization=True
        )

        # Create retriever.
        self.retriever = self.vectorstore.as_retriever(
            search_kwargs={"k": 4}
        )

        # Load Groq LLM.
        self.llm = get_groq_llm()

    def get_context(self, question: str) -> str:
        """
        Retrieve relevant tourism documents from the vector database.
        """

        docs = self.retriever.invoke(question)

        context = "\n\n".join(
            doc.page_content for doc in docs
        )

        return context

    def answer_question(self, question: str) -> str:
        """
        Generate a tourism-related answer using retrieved context.
        """

        context = self.get_context(question)

        # Return a friendly message if no relevant context is found.
        if not context.strip():
            return (
                "I couldn't find relevant information in the tourism "
                "knowledge base to answer your question."
            )

        prompt = ChatPromptTemplate.from_template(
            """
You are an AI Tourism Assistant specialising in Sri Lanka.

Your responsibilities are:

- Answer only tourism-related questions.
- Use only the retrieved context below.
- Never invent information.
- If the answer is unavailable, clearly say you do not have enough information.
- Provide concise, professional and helpful responses.
- Use bullet points whenever appropriate.

Context:
{context}

Question:
{question}
"""
        )

        # Create the RAG chain.
        chain = prompt | self.llm

        try:
            response = chain.invoke(
                {
                    "context": context,
                    "question": question
                }
            )

            return response.content

        except Exception as error:
            return (
                "An error occurred while processing your request: "
                f"{str(error)}"
            )