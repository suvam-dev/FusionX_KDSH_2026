from tiktoken import get_encoding

enc = get_encoding("cl100k_base")

def chunk_text(text, min_tokens=300, max_tokens=500):
    tokens = enc.encode(text)
    chunks = []

    i = 0
    while i < len(tokens):
        chunk = tokens[i:i+max_tokens]
        if len(chunk) >= min_tokens:
            chunks.append(enc.decode(chunk))
        i += max_tokens // 2  # overlap = GLOBAL CONSISTENCY
    return chunks

