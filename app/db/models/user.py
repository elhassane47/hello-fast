from app.db.models.base import Base
from app.db.session import get_async_session
from fastapi import Depends
from fastapi_users.db import (
    SQLAlchemyBaseOAuthAccountTableUUID,
    SQLAlchemyBaseUserTableUUID,
    SQLAlchemyUserDatabase,
)
from enum import Enum as Penum
from sqlalchemy import Column, Date, Enum, String, ForeignKey, Integer

from sqlalchemy.ext.asyncio import AsyncSession

from sqlalchemy.orm import relationship


class GenderEnum(Penum):
    MALE = "M"
    FEMALE = "F"


class City(Base):
    __tablename__ = 'city'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    users = relationship("User", back_populates="city")

    def __str__(self):
        return self.name


class User(SQLAlchemyBaseUserTableUUID, Base):
    birthdate = Column(Date, nullable=True, index=True)
    gender = Column(Enum(GenderEnum), nullable=True,)
    mobile_number = Column(String(15), nullable=True)
    city_id = Column(Integer, ForeignKey('city.id'), nullable=True)  # Reference 'city.id'
    city = relationship("City", back_populates="users")


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)
