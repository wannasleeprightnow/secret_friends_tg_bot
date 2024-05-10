from typing import Literal, Optional
import uuid

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.db import Base


class UserRecommendationStateModel(Base):
    __tablename__ = "associations"

    comment: Mapped[Optional[str]]
    user_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"), primary_key=True
    )
    recommendation_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("recommendations.id", ondelete="CASCADE"), primary_key=True
    )
    state: Mapped[Literal["completed", "not_complete", "deffered", "viewed"]]
    recommendation: Mapped["RecommendationModel"] = relationship(
        foreign_keys=[recommendation_id],
        order_by="RecommendationModel.recommendation_number.desc()",
    )
