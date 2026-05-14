import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def build_index(catalog):

    texts = []

    for item in catalog:

        text = (
            item.get("name", "") + " " +
            item.get("description", "")
        )

        texts.append(text)

    embeddings = model.encode(texts)

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(np.array(embeddings).astype("float32"))

    return index, texts