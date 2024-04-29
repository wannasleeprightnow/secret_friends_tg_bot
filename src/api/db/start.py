from models.state import StateModel
from models.recommendation import RecommendationModel
from models.user_recommendation_state import UserRecommendationStateModel
from models.user import UserModel
from db import Base

import asyncio

from sqlalchemy.ext.asyncio import (
    async_sessionmaker,
    create_async_engine,
)


async_engine = create_async_engine(..., echo=True)
async_session_maker = async_sessionmaker(async_engine, expire_on_commit=False)


async def create_db():
    async with async_engine.begin() as connection:
        await connection.run_sync(Base.metadata.drop_all)
        await connection.run_sync(Base.metadata.create_all)


asyncio.run(create_db())
