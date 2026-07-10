# KB RAG Setup

This project keeps each markdown KB article as a separate source file under:

```text
hackathon2026/data/KB Articles
```

The ingestion script expects each markdown file to start with:

```md
URL: https://example.com/article

ID: 12345

# Article Title

Article content...
```

## Pipeline

```text
Markdown files
  -> parse article_id, title, url
  -> split into semantic chunks
  -> keep markdown tables and code fences intact
  -> upload chunks as files to an OpenAI Vector Store
  -> save a local chunk manifest for keyword retrieval and citations
  -> user question
  -> OpenAI vector search + local keyword search
  -> reciprocal rank fusion
  -> LLM reranking
  -> answer with citations
```

## Ingest

Run this from the repository root when you are ready to create the OpenAI Vector Store:

```powershell
python scripts/ingest_kb_to_openai_vector_store.py
```

The script prints:

```text
OPENAI_VECTOR_STORE_ID=...
KB_CHUNK_MANIFEST=hackathon2026/data/rag/chunks.jsonl
```

Add those values to:

```text
hackathon2026/.env
```

## Ask Locally

After ingestion and `.env` setup:

```powershell
python scripts/ask_kb_rag.py "Explain payment schedule types"
```

The booking API also uses this RAG path for casual/general questions after the flow decider classifies the prompt as `casual`.
