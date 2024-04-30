from db.models.user import UserModel
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
            await self.user_repository.get_one_by_telegram_id(user.t)
            is not None
        ):
            raise UserAlreadyExists

        return await self.user_repository.insert_one(user.model_dump())

    async def update_profile(self, to_update) -> UserModel:
        to_update = to_update.model_dump()
        telegram_id = to_update["telegram_id"]
        del to_update["telegram_id"]
        return await self.user_repository.update_profile(
            telegram_id, to_update
        )
