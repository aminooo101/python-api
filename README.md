# Book Tracker API

REST API to track books (want to read / reading / done). Built with FastAPI, SQLAlchemy, and Pydantic. Includes automated tests.

## Endpoints

| Method | Route              | Description                  |
|--------|--------------------|------------------------------|
| POST   | `/books/`          | Add a book                   |
| GET    | `/books/`          | List all books               |
| GET    | `/books/{id}`      | Get one book                 |
| PUT    | `/books/{id}`      | Update status or rating      |
| DELETE | `/books/{id}`      | Remove a book                |

Filter example: `GET /books/?status=reading`

## Run locally

```bash
git clone https://github.com/aminooo101/python-api
cd python-api
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Open http://localhost:8000/docs

## Run the tests

```bash
pytest test_main.py -v
```

(7 tests currently pass.)

## Tech stack

FastAPI · SQLAlchemy · Pydantic · pytest · SQLite

## Author

Amin Hadian · [github.com/aminooo101](https://github.com/aminooo101)
