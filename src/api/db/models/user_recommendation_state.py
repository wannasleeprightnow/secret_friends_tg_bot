from datetime import datetime
from typing import Optional
import uuid

from sqlalchemy import ForeignKey, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db import Base


class UserRecommendationStateModel(Base):
    __tablename__ = "associations"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(), primary_key=True, default=uuid.uuid4()
    )
    user_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE")
    )
    recommendation_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        ForeignKey("recommendations.id", ondelete="CASCADE")
    )
    state_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        ForeignKey("states.id", ondelete="CASCADE")
    )
    user: Mapped["UserModel"] = relationship(
        back_populates="recommendations", foreign_keys=[user_id]
    )
    recommendation: Mapped["RecommendationModel"] = relationship(
        back_populates="users", foreign_keys=[recommendation_id]
    )
    state: Mapped["StateModel"] = relationship(foreign_keys=[state_id])
