from app.services.vector_store import get_chroma_client

client = get_chroma_client()

collections = client.list_collections()

print("Collections found:")
for col in collections:
    print("-", col.name)
