import faiss
import pickle
import os

DB_PATH = "backend/rag/vector_store/data"

def save_faiss(index, chunks):
    os.makedirs(DB_PATH, exist_ok=True)
    faiss.write_index(index, f"{DB_PATH}/index.faiss")
    with open(f"{DB_PATH}/chunks.pkl", "wb") as f:
        pickle.dump(chunks, f)

def load_faiss():
    index = faiss.read_index(f"{DB_PATH}/index.faiss")
    with open(f"{DB_PATH}/chunks.pkl", "rb") as f:
        chunks = pickle.load(f)
    return index, chunks