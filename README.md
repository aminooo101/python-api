# Book Tracker API

> REST API to track books — want to read, reading, or done.
> Built with FastAPI, SQLAlchemy, and deployed on Render.

![Tests](https://img.shields.io/badge/tests-7%20passed-brightgreen)
![Python](https://img.shields.io/badge/python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-teal)

**Live demo:** https://TU-URL.onrender.com/docs

## Endpoints
| Method | Route | Description |
|--------|-------|-------------|
| `POST` | `/books/` | Add a book |
| `GET` | `/books/` | List all books |
| `GET` | `/books/{id}` | Get one book |
| `PUT` | `/books/{id}` | Update status or rating |
| `DELETE` | `/books/{id}` | Remove a book |

Filter: `GET /books/?status=reading`

## Run locally
```bash
git clone https://github.com/aminooo101/python-api-inventory
cd python-api-inventory
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```
Open http://localhost:8000/docs

## Tests
```bash
pytest test_main.py -v  # 7 passed
```

## Tech stack
FastAPI · SQLAlchemy · Pydantic · pytest · SQLite · Render.com