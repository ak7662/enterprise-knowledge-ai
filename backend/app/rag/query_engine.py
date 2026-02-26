from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core.response_synthesizers import get_response_synthesizer

from app.rag.index import get_index
from app.rag.prompts import qa_prompt  # wherever your prompt is

def get_query_engine(collection_name: str):
    index = get_index(collection_name)

    retriever = index.as_retriever(
        similarity_top_k=3
    )

    response_synthesizer = get_response_synthesizer(
        text_qa_template=qa_prompt
    )

    return RetrieverQueryEngine(
        retriever=retriever,
        response_synthesizer=response_synthesizer
    )
