# AllyAI

AllyAI is a local-first AI assistant with persistent memory, semantic retrieval, and conversation management.

## Features

- Persistent user facts in SQLite
- Semantic memory search with ChromaDB and Sentence Transformers
- Groq-powered chat
- Conversation save, delete, history, and import endpoints
- Memory vault endpoints for listing, adding, deleting, and searching memories
- Static frontend served by FastAPI

## Setup

```bash
poetry install
```

Create `.env` from `.env.example` and add your Groq API key.

## Run

```bash
poetry run uvicorn backend.main:app --host 127.0.0.1 --port 8000
```

Open `http://127.0.0.1:8000`.

## API

- `POST /api/chat`
- `GET /api/conversations`
- `POST /api/conversations`
- `GET /api/conversations/{id}`
- `DELETE /api/conversations/{id}`
- `POST /api/import`
- `GET /api/memories`
- `POST /api/memories`
- `DELETE /api/memories/{id}`
- `GET /api/memories/search?q=...`
