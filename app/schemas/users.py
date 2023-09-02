import uuid
import datetime
from typing import Optional
from fastapi_users import schemas


class UserRead(schemas.BaseUser[uuid.UUID]):
    birthdate: Optional[datetime.date]


class UserCreate(schemas.BaseUserCreate):
    birthdate: Optional[datetime.date] = None


class UserUpdate(schemas.BaseUserUpdate):
    birthdate: Optional[datetime.date]
