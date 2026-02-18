# RAG Chatbot — Document Intelligence System
A Retrieval-Augmented Generation (RAG) based AI chatbot that answers user queries from uploaded documents (PDF or TXT) using semantic search and a Large Language Model.
Instead of generating generic responses, the chatbot retrieves relevant information from documents and produces accurate, context-aware answers.

## 🚀 Features
✅ Upload PDF or TXT documents
✅ Automatic document processing and indexing
✅ Semantic search using vector embeddings
✅ FAISS vector database for fast retrieval
✅ Context-aware answer generation using LLM
✅ FastAPI backend API
✅ Interactive Streamlit user interface
✅ Real-time document question answering

## 🧠 How It Works
1.Document Ingestion Pipeline
2.Upload document (PDF/TXT)
3.Extract text from file
4.Split text into smaller chunks
5.Convert chunks into embeddings
6.Store embeddings in FAISS vector database

## Question Answering Pipeline
1.User asks a question
2.Convert question into embedding
3.Retrieve most relevant document chunks
4.Send context + question to LLM
5.Generate final answer

## ARCHITECTURE:

User → Streamlit UI → FastAPI Server
                ↓
         Document Processing
   (Loader → Chunker → Embeddings → FAISS)
                ↓
           Retriever
                ↓
           LLM (Groq)
                ↓
             Answer


Send context + question to LLM

Generate final answer
