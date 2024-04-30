from repositories.recommendation import RecommendationRepository
from repositories.user import UserRepository
from services.recommendation import RecommendationService
from services.user import UserService


def recommendation_service():
    return RecommendationService(RecommendationRepository)


def user_service():
    return UserService(UserRepository)
