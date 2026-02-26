from app.core.llama_bootstrap import *  # noqa: F401

from fastapi import FastAPI
from app.api.routes import query

app = FastAPI(title="Enterprise Knowledge AI")

app.include_router(query.router, prefix="/api")
