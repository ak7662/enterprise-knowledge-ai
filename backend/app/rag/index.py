from llama_index.core import VectorStoreIndex
from app.services.vector_store import get_vector_store
from app.services.embeddings import get_embedding_model

_index_cache = {}

def get_index(collection_name: str):
    if collection_name in _index_cache:
        return _index_cache[collection_name]

    vector_store = get_vector_store(collection_name)
    embed_model = get_embedding_model()

    index = VectorStoreIndex.from_vector_store(
        vector_store=vector_store,
        embed_model=embed_model
    )

    _index_cache[collection_name] = index
    return index
