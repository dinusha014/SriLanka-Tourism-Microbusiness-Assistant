# 🇱🇰 Sri Lanka Tourism Micro-Business Assistant

An Agentic AI web application built using LangGraph, Retrieval-Augmented Generation (RAG), FAISS, Streamlit, OpenRouter and Groq.

---

## Features

- AI Tourism Assistant
- Trip Planner Agent
- Booking Assistant Agent
- Budget Advisor Agent
- RAG Knowledge Base
- LangGraph Multi-Agent Workflow
- Streamlit Chat Interface

---

## Technologies

- Python
- LangGraph
- LangChain
- FAISS
- Streamlit
- Groq
- OpenRouter
- HuggingFace Embeddings

---

## Folder Structure

```
project/

│

├── agents/

├── utils/

├── data/

│ └── pdfs/

├── vectorstore/

├── app.py

├── build_vectorstore.py

├── requirements.txt

├── README.md

└── .env.example
```

---

## AI Agents

### RAG Agent

Answers tourism questions using the knowledge base.

### Planner Agent

Creates travel itineraries.

### Booking Agent

Provides hotel and transport recommendations.

### Budget Agent

Estimates travel costs.

---

## RAG Workflow

PDF Documents

↓

Text Chunking

↓

Embeddings

↓

FAISS Vector Database

↓

Retriever

↓

LLM

↓

Answer

---

## LangGraph Workflow

User

↓

Supervisor

↓

RAG

↓

Planner

↓

Booking

↓

Budget

↓

Final Response

---

## Installation

Install dependencies

```
pip install -r requirements.txt
```

Build Vector Database

```
python build_vectorstore.py
```

Run Application

```
streamlit run app.py
```

---

## Models

Groq

OpenRouter

---

## Diagrams 

## System Architecture

![System Architecture](diagrams/architecture.png)

---

## Agent Workflow

![Agent Workflow](diagrams/agent_workflow.png)

---

## RAG Workflow

![RAG Workflow](diagrams/rag_workflow.png)

## Author

Chamod Dinusha

BSc Information Technology

Horizon Campus