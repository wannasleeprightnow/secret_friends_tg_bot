import datetime
from uuid import UUID

from db.models.user import UserModel
from db.models.recommendation import RecommendationModel
from repositories.user import UserRepository
from schemas.user import UserRegister
from utils.exceptions import UserAlreadyExists, UserNotExists


class UserService:
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository: UserRepository = user_repository()

    async def get_all_users(self) -> list[UserModel]:
        return await self.user_repository.get_all()

    async def get_user_by_telegram_id(self, telegram_id: int) -> UserModel:
        user = await self.user_repository.get_one_by_telegram_id(telegram_id)
        if user is None:
            raise UserNotExists
        return user

    async def register_user(self, user: UserRegister) -> UserModel:

        if (
            await self.user_repository.get_one_by_telegram_id(user.telegram_id)
            is not None
        ):
            raise UserAlreadyExists

        return await self.user_repository.insert_one(user.model_dump())

    async def update_profile(
        self, telegram_id: int, to_update: dict
    ) -> UserModel:
        return await self.user_repository.update_profile(
            telegram_id, to_update
        )

    async def start_advent(self, telegram_id: int) -> UserModel:
        return await self.user_repository.update_recommendation_number(
            telegram_id, 1
        )

    async def get_by_telegram_id(self, telegram_id: int) -> UserModel:
        return await self.user_repository.get_one_by_telegram_id(telegram_id)

    async def get_actual_recommendations(
        self, telegram_id: int
    ) -> list[RecommendationModel]:
        recommendations = await self.user_repository.get_user_recommendations(
            telegram_id
        )
        return sorted(
            recommendations,
            key=lambda x: x.recommendation_number,
            reverse=True,
        )[:3]

    async def get_user_with_current_notice_time(
        self, notice_time: datetime.time
    ) -> list[UUID]:
        if datetime.datetime.now().weekday() < 5:
            days_of_week = ("everyday", "work_days")
        else:
            days_of_week = ("everyday", "weekday")
        return await self.user_repository.get_user_with_current_notice_time(
            notice_time, days_of_week
        )
