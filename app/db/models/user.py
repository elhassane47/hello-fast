from app.db.models.base import Base
from app.db.session import get_async_session
from fastapi import Depends
from fastapi_users.db import (
    SQLAlchemyBaseOAuthAccountTableUUID,
    SQLAlchemyBaseUserTableUUID,
    SQLAlchemyUserDatabase,
)

from sqlalchemy import Column, Date

from sqlalchemy.ext.asyncio import AsyncSession


class User(SQLAlchemyBaseUserTableUUID, Base):
    birthdate = Column(Date, nullable=True, index=True)


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)