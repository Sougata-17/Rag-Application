from backend.rag.retriever.retriever_node import get_context
from backend.llm.simple_llm import generate_answer

def chat(query):
    context = get_context(query)
    answer = generate_answer(context, query)
    return answer