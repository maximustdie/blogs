from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from database.postgres.config import config

DATABASE_URL = config.pg.construct_url()

engine = create_async_engine(DATABASE_URL, echo=True)
async_session_factory = async_sessionmaker(engine, expire_on_commit=False)
