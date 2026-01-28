from app.rag.ingestion import ingest_documents
from app.rag.retriever import get_retriever

# Ingest once
ingest_documents("data/docs", collection_name="company_docs")

# Retrieve
retriever = get_retriever("company_docs")

results = retriever.retrieve("What is this document about?")

for node in results:
    print("----")
    print(node.get_content())

# from app.rag.ingestion import ingest_documents

# ingest_documents(
#     path="data/docs",
#     collection_name="company_docs"
# )

