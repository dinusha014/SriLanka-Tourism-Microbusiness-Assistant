import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI


# Load variables from the .env file
load_dotenv()


def get_groq_llm():
    """
    Create and return the Groq language model.
    """

    groq_api_key = os.getenv("GROQ_API_KEY")

    if not groq_api_key:
        raise ValueError(
            "GROQ_API_KEY is missing. Add it to the .env file."
        )

    return ChatGroq(
        api_key=groq_api_key,
        model="llama-3.3-70b-versatile",
        temperature=0.3
    )


def get_openrouter_llm():
    """
    Create and return an OpenRouter language model.
    """

    openrouter_api_key = os.getenv("OPENROUTER_API_KEY")

    if not openrouter_api_key:
        raise ValueError(
            "OPENROUTER_API_KEY is missing. Add it to the .env file."
        )

    return ChatOpenAI(
        api_key=openrouter_api_key,
        base_url="https://openrouter.ai/api/v1",
        model="openai/gpt-oss-20b:free",
        temperature=0.3,
        default_headers={
            "HTTP-Referer": "http://localhost:8501",
            "X-Title": "Sri Lanka Tourism Micro-Business Assistant"
        }
    )