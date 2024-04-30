from typing import Optional

from sqlalchemy import select, update

from db.db import async_session_maker
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
