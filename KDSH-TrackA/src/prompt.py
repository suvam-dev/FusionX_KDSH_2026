"""
Prompt templates for RAG (Retrieval Augmented Generation).
"""
from typing import List


def build_rag_prompt(query: str, contexts: List[str]) -> str:
    """
    Build a RAG prompt with query and retrieved contexts.
    
    Args:
        query: User query/question
        contexts: List of retrieved context chunks
        
    Returns:
        Formatted prompt string
    """
    context_text = "\n\n".join([
        f"Context {i+1}:\n{ctx}" 
        for i, ctx in enumerate(contexts)
    ])
    
    prompt = f"""You are a helpful assistant that answers questions based on the provided context.

Contexts:
{context_text}

Question: {query}

Please provide a comprehensive answer based on the contexts above. If the contexts don't contain enough information to answer the question, please say so."""
    
    return prompt


def build_simple_prompt(query: str, contexts: List[str]) -> str:
    """
    Build a simpler RAG prompt.
    
    Args:
        query: User query/question
        contexts: List of retrieved context chunks
        
    Returns:
        Formatted prompt string
    """
    context_text = "\n\n".join(contexts)
    
    return f"""Based on the following context, answer the question.

Context:
{context_text}

Question: {query}

Answer:"""
