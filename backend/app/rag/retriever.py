from llama_index.core import VectorStoreIndex
from app.services.embeddings import get_embedding_model
from app.services.vector_store import get_storage_context


def get_retriever(
    collection_name: str = "default",
    top_k: int = 5
):
    storage_context = get_storage_context(collection_name)
    embed_model = get_embedding_model()

    index = VectorStoreIndex.from_vector_store(
        vector_store=storage_context.vector_store,
        embed_model=embed_model
    )

    return index.as_retriever(similarity_top_k=top_k)
