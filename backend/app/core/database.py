from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncSession
)

from backend.app.core.config import DATABASE_URL
from backend.app.models.base import Base

engine = create_async_engine(
    DATABASE_URL,
    echo=True,
    pool_pre_ping=True
)

SessionLocal = async_sessionmaker(
    engine,
    expire_on_commit=False
)

async def get_session():
    async with SessionLocal() as session:
        yield session

SessionDep = Annotated[AsyncSession, Depends(get_session)]