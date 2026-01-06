import pathlib

def load_novel(path: str) -> str:
    text = pathlib.Path(path).read_text(encoding="utf-8")
    return text.replace("\n\n", "\n").strip()

