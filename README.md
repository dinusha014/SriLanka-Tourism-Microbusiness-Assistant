# 🇱🇰 Sri Lanka Tourism Micro-Business Assistant

An Agentic AI web application built using **LangGraph**, **Retrieval-Augmented Generation (RAG)**, **FAISS**, **Streamlit**, **Groq**, and **OpenRouter** to help tourists plan their trips across Sri Lanka.

---

# 📖 Project Overview

Sri Lanka Tourism Micro-Business Assistant is an AI-powered tourism assistant designed to support travellers by providing intelligent, context-aware travel recommendations.

The application uses **Retrieval-Augmented Generation (RAG)** to retrieve information from a knowledge base built using Sri Lankan tourism documents. Multiple AI agents cooperate through **LangGraph** to answer tourism questions, create travel itineraries, estimate budgets, and recommend accommodation.

---

# ✨ Features

- 🇱🇰 AI Tourism Question Answering
- 🗺️ Smart Trip Planner
- 🏨 Hotel & Accommodation Recommendations
- 💰 Budget Estimation
- 🚗 Transport Suggestions
- 📚 Retrieval-Augmented Generation (RAG)
- 🤖 LangGraph Multi-Agent Workflow
- 💬 Streamlit Chat Interface

---

# 🧠 AI Agents

## RAG Agent
Retrieves tourism information from the FAISS knowledge base and answers user questions.

## Planner Agent
Generates personalised day-by-day travel itineraries.

## Booking Agent
Provides accommodation, transport, and booking recommendations.

## Budget Agent
Estimates travel expenses based on the user's requirements.

---

# ⚙️ Technology Stack

- Python
- Streamlit
- LangGraph
- LangChain
- FAISS
- Groq
- OpenRouter
- HuggingFace Embeddings

---

# 📂 Project Structure

```text
project/

├── agents/
│   ├── rag_agent.py
│   ├── planner_agent.py
│   ├── booking_agent.py
│   ├── budget_agent.py
│   └── graph.py
│
├── utils/
│
├── data/
│   └── pdfs/
│
├── images/
│
├── vectorstore/
│
├── diagrams/
│
├── app.py
├── build_vectorstore.py
├── requirements.txt
├── README.md
└── .env.example
```

---

# 🔄 RAG Workflow

```
PDF Documents
      │
      ▼
Text Chunking
      │
      ▼
Embeddings
      │
      ▼
FAISS Vector Database
      │
      ▼
Retriever
      │
      ▼
Large Language Model
      │
      ▼
Answer
```

---

# 🤖 LangGraph Workflow

```
User Query
      │
      ▼
Supervisor
      │
      ▼
RAG Agent
      │
      ▼
Planner Agent
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

---

# 🏗️ Building the Vector Database

Create the FAISS vector database using:

```bash
python build_vectorstore.py
```

This command:

- Loads tourism PDF documents
- Splits documents into chunks
- Creates embeddings
- Builds the FAISS vector database

---

# 🚀 Installation

## 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/SriLanka-Tourism-Microbusiness-Assistant.git
```

## 2. Install dependencies

```bash
pip install -r requirements.txt
```

## 3. Configure environment variables

Create a `.env` file based on `.env.example`.

## 4. Build the vector database

```bash
python build_vectorstore.py
```

## 5. Run the application

```bash
streamlit run app.py
```

---

# 🧩 AI Models

- Groq
- OpenRouter

---

# 🖼️ Diagrams

## System Architecture

![System Architecture](diagrams/architecture.png)

---

## Agent Workflow

![Agent Workflow](diagrams/agent_workflow.png)

---

## RAG Workflow

![RAG Workflow](diagrams/rag_workflow.png)

---

# 🎨 Project Branding

The application includes custom tourism branding assets to create an engaging user experience.

### Branding Assets

- 🇱🇰 Application Logo
- 🌅 Hero Banner
- 🏛️ Sigiriya
- 🌿 Ella
- 🐋 Mirissa
- 🐘 Yala National Park

These images enhance the application's tourism-focused interface.

---

# 📈 Future Improvements

- 🌤️ Weather Forecast Integration
- 🗺️ Google Maps Integration
- ✈️ Flight Booking APIs
- 🏨 Live Hotel Booking APIs
- 🎤 Voice Assistant
- 🌐 Sinhala & Tamil Language Support
- 📱 Mobile Responsive Improvements

---

# 👨‍💻 Author

**Chamod Dinusha**

BSc (Hons) Information Technology

Horizon Campus

---

# 🤝 Contributors

- Chamod Dinusha

---

# 📄 License

This project was developed for **academic purposes** as part of a university assignment.

---

## ⭐ If you found this project useful, consider giving it a star!