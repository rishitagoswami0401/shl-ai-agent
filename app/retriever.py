import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def search_assessments(query, catalog, index):

    query_embedding = model.encode([query])

    distances, indices = index.search(
        np.array(query_embedding).astype("float32"),
        5
    )

    results = []

    for idx in indices[0]:

        results.append(catalog[idx])

    return results