from fastapi import FastAPI, UploadFile, File
from backend.rag.vector_store.ingest import ingest_single_file
from backend.api.chat_api import chat

app = FastAPI()

# -------------------------------
# Route 1: Insert Document
# -------------------------------
@app.post("/insert")
async def insert_file(file: UploadFile = File(...)):
    
    file_path = f"backend/rag/data/{file.filename}"
    
    with open(file_path, "wb") as f:
        f.write(await file.read())

    # Run ingestion on this file
    ingest_single_file(file_path)

    return {"message": "File uploaded successfully"}


# -------------------------------
# Route 2: Query Chatbot
# -------------------------------
@app.post("/query")
async def query_chatbot(question: str):
    
    answer = chat(question)
    
    return {"answer": answer}
