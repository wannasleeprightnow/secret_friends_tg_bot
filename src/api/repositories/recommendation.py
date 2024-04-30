from db.models.recommendation import RecommendationModel
from utils.repository import Repository


class RecommendationRepository(Repository):
    model = RecommendationModel
