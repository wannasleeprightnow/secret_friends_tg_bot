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
    recommendation_number: int


class UserRegister(BaseModel):
    telegram_id: int
    name: str
    sex: Optional[str]
    age: str
    schedule: Literal["everyday", "work_days", "weekday"]
    notice_time: datetime.time
    recommendation_number: int = 0


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
