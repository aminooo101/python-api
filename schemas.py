from pydantic import BaseModel, Field
from typing import Optional
from models import Status

class BookCreate(BaseModel):
    title: str
    author: str
    status: Status = Status.want
    rating: Optional[int] = Field(None, ge=1, le=5)


class BookUpdate(BaseModel):
    status : Optional[Status] = None
    rating : Optional[int] = Field(None, ge=1, le=5)



class BookResponse(BaseModel):
    id : int
    title : str
    author : str
    status : Status
    rating : Optional[int] = Field(None, ge=1, le=5)

class Config:
    from_attributes = True

