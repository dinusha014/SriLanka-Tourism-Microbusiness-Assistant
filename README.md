# Sri Lanka Tourism Micro-Business Assistant

## 📖 Project Description

Sri Lanka Tourism Micro-Business Assistant is an AI-powered web application developed to help tourists plan their trips across Sri Lanka. The system uses a multi-agent architecture built with **LangGraph** and **Retrieval-Augmented Generation (RAG)** to answer tourism-related questions, generate travel itineraries, provide accommodation suggestions, and estimate travel budgets.

The application retrieves relevant information from a FAISS vector database created from Sri Lankan tourism documents and generates accurate responses using Large Language Models.

---

#  Architecture Diagram

![System Architecture](diagrams/architecture.png)

### Architecture Overview

The system consists of the following components:

- Streamlit User Interface
- LangGraph Supervisor
- RAG Agent
- Planner Agent
- Booking Agent
- Budget Agent
- FAISS Vector Database
- HuggingFace Embedding Model
- Groq & OpenRouter Language Models

The Streamlit application receives user requests, the LangGraph supervisor routes them to the appropriate AI agents, and the responses are generated using the tourism knowledge base.

---

#  Setup Instructions

## 1. Clone the repository

```bash
git clone https://github.com/dinusha014/SriLanka-Tourism-Microbusiness-Assistant
```

## 2. Move into the project

```bash
cd SriLanka-Tourism-Microbusiness-Assistant
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 4. Configure environment variables

Create a `.env` file and add:

```env
GROQ_API_KEY=your_groq_api_key
OPENROUTER_API_KEY=your_openrouter_api_key
```

## 5. Build the vector database

```bash
python build_vectorstore.py
```

## 6. Run the application

```bash
streamlit run app.py
```

---

#  Model Choice Comparison

| Model / Tool | Purpose | Reason for Selection |
|---------------|---------|----------------------|
| Groq | Tourism question answering | Fast inference and high-quality responses |
| OpenRouter | Planner, Booking and Budget agents | Provides access to multiple LLMs through one API |
| HuggingFace Embeddings | Text embeddings | Converts tourism documents into vector representations |
| FAISS | Vector database | Fast semantic similarity search for RAG |

---

#  Agent Communication Diagram

![Agent Communication](diagrams/agent_workflow.png)

### Agent Communication Flow

```
User
   │
   ▼
Streamlit UI
   │
   ▼
LangGraph Supervisor
   │
   ├──────────────┐
   ▼              ▼
RAG Agent    Planner Agent
                    │
                    ▼
            Booking Agent
                    │
                    ▼
             Budget Agent
                    │
                    ▼
            Final AI Response
```

The LangGraph Supervisor analyses the user query and routes it to the appropriate specialised agent. The selected agents process the request and their responses are combined before being returned to the user.

---

#  RAG Pipeline Explanation

![RAG Pipeline](diagrams/rag_workflow.png)

The application follows a Retrieval-Augmented Generation (RAG) pipeline:

1. Tourism PDF documents are collected.
2. Documents are divided into smaller text chunks.
3. HuggingFace Embeddings convert the text into vectors.
4. FAISS stores the vector embeddings.
5. The retriever searches for the most relevant document chunks.
6. The retrieved context is sent to the Large Language Model.
7. The model generates a response using only the retrieved tourism information.

This approach improves response accuracy and reduces hallucinations by grounding answers in the project's tourism knowledge base.

---

# 🌐 Live Streamlit Demo

**Live Application**

https://srilanka-tourism-microbusiness-assistant-jlkskudoaws2g46u9f948.streamlit.app/

**GitHub Repository**

https://github.com/dinusha014/SriLanka-Tourism-Microbusiness-Assistant

---

# ⚠️ Known Limitations

- Supports only tourism-related queries.
- Responses depend on the available tourism documents.
- No real-time hotel or flight booking integration.
- Weather information is not available.
- Internet connection is required for LLM APIs.
- Budget estimates are approximate and may differ from actual travel costs.
