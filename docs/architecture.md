# Enterprise Knowledge AI – Architecture

## Overview
A production-grade RAG system that allows users to upload enterprise documents and chat with them securely.

## Components
- React frontend for chat UI
- FastAPI backend for ingestion and querying
- LangChain + LlamaIndex for RAG
- ChromaDB for vector storage
- OpenAI / Anthropic for LLM inference

## Data Flow
1. User uploads documents
2. Backend chunks and embeds data
3. Vectors stored in ChromaDB
4. User queries trigger RAG pipeline
5. LLM answers with citations


Documents
  → Chunk
  → Embed (local)
  → ChromaDB (persisted)

Query
  → Embed
  → Similarity search
  → Top-K chunks (with metadata)
