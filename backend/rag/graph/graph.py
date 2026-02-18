from backend.rag.retriever.retriever_node import get_context
from backend.llm.simple_llm import generate_answer


def rag_graph(question: str):
    """
    Step-by-step RAG pipeline (Graph-style)
    """

    # Step 1: Retrieve relevant context
    context = get_context(question)

    # Step 2: Generate answer using LLM
    answer = generate_answer(context, question)

    # Step 3: Return final answer
    return answer
