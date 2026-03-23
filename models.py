from sqlalchemy import Column, Integer, String, Enum
from database import Base
import enum

class Status(str, enum.Enum):
    want = "want"
    reading = "reading"
    done = "done"


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    status = Column(Enum(Status), default=Status.want)
    rating = Column(Integer, nullable=True)


