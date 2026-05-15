import faiss
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

texts = []
vectorizer = TfidfVectorizer()

def build_index(catalog):
    global texts

    texts = [
        item["name"] + " " + item.get("description", "")
        for item in catalog
    ]

    vectors = vectorizer.fit_transform(texts).toarray()

    dimension = vectors.shape[1]

    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(vectors).astype("float32"))

    return index

def search_index(query, index, catalog, top_k=5):
    query_vector = vectorizer.transform([query]).toarray()

    distances, indices = index.search(
        np.array(query_vector).astype("float32"),
        top_k
    )

    results = []

    for idx in indices[0]:
        results.append(catalog[idx])

    return results