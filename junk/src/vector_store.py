import pathway as pw
from pathway.xpacks.llm.vector_store import DocumentStore
from pathway.xpacks.llm.embedders import OpenAIEmbedder

def build_store(documents):
    embedder = OpenAIEmbedder()
    store = DocumentStore(
        docs=documents,
        embedder=embedder
    )
    return store

