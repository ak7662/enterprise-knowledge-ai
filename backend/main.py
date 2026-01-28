from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

from app.rag.query_engine import get_query_engine
from app.core.logger import logger

router = APIRouter()
from app.core.llama_bootstrap import *  # noqa: F401

from fastapi import FastAPI
from app.api.routes import query

app = FastAPI(title="Enterprise Knowledge AI")

app.include_router(query.router, prefix="/api")

class QueryRequest(BaseModel):
    question: str


@router.post("/query/stream")
def stream_query(payload: QueryRequest):
    logger.info(f"Streaming query: {payload.question}")

    query_engine = get_query_engine("company_docs")

    # ✅ ENABLE STREAMING
    response = query_engine.query(
        payload.question,
        streaming=True
    )

    def token_generator():
        for token in response.response_gen:
            yield token

    return StreamingResponse(
        token_generator(),
        media_type="text/plain"
    )


@router.post("/query")
def query_docs(payload: QueryRequest):
    logger.info(f"User query: {payload.question}")

    query_engine = get_query_engine("company_docs")
    response = query_engine.query(payload.question)

    logger.info("Answer generated successfully")

    return {
        "answer": response.response,
        "sources": [
            {
                "score": node.score,
                "text": node.node.text[:300]
            }
            for node in response.source_nodes
        ]
    }
