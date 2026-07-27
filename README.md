# 🇱🇰 Sri Lanka Tourism Micro-Business Assistant

An Agentic AI web application built using LangGraph, Retrieval-Augmented Generation (RAG), FAISS, Streamlit, OpenRouter and Groq.

---

## Project Overview

Sri Lanka Tourism Micro-Business Assistant is an AI-powered tourism assistant built using LangGraph and Retrieval-Augmented Generation (RAG). The application helps tourists plan trips, estimate budgets, discover attractions, and receive context-aware answers from a tourism knowledge base created from Sri Lankan tourism documents.

### Key Features

- AI-powered tourism question answering
- Personalised trip planning
- Hotel recommendations
- Budget estimation
- Retrieval-Augmented Generation (RAG)
- LangGraph multi-agent workflow
- Streamlit web interface

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


## Building the Vector Database

Run the following command to create the FAISS vector database.

```bash
python build_vectorstore.py
```

This command loads all tourism documents,
creates embeddings,
and stores them in the local vector database.

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


## Project Branding

The application includes custom tourism branding assets:

- Application Logo
- Hero Banner
- Sigiriya
- Ella
- Mirissa
- Yala National Park

These assets improve the visual experience of the application and provide a tourism-focused user interface.

## Author

Chamod Dinusha

BSc Information Technology

Horizon Campus