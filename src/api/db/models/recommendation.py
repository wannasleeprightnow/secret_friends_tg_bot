import uuid

from sqlalchemy import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.db import Base


class RecommendationModel(Base):
    __tablename__ = "recommendations"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(), primary_key=True, default=uuid.uuid4()
    )
    text: Mapped[str]
    recommendation_number: Mapped[int]
    # users: Mapped[list["UserModel"]] = relationship(
    #     back_populates="recommendation"
    # )
