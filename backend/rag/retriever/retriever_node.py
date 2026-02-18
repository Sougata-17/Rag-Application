from backend.rag.retriever.faiss_retriever import retrieve

def get_context(query):
    docs = retrieve(query)
    return "\n".join(docs)