"""
Text chunking using Pathway's TokenCountSplitter.
Splits documents into chunks based on token count.
"""
import pathway as pw
from pathway.xpacks.llm.parsers import TokenCountSplitter


def chunk_documents(documents: pw.Table, chunk_size: int = 1000, overlap: int = 200) -> pw.Table:
    """
    Split documents into chunks using token-based splitting.
    
    Args:
        documents: Pathway table with document content (must have 'data' column)
        chunk_size: Maximum tokens per chunk
        overlap: Number of overlapping tokens between chunks
        
    Returns:
        Pathway table with chunked documents
    """
    splitter = TokenCountSplitter(
        tokens_per_chunk=chunk_size,
        tokens_overlap=overlap
    )
    
    # Apply splitter to each document
    chunks = documents.select(
        chunks=pw.apply(
            lambda text: splitter.split_text(text) if text else [],
            text=documents.data
        ),
        metadata=documents._metadata
    )
    
    # Flatten chunks from list to individual rows
    chunks = chunks.flatten(pw.this.chunks).select(
        chunk_text=pw.this.chunks,
        metadata=pw.this.metadata
    )
    
    return chunks
