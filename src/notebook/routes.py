from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.notebook.schemas import Note, CreateNote
from src.notebook.service import NoteService
from src.repository.main import get_session

note_router = APIRouter()
note_service = NoteService()


@note_router.get("/{note_uuid}")
async def get_note(
        note_uuid: str,
        session: AsyncSession = Depends(get_session)
):
    note = await note_service.get_note(session, note_uuid)
    if note:
        return note
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Note not found"
        )


@note_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_note(
        note_data: CreateNote,
        session: AsyncSession = Depends(get_session)
) -> dict:
    new_note = await note_service.create_note(session, note_data)
    return new_note
