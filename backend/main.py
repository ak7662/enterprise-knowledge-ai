from fastapi import FastAPI
from app.core.config import settings
from app.core.logging import setup_logging

logger = setup_logging(settings.log_level)

app = FastAPI(
    title="Enterprise Knowledge AI",
    version="0.1.0"
)

@app.get("/health")
def health_check():
    return {"status": "ok"}

logger.info("Application started")
