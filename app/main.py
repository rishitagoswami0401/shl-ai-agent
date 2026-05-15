from fastapi import FastAPI
from app.catalog_loader import load_catalog
from app.retriever import search_assessments
from app.models import ChatRequest
from app.utils import is_vague_query

app = FastAPI()

# Load SHL catalog
catalog = load_catalog()


@app.get("/")
def home():

    return {
        "message": "SHL AI Agent Running",
        "total_assessments": len(catalog)
    }


@app.get("/health")
def health():

    return {
        "status": "ok"
    }


@app.post("/chat")
def chat(request: ChatRequest):

    latest_message = request.messages[-1].content

    # Combine full conversation for refinement support
    conversation_text = " ".join(
        [msg.content for msg in request.messages]
    )

    # Clarification handling
    if is_vague_query(latest_message):

        return {
            "reply": (
                "Could you share the role, "
                "experience level, and skills "
                "you want to assess?"
            ),
            "recommendations": [],
            "end_of_conversation": False
        }

    # Comparison support
    if (
        "difference" in latest_message.lower()
        or "compare" in latest_message.lower()
    ):

        return {
            "reply": (
                "OPQ focuses on personality and "
                "workplace behavior, while GSA "
                "focuses on cognitive and general "
                "skills assessment."
            ),
            "recommendations": [],
            "end_of_conversation": False
        }

    # Semantic retrieval using FAISS
    results = search_assessments(conversation_text)

    recommendations = []

    for item in results:

        recommendations.append({
            "name": item.get("name"),
            "url": item.get("url"),
            "description": item.get("description")
        })

    reply = (
        f"I found {len(recommendations)} "
        f"relevant SHL assessments for your request."
    )

    return {
        "reply": reply,
        "recommendations": recommendations,
        "end_of_conversation": False
    }