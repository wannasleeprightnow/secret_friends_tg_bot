import datetime
from typing import Literal
import uuid

from sqlalchemy import BigInteger, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db import Base


class UserModel(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(), primary_key=True, default=uuid.uuid4()
    )
    telegram_id: Mapped[int] = mapped_column(BigInteger)
    name: Mapped[str]
    sex: Mapped[str]
    age: Mapped[str]
    schedule: Mapped[Literal["everyday", "work_days", "weekday"]]
    notice_time: Mapped[datetime.time]
    recommendation_number: Mapped[int]
    recommendations: Mapped[list["RecommendationModel"]] = relationship(
        back_populates="users"
    )
