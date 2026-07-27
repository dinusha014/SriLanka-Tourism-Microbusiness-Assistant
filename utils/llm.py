import os

from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI

load_dotenv()


def get_groq_llm():

    return ChatGroq(

        model="llama-3.3-70b-versatile",

        temperature=0.3,

        groq_api_key=os.getenv("GROQ_API_KEY")

    )


def get_openrouter_llm():

    return ChatOpenAI(

        model="qwen/qwen3-32b",

        temperature=0.3,

        api_key=os.getenv("OPENROUTER_API_KEY"),

        base_url="https://openrouter.ai/api/v1"

    )