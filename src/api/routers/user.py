import datetime
from uuid import UUID

from fastapi import APIRouter, Body, Depends

from services.user import UserService
from routers.dependencies import user_service
from schemas.user import (
    User,
    UserRegister,
    UserUpdateAge,
    UserUpdateName,
    UserUpdateNoticeTime,
    UserUpdateSchedule,
    UserUpdateSex,
)

router = APIRouter(prefix="/user", tags=["user"])


@router.get("/{telegram_id}", response_model=User, status_code=200)
async def get_user_by_telegram_id(
    telegram_id: int, service: UserService = Depends(user_service)
):
    return await service.get_user_by_telegram_id(telegram_id)


@router.post("", response_model=User, status_code=201)
async def register_user(
    user: UserRegister = Body(), service: UserService = Depends(user_service)
):
    return await service.register_user(user)


@router.patch("/{telegram_id}/name/", response_model=User, status_code=200)
async def update_name(
    telegram_id: int,
    name: UserUpdateName = Body(),
    service: UserService = Depends(user_service),
):
    return await service.update_profile(telegram_id, name.model_dump())


@router.patch("/{telegram_id}/schedule/", response_model=User, status_code=200)
async def update_schedule(
    telegram_id: int,
    schedule: UserUpdateSchedule = Body(),
    service: UserService = Depends(user_service),
):
    return await service.update_profile(telegram_id, schedule.model_dump())


@router.patch(
    "/{telegram_id}/notice_time/", response_model=User, status_code=200
)
async def update_notice_time(
    telegram_id: int,
    notice_time: UserUpdateNoticeTime = Body(),
    service: UserService = Depends(user_service),
):
    return await service.update_profile(telegram_id, notice_time.model_dump())


@router.patch("/{telegram_id}/age/", response_model=User, status_code=200)
async def update_age(
    telegram_id: int,
    age: UserUpdateAge = Body(),
    service: UserService = Depends(user_service),
):
    return await service.update_profile(telegram_id, age.model_dump())


@router.patch("/{telegram_id}/sex/", response_model=User, status_code=200)
async def update_sex(
    telegram_id: int,
    sex: UserUpdateSex = Body(),
    service: UserService = Depends(user_service),
):
    return await service.update_profile(telegram_id, sex)


@router.get(
    "/notice_time/{notice_time}",
    response_model=list[UUID],
    status_code=200)
async def get_user_with_current_notice_time(
    notice_time: datetime.time,
    service: UserService = Depends(user_service)
):
    return await service.get_user_with_current_notice_time(notice_time)
