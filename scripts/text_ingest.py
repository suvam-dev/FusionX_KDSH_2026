import sys
from pathlib import Path

# Add workspace root to sys.path so we can import src modules
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.ingest import load_novel

text = load_novel("data/test/mini_novel.txt")

print("Text loaded:")
print(text[:100])