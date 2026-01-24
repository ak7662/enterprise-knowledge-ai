from pydantic import BaseSettings

class Settings(BaseSettings):
    env: str = "development"
    log_level: str = "INFO"

    openai_api_key: str
    anthropic_api_key: str

    class Config:
        env_file = ".env"

settings = Settings()
