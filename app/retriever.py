from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from app.catalog_loader import load_catalog

catalog = load_catalog()

model = SentenceTransformer("all-MiniLM-L6-v2")

texts = [
    item["name"] + " " + item.get("description", "")
    for item in catalog
]

embeddings = model.encode(texts)

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(np.array(embeddings).astype("float32"))

def search_assessments(query, top_k=5):

    query_embedding = model.encode([query])

    distances, indices = index.search(
        np.array(query_embedding).astype("float32"),
        top_k
    )

    results = []

    for idx in indices[0]:

        results.append({
            "name": catalog[idx]["name"],
            "url": catalog[idx]["url"],
            "description": catalog[idx].get("description", "")
        })

    return results