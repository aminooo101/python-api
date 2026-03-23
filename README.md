# Book Tracker API

REST API for tracking books built with FastAPI, SQLAlchemy, and SQLite.

## Endpoints

| Method | Route | Description |
|--------|-------|-------------|
| POST | /books/ | Add a book |
| GET | /books/ | List all books |
| GET | /books/{id} | Get one book |
| PUT | /books/{id} | Update status or rating |
| DELETE | /books/{id} | Remove a book |

## Run locally
```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Open http://localhost:8000/docs for the interactive API docs.

## Tech stack

- FastAPI
- SQLAlchemy
- Pydantic
- SQLite
