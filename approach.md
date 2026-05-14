# SHL Assessment Recommendation Agent – Approach Document

## Introduction

The objective of this project is to build a conversational AI agent capable of recommending relevant SHL assessments based on user hiring requirements. The system supports multi-turn conversations and semantic retrieval of assessments using vector similarity search.

The application is implemented using FastAPI for API development and FAISS for efficient semantic search over assessment data.

---

# System Architecture

The solution follows a retrieval-based conversational architecture.

The workflow is:

User Query
↓
Conversation Processing
↓
Embedding Generation
↓
FAISS Similarity Search
↓
Relevant Assessment Retrieval
↓
Structured JSON Response

The architecture is lightweight, scalable, and optimized for fast retrieval.

---

# Dataset Handling

The SHL product catalog is provided in JSON format. Each assessment entry contains information such as:

- Assessment Name
- URL
- Description
- Job Levels
- Test Type
- Skills

The catalog is loaded during application startup and stored in memory for fast access.

---

# Semantic Retrieval using FAISS

Traditional keyword matching is often insufficient because user queries may use wording different from assessment descriptions.

To solve this problem, semantic retrieval is implemented using SentenceTransformers and FAISS.

## Embedding Generation

Assessment descriptions are converted into dense vector embeddings using:

all-MiniLM-L6-v2

from the SentenceTransformers library.

This model captures semantic meaning instead of exact keyword matches.

---

## Vector Database

The generated embeddings are stored inside a FAISS vector index.

FAISS enables efficient similarity search across large embedding datasets and significantly improves retrieval speed.

---

## Query Processing

When a user submits a query:

1. The user query is converted into an embedding
2. FAISS performs similarity search
3. Top matching assessments are retrieved
4. Results are formatted into structured API responses

This enables the system to retrieve relevant assessments even when the query wording differs from the assessment text.

---

# Conversational Logic

The chatbot supports multiple conversational behaviors required by the assignment.

---

## 1. Clarification Handling

If the user query lacks sufficient information, the system asks follow-up clarification questions.

Example:

User:
"I need an assessment"

Assistant:
"Could you share the role, experience level, and skills you want to assess?"

This prevents poor-quality recommendations.

---

## 2. Recommendation Generation

Once sufficient context is available, the system retrieves relevant SHL assessments and returns:

- Assessment name
- URL
- Description

The recommendations are generated through semantic similarity search.

---

## 3. Multi-turn Refinement

The system supports refinement across conversation history.

Example:

User:
"Hiring Java developer"

Later:
"Add personality assessments too"

The entire conversation history is combined into a single retrieval query, enabling updated recommendations without restarting the conversation.

---

## 4. Assessment Comparison

The system supports comparison-based queries such as:

"What is the difference between OPQ and GSA?"

The response is generated using catalog information instead of hardcoded answers.

---

# API Design

The application exposes two REST endpoints.

---

## GET /health

Used for health monitoring and deployment validation.

Response:

{
  "status": "ok"
}

---

## POST /chat

Main conversational endpoint.

The API is stateless, meaning the entire conversation history is provided in every request.

Example:

{
  "messages": [
    {
      "role": "user",
      "content": "Hiring Java backend developer"
    }
  ]
}

---

# Technologies Used

- FastAPI
- FAISS
- SentenceTransformers
- NumPy
- Uvicorn
- Python

---

# Deployment Strategy

The application is designed for cloud deployment using Render.

Render deployment is suitable because:
- Simple FastAPI hosting
- Easy GitHub integration
- Free deployment tier
- Automatic HTTPS support

The application uses Uvicorn as the ASGI server.

---

# Future Improvements

Potential future enhancements include:

- LLM integration for better conversation generation
- Hybrid search combining semantic and keyword retrieval
- Persistent conversation memory
- Better ranking and reranking
- Metadata filtering
- Personalized recommendations

---

# Conclusion

This project demonstrates a semantic retrieval-based conversational recommendation system using modern AI retrieval techniques.

By combining FastAPI, SentenceTransformers, and FAISS, the solution provides scalable, accurate, and context-aware SHL assessment recommendations.

# Challenges and Improvements

Initially, keyword-based matching produced inaccurate recommendations because user queries often used wording different from assessment descriptions.

To improve retrieval quality, semantic embeddings using SentenceTransformers and FAISS were introduced. This significantly improved relevance by retrieving assessments based on semantic meaning instead of exact keywords.

Another challenge was handling vague user queries. Clarification logic was added to ensure the system gathers sufficient context before generating recommendations.

The retrieval quality was manually evaluated using multiple sample hiring queries and observing whether relevant assessments appeared in the top retrieved results.