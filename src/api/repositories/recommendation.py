from uuid import UUID
from typing import Optional

from sqlalchemy import and_, insert, select, update
from sqlalchemy.orm import joinedload

from db.db import async_session_maker
from db.models.recommendation import RecommendationModel
from db.models.user import UserModel
from db.models.user_recommendation_state import UserRecommendationStateModel
from schemas.recommendation import UserRecommendationState
from utils.repository import Repository


class RecommendationRepository(Repository):
    model = RecommendationModel

    async def get_by_number(
        self, recommendation_number: int
    ) -> RecommendationModel:
        async with async_session_maker() as session:
            query = select(RecommendationModel).where(
                RecommendationModel.recommendation_number
                == recommendation_number
            )
            result = await session.execute(query)
            return result.scalar_one()

    async def get_first(self) -> RecommendationModel:
        async with async_session_maker() as session:
            query = select(self.model).where(
                self.model.recommendation_number == 1
            )
            result = await session.execute(query)
            return result.scalars().one_or_none()

    async def get_with_state(self, telegram_id: int, page: int):
        async with async_session_maker() as session:
            query = (
                select(UserRecommendationStateModel)
                .where(UserRecommendationStateModel.user_id == UserModel.id)
                .join(UserModel, UserModel.telegram_id == telegram_id)
                .options(
                    joinedload(UserRecommendationStateModel.recommendation)
                )
                .limit(5)
                .offset((page - 1) * 5)
            )
            result = await session.execute(query)
            return result.scalars().all()

    async def add_recommendation_for_user(
        self, data: UserRecommendationState
    ) -> None:
        async with async_session_maker() as session:
            stmt = insert(UserRecommendationStateModel).values(
                data.model_dump()
            )
            await session.execute(stmt)
            await session.commit()

    async def set_recommendation_state(
        self,
        comment: Optional[str],
        telegram_id: int,
        recommendation_id: UUID,
        state: str,
    ) -> None:
        async with async_session_maker() as session:
            stmt = (
                update(UserRecommendationStateModel)
                .where(
                    UserRecommendationStateModel.recommendation_id
                    == recommendation_id
                )
                .where(UserRecommendationStateModel.user_id == UserModel.id)
                .where(UserModel.telegram_id == telegram_id)
                .values(comment=comment, state=state)
            )
            await session.execute(stmt)
            await session.commit()

    async def get_not_complete_recommendations(
        self, user_id: UUID
    ):
        async with async_session_maker() as session:
            query = (
                select(UserRecommendationStateModel)
                .where(and_(
                    UserRecommendationStateModel.user_id == user_id,
                    UserRecommendationStateModel.state == "not_complete"
                ))
                .options(
                    joinedload(UserRecommendationStateModel.recommendation)
                )
            )
            result = await session.execute(query)
            return result.scalars().all()
