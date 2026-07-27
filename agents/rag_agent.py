from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate

from utils.embeddings import get_embeddings
from utils.llm import get_groq_llm


class RAGAgent:
    """
    Retrieval-Augmented Generation (RAG) Agent

    This agent retrieves relevant tourism information from the FAISS
    vector database and generates accurate answers using the Groq LLM.
    """

    def __init__(self):

        # Load embedding model
        self.embeddings = get_embeddings()

        # Load FAISS vector database
        self.vectorstore = FAISS.load_local(
            "vectorstore",
            self.embeddings,
            allow_dangerous_deserialization=True
        )

        # Create retriever
        self.retriever = self.vectorstore.as_retriever(
            search_kwargs={"k": 4}
        )

        # Load Groq LLM
        self.llm = get_groq_llm()

    def get_context(self, question):
        """
        Retrieve relevant tourism documents from the vector database.
        """

        docs = self.retriever.invoke(question)

        context = "\n\n".join(
            doc.page_content for doc in docs
        )

        return context

    def answer_question(self, question):
        """
        Generate a tourism-related answer using retrieved context.
        """

        context = self.get_context(question)

        # Return a friendly message if no relevant context is found.
        if not context.strip():
            return (
                "I couldn't find relevant information in the tourism knowledge base "
                "to answer your question."
            )

        prompt = ChatPromptTemplate.from_template(
            """
You are an AI Tourism Assistant specialising in Sri Lanka.

Your responsibilities are:

- Answer only tourism-related questions.
- Use ONLY the retrieved context below.
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

        # Generate a context-aware answer using retrieved tourism documents.
        chain = prompt | self.llm

        try:

            response = chain.invoke(
                {
                    "context": context,
                    "question": question
                }
            )

            return response.content

        # Handle unexpected runtime errors gracefully.
        except Exception as e:

            return (
                f"An error occurred while processing your request: {str(e)}"
            )