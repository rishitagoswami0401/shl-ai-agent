from app.faiss_index import search_index

def retrieve_assessments(query, index, catalog):
    return search_index(query, index, catalog)