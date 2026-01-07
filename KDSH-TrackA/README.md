# KDSH-TrackA: RAG System with Pathway

A real-time Retrieval Augmented Generation (RAG) system built with Pathway and Google Gemini.

## Project Structure

```
KDSH-TrackA/
├── .env.example              # Template for API keys (create .env from this)
├── requirements.txt          # Dependencies
├── data/
│   ├── novels/               # Folder for .txt files
│   └── backstories/          # Folder for .json files
├── src/
│   ├── __init__.py
│   ├── ingest.py             # Pathway fs.read logic
│   ├── chunking.py           # TokenCountSplitter logic
│   ├── vector_store.py       # Pathway VectorStoreClient
│   ├── prompt.py             # String templates for RAG
│   ├── llm.py                # GeminiChat initialization
│   └── pipeline.py           # Main Pathway orchestration
└── scripts/
    └── run_inference.py      # Entry point to run the server
```

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure API keys:**
   - Copy `.env.example` to `.env`
   - Add your Google Gemini API key:
     ```
     GOOGLE_API_KEY=your_google_api_key_here
     ```

3. **Add novels:**
   - Place `.txt` files in the `data/novels/` directory
   - The system will automatically ingest them in real-time

## Usage

Run the inference server:

```bash
python scripts/run_inference.py
```

The server will start on `http://0.0.0.0:8000`.

### API Endpoint

Send POST requests to `/query` with JSON body:

```json
{
  "query": "Your question here"
}
```

## Implementation Details

- **Framework:** Pathway for real-time data processing
- **LLM:** Google Gemini (gemini-1.5-flash)
- **Embeddings:** Google Gemini (models/embedding-001)
- **Streaming:** Real-time file watching with `pw.io.fs.read`
- **Vector Store:** Pathway VectorStoreClient with GeminiEmbedder

## Notes

- The system uses Pathway's streaming mode to watch the `data/novels` folder in real-time
- Documents are automatically chunked using TokenCountSplitter
- Vector store is built automatically as documents are ingested
- No LangChain or LlamaIndex dependencies - pure Pathway and Google GenAI
