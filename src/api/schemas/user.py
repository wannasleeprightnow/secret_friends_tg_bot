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
    name: str


class UserUpdateSchedule(BaseModel):
    schedule: Literal["everyday", "work_days", "weekday"]


class UserUpdateAge(BaseModel):
    age: str


class UserUpdateSex(BaseModel):
    sex: Optional[str]


class UserUpdateNoticeTime(BaseModel):
    notice_time: datetime.time
