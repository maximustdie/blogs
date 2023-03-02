from typing import Generator

from sqlalchemy.ext.asyncio import AsyncSession

from database.postgres.core import async_session_factory


async def get_session() -> Generator:
    session: AsyncSession = async_session_factory()
    try:
        yield session
    finally:
        await session.close()