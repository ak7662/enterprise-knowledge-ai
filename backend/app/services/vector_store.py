import chromadb
from chromadb.config import Settings
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core import StorageContext
from app.core.config import settings

_chroma_client = None


def get_chroma_client():
    global _chroma_client
    if _chroma_client is None:
        _chroma_client = chromadb.Client(
            Settings(
                persist_directory=settings.vector_db_path,
                anonymized_telemetry=False
            )
        )
    return _chroma_client


def get_vector_store(collection_name: str):
    client = get_chroma_client()
    collection = client.get_or_create_collection(name=collection_name)
    return ChromaVectorStore(chroma_collection=collection)


def get_storage_context(collection_name: str):
    vector_store = get_vector_store(collection_name)
    return StorageContext.from_defaults(vector_store=vector_store)
