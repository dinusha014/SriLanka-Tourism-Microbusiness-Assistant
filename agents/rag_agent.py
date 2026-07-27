from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate

from utils.embeddings import get_embeddings
from utils.llm import get_groq_llm


class RAGAgent:

    def __init__(self):

        self.embeddings = get_embeddings()

        self.vectorstore = FAISS.load_local(
            "vectorstore",
            self.embeddings,
            allow_dangerous_deserialization=True
        )

        self.retriever = self.vectorstore.as_retriever(
            search_kwargs={"k": 4}
        )

        self.llm = get_groq_llm()

    def answer_question(self, question):

        docs = self.retriever.invoke(question)

        context = "\n\n".join(
            doc.page_content for doc in docs
        )
    def get_context(self, question):

        docs = self.retriever.invoke(question)

        context = "\n\n".join(
            doc.page_content for doc in docs
        )

        return context

        prompt = ChatPromptTemplate.from_template(
            """
You are an AI Tourism Assistant specialising in Sri Lanka.

Your responsibilities are:

- Answer only tourism-related questions.
- Use the retrieved context as the primary source.
- If the answer is not found in the context, clearly state that the information is unavailable.
- Never invent facts or make assumptions.
- Provide concise, helpful, and accurate responses.
- Use bullet points when listing attractions or recommendations.

Answer only using the information provided below.
# Generate a context-aware answer using retrieved tourism documents.
If the answer is not available, say:
"I couldn't find that information in the tourism knowledge base."

Context:
{context}

Question:
{question}
"""
        )

        chain = prompt | self.llm

        response = chain.invoke(
            {
                "context": context,
                "question": question
            }
        )

        return response.content