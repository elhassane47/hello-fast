from sqlalchemy.orm import Session

from app.db.models.store import Store
from app.schemas import StoreCreate, StoreUpdate
from fastapi import Depends

from sqlalchemy.orm import Session

from .base import BaseService
from ..db.session import get_async_session


class StoresService(BaseService[Store, StoreCreate, StoreUpdate]):
    def __init__(self, db_session: Session):
        super(StoresService, self).__init__(Store, db_session)


def get_stores_service(db_session: Session = Depends(get_async_session)) -> StoresService:
    return StoresService(db_session)

