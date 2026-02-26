from app.loaders.document_loader import load_documents
from app.rag.text_cleaner import clean_text
from app.rag.chunker import get_chunker
from app.services.embeddings import get_embedding_model

from llama_index.core import VectorStoreIndex, Document


def ingest_documents(directory: str):
    raw_documents = load_documents(directory)

    cleaned_documents = []

    for doc in raw_documents:
        cleaned_text = clean_text(doc.get_content())
        cleaned_documents.append(
            Document(
                text=cleaned_text,
                metadata=doc.metadata
            )
        )

    splitter = get_chunker()
    embed_model = get_embedding_model()

    index = VectorStoreIndex.from_documents(
        cleaned_documents,
        transformations=[splitter],
        embed_model=embed_model
    )

    return index
