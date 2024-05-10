from typing import Literal, Optional
from uuid import UUID

from pydantic import BaseModel


class FirstRecommendation(BaseModel):
    user_name: str
    recommendation_text: str
    recommendation_id: UUID


class Recommendation(BaseModel):
    text: str
    recommendation_number: int


class UserRecommendationState(BaseModel):
    comment: Optional[str]
    user_id: UUID
    recommendation_id: UUID
    state: Literal["completed", "not_complete", "deffered", "viewed"]


class RecommendationWithState(BaseModel):
    recommendation_text: str
    recommendation_number: int
    state: Literal["completed", "not_complete", "deffered", "viewed"]
    recommendation_id: UUID


class SetState(BaseModel):
    comment: Optional[str]
    telegram_id: int
    recommendation_id: UUID
    state: Literal["completed", "not_complete", "deffered", "viewed"] = (
        "viewed"
    )
