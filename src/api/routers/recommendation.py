from uuid import UUID

from fastapi import APIRouter, Body, Depends, Query

from routers.dependencies import recommendation_service, user_service
from schemas.recommendation import (
    FirstRecommendation,
    NotCompleteRecommendation,
    Recommendation,
    RecommendationWithState,
    SetState,
)
from services.recommendation import RecommendationService
from services.user import UserService

router = APIRouter(prefix="/recommendation", tags=["recommendation"])


@router.post(
    "/start_advent/{telegram_id}",
    response_model=FirstRecommendation,
    status_code=200,
)
async def start_advent(
    telegram_id: int,
    recommendation_service: RecommendationService = Depends(
        recommendation_service
    ),
    user_service: UserService = Depends(user_service),
):
    user = await user_service.get_by_telegram_id(telegram_id)
    recommendation = await recommendation_service.start_advent(user.id)
    return FirstRecommendation(
        user_name=user.name,
        recommendation_text=recommendation.text,
        recommendation_id=recommendation.id,
    )


@router.get(
    "/actual/{telegram_id}",
    response_model=list[Recommendation],
    status_code=200,
)
async def get_actual_recommendations(
    telegram_id: int, user_service: UserService = Depends(user_service)
):
    return await user_service.get_actual_recommendations(telegram_id)


@router.get(
    "/with_state/{telegram_id}",
    response_model=list[RecommendationWithState],
    status_code=200,
)
async def get_recommendation_with_state(
    telegram_id: int,
    page: int = Query(1),
    recommendation_service: RecommendationService = Depends(
        recommendation_service
    ),
):
    return await recommendation_service.get_recommendations_with_state(
        telegram_id, page
    )


@router.patch("/set_state", status_code=204)
async def set_state(
    state: SetState = Body(),
    recommendation_service: RecommendationService = Depends(
        recommendation_service
    ),
):
    await recommendation_service.set_recommendation_state(state)


@router.get(
    "/not_complete/{user_id}",
    response_model=list[NotCompleteRecommendation],
    status_code=200,
)
async def get_not_complete(
    user_id: UUID,
    recommendation_service: RecommendationService = Depends(
        recommendation_service
    ),
):
    return await recommendation_service.get_not_complete_recommendations(
        user_id
    )
