"""
Entry point to run the RAG inference server.
"""
import sys
import os
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from src.pipeline import create_rag_pipeline
from rich.console import Console

console = Console()


def main():
    """Run the RAG inference server."""
    console.print("[bold green]Starting KDSH-TrackA RAG Server...[/bold green]")
    console.print(f"[cyan]Server will run on http://0.0.0.0:8000[/cyan]")
    console.print("[yellow]Make sure to set GOOGLE_API_KEY in your .env file[/yellow]")
    
    try:
        create_rag_pipeline(
            novels_path="data/novels",
            host="0.0.0.0",
            port=8000
        )
    except KeyboardInterrupt:
        console.print("\n[yellow]Shutting down server...[/yellow]")
    except Exception as e:
        console.print(f"[bold red]Error: {e}[/bold red]")
        raise


if __name__ == "__main__":
    main()
