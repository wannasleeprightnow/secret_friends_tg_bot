import datetime
from typing import Optional
from uuid import UUID

from sqlalchemy import and_, select, update
from sqlalchemy.orm import joinedload

from db.db import async_session_maker
from db.models.recommendation import RecommendationModel
from db.models.user import UserModel
from utils.repository import Repository


class UserRepository(Repository):
    model = UserModel

    async def get_one_by_telegram_id(
        self, telegram_id: int
    ) -> Optional[UserModel]:
        async with async_session_maker() as session:
            query = select(self.model).where(
                self.model.telegram_id == telegram_id
            )
            result = await session.execute(query)
            return result.scalars().one_or_none()

    async def update_profile(
        self, telegram_id: int, updated_info: dict
    ) -> Optional[UserModel]:
        async with async_session_maker() as session:
            stmt = (
                update(self.model)
                .where(self.model.telegram_id == telegram_id)
                .values(**updated_info)
                .returning(self.model)
            )
            result = await session.execute(stmt)
            await session.commit()
            return result.scalar_one()

    async def get_user_recommendations(
        self, telegram_id: int
    ) -> list[RecommendationModel]:
        async with async_session_maker() as session:
            query = (
                select(UserModel)
                .where(UserModel.telegram_id == telegram_id)
                .options(joinedload(UserModel.recommendations))
            )
            result = await session.execute(query)
            result = result.unique().scalars().one()
            return result.recommendations

    async def get_user_with_current_notice_time(
        self, notice_time: datetime.time, days_of_week: str
    ) -> list[UUID]:
        async with async_session_maker() as session:
            query = select(self.model.id).where(
                and_(
                    self.model.notice_time == notice_time,
                    self.model.schedule.in_(days_of_week),
                )
            )
            result = await session.execute(query)
            return result.scalars().all()
