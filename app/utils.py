def is_vague_query(query):

    vague_words = [
        "assessment",
        "test",
        "hiring",
        "need",
        "job"
    ]

    query = query.lower()

    # if query is too short
    if len(query.split()) <= 2:
        return True

    # vague only if ONLY vague words exist
    if query in vague_words:
        return True

    return False