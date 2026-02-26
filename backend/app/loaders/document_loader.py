from llama_index.core import SimpleDirectoryReader
from pathlib import Path

SUPPORTED_EXTENSIONS = [".pdf", ".docx"]

def load_documents(directory: str):
    files = []
    for ext in SUPPORTED_EXTENSIONS:
        files.extend(Path(directory).rglob(f"*{ext}"))

    if not files:
        raise ValueError("No supported documents found")

    reader = SimpleDirectoryReader(
        input_files=[str(f) for f in files]
    )
    return reader.load_data()
