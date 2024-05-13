import datetime
from uuid import UUID

from db.models.recommendation import RecommendationModel
from repositories.recommendation import RecommendationRepository
from schemas.recommendation import (
    NotCompleteRecommendation,
    RecommendationWithState,
    SetState,
    UserRecommendationState,
)


class RecommendationService:
    def __init__(
        self, recommendation_repository: RecommendationRepository
    ) -> None:
        self.recommendation_repository: RecommendationRepository = (
            recommendation_repository()
        )

    async def get_first_recommendation(self) -> RecommendationModel:
        return await self.recommendation_repository.get_first()

    async def get_recommendations_with_state(
        self, telegram_id: int, page: int
    ) -> list[RecommendationWithState]:

        raw_recommendations = (
            await self.recommendation_repository.get_with_state(
                telegram_id, page
            )
        )
        recommendations = []
        for rec in raw_recommendations:
            recommendations.append(
                RecommendationWithState(
                    recommendation_text=rec.recommendation.text,
                    recommendation_number=rec.recommendation.recommendation_number,
                    state=rec.state,
                    recommendation_id=rec.recommendation.id,
                )
            )
        return recommendations

    async def start_advent(self, user_id: UUID) -> RecommendationModel:
        recommendation = await self.recommendation_repository.get_by_number(1)
        await self.recommendation_repository.add_recommendation_for_user(
            UserRecommendationState(
                comment=None,
                user_id=user_id,
                recommendation_id=recommendation.id,
                state="viewed",
            )
        )
        return recommendation

    async def set_recommendation_state(self, state: SetState) -> None:
        await self.recommendation_repository.set_recommendation_state(
            **state.model_dump()
        )

    async def get_not_complete_recommendations(self, user_id: UUID):
        raw_recommendations = await self.recommendation_repository.get_not_complete_recommendations(
            user_id
        )
        recommendations = []
        for rec in raw_recommendations:
            recommendations.append(
                NotCompleteRecommendation(
                    recommendation_text=rec.recommendation.text,
                    recommendation_number=rec.recommendation.recommendation_number,
                )
            )
        return recommendations
