from backend.rag.vector_store.faiss_store import load_faiss
from backend.rag.embeddings.embedding_model import embed_text

def retrieve(query, top_k=3):
    index, chunks = load_faiss()

    query_embedding = embed_text([query])
    distances, indices = index.search(query_embedding, top_k)

    results = [chunks[i] for i in indices[0]]
    return results