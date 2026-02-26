from llama_index.core import VectorStoreIndex, Document
from app.loaders.document_loader import load_documents
from app.rag.text_cleaner import clean_text
from app.rag.chunker import get_chunker
from app.services.embeddings import get_embedding_model
from app.services.vector_store import get_storage_context


def ingest_documents(
    directory: str,
    collection_name: str = "default"
):
    raw_documents = load_documents(directory)

    cleaned_documents = [
        Document(
            text=clean_text(doc.get_content()),
            metadata=doc.metadata
        )
        for doc in raw_documents
    ]

    splitter = get_chunker()
    embed_model = get_embedding_model()
    storage_context = get_storage_context(collection_name)

    index = VectorStoreIndex.from_documents(
        cleaned_documents,
        storage_context=storage_context,
        transformations=[splitter],
        embed_model=embed_model
    )

    index.storage_context.persist()
    return index
