from fastapi import FastAPI

from contextlib import asynccontextmanager

from src.notebook.routes import note_router
from src.repository.main import init_db


@asynccontextmanager
async def life_span(app: FastAPI):
    print("Server is running")
    await init_db()
    yield
    print("Server shut down")


app = FastAPI(
    title="Server Notebook",
    description="A REST API for notebook web service",
    lifespan=life_span,
)


app.include_router(note_router, prefix="/note", tags=["text_processor"])