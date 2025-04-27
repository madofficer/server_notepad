from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

from src.Config import Config
from src.notebook.models import Base

DATABASE_URL = (f"postgresql+asyncpg://"
                f"{Config.DB_USER}:"
                f"{Config.DB_PASS}@"
                f"{Config.DB_HOST}:"
                f"{Config.DB_PORT}/"
                f"{Config.DB_NAME}")

async_engine = create_async_engine(DATABASE_URL)


async def init_db():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def get_session() -> AsyncSession:
    async_session = async_sessionmaker(
        async_engine,
        class_=AsyncSession,
        expire_on_commit=False
    )
    async with async_session() as session:
        yield session
