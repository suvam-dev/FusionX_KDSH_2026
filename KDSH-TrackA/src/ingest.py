"""
Real-time file ingestion using Pathway's filesystem reader.
Watches the data/novels folder for .txt files in streaming mode.
"""
import pathway as pw


def ingest_novels(novels_path: str = "data/novels"):
    """
    Read .txt files from the novels directory in streaming mode.
    
    Args:
        novels_path: Path to the directory containing novel .txt files
        
    Returns:
        Pathway table with file contents
    """
    return pw.io.fs.read(
        novels_path,
        format="text",
        mode="streaming",
        with_metadata=True
    )
