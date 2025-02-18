from datetime import datetime
from beanie import Document
from pydantic import BaseModel
from typing import List

class Comment(BaseModel):
    posterElementId: str
    name: str
    body: str
    date: datetime = datetime.date(datetime.now())

class Forum(Document):
    projectElementId: str
    posterElementId: str
    name: str
    body: str
    comments: List[Comment] = []
    date: datetime = datetime.date(datetime.now())

    class Settings:
        collection = "forum_collection"
