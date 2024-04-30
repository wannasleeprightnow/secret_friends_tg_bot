from fastapi import APIRouter, Depends


router = APIRouter(prefix="/recommendation", tags="recommendation")


async def start_advent(): ...


async def get_actual_recommendations(): ...


# пагинация
async def get_all_recommendations(): ...


async def get_all_not_completed_recommendations(): ...


async def get_one_recommendation(): ...


async def mark_as_complete(): ...


async def mark_as_not_complete(): ...


async def mark_as_deferred_with_comment(): ...
