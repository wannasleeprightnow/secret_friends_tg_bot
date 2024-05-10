from fastapi import APIRouter, Body, Depends

from services.user import UserService
from routers.dependencies import user_service
from schemas.user import (
    User,
    UserRegister,
    UserUpdateAge,
    UserUpdateName,
    UserUpdateSchedule,
    UserUpdateSex,
)

router = APIRouter(prefix="/user", tags=["user"])


@router.get("/{telegram_id}", response_model=User, status_code=200)
async def get_user_by_telegram_id(
    telegram_id: int, service: UserService = Depends(user_service)
):
    return await service.get_user_by_telegram_id(telegram_id)


@router.post("/register", response_model=User, status_code=201)
async def register_user(
    user: UserRegister = Body(), service: UserService = Depends(user_service)
):
    return await service.register_user(user)


@router.put("/update/name/", response_model=User, status_code=200)
async def update_name(
    to_update: UserUpdateName = Body(),
    service: UserService = Depends(user_service),
):
    return await service.update_profile(to_update)


@router.put("/update/schedule/", response_model=User, status_code=200)
async def update_schedule(
    to_update: UserUpdateSchedule = Body(),
    service: UserService = Depends(user_service),
):
    return await service.update_profile(to_update)


@router.put("/update/age/", response_model=User, status_code=200)
async def update_age(
    to_update: UserUpdateAge = Body(),
    service: UserService = Depends(user_service),
):
    return await service.update_profile(to_update)


@router.put("/update/sex/", response_model=User, status_code=200)
async def update_sex(
    to_update: UserUpdateSex = Body(),
    service: UserService = Depends(user_service),
):
    return await service.update_profile(to_update)
