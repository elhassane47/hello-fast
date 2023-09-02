import uuid
import datetime
from typing import Optional
from fastapi_users import schemas

from app.db.models import GenderEnum


class UserRead(schemas.BaseUser[uuid.UUID]):
    birthdate: Optional[datetime.date] = None
    mobile_number: Optional[str] = None
    city_id: Optional[int] = None
    gender: Optional[GenderEnum] = None


class UserCreate(schemas.BaseUserCreate):
    birthdate: Optional[datetime.date] = None
    mobile_number: Optional[str] = None
    city_id: Optional[int] = None
    gender: Optional[GenderEnum] = None


class UserUpdate(schemas.BaseUserUpdate):
    birthdate: Optional[datetime.date] = None
    mobile_number: Optional[str] = None
    city_id: Optional[int] = None
    gender: Optional[GenderEnum] = None

