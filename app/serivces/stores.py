from sqlalchemy.orm import Session

from app.db.models import Store
from app.db.schemas import StoreCreate, StoreUpdate

from .base import BaseService


class StoresService(BaseService[Store, StoreCreate, StoreUpdate]):
    def __init__(self, db_session: Session):
        super(StoresService, self).__init__(Store, db_session)