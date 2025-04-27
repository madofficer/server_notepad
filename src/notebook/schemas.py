from datetime import datetime
from uuid import UUID
from pydantic import BaseModel

class NoteMetrics(BaseModel):
    creation_time: float
    created_at: datetime
    char_count: int

class Note(BaseModel):
    uuid: UUID
    title: str
    text: str
    metrics: None | NoteMetrics = None

class CreateNote(BaseModel):
    title: str
    text: str
    metrics: None | NoteMetrics = None