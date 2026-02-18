import streamlit as st
import requests

BACKEND_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="RAG Chatbot", page_icon="🤖")
st.title("📄 RAG Based Chatbot")

# -------- File Upload --------
st.subheader("Upload Document")

uploaded_file = st.file_uploader(
    "Upload a PDF or TXT file",
    type=["pdf", "txt"]
)

if uploaded_file:
    files = {"file": uploaded_file}
    with st.spinner("Uploading and indexing document..."):
        res = requests.post(f"{BACKEND_URL}/insert", files=files)

    if res.status_code == 200:
        st.success("Document uploaded successfully!")
    else:
        st.error("Failed to upload document")

# -------- Chat Section --------
st.subheader("Ask a Question")

question = st.text_input("Enter your question")

if st.button("Ask"):
    if not question:
        st.warning("Please enter a question")
    else:
        with st.spinner("Thinking..."):
            res = requests.post(
                f"{BACKEND_URL}/query",
                params={"question": question}
            )

        if res.status_code == 200:
            answer = res.json().get("answer", "")
            st.markdown("### 🤖 Answer")
            st.write(answer)
        else:
            st.error("Error getting response from chatbot")
