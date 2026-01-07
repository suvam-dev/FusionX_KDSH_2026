from ingest import load_novel
from chunking import chunk_text
from vector_store import build_store
from retrieval import retrieve
from prompt import build_prompt
from llm import call_llm
from classifier import classify

def run(novel_path, backstory_text):
    novel = load_novel(novel_path)
    chunks = chunk_text(novel)
    store = build_store(chunks)

    retrieved = retrieve(store, backstory_text)
    prompt = build_prompt(backstory_text, retrieved)
    llm_out = call_llm(prompt)

    return classify(llm_out)

