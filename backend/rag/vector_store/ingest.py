import faiss
import os

from backend.rag.loaders.pdf_loader import load_pdf
from backend.rag.loaders.text_loader import load_text
from backend.rag.splitter.chunker import chunk_text
from backend.rag.embeddings.embedding_model import embed_text
from backend.rag.vector_store.faiss_store import save_faiss

DB_FOLDER = "backend/rag/vector_store/data"
DB_INDEX = f"{DB_FOLDER}/index.faiss"
DB_CHUNKS = f"{DB_FOLDER}/chunks.pkl"


def ingest_single_file(file_path):

    # Load text
    if file_path.endswith(".pdf"):
        text = load_pdf(file_path)
    elif file_path.endswith(".txt"):
        text = load_text(file_path)
    else:
        return

    # Chunk
    chunks = chunk_text(text)

    # Embed
    embeddings = embed_text(chunks)

    # Always rebuild index safely
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)

    # Save fresh index
    save_faiss(index, chunks)

    print("✅ Vector Store rebuilt successfully")
