from fastapi import APIRouter

from routers.recommendation import router as recommendation_router
from routers.user import router as user_router
from settings import Settings

all_routers = [recommendation_router, user_router]

apiv1 = APIRouter(prefix=Settings.api_prefix)

for router in all_routers:
    apiv1.include_router(router)
