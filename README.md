# SHL AI Assessment Recommendation Agent

A conversational AI recommendation system built using FastAPI, SentenceTransformers, and FAISS for recommending SHL assessments based on hiring requirements.

---

# Features

- Conversational recommendation system
- Clarification handling for vague queries
- Semantic search using FAISS vector database
- Retrieval-Augmented Generation (RAG) style retrieval
- Multi-turn conversation refinement
- Assessment comparison support
- FastAPI REST API
- Swagger API documentation

---

# Tech Stack

- Python
- FastAPI
- FAISS
- SentenceTransformers
- NumPy
- Uvicorn

---

# Project Structure

app/
│
├── main.py
├── retriever.py
├── faiss_index.py
├── catalog_loader.py
├── models.py
├── utils.py
│
data/
│
├── assessments.json
│
requirements.txt
README.md
approach.md

---

# Installation

## Create Virtual Environment

python -m venv venv

---

## Activate Virtual Environment

### Windows

venv\Scripts\activate

---

## Install Dependencies

pip install -r requirements.txt

---

# Running the Application

uvicorn app.main:app --reload

Server runs on:

http://127.0.0.1:8000

---

# API Documentation

Swagger UI:

http://127.0.0.1:8000/docs

---

# API Endpoints

## Health Endpoint

GET /health

Response:

{
  "status": "ok"
}

---

## Chat Endpoint

POST /chat

Request Example:

{
  "messages": [
    {
      "role": "user",
      "content": "Hiring Java backend developer"
    }
  ]
}

---

# Retrieval Architecture

The system uses semantic retrieval instead of keyword matching.

Process:

1. Assessment descriptions are converted into vector embeddings
2. Embeddings are stored in a FAISS vector database
3. User queries are converted into embeddings
4. FAISS retrieves semantically similar assessments

Embedding Model Used:

all-MiniLM-L6-v2

---

# Conversational Capabilities

The agent supports:

- Clarification questions
- Recommendation generation
- Conversation refinement
- Assessment comparison

---

# Deployment

The project can be deployed on Render.

## Start Command

uvicorn app.main:app --host 0.0.0.0 --port 10000

---

# Author

Rishita Goswami