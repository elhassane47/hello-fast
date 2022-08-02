from fastapi import Depends

from app.db import get_session
from app.serivces.stores import StoresService
from sqlalchemy.orm import Session


def get_stores_service(db_session: Session = Depends(get_session)) -> StoresService:
    return StoresService(db_session)

