from uuid import uuid4, UUID

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from src.notebook.schemas import CreateNote
from src.notebook.models import Note, NoteMetrics


class NoteService:

    async def create_note(self, db: AsyncSession, new_note: CreateNote) -> dict:
        new_note_dict = new_note.model_dump(exclude={'metrics'})
        print(new_note_dict)
        note = Note(**new_note_dict)
        db.add(note)
        await db.flush()

        if new_note.metrics:
            metrics = NoteMetrics(
                note_uuid=note.uuid,
                **new_note.metrics.model_dump()
            )
            db.add(metrics)

        await db.commit()
        await db.refresh(note)
        result = note.get_dict()
        return result

    async def get_note(self, db: AsyncSession, note_uuid: str):
        statement = select(Note).where(Note.uuid == note_uuid)
        result = await db.execute(statement)

        note = result.scalars().first()
        return note
