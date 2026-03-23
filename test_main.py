from fastapi.testclient import TestClient
from main import app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base, get_db




engine = create_engine("sqlite:///./test.db", connect_args={"check_same_thread": False})
TestingSession = sessionmaker(bind=engine)

def override_get_db():
    db = TestingSession()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db
Base.metadata.create_all(bind=engine)
client = TestClient(app)


def test_create_book():
    r = client.post("/books/", json={"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "status": "want"})
    assert r.status_code == 201
    assert r.json()["title"] == "The Great Gatsby"
    assert r.json()["author"] == "F. Scott Fitzgerald"

def test_get_books():
    r = client.get("/books/")
    assert r.status_code == 200
    assert isinstance(r.json(), list)

def test_get_book():
    r = client.get("/books/1")
    assert r.status_code == 200
    assert r.json()["title"] == "The Great Gatsby"

def test_get_book_not_found():
    r = client.get("/books/999")
    assert r.status_code == 404



def test_update_book():
    r = client.put("/books/1", json={"status": "reading", "rating": 5})
    assert r.status_code == 200
    assert r.json()["status"] == "reading"
    assert r.json()["rating"] == 5


def test_delete_book():
    r = client.delete("/books/1")

def test_rate_book_invalid_rating():
    r = client.post("/books/", json={"title": "1984", "author": "George Orwell", "status": "reading"})
    assert r.status_code == 201
    book_id = r.json()["id"]
    r = client.put(f"/books/{book_id}", json={"rating": 6})
    assert r.status_code == 422 





