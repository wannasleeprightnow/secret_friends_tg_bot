import datetime
from typing import Literal, Optional
from uuid import UUID

from pydantic import BaseModel


class User(BaseModel):
    id: UUID
    telegram_id: int
    name: str
    sex: Optional[str]
    age: str
    schedule: Literal["everyday", "work_days", "weekday"]
    notice_time: datetime.time


class UserRegister(BaseModel):
    telegram_id: int
    name: str
    sex: Optional[str]
    age: str
    schedule: Literal["everyday", "work_days", "weekday"]
    notice_time: datetime.time


class UserUpdateName(BaseModel):
    telegram_id: int
    name: str


class UserUpdateSchedule(BaseModel):
    telegram_id: int
    schedule: Literal["everyday", "work_days", "weekday"]


class UserUpdateAge(BaseModel):
    telegram_id: int
    age: str


class UserUpdateSex(BaseModel):
    telegram_id: int
    sex: Optional[str]


class UserUpdateNoticeTime(BaseModel):
    telegram_id: int
    notice_time: datetime.time
