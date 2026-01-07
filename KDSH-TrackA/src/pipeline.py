"""
Main Pathway orchestration for RAG pipeline.
Creates a web server that accepts queries, retrieves contexts, and generates answers.
"""
import os
import pathway as pw
from pathway.io.http import rest_connector
from dotenv import load_dotenv

from src.ingest import ingest_novels
from src.chunking import chunk_documents
from src.vector_store import create_vector_store
from src.prompt import build_rag_prompt
from src.llm import create_gemini_chat

load_dotenv()


def create_rag_pipeline(novels_path: str = "data/novels", host: str = "0.0.0.0", port: int = 8000):
    """
    Create and run the RAG pipeline with Pathway web server.
    
    Args:
        novels_path: Path to novels directory
        host: Server host address
        port: Server port number
    """
    # Initialize components
    vector_store = create_vector_store()
    gemini_client, model = create_gemini_chat()
    
    # Ingest novels in streaming mode
    novels = ingest_novels(novels_path)
    
    # Extract text content from file data
    documents = novels.select(
        data=pw.this.data,
        metadata=pw.this._metadata
    )
    
    # Chunk documents
    chunks = chunk_documents(documents)
    
    # Prepare chunks for vector store (with text and metadata)
    indexed_chunks = chunks.select(
        text=pw.this.chunk_text,
        metadata=pw.this.metadata
    )
    
    # Build vector store index from chunks
    # Note: VectorStoreClient should handle indexing automatically when documents are added
    vector_store.build_index(indexed_chunks)
    
    # Define query input schema
    class QueryInputSchema(pw.Schema):
        query: str
    
    # Create query input table via REST API
    query_input = rest_connector(
        host=host,
        port=port,
        schema=QueryInputSchema,
        route="/query",
        method="POST"
    )
    
    # Retrieve contexts and generate answers
    def retrieve_and_answer(query: str) -> str:
        """Retrieve relevant contexts and generate answer using Gemini."""
        try:
            # Retrieve relevant chunks from vector store
            results = vector_store.retrieve_query(
                queries=[query],
                k=5
            )
            
            # Extract context texts from results
            # Results format may vary, so we handle different cases
            contexts = []
            if results:
                if isinstance(results, list):
                    for result in results:
                        if isinstance(result, dict):
                            contexts.append(result.get('text', ''))
                        elif hasattr(result, 'text'):
                            contexts.append(result.text)
                        else:
                            contexts.append(str(result))
                elif hasattr(results, 'text'):
                    contexts = [results.text]
            
            # Build prompt with contexts
            prompt = build_rag_prompt(query, contexts)
            
            # Generate answer using Gemini
            response = gemini_client.models.generate_content(
                model=model,
                contents=prompt
            )
            
            # Extract text from response
            if hasattr(response, 'text'):
                return response.text
            elif hasattr(response, 'candidates') and len(response.candidates) > 0:
                return response.candidates[0].content.parts[0].text
            else:
                return str(response)
        except Exception as e:
            return f"Error generating response: {str(e)}"
    
    # Process queries and generate answers
    answers = query_input.select(
        query=pw.this.query,
        answer=pw.apply(
            retrieve_and_answer,
            query=pw.this.query
        )
    )
    
    # Serve responses via HTTP
    pw.io.http.serve(
        query_input,
        answers,
        host=host,
        port=port
    )
    
    # Run the pipeline
    pw.run()


if __name__ == "__main__":
    create_rag_pipeline()
