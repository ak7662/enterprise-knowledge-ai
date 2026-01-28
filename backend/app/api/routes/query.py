from fastapi import APIRouter
from pydantic import BaseModel

from app.rag.query_engine import get_query_engine

router = APIRouter()


class QueryRequest(BaseModel):
    question: str


@router.post("/query/stream")
def query_docs(payload: QueryRequest):
    query_engine = get_query_engine(collection_name="company_docs")
    response = query_engine.query(payload.question)

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

@router.post("/query")
def query_docs(payload: QueryRequest):
    query_engine = get_query_engine(collection_name="company_docs")
    response = query_engine.query(payload.question)

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
