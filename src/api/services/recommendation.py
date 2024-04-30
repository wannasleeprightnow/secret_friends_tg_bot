from db.models.recommendation import RecommendationModel
from repositories.recommendation import RecommendationRepository


class RecommendationService:
    def __init__(
        self, recommendation_repository: RecommendationRepository
    ) -> None:
        self.recommendation_repository: RecommendationModel = (
            recommendation_repository()
        )
