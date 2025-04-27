from uuid import uuid4

from sqlalchemy import Column, Text, ForeignKey, Float, TIMESTAMP, Integer
from sqlalchemy.orm import relationship, declarative_base
import sqlalchemy.dialects.postgresql as pg
Base = declarative_base()

class Note(Base):
    __tablename__ = "notes"

    uuid = Column(pg.UUID, primary_key=True, default=uuid4,unique=True, nullable=False)
    title = Column(Text, nullable=False)
    text = Column(Text, nullable=False)
    metrics = relationship("NoteMetrics", back_populates="note", uselist=False)

    def get_dict(self):
        result = {
            "uuid": str(self.uuid),
            "title": self.title,
            "text": self.text
        }

        if self.metrics is not None:
            result['metrics'] = {
                "creation_time": self.metrics.creation_time,
                "created_at": self.metrics.created_at.isoformat(),
                "char_count": self.metrics.char_count
            }
        return result




class NoteMetrics(Base):
    __tablename__ = "note_metrics"
    note_uuid = Column(pg.UUID, ForeignKey("notes.uuid"), primary_key=True)
    creation_time = Column(Float, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False)
    char_count = Column(Integer, nullable=False)
    note = relationship("Note", back_populates="metrics")