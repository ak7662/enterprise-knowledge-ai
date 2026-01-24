from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # App
    env: str = "development"
    log_level: str = "INFO"

    # Ollama (Local LLM)
    ollama_base_url: str = "http://localhost:11434"
    llm_model: str = "llama3.1:8b"
    embedding_model: str = "nomic-embed-text"

    # Vector DB
    vector_db_path: str = "./data/chroma"

    class Config:
        env_file = ".env"

settings = Settings()
