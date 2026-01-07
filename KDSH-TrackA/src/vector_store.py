"""
Vector store implementation using Pathway's VectorStoreClient
with Google Gemini embeddings.
"""
import os
import pathway as pw
from pathway.xpacks.llm.vector_store import VectorStoreClient
from pathway.xpacks.llm.embedders import GeminiEmbedder
from dotenv import load_dotenv

load_dotenv()


def create_vector_store(embedding_model: str = "models/embedding-001"):
    """
    Create a Pathway VectorStoreClient with Gemini embeddings.
    
    Args:
        embedding_model: Gemini embedding model name
        
    Returns:
        VectorStoreClient instance configured with Gemini embedder
    """
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY not found in environment variables. Please set it in your .env file.")
    
    embedder = GeminiEmbedder(
        model=embedding_model,
        api_key=api_key
    )
    
    return VectorStoreClient(
        embedder=embedder
    )
