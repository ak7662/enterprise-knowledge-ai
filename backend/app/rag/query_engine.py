from llama_index.core import VectorStoreIndex
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.core.postprocessor import SimilarityPostprocessor

from app.services.vector_store import get_storage_context
from app.services.llm import get_llm
from app.services.embeddings import get_embedding_model


def get_query_engine(
    collection_name: str,
    similarity_top_k: int = 4,
    similarity_cutoff: float = 0.7
):
    storage_context = get_storage_context(collection_name)

    index = VectorStoreIndex.from_vector_store(
        vector_store=storage_context.vector_store,
        embed_model=get_embedding_model()
    )

    retriever = VectorIndexRetriever(
        index=index,
        similarity_top_k=similarity_top_k
    )

    query_engine = RetrieverQueryEngine(
        retriever=retriever,
        node_postprocessors=[
            SimilarityPostprocessor(similarity_cutoff=similarity_cutoff)
        ]
    )

    return query_engine
