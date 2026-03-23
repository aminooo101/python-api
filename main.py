from fastapi import FastAPI, Depends, HTTPException, status  # Depends must be here
from fastapi import Response                                  # needed for DELETE
from sqlalchemy.orm import Session                            # Session from sqlalchemy
from database import engine, get_db                          # get_db from your file
import models, schemas                                        # your local files
from typing import List, Optional



models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Book Tracker API", description="API for tracking books you want to read, are reading, or have read.", version="1.0.0"
              )

@app.get("/")
def root():
    return {"message": "Book Tracker API is running", "docs": "/docs"}

@app.post("/books/", response_model=schemas.BookResponse, status_code=status.HTTP_201_CREATED)

def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    db_book = models.Book(title=book.title, author=book.author, status=book.status, rating=book.rating)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

@app.get("/books/", response_model=List[schemas.BookResponse])

def get_books(status: Optional[models.Status] = None, db: Session = Depends(get_db)):
    if status:
        return db.query(models.Book).filter(models.Book.status == status).all()
    return db.query(models.Book).all()

@app.get("/books/{book_id}", response_model=schemas.BookResponse)

def get_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@app.put("/books/{book_id}", response_model=schemas.BookResponse)
def update_book(book_id: int, book_update: schemas.BookUpdate, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    if book_update.status is not None:
        book.status = book_update.status
    if book_update.rating is not None:
        book.rating = book_update.rating
    db.commit()
    db.refresh(book)
    return book


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(book)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)








