from fastapi import FastAPI
from app.catalog_loader import load_catalog
from app.retriever import search_assessments
from app.models import ChatRequest
from app.utils import is_vague_query
from app.faiss_index import build_index

app = FastAPI()

# Load SHL catalog
catalog = load_catalog()

# Build FAISS vector index
index, texts = build_index(catalog)


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

    # combine full conversation
    conversation_text = " ".join(
        [msg.content for msg in request.messages]
    )

    # clarification handling
    if is_vague_query(latest_message):

        return {
            "reply": "Could you share the role, experience level, and skills you want to assess?",
            "recommendations": [],
            "end_of_conversation": False
        }

    # comparison handling
    if (
        "difference" in latest_message.lower()
        or "compare" in latest_message.lower()
    ):

        return {
            "reply": (
                "OPQ focuses on personality and workplace behavior, "
                "while GSA focuses on cognitive and general skills assessment."
            ),
            "recommendations": [],
            "end_of_conversation": False
        }

    # semantic search using FAISS
    results = search_assessments(
        conversation_text,
        catalog,
        index
    )

    recommendations = []

    for item in results:

        recommendations.append({
            "name": item.get("name"),
            "url": item.get("link"),
            "description": item.get("description")
        })

    reply = (
        f"I found {len(recommendations)} relevant "
        f"SHL assessments for your request."
    )

    return {
        "reply": reply,
        "recommendations": recommendations,
        "end_of_conversation": False
    }