from llama_index.core import Settings
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding

# 🔒 FORCE local-only LLM
Settings.llm = Ollama(
    model="llama3.1:8b",
    temperature=0.1,
    request_timeout=120,
)

# 🔒 FORCE local-only embeddings
Settings.embed_model = OllamaEmbedding(
    model_name="nomic-embed-text"
)

# Optional but good practice
Settings.chunk_size = 512
Settings.chunk_overlap = 50
settings.vector_db_path = "./data/chroma"
