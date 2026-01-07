# Setup Instructions

## Environment Configuration

Create a `.env` file in the project root with the following content:

```
GOOGLE_API_KEY=your_google_api_key_here
```

Replace `your_google_api_key_here` with your actual Google Gemini API key.

## Quick Start

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Create `.env` file (see above)

3. Add your novel `.txt` files to `data/novels/`

4. Run the server:
   ```bash
   python scripts/run_inference.py
   ```

5. Send queries to `http://0.0.0.0:8000/query`:
   ```bash
   curl -X POST http://localhost:8000/query \
     -H "Content-Type: application/json" \
     -d '{"query": "What is the main character like?"}'
   ```
