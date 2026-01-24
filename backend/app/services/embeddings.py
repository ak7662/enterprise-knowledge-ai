from llama_index.embeddings.ollama import OllamaEmbedding
from app.core.config import settings

def get_embedding_model():
    return OllamaEmbedding(
        model_name=settings.embedding_model,
        base_url=settings.ollama_base_url
    )
