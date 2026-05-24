# GenAI RAG Chat Assistant

A production‑style **Retrieval‑Augmented Generation (RAG)** powered Chat Assistant built with **FastAPI (Python backend)** and a simple **HTML/CSS/JavaScript frontend**.  
The assistant answers user questions by retrieving relevant context from stored documents and grounding responses with a Large Language Model (LLM).

---

## 🚀 Tech Stack

- **Backend**: Python (FastAPI)
- **Frontend**: HTML, CSS, JavaScript
- **LLM API**: OpenAI / Gemini / Claude / Mistral
- **Embeddings API**: OpenAI (text‑embedding‑3‑small or similar)
- **Vector Storage**: FAISS / ChromaDB / SQLite (configurable)
- **RAG Pipeline**: Document ingestion → Embeddings → Vector similarity search → Context injection → LLM response
- **Conversation Memory**: Short history (last 5 turns)

---

## 🏗️ Architecture

```mermaid
flowchart TD
    A[User Query] --> B[Frontend (HTML/JS)]
    B --> C[FastAPI Backend]
    C --> D[Embeddings API]
    D --> E[Vector Store (FAISS/ChromaDB)]
    E --> F[Relevant

genai-rag-assistant/
│── backend/
│   ├── main.py              # FastAPI server
│   ├── rag_pipeline.py      # RAG logic
│   ├── vector_store.py      # FAISS/ChromaDB wrapper
│   ├── models.py            # Pydantic schemas
│   └── requirements.txt
│
│── frontend/
│   ├── index.html           # Chat UI
│   ├── style.css            # Styling
│   └── app.js               # API calls
│
└── README.md

git clone https://github.com/your-username/genai-rag-assistant.git
cd genai-rag-assistant

