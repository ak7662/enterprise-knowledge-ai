from llama_index.core.node_parser import SentenceSplitter

def get_chunker():
    return SentenceSplitter(
        chunk_size=512,
        chunk_overlap=100
    )


# “We tuned chunk size and overlap to balance retrieval accuracy and context window usage.”