from sqlalchemy.ext.asyncio import (
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import DeclarativeBase

from settings import database_settings


class Base(DeclarativeBase):

    def __repr__(self):
        cols = [
            f"{col}={getattr(self, col)}"
            for col in self.__table__.columns.keys()
        ]
        return " ".join(cols)


DSN = f"postgresql+asyncpg://{database_settings.POSTGRES_USER}\
:{database_settings.POSTGRES_PASSWORD}@\
{database_settings.POSTGRES_HOST}:\
{database_settings.POSTGRES_PORT}/\
{database_settings.POSTGRES_DB}"
async_engine = create_async_engine(DSN, echo=True)
async_session_maker = async_sessionmaker(async_engine, expire_on_commit=False)


async def create_db():
    async with async_engine.begin() as connection:
        await connection.run_sync(Base.metadata.drop_all)
        await connection.run_sync(Base.metadata.create_all)
